from langchain_community.llms import Ollama 
from langchain_community.document_loaders import PyPDFLoader 
from langchain.text_splitter import RecursiveCharacterTextSplitter 
from langchain_community.embeddings import HuggingFaceEmbeddings 
from langchain_community.vectorstores import Chroma 
from langchain.chains import RetrievalQA 

# 1. Load the PDF 
loader = PyPDFLoader("sample.pdf") 
documents = loader.load() 

# 2. Split into chunks 
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0) 
docs = splitter.split_documents(documents) 

# 3. Create embeddings 
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2") 

# 4. Store in Chroma DB 
vectordb = Chroma.from_documents(docs, embeddings) 

# 5. Initialize Ollama with Gemma 3 (1B) 
llm = Ollama(model="gemma3:1b") 

# 6. Build Retrieval-QA pipeline 
qa = RetrievalQA.from_chain_type(llm=llm, retriever=vectordb.as_retriever()) 

# 7. Ask a question 
query = input("Please enter your query regarding the document:")
print(qa.run(query))