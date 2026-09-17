def camel_to_hyphen(text: str) -> str:
    l1 = list(text)
    place_count = 0
    for letter in l1:
        if letter.isupper():
            l1[place_count] = letter.lower()
            l1.insert(place_count, '-')
        place_count += 1
    return ''.join(l1)

print(camel_to_hyphen('helloPython'))
print(camel_to_hyphen('myVariableName'))
print(camel_to_hyphen('python'))
print(camel_to_hyphen('aBigTest'))
