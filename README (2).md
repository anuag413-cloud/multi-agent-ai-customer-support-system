# Multi-Agent Customer Support System

## Overview

Multi-Agent Customer Support System is an AI-powered customer support platform developed using Python. The system uses multiple agents to classify customer queries, analyze sentiment, provide support responses, and manage customer tickets efficiently.

## Features

* Query Classification Agent
* Sentiment Analysis Agent
* Billing Support Agent
* Technical Support Agent
* Escalation Agent
* Response Generation Agent
* Ticket Management System
* SQLite Database Integration
* Streamlit User Interface

## Project Structure

```text
Multi-agent-customer-support/
│
├── main.py
├── requirements.txt
├── README.md
├── support.db
│
├── agents/
│   ├── classifier_agent.py
│   ├── sentiment_agent.py
│   ├── billing_agent.py
│   ├── tech_support_agent.py
│   ├── escalation_agent.py
│   └── response_agent.py
│
├── database/
│   ├── __init__.py
│   └── db.py
│
└── frontend/
    └── app.py
```

## Technologies Used

* Python
* Streamlit
* SQLite
* TextBlob
* Pandas

## Installation

1. Clone the repository

```bash
git clone <repository-url>
```

2. Navigate to project folder

```bash
cd Multi-agent-customer-support
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

## Running the Project

For Streamlit UI:

```bash
streamlit run frontend/app.py
```

For Python execution:

```bash
python main.py
```

## Workflow

1. Customer submits a query.
2. Query Classification Agent categorizes the query.
3. Sentiment Analysis Agent analyzes customer sentiment.
4. Query is routed to the appropriate support agent.
5. Response Generation Agent creates a response.
6. Escalation Agent checks whether escalation is required.
7. Ticket is stored in the database.

## Future Enhancements

* LangChain Integration
* LangGraph Workflow
* OpenAI API Integration
* RAG-based Knowledge Base
* FastAPI Backend
* Analytics Dashboard

## Author

Anupriya Barnawal

## License

This project is created for educational and learning purposes.
