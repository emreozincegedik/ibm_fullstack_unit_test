from translator import frenchToEnglish

from translator import englishToFrench

assert frenchToEnglish("Salut") == "Hi"
assert frenchToEnglish("Au revoir") != "Hi"

assert englishToFrench("Hi") == "Salut"
assert englishToFrench("Bye") != "Salut"
print("All tests passed")
