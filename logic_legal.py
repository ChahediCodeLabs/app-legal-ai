# logic_legal.py
import time
import google.generativeai as genai
from config import get_gemini_model

def analyser_contrat(path, mime_type, role, adverse):
    try:
        model = get_gemini_model()
        
        # 1. Envoi du fichier dans le cloud de Google
        fichier_cloud = genai.upload_file(path=path, mime_type=mime_type)
        
        # 2. Attente active (le serveur doit "lire" le PDF)
        while fichier_cloud.state.name == "PROCESSING":
            time.sleep(1)
            fichier_cloud = genai.get_file(fichier_cloud.name)

        if fichier_cloud.state.name == "FAILED": return "Erreur de lecture."

        # 3. Analyse
        prompt = f"Je suis {role} face à {adverse}. Analyse ce contrat : Synthèse, ✅ Avantages, 🚨 Pièges."
        
        return model.generate_content([prompt, fichier_cloud]).text
    except Exception as e:
        return f"Erreur : {e}"