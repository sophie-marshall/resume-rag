insert_content_embeddings = """
    INSERT INTO content_embeddings(document_id, chunk_id, tags, clean_text, embedding)
        VALUES(%s, %s, %s, %s, %s);
"""
