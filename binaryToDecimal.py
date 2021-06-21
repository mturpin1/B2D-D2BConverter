import os

def d2b():
    decimal = input("Please enter the decimal number that you want converted to binary:   ")
    os.system("cls")
    dec = int(decimal)
    byteCount = 0
    binArray = []

    if dec <= 255:
        byteCount = 8
    elif dec > 255:
        dec -= 255
        byteCount = 8
        while dec >= (2**(byteCount)):
            dec -= 2**(byteCount)
            byteCount += 1
        byteCount += 1

    byteCount = str(byteCount)

    byteNum = (int(byteCount) - 1)
    dec2 = int(decimal)
    for x in range (int(byteCount)):
        if dec2 >= (2**(byteNum)):
            print(f"2^{byteNum} >> {2**(byteNum)}")
            print(f"{dec2} greater than or equal to {2**(byteNum)}")
            dec2 -= (2**(byteNum))
            print(f"{dec2 + (2**(byteNum))} - {2**(byteNum)} >> {dec2}")
            byteNum -= 1
            binArray.append("1")
            print(str(binArray) + "\n")
        else:
            print(f"2^{byteNum} >> {2**(byteNum)}")
            print(f"{dec2} is less than {2**(byteNum)}")
            print(f"decimal remains at >> {dec2}")
            byteNum -= 1
            binArray.append("0")
            print(str(binArray) + "\n")

    arrayNum = 0
    finalAnswer = ""
    for x in range(int(byteCount)):
        finalAnswer += binArray[arrayNum]
        arrayNum += 1

    print(input(f"Final decimal to binary conversion >> {finalAnswer}"))

def b2d():
    binary = input("Please enter the binary digits that you want converted to decimal:   ")
    os.system("cls")
    print(binary)
    bin = int(binary)
    byteCount = len(binary)
    multiplier = byteCount - 1
    counter = 0
    dec = 0
    for x in range(byteCount):
        if binary[counter] == "1":
            dec += (2**multiplier)
            print(f"byte {byteCount} >> 1")
            print(f"byte {byteCount}'s value >> {2**multiplier}")
            print(f"{dec - 2**multiplier} + {2**multiplier} >> {dec}")
            multiplier -= 1
            byteCount -= 1
            counter += 1
        elif binary[counter] == "0":
            print(f"byte {byteCount} >> 0")
            print(f"{dec} + 0 >> {dec}")
            multiplier -= 1
            byteCount -= 1
            counter += 1
    print(input(f"Final binary to decimal conversion >> {dec}"))

def run():
    run = input("Please choose either decimal to binary or binary to decimal(d2b/b2d):   ").lower()
    if run == "d2b":
        d2b()
    elif run == "b2d":
        b2d()

run()

while True:
    wantContinue = input("Would you like to continue(Y/N):   ").lower()
    if wantContinue == "y":
        os.system("cls")
        run()
    else:
        exit()