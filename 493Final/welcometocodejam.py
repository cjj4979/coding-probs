def count(s1, s2, l1, l2):
    if (l1 == 0 and l2 == 0) or l2 == 0:
        return 1

    if l1 == 0:
        return 0

    if s1[l1 - 1] == s2[l2 - 1]:
        return count(s1, s2, l1 - 1, l2 - 1) + count(s1, s2, l1 - 1, l2)
    else:
        return count(s1, s2, l1 - 1, l2)


T = int(input())
sequence = "welcome to code jam"
seq_len = len(sequence)

for caseNum in range(T):
    sentence = input()
    sen_len = len(sentence)

    num = count(sentence, sequence, sen_len, seq_len)

    num = str(num)
    if len(num) > 4:
        num = num[-4:]
    elif len(num) == 3:
        num = '0' + num
    elif len(num) == 2:
        num = '00' + num
    elif len(num) == 1:
        num = '000' + num
    print("Case #" + str(caseNum+1) + ": " + num)








# sequence = "welcome to code jam"
# T = int(input())
# for caseNum in range(T):
#     count = [0] * len(sequence)
#     sentence = input()
#     curr = 0
#     num = 1
#     for i in range(len(sentence)):
#         if sentence[i] == sequence[curr]:
#             count[curr] += 1
#
#         elif (not curr == len(sequence)-1) and (sentence[i] == sequence[curr+1]) and (not count[curr] == 0):
#             curr += 1
#             count[curr] += 1
#
#     for c in count:
#         num *= c
#     num = str(num)
#     if len(num) > 4:
#         num = num[-4:]
#     elif len(num) == 3:
#         num = '0' + num
#     elif len(num) == 2:
#         num = '00' + num
#     elif len(num) == 1:
#         num = '000' + num
#     print("Case #" + str(caseNum+1) + ": " + num)

