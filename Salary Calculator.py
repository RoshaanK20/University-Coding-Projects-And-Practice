#Salary calculator for 2 Employees

# User Input For Employee 1:
employee_name_1 = input("Enter Employee 1 Name: ")
salary_1 = float(input("Enter Your Salary Amount: "))
petrol_allowance_1 = float(input("Enter The Allowance Amount: "))

# Tax Calculation:
tax_rate = 0.18 # 18% tax rate
min_salary = 20000

# Employee 1:
gross_salary_1 = salary_1 + petrol_allowance_1
if (salary_1 >= min_salary):
    tax_amount_1 = gross_salary_1 * tax_rate
    net_salary_1 = gross_salary_1 - tax_amount_1
else: 
    tax_amount_1 = 0 
    net_salary_1 = gross_salary_1

# User Input For Employee 2:
employee_name_2 = input("\nEnter Employee 2 Name: ")
salary_2 = float(input("Enter Your Salary Amount: "))
petrol_allowance_2 = float(input("Enter The Allowance Amount: "))

    # Employee 2:
gross_salary_2 = salary_2 + petrol_allowance_2
if (salary_2 >= min_salary):
    tax_amount_2 = gross_salary_2 * tax_rate
    net_salary_2 = gross_salary_2 - tax_amount_2
else: 
    tax_amount_2 = 0 
    net_salary_2 = gross_salary_2

# Display Result:
print ("\033[1;34;40m ***----------SALARY CALCULATOR----------***")
print ("\033[0;36;47m~:Salary Detail For Employee 1:~: ")
print (f"Employee Name: {employee_name_1}")
print (f"Net Salary: Rs.{net_salary_1}")
print (f"Tax Dedcution: Rs.{tax_amount_1}")
print ("\n")

print ("\033[0;36;47m~:Salary Detail For Employee 2:~: ")
print (f"Employee Name: {employee_name_2}")
print (f"Net Salary: Rs.{net_salary_2}")
print (f"Tax Dedcution: Rs.{tax_amount_2}")
print ("\n")
