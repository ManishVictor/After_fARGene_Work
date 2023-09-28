from Bio import SeqIO
import os 
with open('ClusterA_report.txt','r') as f1:##############  Change filename here  ####################
    rdf1 = f1.readlines()
cluster_records = []
for i in range(1,len(rdf1)):
    cluster_records.append((((rdf1[i].rstrip('\n')).split('_')[0])[0]).lower()+'_'+(((rdf1[i].rstrip('\n')).split('_')[0]).split('Cluster')[1]))
for record in cluster_records:
    cluster_file = os.path.join('cluster_dir',record)
    for each in SeqIO.parse(cluster_file,'fasta'):
        with open('A_SequencesFromCluster.xls','a')as f3:############### Change Filename here ###############
            f3.write(('{}\t{}\t{}\n').format(record,each.id,each.seq))