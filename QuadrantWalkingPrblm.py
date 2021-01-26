n = 5

c = "R"
x = 0
y = 0
distance = 10

while(n):
  if c == "R":
    x = x + distance
    distance += 10
    c = "U"
  
    
  elif c == "U":
    y = y + distance
    distance +=10
    c = "L"
  
  elif c == "L":
    x = x - distance
    distance+=10
    c = "D"
  
    
  elif c == "D":
    y = y - distance
    distance +=10
    c = "A"
  
    
  elif c == "A":
    x = x + distance
    distance += 10
    c = "R"  
    
  n -=1


print(f"({x},{y})")  



