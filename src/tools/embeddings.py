from sentence_transformers import SentenceTransformer
from functools import lru_cache
from src.app.settings import settings

@lru_cache(maxsize=1)
def get_embedder():
    return SentenceTransformer(settings.EMBED_MODEL)

