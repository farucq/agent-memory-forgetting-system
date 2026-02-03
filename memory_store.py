import time
import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer

from config import CHROMA_DIR
from logger import log_event
from memory_scoring import calculate_memory_score

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

chroma_client = chromadb.Client(
    Settings(
        persist_directory=CHROMA_DIR,
        anonymized_telemetry=False
    )
)

memory_collection = chroma_client.get_or_create_collection(
    name="agent_memory"
)

FORGET_THRESHOLD = 0.3


def write_memory(text, memory_type="short_term"):
    embedding = embedding_model.encode(text).tolist()
    memory_id = f"mem_{int(time.time() * 1000)}"

    metadata = {
        "memory_type": memory_type,
        "access_count": 0,
        "last_accessed": time.time()
    }

    memory_collection.add(
        documents=[text],
        embeddings=[embedding],
        metadatas=[metadata],
        ids=[memory_id]
    )

    log_event("write_memory", {"id": memory_id, "text": text})
    return memory_id


def read_memory(query, top_k=1):
    query_embedding = embedding_model.encode(query).tolist()

    results = memory_collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    if not results["documents"]:
        return None

    memory_id = results["ids"][0][0]
    metadata = results["metadatas"][0][0]

    metadata["access_count"] += 1
    metadata["last_accessed"] = time.time()

    memory_collection.update(
        ids=[memory_id],
        metadatas=[metadata]
    )

    log_event("read_memory", {"id": memory_id, "query": query})
    return results["documents"][0][0]


def forget_memories():
    all_data = memory_collection.get(include=["metadatas", "documents", "ids"])

    for mem_id, metadata in zip(all_data["ids"], all_data["metadatas"]):
        score = calculate_memory_score(metadata)
        if score < FORGET_THRESHOLD:
            memory_collection.delete(ids=[mem_id])
            log_event("forgot_memory", {"id": mem_id, "score": score})


def promote_to_long_term(threshold=2):
    all_data = memory_collection.get(include=["metadatas", "ids"])

    for mem_id, metadata in zip(all_data["ids"], all_data["metadatas"]):
        if metadata["access_count"] >= threshold:
            metadata["memory_type"] = "long_term"
            memory_collection.update(
                ids=[mem_id],
                metadatas=[metadata]
            )
            log_event("promoted_memory", {"id": mem_id})
