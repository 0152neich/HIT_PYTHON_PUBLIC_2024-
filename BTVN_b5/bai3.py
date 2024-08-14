import random

N = int(input())
password_prefixes = ["CNTT", "KHMT", "KTPM", "HTTT"]
accounts = {}
for i in range(N):
    student_id = 2023600001 + i
    student_id = str(student_id)
    password_prefix = random.choice(password_prefixes)
    password = f"{password_prefix}{student_id}"
    accounts[f"Account{i + 1}"] = {
            "Username": student_id,
            "Password": password
        }
    
print(accounts)