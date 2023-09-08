#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Average Mark Calculator
# Author: KafetzisThomas - https://github.com/KafetzisThomas

subjects = {}
count = int(input("\nHow many subjects do you have?\n> "))

i = 0
while i != count:
  i += 1
  subject = str(input(f"\nSubject {i}: "))
  grade = float(input("Grade: "))
  subjects[subject] = grade
  print(f"Added: {subject}")

values = subjects.values()
total = sum(values) / count
print(f"\nAverage grade: {total}")
