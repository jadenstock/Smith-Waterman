# Smith-Watermankkj

##The Algorithm The Smith Waterman algorithm is a dynamic programming algorithm for sequence alignment. We can view an alignment of two strings, S and T not neccecarily of the same length, as two new strings S' and T' such that |S'|=|T'| where S' and T' are S and T with "gaps" inserted into various locations. Our goal is to maximiuze the number of aligned characters in S' and T' while minimizing the number of gaps and misaligned characters. We can penalize certain mismatches more than others by using a score matrix \sigma.
