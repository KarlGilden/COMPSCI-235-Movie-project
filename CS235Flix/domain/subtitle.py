class Subtitle:
    def __init__(self, language: str, transcript):
        self._language = language.strip().lower()
        self._transcript = transcript
    @property
    def language(self):
        return self._language.strip().lower()

    @language.setter
    def language(self, lang):
        self._language = lang.strip().lower()

    @property
    def transcript(self):
        return self._transcript

    @transcript.setter
    def transcript(self, script):
        self._transcript = script
        
    def __repr__(self):
        return f"<Subtitle {self._language}>"

    def __eq__(self, other):
        if not isinstance(other, Subtitle):
            return False
        return other._language == self._language

    def __hash__(self):
        return hash((self._language))