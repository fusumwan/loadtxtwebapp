import openai
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader
from langchain.schema import Document
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

class ChromaLangchainDatabase:
    def __init__(self, db_directory: str):
        self.db_directory = db_directory

    def load_documents(self):
        loader = DirectoryLoader(self.db_directory)
        documents = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        docs = text_splitter.split_documents(documents)
        return docs

    def embed_documents(self, docs):
        embeddings = OpenAIEmbeddings()
        return embeddings.embed_documents(docs)

    def create_chroma_index(self, docs):
        embeddings = self.embed_documents(docs)
        chroma_store = Chroma(embedding_function=embeddings)
        chroma_store.add_documents(docs)
        return chroma_store

    def create_persistent_db(self):
        # Load and split the documents
        docs = self.load_documents()

        # Embed the documents
        embeddings = self.embed_documents(docs)

        # Create the Chroma vector store and add the documents
        chroma_store = Chroma(persistent=True, embedding_function=embeddings)
        chroma_store.add_documents(docs)
        
        # Save the Chroma vector store to disk
        chroma_store.save()

        print("Persistent Chroma database created successfully.")


    def load_persistent_db(self):
        try:
            chroma_store = Chroma.load(self.db_directory)
            print("Persistent Chroma database loaded successfully.")
            return chroma_store
        except FileNotFoundError:
            print("No existing database found at the specified directory.")
            return None

    def search(self, query: str):
        chroma_store = self.load_persistent_db()
        if chroma_store:
            results = chroma_store.similarity_search(query)
            return results
        else:
            return []
