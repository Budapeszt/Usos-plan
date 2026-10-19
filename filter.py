import requests
from icalendar import Calendar

URL_USOS = "https://usosapi.panschelm.edu.pl/services/tt/upcoming_ical?lang=pl&user_id=527562&key=6xBBvp67QjQbnG9yvWyT"

def update_calendar():
    response = requests.get(URL_USOS)
    response.raise_for_status()
    oryginalny_kalendarz = Calendar.from_ical(response.content)

    nowy_kalendarz = Calendar()
    for k, v in oryginalny_kalendarz.items():
        nowy_kalendarz.add(k, v)

    for component in oryginalny_kalendarz.walk('VEVENT'):
        tytul = str(component.get('summary', ''))
        
        if "Zasady" in tytul or "Łączność" in tytul:
            continue
            
        nowy_kalendarz.add_component(component)

    with open('filtered.ics', 'wb') as f:
        f.write(nowy_kalendarz.to_ical())

if __name__ == "__main__":
    update_calendar()