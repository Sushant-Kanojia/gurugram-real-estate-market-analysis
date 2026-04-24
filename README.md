# Gurugram Real Estate Market Analysis

## 📊 Overview

This project analyzes real estate data from Gurugram to uncover pricing trends, locality-wise insights, and key factors influencing property prices. The analysis focuses on data cleaning, exploratory data analysis (EDA), and answering business-driven questions.

Dataset link : https://www.kaggle.com/datasets/nikhilmehrahr26/gurgaon-real-estate-dataset?resource=download

---

## 🛠️ Tools & Technologies

* Python (Pandas, NumPy)
* Data Visualization (Matplotlib, Seaborn)
* Jupyter / VS Code

---

## 🔧 Data Cleaning

* Standardized column names for consistency
* Converted price and rate per sqft into numerical format
* Cleaned categorical variables (status, flat type, RERA approval)
* Removed duplicate records to improve data quality

---

## 📈 Key Analysis Performed

* Identified the **costliest property** in Gurugram
* Determined **localities with highest average price**
* Analyzed **price per square foot across locations**
* Compared **ready-to-move vs under-construction pricing**
* Evaluated **impact of RERA approval on pricing**
* Examined **relationship between area and price**
* Identified **most expensive BHK configurations and property types**
* Analyzed **top builders with highest pricing trends**

---

## 📊 Visualizations

* Scatter plots to analyze:

  * Area vs Price
  * Area vs Rate per Sqft

---

## 🔍 Key Insights

* Pricing varies significantly across localities, with certain areas consistently commanding higher average prices
* Larger properties tend to have higher total prices but not always higher price per sqft
* Builder reputation and locality play a major role in pricing
* RERA approval and property status show measurable impact on price trends

---

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py
```

---

## 📁 Project Structure

```
gurugram-real-estate-analysis/
│
├── data.csv
├── main.py
├── README.md
```
