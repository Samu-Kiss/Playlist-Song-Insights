import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Configuración de credenciales usando las variables de entorno
client_id = os.getenv('SPOTIPY_CLIENT_ID')
client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')
redirect_uri = os.getenv('SPOTIPY_REDIRECT_URI')
username = os.getenv('SPOTIPY_USERNAME')

scope = 'playlist-read-private'

# Obtén el token de acceso
username = 'tu5psekd3enzvn9azm3cbgcxa'
token = util.prompt_for_user_token(username, scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)

# Crea un objeto de la API de Spotify
sp = spotipy.Spotify(auth=token)


# Diccionario para mapear los números de tonalidades a cifrado americano
tonalidades = {
    0: 'C', 1: 'C#', 2: 'D', 3: 'D#', 4: 'E', 5: 'F', 6: 'F#', 7: 'G', 8: 'G#', 9: 'A', 10: 'A#', 11: 'B'
}

# Obtiene las playlists del usuario
if token:
    playlists = sp.user_playlists(username)
    print("Selecciona una playlist:")
    for i, playlist in enumerate(playlists['items']):
        print(f"{i+1}. {playlist['name']}")
    
    selected_index = int(input("Ingresa el número de la playlist: ")) - 1
    
    if selected_index < 0 or selected_index >= len(playlists['items']):
        print("Índice de playlist no válido.")
    else:
        selected_playlist_name = playlists['items'][selected_index]['name']
        selected_playlist_id = playlists['items'][selected_index]['id']
        print(f"\nObteniendo información de las canciones de '{selected_playlist_name}'...\n")
        
        # Obtiene la información de la playlist
        playlist_info = sp.playlist(selected_playlist_id)
        total_tracks = playlist_info['tracks']['total']  # Cantidad total de canciones en la playlist
        
        # Crear un nuevo archivo de Excel
        wb = Workbook()
        ws = wb.active
        ws.title = selected_playlist_name
        
        # Encabezados de las columnas
        ws.append(["Artista", "Canción", "Álbum", "BPM", "Tonalidad", "Modo"])
        
        # Obtiene todas las canciones de la playlist seleccionada (manejo de paginación)
        offset = 0
        track_number = 1  # Inicializa el contador de canciones
        pbar = tqdm(total=total_tracks, desc="Procesando", unit="canción")
        while True:
            playlist_tracks = sp.playlist_tracks(selected_playlist_id, offset=offset)
            for item in playlist_tracks['items']:
                track_info = item['track']
                artist_name = track_info['artists'][0]['name']
                track_name = track_info['name']
                album_name = track_info['album']['name']  # Nombre del álbum
                track_id = track_info['id']
                
                # Obtiene el análisis de audio para la canción
                audio_features = sp.audio_features(track_id)
                if audio_features:
                    bpm = round(audio_features[0]['tempo'])  # Redondea el tempo al entero más cercano
                    key_num = audio_features[0]['key']
                    mode = audio_features[0]['mode']
                    key_str = tonalidades[key_num]  # Convierte el número de tonalidad a cifrado americano
                    mode_str = "Menor" if mode == 0 else "Mayor"
                    
                    # Agrega la información al archivo de Excel
                    ws.append([artist_name, track_name, album_name, bpm, f"{key_str} {mode_str}"])
                    track_number += 1  # Incrementa el contador de canciones
                    pbar.update(1)  # Actualiza la barra de progreso
                else:
                    print(f"{track_number}. {artist_name} - {track_name} | No se pudo obtener información de análisis de audio")
                    track_number += 1  # Incrementa el contador de canciones
                    pbar.update(1)  # Actualiza la barra de progreso
            
            # Verifica si hay más resultados y actualiza el offset
            if playlist_tracks['next']:
                offset += len(playlist_tracks['items'])
            else:
                break
        
        # Cierra la barra de progreso
        pbar.close()
        
        # Guardar el archivo Excel con el nombre de la playlist y la fecha actual
        date_string = datetime.now().strftime("%d-%m-%Y")
        excel_filename = f"{selected_playlist_name}_{date_string}.xlsx"
        wb.save(excel_filename)
        print(f"\nSe ha creado el archivo '{excel_filename}' con la información de la playlist.")
else:
    print("No se pudo obtener el token de acceso")