import torch
from transformers import AutoProcessor, AutoModelForImageTextToText
import time
import os
from datetime import datetime

# --- MODEL LOADING ---
MODEL_ID = "Qwen/Qwen3.5-0.8B"
print(f"Loading {MODEL_ID}... This may take a moment.")

processor = AutoProcessor.from_pretrained(MODEL_ID)
model = AutoModelForImageTextToText.from_pretrained(
    MODEL_ID,
    device_map="auto",
    torch_dtype="auto",
    trust_remote_code=True
).eval()

# --- FILE PATHS ---
SAVE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "prompts_and_responses.md")

def ask_model(prompt_text: str) -> tuple:
    """Uses the transformers model to generate a response."""
    start = time.time()
   
    # Simple text-based message structure for the evaluation tool
    messages = [
        {
            "role": "user",
            "content": [{"type": "text", "text": prompt_text}]
        },
    ]
   
    inputs = processor.apply_chat_template(
        messages,
        add_generation_prompt=True,
        tokenize=True,
        return_dict=True,
        return_tensors="pt",
    ).to(model.device)

    generated_ids = model.generate(**inputs, max_new_tokens=512)
   
    # Decode only the new tokens (the response)
    response = processor.decode(generated_ids[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True).strip()
   
    elapsed = round(time.time() - start, 2)
    return response, elapsed

def save_to_markdown(entries: list):
    grouped = {}
    for entry in entries:
        cat = entry["category"]
        grouped.setdefault(cat, []).append(entry)

    with open(SAVE_PATH, "w", encoding="utf-8") as f:
        f.write(f"# Prompt Evaluation — {MODEL_ID}\n\n")
        f.write(f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n---\n\n")

        for category, cat_entries in grouped.items():
            f.write(f"# {category}\n\n")
            for i, entry in enumerate(cat_entries, 1):
                f.write(f"## Prompt {i}\n\n**Prompt:** {entry['prompt']}\n\n")
                f.write(f"**Response:**\n{entry['response']}\n\n")
                f.write(f"**Response Time:** {entry['time']}s\n\n")
                f.write(f"**Notes:** {entry['notes']}\n\n---\n\n")
    print(f"✅ Saved to {os.path.abspath(SAVE_PATH)}")

# --- CLI TOOL LOGIC ---
CATEGORIES = ["Coding", "General Knowledge", "Reasoning", "Visual Question Answering"]
entries = []

print("\n" + "="*40)
print(" Qwen 3.5 Evaluation Tool (Transformers)")
print("="*40)

# Select Category
for i, cat in enumerate(CATEGORIES, 1):
    print(f"{i}. {cat}")
choice = input("\nSelect category number: ")
current_category = CATEGORIES[int(choice)-1] if choice.isdigit() and 0 < int(choice) <= len(CATEGORIES) else CATEGORIES[0]

while True:
    prompt = input(f"\n[{current_category}] Your prompt (or /save, /quit): ").strip()

    if prompt == "/quit": break
    if prompt == "/save":
        save_to_markdown(entries)
        break
    if not prompt: continue

    print("⏳ Model is thinking...")
    response, elapsed = ask_model(prompt)
   
    print(f"\nMODEL: {response}")
    print(f"TIME: {elapsed}s")
   
    note = input("Add a note (Enter to skip): ")
    entries.append({
        "category": current_category,
        "prompt": prompt,
        "response": response,
        "time": elapsed,
        "notes": note if note else "N/A"
    })
   
    # Auto-save after every prompt just in case
    save_to_markdown(entries)
