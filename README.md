# Smith-Waterman

##The Algorithm
The Smith Waterman algorithm is a dynamic programming algorithm for sequence alignment. We can view an alignment of two strings, S and T not necessarily of the same length, as two new strings S' and T' such that |S'|=|T'| where S' and T' are S and T with "gaps" inserted into various locations. Our goal is to maximize the number of aligned characters in S' and T' while minimizing the number of gaps and misaligned characters. We can penalize certain mismatches more than others by using a score matrix sigma.

This algorithm is used in many places such as detecting plagiarism or spell checking, but it is perhaps most commonly used in computational biology for gene sequence alignment. In that setting, a very common choice of score matrix is the BLOSUM62 score matrix (https://www.ncbi.nlm.nih.gov/pubmed/15286655?dopt=Abstract). I have attached this as a text file. If you would like to use a different matrix, make sure it is in the same format as this one.

##Using the code
###1.) reading a score matrix
First, you must read a score matrix from a file. This can be done using the read_score_matrix function. I suggest using "BLOSUM62.txt".

###2.) reading in sequences
The next step is to get some sequences that you wish to align. I have added a list of them to the file and I have also included them in a separate text file and provided a read_sequences function. These sequences were gotten from http://www.expasy.org/. You may wish to get different sequences from there, or from another source. Remember, if you use other sequences then you will need to make a different score matrix.

###3.) alignment
Now that we have some sequences and a matrix we can just use the local_alignment function. Pass in the two strings and the matrix, in that order. There are various flags to that function for how you would like the output. By default, the function just outputs the score of the alignments, if the score is all you need then setting all the flags to False will make the algorithm much faster.
