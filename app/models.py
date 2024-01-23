from enum import Enum
from abc import ABC, abstractmethod

class NoteType(str, Enum):
    TEXT = "text"
    IMAGE = "image"
    AUDIO = "audio"
    LIST = "list"

class Note(ABC):
    @abstractmethod
    def __init__(self, title, date, type, done):
        self.title = title
        self.date = date
        self.type = None
        self.done = done

class NoteText(Note):
    def __init__(self, title, date, done, text=""):
        super().__init__(title, date, done)
        self.type = NoteType.TEXT
        self.text = text
                
class NoteImage(Note):
    def __init__(self, title, date, done, image=""):
        super().__init__(title, date, done)
        self.type = NoteType.IMAGE
        self.image = image
        
class NoteAudio(Note):
    def __init__(self, title, date, done, audio=""):
        super().__init__(title, date, done)
        self.type = NoteType.AUDIO
        self.audio = audio
        
class NoteList(Note):
    def __init__(self, title, date, done, list_note=None):
        super().__init__(title, date, done)
        self.type = NoteType.LIST
        if list_note is None:
            list_note = []
        self.list = list_note

