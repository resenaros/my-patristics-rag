from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model = OllamaLLM(model="phi3:mini")

template= """
You are a helpful assistant that answers questions about the early church fathers.
Here is the relevant information: {information} 
Here is the question to answer: {question}
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

while True:
    print("\n\n------------------------------")
    question =  input("Ask a question about the early church fathers (or type 'q' to quit):\n")
    print("\n\n------------------------------")
    if question.lower() == 'q':
        break
    
    information = retriever.invoke(question)
    result = chain.invoke({"information": information, "question": question})
    print("\nAnswer:\n\n", result)
    
    print("\nReferences:")
    
    if isinstance(information, list):
        seen = set()
        for doc in information:
            src = doc.metadata.get("source")
            author = doc.metadata.get("author")
            if src and src not in seen:
                print(f"- {src}" + (f" by {author}" if author else ""))
                seen.add(src)
    elif hasattr(information, "metadata"):
       src = information.metadata.get("source")
       author = information.metadata.get("author")
       print(f"- {src}" + (f" by {author}" if author else ""))
    else:
        print("- No sources found") 

