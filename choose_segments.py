import os
import glob
import random
import shutil

pc_path = "/home/meiying/batch_segmentation/data_demo_segmented_numbered"

for tool_name in [os.path.basename(i) for i in glob.glob(pc_path + "/*")]:
    num_cluster_counter = {}
    for num_cluster in [os.path.basename(i) for i in glob.glob(pc_path + "/" + tool_name + "/*")]:
        num_cluster_counter[num_cluster] = len([i for i in glob.glob(pc_path + "/" + tool_name + "/" + str(num_cluster) + "/*")])
        
    # choose the one with maximum number of pcs
    max_number = 0
    max_cluster = None
    for key, value in num_cluster_counter.items():
        if value > max_number:
            max_number = value
            max_cluster = key
    if max_cluster == "1":
        second_max_number = 0
        second_max_cluster = None
        for key, value in num_cluster_counter.items():
            if value > second_max_number and key != "1":
                second_max_number = value
                second_max_cluster = key
        #print "second_max_cluster: ", second_max_cluster
        #print "second_max_number: ", second_max_number
        if max_number < 3 * second_max_number:
            max_number = second_max_number
            max_cluster = second_max_cluster
    
    print tool_name
    print num_cluster_counter
    print "choose: ", max_cluster
    
    if max_cluster is not None:
        chosen_pc_path = os.path.join(pc_path, tool_name, max_cluster)
        pc_names = [i for i in glob.glob(chosen_pc_path + "/*")]
        chosen_pc = random.choice(pc_names)
        chosen_pc_name = os.path.basename(chosen_pc)
        print "chosen pc is: ", chosen_pc_name
        save_path = "/home/meiying/batch_segmentation/chosen_segmented_tools"
        # copy the file
        shutil.copy(chosen_pc, save_path)
        # rename the file
        os.rename(save_path + "/" + chosen_pc_name, save_path + "/" + tool_name + ".ply")