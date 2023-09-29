from Bio import SeqIO
import os 
with open('classA_BLDB_raw.csv','r') as f1:##############  Change filename here  ####################
    rdf1 = f1.readlines()
ncbirecords = []
for i in range(len(rdf1)):
    ncbirecords.append(rdf1[i].rstrip('\n'))
print(ncbirecords)
for each in SeqIO.parse('A_all_from_clusterNovelNamesOutgroup.fasta','fasta'):
    flag = 0
    recseq = each
    for every in ncbirecords:
        if(each.id.split('.')[0] in every):
            flag = 1
            rec = every
            recseq = each
            break
    if(flag == 1):
        with open('A_all_from_clusterFinalOutgroup.fasta','a') as f2:
            f2.write(('>{}\n{}\n').format(rec.split(';')[0],recseq.seq))
    if(flag == 0):
        with open('A_all_from_clusterFinalOutgroup.fasta','a') as f2:
            f2.write(('>{}\n{}\n').format(recseq.id,recseq.seq))
