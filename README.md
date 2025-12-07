# Profitability Intelligence Engine (Proof of Concept) 🛡️

![Status](https://img.shields.io/badge/Status-Active_Development-green)
![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Platform](https://img.shields.io/badge/Platform-Looker_Studio-orange)

### 🔴 [**LAUNCH LIVE COMMAND CENTER**](https://lookerstudio.google.com/reporting/551f2a30-58d2-4443-a055-8de4780bebd2)
*(Click above to access the interactive dashboard)*

---

## 📖 Project Context
This repository serves as a **technical demonstration** of the data auditing architectures I deploy in enterprise environments.

Due to Non-Disclosure Agreements (NDAs) regarding my professional work, I cannot share proprietary code or data. Instead, I have engineered this **Proof of Concept (PoC)** using a public e-commerce dataset from Kaggle to simulate the complexity of a high-volume retail environment.

**The Goal:** To demonstrate how raw, unstructured transaction logs can be transformed into an automated "Profitability Audit" system using Python and Cloud Visualization tools.

---

## ⚙️ System Architecture

Most dashboards are passive—they just show sales. This system is active. It acts as an **Automated Auditor** that flags operational inefficiencies before they destroy margins.

### 1. The Ingestion Layer (Python ETL)
The `etl_script.py` module mimics a production-grade ETL pipeline. It handles the "dirty work" of data engineering:
* **Sanitization:** Enforces strict datetime typing and handles null values/messy schemas.
* **Standardization:** Normalizes column names to match enterprise warehouse standards.

### 2. The Logic Layer (Rule-Based AI)
I implemented a custom audit algorithm that classifies every single transaction into performance buckets:
* **CRITICAL:** Negative Margin events (immediate cash bleed).
* **WARNING:** Low Margin (<10%) events (efficiency leaks).
* **AUDIT FLAG:** Detects the "Bad Discount" anomaly (Discount > 30% resulting in Net Loss).

### 3. The Visualization Layer (Command Center)
The processed data is piped into **Google Looker Studio**, featuring:
* **Dark Mode UI:** Designed for high-contrast executive monitoring.
* **Executive Filters:** One-click filtering to isolate "Critical" alerts.
* **Drill-Down Capabilities:** Deep-dive analysis by Region, Category, and SKU.

---

## 🛠️ Technical Stack
* **Language:** Python 3.9+ (`pandas`, `numpy`)
* **Visualization:** Google Looker Studio
* **Data Source:** [Kaggle E-Commerce Sales Dataset](https://www.kaggle.com/) (Simulated Production Data)
* **Output:** Processed Audit Logs (CSV)

---

## 📂 Repository Structure

```text
├── etl_script.py                   # The core processing logic
├── Ecommerce_Sales_Data_2024_2025.csv   # Raw input data (Simulated)
├── Processed_Profitability_Audit.csv    # Output data (Ready for Viz)
└── README.md                       # System documentation
