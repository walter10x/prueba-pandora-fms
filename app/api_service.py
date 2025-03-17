import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import logging

class APIService:
    """
    Cliente HTTP con retries y timeout.
    Cumple con manejo de errores del PDF.
    """
    BASE_URL = "https://jsonplaceholder.typicode.com"
    
    def __init__(self):
        self.session = requests.Session()
        retries = Retry(
            total=3,
            backoff_factor=0.5,
            status_forcelist=[500, 502, 503, 504]
        )
        self.session.mount('https://', HTTPAdapter(max_retries=retries))
    
    def get_photos(self, limit: int = None) -> list:
        """Obtiene lista de fotos con límite opcional."""
        try:
            response = self.session.get(f"{self.BASE_URL}/photos", timeout=5)
            response.raise_for_status()
            return response.json()[:limit] if limit else response.json()
        except Exception as e:
            logging.error(f"Error obteniendo fotos: {str(e)}")
            return []
    
    def get_album(self, album_id: int) -> dict:
        """Obtiene un álbum por su ID."""
        try:
            response = self.session.get(f"{self.BASE_URL}/albums/{album_id}", timeout=5)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            logging.error(f"Error obteniendo álbum {album_id}: {str(e)}")
            return {"title": "Error al obtener álbum"}
