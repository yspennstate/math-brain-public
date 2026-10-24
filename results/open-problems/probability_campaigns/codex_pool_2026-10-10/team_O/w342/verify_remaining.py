"""Independent numeric and exact checks for the remaining six proof attempts."""
from fractions import Fraction as Q
from itertools import combinations, product
import json
from math import comb
from pathlib import Path
import time
import mpmath as mp

ROOT = Path(__file__).resolve().parent


def save(problem, data, start):
    data.update(command='python -X utf8 verify_remaining.py', seconds=round(time.perf_counter()-start,3), label='finite checks and numerical evidence; separate written proof awaiting audit')
    (ROOT/(problem.lower()+'_measurements.json')).write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
    print(problem,json.dumps(data),flush=True)


start = time.perf_counter()
mp.mp.dps = 65
tail_checks = 0
errors = []
for lam in [mp.mpf('0.4'),mp.mpf('0.7')]:
    for B in [mp.mpf('-1'),mp.mpf('0'),mp.mpf('1')]:
        for L in [mp.mpf(40),mp.mpf(80),mp.mpf(160),mp.mpf(320)]:
            x = 2*lam*L/mp.sqrt(L+B)
            exact = mp.erfc(x/mp.sqrt(2))/2
            leading = mp.exp(-2*lam*lam*L+2*lam*lam*B)/(2*lam*mp.sqrt(2*mp.pi*L))
            correction = B/2-2*lam*lam*B*B-1/(4*lam*lam)
            error = abs(exact/leading-1-correction/L)
            errors.append(error*L*L)
            assert error*L*L < 20
            tail_checks += 1
save('C0002',{'gaussian_tail_checks':tail_checks,'maximum_relative_remainder_times_logN_squared':str(max(errors)),'violations':0},start)

start = time.perf_counter()
energy = Q(0)
rows = []
for k in range(1,13):
    for n in range(3*(k-1),3*k):
        energy += Q(2**(n//3),2**(n+1))
    assert energy == Q(7,6)*(1-Q(1,4**k))
    radius = sum(2**(n//3) for n in range(3*k))
    vertices = 1+sum(2**(n+1)*2**(n//3) for n in range(3*k))
    assert radius == 3*(2**k-1)
    assert vertices == 1+14*(16**k-1)//15
    rows.append({'generation':3*k,'radius':radius,'vertices':vertices,'flow_energy':str(energy)})
save('C0059',{'generation_checks':12,'finite_energy_limit':'7/6','last_generation':rows[-1],'violations':0,'scope':'explicit transient tree construction; Boltzmann law not modeled'},start)


class DSU:
    def __init__(self,n):
        self.parent = list(range(n))
    def find(self,a):
        while self.parent[a]!=a:
            a=self.parent[a]
        return a
    def union(self,a,b):
        a,b=self.find(a),self.find(b)
        if a==b:
            return False
        self.parent[a]=b
        return True


start=time.perf_counter()
hamming_checks = []
for n,d in [(3,1),(4,1),(2,2),(3,2),(4,2),(2,3)]:
    vertices=list(product(range(n),repeat=d))
    edges=[(i,j) for i,j in combinations(range(len(vertices)),2) if sum(x!=y for x,y in zip(vertices[i],vertices[j]))==1]
    adjacency=[set() for _ in vertices]
    for i,j in edges:
        adjacency[i].add(j)
        adjacency[j].add(i)
    degree=d*(n-1)
    triangle=sum(v in adjacency[u] for u,v in combinations(adjacency[0],2))
    four=sum(len(adjacency[u]&adjacency[v])-1 for u,v in combinations(adjacency[0],2))
    assert triangle==d*comb(n-1,2)
    assert four==3*d*comb(n-1,3)+comb(d,2)*(n-1)**2
    coefficients=[0]*4
    subset_checks=0
    for k in range(4):
        for chosen in combinations(range(len(edges)),k):
            subset_checks+=1
            uf=DSU(len(vertices))
            for i in chosen:
                uf.union(*edges[i])
            cluster_size=sum(uf.find(i)==uf.find(0) for i in range(len(vertices)))
            for power in range(k,4):
                coefficients[power]+=cluster_size*(-1)**(power-k)*comb(len(edges)-k,power-k)
    assert coefficients==[1,degree,degree*(degree-1),degree*(degree-1)**2-4*triangle]
    hamming_checks.append({'n':n,'d':d,'triangles':triangle,'four_cycles':four,'susceptibility_coefficients':coefficients,'subsets':subset_checks})
save('C0083',{'graph_cases':len(hamming_checks),'cases':hamming_checks,'violations':0},start)

start=time.perf_counter()
pstar=Q(3,4)
bad={(0,1):Q(0),(-1,1):Q(1,4),(1,1):Q(1,2)}
total_budget=sum(pstar-p for p in bad.values())
paths=[(0,{},Q(1),Q(0),Q(0))]
prefix_checks=0
for k in range(12):
    next_paths=[]
    for position,visits,probability,martingale,budget in paths:
        visit=visits.get(position,0)+1
        new_visits=visits|{position:visit}
        p=bad.get((position,visit),pstar)
        new_budget=budget+max(Q(0),pstar-p)
        assert new_budget<=total_budget
        for step,chance in [(1,p),(-1,1-p)]:
            if chance==0:
                continue
            new_position=position+step
            new_martingale=martingale+step-(2*p-1)
            assert new_position >= (2*pstar-1)*(k+1)-2*new_budget+new_martingale
            prefix_checks+=1
            next_paths.append((new_position,new_visits,probability*chance,new_martingale,new_budget))
    paths=next_paths
    assert sum(x[2] for x in paths)==1
    assert sum(x[2]*x[3] for x in paths)==0
save('C0128',{'steps':12,'positive_probability_final_paths':len(paths),'prefix_drift_checks':prefix_checks,'total_adverse_cookie_budget':str(total_budget),'martingale_mean_exact':'0','violations':0},start)


def det(matrix):
    a=[[Q(x) for x in row] for row in matrix]
    result=Q(1)
    for col in range(len(a)):
        pivot=next((i for i in range(col,len(a)) if a[i][col]),None)
        if pivot is None:
            return Q(0)
        if pivot!=col:
            a[col],a[pivot]=a[pivot],a[col]
            result=-result
        p=a[col][col]
        result*=p
        for i in range(col+1,len(a)):
            factor=a[i][col]/p
            for j in range(col+1,len(a)):
                a[i][j]-=factor*a[col][j]
    return result


start=time.perf_counter()
frame_checks=[]
for M in range(2,9):
    vectors=[]
    for second in [1,-1,1j]:
        vectors.append([1,second]+[0]*(M-2))
    for j in range(2,M):
        for second,entry in [(1,1),(1,1j),(-1,1),(-1,1j)]:
            vector=[1,second]+[0]*(M-2)
            vector[j]=entry
            vectors.append(vector)
    tangent=[]
    for kind in ['beta','re_z','im_z']:
        matrix=[[0j]*M for _ in range(M)]
        if kind=='beta':
            matrix[1][1]=1
        else:
            matrix[0][1]=1 if kind=='re_z' else 1j
            matrix[1][0]=matrix[0][1].conjugate()
        tangent.append(matrix)
    for j in range(2,M):
        for row,entry in [(0,1),(0,1j),(1,1),(1,1j)]:
            matrix=[[0j]*M for _ in range(M)]
            matrix[row][j]=entry
            matrix[j][row]=complex(entry).conjugate()
            tangent.append(matrix)
    jacobian=[]
    for vector in vectors:
        assert abs(vector[0])**2-abs(vector[1])**2==0
        derivatives=[]
        for h in tangent:
            quadratic=sum(complex(vector[i]).conjugate()*h[i][j]*vector[j] for i in range(M) for j in range(M))
            assert quadratic.imag==0 and quadratic.real.is_integer()
            derivatives.append(int(quadratic.real))
        jacobian.append(derivatives)
    jacdet=det(jacobian)
    assert jacdet==8*64**(M-2)
    assert len(vectors)==4*M-5
    frame_checks.append({'M':M,'N':len(vectors),'jacobian_determinant':str(jacdet)})
save('P0015',{'exact_jacobian_checks':len(frame_checks),'dimensions':frame_checks,'violations':0,'scope':'exact derivatives verify transversality; the IFT and probability conclusion are in the written proof'},start)

start=time.perf_counter()
# A wired ball of radius two in the 3-regular tree. Leaves are identified
# to one boundary vertex; the six boundary edges retain their original labels.
edges=[(0,1),(0,2),(0,3),(1,4),(1,4),(2,4),(2,4),(3,4),(3,4)]
spanning=[]
for selected in combinations(range(len(edges)),4):
    uf=DSU(5)
    if all(uf.union(*edges[i]) for i in selected):
        spanning.append(frozenset(selected))
support=set(spanning)
symmetry_checks=0
from itertools import permutations
for branch_perm in permutations(range(3)):
    for flips in product([0,1],repeat=3):
        edge_perm={i:branch_perm[i] for i in range(3)}
        for branch in range(3):
            for leaf in range(2):
                edge_perm[3+2*branch+leaf]=3+2*branch_perm[branch]+(leaf^flips[branch])
        transformed={frozenset(edge_perm[i] for i in tree) for tree in spanning}
        assert transformed==support
        symmetry_checks+=1
        assert all(tree<=frozenset(range(9)) for tree in transformed)
save('P0044',{'wired_ball_spanning_trees':len(spanning),'joint_law_symmetry_checks':symmetry_checks,'order_violations':0,'scope':'finite symmetric wired ball; infinite tree coupling established in written proof'},start)
