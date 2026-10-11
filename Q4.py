import schedule
import time
import datetime

def CreateLog():
    CurrentTime = datetime.datetime.now()

    FileName = "MarvellousLog_" + CurrentTime.strftime("%d_%m_%Y_%H_%M_%S") + ".txt"

    File = open(FileName, "w")
    File.write("Log file created successfully.\n")
    File.write("Creation Time: " + CurrentTime.strftime("%d-%m-%Y %I:%M:%S %p"))
    File.close()

    print("Log file created:", FileName)

def main():
    CreateLog()

    schedule.every(10).minutes.do(CreateLog)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()