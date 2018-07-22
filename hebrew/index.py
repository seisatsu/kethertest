import cgi
import cgitb
import random

cgitb.enable()

# Characters to test. Mapping of HTML escape code number to list of names.
characters = {
    '1488': ['Alef', 'Aleph', 'A'],
    '1489': ['Bet', 'Beth', 'B'],
    '1490': ['Gimel', 'G'],
    '1491': ['Dalet', 'Daleth', 'D'],
    '1492': ['He', 'Heh', 'H', 'E'],
    '1493': ['Vav', 'Vau', 'V', 'W', 'U', 'O'],
    '1494': ['Zain', 'Zayin', 'Z'],
    '1495': ['Het', 'Cheth', 'Ch'],
    '1496': ['Tet', 'Teth', 'T'],
    '1497': ['Yod', 'Y', 'I', 'J'],
    '1498': ['Kaf Final', 'Kaph Final'],
    '1499': ['Kaf', 'Kaph', 'K'],
    '1500': ['Lamed', 'L'],
    '1501': ['Mem Final'],
    '1502': ['Mem', 'M'],
    '1503': ['Nun Final'],
    '1504': ['Nun', 'N'],
    '1505': ['Samekh', 'S'],
    '1506': ['Ayin', 'Ay', 'Au', 'O', 'Ng'],
    '1507': ['Pe Final', 'Peh Final'],
    '1508': ['Pe', 'Peh', 'P', 'Ph', 'F'],
    '1509': ['Tsadi Final', 'Tzaddi Final'],
    '1510': ['Tsadi', 'Tzaddi', 'Ts', 'Tz', 'X'],
    '1511': ['Qof', 'Qoph', 'Q'],
    '1512': ['Resh', 'R'],
    '1513': ['Shin', 'Sh'],
    '1514': ['Tav', 'Tau', 'Th', 'T']
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

