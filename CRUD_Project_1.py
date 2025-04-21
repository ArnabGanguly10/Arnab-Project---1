import pymysql

conn_obj = pymysql.connect(
        host='localhost',
        user='root',
        password='Arnab@1234',
        database='CRUD_Project_1')
cur_obj = conn_obj.cursor()

#Define function to enter the data in the database
def data_entry_sql(cust_name,cust_address,cust_ph_no,cust_user_id,cust_password):

    sql = "INSERT INTO cust_details (cust_name, cust_address, cust_ph_no, user_id, password) VALUES (%s, %s, %s, %s, %s)"
    data = (cust_name,cust_address,cust_ph_no,cust_user_id,cust_password)

    try:
        cur_obj.execute(sql, data)
        print("YOUR DETAILS HAVE BEEN STORED SUCCESSFULLY")
        conn_obj.commit()
    except pymysql.Error as e:
        print("Error retrieving data from MySQL:", e)
        conn_obj.rollback()

#Define function to retrieve the data
def data_retrieve(cust_user_id):
    query = f"select * from cust_details WHERE user_id=\'{cust_user_id}\'"
    #print(query)
    try:
        cur_obj.execute(query)
        result = cur_obj.fetchone()
        conn_obj.commit()
    except pymysql.Error as e:
        print("Error retrieving data from MySQL:", e)
        conn_obj.rollback()
    return result

#Define function to enter the user details
def user_details_entry():
    cust_name=input("Please Enter Your Full Name->").upper()
    cust_address = input("Please Enter Your Full Address->").upper()
    cust_ph_no = input("Please Enter Your Phone Number->").upper()
    cust_user_id=input("Please Set Your User ID->")
    cust_password = input("Please Set Your Password->")
    data_entry_sql(cust_name,cust_address,cust_ph_no,cust_user_id,cust_password)

#Define function to update the data by user
def data_update(cust_user_id,cust_address,cust_ph_no,cust_password):
    update_user = f"UPDATE cust_details SET cust_address=\'{cust_address}\',cust_ph_no=\'{cust_ph_no}\',password=\'{cust_password}\' WHERE user_id=\'{cust_user_id}\'"
    try:
        cur_obj.execute(update_user)
        updated_result = cur_obj.fetchall()
        conn_obj.commit()
    except pymysql.Error as e:
        print("Error Updating data from MySQL:", e)
        conn_obj.rollback()
    return updated_result

#Define function to delete the data by user
def data_delete(cust_user_id):
    delete_user = f"DELETE from cust_details Where user_id=\'{cust_user_id}\'"
    try:
        cur_obj.execute(delete_user)
        deleted_result = cur_obj.fetchone()
        conn_obj.commit()
    except pymysql.Error as e:
        print("Error Deleting the data from MySQL:", e)
        conn_obj.rollback()
    return deleted_result

#starting point of our code
print("!! Welcome To Our Customer Services !!")
print("--------------------------------------")
cust_choice=input("Please Select \n1- For New Customer\n 2- For Existing Customer\n->")
if cust_choice=='1':
    user_details_entry()
elif cust_choice=='2':
    cust_user_id=input("Please Enter Your User ID->")
    cust_password = input("Please Enter Your Password->")
    result_from_db=data_retrieve(cust_user_id)
    if result_from_db:
        if result_from_db[-1]==cust_password:
            print("access granted")
            edit_customer = input("1 - Enter U to Update Details \n2 - Enter D to Delete the Details \n -->")
            if edit_customer=='U':
                print("!! NOTE : CUSTOMER NAME CANNOT BE MODIFIED !!")
                cust_address = input("Enter Your New Address -->")
                cust_ph_no = input("Enter Your New Phone Number -->")
                cust_password = input("Enter Your New Password -->")
                data_update(cust_user_id,cust_address,cust_ph_no,cust_password)
                print("Your User Account Has Been Updated !!")
            elif edit_customer=='D':
                data_delete(cust_user_id)
                print("Your User Account Has Been Deleted !!")
            else :
               print("Thank You for Visiting!")
        else:
            print("access denied")
    else:
        user_details_entry()
    #print(result_from_db)
else:
    print("Wrong choice, try again...")

conn_obj.close();