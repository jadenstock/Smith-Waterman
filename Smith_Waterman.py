
# Jaden Stock
# Smith-Waterman alignment algorithm for local alignment

import random

#MYOD1_HUMAN (human)
P15172 = "MELLSPPLRDVDLTAPDGSLCSFATTDDFYDDPCFDSPDLRFFEDLDPRLMHVGALLKPEEHSHFPAAVHPAPGAREDEHVRAPSGHHQAGRCLLWACKACKRKTTNADRRKAATMRERRRLSKVNEAFETLKRCTSSNPNQRLPKVEILRNAIRYIEGLQALLRDQDAAPPGAAAAFYAPGPLPPGRGGEHYSGDSDASSPRSNCSDGMMDYSGPPSGARRRNCYEGAYYNEAPSEPRPGKSAAVSSLDCLSSIVERISTESPAAPALLLADVPSESPPRRQEAAAPSEGESSGDPTQSPDAAPQCPAGANPNPIYQVL" 
#TAL1_HUMAN (human)
P17542 = "MTERPPSEAARSDPQLEGRDAAEASMAPPHLVLLNGVAKETSRAAAAEPPVIELGARGGPGGGPAGGGGAARDLKGRDAATAEARHRVPTTELCRPPGPAPAPAPASVTAELPGDGRMVQLSPPALAAPAAPGRALLYSLSQPLASLGSGFFGEPDAFPMFTTNNRVKRRPSPYEMEITDGPHTKVVRRIFTNSRERWRQQNVNGAFAELRKLIPTHPPDKKLSKNEILRLAMKYINFLAKLLNDQEEEGTQRAKTGKDPVVGAGGGGGGGGGGAPPDDLLQDVLSPNSSCGSSLDGAASPDSYTEEPAPKHTARSLHPAMLPAADGAGPR"
#MYOD1_MOUSE (Mouse)
P10085 = "MELLSPPLRDIDLTGPDGSLCSFETADDFYDDPCFDSPDLRFFEDLDPRLVHMGALLKPEEHAHFPTAVHPGPGAREDEHVRAPSGHHQAGRCLLWACKACKRKTTNADRRKAATMRERRRLSKVNEAFETLKRCTSSNPNQRLPKVEILRNAIRYIEGLQALLRDQDAAPPGAAAFYAPGPLPPGRGSEHYSGDSDASSPRSNCSDGMMDYSGPPSGPRRQNGYDTAYYSEAARESRPGKSAAVSSLDCLSSIVERISTDSPAAPALLLADAPPESPPGPPEGASLSDTEQGTQTPSPDAAPQCPAGSNPNAIYQVL" 
#MYOD1_CHICK (Chicken)
P16075 = "MDLLGPMEMTEGSLCSFTAADDFYDDPCFNTSDMHFFEDLDPRLVHVGGLLKPEEHPHTRAPPREPTEEEHVRAPSGHHQAGRCLLWACKACKRKTTNADRRKAATMRERRRLSKVNEAFETLKRCTSTNPNQRLPKVEILRNAIRYIESLQALLREQEDAYYPVLEHYSGESDASSPRSNCSDGMMEYSGPPCSSRRRNSYDSSYYTESPNDPKHGKSSVVSSLDCLSSIVERISTDNSTCPILPPAEAVAEGSPCSPQEGGNLSDSGAQIPSPTNCTPLPQESSSSSSSNPIYQVL" 
#MYODA_XENLA (African clawed frog)
P13904 = "MELLPPPLRDMEVTEGSLCAFPTPDDFYDDPCFNTSDMSFFEDLDPRLVHVTLLKPEEPHHNEDEHVRAPSGHHQAGRCLLWACKACKRKTTNADRRKAATMRERRRLSKVNEAFETLKRYTSTNPNQRLPKVEILRNAIRYIESLQALLHDQDEAFYPVLEHYSGDSDASSPRSNCSDGMMDYNSPPCGSRRRNSYDSSFYSDSPNDSRLGKSSVISSLDCLSSIVERISTQSPSCPVPTAVDSGSEGSPCSPLQGETLSERVITIPSPSNTCTQLSQDPSSTIYHV" 
#MYOD1_DANRE (Zebrafish)
Q90477 = "MELSDIPFPIPSADDFYDDPCFNTNDMHFFEDLDPRLVHVSLLKPDEHHHIEDEHVRAPSGHHQAGRCLLWACKACKRKTTNADRRKAATMRERRRLSKVNDAFETLKRCTSTNPNQRLPKVEILRNAISYIESLQALLRSQEDNYYPVLEHYSGDSDASSPRSNCSDGMMDFMGPTCQTRRRNSYDSSYFNDTPNADARNNKNSVVSSLDCLSSIVERISTETPACPVLSVPEGHEESPCSPHEGSVLSDTGTTAPSPTSCPQQQAQETIYQVL" 
#Q8IU24_BRABE (Amphioxus)
Q8IU24 = "MEFVELSSCRFDATPTFCDRPAAPNATVLPGEHFPVPNGSYEDQGDGHVLAPGPSFHGPGRCLLWACKACKKKTVPIDRRKAATMRERRRLVKVNEAFDILKKKSCANPNQRLPKVEILRNAISYIEQLHKLLRDSKENSSGEVSDTSAPSPGSCSDGMAAHSPHSFCTDTSGNSSWEQGDGQPGNGYENQSCGNTVSSLDCLSLIVQSISTIEGEENNNASNTPR"
#MYOD_DROME (Fruit fly)
P22816 = "MTKYNSGSSEMPAAQTIKQEYHNGYGQPTHPGYGFSAYSQQNPIAHPGQNPHQTLQNFFSRFNAVGDASAGNGGAASISANGSGSSCNYSHANHHPAELDKPLGMNMTPSPIYTTDYDDENSSLSSEEHVLAPLVCSSAQSSRPCLTWACKACKKKSVTVDRRKAATMRERRRLRKVNEAFEILKRRTSSNPNQRLPKVEILRNAIEYIESLEDLLQESSTTRDGDNLAPSLSGKSCQSDYLSSYAGAYLEDKLSFYNKHMEKYGQFTDFDGNANGSSLDCLNLIVQSINKSTTSPIQNKATPSASDTQSPPSSGATAPTSLHVNFKRKCST"
#LIN32_CAEEL (C. elegans)
Q10574 = "MSWEQYQMYVPQCHPSFMYQGSIQSTMTTPLQSPNFSLDSPNYPDSLSNGGGKDDKKKCRRYKTPSPQLLRMRRSAANERERRRMNTLNVAYDELREVLPEIDSGKKLSKFETLQMAQKYIECLSQILKQDSKNENLKSKSG" 
#SYFM_HUMAN (Human)
O95363 = "MVGSALRRGAHAYVYLVSKASHISRGHQHQAWGSRPPAAECATQRAPGSVVELLGKSYPQDDHSNLTRKVLTRVGRNLHNQQHHPLWLIKERVKEHFYKQYVGRFGTPLFSVYDNLSPVVTTWQNFDSLLIPADHPSRKKGDNYYLNRTHMLRAHTSAHQWDLLHAGLDAFLVVGDVYRRDQIDSQHYPIFHQLEAVRLFSKHELFAGIKDGESLQLFEQSSRSAHKQETHTMEAVKLVEFDLKQTLTRLMAHLFGDELEIRWVDCYFPFTHPSFEMEINFHGEWLEVLGCGVMEQQLVNSAGAQDRIGWAFGLGLERLAMILYDIPDIRLFWCEDERFLKQFCVSNINQKVKFQPLSKYPAVINDISFWLPSENYAENDFYDLVRTIGGDLVEKVDLIDKFVHPKTHKTSHCYRITYRHMERTLSQREVRHIHQALQEAAVQLLGVEGRF"

#array of sequences that will be used
sequences = [P15172, P17542, P10085, P16075, P13904, Q90477, Q8IU24, P22816, Q10574, O95363]
sequences_abrv = ["P15172", "P17542", "P10085", "P16075", "P13904", "Q90477", "Q8IU24", "P22816", "Q10574", "O95363"]

def read_score_matrix(file_name):
	sigma = {}
	f = open(file_name, "r")

	#first get the characters in the dict
	while True:
		line = f.next()
		if not line.startswith("#"):
			chars = line.split()
			break

	#now we fill in the matrix
	for line in f:
		if line.startswith("#"):
			pass
		else:
			sentence = line.split()
			sigma[sentence[0]] = {}
			for i in range(1, len(sentence)):
				sigma[sentence[0]][chars[i-1]] = int(sentence[i])
	return sigma

#return the sequences from lines that do not start with a #
def read_sequences(file_name):
	f = open(file_name, "r")
	sequences = {}
	for line in f:
		if not line.startswith("#"):
			line = line.split(":")
			sequences[line[0]] = line[1] #do I need to get rid of the new line?
	return sequences


#permutes an array using the technique discussed in class
#input: an array
#output: a new, permuted array
def permute_array(array):
	permuted_array = list(array)
	for i in range(len(array)):
		i = len(array)-i-1
		j = random.randint(0,i)
		permuted_array[i], permuted_array[j] = permuted_array[j], permuted_array[i]
	return permuted_array


# Smith-Waterman Local sequence alignment algorithm
# input: Two strings S and T as well and a score dictionary. Optional tags for printing the alignment matrix, 
# 		printing the aligned substrings, printing the score, and an optional output_file
# effects: if any of the print_matrix, print_strings, print_score tags are set to true, the corresponding object will be printed, 
#		if an output_file is given they will print to that.
# output: the score of the optimal local alignment
def local_alignment(S, T, sigma, print_matrix = False, print_strings = True, print_score = True, output_file = None):
	#first we will create our 2D array and fill it with values using the recurrence relation
	v = [[0 for j in range(len(T)+1)] for i in range(len(S)+1)]
	for j in range(1, len(T)+1):
		for i in range(1, len(S)+1):
			v[i][j] = max([0, v[i-1][j-1]+sigma[S[i-1]][T[j-1]], v[i-1][j]+sigma[S[i-1]]["*"], v[i][j-1]+sigma["*"][T[j-1]]])

	#if print_matrix is true we print out the alignment matrix
	if print_matrix:
		matrix_string = ""
		t_string = "     *"
		for i in range(len(T)):
			t_string += "  "
			t_string += T[i]
		matrix_string += t_string
		matrix_string += "\n"
		for i in range(len(S)+1):
			number_string = ""
			if(i == 0):
				number_string += "  *"
			else:
				number_string += "  "
				number_string += S[i-1]
			for j in range(len(T)+1):
				if(len(str(v[i][j])) == 1):
					number_string += "  "
					number_string += str(v[i][j])
				elif(len(str(v[i][j])) == 2):
					number_string += " "
					number_string += str(v[i][j])
			matrix_string += number_string
			matrix_string += "\n"
		if output_file == None:
			print(matrix_string + "\n")
		else:
			output_file.write(matrix_string + "\n")

	# now we find the cell of v which holds the maximum value
	max_value = 0
	max_i, max_j = 0, 0
	for i in range(1,len(S)+1):
		for j in range(1, len(T)+1):
			if (v[i][j] > max_value):
				max_value = v[i][j]
				max_i, max_j = i, j

	#now if the print flag was set to true then we want to construct the aligned strings and print them out
	if(print_strings == True):
		#if S and T are one of the default sequences we can find which ones they are
		s_abbreviation = ""
		t_abbreviation = ""
		for i in range(len(sequences)):
			if S == sequences[i]:
				s_abbreviation = sequences_abrv[i]
				s_abbreviation += ":"
			if T == sequences[i]:
				t_abbreviation = sequences_abrv[i]
				t_abbreviation += ":"

		#We trace back thruogh the 2-D to find the optimal alignment
		opt_path = [(max_i,max_j)]
		cur_i = max_i
		cur_j = max_j
		while(v[cur_i][cur_j] != 0):
			#construct an array of possible steps before the cur pointers that lead to the cur pointers.
			reverse_path_positions = []
			if(v[cur_i-1][cur_j]+sigma[S[cur_i-1]]["*"] == v[cur_i][cur_j]):
				reverse_path_positions += [(cur_i-1,cur_j)]

			if(v[cur_i][cur_j-1]+sigma["*"][T[cur_j-1]] == v[cur_i][cur_j]):
				reverse_path_positions += [(cur_i,cur_j-1)]

			if(v[cur_i-1][cur_j-1]+sigma[S[cur_i-1]][T[cur_j-1]] == v[cur_i][cur_j]):
				reverse_path_positions += [(cur_i-1,cur_j-1)]

			#pick a random, valid path direction
			reverse_path_positions = permute_array(reverse_path_positions)
			a,b = reverse_path_positions[0]
			opt_path += [(a,b)]
			cur_i = a
			cur_j = b

		#finally, we construct the strings in the alignment to be printed out.
		local_aligned_S = ""
		local_aligned_T = ""
		opt_path = opt_path[::-1] #reverse the path and throw away the first element because it corresponds to a 0 in the alignment matrix
		opt_path = opt_path[1:]
		start_i, start_j = opt_path[0] #the start index of each string, will be printed later.
		for i in range(len(opt_path)):
			a,b = opt_path[i]
			if i==0:
				local_aligned_S += S[a-1]
				local_aligned_T += T[b-1]
			else:
				c,d = opt_path[i-1]
				if((a == c+1) and (b == d+1)):
					local_aligned_S += S[a-1]
					local_aligned_T += T[b-1]
				elif((a == c) and (b == d+1)):
					local_aligned_S += "-"
					local_aligned_T += T[b-1]
				elif((a == c+1) and (b == d)):
					local_aligned_S += S[a-1]
					local_aligned_T += "-"

		#create the middle line, This just tells you which characters are aligned.
		middle_line = ""
		for i in range(len(local_aligned_S)):
			if(local_aligned_S[i] == local_aligned_T[i]):
				middle_line += local_aligned_S[i]
			elif((local_aligned_S[i] == "-") or (local_aligned_T[i] == "-")):
				middle_line += " "
			elif(sigma[local_aligned_S[i]][local_aligned_T[i]] > 0):
				middle_line += "+"
			else:
				middle_line += " "
		
		#now we want to only print out 60 characters of each string at a time
		counter = 0
		while(len(local_aligned_S) > 0):
			if output_file == None:
				print(s_abbreviation + "\t" + str(start_i + counter) + "\t" + local_aligned_S[:60] + "\n")
				print("\t\t" + middle_line[:60] + "\n")
				print(t_abbreviation + "\t" + str(start_j +counter ) + "\t" + local_aligned_T[:60] + "\n")
				print("\n")
			else:
				output_file.write(s_abbreviation + "\t" + str(start_i + counter) + "\t" + local_aligned_S[:60] + "\n")
				output_file.write("\t\t" + middle_line[:60] + "\n")
				output_file.write(t_abbreviation + "\t" + str(start_j + counter) + "\t" + local_aligned_T[:60] + "\n")
				output_file.write("\n")

			local_aligned_S = local_aligned_S[60:]
			local_aligned_T = local_aligned_T[60:]
			middle_line = middle_line[60:]
			counter += 60

	#if the score tag was set to True then pring the score
	if print_score:
		if output_file == None:
			print("Score = " + str(max_value) + "\n\n\n")
		else:
			output_file.write("Score = " + str(max_value) + "\n\n\n")
	return max_value


#an example of how to run the code:
#sigma = read_score_matrix("BLOSUM62.txt")
#local_alignment(P15172,P17542, sigma)