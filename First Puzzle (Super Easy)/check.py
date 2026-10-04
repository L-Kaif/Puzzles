# use this to check your password


import hashlib

password = input("Enter password: ")

expected_hash = '5674991da3fa1a3efcc45ffccdaf770a7a1a6d0fa0e00a1d6eed5a979285e4bc'
input_hash = hashlib.sha256(password.encode()).hexdigest()

if input_hash == expected_hash:
    print("Correct")
else:
    print("Wrong")