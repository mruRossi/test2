import time
from datetime import datetime
import display_library  # Hier den Namen der Display-Bibliothek einfügen

# Initialisierung des Displays
display = display_library.Display()

# Hauptprogrammschleife
while True:
    # Aktuelle Uhrzeit und Datum abrufen
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%d.%m.%Y")

    # Uhrzeit und Datum auf dem Display anzeigen
    display.show_text(current_time + " " + current_date)

    # Eine Sekunde warten
    time.sleep(1)