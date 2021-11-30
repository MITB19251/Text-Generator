import random

f=open('data.txt','r')
data=f.read()

data=data.replace('\n',' ')
data=data.replace('\t',' ')
for character in ['-','(','—',')','“','”','[',']',':',';']:
    data = data.replace(character, '')
for character in ['.',',','!','?']:
    data = data.replace(character, ' {0} '.format(character))

sequence=data.split(' ')
sequence.remove('')
for i in range(0,len(sequence)):
    sequence[i]=sequence[i].lower()
words=list(set(sequence))
wordidx={}
for i in range(0,len(words)):
    wordidx[words[i]]=i

print()
print("Hi, I am a programmed text generator!")
print()
n=int(input("Enter k (I'll take k words into account for generation): "))
print()

states=[]
for i in range(n,len(sequence)):
    state=""
    for j in range(0,n):
        state+=sequence[(i-n)+j]
        state+=" "
    states.append(state)

states=list(set(states))
stateidx={}
for i in range(0,len(states)):
    stateidx[states[i]]=i

matrix=[]
for i in range(0,len(states)):
    L=[]
    for j in range(0,len(words)):
        L.append(0)
    matrix.append(L)

for i in range(n,len(sequence)):
    state=""
    for j in range(0,n):
        state+=sequence[(i-n)+j]
        state+=" "
    matrix[stateidx[state]][wordidx[sequence[i]]]+=1

starting=input("Enter some k words: ")
print()
print("Next 10 predicted words:")
print()
prediction=starting.split(' ')
currentState=prediction.copy()

for i in range(0,10):
    state=""
    for j in range(0,n):
        state+=currentState[j]
        state+=" "
    if state in states:
        nextWord=random.choices(words,weights=tuple(matrix[stateidx[state]]),k=1)
    else:
        nextWord=random.choice(words)
        nextWord=[nextWord]
    prediction.append(nextWord[0])
    currentState.append(nextWord[0])
    currentState.pop(0)

for i in prediction:
    print(i,end=" ")

print();print()