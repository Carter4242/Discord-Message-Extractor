import os
import csv
        
input = r"C:\Discord\Package\Path"

folder = os.path.join(input, "messages")

print(folder)

messages = 0
empty = 0
runs = 0
with open("discordMessages.txt", "w", encoding="utf8") as demo:
    for root, dirs, files in os.walk(folder):
        if ("messages.csv" in files):
            with open(os.path.join(root, "messages.csv"), 'r', encoding="utf8") as f:
                reader = csv.reader(f)
                next(reader) # Ignore first row
                for row in reader:
                    messages += 1
                    if (row[2] != ""):
                        demo.write(row[2] + "\n")
                    else:
                        empty += 1

            print (runs, messages)
            runs += 1
print(messages, empty)
