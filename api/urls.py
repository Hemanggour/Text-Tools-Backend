from django.urls import path

from api.views import (
    AiReplyView,
    GrammarCheckView,
    ParaphaseView,
    SummarizeView,
    TextToSpeechView,
)

urlpatterns = [
    path("summarize/", SummarizeView.as_view(), name="summarize"),
    path("paraphase/", ParaphaseView.as_view(), name="paraphase"),
    path("grammer-check/", GrammarCheckView.as_view(), name="grammer-check"),
    path("ai-reply/", AiReplyView.as_view(), name="ai-reply"),
    path("tts/", TextToSpeechView.as_view(), name="text-to-speech"),
]
