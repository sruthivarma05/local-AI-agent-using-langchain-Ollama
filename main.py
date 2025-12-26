from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever 

model = OllamaLLM(model="llama3.2")

# UPGRADE: stricter grounding
template = """
You are an expert in answering questions about a pizza restaurant.

Use ONLY the information from the reviews below.
If the answer is not found in the reviews, say:
"I don't have enough review data to answer that."

Reviews:
{reviews}

Question:
{question}
"""

promt = ChatPromptTemplate.from_template(template)
chain = promt | model

while True:
    print("\n\n--------------------------------")
    question = input("Ask your question (q to quit): ")
    print("\n\n")
    if question == "q":
        break 

    reviews = retriever.invoke(question)

    # UPGRADE: convert Document objects → clean text
    reviews_text = "\n\n".join(
        doc.page_content for doc in reviews
    )

    result = chain.invoke({
        "reviews": reviews_text,
        "question": question
    })

    print(result)
