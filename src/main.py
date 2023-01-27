import sys

def main():
    match sys.argv[1]:
        case "--list":
            print("available scripts")
        case "--help":
            print("help text")
        case _:
            # load plugins
            # find script
            # run script
            print("Hello World!")

if __name__ == "__main__":
    main()