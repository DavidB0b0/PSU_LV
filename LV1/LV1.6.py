
def load_messages(filename):
    ham_messages = []
    spam_messages = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            label, message = line.strip().split('\t')
            if label == 'ham':
                ham_messages.append(message)
            elif label == 'spam':
                spam_messages.append(message)
    return ham_messages, spam_messages

def average_words_per_message(messages):
    total_words = sum(len(message.split()) for message in messages)
    return total_words / len(messages)

def count_exclamation(messages):
    count = sum(message.endswith('!') for message in messages)
    return count

def main():
    filename = 'SMSSpamCollection.txt'
    ham_messages, spam_messages = load_messages(filename)

    avg_words_ham = average_words_per_message(ham_messages)
    avg_words_spam = average_words_per_message(spam_messages)

    print("Prosjeèan broj rijeèi u ham porukama:", avg_words_ham)
    print("Prosjeèan broj rijeèi u spam porukama:", avg_words_spam)

    spam_with_exclamation = count_exclamation(spam_messages)
    print("Broj spam poruka koje završavaju uskliènikom:", spam_with_exclamation)

