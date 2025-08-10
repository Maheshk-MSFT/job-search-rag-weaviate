# job-search-rag-weaviate
GenAI Job Search: BM25 vs. Semantic vs. Hybrid Search with Weaviate
This project demonstrates and compares different search strategies—keyword (BM25), semantic, and hybrid—for a job search application. It uses a dataset of job descriptions, ingests them into a Weaviate vector database, and provides a Streamlit interface to query the data.

# Tech stack used: 
	- Python
	- Weaviate
	- Streamlit
	- Ollama

Features
Data Processing: Cleans and prepares raw job posting data for vectorization.

Weaviate Integration: Sets up a Weaviate collection with a custom schema using Ollama for local embeddings.

Search Comparison: Implements and allows for testing of:

Keyword Search (BM25)

Semantic Search

Hybrid Search

Interactive UI: A simple Streamlit application to perform searches and view results.

Tech Stack
Python with Pandas for data manipulation.

Weaviate as the vector database.

Ollama for generating text embeddings locally.

Postman (optional) for interacting with the Weaviate API.

Streamlit for the user interface.

Docker for running Weaviate.

 Steps to setup/flow: 
 (1) Data sourcing - Download the sample data from Kaggle https://www.kaggle.com/datasets/ravindrasinghrana/job-description-dataset  [1.5 GB]	
 (2) Data cleaning - prepare the data (smallset) using Pandas library - bring it to 300 rows with one column prepared for vector indexing 'search_text' - last column 
 (3) Weaviate setup - https://docs.weaviate.io/weaviate/quickstart/local
 (4) Weaviate prep - Create required collection - first create required collection -create using Postman - make sure to not mark "Skip:true" to index/not 
 (5) Data Injestion - use the python code to injest, VScode weaviate studio plugin to verify - 300 should be there as per CSV count 
 (6) Data Fetch
		- Exact search BM25
		- Semantic Search
		- Hybrid Search
  (7) UI Streamlit 

<img width="1330" height="911" alt="b1" src="https://github.com/user-attachments/assets/adb624b8-8e2d-4926-8710-11449517233a" />

<img width="1047" height="746" alt="b2" src="https://github.com/user-attachments/assets/ad491de0-8517-4eb9-8c8a-29a715505c69" />

<img width="1872" height="992" alt="b3" src="https://github.com/user-attachments/assets/d8dcaae2-e61d-4b92-a6e5-e0480e23ea0b" />

<img width="1802" height="1082" alt="b4" src="https://github.com/user-attachments/assets/fdd24e06-f3d8-4c24-a031-7e5d6a334dd1" />

<img width="1632" height="847" alt="b5" src="https://github.com/user-attachments/assets/3ded759c-4fd3-4f87-95c5-1812b754e798" />

<img width="1869" height="980" alt="b6" src="https://github.com/user-attachments/assets/2413ecb3-46bf-486b-abbe-b43f0777779a" />

<img width="1901" height="1198" alt="b7" src="https://github.com/user-attachments/assets/6836ffab-b42d-4698-98e6-e4fcf8e021a8" />

<img width="1902" height="1133" alt="b8" src="https://github.com/user-attachments/assets/0130ab6b-b48d-484b-80b3-155da2b8dfc2" />

<img width="1321" height="1038" alt="b9" src="https://github.com/user-attachments/assets/4e6f07c2-d9e9-4787-8f2e-e5c1fd8b7c05" />

<img width="1267" height="1065" alt="b10" src="https://github.com/user-attachments/assets/0389f27e-f360-4be3-b11b-caff8e2e8f3c" />
