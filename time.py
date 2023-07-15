import time
from datetime import datetime
import display_library  # Hier den Namen der Display-Bibliothek einfügen

# Initialisierung des Displays
display = display_library.Display()

# Hauptprogrammschleife
while True:
    # Aktuelle Uhrzeit abrufen
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    # Uhrzeit auf dem Display anzeigen
    display.show_text(current_time)

    # Eine Sekunde warten
    time.sleep(1)