# Step 1: Create a small document collection

documents = [
    "Machine learning enables computers to learn from data without being explicitly programmed.",
    "Cooking requires a balance of ingredients, timing, and temperature control.",
    "Space exploration helps us understand planets, stars, and the universe.",
    "Programming involves writing instructions for computers using languages like Python.",
    "Sports improve physical fitness and promote teamwork and discipline."
]

from sentence_transformers import SentenceTransformer

# Load the embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Generate embeddings for all documents
document_embeddings = model.encode(documents)

# Print to verify
print("Number of documents:", len(documents))
print("Embedding shape:", document_embeddings.shape)

# Step 3: Encode the user query

query = "What does a chef need?"

# Convert query into embedding
query_embedding = model.encode(query)

# Verify
print("Query:", query)
print("Query embedding shape:", query_embedding.shape)

from sklearn.metrics.pairwise import cosine_similarity

# cosine_similarity expects 2D arrays
# So reshape query embedding
query_embedding_2d = query_embedding.reshape(1, -1)

# Compute similarity scores
similarity_scores = cosine_similarity(query_embedding_2d, document_embeddings)

# Flatten to make it easier to read
similarity_scores = similarity_scores.flatten()

# Print scores
for i, score in enumerate(similarity_scores):
    print(f"Document {i+1} similarity: {score:.4f}")

import numpy as np

# Find index of highest similarity score
most_similar_index = np.argmax(similarity_scores)

# Retrieve the most relevant document
most_relevant_document = documents[most_similar_index]

# Print result
print("Query:", query)
print("Most relevant document:")
print(most_relevant_document)

