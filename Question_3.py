def camel_to_hyphen(text: str) -> str:
    for l in text:
        if l.isupper():
            text.insert('-')
    return 'text'
print(camel_to_hyphen('PytHone'))
