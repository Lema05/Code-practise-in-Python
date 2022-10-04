lettersA = {"A", "B", "C", "D"}
lettersB = {"E", "B", "D", "H"}

#print(lettersA | lettersB)
union = lettersA | lettersB
intersection = lettersA & lettersB
difference =lettersA - lettersB
print(f"union ={union}")
print(f"intersection = {intersection}")
print(f"difference = {difference}")
