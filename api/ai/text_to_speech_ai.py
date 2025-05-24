import os

from django.conf import settings
from gradio_client import Client


class TextToSpeech:
    def __init__(self):
        self.client = Client(settings.TEXT_TO_SPEECH_SRC_URL)
        self.client.output_dir = settings.TEMP_MEDIA_DIR

    @staticmethod
    def available_voices() -> list:
        voices = [
            "alloy",
            "echo",
            "fable",
            "onyx",
            "nova",
            "shimmer",
            "coral",
            "verse",
            "ballad",
            "ash",
            "sage",
            "amuch",
            "dan",
        ]
        return voices

    def delete_audio(self) -> bool:
        try:
            if os.path.exists(self.result_path):
                os.remove(self.result_path)
                return True
            else:
                return False
        except Exception as e:
            return False

    def generate_audio(
        self, text: str, voice: str = "alloy", emotion: str = "neutral"
    ) -> str | None:
        if voice not in self.available_voices():
            voice = "alloy"

        result = self.client.predict(
            prompt=text,
            voice=voice,
            emotion=emotion,
            use_random_seed=True,
            specific_seed=12345,
            api_name="/text_to_speech_app",
        )
        if not result or not isinstance(result, tuple):
            return None
        self.result_path = result[0]
        return self.result_path
