import pubchempy as pc
def fetch_compounds(cids, batch=50):
    def gen(itr):
        for i in range(0,len(itr),batch):
            yield itr[i:min(i+batch,len(itr))]
    return sum([pc.get_compounds(q) for q in gen(cids)],[])
