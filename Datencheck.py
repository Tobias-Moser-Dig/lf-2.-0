import requests

def search_lyric_text(lyric_text):
    # URL der API
    url = "http://api.chartlyrics.com/apiv1.asmx/SearchLyricText"
    
    # Parameter für die Anfrage
    params = {
        'lyricText': lyric_text  # Hier das Fragezeichen entfernen
    }
    
    # GET-Anfrage an die API senden
    print (f"Anfrage an die API: {url}?lyricText={lyric_text}")
    response = requests.get(url, params=params)
    
    # Überprüfen, ob die Anfrage erfolgreich war
    if response.status_code == 200:
        # Die Antwort im XML-Format ausgeben
        print("Antwort von der API:")
        print(response.text)
    else:
        print(f"Fehler: {response.status_code}")

def get_lyric(lyric_id, lyric_checksum):
    # URL der API
    url = "http://api.chartlyrics.com/apiv1.asmx/GetLyric"
    
    # Parameter für die Anfrage
    params = {
        'lyricId': lyric_id,
        'lyricCheckSum': lyric_checksum
    }
    
    # GET-Anfrage an die API senden
    response = requests.get(url, params=params)
    
    # Überprüfen, ob die Anfrage erfolgreich war
    if response.status_code == 200:
        # Die Antwort im XML-Format ausgeben
        print("Antwort von der API:")
        print(response.text)
    else:
        print(f"Fehler: {response.status_code}")

# Beispielaufruf der Funktion
if __name__ == "__main__":
    lyric_text = input("Gib den Text der Lyrics ein (max. 250 Zeichen): ")
    if len(lyric_text) > 0 and len(lyric_text) <= 250:
        search_lyric_text(lyric_text)
    else:
        print("Bitte gib einen gültigen Text ein.")
    
    lyric_id = input("Gib die Lyric ID ein: ")
    lyric_checksum = input("Gib die Lyric Checksum ein: ")
    
    if lyric_id and lyric_checksum:
        get_lyric(lyric_id, lyric_checksum)
    else:
        print("Bitte gib sowohl die Lyric ID als auch die Checksum ein.")
