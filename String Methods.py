username = input("Enter your username :")

if len(username) > 14:
  print("your username cant contain more than 14 characters.")

elif not username.find(" ") == -1:
  print("your username cant contain spaces.")
  
elif not username.isalpha():
 print("your username cant contain numbers.")

else:
 print(f"welcome {username}")