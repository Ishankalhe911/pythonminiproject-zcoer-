
# Voice AI Async Demo

> **Status:** 🚧 **Work in Progress / Proof of Concept**

This repository demonstrates the foundational **asynchronous architecture** and **basic API logic** for our Voice AI system.

## 🎯 Current Progress

This build focuses on demonstrating the split-workflow logic to handle high-concurrency environments efficiently:

### 1. Asynchronous Workflow

We have implemented the "Record now, Answer later" logic:

* **Inbound Flow:** The AI greets the user, records their query, and immediately terminates the call to release resources.
* **Async Processing:** The system processes the audio in the background (Speech-to-Text  Knowledge Base  Text-to-Speech).
* **Outbound Flow:** Once the answer is ready, the system automatically initiates a **callback** to deliver the response.

### 2. Basic API Integration

The core backend logic is currently functional for the demo:

* Telephony gateway routing.
* Audio recording and storage.
* Triggering the logic chain for answer generation.

---

## 🔮 Under Production

This project is currently under active development. The following features are in the pipeline:

* Real-time latency optimization (reducing the callback gap).
* Full conversational context retention.
* Advanced error handling for failed callbacks.
