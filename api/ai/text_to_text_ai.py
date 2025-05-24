from django.conf import settings
from langchain_google_genai import ChatGoogleGenerativeAI


class TextToText:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(model=settings.GOOGLE_GEMINI_MODEL)

    def __generate(self, prompt):
        try:
            response = self.llm.invoke(prompt)
            return response.content
        except Exception as err:
            return None

    def summarize(self, query) -> str | None:
        prompt = f"""summarize this text: ```{query}```"""
        text_response = self.__generate(prompt=prompt)
        return text_response

    def paraphase(self, query) -> str | None:
        prompt = f"""paraphase this text: ```{query}```"""
        text_response = self.__generate(prompt=prompt)
        return text_response

    def ai_reply(self, query) -> str | None:
        prompt = f"""reply to this text: ```{query}```"""
        text_response = self.__generate(prompt=prompt)
        return text_response

    def grammer_check(self, query) -> str | None:
        prompt = f"""check grammer in this text: ```{query}```"""
        text_response = self.__generate(prompt=prompt)
        return text_response
