# 📊 Amazon Sales Exploratory Data Analysis (EDA)

This project performs an **Exploratory Data Analysis (EDA)** on an Amazon sales dataset using Python.  
The goal is to uncover insights into **customer behavior, product performance, and geographical trends** to support business decision-making.

---

## 🎯 Objective
To analyze Amazon sales transactional data to identify sales patterns, customer segments, and state-wise order distribution, enabling **data-driven strategies for sales optimization and inventory planning**.

---

## 🛠️ Approach
- **Data Ingestion:**  
  - Imported `Amazon Sale Report.csv` using **Pandas**, handled encoding with `encoding='unicode_escape'`.  
  - Used **NumPy** for numerical operations.

- **Data Cleaning & Preprocessing:**  
  - Removed irrelevant columns (`New`, `PendingS`).  
  - Handled **missing values** using `df.dropna()`.  
  - Converted `ship-postal-code` to integer and parsed `Date` as **datetime object**.  

- **Descriptive Statistics:**  
  - Summarized numerical columns (`Qty`, `Amount`) using `df.describe()`.  

- **Univariate Analysis:**  
  - Visualized frequency distributions (e.g., product **Size**) using **countplots** and **histograms**.  

- **Bivariate Analysis:**  
  - Analyzed relationships (e.g., `Size` vs. `Qty`) using **Seaborn barplots**.  

- **Categorical & Geographical Insights:**  
  - Used **pie charts** to compare **B2B vs retail** customers.  
  - Identified top-performing states using **countplots** on `ship-state`.  

- **Visualization Tools:**  
  - Created interactive and static plots with **Matplotlib** and **Seaborn**.

---

## ✅ Results
- **T-shirts (Size M)** identified as the **highest-selling category**.  
- **Retail customers** significantly outnumber **B2B buyers**.  
- **Maharashtra** recorded the **highest number of orders**.  
- **Amazon fulfillment** emerged as the **dominant delivery channel**.  
- Insights can guide **sales strategy optimization, inventory control, and regional targeting**.

---

## 📂 Technologies Used
- Python  
- Pandas, NumPy  
- Matplotlib, Seaborn  

---

## 🚀 How to Run
1. Clone this repository:
   ```bash
