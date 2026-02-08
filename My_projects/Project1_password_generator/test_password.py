
from src.generator import PasswordGenerator

gen = PasswordGenerator()


password = gen.generate(10)
print(f"{password}")
print(f"{gen.password_validator(password)}")


test_passwords = [
    "short",
    "password",
    "Password",
    "Password123",
    "Password123!",
    "StrongPass123!"
]
for pwd in test_passwords:
    print(f"\n{pwd}'")
    print(f"{gen.password_strength_analyzer(pwd)}")

try:
    pin = gen.generate_pin(4)
    print(f"   PIN: {pin}")
except ValueError as e:
    print(f"{e}")

try:
    gen.generate_pin(0)
except ValueError as e:
    print(f"{e}")