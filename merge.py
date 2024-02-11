import mmap

from utils import timer, get_file_size


class MergeSortedFiles:
    def __init__(self):
        self.first = "first.csv"
        self.second = "second.csv"
        self.merged = "merged.csv"

    @timer
    def merge_files(self):
        with open(self.first, "r+b") as f1, open(self.second, "r+b") as f2, open(self.merged, "w+b") as f3:
            mm1 = mmap.mmap(f1.fileno(), 0)
            mm2 = mmap.mmap(f2.fileno(), 0)
            heading = mm1.readline()
            mm2.readline()
            f1_line = mm1.readline().decode("utf-8").strip()
            f2_line = mm2.readline().decode("utf-8").strip()
            f3.write(heading)
            while f1_line and f2_line:
                f1_id, f1_sentence = f1_line.strip().split(",")
                f2_id, f2_sentence = f2_line.strip().split(",")
                if int(f1_id) < int(f2_id):
                    f3.write(f"{f1_id},{f1_sentence}\n".encode("utf-8"))
                    f1_line = mm1.readline().decode("utf-8")
                else:
                    f3.write(f"{f2_id},{f2_sentence}\n".encode("utf-8"))
                    f2_line = mm2.readline().decode("utf-8")
            if f1_line:
                f1_line = f1_line.encode("utf-8")
            if f2_line:
                f2_line = f2_line.encode("utf-8")
            while f1_line:
                f3.write(f1_line)
                f1_line = mm1.readline()
            while f2_line:
                f3.write(f2_line)
                f2_line = mm2.readline()
        print(f"Sorted files ({get_file_size(self.first)}, {get_file_size(self.second)}) merged while sorting into {get_file_size(self.merged)}")


if __name__ == "__main__":
    merge_sorted_files = MergeSortedFiles()
    merge_sorted_files.merge_files()
