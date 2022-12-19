import os

if __name__ == "__main__":
    fileCounter = 0
    for root, dirs, files in os.walk("Linux_Challenge"):
        for file in files:    
            if file.endswith('.txt') and "Meta" in file:
                fileCounter += 1

    print(fileCounter)