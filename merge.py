class MergeSortedFiles:
    def __init__(self):
        self.file_name = "merged.csv"

    def merge_files(self):
        with open("first.csv", "r") as f1, open("second.csv", "r") as f2, open(self.file_name, "w") as f3:
            f1.readline()
            f2.readline()
            f3.write("ID,Sentence\n")
            f1_line = f1.readline()
            f2_line = f2.readline()
            while f1_line and f2_line:
                f1_id, f1_sentence = f1_line.strip().split(",")
                f2_id, f2_sentence = f2_line.strip().split(",")
                if int(f1_id) < int(f2_id):
                    f3.write(f"{f1_id},{f1_sentence}\n")
                    f1_line = f1.readline()
                else:
                    f3.write(f"{f2_id},{f2_sentence}\n")
                    f2_line = f2.readline()
            while f1_line:
                f3.write(f1_line)
                f1_line = f1.readline()
            while f2_line:
                f3.write(f2_line)
                f2_line = f2.readline()
        print(f"Files merged into {self.file_name}")


if __name__ == "__main__":
    merge_sorted_files = MergeSortedFiles()
    merge_sorted_files.merge_files()
