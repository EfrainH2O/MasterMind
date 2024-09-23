import random as ran
import library as t
win = False
kind = 0
want = True
def main():
  global want
  global kind
  global win
  while(want):
    want = False
    win =  False
    kind = getBalls()
    correct = createRandom(kind)
    tri = [0] * kind
    output = [-1]*kind


    print ("Your will have ", kind*2, "attemps, so look out for it")
    for i in range (kind*2):
        tri = getInput(i, kind)
        output = check(tri, correct, kind)
        printR(output, kind)
        winCheck(output, kind)
        if (win):
          break
    if win:
      print("You Won, congratulations \nTry again?")
    else: 
      print(correct)
      print("You Lose \nTry again?")
    if (input("Y?")=="Y"):
      want = True
  return 0


def createRandom(kind):
    example = [0]*kind
    for i in range (kind):
        pas = True
        while pas:
            example[i]=int(ran.randrange(1,9))
            if example.count(example[i]) == 1:
                pas = False
    return example

def getInput(j, kind):
    ex = [0]*kind
    print("Attemp", j+1, ":")
    ex = input ()
    for i in range (kind):
      ex[i]= int (ex[i])
    return ex

def check(answer, base, kind):
    cancelled = [-1]*kind
    results = [-1] * kind
    for i in range (kind):
        if(base[i] == answer[i] and (cancelled.count(answer[i])==0)):
            results[i] = 1
            cancelled.append(answer[i])
        elif((base.count(answer[i])>=1 ) and (cancelled.count(answer[i])==0)):
            results[i]= 0
            cancelled.append(answer[i])
            for j in range(kind):
                if(base[j] == answer[j] and base[j] == answer[i]):
                    results[i] = 1
                    cancelled.append(answer[i])
        else:
            results[i] = -1
    return results


def printR(results, kind):
    results.sort(reverse=True)
    print("                ", end=" ")
    for i in range (kind):
        if(results[i]>=0):
            print (results[i], end=" ")
    print("\n")
    return 0
  
def winCheck(k, kind):
  global win
  for i in range (kind):
    if (k[i]!=1):
      return 0
  win = True

def getBalls():
  k = t.get_Int("Amount of balls:")
  while k > 8 or k < 3:
    k = t.get_Int("Please give a number between 3 and 8: ")
  return k

main()