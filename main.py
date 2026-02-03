from memory_store import (
    write_memory,
    read_memory,
    forget_memories,
    promote_to_long_term
)

# Create memories
write_memory("User likes deep learning projects")
write_memory("User is working on agent memory systems")
write_memory("Temporary task note")

# Read memory
result = read_memory("What does the user like?")
print("Retrieved Memory:", result)

# Promote important memories
promote_to_long_term()

# Forget low-importance memories
forget_memories()
