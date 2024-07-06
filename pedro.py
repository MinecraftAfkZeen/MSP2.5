import requests
import time

def keep_url_open(url):
    try:
        while True:
            response = requests.get(url)
            print(f"Status code: {response.status_code}")
            time.sleep(5)  # Espera 10 segundos antes de hacer la siguiente solicitud
    except KeyboardInterrupt:
        print("\nPrograma interrumpido.")
    except requests.RequestException as e:
        print(f"Error en la solicitud: {e}")

if __name__ == "__main__":
    url = "https://reimagined-giggle-x59p6w9vw57v36p67.github.dev/"  # Aquí debes poner la URL que quieres mantener abierta
    keep_url_open(url)