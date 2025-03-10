import pyjokes

def tell_joke(lang="en"):
    print(pyjokes.get_joke(language=lang))

if __name__ == "__main__":
    lang = input("Choisissez une langue (en, de, es, it, gl, hu): ")
    joke_type = input("Choisissezs une catégorie de blague (neutral, chuck, all): ")
    tell_joke(lang, joke_type)

