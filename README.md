# Analytics-Dashboard
This Streamlit-based dashboard analyzes BTech student data from Arpit's Institute using MySQL and Plotly. It features CGPA insights, placement stats, top recruiters, and attendance correlation, all with interactive filters.


# 🎓 BTech Student Analytics Dashboard - Arpit's Institute

An interactive student performance analytics dashboard built using **Streamlit**, **MySQL**, **Pandas**, and **Plotly**. This tool helps visualize academic and placement data of BTech students with insightful charts and filters.

---

## 📊 Features

- **Filter by Branch and Year**
- **Total Students, Average CGPA & Placement Rate**
- **CGPA Distribution (Histogram)**
- **Placement Overview (Pie Chart)**
- **Top Recruiters (Bar Chart)**
- **Attendance vs CGPA (Scatter Plot)**
- **Raw Data Viewer**

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python, Pandas
- **Database**: MySQL
- **Visualization**: Plotly Express

---

## 🗄️ MySQL Table Structure

Table Name: `students`

```sql
CREATE TABLE students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    branch VARCHAR(50),
    year INT,
    cgpa FLOAT,
    placed BOOLEAN,
    company VARCHAR(100),
    attendance_percent FLOAT
);

