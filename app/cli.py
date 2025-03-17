import typer
import time
from typing import Optional
from app.sequential import SequentialProcessor
from app.multithreading import MultiThreadingProcessor
from app.multiprocessing import MultiProcessingProcessor
from app.api_service import APIService

app = typer.Typer(help="CLI para prueba técnica Pandora FMS")

@app.command()
def main(
    mode: str = typer.Option(..., "--mode", 
        help="Modo de ejecución: secuencial|multihilos|multiprocesos"),
    photos: Optional[int] = typer.Option(   # ✅ Opcional
        None, 
        "--photos", 
        help="Límite de fotos. Si no se usa, se obtienen todas."
    )
):
    mode = mode.lower()

    if mode not in ("secuencial", "multihilos", "multiprocesos"):
        typer.secho("ERROR: Modo no válido", fg="red", err=True)
        raise typer.Exit(code=1)

    typer.echo(f"Ejecutando en modo: {mode}")

    api = APIService()
    photos_data = api.get_photos(photos)
    if not photos_data:
        typer.secho("ERROR: No se obtuvieron fotos", fg="red", err=True)
        raise typer.Exit(code=1)

    start_time = time.perf_counter()

    if mode == "secuencial":
        processor = SequentialProcessor()
        results = processor.run(photos_data)
    elif mode == "multihilos":
        processor = MultiThreadingProcessor()
        results = processor.run(photos_data)
    else:
        processor = MultiProcessingProcessor()
        results = processor.run(photos_data)

    elapsed = time.perf_counter() - start_time

    typer.echo(f"\nModo de ejecución: {mode}")
    for result in results:
        typer.echo("-" * 40)
        typer.echo(f"Foto ID: {result['photo_id']}")
        typer.echo(f"Título: {result['photo_title']}")
        typer.echo(f"URL: {result['photo_url']}")
        typer.echo(f"Álbum ID: {result['album_id']}")
        typer.echo(f"Álbum Título: {result['album_title']}")

    typer.echo("-" * 40)
    typer.echo(f"Tiempo total de ejecución: {elapsed:.3f} segundos")
