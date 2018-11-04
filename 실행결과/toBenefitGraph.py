import matplotlib.pyplot as plt
for i in range (1,15):
    filename = 'result' + str(i) + '.txt'
    f=open(filename,'r')
    lines=f.readlines()
    GiverBenefit=[]
    ReceiverBenefit=[]
    GiverAverage=[]
    ReceiverAverage=[]
    for line in lines:
        if line[0] != '(':
            continue
        for i in range(len(line)):
            if line[i] == ":" and i<25:
                i+=1
                string=""
                while(line[i]!='%'):
                    string=string+line[i]
                    i+=1
                avg=float(string)
                GiverAverage.append(avg)
            if line[i] == ":" and i>25:
                i+=1
                string=""
                while(line[i]!='%'):
                    string=string+line[i]
                    i+=1
                avg=float(string)
                ReceiverAverage.append(avg)
    for line in lines:
        if line[0] != 'G':
            continue
        for i in range(len(line)):
            if line[i] == ":" and i<30:
                i+=2
                string=""
                while(line[i]!=' '):
                    string=string+line[i]
                    i+=1
                avg=float(string)
                GiverBenefit.append(avg)
            if line[i] == ":" and i>30:
                i+=2
                string=""
                while(line[i]!=' '):
                    string=string+line[i]
                    i+=1
                avg=float(string)
                ReceiverBenefit.append(avg)
    generation=range(1,501)
    #plt.plot(generation,GiverBenefit)
    #plt.plot(generation,ReceiverBenefit)
    #print(GiverAverage)
    #print(ReceiverAverage)
    f.close()
    plt.scatter(x=ReceiverAverage,y=ReceiverBenefit,linewidth=0.01)
plt.title("Benefit-Cooperating Rate Relationship")
#plt.xlabel("Giver's cooperating rates(%)")
plt.xlabel("Receiver's cooperating rates(%)")
#plt.ylabel("Giver's Benefit(KRW)")
plt.ylabel("Receiver's Benefit(KRW)")

plt.show()
