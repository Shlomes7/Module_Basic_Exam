reversed_dict = dict()
while True:
    word = input('enter a string: ')
    if word == "quit":
        break
    reversed_dict[word] = word[::-1]

found = None
for w in reversed_dict:
    if reversed_dict[w] in reversed_dict:
        print("Reversed match found")
        found = True
        break
if found is None:
    print("No Reversed match found")