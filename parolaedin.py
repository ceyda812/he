import random
char_pool = "ABCDEFGHIJKLMNOPRSTUVXWYZabcdefghijklmnoprstuvxwyz1234567890@-_*()/\?*!+%"
password = ""
pass_length = int(input("Lütfen şifrenizin kaç karakter uzunluğunda olması gerektiğini yazın: "))
for i in range(pass_length):
    password = password + random.choice(char_pool)
print("Your new password is:"+password)
