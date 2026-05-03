import pandas as pd
import sqlite3

# --- 1. Bronze Stage (الاستلام) ---
print("📂 Loading raw Olist data...")
df_customers = pd.read_csv('raw_customers.csv')
df_products = pd.read_csv('raw_products.csv')
df_sales = pd.read_csv('raw_sales_transactions.csv')

# --- 2. Silver Stage (التنظيف) ---
print("🧼 Transforming data to Silver Layer...")
# توحيد المدن
df_customers['customer_city'] = df_customers['customer_city'].str.upper().str.strip()
# تصفية المبيعات
df_sales = df_sales[df_sales['price'] > 0]

# --- 3. Gold Stage (التحميل) ---
print("🏛️ Saving to SQLite Warehouse...")
conn = sqlite3.connect('olist_warehouse.db')
df_customers.to_sql('customers', conn, if_exists='replace', index=False)
df_products.to_sql('products', conn, if_exists='replace', index=False)
df_sales.to_sql('sales', conn, if_exists='replace', index=False)


print("✅ Pipeline Completed! Gold Warehouse created.")

import json
# --- معالجة وحش الـ JSONL (Web Events) ---
print("🌐 Processing Web Events (JSONL)...")
# بايثون بيقرأ الـ JSONL سطر بسطر بسهولة
events_list = []
with open('raw_web_events.jsonl', 'r') as f:
    for line in f:
        events_list.append(json.loads(line))

df_events = pd.DataFrame(events_list)
# صب الـ Events في جدول جديد
df_events.to_sql('web_events', conn, if_exists='replace', index=False)
conn.close()
