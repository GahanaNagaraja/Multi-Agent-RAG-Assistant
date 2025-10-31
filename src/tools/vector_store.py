import os, glob
from chromadb.utils import embedding_functions
import chromadb
from src.app.settings import settings
from src.tools.embeddings import get_embedder

def _read_docs():
    paths = sorted(glob.glob(os.path.join(settings.DOC_DIR, "*.*")))
    docs, metadatas, ids = [], [], []
    for i, p in enumerate(paths):
        with open(p, "r", encoding="utf-8", errors="ignore") as f:
            txt = f.read()
        docs.append(txt)
        metadatas.append({"path": p})
        ids.append(f"doc-{i}")
    return docs, metadatas, ids

def build_or_load_collection():
    os.makedirs(settings.VECTOR_DIR, exist_ok=True)
    client = chromadb.PersistentClient(path=settings.VECTOR_DIR)

    # use custom embedding fn (SentenceTransformers)
    embedder = get_embedder()
    def emb_fn(texts): return embedder.encode(texts, normalize_embeddings=True).tolist()
    ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=settings.EMBED_MODEL)

    name = "docs"
    try:
        col = client.get_collection(name)
    except:
        col = client.create_collection(name, embedding_function=ef)
        docs, metas, ids = _read_docs()
        if docs:
            col.add(documents=docs, metadatas=metas, ids=ids)
    return col

def retrieve(query: str, k: int = None):
    col = build_or_load_collection()
    k = k or settings.TOP_K
    res = col.query(query_texts=[query], n_results=k)
    out = []
    for doc, meta in zip(res["documents"][0], res["metadatas"][0]):
        out.append({"text": doc, "meta": meta})
    return out

