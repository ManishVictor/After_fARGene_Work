# After_fARGene_Work
Post working for fARGene and clustering using usearch.
1. fargene_a_model.py : Run the program for finding the fARGenes in the samples
2. changingNamesinPredictedOrfs.py : It extracts the predicted ORFs and changes header names 
3. New_cluster_separator.py : After clustering the sequences at 70% (All the assembled predicted ORFs are first clustered at 100% uniqueness) all the fasta clustered files are extracted for representative Novel families of ARGs and a single fasta file (SFF) for further alignment and tree formation is prepared
4. ExtractingRepresentativeSequences.py : From SFF and exclusive fasta file (EFF) only having representative predicted ORFs are prepared
5. MakingExcelFromClusterDir.py : All the precticted ORFs that clustered at 100% is filtered
6. NovelNamesInClusterFileXl.py : In SFF the headers for representative predicted ORFs are changed to a suitable name as required
