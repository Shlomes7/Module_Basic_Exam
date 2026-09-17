def valid_ranks():
    valid_numbers = list()
    valid_numbers_count = 0
    while True:
        try:
            rank = int(input("enter a rank (1-5): "))
            if valid_numbers_count >= 10 and rank == -999:
                break
            elif rank == -999:
                print('Need at least 10 valid ranks, keep entering')
            elif rank < 1 or rank > 5:
                print('Not in range, skip')
                continue
            else:
                valid_numbers.append(rank)
                valid_numbers_count += 1
        except ValueError:
            print('Invalid input, skip')
    return valid_numbers

valid = valid_ranks()
print(f"Number of valid ranks: {len(valid)}")
print(f"Average rank: {sum(valid)/len(valid)}")
print(f"Highest rank: {max(valid)}")