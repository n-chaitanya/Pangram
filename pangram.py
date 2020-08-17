l = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
q = []
sentence = eval(input("Enter a String"))
sentence.lower()
print(sentence)
split = sentence.split()
for i in l:
    if(i in sentence):
        q.append(i)
print(l)
print(q)
if(q == l):
    print("It is a pangram")
else:
    print("It is not a pangram")

