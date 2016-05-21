# Q28
test = 0
for i in range(n):
   for j in range(n):
      test = test + i * j

# n + n^2 + (c + n^2)
# Answer: O(n^2)

# Q29
test = 0
for i in range(n):
   test = test + 1

for j in range(n):
   test = test - 1

# x + 1 - x
# O(n)

# Q30
i = n
while i > 0:
   k = 2 + 2
   i = i // 2
# n + 1 + n / 2
# (2n + 1 ) / 2
# O(log n)
