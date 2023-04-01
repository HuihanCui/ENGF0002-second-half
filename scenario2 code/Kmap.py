from utils import *

class Minterms(object):
    def __init__(self, minterms=None):
        if minterms is None:
            minterms = []
        self.minterms = minterms
        
    def simplify(self):
        return find_essential_prime_implicants(find_prime_implicants(self.minterms), self.minterms)

def conversion(result):
    conversion_dict_1 = {0:"A", 1:"B", 2:"C", 3:"D"}
    conversion_dict_0 = {0:"¬A", 1:"¬B", 2:"¬C", 3:"¬D"}
    final = []
    for i in result:
        i = str(i)
        string = ""
        for j in range(len(i)):
            if i[j] == "0":
                string += conversion_dict_0[j]
            elif i[j] == "1":
                string += conversion_dict_1[j]
        final.append(string)
    final_str = ""
    for i in range(len(final)-1):
        final_str += final[i] + " ∨ "
    final_str += final[-1] 
    return final_str

def finalize(str_terms):
    t_minterms = [Term(term) for term in str_terms]
    minterms = Minterms(t_minterms)
    result = minterms.simplify()
    #print(result)
    return conversion(result)

str_terms = ["0000", "0010", "0111", "0101", "1010", "1000","1101","1111"]
#str_terms = ["0000", "0001", "1000", "0011", "0101", "0111","1110","1111"]
str_terms = ['0110', '1000', '1001', '1010', '1011', '1100', '1101', '1110']
#str_terms = ['001', '000', '111']
str_terms2 = ['000', '111']
print(finalize(str_terms))
#print(finalize(str_terms2))
#print(conversion(str_terms))