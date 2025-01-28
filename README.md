# Ask your knowledge base

This project is a **Document Question-Answering (QA) Chatbot** built using the following technologies:  

- **LangChain**: For building the retrieval-augmented generation (RAG) pipeline.  
- **Pinecone**: As the vector store for document embedding storage and retrieval.  
- **Amazon Bedrock**:  
  - **`mistral.mixtral-8x7b-instruct`**: A powerful large language model (LLM) for generating responses.  
  - **`amazon.titan-embed-text-v1`**: An embedding model used to generate vector representations of the documents.  
- **Streamlit**: For creating an interactive frontend for document upload and chatting.  

This chatbot allows users to upload documents, index them into Pinecone, and then ask questions that the chatbot answers using the uploaded content.

---

## Features

1. **Document Upload**: Users can upload `.pdf` documents, which are processed and stored in a vectorized format.  
2. **Contextual Question Answering**: Questions are answered using the uploaded documents as the primary source of context.  
3. **Streamlit Frontend**: Provides a simple and user-friendly interface for document upload and chat functionality.  
4. **Persistent Vector Storage**: Indexed documents are stored in Pinecone for efficient retrieval.  
5. **Robust LLM Integration**: Utilizes Amazon Bedrock's state-of-the-art models for embeddings and language understanding.  

---

## Requirements

### Prerequisites

1. **Python 3.8+** installed on your system.  
2. **Pinecone Account**: [Sign up for Pinecone](https://www.pinecone.io/) and get an API key.  
3. **Amazon Bedrock Access**: Ensure you have access to Amazon Bedrock and necessary credentials.  
4. **Streamlit**: Install Streamlit for running the frontend.  

### Python Libraries

Install the required libraries using `pip`:

```bash
pip install -r requirements.txt
```

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/sayan-dg/ask-knowledge-base
cd ask-knowledge-base
```

### 2. Set Up Environment Variables

Create a `.env` file or set the following environment variables in your system:

```
export aws_access_key_id
aws_secret_access_key
pinecone_api_key
```

### 3. Initialize Pinecone
Log in to Pinecone, create an index named `vectorstore`, and note the environment.

### 4. Run the Application
Start the Streamlit app:

```bash
streamlit run app.py
```

---

## Application Workflow

1. **Document Upload**:  
   - Upload a `.pdf` file.
   - Press `Process document`
   - The document is processed, vectorized using `amazon.titan-embed-text-v1`, and stored in Pinecone under a specific namespace.  

2. **Chat Interface**:  
   - Enter your question in the input box.
   - Press `Generate response`  
   - The chatbot retrieves relevant context from Pinecone and generates a response using `mistral.mixtral-8x7b-instruct`.  

---

## Technologies Used

| Component                  | Technology                              |
|----------------------------|-----------------------------------------|
| Frontend                   | Streamlit                              |
| LLM                        | mistral.mixtral-8x7b-instruct (Amazon Bedrock) |
| Embedding Model            | amazon.titan-embed-text-v1 (Amazon Bedrock) |
| Vector Store               | Pinecone                               |
| Backend Pipeline           | LangChain                              |

---

## Contributing

Contributions are welcome! Please fork the repository, make changes, and submit a pull request.

---

## License

This project is licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0).

---

## Contact

For any questions or issues, feel free to contact:  
**Your Name**  
**Email**: sayandg05@gmail.com  
**GitHub**: [sayan-dg](https://github.com/sayan-dg)