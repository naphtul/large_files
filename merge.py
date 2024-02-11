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

            def read_chunk(file, prev_remainder="", chunk_size=10 * 1024 * 1024):  # Chunk size is set to 10 MB
                data = file.read(chunk_size)
                lines = data.split("\n")
                if prev_remainder:
                    lines[0] = prev_remainder + lines[0]
                remainder = lines.pop()
                return lines, remainder

            f1_chunk, f1_remainder = read_chunk(f1)
            f2_chunk, f2_remainder = read_chunk(f2)

            i = j = 0
            f1_id, f1_sentence = f1_chunk[i].split(",")
            f2_id, f2_sentence = f2_chunk[j].split(",")
            while f1_chunk and f2_chunk:
                if int(f1_id) < int(f2_id):
                    if i == len(f1_chunk) - 1:
                        f1_chunk, f1_remainder = read_chunk(f1, f1_remainder)
                        i = -1
                    f3.write(f"{f1_id},{f1_sentence}\n")
                    i += 1
                    if not f1_chunk: break
                    f1_id, f1_sentence = f1_chunk[i].split(",")
                else:
                    if j == len(f2_chunk) - 1:
                        f2_chunk, f2_remainder = read_chunk(f2, f2_remainder)
                        j = -1
                    f3.write(f"{f2_id},{f2_sentence}\n")
                    j += 1
                    if not f2_chunk: break
                    f2_id, f2_sentence = f2_chunk[j].split(",")

            while i < len(f1_chunk):
                f3.write(f1_chunk[i] + "\n")
                i += 1
                if not f1_chunk:
                    f1_chunk, f1_remainder = read_chunk(f1)
                    i = -1

            while j < len(f2_chunk):
                f3.write(f2_chunk[j] + "\n")
                j += 1
                if not f2_chunk:
                    f2_chunk, f2_remainder = read_chunk(f2)
                    j = -1

        print(f"Sorted files ({get_file_size(self.first)}, {get_file_size(self.second)}) merged while sorting into {get_file_size(self.merged)}")


if __name__ == "__main__":
    merge_sorted_files = MergeSortedFiles()
    merge_sorted_files.merge_files()
