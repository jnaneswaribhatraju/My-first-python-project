# My First Python Project - BCA 1st Year
# After IBM Python 101 Certificate
students = ["Jnaneswari", "Ravi", "Priya"]
marks = [85, 78, 92]
print("--- Student Marks Report ---")
for i in range(len(students)):
    print(f"{students[i]} scored {marks[i]} marks")
average = sum(marks) / len(marks)
print(f"\nClass Average: {average:.2f}")
print("Great Performance!")
