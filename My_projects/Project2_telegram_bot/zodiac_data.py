
"""
Zodiacs data.
"""

# Chinese
CHINESE_ZODIAC = [
    "🐭 Rat", "🐮 Ox", "🐯 Tiger", "🐰 Rabbit",
    "🐲 Dragon", "🐍 Snake", "🐴 Horse", "🐑 Sheep",
    "🐵 Monkey", "🐔 Rooster", "🐶 Dog", "🐷 Pig"
]

# Western
WESTERN_ZODIAC = [
    {"name": "♑ Capricorn", "start": "12-22", "end": "01-19"},
    {"name": "♒ Aquarius", "start": "01-20", "end": "02-18"},
    {"name": "♓ Fishes", "start": "02-19", "end": "03-20"},
    {"name": "♈ Aries", "start": "03-21", "end": "04-19"},
    {"name": "♉ Taurus", "start": "04-20", "end": "05-20"},
    {"name": "♊ Gemini", "start": "05-21", "end": "06-20"},
    {"name": "♋ Cancer", "start": "06-21", "end": "07-22"},
    {"name": "♌ Leo", "start": "07-23", "end": "08-22"},
    {"name": "♍ Virgo", "start": "08-23", "end": "09-22"},
    {"name": "♎ Libra", "start": "09-23", "end": "10-22"},
    {"name": "♏ Scorpio", "start": "10-23", "end": "11-21"},
    {"name": "♐ Sagittarius", "start": "11-22", "end": "12-21"},
]

def get_chinese_zodiac(year):
    """Finding chinese zodiac."""
    start_year = 1900  # 1900 - Rat year
    index = (year - start_year) % 12
    return CHINESE_ZODIAC[index]

def get_western_zodiac(month, day):
    """Finding western zodiac."""
    date = f"{month:02d}-{day:02d}"
    
    for sign in WESTERN_ZODIAC:
        if sign["name"] == "♑ Capricorn":
            if date >= "12-22" or date <= "01-19":
                return sign["name"]
        elif sign["start"] <= date <= sign["end"]:
            return sign["name"]
    
    return "❓ Unkonwn"

def get_fun_fact(chinese_sign, western_sign):
    """Chosing a random fact"""
    import random
    facts = [
        f"You combine the wisdom of a {chinese_sign} with the charisma of a {western_sign}!",
        f"{chinese_sign} and {western_sign} - a rare combination!!",
        "The stars say today is a great day for new beginnings!"
    ]
    return random.choice(facts)
