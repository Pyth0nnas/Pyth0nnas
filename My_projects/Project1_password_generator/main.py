from src.generator import PasswordGenerator

def show_demo():
    gen = PasswordGenerator()
    # 1. basic password
    password = gen.generate(12)
    print(f"1. - {password}")
    print(f"   strength: {gen.password_strength_analyzer(password)}")
    
    # 2. PIN
    print(f"\n2. PIN-: {gen.generate_pin(6)}")
    
    # 3. code word
    print(f"\n3. code word: {gen.generate_code_word(8)}")
    
    # 4. validation
    print(f"\n4. validator for - 'Password123': {gen.password_validator('Password123')}")
    
if __name__ == "__main__":
    show_demo()