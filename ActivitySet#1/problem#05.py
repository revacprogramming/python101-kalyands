# Functions


score = float(input("Enter Score: "))
if (score >= 0.9 and score < 1.0 and score > 0.0):
    print("A")
elif (score >= 0.8 and < 1.0 and score > 0.0):
    print("B")
elif (score >= 0.7 and < 1.0 and score > 0.0):
    print("C")
elif (score >= 0.6 and < 1.0 and score > 0.0):
    print("D")
elif (score < 0.6 and < 1.0 and score > 0.0):
    print("F")
elif (score > 1.0 and score < 0.0):
    print("error")