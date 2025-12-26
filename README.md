# local-AI-agent-using-langchain-Ollama
Built a local Retrieval-Augmented Generation (RAG) system using LangChain, Ollama, and ChromaDB to answer questions from restaurant reviews. Implemented semantic search over customer feedback using vector embeddings and similarity retrieval. Enabled grounded, review-based responses through prompt engineering and a local large language model.

---

This project is a local Retrieval Augmented Generation system built using LangChain, Ollama, and ChromaDB to answer user questions based strictly on real restaurant reviews. The goal was to move beyond generic large language model responses and instead ground answers in actual customer feedback stored in a vector database.

At the beginning of the project, restaurant reviews were loaded from a CSV file and converted into LangChain Document objects. Each review was embedded using Ollama’s mxbai embedding model and stored in a persistent Chroma vector database. This allowed the system to perform semantic similarity search instead of relying on keyword matching, making the retrieval process more accurate and context aware.

When a user asks a question, the system does not directly send the question to the language model. Instead, the question is first converted into an embedding and used to retrieve the most relevant reviews from the vector database. This retrieval step ensures that only the most contextually related reviews are selected for answering the query.

Initially, the retrieved results were passed directly as Document objects to the language model, which led to generic or weakly grounded answers. To fix this, the retrieved documents were explicitly converted into plain text before being sent to the model. This change was necessary because large language models operate on text, not structured Python objects. By converting everything into clean review text, the model could clearly see and reason over the actual customer feedback.

The prompt was also refined to strictly instruct the model to use only the provided reviews and to respond with uncertainty if sufficient information was not available. This step is what enforces true grounding and prevents hallucinations. The language model is no longer answering from its general knowledge but is instead constrained by retrieved data.

This architecture qualifies as Retrieval Augmented Generation because the generation step is augmented by a retrieval step. The language model is not working in isolation. It depends on an external knowledge source, retrieves relevant information at runtime, and then generates answers based on that retrieved context. LangChain acts as the orchestration layer that connects retrieval, prompting, and generation into a single pipeline.

Overall, this project demonstrates a practical implementation of a local RAG system that improves answer accuracy, transparency, and reliability by grounding responses in real data. It reflects how modern AI applications are built in production settings where factual consistency and traceability are critical.
