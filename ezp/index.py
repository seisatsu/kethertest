import cgi
import cgitb
import random

cgitb.enable()

# Characters to test. Mapping of HTML escape code number to list of names.
characters = {
    '128769': ['Air'],
    '128770': ['Fire'],
    '128771': ['Earth'],
    '128772': ['Water'],
    '9800': ['Aries'],
    '9801': ['Taurus'],
    '9802': ['Gemini'],
    '9803': ['Cancer'],
    '9804': ['Leo'],
    '9805': ['Virgo'],
    '9806': ['Libra'],
    '9807': ['Scorpio', 'Scorpius'],
    '9808': ['Sagittarius'],
    '9809': ['Capricorn'],
    '9810': ['Aquarius'],
    '9811': ['Pisces'],
    '9790': ['Moon'],
    '9737': ['Sun'],
    '9791': ['Mercury'],
    '9792': ['Venus'],
    '9794': ['Mars'],
    '9795': ['Jupiter'],
    '9796': ['Saturn'],
    '9797': ['Uranus', 'Herschel'],
    '9798': ['Neptune'],
    '9738': ['Caput Draconis'],
    '9739': ['Cauda Draconis']
}

# Read page template.
with open('index.tpl', 'r') as tpl:
    body = tpl.read()

# Retrieve HTTP request fields.
fields = cgi.FieldStorage()

# Setup Question
if (not "question" in fields) or ("choice" in fields and fields["choice"].value.lower() in [char.lower() for char in characters[fields["question"].value]]):
    # None answered yet, or correct answer given.
    possible = ""
    while True:
        question = characters.keys()[random.randint(0, len(characters.keys())-1)]
        # Make sure it's a different question than the one we just answered, if applicable.
        if not "question" in fields or question != fields["question"].value:
            break
    color = "black"
    # Update winning streak.
    if "streak" in fields:
        streak = int(fields["streak"].value) + 1
    else:
        streak = 0
else:
    # Incorrect answer given.
    question = fields["question"].value
    possible = ' / '.join(characters[question])
    streak = 0
    color = "red"

# Format the template.
body = body.format(
        question=question,
        possible=possible,
        streak=streak,
        streakmarks="&#10004;&#xFE0E; "*streak,
        color=color
)

# HTTP Header.
print("Content-type: text/html; charset=utf-8\n")

# Page body.
print(body)

