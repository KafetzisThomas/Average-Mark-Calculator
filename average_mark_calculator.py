#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Average Mark Calculator
# Author: KafetzisThomas - https://github.com/KafetzisThomas

subjects = {}
i = 0
count = int(input("\nHow many subjects do you have? \n> "))
while i != count:
    i += 1
    for x in range(1):
        x += 1
        subject = str(input(f"\nSubject {i}: "))
        grade = float(input("Grade: "))
        subjects[subject] = grade
        print(f"Added: {subjects}")
    print("----------------------" * i)

values = subjects.values()
sum = sum(values)
total = (sum/count)
print(f"Total Grade: {total}")
