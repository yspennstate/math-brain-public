from itertools import combinations_with_replacement
import hashlib

# Directed P14 -> P15 auxiliary audit of the newest P15 finite self-check.
# P15 did not assign this newest row-sum self-check a formal claim ID, so this
# artifact does not invent one.  It independently enumerates the exact finite set.
n=515
target=4*n
vals=list(range(1,int(target**0.5)+1,2))
sol=[]
for a,b,c,d in combinations_with_replacement(vals,4):
    if a*a+b*b+c*c+d*d==target:
        sol.append((a,b,c,d))
payload='\n'.join(','.join(map(str,t)) for t in sol)+'\n'
h=hashlib.sha256(payload.encode()).hexdigest()
print('target=',target)
print('count=',len(sol))
for t in sol: print(t)
print('sha256=',h)
assert len(sol)==29
assert h=='a769190c974f5cd9210fbbd337fa055418314e26ec4a7de8fe89d440e028e5a6'
assert all(all(x%2 for x in t) for t in sol)
assert all(sum(x*x for x in t)==target for t in sol)
print('AUDIT PASS: exact 29 sorted positive odd row-sum signatures and payload hash match P15')
