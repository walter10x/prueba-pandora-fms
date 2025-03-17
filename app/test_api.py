from app.api_service import APIService

def test_get_photos():
    api = APIService()
    photos = api.get_photos(5)  # Pedimos 5 fotos para probar

    if not photos:
        print("❌ No se recibieron fotos.")
    else:
        print("✅ Fotos obtenidas:")
        for photo in photos:
            print(f"ID: {photo['id']} - Título: {photo['title']} - URL: {photo['url']}")

if __name__ == "__main__":
    test_get_photos()
