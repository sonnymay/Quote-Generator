import random

# List of quotes
quotes = [
    "The only limit to our realization of the tomorrow is our doubts of today. - Franklin D. Roosevelt",
    "In the end, we will remember not the words of our enemies, but the silence of our friends. - Martin Luther King Jr.",
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "The best and most beautiful things in the world cannot be seen or even touched - they must be felt with the heart. - Helen Keller",
    "Life is really simple, but we insist on making it complicated. - Confucius",
    "In this life we cannot do great things. We can only do small things with great love. - Mother Teresa",
    "Happiness is not something ready made. It comes from your own actions. - Dalai Lama"
]

# Select a random quote
random_quote = random.choice(quotes)

# Output the selected quote
print(random_quote)
