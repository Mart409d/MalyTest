
import pandas as pd


### Step 1: Hent data

def getData(path,sheet):
    return pd.DataFrame(pd.read_excel(path,sheet))

employee_data = getData("C:\Users\marti\OneDrive\Desktop\mysql\my_shop_data.xlsx","employee")
order_data = getData("C:Users\marti\OneDrive\Desktop\mysql\my_shop_data.xlsx","order")

print(employee_data,order_data)


### Step 2: 'Mysql joins'
# How to loop korrektly
# For hver employee
def salesByEmployee():
    results = {
        "employees": [],
        "sales": []
    }
    for index,employee in employee_data.iterrows():
        results.append(employee["firstname"]+" "+employee["lastname"])
        sales = 0
        for index,order in order_data.iterrows():
            if employee["employee_id"] == order["employee_id"]:
                sales += float(order["unitprice"])*float(order["quantity"])
        results.append(sales)
    return pd.DataFrame(results)


     


#print(salesByEmployee())

# 1. Læg filen i den rigtige mappe
# 2. Kør programmet



### Step 3: Lav grafer

### Step 4: Dash html ting



    