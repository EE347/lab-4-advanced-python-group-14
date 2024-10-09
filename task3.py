#!/usr/bin/env python3

for i in range(0,3):

    name = input("Enter a name:")
    with open("task3.txt", "a") as task3_text:
        task3_text.write(name + "\n")

task3_text.close()