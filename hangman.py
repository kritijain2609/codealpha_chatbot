import random

# Dictionary of word categories with corresponding words
word_categories = {
    "Programming Languages": ["python", "javascript", "ruby", "java", "swift", "kotlin", "typescript"],
    "Animals": ["elephant", "tiger", "giraffe", "kangaroo", "panda", "alligator"],
    "Fruits": ["apple", "banana", "watermelon", "strawberry", "pineapple", "blueberry"],
    "Countries": ["australia", "canada", "brazil", "india", "italy", "japan", "france"],
}

# Hints for the words
word_hints = {
    "python": "A popular programming language named after a type of snake.",
    "javascript": "The programming language of the web.",
    "ruby": "A precious gemstone and a programming language.",
    "java": "A programming language and a type of coffee.",
    "swift": "Apple's programming language.",
    "kotlin": "A modern programming language for Android development.",
    "typescript": "A superset of JavaScript with static types.",
    "elephant": "The largest land animal.",
    "tiger": "A big cat known for its stripes.",
    "giraffe": "The tallest animal with a long neck.",
    "kangaroo": "An animal known for jumping and having a pouch.",
    "panda": "A bear known for its black and white color.",
    "alligator": "A large reptile found in freshwater habitats.",
    "apple": "A fruit often associated with technology companies.",
    "banana": "A long, curved fruit with yellow skin.",
    "watermelon": "A large, juicy fruit with a green rind and red flesh.",
    "strawberry": "A small, red fruit with tiny seeds on the outside.",
    "pineapple": "A tropical fruit with spiky skin and sweet, yellow flesh.",
    "blueberry": "A small, blue fruit often found in muffins.",
    "australia": "A country and continent known for kangaroos.",
    "canada": "A North American country known for maple syrup.",
    "brazil": "The largest country in South America.",
    "india": "A South Asian country with a diverse culture and large population.",
    "italy": "A European country known for pasta and pizza.",
    "japan": "An island nation in East Asia known for technology and sushi.",
    "france": "A European country famous for wine and the Eiffel Tower.",
}

def choose_category():
    categories = list(word_categories.keys())
    print("Choose a category:")
    for idx, category in enumerate(categories, 1):
        print(f"{idx}. {category}")
    choice = int(input("Enter the number of the category: ")) - 1
    return categories[choice]

def choose_word(category):
    return random.choice(word_categories[category]).lower()

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    category = choose_category()
    word_to_guess = choose_word(category)
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6
    score = 0

    print(f"\nCategory: {category}")
    print(f"Hint: {word_hints[word_to_guess]}")
    print("Welcome to Hangman!")
    print("Try to guess the word, one letter at a time.")

    while incorrect_guesses < max_incorrect_guesses:
        print(f"\nWord: {display_word(word_to_guess, guessed_letters)}")
        print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")
        print(f"Score: {score}")
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try a different letter.")
            continue

        guessed_letters.add(guess)

        if guess in word_to_guess:
            print(f"Good job! '{guess}' is in the word.")
            score += 10
            if all(letter in guessed_letters for letter in word_to_guess):
                print(f"Congratulations! You've guessed the word: {word_to_guess}")
                score += 50
                break
        else:
            incorrect_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.")
            score -= 5

    if incorrect_guesses == max_incorrect_guesses:
        print(f"Game over! The word was '{word_to_guess}'. Better luck next time!")
        score -= 20

    print(f"Your final score: {score}")

if __name__ == "__main__":
    hangman()
