import argparse, glob
from os import path

def search_file(file_path, word):
    results = 0
    try:
        opened_file =  open(file_path, "r")
    except FileNotFoundError:
        print(f"File {repr(file_path)} is not found!")
    except Exception as e:
        print(file_path, e)
    else:
        line_counter = 0
        for line in opened_file:
            line_counter += 1
            if(word in line):
                print(f"{file_path}:{line_counter}:{word} -> {repr(line)}")
                results += 1
    finally:
        if(results):
            print("="*30)

def main():
    parser = argparse.ArgumentParser(description="File searcher")
    requiredNamed = parser.add_argument_group('required named arguments')
    requiredNamed.add_argument("-f", dest="files", nargs='*', required=True)
    requiredNamed.add_argument("-w", dest="words", nargs='*', required=True)

    args = parser.parse_args()

    files = args.files
    words = args.words

    for file_path in files:
        list_of_files = glob.glob(file_path)
        for each_file in list_of_files:
            if(path.isdir(each_file)):
                continue
            for each_word in words:
                search_file(each_file, each_word)

if __name__ == "__main__":
    main()
