import matplotlib.pyplot as plt
for i in range (1,16):
    filename = 'result' + str(i) + '.txt'
    f=open(filename,'r')
    lines=f.readlines()
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
    generation=range(1,501)
    plt.plot(generation,GiverAverage)
    #plt.plot(generation,ReceiverAverage)
    #print(GiverAverage)
    #print(ReceiverAverage)
    f.close()
plt.title("Giver")
plt.ylim([0, 100])
plt.xlabel('Generation')
plt.ylabel('Cooperating Rate(%)')
plt.show()