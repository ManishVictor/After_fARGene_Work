from Bio import SeqIO
for each in SeqIO.parse('A_all_from_cluster.fasta','fasta'):####### Change Filename #########
    if(('sample' in each.id) or ('WW9' in each.id)):
        with open('A_RepresentativeSequences.xls','a') as f1:
            f1.write(('{}\t{}\t{}\n').format('_'.join(each.id.split('_')[1:3]),each.id.split('_')[0],each.seq))