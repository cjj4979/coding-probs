startChars = ['b','b','c','d','d','g','g','g','g','k','k','k','n','n','n','p','p','p','t','t','u','v','w','x','y','z']
endChars = ['ah', 'ah', 'ah', 'ah', 'oh', 'oh', 'oh', 'uh'] # b,c,d,g,k,n,p,t
hard_con = ['b','c','d','g','k','n','p','t']
#[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]
sentence = input()
words = list(sentence.split())
for i, word in enumerate(words):
    words[i][0] = startChars[ord(words[i][0].lower())-97]

for i in range(len(words)):
    syllables = list(words[i].split("-"))
    for j in range(1, len(syllables)):
        for k in range(len(syllables[j])):
            if syllables[j][k] in hard_con:
                syllables[j][k] = syllables[0][0]


