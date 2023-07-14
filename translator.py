import json
import os
from deep_translator import MyMemoryTranslator


def englishToFrench(englishText):
    frenchText = MyMemoryTranslator(
        source='en-US', target='fr-FR').translate(englishText)
    print(frenchText)
    return frenchText


def frenchToEnglish(frenchText):
    englishText = MyMemoryTranslator(
        source='fr-FR', target='en-US').translate(frenchText)
    print(englishText)
    return englishText


if __name__ == "__main__":
    englishToFrench("Hi")
    frenchToEnglish("Salut")
    print(englishToFrench("Hi") == "Salut")
