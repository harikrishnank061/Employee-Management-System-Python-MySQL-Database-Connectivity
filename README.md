
# 🧾 Employee Management System (Python + MySQL)

A simple yet powerful command-line based **Employee Management System** developed using **Python** and **MySQL**. This system provides essential functionalities for managing employee records, salaries, performance, and user authentication in an office environment.

---

## 🔧 Features

- 🔐 User Login and Registration
- ➕ Add New Employees
- 📝 View Employee Details
- 💵 Update Salary
- ✍️ Update Name and Age
- 🔢 View Total Employee Count
- 🔠 Display Employees Alphabetically by Name
- 📈 Record Employee Performance
- 👀 View Performance Records
- 💰 Show Salary by Employee Number

---

## 📦 Requirements

- Python 3.7 or above
- MySQL Server
- mysql-connector-python

---

## 🛠️ Setup & Installation

### 1. 🔽 Install Python

If you don't have Python installed, download it from the official site:  
👉 [https://www.python.org/downloads/](https://www.python.org/downloads/)

Verify installation:

```bash
python --version
```

### 2. 🐬 Install MySQL Server
Download and install MySQL from:
👉 https://dev.mysql.com/downloads/mysql/

After installation:

Open MySQL Command Line or Workbench

Set up a user (default: root) and password

Verify installation:
```
mysql -u root -p
```
### 3. 🧩 Install Required Python Packages
Install dependencies from requirements.txt:
```
pip install -r requirements.txt
```
Or install manually:
```
pip install mysql-connector-python
```
### 🗃️ Database Schema
Run the following SQL commands in your MySQL client to create the necessary tables:
```
CREATE DATABASE IF NOT EXISTS employees;
USE employees;

CREATE TABLE IF NOT EXISTS log_id (
    user_id VARCHAR(25) PRIMARY KEY,
    password INT NOT NULL
);

CREATE TABLE IF NOT EXISTS office (
    v_em_no INT PRIMARY KEY,
    v_em_name VARCHAR(50),
    v_em_dept VARCHAR(50),
    v_em_salary FLOAT,
    v_em_age INT
);

CREATE TABLE IF NOT EXISTS v_em_performance (
    v_em_no INT,
    v_em_name VARCHAR(50),
    v_em_dept VARCHAR(50),
    v_em_performance VARCHAR(100),
    v_em_work INT
);
```
### 🚀 How to Run
1.Clone this repository:
```
git clone https://github.com/your-username/employee-management-system.git
cd employee-management-system
```

2.Ensure your MySQL server is running.

3.Open main.py and update your DB credentials if needed:
```
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # update this
    database="employees"
)
```
4.Run the project:
```
python main.py
```
### 💡 Usage Notes
Default login system is handled via the log_id table.

New users can register through the prompt.

All employee data is stored and managed through MySQL.

### 👨‍💻 Author
Harikrishnan K

💌 harikrishnank061@gmail.com

### 🌟 Show your support!
If you like this project, leave a ⭐ on the repo. Contributions and suggestions are welcome!
