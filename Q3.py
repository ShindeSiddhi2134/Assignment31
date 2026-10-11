import os
import schedule
import time
import datetime

def ScanDirectory(Directory):
    Files = 0
    Directories = 0

    for Item in os.listdir(Directory):
        Path = os.path.join(Directory, Item)

        if os.path.isfile(Path):
            Files = Files + 1
        elif os.path.isdir(Path):
            Directories = Directories + 1

    CurrentTime = datetime.datetime.now()

    print("Directory Scanned:", Directory)
    print("Total Files:", Files)
    print("Total Subdirectories:", Directories)
    print("Scan Time:", CurrentTime.strftime("%d-%m-%Y %I:%M:%S %p"))
    print("--------------------------------")

def main():
    Directory = input("Enter directory path: ")

    if not os.path.isdir(Directory):
        print("Directory does not exist")
        return

    ScanDirectory(Directory)

    schedule.every(1).minutes.do(ScanDirectory, Directory)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()