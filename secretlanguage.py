import random
import string
st = input("Enter your message : ")
words = st.split(" ")
coding = input("1 for coding 0 for dicoding : ")
coding =True if (coding == "1") else False
if(coding):
    nwords =[]
    for word in words:
        if len(word)>=3:
            r1 = "".join(random.choice(string.ascii_letters) for i in range(3))
            r2 = "".join(random.choice(string.ascii_letters) for i in range(3))
            stnew = r2 + word[1:] + word[0] + r1
            nwords.append(stnew)
        else:
            r1 = "".join(random.choice(string.ascii_letters) for i in range(3))
            r2 = "".join(random.choice(string.ascii_letters) for i in range(3))
            stnew = r1+ word[::-1] + r2
            nwords.append(stnew)
    print(" ".join(nwords))
            
else:
     nwords =[]
     for word in words:
        if len(word)>=3:
            stnew = word[3 : -3]
            stnew = stnew[-1]+stnew[ : -1]
            nwords.append(stnew)
        else:
            stnew = word[3 : -3]
            stnew = stnew[::-1]
            nwords.append(stnew)
     print(" ".join(nwords))