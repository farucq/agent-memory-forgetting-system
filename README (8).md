# Agent Memory & Forgetting System

This project implements an autonomous **agent memory lifecycle system** that can store, retrieve, promote, and manage memories over time.

The system demonstrates how an agent decides **what to remember**, **what to retain long-term**, and **when to promote information** based on usage.

---

## Key Features

- **Short-Term Memory (STM)**  
  Temporary, task-specific memories created during each run.

- **Long-Term Memory (LTM)**  
  Frequently accessed memories are automatically promoted and persist across executions.

- **Vector-Based Retrieval**  
  Memories are embedded and retrieved using semantic similarity.

- **Autonomous Promotion Logic**  
  Memories are promoted from STM to LTM based on access frequency (no manual intervention).

- **Persistent Memory Store**  
  Memories created in earlier runs can be retrieved and promoted in later runs.

---

## Memory Lifecycle Events

The system logs all memory actions in JSON format:

- `MEMORY_CREATED` – A new memory is stored  
- `MEMORY_RETRIEVED` – A memory is accessed based on relevance  
- `MEMORY_PROMOTED` – A memory is promoted to long-term storage  

These logs demonstrate realistic agent behavior across multiple executions.

---

## Notes

- Memory promotion is **usage-based**, not automatic  
- Different runs may promote different memories  
- This behavior is intentional and reflects real agent memory dynamics

---

## Execution

Run the notebook cells sequentially in Google Colab.  
Logs are generated automatically during execution.
