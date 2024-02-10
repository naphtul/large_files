import random

from nltk.corpus import words


class FileCreator:
    def __init__(self):
        self.word_bank = words.words('en')

    def create_files(self):
        counter = 1
        with open("first.csv", "w") as f1, open("second.csv", "w") as f2:
            f1.write("ID,Sentence\n")
            f2.write("ID,Sentence\n")
            for _ in range(20_000_000):
                words_per_sentence = random.randint(1, 50)
                random_file = random.choice([f1, f2])
                random_file.write(f"{counter},{self.build_sentence(words_per_sentence)}\n")
                counter += 1

    def build_sentence(self, words_per_sentence: int) -> str:
        return " ".join(random.choices(self.word_bank, k=words_per_sentence))


if __name__ == "__main__":
    file_creator = FileCreator()
    file_creator.create_files()
