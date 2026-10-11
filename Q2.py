import schedule
import time

def DisplayMessage(message):
    print(message)

def main():
    Message = input("Enter message: ")

    schedule.every(5).seconds.do(DisplayMessage, message=Message)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()