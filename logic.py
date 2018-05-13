from gtts import gTTS


class Reader():
    @classmethod
    def process(self, text):
        tts = gTTS(text=text, lang='en')
        tts.save("text_to_speech_file.mp3")
