import psycopg2
from pgvector.psycopg2 import register_vector


class PgClient:
    def __init__(self, pg_host: str, pg_user: str, pg_password: str, pg_db: str):
        self.pg_host = pg_host
        self.pg_user = pg_user
        self.pg_password = pg_password
        self.pg_db = pg_db

    def _make_conn(self):
        try:
            conn = psycopg2.connect(
                host=self.pg_host,
                user=self.pg_user,
                password=self.pg_password,
                dbname=self.pg_db,
            )
            register_vector(conn)
            return conn
        except Exception as e:
            print(f"Error connecting to Postgres: {str(e)}")
            return None

    def insert_content_embeddings(self, content_embeddings: list):
        try:
            conn = self._make_conn()
            cursor = conn.cursor()
            for record in content_embeddings:
                try:
                    cursor.execute(
                        """
                                INSERT INTO content_embeddings(document_id, chunk_id, tags, clean_text, embedding)
                                    VALUES(%s, %s, %s, %s, %s);
                            """,
                        (
                            record["document_id"],
                            record["chunk_id"],
                            record["tags"],
                            record["clean_text"],
                            record["embedding"],
                        ),
                    )
                except Exception as e:
                    print(f"Error inserting record: {str(e)}")
            conn.commit()
            cursor.close()
            conn.close()
        except Exception as e:
            print(f"Error connecting to Postgres: {str(e)}")

    def semantic_search(self, query_embedding: list, table: str, n_results: int = 5):
        # convert query embedidng to the proper format
        query_embedding_str = ", ".join(map(str, query_embedding))

        # build query
        search = f"SELECT document_id, chunk_id, tags, clean_text FROM {table} ORDER BY embedding <=> '[{query_embedding_str}]' LIMIT {n_results};"

        # establish a connection to the DB
        conn = self._make_conn()
        try:
            cursor = conn.cursor()
            cursor.execute(search)
            results = cursor.fetchall()
            return results
        except Exception as e:
            print(f"Error conduting semantic search: {str(e)}")
            return None
        finally:
            cursor.close()

    def lexical_search(self, query: str, table: str, n_results: int = 5):
        search = f"SELECT document_id, chunk_id, tags, clean_text FROM {table} WHERE search_terms @@ phraseto_tsquery('english', '{query}');"
        conn = self._make_conn()
        try:
            cursor = conn.cursor()
            cursor.execute(search)
            results = cursor.fetchall()
            return results
        except Exception as e:
            print(f"Error conduting semantic search: {str(e)}")
            return None
        finally:
            cursor.close()
