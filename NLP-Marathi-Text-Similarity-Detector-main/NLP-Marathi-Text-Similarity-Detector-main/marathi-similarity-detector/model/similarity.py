from sentence_transformers import SentenceTransformer, util

# Load pre-trained model (You can switch to any other multilingual model)
model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

def calculate_similarity(text1, text2):
    # Encode the Marathi sentences
    embeddings = model.encode([text1, text2])
    
    # Calculate cosine similarity
    similarity_score = util.pytorch_cos_sim(embeddings[0], embeddings[1]).item()

    return round(similarity_score, 3)  # Round to 3 decimal places
