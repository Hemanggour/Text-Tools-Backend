import random
import string
from wsgiref.util import FileWrapper

from django.http import FileResponse
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from account.authentication import ApiKeyAuthentication
from api.ai.text_to_speech_ai import TextToSpeech
from api.ai.text_to_text_ai import TextToText


class SummarizeView(APIView):
    authentication_classes = [ApiKeyAuthentication]
    permission_classes = [IsAuthenticated]

    class SummarizePostSerializer(serializers.Serializer):
        query_text = serializers.CharField(max_length=2000, required=True)

    def post(self, *args, **kwargs):
        serializer = self.SummarizePostSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        query_text = serializer.validated_data.get("query_text")

        text_to_text_obj = TextToText()
        response = text_to_text_obj.summarize(query=query_text)

        if response is None:
            return Response({"message": "Can't generate response"}, status=502)

        return Response({"data": response}, status=200)


class ParaphaseView(APIView):
    authentication_classes = [ApiKeyAuthentication]
    permission_classes = [IsAuthenticated]

    class ParaphasePostSerializer(serializers.Serializer):
        query_text = serializers.CharField(max_length=2000, required=True)

    def post(self, *args, **kwargs):
        serializer = self.ParaphasePostSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        query_text = serializer.validated_data.get("query_text")

        text_to_text_obj = TextToText()
        response = text_to_text_obj.paraphase(query=query_text)

        if response is None:
            return Response({"message": "Can't generate response"}, status=502)

        return Response({"data": response}, status=200)


class AiReplyView(APIView):
    authentication_classes = [ApiKeyAuthentication]
    permission_classes = [IsAuthenticated]

    class AiReplyPostSerializer(serializers.Serializer):
        query_text = serializers.CharField(max_length=2000, required=True)

    def post(self, *args, **kwargs):
        serializer = self.AiReplyPostSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        query_text = serializer.validated_data.get("query_text")

        text_to_text_obj = TextToText()
        response = text_to_text_obj.ai_reply(query=query_text)

        if response is None:
            return Response({"message": "Can't generate response"}, status=502)

        return Response({"data": response}, status=200)


class GrammarCheckView(APIView):
    authentication_classes = [ApiKeyAuthentication]
    permission_classes = [IsAuthenticated]

    class GrammarCheckPostSerializer(serializers.Serializer):
        query_text = serializers.CharField(max_length=2000, required=True)

    def post(self, *args, **kwargs):
        serializer = self.GrammarCheckPostSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        query_text = serializer.validated_data.get("query_text")

        text_to_text_obj = TextToText()
        response = text_to_text_obj.grammer_check(query=query_text)

        if response is None:
            return Response({"message": "Can't generate response"}, status=502)

        return Response({"data": response}, status=200)


class TextToSpeechView(APIView):
    authentication_classes = [ApiKeyAuthentication]
    permission_classes = [IsAuthenticated]

    class TextToSpeechPostSerializer(serializers.Serializer):
        query_text = serializers.CharField(max_length=2000, required=True)
        voice = serializers.ChoiceField(
            choices=TextToSpeech.available_voices(), required=False
        )
        emotion = serializers.CharField(max_length=50, required=False)

    def post(self, *args, **kwargs):
        serializer = self.TextToSpeechPostSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        query_text = serializer.validated_data.get("query_text")
        voice = serializer.validated_data.get("voice")
        emotion = serializer.validated_data.get("emotion")

        text_to_speech_obj = TextToSpeech()
        audio_path = text_to_speech_obj.generate_audio(
            text=query_text, voice=voice, emotion=emotion
        )

        if audio_path is None:
            return Response({"message": "Can't generate audio"}, status=502)

        random_suffix = "".join(
            random.choices(string.ascii_letters + string.digits, k=5)
        )

        try:
            file = open(audio_path, "rb")
            file_response = FileResponse(
                FileWrapper(file),
                content_type="audio/mpeg",
                as_attachment=True,
                filename=f"{query_text[:10]}_{random_suffix}.mp3",
            )
            file_response["Content-Disposition"] = (
                f'attachment; filename="{query_text[:10]}_{random_suffix}.mp3"'
            )

            def cleanup():
                file.close()
                text_to_speech_obj.delete_audio()

            file_response.close = cleanup

            return file_response

        except FileNotFoundError:
            return Response({"message": "Audio file not found"}, status=404)
