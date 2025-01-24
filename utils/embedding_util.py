from sentence_transformers import SentenceTransformer

class EmbeddingUtility:
    def __init__(self, model_name="BAAI/bge-small-en-v1.5"):
        self.embedding_model = SentenceTransformer(model_name)

    def generate_embedding(self, text):
        return self.embedding_model.encode([text], normalize_embeddings=True).tolist()[0]

    def get_embedding_dimension(self):
        test_embedding = self.generate_embedding("This is a test")
        return len(test_embedding)
