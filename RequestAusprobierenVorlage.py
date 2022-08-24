import json
from datetime import datetime

import requests

# Lade Bild von https://www.dkriesel.com/_media/coronaplot-germany.png und speichere als coronaplot-germany.png
r = requests.get("http://2.bp.blogspot.com/-WwEPfBy3P4k/U_vUKEVly1I/AAAAAAAAEbg/eUm2cfCv7Ys/s1600/nao-robot.jpg")
with open("robo.png", "wb") as f:
    f.write(r.content)

# Lade Informationen von der Tübinger Website.
b = requests.get("https://www.tuebingen.de/")

# Untersuche sie mithilfe von den Developer-Tools (F12).
# Findest du den Link, der zum Stellencounter führt?
# (Tipp: Untersuche die einzelnen Elemente auf der Seite,
# indem du mit dem Mauszeiger über bestimmten Code-Abschnitten schwebst.)

# Füge den Link hier ein.
c = requests.get("")

with open("Stellencounter.txt", "wb") as e:
    e.write(c.content)

with open("Stellencounter.txt", "r") as h:
    fileData = h.read()
    jsonData = json.loads(fileData)
    print("Interne Stellenanzeigen: ", jsonData["intern"])

print("Auslesedatum: ", datetime.now())
