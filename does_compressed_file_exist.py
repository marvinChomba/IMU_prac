import sys
from pathlib import Path

def check_file(file_name):
    my_file = Path(sys.argv[1][:-4] + "-compressed.csv")
#    print(my_file)
    if my_file.is_file():
        print("True")
    else:
        print("False")


if __name__ == "__main__":
    check_file(sys.argv[1])