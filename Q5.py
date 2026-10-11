import os
import schedule
import time
import datetime

def CountFiles(Directory):
    Count = 0

    for Item in os.listdir(Directory):
        Path = os.path.join(Directory, Item)

        if os.path.isfile(Path):
            Count = Count + 1

    CurrentTime = datetime.datetime.now()

    File = open("DirectoryCountLog.txt", "a")
    File.write("Directory Path: " + Directory + "\n")
    File.write("Number of Files: " + str(Count) + "\n")
    File.write("Date and Time: " + CurrentTime.strftime("%d-%m-%Y %I:%M:%S %p") + "\n")
    File.write("------------------------------\n")
    File.close()

    print("Number of Files:", Count)
    print("Result saved in DirectoryCountLog.txt")

def main():
    Directory = input("Enter directory path: ")

    if not os.path.isdir(Directory):
        print("Directory does not exist")
        return

    CountFiles(Directory)

    schedule.every(5).minutes.do(CountFiles, Directory)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()