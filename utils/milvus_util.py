from pymilvus import MilvusClient

class MilvusUtility:
    def __init__(self, uri="./milvus_demo.db", collection_name="nutrition_collection", dimension=768):
        self.client = MilvusClient(uri=uri)
        self.collection_name = collection_name
        self.dimension = dimension

    def setup_collection(self):
        if self.client.has_collection(self.collection_name):
            self.client.drop_collection(self.collection_name)

        self.client.create_collection(
            self.collection_name,
            dimension=self.dimension,
            metric_type="IP",
            consistency_level="Strong",
        )

    def insert_data(self, data):
        insert_res = self.client.insert(collection_name=self.collection_name, data=data)
        return insert_res["insert_count"]

    def search(self, embedding, limit=3):
        return self.client.search(
            collection_name=self.collection_name,
            data=[embedding],
            limit=limit,
            search_params={"metric_type": "IP", "params": {}},
            output_fields=["text"],
        )
