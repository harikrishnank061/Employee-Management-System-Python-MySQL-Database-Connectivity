print('===============================================================')
import mysql.connector as sql
import datetime as dt
import time
import sys
#github-jenkins-sonarqube-integretion
conn = sql.connect(host='localhost', user='root', passwd='root', database='employees')
cur = conn.cursor()

print('==================== WELCOME TO START EMPLOYEE MANAGEMENT SYSTEM ====================')
print(dt.datetime.now())

print('1. REGISTER')
print('2. LOGIN')
n = int(input('Enter your choice: '))
print()

if n == 1:
    name = input('Enter a Username: ')
    passwd = int(input('Enter a 4 DIGIT Password: '))
    V_SQLInsert = "INSERT INTO log_id (user_id, password) VALUES (%s, %s)"
    cur.execute(V_SQLInsert, (name, str(passwd)))
    conn.commit()
    print('\nUSER created successfully')

elif n == 2:
    name = input('Enter your Username: ')
    passwd = int(input('Enter your 4 DIGIT Password: '))
    V_Sql_Sel = "SELECT * FROM log_id WHERE password=%s AND user_id=%s"
    cur.execute(V_Sql_Sel, (str(passwd), name))
    result = cur.fetchone()
    if result is None:
        print('\nInvalid username or password')
        sys.exit()
    else:
        print("\nLogged in successfully as", name)
        print("\t\t\t", time.ctime())

        def menu():
            print(" EMPLOYEES MANAGEMENT SYSTEM ")
            while True:
                print("\n1. Employee Registration")
                print("2. Employee Details")
                print("3. Update Salary/Details")
                print("4. Employees List")
                print("5. Number of Employees")
                print("6. Work Experience")
                print("7. Know Your Salary")
                print("8. Exit")

                choice = int(input("Enter your choice: "))
                if choice == 1:
                    register()
                elif choice == 2:
                    details()
                elif choice == 3:
                    em_salary()
                elif choice == 4:
                    em_list()
                elif choice == 5:
                    em_count()
                elif choice == 6:
                    em_perform()
                elif choice == 7:
                    salary()
                elif choice == 8:
                    print("Thank You. Exiting...")
                    break
                else:
                    print("Invalid Choice.")

        def register():
            v_em_no = int(input("Enter your employee ID: "))
            v_em_name = input("Enter your name: ")
            v_em_dept = input("Enter department you want to join: ")
            v_em_salary = int(input("Enter your salary: "))
            v_em_age = int(input("Enter your age: "))
            v_sql_insert = "INSERT INTO office VALUES (%s, %s, %s, %s, %s)"
            cur.execute(v_sql_insert, (v_em_no, v_em_name, v_em_dept, v_em_salary, v_em_age))
            conn.commit()
            print("Registered successfully.")

        def details():
            cur.execute("SELECT * FROM office")
            results = cur.fetchall()
            for x in results:
                print(x)

        def em_salary():
            eid = int(input('Enter your ID to update: '))
            empup = int(input('1. Update Name\n2. Update Salary\n3. Update Age\nEnter choice: '))
            if empup == 1:
                nam = input("Enter updated name: ")
                cur.execute("UPDATE office SET v_em_name=%s WHERE v_em_no=%s", (nam, eid))
            elif empup == 2:
                ch = int(input('1. 10%\n2. 15%\n3. 20%\nEnter choice: '))
                percent = {1: 0.10, 2: 0.15, 3: 0.20}.get(ch, 0)
                if percent:
                    cur.execute("UPDATE office SET v_em_salary = v_em_salary + v_em_salary * %s WHERE v_em_no = %s", (percent, eid))
            elif empup == 3:
                ag = int(input("Enter updated age: "))
                cur.execute("UPDATE office SET v_em_age=%s WHERE v_em_no=%s", (ag, eid))
            conn.commit()
            print("Update successful.")

        def em_list():
            try:
                cur.execute("SELECT v_em_name FROM office ORDER BY v_em_name ASC")
                list_ = cur.fetchall()
                for x in list_:
                    print(x)
                print("Total employees:", cur.rowcount)
            except:
                print("Unable to show the list")

        def em_count():
            cur.execute("SELECT COUNT(*) FROM office")
            count = cur.fetchone()[0]
            print("Number of employees:", count)

        def salary():
            nam = input("Enter your name: ")
            cur.execute("SELECT v_em_salary FROM office WHERE v_em_name=%s", (nam,))
            salary = cur.fetchone()
            if salary:
                print(f"{salary[0]} is your current salary, {nam}")
            else:
                print("Employee not found.")

        def em_perform():
            v_em_no = int(input("Enter your employee ID: "))
            v_em_name = input("Enter your name: ")
            v_em_dept = input("Enter department: ")
            v_em_performance = input("Enter your performance: ")
            v_em_work = int(input("Enter your experience (YEARS): "))
            v_sql_insert = "INSERT INTO v_em_performance VALUES (%s, %s, %s, %s, %s)"
            cur.execute(v_sql_insert, (v_em_no, v_em_name, v_em_dept, v_em_performance, v_em_work))
            conn.commit()
            print("Performance added")

        menu()
print('====================================================================')
