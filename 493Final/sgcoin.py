def H(previousHash, transaction, token):
    v = previousHash
    for i in range(len(transaction)):
        # print("before" + str(v * 31 + ord(transaction[i])))
        v = (v * 31 + ord(transaction[i])) % 1000000007
    #     print("after" + str(v))
    # print("before adding token: " + str(v * 7))
    # print("before mod: " + str(v * 7 + token))
    return (v * 7 + token) % 1000000007

def getToken(previousHash, transaction):
    v = previousHash
    for i in range(len(transaction)):
        v = (v * 31 + ord(transaction[i])) % 1000000007
    val = str(v*7)
    val2 = "100000"
    if int(val) < 1000000000:
        trailing = "00"
    else:
        first = val[0]
        trailing = int(first) * 7
        trailing = str(trailing)
        if trailing == "7":
            trailing = "0" + trailing
    val2 += trailing
    # print("val: " + val)
    # print("val2: " + val2)
    # print("trailing7: " + val[-7:])
    return int(val2) - int(val[-7:])


hv1 = int(input())
transaction1 = "charlie-pays-to-eve-9-sg-coins"
token1 = getToken(hv1, transaction1) # 218216710 #
hv2 = H(hv1, transaction1, token1)
# print("hv2: " + str(hv2))
print(transaction1 + " " + str(token1))
transaction2 = "icpc-sg-2018-at-nus"
token2 = getToken(hv2, transaction2) # 620658977 #
# hv3 = H(hv2, transaction2, token2)
# print("hv3: " + str(hv3))
print(transaction2 + " " + str(token2))