import os
from chromadb import Client
from chromadb.config import Settings

class ChromaDatabase:
    def __init__(self, db_directory):
        self.db_directory = db_directory
        self.client = None
        self.collection = None

    def create_persistent_db(self):
        if not os.path.exists(self.db_directory):
            os.makedirs(self.db_directory)
        self.client = Client(Settings(persistence_directory=self.db_directory))
        return self.client

    def create_collection(self, collection_name):
        self.collection = self.client.get_or_create_collection(name=collection_name)
        return self.collection

    def create_vectorstore_from_documents(self, documents):
        ids = [str(i) for i in range(len(documents))]
        metadata = [{} for _ in range(len(documents))]
        self.collection.add(ids=ids, documents=documents, metadatas=metadata)

    def add_data_with_metadata(self, texts, metadata_list, ids):
        self.collection.add(ids=ids, documents=texts, metadatas=metadata_list)
        
    def similarity_search(self, query_text, top_k=5):
        results = self.collection.query(query_text=query_text, top_k=top_k)
        return results

    def create_openai_embedding(self, texts):
        # Placeholder for embedding generation logic
        return texts

    def add_to_new_collection(self, collection_name, texts, metadata_list, ids):
        new_collection = self.create_collection(collection_name)
        self.add_data_with_metadata(texts, metadata_list, ids)
        return new_collection

    def update_or_remove_values(self, id, new_text=None, new_metadata=None):
        if new_text:
            self.collection.update(id=id, document=new_text, metadata=new_metadata)
        else:
            self.collection.delete(id=id)

    def manage_collections(self, collection_name, texts, metadata_list, ids):
        self.create_collection(collection_name)
        self.add_data_with_metadata(texts, metadata_list, ids)
        
    def count_records(self):
        return self.collection.count()

    def view_all_records(self):
        return self.collection.find()
    
    def load_persistent_db(self):
        # Load the existing database
        if os.path.exists(self.db_directory):
            settings = Settings()
            settings.persist_directory = self.db_directory
            
            self.client = Client(settings)
        else:
            raise FileNotFoundError(f"Chroma database directory not found at {self.db_directory}")

    def list_collections(self):
        if self.client is None:
            self.load_persistent_db()
        collections = self.client.list_collections()
        return collections
    

# Usage example
# db = ChromaDB(db_directory="./chroma_db")
# client = db.create_persistent_db()
# collection = db.create_collection("example_collection")
# db.create_vectorstore_from_documents(["doc1", "doc2", "doc3"])
# db.add_data_with_metadata(["new text"], [{"key": "value"}], ["unique_id"])
# results = db.similarity_search("query text")
# print(results)
# db.update_or_remove_values("unique_id", new_text="updated text")
# print(db.count_records())
# print(db.view_all_records())
