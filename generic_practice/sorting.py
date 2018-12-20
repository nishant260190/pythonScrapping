x = [3,10,-100,-1000,1, 6]

for i in range(len(x)):
    mElem = x[i];
    needSwap = False;
    index = i;
    print("*********** " + str(i));
    for j in range(i+1, len(x)):
        if x[j] < mElem :
            mElem = x[j];
            needSwap = True;
            index = j;
            print(x);
            print("<<<<<< " + str(mElem));

    if needSwap :
        temp = x[i];
        x[i] = mElem;
        x[index] = temp;


print("finally")
print(x);
