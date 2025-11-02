import string
import random
def check_password_strength(password):
    length_error=len(password)<8
    uppercase_error=not any(ch.isupper()for ch in password)
    lowercase_error=not any(ch.islower()for ch in password)
    digit_error=not any(ch.isdigit()for ch in password)
    special_error=not any(ch in string.punctuation for ch in password)
    feedback=[]
    if length_error:
        feedback.append("Password should be at least 8 characters long.")
    if uppercase_error:
        feedback.append("Add at least one uppercase letter.")
    if lowercase_error:
        feedback.append("Add at least one lowercase letter.")
    if digit_error:
        feedback.append("Add at least one number.")
    if special_error:
        feedback.append("Add special characters for examples(@,%,$,#,&)")
    strong=not(length_error or uppercase_error or lowercase_error or digit_error or special_error)
    return strong,feedback
def strengthen_password(password):
    if len(password) < 8:
        password+=''.join(random.choices(string.ascii_letters+string.digits+string.punctuation,k=(8-len(password))))
    if not any(ch.isupper() for ch in password):
        password+=random.choice(string.ascii_uppercase)
    if  not any(ch.islower() for ch in password):
        password += random.choice(string.ascii_lowercase)
    if not any(ch.isdigit() for ch in password):
        password += random.choice(string.digits)
    if not any(ch in string.punctuation for ch in password):
        password += random.choice(string.punctuation)
    password_list = list(password)
    random.shuffle(password_list)
    return ''.join(password_list)
user_password = input("Enter your password: ")
strong, feedback = check_password_strength(user_password)
if strong:
        print("✅Password is strong and unbreakable , Feeling Powerful🔐!")
else:
        print("⚠️ Weak password detected,Feeling nervous😰!")
        print("Suggestions:")
        for f in feedback:
            print(" -", f)
        new_password = strengthen_password(user_password)
        print("\n🔒 Suggested stronger password:", new_password)