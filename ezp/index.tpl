<!doctype html>
<html>
<head>
    <title>KetherTest - Elements, Zodiac, and Planets</title>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <table>
        <tr>
            <td style="width: 400px; text-align: center;">
                <div id="question" style="font-family: symbola; font-size: 20em; color: {color};">&#{question};&#xFE0E;</div>
                <div id="possible" style="font-size: 2em; color: red;">{possible}</div>
            </td>
            <td>
                <form action="index.py" method="post">
                    <span style="color: green;">{streakmarks}</span><br>
                    <input type="text" name="choice" value=""><br>
                    <input type="hidden" name="question" value="{question}">
                    <input type="hidden" name="streak" value="{streak}">
                    <input type="submit" value="Check">
                </form>
            </td>
        </tr>
    </table>
</body>

