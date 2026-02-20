from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

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
    question =  input("Ask a question about the early church fathers (or type 'q' to quit): ")
    print("\n\n------------------------------")
    if question.lower() == 'q':
        break
    result = chain.invoke({"information": [], "question": question})
    print(result)
# def main():
#     print("Hello from local-ai-agent-rag!")


# if __name__ == "__main__":
#     main()
