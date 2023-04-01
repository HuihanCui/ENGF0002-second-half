import itertools
from collections import defaultdict

class Term:
    def __init__(self, term="", source=None, flag=False):
        self.term = term
        if source is None:
            source = set((int(term, 2),))
        self.source = source
        self.flag = flag
        self.length = len(term)

    @property
    def ones(self):
        return len(list(filter(lambda c: c == "1", self.term)))
    
    def __eq__(self, other):
        return self.term == other.term
    
    def __hash__(self):
        return hash(self.term)
    
    def __str__(self):
        return self.term

    def __repr__(self):
        return self.__str__()


def generate_new(term1, term2):
    if term1.length != term2.length:
        return
    difference = 0
    pos = -1
    for index, (t1, t2) in enumerate(zip(term1.term, term2.term)):
        if difference > 1:
            return
        else:
            if t1 != t2:
                difference += 1
                pos = index
    #create new terms for two terms with only 1 difference
    if difference == 1:
        new_term = "*".join((term1.term[:pos], term2.term[pos + 1 :]))
        new_source = term1.source | term2.source
        term1.flag = True
        term2.flag = True
        return Term(new_term, new_source)

def find_prime_implicants(minterms):
    tables = defaultdict(set)
    prime_implicants = []
    for term in minterms:
        tables[term.ones].add(term)
    new_implicants = True
    while new_implicants:
        new_implicants = False
        new_table = defaultdict(set)
        for key in sorted(tables.keys()):
            terms1 = tables[key]
            terms2 = tables[key + 1]
            #when terms1 is not the last one 
            if terms2 != None:
                for t1, t2 in itertools.product(terms1, terms2):
                    new_term = generate_new(t1, t2)
                    if not new_term:
                        continue
                    new_table[key].add(new_term)
                    new_implicants = True
            for term in terms1:
                if term.flag == False:
                    prime_implicants.append(term)
        tables = new_table
    return prime_implicants

def cartesian(result, product):
    if result == None:
        return set((frozenset((p,)) for p in product))
    new_result = set()
    for a, b in itertools.product(result, product):
        new_result.add(a | set((b,)))
    return new_result

def find_essential_prime_implicants(prime_implicants, minterms):
    dict = {}
    indexes = set()
    for source in itertools.chain.from_iterable((t.source for t in minterms)):
        dict[source] = set()
    for index, implicant in enumerate(prime_implicants):
        for source in implicant.source:
            dict[source].add(index)
    #Sum-of-Products
    sop = None
    for products in dict.values():
        sop = cartesian(sop, products)
    min = 1000000
    for p in sop:
        if len(p) < min:
            min = len(p)
            indexes = p
    return [prime_implicants[i] for i in indexes]