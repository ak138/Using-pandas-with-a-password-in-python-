import pandas as pd
print('Enter your name:')
name = input()
print('Hello, ' + name)

print('Enter your password:')
password = input()

dict = {'id':[1, 2, 3, 4],
        'username': ["newUser", "person", "person2", "person3"],
        'password':["123abc", "password","newpassword", "abc"]}
 
df = pd.DataFrame(dict)
if password=="123":
 print('hello, the employees that are working today are: ')
 print(df[['id','username','password']])
else:
 print('coworker working today are:')
 print(df[['id','username']])
