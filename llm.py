from llama_index import StorageContext, load_index_from_storage, ServiceContext
from dotenv import load_dotenv, find_dotenv
from llama_index.llms import Ollama
from llama_index import ServiceContext

load_dotenv(find_dotenv(), override=True)

use_offline_model = False

if use_offline_model:
    service_context = ServiceContext.from_defaults(
        llm=Ollama(model="llama2"), embed_model="local:BAAI/bge-large-en"
    )

    storage_context = StorageContext.from_defaults(persist_dir="./content/VectorStore")
    print("offline model")

else:
    service_context = ServiceContext.from_defaults()
    storage_context = StorageContext.from_defaults(
        persist_dir="./content/VectorStore-online"
    )
# Load secrets from .env file

loaded_index = load_index_from_storage(storage_context, service_context=service_context)
