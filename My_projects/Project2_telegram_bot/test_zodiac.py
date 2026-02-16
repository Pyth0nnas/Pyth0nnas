"""
Testing 
"""

from zodiac_data import get_chinese_zodiac, get_western_zodiac

def test_chinese_zodiac():
    print("🧪 Chinese zodiacs testing")
    print("-" * 40)
    
    test_years = [1900, 1912, 1924, 1936, 1948, 1960, 1972, 1984, 1996, 2008, 2020]
    
    for year in test_years:
        sign = get_chinese_zodiac(year)
        print(f"  {year} year: {sign}")

def test_western_zodiac():
    print("\n🧪 Western zodiacs testing")
    print("-" * 40)
    
    test_dates = [
        (1, 1, "Capricorn"),   
        (2, 14, "Aquarius"),   
        (3, 21, "Aries"),     
        (5, 15, "Taurus"),  
        (7, 4, "Cancer"),       
        (9, 10, "Virgo"),      
        (11, 30, "Sagittarius"),  
        (12, 25, "Capricorn")
    ]
    
    for month, day, expected in test_dates:
        sign = get_western_zodiac(month, day)
        status = "✅" if expected in sign else "❌"
        print(f"  {status} {day:02d}.{month:02d}: {sign} (expexted {expected})")

def test_edge_cases():
    print("\n🧪 Testing edge values")
    print("-" * 40)
    
    edge_dates = [
        (1, 19, "Capricorn"),   
        (1, 20, "Aquarius"),   
        (2, 18, "Aquarius"),  
        (2, 19, "Fishes"),      
        (3, 20, "Fishes"),      
        (3, 21, "Aries"),      
    ]
    
    for month, day, expected in edge_dates:
        sign = get_western_zodiac(month, day)
        status = "✅" if expected in sign else "❌"
        print(f"  {status} {day:02d}.{month:02d}: {sign} (expected {expected})")

def test_invalid_dates():
    print("\n🧪 Incorrect dates validation")
    print("-" * 40)
    
    invalid_dates = [
        (2, 30), 
        (4, 31), 
        (13, 1), 
        (0, 1),   
    ]
    
    from datetime import datetime
    
    for month, day in invalid_dates:
        try:
            datetime(2000, month, day)
            print(f"  ⚠️  {day:02d}.{month:02d} - expexted error, but no error")
        except ValueError:
            print(f"  ✅ {day:02d}.{month:02d} - valid error")

if __name__ == "__main__":
    print("=" * 50)
    print("🔍 Tests activated")
    print("=" * 50)
    
    test_chinese_zodiac()
    test_western_zodiac()
    test_edge_cases()
    test_invalid_dates()
    
    print("\n" + "=" * 50)
    print("✅ testing completed")
    input("\nPress enter now.")