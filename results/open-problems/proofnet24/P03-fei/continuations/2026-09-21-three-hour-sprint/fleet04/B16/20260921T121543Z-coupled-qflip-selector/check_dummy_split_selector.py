#!/usr/bin/env python3
from fractions import Fraction
import itertools, math, json, random

def mobius(values, m):
    d = list(values)
    for j in range(m):
        b = 1 << j
        for mask in range(1 << m):
            if mask & b:
                d[mask] -= d[mask ^ b]
    return d

def shapley_from_values(values, m):
    f = [math.factorial(i) for i in range(m+1)]
    den = math.factorial(m)
    out = [0 for _ in range(m)]
    for j in range(m):
        b = 1 << j
        for mask in range(1 << m):
            if mask & b:
                continue
            s = mask.bit_count()
            out[j] += Fraction(f[s]*f[m-s-1], den) * (values[mask|b] - values[mask])
    return out

def block_selector_values(values, groups):
    # Fine players are pairs (2g,2g+1). Outer group order is uniform; inside each pair is fair.
    m=2*groups
    out=[Fraction(0) for _ in range(m)]
    perms=list(itertools.permutations(range(groups)))
    for order in perms:
        # enumerate the 2^groups fair internal orders
        for flips in range(1<<groups):
            prefix=0
            weight=Fraction(1, len(perms)*(1<<groups))
            for g in order:
                a,b=2*g,2*g+1
                if flips>>g&1: a,b=b,a
                out[a]+=weight*(values[prefix|(1<<a)]-values[prefix])
                prefix|=1<<a
                out[b]+=weight*(values[prefix|(1<<b)]-values[prefix])
                prefix|=1<<b
    return out

def global_pair_swap(mask, groups):
    out=0
    for g in range(groups):
        b0=(mask>>(2*g))&1
        b1=(mask>>(2*g+1))&1
        if b0: out|=1<<(2*g+1)
        if b1: out|=1<<(2*g)
    return out

def exact_pair_split_checks():
    rng = random.Random(20260921)
    cases = 0
    symmetric_cases = 0
    max_l1 = Fraction(0)
    # generic games on 2s fine players grouped into pairs
    for sgroups in range(2,6):
        m=2*sgroups
        for rep in range(20):
            vals=[Fraction(rng.randint(-9,9)) for _ in range(1<<m)]
            vals[0]=Fraction(0)
            fine_phi=shapley_from_values(vals,m)
            agg=[]
            for g in range(sgroups):
                agg.append(fine_phi[2*g]+fine_phi[2*g+1])
            # coarse game = restriction to unions of complete pairs
            coarse=[Fraction(0)]*(1<<sgroups)
            for mask in range(1<<sgroups):
                fm=0
                for g in range(sgroups):
                    if mask>>g&1:
                        fm |= (1<<(2*g)) | (1<<(2*g+1))
                coarse[mask]=vals[fm]
            coarse_phi=shapley_from_values(coarse,sgroups)
            # Coupled block selector has exact group conservation for every game.
            block_phi=block_selector_values(vals,sgroups)
            for g in range(sgroups):
                assert block_phi[2*g]+block_phi[2*g+1] == coarse_phi[g]
            # If the fine game has the global dummy-swap symmetry, each clone gets half.
            sym=list(vals)
            for mask in range(1<<m):
                mate=global_pair_swap(mask,sgroups)
                if mask<=mate:
                    z=Fraction(sym[mask]+sym[mate],2)
                    sym[mask]=sym[mate]=z
            sym_block=block_selector_values(sym,sgroups)
            sym_coarse=[Fraction(0)]*(1<<sgroups)
            for mask in range(1<<sgroups):
                fm=0
                for g in range(sgroups):
                    if mask>>g&1:
                        fm |= (1<<(2*g)) | (1<<(2*g+1))
                sym_coarse[mask]=sym[fm]
            sym_coarse_phi=shapley_from_values(sym_coarse,sgroups)
            for g in range(sgroups):
                assert sym_block[2*g] == sym_block[2*g+1] == sym_coarse_phi[g]/2
            symmetric_cases += 1
            d=mobius(vals,m)
            delta=[Fraction(0) for _ in range(sgroups)]
            for T in range(1,1<<m):
                touched=[]
                total=T.bit_count()
                for g in range(sgroups):
                    t=((T>>(2*g))&1)+((T>>(2*g+1))&1)
                    if t:
                        touched.append((g,t))
                ss=len(touched)
                for g,t in touched:
                    delta[g] += d[T]*(Fraction(t,total)-Fraction(1,ss))
                # coefficient identities / norm bound
                r=sum(1 for _,t in touched if t==2)
                if r==0 or r==ss:
                    assert all(Fraction(t,total)==Fraction(1,ss) for _,t in touched)
                else:
                    coeff=[]
                    for _,t in touched:
                        c=Fraction(t,total)-Fraction(1,ss)
                        coeff.append(c)
                        if t==2:
                            assert c == Fraction(ss-r, ss*(ss+r))
                        else:
                            assert c == -Fraction(r, ss*(ss+r))
                    assert sum(coeff)==0
                    norm2=sum(c*c for c in coeff)
                    assert norm2 == Fraction(r*(ss-r), ss*(ss+r)*(ss+r))
                    assert norm2 <= Fraction(1,8*ss)
                    l1=sum(abs(c) for c in coeff)
                    if l1>max_l1: max_l1=l1
            for g in range(sgroups):
                assert agg[g]-coarse_phi[g] == delta[g]
            assert sum(delta)==0
            cases += 1
    return cases, symmetric_cases, max_l1

def exact_parity_block_selector_checks():
    checks=0
    for groups in range(2,5):
        m=2*groups
        for R in range(1,1<<m):
            if R.bit_count()%2==0:
                continue
            c=Fraction(-3 if (R%3==0) else 5, 7)
            vals=[]
            for S in range(1<<m):
                parity=(S&R).bit_count()%2
                vals.append(c if parity else Fraction(0))
            phi=block_selector_values(vals,groups)
            for g in range(groups):
                got=phi[2*g]+phi[2*g+1]
                tg=((R>>(2*g))&1)+((R>>(2*g+1))&1)
                odd_groups=sum(
                    1 for h in range(groups)
                    if (((R>>(2*h))&1)+((R>>(2*h+1))&1))%2==1
                )
                want=c/Fraction(odd_groups) if tg%2 else Fraction(0)
                assert got==want
            checks += 1
    return checks

def fwht(vals):
    a=[float(x) for x in vals]
    h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h]
                a[j],a[j+h]=x+y,x-y
        h*=2
    N=len(a)
    return [x/N for x in a]

def entropy(vals):
    H=0.0
    for a in fwht(vals):
        p=a*a
        if p>1e-15: H-=p*math.log2(p)
    return H

def generators(n):
    out=[]
    for v in range(1,1<<n):
        if v.bit_count()<2: continue
        p=(v & -v).bit_length()-1
        g=[]
        for x in range(1<<n):
            match=True
            for j in range(p,n):
                if ((x>>j)&1)!=((v>>j)&1):
                    match=False; break
            g.append(-1 if match else 1)
        out.append((v,p,g))
    return out

GEN={n:generators(n) for n in (3,4)}

def active(vals,n):
    out=[]
    for v,p,g in GEN[n]:
        z=vals[0]*vals[1<<p]*vals[v]*vals[v^(1<<p)]
        if z==-1: out.append((v,p,g))
    return out

def coalition_values(vals,n):
    act=active(vals,n)
    m=len(act); N=1<<n
    phases={0:[1]*N}
    ent=[0.0]*(1<<m)
    for mask in range(1,1<<m):
        lb=mask&-mask; j=lb.bit_length()-1; prev=mask^lb
        phases[mask]=[a*b for a,b in zip(phases[prev],act[j][2])]
        ent[mask]=entropy(phases[mask])
    return act,ent

def shapley_float(values,m):
    f=[math.factorial(i) for i in range(m+1)]
    den=math.factorial(m)
    phi=[0.0]*m
    for j in range(m):
        bit=1<<j
        for mask in range(1<<m):
            if mask&bit: continue
            ss=mask.bit_count()
            phi[j]+=f[ss]*f[m-ss-1]/den*(values[mask|bit]-values[mask])
    return phi

def extend(vals,k=3):
    return [vals[x&((1<<k)-1)] for x in range(1<<(k+1))]

def entropy_exhaustive():
    max_formula_err=0.0
    max_redis=0.0
    witness=None
    checked=0
    for truth in range(256):
        vals=[1 if (truth>>x)&1 else -1 for x in range(8)]
        a0,V0=coalition_values(vals,3)
        p0=shapley_float(V0,len(a0))
        coarse={a0[j][0]:p0[j] for j in range(len(a0))}
        ext=extend(vals)
        a1,V1=coalition_values(ext,4)
        p1=shapley_float(V1,len(a1))
        m=len(a1)
        # Every active coarse generator has exactly two active clones: v and v+8.
        bybase={}
        for j,(v,p,g) in enumerate(a1):
            bybase.setdefault(v&7,[]).append(j)
        assert set(bybase)==set(coarse)
        assert all(len(js)==2 for js in bybase.values())
        # Product of the two clone duals is the dummy extension of the coarse dual.
        base_g={v:g for v,p,g in a0}
        for v,js in bybase.items():
            prod=[a1[js[0]][2][x]*a1[js[1]][2][x] for x in range(16)]
            target=[base_g[v][x&7] for x in range(16)]
            assert prod==target
        fine_agg={v:sum(p1[j] for j in js) for v,js in bybase.items()}
        d=mobius(V1,m)
        delta={v:0.0 for v in bybase}
        index_group=[a1[j][0]&7 for j in range(m)]
        for T in range(1,1<<m):
            touched={}
            for j in range(m):
                if T>>j&1:
                    touched[index_group[j]]=touched.get(index_group[j],0)+1
            ss=len(touched); total=T.bit_count()
            for v,t in touched.items():
                delta[v]+=d[T]*(t/total-1/ss)
        for v in coarse:
            err=abs((fine_agg[v]-coarse[v])-delta[v])
            max_formula_err=max(max_formula_err,err)
            red=abs(fine_agg[v]-coarse[v])
            if red>max_redis:
                max_redis=red
                witness={
                    "truth_integer":truth,
                    "truth_values_index_0_to_7":vals,
                    "coarse_active_generators":[x[0] for x in a0],
                    "fine_active_generators":[x[0] for x in a1],
                    "coarse_shapley":coarse,
                    "fine_orbit_aggregate":fine_agg,
                    "redistribution":{u:fine_agg[u]-coarse[u] for u in coarse},
                }
        assert abs(sum(fine_agg.values())-sum(coarse.values()))<1e-12
        checked+=1
    assert max_formula_err<2e-12
    return checked,max_formula_err,max_redis,witness

generic_cases,symmetric_cases,max_l1=exact_pair_split_checks()
parity_checks=exact_parity_block_selector_checks()
boolean_cases,max_formula_err,max_redis,witness=entropy_exhaustive()
out={
    "status":"PASS",
    "generic_exact_games_checked":generic_cases,
    "generic_globally_swap_symmetric_games_checked":symmetric_cases,
    "signed_parity_block_selector_exact_checks":parity_checks,
    "coupled_block_selector_group_conservation":"exact PASS",
    "coupled_block_selector_clone_halving_under_global_swap_symmetry":"exact PASS",
    "generic_arithmetic":"fractions.Fraction exact",
    "coefficient_l2_bound":"sum_g w_g(T)^2 <= 1/(8 s(T))",
    "largest_exact_l1_seen":str(max_l1),
    "boolean_functions_k3_extended_to_k4_checked":boolean_cases,
    "max_float_formula_error":max_formula_err,
    "max_orbit_shapley_redistribution_bits":max_redis,
    "counterexample_to_orbit_aggregate_invariance":witness,
}
print(json.dumps(out,indent=2,sort_keys=True))
