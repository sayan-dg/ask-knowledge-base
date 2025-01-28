# Importing libraries
from bedrock_client import client
from langchain_aws import BedrockLLM
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.prompts import ChatPromptTemplate
from embedding import vector_store

# Setting up the LLM
llm = BedrockLLM(model_id = "mistral.mixtral-8x7b-instruct-v0:1",
              client = client)

def generate_response(query):
    
    system_prompt = """
    Use the provided context to answer the question.
    If you can't find the answer, say that you don't know.
    Keep your answer concise.
    Context : {context}
    """

    prompt = ChatPromptTemplate.from_messages(
        [
         ("system" , system_prompt),
         ("human" , "{input}")
         ]
    )

    qa_chain = create_stuff_documents_chain(llm, prompt)

    chain = create_retrieval_chain(vector_store.as_retriever(), qa_chain)
    
    response = chain.invoke({"input" : query})
    
    return response['answer']
