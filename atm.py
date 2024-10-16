import sqlite3
con = sqlite3.connect("atm.db")
cursor = con.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS atm(email TEXT,name TEXT,password TEXT,bal INT)
            ''')
con.commit()
def create_account(email,password,name,bal = 100):
    cursor.execute("SELECT * FROM atm WHERE email = ?",(email,))
    acc = cursor.fetchone()
    if acc:
        print(f"Oops! An account already exists under the name {acc[1]} with email {acc[0]}. Your current balance is {acc[3]}.")
    else:
        cursor.execute("INSERT INTO atm(email,password,name,bal) VALUES (?,?,?,?)",(email,password,name,bal))
        print(f"🎉 Congratulations, {name}! Your account has been successfully created with a balance of {bal}.")
    con.commit()
def check_account(email):
        cursor.execute("SELECT * FROM atm WHERE email = ?",(email,))
        acc = cursor.fetchone()
        if acc:
            print(f"Account found! 📝\nName: {acc[1]}\nEmail: {acc[0]}\nPassword: {acc[2]}\nBalance: ₹{acc[3]}")
        else:
            print("❌ No account found with this email.")
def debit(email):
    cursor.execute("SELECT * FROM atm WHERE email = ?",(email,))
    acc = cursor.fetchone()
    if acc:
        deb = int(input("💸 How much would you like to withdraw? "))
        if deb <= 0:
            print("Please Provide Positive Number!")
        elif deb > acc[3]:
            print("❌ You don't have enough balance! Transaction failed.")
        else:
            new_bal = acc[3] - deb
            cursor.execute("UPDATE atm SET bal = ? WHERE email = ?",(new_bal,email))
            print(f"✔️ Transaction successful! You have withdrawn {deb}. Your new balance is {new_bal}.")
        con.commit()
    else:
        print("❌ Account not found.")
def credit(email):
        cursor.execute("SELECT * FROM atm WHERE email = ?",(email,))
        acc = cursor.fetchone()
        if acc:
            bal = int(input("how many money do you want to credit: "))
            if bal <= 0:
                print("Please Provide Positive Number!")
            else:
                new_bal = acc[3] + bal
                cursor.execute("UPDATE atm SET bal = ? WHERE email = ?",(new_bal,email))
                con.commit()
                print(f"✔️ Transaction successful! You have deposited {bal}. Your new balance is {new_bal}.")
        else:
            print("don't have any account")
print("Welcome to the ATM system! 🏦\nPlease select an option:")
print("1. 🆕 Create a new account (L for Login)")
print("2. 🔍 Check account details (C for Check Account)")
print("3. ➕ Deposit money (credit)")
print("4. ➖ Withdraw money (debit)")
choice = input("Enter your choice: ").lower()
email = input("📧 Enter your email: ")
name = input("👤 Enter your name: ")
password = input("🔑 Enter your password: ")

if choice == "l":
    create_account(email, password, name)
elif choice == "c":
    check_account(email)
elif choice == "credit":
    credit(email)
elif choice == "debit":
    debit(email)
else:
    print("❌ Invalid choice! Please try again.")
