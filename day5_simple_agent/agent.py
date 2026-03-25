import google.generativeai as genai
import os
import re
from dotenv import load_dotenv
from tools import calculator


load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))



model = genai.GenerativeModel("gemini-2.5-flash")




def decide_tool(query: str):
    
    prompt = f"""
You are an AI agent.

User question: {query}

Available tools:
- calculator → performs mathematical calculations

If the question requires math, respond EXACTLY with:
TOOL: calculator

Otherwise respond EXACTLY with:
TOOL: none
"""

    response = model.generate_content(prompt)
    return response.text.strip()



def generate_final_answer(query: str, tool_result: str):
    
    prompt = f"""
User question:
{query}

Tool result:
{tool_result}

Write a helpful response.
"""

    response = model.generate_content(prompt)
    return response.text.strip()



def execute_tool(query: str, decision: str):
    
    if "TOOL: calculator" in decision:
        
        # Extract math expression from query
        expression = re.findall(r"[0-9+\-*/().%]+", query)
        expression = "".join(expression)
        
        print("Tool used: calculator")
        
        # Run calculator
        result = calculator(expression)
        
        # Generate final answer
        final_answer = generate_final_answer(query, result)
        
        print("Answer:")
        print(final_answer)
        
    else:
        # Direct answer
        response = model.generate_content(query)
        
        print("Answer:")
        print(response.text.strip())



def agent():
    
    query = input("Ask something: ")
    
    decision = decide_tool(query)
    
    print("\nAgent decision:", decision)
    
    execute_tool(query, decision)



if __name__ == "__main__":
    agent()