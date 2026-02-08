
import random
import string

class PasswordGenerator:
    def __init__(self):
        self.lowercase = string.ascii_lowercase  
        self.uppercase = string.ascii_uppercase  
        self.digits = string.digits              
        self.symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    def password_validator(self, password):
        if len(password) > 1:
            return True
        return False
    def generate(self, length=8):
        chars = string.ascii_letters + string.digits
        password = ''.join(random.choice(chars) for _ in range(length))
        if self.password_validator(password):
            return password
        else:
            return "Password is too short"
    def generate_pin(self, length = 4):
        if length < 1:
            raise ValueError("PIN is too short")
        pin = ''.join(random.choice(string.digits) for _ in range(length))
        return pin
    def password_strength_analyzer(self, password):
        strength_points = 0
        advise = "To make your password stronger - "
        if any(c in self.lowercase for c in password):
            strength_points += 2
        else:
            advise += "add lower case letters "
        if any(c in self.uppercase for c in password):
            strength_points += 2
        else:
            advise += "add upper case letters "
        if any(c in self.digits for c in password):
            strength_points += 2
        else:
            advise += "add digits "
        if any(c in self.symbols for c in password):
            strength_points += 2
        else:
            advise += "add special symbols "
        if len(password) >= 8:
            strength_points += 2
        else:
            advise += "add more symbols"
        if strength_points == 10:
            return f"Your password strength - {strength_points}/10 - strongest password"
        if strength_points == 8:
            return f"Your password strength - {strength_points}/10 - strong password. {advise}"
        if strength_points == 6:
            return f"Your password strength - {strength_points}/10 - medium password. {advise}"
        if strength_points == 4:
            return f"Your password strength - {strength_points}/10 - weak password. {advise}"
        if strength_points == 2:
            return f"Your password strength - {strength_points}/10 - very weak password. {advise}"