import itertools

def unscramble_words(scrambled, wordlist):
    unscrambled_words = []
    for word in scrambled:
        permutations = [''.join(p) for p in itertools.permutations(word)]
        for perm in permutations:
            if perm in wordlist:
                unscrambled_words.append(perm)
    return unscrambled_words

def main():
  
    with open('scrambled.txt', 'r') as file:
        scrambled = file.read().splitlines()

    
    with open('wordlist.txt', 'r') as file:
        wordlist = set(file.read().splitlines())

    unscrambled_words = unscramble_words(scrambled, wordlist)

    
    valid_words = [word for word in unscrambled_words if word in wordlist]

    for word in valid_words:
        print(word)

if __name__ == '__main__':
    main()