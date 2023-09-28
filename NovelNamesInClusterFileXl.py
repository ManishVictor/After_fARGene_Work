from Bio import SeqIO
########################
with open('ClusterA_report.txt','r') as f1:##############  Change filename here  ####################
    rdf1 = f1.readlines()
cluster_records = []
for i in range(1,len(rdf1)):
    cluster_records.append((rdf1[i].rstrip('\n').split('TotalGenes'))[1]+':'+(((rdf1[i].rstrip('\n')).split('_')[0])[0]).lower()+'_'+(((rdf1[i].rstrip('\n')).split('_')[0]).split('Cluster')[1]+'_'))
########################
count = 0
#print(cluster_records)
for each in SeqIO.parse('A_all_from_cluster.fasta','fasta'):############## change filename ############
    if(('sample' in each.id) or ('WW9R' in each.id)):
        count += 1
        for every in cluster_records:
            if('_'.join(each.id.split('_')[1:3])+'_' in every):
                print(every,'_'.join(each.id.split('_')[1:3])+'_',count)
                geneCount = every.split(':')[0]
        with open('FromClusterNovelNames.xls','a') as f2:
                                    ################## Change Name #####################
            f2.write(('{}\t{}\t{}\t{}\t{}\n').format(('NSF{}A').format(count),'_'.join(each.id.split('_')[1:3]),geneCount,each.id.split('_')[0],each.seq))
        with open('A_all_from_clusterNovelNames.fasta','a') as f2:
            f2.write(('>NSF{}A<{}>\n{}\n').format(count,geneCount,each.seq))##### Change Name ############
    if(('sample' not in each.id) and ('WW9R' not in each.id)):
        with open('A_all_from_clusterNovelNames.fasta','a') as f2:############# Change Name ##############
            f2.write(('>{}\n{}\n').format(each.id.split('_c_')[0],each.seq))