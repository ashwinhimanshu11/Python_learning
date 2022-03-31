from gettext import translation


def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "A"
            else:
                translation = translation + "a"
        else:
            translation = translation + letter
    return translation

print(translate(input("enter a phrase: ")))