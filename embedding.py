# Importing libraries
import os
from dotenv import load_dotenv
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from bedrock_client import client
from langchain_aws import BedrockEmbeddings
from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore

# Setting up the environment
load_dotenv()

# Setting up the text splitter
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)

# Setting up the embedding model
bedrock_embedding = BedrockEmbeddings(model_id = "amazon.titan-embed-text-v1",
                                      client = client)

# Setting up the vector store
pc = Pinecone(api_key = os.environ['pinecone_api_key'])
vector_store = PineconeVectorStore(index = pc.Index('vectorstore'),
                                   embedding = bedrock_embedding,
                                   namespace = "New namespace")
 
def add_documents(documents):
    
    # Split the document
    documents = splitter.split_documents(documents)
    
    # Add document to namespace
    vector_store.add_documents(documents = documents)

    return vector_store