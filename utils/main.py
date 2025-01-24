from utils.pdf_util import read_pdf_from_url
from utils.embedding_util import EmbeddingUtility
from utils.milvus_util import MilvusUtility
from llm.prompt_util import PromptUtility
from llm.chat_util import ChatUtility

def main():
    # Initialize utilities
    embed_util = EmbeddingUtility()
    milvus_util = MilvusUtility(dimension=embed_util.get_embedding_dimension())
    chat_util = ChatUtility()

    # Setup Milvus collection
    milvus_util.setup_collection()

    # Example PDF links
    pdf_links = ["https://example.com/nutrition-document.pdf"]
    pdf_texts = [read_pdf_from_url(link) for link in pdf_links if read_pdf_from_url(link)]

    # Generate embeddings and insert into Milvus
    data = [{"id": i, "vector": embed_util.generate_embedding(text), "text": text} for i, text in enumerate(pdf_texts)]
    milvus_util.insert_data(data)

    # Search and chat
    question = "What are dietary guidelines?"
    embedding = embed_util.generate_embedding(question)
    search_results = milvus_util.search(embedding)

    context = "\n".join([res["entity"]["text"] for res in search_results[0]])
    answer = chat_util.get_answer(context, question)
    print(f"Bot: {answer}")

if __name__ == "__main__":
    main()
