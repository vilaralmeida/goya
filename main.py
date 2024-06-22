import chromadb
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.document_loaders import TextLoader
from typing import List
from langchain.schema import Document
import os
from chromadb.config import Settings

client = chromadb.Client()   


collection = client.create_collection(name="Students")

# Construct the full path to the file
diretrizes_path = os.path.join(".", 'diretrizes')

principios_path = os.path.join(".", 'principios')

deveres_responsabilidades_path = os.path.join(".", 'deveres_responsabilidades')

# Open the file in read mode
with open(diretrizes_path, 'r', encoding='utf-8') as file:
    diretrizes = file.read()


# Open the file in read mode
with open(principios_path, 'r', encoding='utf-8') as file:
    principios = file.read()


# Open the file in read mode
with open(deveres_responsabilidades_path, 'r', encoding='utf-8') as file:
    deveres_responsabilidades = file.read()    

collection.add(
    documents = [principios, diretrizes, deveres_responsabilidades],
    metadatas = [{"source": "principios"},{"source": "diretrizes"},{'source':'deveres responsabilidades'}],
    ids = ["id1", "id2", "id3"]
)


results = collection.query(
    query_texts=["O que se fala sobre clima organizacional?"],
    n_results=2
)

print(results)
