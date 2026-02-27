# app.py entry point for the RAG agent application
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever
import gradio as gr

model = OllamaLLM(model="phi3:mini")

template = """
You are a helpful assistant that answers questions about the early church fathers.
Please answer concisely, using no more than 2-3 sentences, and only include the most essential information.
Here is the relevant information: {information} 
Here is the question to answer: {question}
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def rag_agent(question):
    information = retriever.invoke(question)
    result = chain.invoke({"information": information, "question": question})
    
    refs = []
    if isinstance(information, list):
        seen = set()
        for doc in information:
            src = doc.metadata.get("source")
            author = doc.metadata.get("author")
            if src and src not in seen:
                refs.append(f"- {src}" + (f" by {author}" if author else ""))
                seen.add(src)
    elif hasattr(information, "metadata"):
        src = information.metadata.get("source")
        author = information.metadata.get("author")
        refs.append(f"- {src}" + (f" by {author}" if author else ""))
    else:
        refs.append("- No sources found")
    return result, "\n".join(refs)

with gr.Blocks(title="Church Fathers RAG Assistant", theme=gr.themes.Glass()) as demo:
    gr.Markdown("Ask anything about the early church fathers and get a concise answer from a local RAG agent.")
    with gr.Row():
        question = gr.Textbox(lines=2, label="Ask a question about the early church fathers")
        with gr.Column():
            answer = gr.Textbox(label="Answer")
            refs = gr.Textbox(label="References")
    question.submit(rag_agent, question, [answer, refs])

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)