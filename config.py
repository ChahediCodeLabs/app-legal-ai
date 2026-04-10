import os
import google.generativeai as genai
from dotenv import load_dotenv

def get_gemini_model(model_version='gemini-2.5-flash'):
    """
    Charge la clé API, configure Gemini et retourne l'objet modèle prêt à l'emploi.
    """
    # 1. Chargement des variables d'environnement
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("❌ Erreur : La clé GEMINI_API_KEY est introuvable dans le fichier .env")

    # 2. Configuration globale
    genai.configure(api_key=api_key)

    # 3. Retourne le modèle configuré
    return genai.GenerativeModel(model_version)