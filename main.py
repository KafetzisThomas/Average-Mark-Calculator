#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Project Title: Average-Mark-Calculator (https://github.com/KafetzisThomas/Average-Mark-Calculator)
# Author / Project Owner: KafetzisThomas (https://github.com/KafetzisThomas)

def get_subject_grades(**subjects):
    """Return a dict of subjects associated with grades"""
    count = int(input("\nHow many subjects do you have?\n> "))
    for i in range(count):
        subject = str(input(f"\nSubject {i+1}: "))
        grade = float(input("Grade: "))
        subjects[subject] = grade
        print(f"Added: {subject}")

    return subjects

def calculate_average_grade(subjects):
    """Return average grade by dividing the sum of grades"""
    values = subjects.values()
    total = sum(values) / len(values)
    return total


subjects = get_subject_grades()
average_grade = calculate_average_grade(subjects)
print(f"\nAverage grade: {average_grade:.1f}")
