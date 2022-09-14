import json
from datetime import datetime

import requests

# Lade Bild und speichere unter "Bild.png".
r = requests.get(
    "https://www.wildermuth-gymnasium.de/fileadmin/user_upload/Bilder/Geschichte/ottiliewildermuth.jpg"
)

with open("Bild.png", "wb") as f:
    f.write(r.content)

# Lade Informationen von der Tübinger Website.
b = requests.get("https://www.tuebingen.de/")

# Untersuche sie mithilfe von den Developer-Tools (F12).
# Findest du den Link, der zum Stellencounter führt?
# (Tipp: Untersuche die einzelnen Elemente auf der Seite,
# indem du mit dem Mauszeiger über bestimmten Code-Abschnitten schwebst.)

# Füge den Link hier ein.
c = requests.get("https://www.tuebingen.de/ws/stellencount")

with open("Stellencounter.txt", "wb") as e:
    e.write(c.content)

with open("Stellencounter.txt", "r") as h:
    fileData = h.read()
    jsonData = json.loads(fileData)
    print("Interne Stellenanzeigen: ", jsonData["intern"])

print("Auslesedatum: ", datetime.now())
