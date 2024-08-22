import sys

def is_pangram(sentence):
    return all(letter in sentence.lower() for letter in 'abcdefghijklmnopqrstuvwxyz')

if __name__ == "__main__":
    try:
        input_sentence = sys.argv[1]
        if is_pangram(input_sentence):
            print("The sentence is a pangram.")
        else:
            print("The sentence is not a pangram.")
    except IndexError:
        print("Please provide a sentence as an argument.")
    except Exception as e:
        print("An error occurred:", e)
