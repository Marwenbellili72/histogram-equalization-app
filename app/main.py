from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import cv2 as cv
import numpy as np
import os

app = FastAPI()

@app.post("/histogram-equalization/")
async def histogram_equalization(image: UploadFile = File(...)):
    # Lire le fichier image téléchargé
    contents = await image.read()
    np_arr = np.frombuffer(contents, np.uint8)
    img = cv.imdecode(np_arr, cv.IMREAD_GRAYSCALE)

    # Vérifier si l'image a été correctement chargée
    if img is None:
        return {"error": "L'image n'a pas été lue correctement."}

    # Égalisation de l'histogramme
    equ_img = cv.equalizeHist(img)

    # Créer le dossier pour le fichier de résultat si nécessaire
    result_dir = "/app/static"
    if not os.path.exists(result_dir):
        os.makedirs(result_dir)

    # Enregistrer l'image modifiée sur le disque
    result_path = os.path.join(result_dir, "result.png")
    cv.imwrite(result_path, equ_img)

    # Vérifier si l'image a bien été sauvegardée
    if not os.path.exists(result_path):
        return {"error": f"Le fichier de résultat n'a pas été créé à l'emplacement {result_path}"}

    # Retourner l'image modifiée
    return FileResponse(result_path, media_type="image/png", filename="result.png")
