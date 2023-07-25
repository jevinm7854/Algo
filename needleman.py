# s1=['C','A','G','C','T','A']
# d1=['C','A','C','A','T','A']
s1 = []
d1 = []
inp1 = input("Enter first sequence: ")
inp2 = input("Enter second sequence: ")

for i in inp1:
    s1.append(i)
for j in inp2:
    d1.append(j)
if len(s1) != len(d1):
    print("Will give error as sequences are not equal length. Please quit")
lens1 = len(s1) + 1
gap = int(input("Enter the gap : "))
mismatch = int(input("Enter the mismatch : "))
match = int(input("Enter the match : "))

res = [[0 for i in range(len(s1) + 1)] for j in range(len(s1) + 1)]

res[0][0] = 0
total = gap

for i in range(1, lens1):
    res[0][i] += total
    res[i][0] += total
    total += gap
    for j in range(1, lens1):
        left = (res[i][j - 1]) + gap
        top = (res[i - 1][j]) + gap
        diag = (res[i - 1][j - 1]) + mismatch
        if d1[i - 1] == s1[j - 1]:
            diag = (res[i - 1][j - 1]) + match

        res[i][j] = max(left, top, diag)


print(res)
print("The Needleman Wunsch score is ", res[-1][-1])
