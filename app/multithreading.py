import threading
from typing import List, Dict
from app.api_service import APIService

class MultiThreadingProcessor:
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
        results = [None] * len(photos)
        threads = []

        def worker(index: int, photo: Dict):
            results[index] = self.process_photo(photo)

        for idx, photo in enumerate(photos):
            thread = threading.Thread(target=worker, args=(idx, photo))
            thread.start()
            threads.append(thread)
            if len(threads) >= 20:  # Controlamos el número de hilos activos
                for t in threads:
                    t.join()
                threads.clear()

        for thread in threads:
            thread.join()

        return results
