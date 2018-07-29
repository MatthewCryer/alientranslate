with open("D:/GitHome/A-large-practice.in") as f: #opens the input file
    content = f.readlines() #returns a list of each line of the inout file

def trans(caseno, alien_number, source_language, target_language):
    bs = len(source_language)
    bt = len(target_language)
    #print (("Case #%s: bs is %s, bt is %s") % (str(caseno + 1), bs, bt))
    sdict = dict()
    for idx,j in enumerate(source_language): #dictionary links the the jth element in the source_language to it's binary counterpart
        sdict[j] = idx
    count = 0
    total = 0
    for i in alien_number:
        count += 1
        total += ((bs**((len(alien_number) - count))) * sdict[i]) #gives a total binary value of the target number, count keeps the base index correct
    #print (("Case #%s: total being aimed for in decimal is %s") % (str(caseno + 1), total))
    tdict = dict()
    for idx,j in enumerate(target_language): #reversed as need to pull values, not read them, i.e. links binary counterpart (key) to target digits
        tdict[idx] = j
    nod = 0
    while (bt ** nod) <= total: #determines the total number of digits in the output
        nod += 1
    #print (("Case #%s: number of digits in target number is %s") % (str(caseno + 1), nod))
    output = []
    for x in list(reversed(range(nod))):# cycles through with the highest base index first
        output.append(tdict[total//(bt**x)]) #appends the target digit number of base**indexes required at the first posn
        total = total - ((total//(bt**x)) * (bt**x)) #gives a new target total to start with the new base index
    outputstring = ""
    for i in range(len(output)):
        outputstring += str(output[i]) #appends each outpout digit as a string
    with open("D:/GitHome/A-large-practice-solution.in", 'a') as g: #opens an output file in append mode so doesn't rewrite each time
        print (("Case #%s: %s") % (str(caseno + 1), outputstring), file = g) #prints directly to g

data = []
for idx,i in enumerate(content):
    data.append([idx, i.split( )[0], i.split( )[1], i.split( )[2]])

for i in range(len(data)):
    trans(data[i][0], data[i][1], data[i][2], data[i][3])
