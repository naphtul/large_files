import time
from os import stat

import humanize


def get_file_size(file_name: str) -> str:
    return humanize.naturalsize(stat(file_name).st_size)


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function {func.__name__} took {end - start:.4f} seconds to complete.")
        return result

    return wrapper


@timer
def compare_files(file1: str, file2: str) -> None:
    with open(file1, "r") as f1, open(file2, "r") as f2:
        f1_line = f1.readline()
        f2_line = f2.readline()
        if f1_line != f2_line:
            print(f"Files do not match at line {f1.tell()}")
            exit(1)
        while f1_line and f2_line:
            f1_line = f1.readline()
            f2_line = f2.readline()
            if f1_line != f2_line:
                print(f"Files do not match at line {f1.tell()}")
                break
        print(f"There files are identical.")


@timer
def validate_file(file: str) -> None:
    with open(file, "r") as f:
        counter = 1
        f.readline()
        for line in f:
            data = line.split(",")
            if int(data[0]) != counter:
                print(f"Error at line {counter}: {line}")
                break
            counter += 1
        print(f"There are {counter - 1} lines in the file.")


if __name__ == "__main__":
    compare_files("merged.csv", "merged_org.csv")
    validate_file("merged.csv")
