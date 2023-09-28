import os
files = ['sample1_R12','sample2_R12','sample3_R12','sample4_R12','sample5_R12','sample6_R12','sample7_R12','sample8_R12','WW9_R12']
path = os.path.join('fargene_output','predictedGenes','predicted-orfs-amino.fasta')
for every in files:
    try:
        pathtofile = os.path.join(every,path)
        with open(pathtofile,'r') as f1:
            rdf1 = f1.readlines()
        count = 1
        for each in rdf1:
            nameoffile = (('{}').format(''.join(every.split('_'))))
            if('>' in each):
                with open(nameoffile+'.fasta','a') as f2:
                    f2.write(('>{}{}\n').format(count,nameoffile))
                count +=1
            else:
                with open(nameoffile+'.fasta','a') as f2:
                    f2.write(('{}').format(each))
    except FileNotFoundError:
        continue