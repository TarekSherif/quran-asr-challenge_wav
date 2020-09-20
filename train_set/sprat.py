import  os
 
k=10

for dirname, _, filenames in os.walk('.'):
    part=len(filenames)/k
    for d in range(1,k+1):
        os.mkdir("s"+str(d))
    n=1
    index=1
    for filename in filenames:
        if index<7105:
             os.rename(dirname +"/" +filename, dirname +"/s"+ str(n) +"/"+filename)
             index+=1

        else:
            print("====================/n",n)
            index=1
            n+=1



