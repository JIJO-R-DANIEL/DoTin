from googletrans import Translator,LANGUAGES
text = "how are you"
print(Translator().detect(text))
for lang in LANGUAGES:
    l=Translator().translate(text,dest=lang)
    print(LANGUAGES[lang]+ ":"+ l.text)
