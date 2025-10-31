from pydantic import BaseSettings

class Settings(BaseSettings):
    DOC_DIR: str = "data/docs"
    TABLE_DIR: str = "data/tables"
    VECTOR_DIR: str = "data/.chroma"
    EMBED_MODEL: str = "sentence-transformers/all-MiniLM-L6-v2"
    TOP_K: int = 5

settings = Settings()

