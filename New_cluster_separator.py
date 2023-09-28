'''
This program is extracting the sequences from the cluster. If it finds that a cluster file has
known sequence amongst other unknown sequences, it will only extract the known sequence as a
representative sequence.
'''
import os
from Bio import SeqIO
all_names = []
# with open('centoids_at_1_ncbi_b3.fasta','r') as f1:
#     amr_reads = f1.readlines()
with open('negatives_db.fasta','r') as f2:
    fanny_reads = f2.readlines()
# for amrnames in amr_reads:
#     if('>' in amrnames):
#         headeramr = amrnames.rstrip('\n').lstrip('>')
#         all_names.append(headeramr)
#print(all_names)
for fannynames in fanny_reads:
    if('>' in fannynames):
        headerfanny = fannynames.rstrip('\n').lstrip('>')
        all_names.append(headerfanny)
cluster = sorted(os.listdir('cluster_dir'))
#print(cluster)
final_cluster = []
for every in cluster:
    cluster_list = []
    with open('cluster_dir/'+every,'r') as f3:
        rd_f3 = f3.readlines()
    for lines in rd_f3:
        if('>' in lines):
            header = lines.lstrip('>').rstrip('\n')
            cluster_list.append(header)
    for genes in all_names:
        if(genes not in cluster_list):
            flag = 1
        else:
            flag = 0
            break
    if(flag == 1):
        final_cluster.append(every)
#print(final_cluster)
our_cluster = []
with open ('ClusterA_report.txt','a') as clr: ############################## FileName chnage
    clr.write('*** Clusters having only Fargene ***\n')
for clust in final_cluster:
    #print(clust)
    (os.system(("grep -c '>' cluster_dir/{} > size.txt").format(clust)))
    #print(size.txt)
    with open('size.txt','r') as f4:
        rd_f4 = f4.readlines()
    size = rd_f4[0].rstrip('\n')
    os.system('rm -rf size.txt')
    with open ('ClusterA_report.txt','a') as clr:################################ Filename Change 
        clr.write(('{}_TotalGenes{}\n').format('Cluster'+clust.split('_')[1],size))
    print(('{}_TotalGenes{}').format('Cluster'+clust.split('_')[1],size))
    our_cluster.append(clust)
print(len(final_cluster))
header_flagg = 0
counter = 0
for seqclust in cluster:#final_cluster:
    cluster_sequence_header = []
    cluster_sequence = []
    count = 0
    seq_names = []
    with open('cluster_dir/'+seqclust,'r') as f5:
        rd_f5 = f5.readlines()
    for eachline in rd_f5:
        header = eachline.rstrip('\n').lstrip('>')
        cluster_sequence_header.append(header)
    for cluster_header in cluster_sequence_header:
        if(cluster_header in all_names):
            Header = cluster_header.rstrip('\n')
            header_flagg = 1
            break
        else:
            header_flagg = 0
    if(header_flagg == 0):
        Header = cluster_sequence_header[0].rstrip('\n')
    #print('*'+Header+'\n*')
    #print(seqclust,Header)
    for seq_record in SeqIO.parse('cluster_dir/'+seqclust,'fasta'):
        #print(seqclust)
#         print(seq_record.id+'++++++++++'+seq_record.description)
        if(Header == seq_record.description):
#             print(Header,seqclust)
            counter+=1
            with open('A_all_from_cluster.fasta','a') as f6:################################ Filename Change
                f6.write('>'+seq_record.description+'_'+seqclust+'_cluster'+'\n'+str(seq_record.seq)+'\n')
#print(counter)
