# Multi-Source Knowledge Retrieval System

A high-speed, Retrieval-Augmented Generation (RAG) pipeline that integrates multiple knowledge sources to deliver precise, relevant search results. This end-to-end system is built using LangChain and FAISS, and leverages OpenAI embeddings to perform semantic searches across platforms such as [Wikipedia](https://www.wikipedia.org/), [arXiv](https://arxiv.org/), and custom user-defined websites.

## Features

- **RAG Pipeline with LangChain & FAISS**: 
   Efficient semantic search using FAISS, enhanced by OpenAI embeddings, to achieve high-speed, accurate query matching.

- **Multi-Source Retrieval**:
   Seamlessly integrates Wikipedia, arXiv research papers, and custom websites for diverse data retrieval.

- **Smart Agent Selection**:
   Employs LangChain agents and tools to intelligently select the optimal source based on the query, optimizing response relevance.

- **Real-Time API Access**:
   Utilizes real-time API connections for updated and precise content retrieval across multiple repositories.

## Project Overview

This project addresses the need for comprehensive information retrieval across various sources by:

1. Building a retrieval-augmented generation pipeline to automate document retrieval from multiple sources.
  
2. Optimizing search relevance through OpenAI-powered embeddings and FAISS similarity search.

3. Enabling smart decision-making on which source to use based on query context, using LangChain agents.

## Technology Stack

- **LangChain**: Framework for creating language model applications, utilized for agent-based source selection and tool integration.
  
- **FAISS (Facebook AI Similarity Search)**: Provides vector-based similarity search for efficient retrieval.

- **OpenAI Embeddings**: Supports semantic search by converting queries and documents into high-dimensional embeddings for better relevance.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/multi-source-knowledge-retrieval.git
   cd multi-source-knowledge-retrieval

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt

3. **Set up API keys**:
-   Add your OpenAI API key and any other API credentials in an .env file:
    ```bash
    OPENAI_API_KEY="your_openai_api_key"
    LANGCHAIN_API_KEY="your_langchain_api_key"
    GROQ_API_KEY="your_groq_api_key"
    OTHER_API_KEYS="..."

## Usage

1. **Run the pipeline**:
-   Go to 'agents' folder and execute the following command to run all the cells in the jupyter file and save the output back to the same file
    ```bash
    jupyter nbconvert --execute --to notebook agents.ipynb

2. **Make a query**:
-   Use the terminal interface to input queries.
-   The system will automatically select the best source and return relevant information.

## Results
This project delivers rapid, relevant responses by leveraging the strengths of multiple knowledge sources. With FAISS, it ensures efficient vector-based matching, while LangChain agents guarantee the best source selection for every query.

## Future Enhancements
- **Additional Knowledge Sources**: Expand integration to other repositories or specific domain databases.
- **Enhanced Customization**: User-defined filtering to limit results based on document type, date, or other attributes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE.txt) file for details.


