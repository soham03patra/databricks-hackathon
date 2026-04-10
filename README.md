# 🏥 AI-Powered Healthcare Intelligence System

## 📌 Overview
This project is an AI-powered healthcare intelligence system built using Databricks. It transforms unstructured healthcare data into structured, actionable insights using Large Language Models (LLMs) and Apache Spark.

The system helps identify healthcare gaps, detect anomalies in facility claims, and support data-driven decision-making for organizations like the Virtue Foundation.

---

## 🚀 Problem Statement
Healthcare data is often unstructured and scattered across multiple sources, making it difficult to analyze and trust. This leads to poor visibility of medical resources and creates "medical deserts" where essential healthcare services are unavailable.

There is a need for an intelligent system that can extract, validate, and analyze healthcare data to improve accessibility and planning.

---

## 💡 Solution
We developed an end-to-end pipeline using Databricks that:
- Extracts structured data from unstructured text using LLMs (IDP)
- Processes and analyzes data using Apache Spark
- Detects anomalies in facility claims
- Identifies underserved regions (medical deserts)
- Enables natural language querying via an agent system

---

## ⚙️ Key Features
- Intelligent Document Parsing (IDP) using LLMs
- Extraction of procedures, equipment, capabilities, and specialties
- Spark-based data processing pipeline
- Anomaly detection for inconsistent facility claims
- Regional analysis to detect medical deserts
- SQL-based analytics
- Agent-based query system for natural language interaction

---

## 🏗️ Tech Stack
- **Databricks**
- **Apache Spark (PySpark)**
- **Python**
- **OpenAI API (LLM)**
- **Pydantic**
- **SQL**

---

## 📂 Project Structure

project/
|── notebook (Databricks notebook)
|── llm_extractor.py
|── main_agent.py
|── facility_and_ngo_fields.py
|── free_form.py
|── medical_specialties.py
|── organization_extraction.py
|── README.md


▶️ How to Run

 1. Upload Data
Upload dataset to Databricks table:
workspace.default.virtue_foundation_ghana_v_0_3_sheet_1

2. Install Dependencies
%pip install openai==0.28.1

3. Set API Key
```python
import openai
openai.api_key = "YOUR_API_KEY"

4. Run Notebook
Execute cells step-by-step:
Data loading
Cleaning
Feature engineering
SQL queries
Agent queries
LLM extraction
