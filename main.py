from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from llama_index.vector_stores.types import MetadataFilters, ExactMatchFilter
from llm import loaded_index


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/get_answer")
async def get_answer(query,file_name):
    filters = MetadataFilters(filters=[ExactMatchFilter(key="filename", value=file_name)])
    query_engine = loaded_index.as_query_engine(similarity_top_k=3,filters=filters)
    response  = query_engine.query(query) 
    return {"answer": response.response,"source":response.source_nodes}
