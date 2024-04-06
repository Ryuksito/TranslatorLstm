from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse


app = FastAPI()


@app.get("/download-file/{filename}")
async def download_file(filename: str):
    """
    Descarga un archivo del servidor.

    Args:
        filename: Nombre del archivo a descargar.

    Returns:
        Archivo a descargar.
    """
    file_path = filename
    return FileResponse(file_path, filename=filename)
