"""Exact exploratory search: must a current response Gram be an M-matrix?"""
from fractions import Fraction as Q
import json
import random
from general_h2_sos_independent_audit import invdet, laplacian


def response_B(nI, nS, edges, mark=(0,1)):
    L = laplacian(nI+nS, edges)
    D, _ = invdet([row[:nI] for row in L[:nI]])
    p = [[-sum(D[i][k]*L[k][nI+j] for k in range(nI))
          for j in range(nS)] for i in range(nI)]
    p += [[Q(i == j) for j in range(nS)] for i in range(nS)]
    a,b = mark
    v = [D[i][a]-D[i][b] for i in range(nI)] + [Q(0)]*nS
    assert all(sum(L[s][i]*v[i] for i in range(nI)) == 0
               for s in range(nI,nI+nS))
    assert p[a] == p[b]
    eta = [[v[x]*p[y][j]-v[y]*p[x][j]-(v[x]-v[y])*p[a][j]
            for j in range(nS)] for x,y,c in edges]
    B = [[sum(c*eta[g][i]*eta[g][j] for g,(x,y,c) in enumerate(edges))
          for j in range(nS)] for i in range(nS)]
    assert all(sum(row) == 0 for row in B)
    return B


def trial(rng):
    nS = rng.randint(3,6)
    ca = [rng.randint(0,8) for _ in range(nS)]
    cx = [2*rng.randint(0,8) for _ in range(nS)]
    if not sum(cx) or not sum(ca):
        return None
    cb = [a+x//2 for a,x in zip(ca,cx)]
    u = rng.randint(1,8)
    edges = [(0,1,rng.randint(1,8)),(0,2,sum(cx)+3*u),(1,2,u)]
    for j in range(nS):
        for i,weight in enumerate((ca[j],cb[j],cx[j])):
            if weight:
                edges.append((i,3+j,weight))
    B = response_B(3,nS,edges)
    positives = [(i,j,str(B[i][j])) for i in range(nS) for j in range(i)
                 if B[i][j] > 0]
    if positives:
        return {'nI':3,'nS':nS,'edges':edges,'positive_offdiagonal':positives,
                'B':[[str(x) for x in row] for row in B]}


def trial_four(rng):
    nS = rng.randint(3,6)
    cx = [6*rng.randint(0,8) for _ in range(nS)]
    cy = [6*rng.randint(0,8) for _ in range(nS)]
    ca = [rng.randint(1,8)+max(0,(y-x)//3) for x,y in zip(cx,cy)]
    cb = [a+(x-y)//3 for a,x,y in zip(ca,cx,cy)]
    Bx, Ay, C = [rng.randint(1,8) for _ in range(3)]
    Ax = sum(cx)//2+2*Bx+C
    By = sum(cy)//2+2*Ay+C
    edges = [(0,1,rng.randint(1,8)),(0,2,Ax),(1,2,Bx),
             (0,3,Ay),(1,3,By),(2,3,C)]
    for j in range(nS):
        for i,weight in enumerate((ca[j],cb[j],cx[j],cy[j])):
            if weight:
                edges.append((i,4+j,weight))
    mat = response_B(4,nS,edges)
    positives = [(i,j,str(mat[i][j])) for i in range(nS) for j in range(i)
                 if mat[i][j] > 0]
    if positives:
        return {'nI':4,'nS':nS,'edges':edges,'positive_offdiagonal':positives,
                'B':[[str(x) for x in row] for row in mat]}


def trial_general(rng):
    nI, nS = rng.randint(4,8), rng.randint(3,6)
    potential = [Q(10),Q(-10)]
    potential += [Q(rng.choice((-1,1))*rng.randint(1,9)) for _ in range(nI-2)]
    edges = [(0,1,Q(rng.randint(1,8)))]
    spoke = [[Q(rng.randint(0,8)) for j in range(nS)] for i in range(nI)]
    for j in range(nS):
        imbalance = sum(potential[i]*spoke[i][j] for i in range(2,nI))
        base = Q(rng.randint(1,8))
        spoke[0][j] = base+max(Q(0),-imbalance/10)
        spoke[1][j] = base+max(Q(0),imbalance/10)
    interior_flow = [Q(0)]*nI
    for i in range(2,nI):
        for j in range(2,i):
            if rng.randrange(2):
                conductance = Q(rng.randint(1,8))
                edges.append((i,j,conductance))
                current = conductance*(potential[i]-potential[j])
                interior_flow[i] += current
                interior_flow[j] -= current
    for i in range(2,nI):
        vi, Di, other = potential[i], sum(spoke[i]), interior_flow[i]
        free = Q(rng.randint(1,8))
        if vi > 0:
            while free*(vi+10)+Di*vi+other <= 0:
                free += 1
            ca = (free*(vi+10)+Di*vi+other)/(10-vi)
            cb = free
        else:
            while free*(10-vi)-Di*vi-other <= 0:
                free += 1
            ca = free
            cb = (free*(10-vi)-Di*vi-other)/(vi+10)
        edges += [(0,i,ca),(1,i,cb)]
    for i in range(nI):
        for j in range(nS):
            if spoke[i][j]:
                edges.append((i,nI+j,spoke[i][j]))
    mat = response_B(nI,nS,edges)
    positives = [(i,j,str(mat[i][j])) for i in range(nS) for j in range(i)
                 if mat[i][j] > 0]
    if positives:
        return {'nI':nI,'nS':nS,
                'potential':list(map(str,potential)),
                'edges':[(i,j,str(c)) for i,j,c in edges],
                'positive_offdiagonal':positives,
                'B':[[str(x) for x in row] for row in mat]}


if __name__ == '__main__':
    rng = random.Random(20261002)
    checked = 0
    answer = None
    for i in range(3500):
        checked += 1
        answer = (trial(rng) if i < 1000 else trial_four(rng)
                  if i < 3000 else trial_general(rng))
        if answer:
            break
    out = {'cases_checked':checked,'counterexample':answer}
    with open('/workspace/scratch/61b7096f9f41/random_cluster_research/response_space_laplacian_search_results.json','w') as f:
        json.dump(out,f,indent=2)
    print(json.dumps(out,indent=2))
