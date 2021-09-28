p = int(input("Enter the no of student in Cricket: "))
cricket = []

for i in range(p):
    x = int(input(f"Enter Roll No of students {i+1} playing Cricket: "))
    cricket.append(x)
print("Roll Nos of Students who play Cricket: ", cricket)

q = int(input("Enter the no of student in Badminton: "))
badminton = []

for i in range(q):
    y = int(input(f"Enter Roll No of student {i+1} playing Badminton: "))
    badminton.append(y)
print("Roll Nos of Students who play Badminton: ", badminton)

r = int(input("Enter the no of student in Football: "))
football = []

for i in range(r):
    z = int(input(f"Enter Roll No of student {i+1} playing Football: "))
    football.append(z)
print("Roll Nos of Students who play Football: ", football)


# students playing both cricket and badminton
inters1 = []
for i in cricket:
    for j in badminton:
        if i == j:
            inters1.append(i)
print("Students who Play both Cricket and Badminton are: ", inters1)

# students playing either cricket or badminton but not both
def union(cricket, badminton):
    res = list(cricket)
    for i in badminton:
        if i not in cricket:
            res.append(i)
    return res
print("Roll no of Students who play either Cricket or Badminton but not both: ", union(cricket, badminton))

# students playing neither cricket nor badminton
def a_not_b(cricket, badminton):
    res = list(cricket)
    for i in badminton:
        if i in res:
            res.remove(i)
        for a in res:
            return res
print("Roll no of Students who play neither cricket nor badminton:", a_not_b(a_not_b(cricket,badminton),football))

# students playing cricket and football but not badminton
def a_and_c(cricket,badminton):
  for i in cricket:
    if i not in badminton:
        a_and_c.append(i)
        for i in football:
          if i not in badminton:
            a_and_c.append(i)
print("Roll no of students who play cricket and football but not badminton: ", a_and_c)
