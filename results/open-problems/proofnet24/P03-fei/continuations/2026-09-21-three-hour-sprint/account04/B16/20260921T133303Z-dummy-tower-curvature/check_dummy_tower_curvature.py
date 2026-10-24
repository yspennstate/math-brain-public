#!/usr/bin/env python3
import itertools, math, functools, json

def fwht(a):
    a=list(a); h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h]
                a[j],a[j+h]=x+y,x-y
        h*=2
    return a

def entropy(vals):
    N=len(vals)
    H=0.0
    for z in fwht(vals):
        if z:
            p=(z/N)**2
            H-=p*math.log2(p)
    return H

def clone_phase(g,d,y0):
    out=[]
    for y in range(1<<d):
        for val in g:
            out.append(-1 if val==-1 and y==y0 else 1)
    return out

def lift_phase(g,d):
    return list(g)*(1<<d)

def build_game(phases):
    N=len(phases[0]); m=len(phases)
    @functools.lru_cache(None)
    def G(mask):
        vals=[1]*N
        for a in range(m):
            if (mask>>a)&1:
                vals=[x*y for x,y in zip(vals,phases[a])]
        return entropy(vals)
    return G

def shapley(phases):
    m=len(phases); G=build_game(phases)
    ans=[0.0]*m
    for perm in itertools.permutations(range(m)):
        mask=0
        for v in perm:
            ans[v]+=G(mask|(1<<v))-G(mask)
            mask|=1<<v
    fac=math.factorial(m)
    return [x/fac for x in ans]

def coupled_check(old_phases,d):
    m=len(old_phases); k=1<<d
    clones=[]; blocks=[]
    for g in old_phases:
        B=[]
        for y in range(k):
            B.append(len(clones)); clones.append(clone_phase(g,d,y))
        blocks.append(B)
    G=build_game(clones)
    oldphi=shapley(old_phases)
    shares=[0.0]*len(clones)
    banks=[0.0]*len(clones)
    inner=list(itertools.permutations(range(k)))
    count=0
    for outer in itertools.permutations(range(m)):
        for choices in itertools.product(inner, repeat=m):
            order=[]
            for v in outer:
                order += [blocks[v][r] for r in choices[v]]
            prefix=[]; mask=0
            for a in order:
                marg=G(mask|(1<<a))-G(mask)
                sig=0; curv=0.0
                for b in prefix:
                    curv += G(sig|(1<<a))+G(sig|(1<<b))-G(sig)-G(sig|(1<<a)|(1<<b))
                    sig |= 1<<b
                shares[a]+=marg
                banks[a]+=curv
                prefix.append(a); mask|=1<<a
            count+=1
    shares=[x/count for x in shares]
    banks=[x/count for x in banks]
    max_product_error=0.0
    for v,g in enumerate(old_phases):
        vals=[1]*len(clones[0])
        for a in blocks[v]:
            vals=[x*y for x,y in zip(vals,clones[a])]
        max_product_error=max(max_product_error,
                              max(abs(x-y) for x,y in zip(vals,lift_phase(g,d))))
    max_block_error=max(abs(sum(shares[a] for a in blocks[v])-oldphi[v])
                        for v in range(m))
    max_clone_error=max(abs(shares[a]-oldphi[v]/k)
                        for v in range(m) for a in blocks[v])
    max_curvature_error=max(abs((G(1<<a)-shares[a])-banks[a])
                            for a in range(len(clones)))
    return {
        "old_players":m,"dummy_bits":d,"clones_per_block":k,
        "selector_orders":count,
        "max_product_error":max_product_error,
        "max_block_share_error":max_block_error,
        "max_equal_clone_share_error":max_clone_error,
        "max_plaquette_telescope_error":max_curvature_error
    }

def Hc(c):
    q=2.0**(-c)
    p0=(1-2*q)**2
    p1=4*q*q
    return -p0*math.log2(p0)-(2**c-1)*p1*math.log2(p1)

def gap(c,d):
    return (2**d)*Hc(c+d)-Hc(c)

def main():
    # General Boolean phases; no subcube assumption in the Ward test.
    case1=coupled_check([
        [1,-1,1,1],
        [1,1,-1,1],
        [1,-1,-1,1],
    ],1)
    case2=coupled_check([
        [1,-1,1,1],
        [1,1,-1,-1],
    ],2)
    ward=[case1,case2]
    tol=2e-11
    assert all(max(c["max_product_error"],c["max_block_share_error"],
                       c["max_equal_clone_share_error"],c["max_plaquette_telescope_error"])<tol
               for c in ward)

    tower=[]
    min_gap=1e100
    max_tel=0.0
    for c in range(2,9):
        for d in range(1,9):
            g=gap(c,d)
            min_gap=min(min_gap,g)
            tel=sum((2**r)*(2*Hc(c+r+1)-Hc(c+r)) for r in range(d))
            max_tel=max(max_tel,abs(g-tel))
            assert g>0
            tower.append({"c":c,"d":d,"refund_bits":g,
                          "slope_normalized":g/(8*(2**(-c))*d)})
    assert max_tel<2e-12

    asym=[]
    for c in range(2,7):
        d=40
        g=gap(c,d)
        asym.append({"c":c,"d":d,
                     "refund_bits":g,
                     "refund_over_8d2^-c":g/(8*d*(2**(-c)))})
    out={
        "status":"PASS",
        "claim":"dummy-tower coupled-selector Ward/plaquette renormalization",
        "ward_cases":ward,
        "tower_cases":len(tower),
        "minimum_refund_bits":min_gap,
        "max_layer_telescoping_error":max_tel,
        "sample_refunds":[
            {"c":2,"d":1,"bits":gap(2,1)},
            {"c":2,"d":4,"bits":gap(2,4)},
            {"c":3,"d":4,"bits":gap(3,4)},
            {"c":4,"d":4,"bits":gap(4,4)}
        ],
        "asymptotic_checks":asym,
        "note":"Finite checks support the exact algebraic proof; they do not prove unrestricted FEI."
    }
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=="__main__":
    main()
