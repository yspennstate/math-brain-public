from itertools import combinations, permutations
from collections import defaultdict

def closure(n, mask):
    rel=[[False]*n for _ in range(n)]
    pairs=list(combinations(range(n),2))
    for bit,(i,j) in enumerate(pairs):
        if (mask>>bit)&1:
            rel[i][j]=True
    for k in range(n):
        for i in range(n):
            if rel[i][k]:
                for j in range(n):
                    if rel[k][j]:
                        rel[i][j]=True
    return tuple(tuple(r) for r in rel)

def exact_relation(n, mask, rel):
    pairs=list(combinations(range(n),2))
    return all(bool((mask>>bit)&1)==rel[i][j] for bit,(i,j) in enumerate(pairs))

def width(n, rel):
    ans=0
    for mask in range(1,1<<n):
        S=[i for i in range(n) if (mask>>i)&1]
        if all(not rel[a][b] and not rel[b][a] for a,b in combinations(S,2)):
            ans=max(ans,len(S))
    return ans

def linexts(n, rel):
    out=[]
    for p in permutations(range(n)):
        pos=[0]*n
        for i,v in enumerate(p): pos[v]=i
        if all((not rel[i][j]) or pos[i]<pos[j] for i in range(n) for j in range(n)):
            out.append(p)
    return out

def cat(z,x,rel):
    if rel[z][x]: return -1
    if rel[x][z]: return 1
    return 0

def cover(a,b,n,rel):
    return rel[a][b] and not any(k not in (a,b) and rel[a][k] and rel[k][b] for k in range(n))

def swap_pos(p,a,b):
    q=list(p)
    ia=q.index(a); ib=q.index(b)
    q[ia],q[ib]=q[ib],q[ia]
    return tuple(q)

def is_ext(p,n,rel):
    pos=[0]*n
    for i,v in enumerate(p): pos[v]=i
    return all((not rel[i][j]) or pos[i]<pos[j] for i in range(n) for j in range(n))

def special_word(p,d,x,y,u):
    pos={v:i for i,v in enumerate(p)}
    return tuple(sorted((d,x,y,u),key=lambda v:pos[v]))

detail={}
fail=defaultdict(int)

for n in range(4,7):
    s=defaultdict(int)
    for mask in range(1<<(n*(n-1)//2)):
        rel=closure(n,mask)
        if not exact_relation(n,mask,rel) or width(n,rel)>3:
            continue
        s["posets"]+=1
        Elist=linexts(n,rel)
        E=len(Elist)
        for x,y,d,u in permutations(range(n),4):
            if rel[x][y] or rel[y][x]:
                continue
            if not rel[d][y] or rel[d][x] or rel[x][d]:
                continue
            if not rel[x][u] or rel[u][y] or rel[y][u]:
                continue
            disting=[z for z in range(n) if z not in (x,y) and cat(z,x,rel)!=cat(z,y,rel)]
            if set(disting)!={d,u}:
                continue

            s["exact_two"]+=1
            cells=defaultdict(list)
            for p in Elist:
                cells[special_word(p,d,x,y,u)].append(p)

            A=len(cells[(d,y,x,u)])
            C=len(cells[(d,x,y,u)])
            Y=len(cells[(x,d,y,u)])
            Z=len(cells[(x,d,u,y)])
            W=len(cells[(x,u,d,y)])
            X=len(cells[(d,x,u,y)])
            if A+C+X+Y+Z+W != E:
                fail["six_cell_partition"]+=1
            if C != A:
                fail["C_equals_A"]+=1

            for p in cells[(x,d,y,u)]:
                q=swap_pos(p,d,x)
                if not is_ext(q,n,rel) or special_word(q,d,x,y,u)!=(d,x,y,u):
                    fail["Y_to_C_swap"]+=1

            bad=0
            for p in cells[(d,x,y,u)]:
                q=swap_pos(p,d,x)
                if is_ext(q,n,rel):
                    continue
                bad+=1
                pos={v:i for i,v in enumerate(p)}
                low=[r for r in range(n)
                     if cover(r,x,n,rel) and not rel[r][d] and not rel[d][r]
                     and pos[d]<pos[r]<pos[x]]
                up=[r for r in range(n)
                    if cover(d,r,n,rel) and not rel[r][x] and not rel[x][r]
                    and pos[d]<pos[r]<pos[x]]
                if not low and not up:
                    fail["canonical_witness"]+=1

            if bad != C-Y:
                fail["defect_count"]+=1

            lowfam=[r for r in range(n)
                    if cover(r,x,n,rel) and not rel[r][d] and not rel[d][r]]
            upfam=[r for r in range(n)
                   if cover(d,r,n,rel) and not rel[r][x] and not rel[x][r]]
            if len(lowfam)>2 or len(upfam)>2:
                fail["width_three_family_bound"]+=1

            B=sum(1 for p in Elist if p.index(x)<p.index(d))
            for r in lowfam:
                ret=sum(1 for p in Elist if p.index(r)<p.index(x)<p.index(d))
                if ret != B:
                    fail["left_return_tax"]+=1
            for r in upfam:
                ret=sum(1 for p in Elist if p.index(x)<p.index(d)<p.index(r))
                if ret != B:
                    fail["right_return_tax"]+=1

            omega=A-Y-W
            if omega>0:
                s["positive_overload"]+=1
                if bad < W+omega or bad < omega:
                    fail["overload_export"]+=1

    detail[n]=dict(s)

assert not fail, dict(fail)
print("POS3_BOUNDARY_OVERLOAD_FOUR_CHANNEL_CHECK_PASS")
for n in range(4,7):
    print("n",n,"width_le_3_natural_posets",detail[n].get("posets",0),
          "exact_two_quadruples",detail[n].get("exact_two",0),
          "positive_overload_cases",detail[n].get("positive_overload",0))
print("total_exact_two_quadruples",sum(detail[n].get("exact_two",0) for n in detail))
print("total_positive_overload_cases",sum(detail[n].get("positive_overload",0) for n in detail))
print("all_failure_counters_zero", True)
