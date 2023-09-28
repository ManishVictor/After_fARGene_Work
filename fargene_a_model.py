import os
folder_file = '/scratch/a40540/Svalbard_Combined_Sequence/_13_svalbardCombined_files'
list_of_dir = os.listdir(folder_file)
print(sorted(list_of_dir))
working_folder = '/scratch/a40540/A'
#model_path = '/scratch/a40540/far_gene_apna_model_analysis_folder/apna_B12_model.hmm'
for each in sorted(list_of_dir):
    # moving file
    #os.system(('cp -rf {source} {destination}').format(source = os.path.join(folder_file,each),\destination = working_folder))
    os.system(('mkdir {}').format(os.path.join(working_folder,each)))
    fargene_output_folder = os.path.join(working_folder,each,'fargene_output')
    temp_dir = os.path.join(working_folder,each,'OUT_DIR/tmpdir')
    moving_result_folder = os.path.join(working_folder,each)
    print(os.listdir(os.path.join(folder_file,each)))
    fastq1,fastq2 = os.listdir(os.path.join(folder_file,each))
    #unzipping
    #os.system(('gunzip -d {} {}').format(os.path.join(working_folder,each,fastq1),os.path.join(working_folder,each,fastq2)))
    os.system(('fargene -i {in1} {in2} \
                --meta \
                --hmm-model {m_path} \
                --output {o_path} \
                --tmp-dir {t_dir} \
                --processes 99999999999 \
                --orf-finder \
                ').\
              format(in1 = os.path.join(folder_file,each,fastq1),\
                     in2 = os.path.join(folder_file,each,fastq2), \
                     m_path = 'class_a',\
                     o_path = fargene_output_folder,\
                     t_dir = temp_dir,\
                     ))
    #os.system(('mv -rf {} {}').format(moving_result_folder,'/data/prosjekt/15719-Res-Marine/fargene_apna_model/result'))
