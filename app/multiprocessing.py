import multiprocessing
from typing import List, Dict
from app.api_service import APIService

class MultiProcessingProcessor:
    def __init__(self):
        self.api = APIService()

    def process_photo(self, photo: Dict) -> Dict:
        album = self.api.get_album(photo['albumId'])
        return {
            "photo_id": photo['id'],
            "photo_title": photo['title'],
            "photo_url": photo['url'],
            "album_id": photo['albumId'],
            "album_title": album.get('title', 'Sin título')
        }

    def run(self, photos: List[Dict]) -> List[Dict]:
        with multiprocessing.Pool() as pool:
            return pool.map(self.process_photo, photos)
