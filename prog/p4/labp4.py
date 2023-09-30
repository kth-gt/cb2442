### Your task is to finish the 'upgma' function below. You may use as much of the existing code as you please. 
### If you use all existing code, it should be enough to enter code under each "Write code here:" statement.

import numpy as np

# Replace these with your names
authors = ['A. Student', 'B. Helper']


# 'dist_matr' is set
dist_matr = np.array([[0, 0.1, 0.2, 0.3],
                      [0.1, 0, 0.2, 0.3],
                      [0.2, 0.2, 0, 0.3],
                      [0.3, 0.3, 0.3, 0]])

# 'names_list' is set
names_list = ['S1', 'S2', 'S3', 'S4']
# This allows testing the code by running the script in the terminal: $ python3 labp4.py 
# Keeping these unchanged, the output should be '(S4,(S3,(S1,S2)));' or '(S4,(S3,(S2,S1)));' or corresponding.

def upgma(dist_matr, names_list):
    # 'names_list' is copied into 'nwk_list'. To start with, 'nwk_list' will contain one sequence name per element, 
    # but it will be updated in each iteration of the while-loop below.
    nwk_list = names_list

    # 'cluster_list' is generated. This is a list of lists. Each element represents a cluster, as a list of the 
    # indices of the sequences of the cluster (0 for 'S1', 1 for 'S2', etc). To start with, each element has just one 
    # index in it, but it will be updated in each iteration of the while-loop below.
    cluster_list = []
    for i in range(len(names_list)):
        cluster_list.append([i])

    # The orginal 'dist_matr' is copied into 'updated_dist_matr'. The idea is to keep 'dist_matr' unchanged 
    # but make changes to 'updated_dist_matr' in each iteration of the while-loop below.
    updated_dist_matr = dist_matr

    # while-loop that in each iteration merges the pair of clusters with smallest average distance between objects
    # until there is only one cluster.
    while(len(cluster_list) > 1):
        ### Find the pair of clusters in 'updated_dist_matr' with the smallest distance (we call these "winning clusters"
        # in the comments below), and get their indices in 'updated_dist_matr'.
        # One way could be to go through each row / column combination of 'updated_dist_matr' with a nested for loop.
        # Write code here:


        ### Update 'cluster_list'.
        # Make a list 'in_new_cluster' by combining the lists of sequence indices (from 'cluster_list') of the two "winning clusters".
        # Write code here:


        # Remove the elements of the two "winning clusters" in 'cluster_list' (if done in two steps, it may be wise to remove 
        # the later element first, to not screw up the indexing).
        # Write code here:


        # Add the 'in_new_cluster' list as an element to the end of 'cluster_list'.
        # Write code here:


        ### Updaate 'nwk_list'.
        # Combine the two "winning clusters" of 'nwk_list' in one string, separating them with a "," and adding a "(" before 
        # and a ")" after. For example, combining 'S1' and 'S2' should give '(S1,S2)'.
        # Write code here:


        # Remove the elements of of the two "winning clusters" in 'nwk_list' (if done in two steps, it may be wise to remove 
        # the later element first, to not screw up the indexing).
        # Write code here:


        # Add the 'new_cluster_nwk' string as an element to the end of 'nwk_list'.
        # Write code here:


        ### Update 'updated_dist_matr'.
        # Remove the two rows and columns of 'updated_dist_matr' that correspond to the two "winning clusters".
        # Write code here:


        # Add a new row of zeros and a new column of zeros to the "end" of 'updated_dist_matr' (the zeros will be replaced below).
        # We've done it for you since it's a bit tricky.
        updated_dist_matr = np.append(updated_dist_matr, np.zeros((1, updated_dist_matr.shape[1])), 0) # add row with zeros to the end (bottom)
        updated_dist_matr = np.append(updated_dist_matr, np.zeros((updated_dist_matr.shape[0], 1)), 1) # add column with zeros to the end (right)
        
        # Calculate the distance between the new cluster and each other cluster, using the average method, 
        # and insert these distances in the last row and column of 'updated_dist_matr'.
        # The indices of the sequences of the new cluster are in 'in_new_cluster'. One approach could be to go through each element 
        # of 'cluster_list', except the last, to get the indices of the sequences of the other clusters, and calculate the average of 
        # these sequences' distances to the sequences of the new cluster, using the values in the original 'dist_matr'.
        # Write code here:

            
    ## After the while loop, all clusters should have been merged into one, and only one element should exist in 'nwk_list'. 
    # We convert this to a string and add a ";" to the end, to get proper Newick format. This string is then returned.
    nwk = nwk_list[0] + ';'
    return (nwk)

# Test code for the upgma function. 
# Will only be executed if this file is run directly
# e.g. by running the command "python3 labp4.py"
if __name__ == "__main__":
    nwk = upgma(dist_matr, names_list)
    print(nwk)

