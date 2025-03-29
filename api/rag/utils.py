from sentence_transformers import SentenceTransformer

EMBEDDING_MODEL = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def embed_clean_text(clean_text: str): 
    # generate content embeddings for each chunk of split text
    return EMBEDDING_MODEL.encode(clean_text)