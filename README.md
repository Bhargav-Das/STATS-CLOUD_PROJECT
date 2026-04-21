# 📂 GitHub Repository

🔗 Project Repository: [Click Here to View Repo](https://github.com/Bhargav-Das/STATS-CLOUD_PROJECT)

🌐 Dashboard: [Live Dashboard](https://bhargav-das.github.io/STATS-CLOUD_PROJECT/)

---

# 📊 Statistical Analysis of Website Performance Metrics for Cloud Infrastructure Optimization

A Python-based statistics and cloud analytics project that analyzes website performance data using descriptive statistics, visualization, hypothesis testing, and a professional HTML dashboard.

---

## 📌 Project Objective

The aim of this project is to analyze website performance metrics and identify patterns useful for real cloud infrastructure optimization.

This project demonstrates practical cloud use cases such as:

- Auto Scaling  
- Load Balancing  
- Performance Monitoring  
- Capacity Planning  
- CDN Optimization  
- Better User Experience  

---

## 📂 Dataset Used

**File:** `labeled_dataset.csv`

Dataset contains **734 rows** and **9 columns**.

### Columns:

- Sr No  
- website_url  
- Category  
- Page Size (KB)  
- Load Time(s)  
- Response Time(s)  
- Throughput  
- Performance_Label  
- User Response  

---

## 🛠️ Technologies Used

- Python  
- Pandas  
- NumPy  
- Matplotlib  
- SciPy  
- HTML/CSS  
- VS Code  

---

## 📁 Python Workflow Used

```bash
Stats_Cloud_Project/
│── Load dataset using Pandas
│── Clean duplicate & null values
│── Standardize text labels
│── Generate descriptive statistics
│── Create visualizations
│── Perform T-Test
│── Perform ANOVA
│── Perform Chi-Square Test

```
## ⚙️ Workflow

**1️⃣ Load Dataset**

python 1_load_data.py

- Loads CSV file
- Shows dataset preview
- Checks rows and columns

## 2️⃣ Data Cleaning

python 2_clean_data.py

- Removed duplicate rows
- Checked missing values

Result:

- Before Cleaning: 734 rows
- After Cleaning: 733 rows
 
## 3️⃣ Descriptive Statistics

python 3_statistics.py

Calculated:

- Mean
- Median
- Standard Deviation
- Minimum / Maximum
- Metric	Load Time	Response Time	Throughput
- Mean	1.786	1.013	317.69
- Median	1.38	0.599	97.30
- Max	7.94	7.419	15227

## 4️⃣ Visualization

python 4_visualization.py

Generated graphs:

- Histogram of Load Time
- Throughput Bar Chart
- Performance Label Pie Chart

Saved as:

- graph1.png
- graph2.png
- graph3.png

## 5️⃣ Hypothesis Test 1 (T-Test)

python 5_hypothesis_test1.py

Compared Load Time between Fast and Slow websites.

Result:

p-value = 0.000632

✅ Significant difference found.

## 6️⃣ Hypothesis Test 2 (Chi-Square)

python 6_hypothesis_test2.py

Checked relationship between:

- Category
- Performance_Label

Result:

p-value = 0.006116

✅ Category and Performance are related.

## 7️⃣ Final Dashboard

Files used:

- 7_final_report.py
- index.html

Displays complete project report in browser.

## 🌐 Real Cloud Use Cases
Metric	Cloud Use Case
Load Time	Auto Scaling
Response Time	Monitoring
Throughput	Load Balancing
Performance_Label	SLA Tracking
Category	Capacity Planning
Page Size	CDN Optimization

## 📈 Key Insights
- Fast websites load quicker than slow websites
- Website category affects performance
- Throughput varies widely
- Larger pages may slow loading speed
- Statistical analysis helps cloud optimization

## 🎯 Final Conclusion

This project successfully analyzed real website performance metrics using Python and statistics.

The results can be used in real cloud environments to improve:

- Server efficiency
- User experience
- Scaling decisions
- Website speed
- Resource optimization
