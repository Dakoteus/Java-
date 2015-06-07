import time
def CoffeeTime(time):
    if ":" not in time:
		return int(time)
    else:
        part = time.split(':')
        return int(part[0]) * 60 + int(part[1])

def cooking(seconds, a):
    print(a + " is brewing.")

    time.sleep(.5)
    for x in range(seconds):
        print("shshshscscsch")
        time.sleep(.5)
        print(seconds - x)
        time.sleep(.5)
    for x in range(5):
        time.sleep(.5)
        print("CHCHHCHCSSHSHSCSH")
        time.sleep(.5)
    time.sleep(.5)
    print("Your coffee is done!")
def main():
    cooking(CoffeeTime(raw_input("How long?")), "Coffee")
main()
