import time

def calculate_recency_score(last_accessed):
    elapsed = time.time() - last_accessed
    return max(0, 1 - (elapsed / 3600))  # decays over 1 hour

def calculate_frequency_score(access_count):
    return min(1, access_count / 10)

def calculate_memory_score(metadata):
    recency = calculate_recency_score(metadata["last_accessed"])
    frequency = calculate_frequency_score(metadata["access_count"])
    return (recency + frequency) / 2
