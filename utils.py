"""
Local stand-in for the DeepLearning.AI course's `utils` helper.

The course's real `utils` module only exists on their hosted platform — it
isn't a pip-installable package, which is why it throws ModuleNotFoundError
anywhere else (Colab, Kaggle, or here in VS Code).

This file gives you the same function-call style (`get_openai_api_key()`,
etc.) but reads from a local `.env` file instead, using python-dotenv.
Keep this file in the same folder as your notebook.
"""

import os
from dotenv import load_dotenv

load_dotenv()


def _get_required(var_name: str) -> str:
    value = os.getenv(var_name)
    if not value:
        raise ValueError(
            f"{var_name} not found. Make sure it's set in your .env file "
            f"in the same folder as this notebook."
        )
    return value


def get_openai_api_key() -> str:
    return _get_required("OPENAI_API_KEY")


def get_groq_api_key() -> str:
    return _get_required("GROQ_API_KEY")


def get_gemini_api_key() -> str:
    return _get_required("GEMINI_API_KEY")


def get_serper_api_key() -> str:
    return _get_required("SERPER_API_KEY")


def get_google_places_api_key() -> str:
    return _get_required("GOOGLE_PLACES_API_KEY")


def get_google_maps_api_key() -> str:
    return _get_required("GOOGLE_MAPS_API_KEY")
