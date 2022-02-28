# Gaussian_elimination.py

A=np.mat([2,4,8,2,4,8,6,12,26])
A=np.reshape(A, (3,3))
# P,A,E,elementary_operation_list=Gaussian_operation(A,op='GJ') # GJ,GEP,GE
P,A,E,elementary_operation_list=Gaussian_operation(A,op='GEP') # GJ,GEP,GE
# P,A,E,elementary_operation_list=Gaussian_operation(A,op='GE') # GJ,GEP,GE
print("PA = E",'\n\nP = \n',P,'\n\nA = \n',A,'\n\nE = \n',E)

# =======================================================================
# step by step
print(elementary_operation_list["elementary_operation_type"])
print(elementary_operation_list["elementary_operation_matrix"])
print(elementary_operation_list["elementary_operation_manual_calculations"])
print(elementary_operation_list["elementary_operation_result"])
# =======================================================================
# LU factorization 

A=np.mat([2,2,2,4,7,7,6,18,22])
A=np.reshape(A, (3,3))
P,A,U,elementary_operation_list = Gaussian_operation(A,op='GE') # GJ,GEP,GE
L = np.linalg.inv(P)
print("LU factorization ( A = LU )",'\n\nA = \n',A,'\n\nL = \n',L,'\n\nU = \n',U)

