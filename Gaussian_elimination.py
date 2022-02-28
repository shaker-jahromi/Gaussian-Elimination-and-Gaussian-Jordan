import numpy as np


def Zero_Gen(M,i,j,op):
	local_elementary_operation_list = {  "elementary_operation_type":  list(),  "elementary_operation_matrix":  list(),  "elementary_operation_manual_calculations":  list(),  "elementary_operation_result":  list()}

	M=M.astype('float')
	
	if op=="GJ":
		operation_index = range(0,M.shape[0])
	if op=="GEP":
		operation_index = range(i,M.shape[0]) 
	if op=="GE":
		operation_index = range(i+1,M.shape[0]) 

	for s in operation_index:
		if s==i:
			if M[i,j]==1:
				continue
			
			em=np.identity(M.shape[0])
			em[s][i]=(1/M[i,j])
			local_elementary_operation_list["elementary_operation_matrix"].append(em)
			local_elementary_operation_list["elementary_operation_type"].append(2)	
                
			local_elementary_operation_list["elementary_operation_manual_calculations"].append('(type 2)  -  R'+str(s)+' * ( 1 / '+str(M[i,j])+' )') #+str( )+

			M[s]=(M[i]/M[i,j])
			local_elementary_operation_list["elementary_operation_result"].append(np.array(M))
			
		else:
			if M[s,j]==0:
				continue
			
			em=np.identity(M.shape[0])
			em[s][i]=-(M[s,j]/M[i,j])

			local_elementary_operation_list["elementary_operation_type"].append(3)
			local_elementary_operation_list["elementary_operation_matrix"].append(em)

			local_elementary_operation_list["elementary_operation_manual_calculations"].append('(type 3)  -  R'+str(s)+' = R'+str(s)+' + ['+str(-(M[s,j]/M[i,j]))+'*R'+str(i)+']') #+str( )+
			M[s]=M[s]-((M[s,j]/M[i,j])*M[i])
			
			local_elementary_operation_list["elementary_operation_result"].append(np.array(M))
			
		# =============================================
	# =======================================================================
	return [M,local_elementary_operation_list]

def Gaussian_operation(M,op="GJ"):
	elementary_operation_list = {  "elementary_operation_type":  list(),  "elementary_operation_matrix":  list(),  "elementary_operation_manual_calculations":  list(),  "elementary_operation_result":  list()}

	A=M
	i=0
	j=0
	while i < M.shape[0] and j < M.shape[1]:
		# =========================================================
		if (int(M[i:,j][0])!=0):
			M,local_elementary_operation_list=Zero_Gen(M,i,j,op)

			elementary_operation_list["elementary_operation_type"].extend(local_elementary_operation_list["elementary_operation_type"])
			elementary_operation_list["elementary_operation_matrix"].extend(local_elementary_operation_list["elementary_operation_matrix"])
			elementary_operation_list["elementary_operation_manual_calculations"].extend(local_elementary_operation_list["elementary_operation_manual_calculations"])
			elementary_operation_list["elementary_operation_result"].extend(local_elementary_operation_list["elementary_operation_result"])

			i=i+1# zeroing
		else: # Zero Detected
			l=np.array(np.where(M[i:,j] != 0)) # search for non zero elenent under zero
			if l.size != 0: # find
				l=(l[0]+i)[0]
				
				em=np.identity(M.shape[0])
				em[np.mat([i,l])]=em[np.mat([l,i])] #swap


				elementary_operation_list["elementary_operation_type"].append(1)
				elementary_operation_list["elementary_operation_matrix"].append(em)


				M[np.mat([i,l])]=M[np.mat([l,i])] #swap

				elementary_operation_list["elementary_operation_manual_calculations"].append('(type 1)  -  '+str(i)+' <Swap Row> '+str(l)) #+str( )+
				elementary_operation_list["elementary_operation_result"].append(np.array(M))
				
				M,local_elementary_operation_list=Zero_Gen(M,i,j,op) # zeroing

				elementary_operation_list["elementary_operation_type"].extend(local_elementary_operation_list["elementary_operation_type"])
				elementary_operation_list["elementary_operation_matrix"].extend(local_elementary_operation_list["elementary_operation_matrix"])
				elementary_operation_list["elementary_operation_manual_calculations"].extend(local_elementary_operation_list["elementary_operation_manual_calculations"])
				elementary_operation_list["elementary_operation_result"].extend(local_elementary_operation_list["elementary_operation_result"])




				i=i+1
				
			else: # not find
				j=j+1
		# =========================================================
	else:
		p=np.identity(elementary_operation_list["elementary_operation_matrix"][0].shape[0])
		for x in elementary_operation_list["elementary_operation_matrix"]:
			p=np.matmul(x,p)
        
		return [p,A,M,elementary_operation_list]

# ======================================================

