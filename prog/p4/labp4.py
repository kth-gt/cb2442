### Your task is to finish the 'upgma' function below. You may use as much of the existing code as you please. 
### If you use all existing code, it should be enough to enter code under each "Write code here:" statement.

import numpy as np


# Replace these with your names:
authors = ['A. Student', 'B. Helper']


# 'dist_matr' is set. This is a 2-dimensional NumPy array
dist_matr = np.array([[0, 0.1, 0.2, 0.3],
                      [0.1, 0, 0.2, 0.3],
                      [0.2, 0.2, 0, 0.3],
                      [0.3, 0.3, 0.3, 0]])

# 'names_list' is set
names_list = ['S1', 'S2', 'S3', 'S4']
# This allows testing the code by running the script in the terminal: $ python3 labp4.py 
# Keeping these unchanged, the output should be '(S4,(S3,(S1,S2)));' or '(S4,(S3,(S2,S1)));' or corresponding.

def upgma(dist_matr, names_list, print_details):
    # 'names_list' is copied into 'nwk_list'. To start with, 'nwk_list' will contain one sequence name per element, 
    # but it will be updated in each iteration of the while-loop below, such that each element will represent a cluster of sequences, written in Newick format.
    # After the while-loop, only one element (cluster) should remain, with all sequences, representing the final tree in Newick format.
    nwk_list = names_list

    # 'cluster_list' is generated. This is a list of lists. Each element of the outer list is itself a list that represents a cluster, as a list of the 
    # indices of the sequences of the cluster (0 for 'S1', 1 for 'S2', etc). To start with, each element of the outer list (i.e. cluster) has just one 
    # index in it, but it will be updated in each iteration of the while-loop below.
    cluster_list = []
    for i in range(len(names_list)):
        cluster_list.append([i])

    # The orginal 'dist_matr' is copied into 'updated_dist_matr'. The idea is to keep 'dist_matr' unchanged 
    # but make changes to 'updated_dist_matr' in each iteration of the while-loop below.
    updated_dist_matr = dist_matr

    # Here we print how 'updated_dist_matr' and 'nwk_list' look to start with, for your information.
    if (print_details == True):
            print("updated_dist_matr (before while loop):")
            print(updated_dist_matr)
            print("nwk_list (before while loop):")
            print(nwk_list)
            print("")

    # While-loop that in each iteration merges the pair of clusters with smallest average distance between objects
    # until there is only one cluster. 'cluster_list', 'nwk_list' and 'updated_dist_matr' will be updated in each iteration.
    while(len(cluster_list) > 1):
        ### Find the pair of clusters in 'updated_dist_matr' with the smallest distance (we call these "nearest clusters" 
        # in the comments below). Save the indices of the two clusters in the objects that you name 'smallest_row' and 
        # 'smallest_col'. Note that 'smallest_row' should be the smaller index of the two, otherwise the code below will not work.
        # One approach could be to go through each row / column combination of 'updated_dist_matr' with a nested for loop.
        # Write code here:


        ### Update 'cluster_list'.
        # Here we make a list 'in_new_cluster' by combining the lists of sequence indices of the two "nearest clusters".
        in_new_cluster = cluster_list[smallest_row] + cluster_list[smallest_col]

        # Here we remove the elements of the two "nearest clusters" in 'cluster_list'. We remove the element with the highest 
        # index first, to avoid changing the index of the other element.
        del(cluster_list[smallest_col])
        del(cluster_list[smallest_row])
        
        # Here we add the 'in_new_cluster' list as an element to the end of 'cluster_list'.
        cluster_list.append(in_new_cluster)

        ### Updaate 'nwk_list'.
        # Combine the two "nearest clusters" of 'nwk_list' in one string, separating them with a "," and adding a "(" before 
        # and a ")" after. Call the string object 'new_cluster_nwk'. For example, combining 'S1' and 'S2' should give '(S1,S2)'.
        # Write code here:


        # Remove the elements of of the two "nearest clusters" in 'nwk_list'. If done in two steps, it may be wise to remove 
        # the later element first, to not screw up the indexing.
        # Write code here:


        # Add the 'new_cluster_nwk' string as an element to the end of 'nwk_list'.
        # Write code here:


        ### Update 'updated_dist_matr'.
        # Here we remove the two rows and columns of 'updated_dist_matr' that correspond to the two "nearest clusters".
        updated_dist_matr = np.delete(updated_dist_matr, [smallest_row, smallest_col], 0) # removes rows
        updated_dist_matr = np.delete(updated_dist_matr, [smallest_row, smallest_col], 1) # removes columns

        # Here we add a new row and a new column to the "bottom" and "right" of 'updated_dist_matr' where the distances between the newly formed 
        # cluster and the other clusters will be inserted. To start with, the values will all be set to 0 but they will later be replaced with 
        # calculated distances.
        updated_dist_matr = np.append(updated_dist_matr, np.zeros((1, updated_dist_matr.shape[1])), 0) # adds row with zeros to the end (bottom)
        updated_dist_matr = np.append(updated_dist_matr, np.zeros((updated_dist_matr.shape[0], 1)), 1) # adds column with zeros to the end (right)
        
        # Calculate the distance between the new cluster and the other clusters, using the average method, and insert these distances 
        # in the last row and column of 'updated_dist_matr'. The indices of the sequences of the new cluster are in the list 'in_new_cluster' (as 
        # well as in the last elememt of cluster_list). One approach could be to go through each element of 'cluster_list', except the last, to get 
        # the indices of the sequences of the other clusters, and calculate the average of these sequences' distances to the sequences of the new 
        # cluster, using the values in the original 'dist_matr'.
        # Write code here:


        # Here we print 'updated_dist_matr' and 'nwk_list' after each iteration of the while loop, which might help you trouble shoot the code.
        if (print_details == True):
            print("updated_dist_matr:")
            print(updated_dist_matr)
            print("nwk_list:")
            print(nwk_list)
            print("")

    ## After the while loop has finished, all clusters should have been merged into one, and only one element should exist in 'nwk_list'.
    # We convert this to a string and add a ";" to the end, to get proper Newick format. This string is then returned.
    nwk = nwk_list[0] + ';'
    return (nwk)

# Test code for the upgma function. 
# Will only be executed if this file is run directly
# e.g. by running the command "python3 labp4.py"
if __name__ == "__main__":
    nwk = upgma(dist_matr, names_list, print_details = True)
    print(nwk)

