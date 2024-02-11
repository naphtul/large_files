from utils import timer, get_file_size


class MergeSortedFiles:
    def __init__(self):
        self.first = "first.csv"
        self.second = "second.csv"
        self.merged = "merged.csv"

    @timer
    def merge_files(self):
        with open(self.first, "r") as f1, open(self.second, "r") as f2, open(self.merged, "w") as f3:
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
        print(f"Sorted files ({get_file_size(self.first)}, {get_file_size(self.second)}) merged while sorting into {get_file_size(self.merged)}")


if __name__ == "__main__":
    merge_sorted_files = MergeSortedFiles()
    merge_sorted_files.merge_files()
