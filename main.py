import pyjokes

def tell_joke(lang="en"):
    print(pyjokes.get_joke(language=lang))

if __name__ == "__main__":
<<<<<<< HEAD
    lang = input("Choisissez une langue (en, de, es, it, gl, hu): ")
    joke_type = input("Choisissezs une catégorie de blague (neutral, chuck, all): ")
=======
    lang = input("Choisissez une langue (en, de, es, it, gl, fr): ")
    joke_type = input("Choisissez une catégorie de blague (neutral, chuck, all): ")
>>>>>>> 41a7d0cda9c4c6efbb350ee077d541ff0de0b182
    tell_joke(lang, joke_type)

