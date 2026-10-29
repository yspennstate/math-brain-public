import itertools, random, networkx as nx, brute, fastN
rnd=random.Random(7); ok=0; tot=0
for t in range(8):
    n=rnd.randint(4,6); allE=list(itertools.combinations(range(n),2)); E=sorted(rnd.sample(allE,rnd.randint(3,min(len(allE),10))))
    F=fastN.all_N(n,E)
    for (e,f),N in F.items():
        tot+=1; ok+= (N==brute.N_of(n,E,e,f))
print('fastN vs brute pairs equal',ok,'of',tot)
