# Olist-Data-Pipeline-Python# 🐍 Olist Retail Data Pipeline (Python & SQL)

## 🎯 Overview
This project demonstrates an **End-to-End Data Pipeline** implemented in Python, transforming raw E-commerce data into a structured **Gold Data Warehouse**.

## 🏗️ Architecture (Medallion)
- **Bronze Layer:** Ingestion of raw CSV (Customers, Products, Sales) and JSONL (Web Events).
- **Silver Layer:** Data cleaning, city name normalization using Pandas, and validation filtering.
- **Gold Layer:** Final structured tables stored in an **SQLite Warehouse** for analytical querying.

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Data Processing:** Pandas
- **Storage:** SQLite
- **Environment:** GitHub Codespaces & Actions

## 📊 Key Features
- Handled **Semi-structured data** (JSONL) alongside structured CSVs.
- Optimized performance for processing **100K+ records** in seconds.
- Built a **Clean Schema** ready for Power BI or Tableau integration.
