#!/usr/bin/env python3
from itertools import combinations

MAXP=229

def primes_upto(n):
    out=[]
    for p in range(2,n+1):
        if all(p%d for d in range(2,int(p**0.5)+1)):
            out.append(p)
    return out

def chi_table(p):
    q=[-1]*p
    q[0]=0
    for x in range(1,p):
        q[(x*x)%p]=1
    return q

def is_clique(C,p,chi):
    return all(chi[(a-b)%p]==1 for a,b in combinations(C,2))

def normalized_five_cliques(p,chi):
    H=[x for x in range(2,p) if chi[x]==1 and chi[(x-1)%p]==1]
    out=[]
    for ia,c in enumerate(H):
        for ib in range(ia+1,len(H)):
            d=H[ib]
            if chi[(d-c)%p]!=1:
                continue
            for e in H[ib+1:]:
                if chi[(e-c)%p]==1 and chi[(e-d)%p]==1:
                    out.append((0,1,c,d,e))
    return out

def common_neighbors(C,p,chi):
    S=set(C)
    return sum(1 for x in range(p) if x not in S and all(chi[(x-a)%p]==1 for a in C))

def curve_count(C,p,chi):
    s=0
    for x in range(p):
        prod=1
        for a in C:
            prod=(prod*((x-a)%p))%p
        s += chi[prod]
    # Smooth projective count: odd degree has one rational infinity;
    # monic even degree has two rational infinities.
    return p + (1 if len(C)%2 else 2) + s

def e2_of_direct_sum(factors):
    # factors are (e1,e2), where det(I+tM)=1+e1 t+e2 t^2+...
    ans=sum(e2 for e1,e2 in factors)
    for i in range(len(factors)):
        for j in range(i+1,len(factors)):
            ans += factors[i][0]*factors[j][0]
    return ans

def check_tate_identity():
    total=0
    primes_with5=0
    max_t5=0
    residues=set()
    for p in (q for q in primes_upto(MAXP) if q%4==1):
        chi=chi_table(p)
        cliques=normalized_five_cliques(p,chi)
        if not cliques:
            continue
        primes_with5 += 1
        local=0
        for C in cliques:
            assert is_clique(C,p,chi)
            t5=common_neighbors(C,p,chi)
            factors=[]
            # Fifteen elliptic factors: 10 triples and 5 quadruples.
            for r in (3,4):
                for S in combinations(C,r):
                    N=curve_count(S,p,chi)
                    assert N%16==0, (p,C,S,N)
                    a=p+1-N
                    assert (a-2)%4==0
                    e1=(a-2)//4
                    e2=N//16
                    factors.append((e1,e2))
            assert len(factors)==15
            # Genus-two factor Y_C. Pairwise-square branch differences imply
            # full rational 4-torsion by the standard x-T 2-descent criterion.
            N5=curve_count(C,p,chi)
            a1=p+1-N5
            assert (a1-4)%4==0, (p,C,N5,a1)
            e1Y=(a1-4)//4
            numer=p*p-1-4*e1Y
            assert numer%16==0
            e2Ymod4=(numer//16)%4
            factors.append((e1Y,e2Ymod4))
            e2=e2_of_direct_sum(factors)%4
            assert e2==(2*t5)%4, (p,C,t5,e2)
            residues.add(e2)
            max_t5=max(max_t5,t5)
            local+=1
        total += local
        print(f"p={p} normalized_five_cliques={local} tate_e2_identity=PASS")
    print(f"PRIMES_WITH_FIVE_CLIQUES={primes_with5}")
    print(f"TOTAL_NORMALIZED_FIVE_CLIQUES={total}")
    print(f"MAX_T5_OBSERVED={max_t5}")
    print(f"E2_MOD4_RESIDUES_OBSERVED={sorted(residues)}")
    assert total==12533 and primes_with5==17 and max_t5==10
    assert residues=={0}  # empirical t5-even through 229, not a theorem
    print("B7_B11_TATE_E2_IDENTITY_ALL=PASS")
    print("T5_EVEN_EQUIV_E2_DIV4_THROUGH_229=EMPIRICAL_PASS_NOT_THEOREM")

def e2_diag(vals):
    return sum(vals[i]*vals[j] for i in range(len(vals)) for j in range(i+1,len(vals)))%4

def check_gsp_congruence_models():
    # Congruence models only, not claimed to be Frobenius matrices of actual
    # abelian varieties. Each 2x2 block is diagonal symplectic, with
    # determinant equal to the desired multiplier mod 64 and F=I+4M.
    models=[]
    # p == 5 mod 64
    vals_even=[0,1]*17         # F block diag(1,5)
    vals_odd=[2,7]*17          # F block diag(9,29), 9*29 == 5 mod 64
    models.append((5,"even-model",vals_even,1,5))
    models.append((5,"odd-model",vals_odd,9,29))
    # p == 1 mod 64
    vals_even1=[0,0]*17        # F block diag(1,1)
    vals_odd1=[0,0]*3+[1,3]*14 # 3 trivial blocks, 14 diag(5,13), 5*13 == 1 mod64
    models.append((1,"even-model",vals_even1,1,1))
    models.append((1,"odd-model",vals_odd1,5,13))
    seen={}
    for pmod,name,vals,u,v in models:
        assert (u*v-pmod)%64==0
        assert u%4==1 and v%4==1
        e2=e2_diag(vals)
        trF=(34+4*sum(vals))%64
        formal_count=(pmod+1-trF)%64
        assert e2 in (0,2)
        assert formal_count == (32 if e2==0 else 0)
        seen.setdefault(pmod,set()).add(e2)
        print(f"GSP64 pmod64={pmod} {name} e2mod4={e2} formal_count_mod64={formal_count} PASS")
    assert seen[5]=={0,2} and seen[1]=={0,2}
    print("B7_GENERIC_GSP64_DOES_NOT_FIX_HALF_E2=PASS")

def check_fixed_level_parity_nogo():
    # Toggling every one of the 2^k exact Boolean atoms preserves every
    # zeta/moment parity of order < k, but flips the top atom parity.
    for k in range(6,11):
        full=(1<<k)-1
        for r in range(0,6):
            for S in combinations(range(k),r):
                mask=sum(1<<i for i in S)
                count=sum(1 for atom in range(1<<k) if atom & mask == mask)
                assert count%2==0, (k,S,count)
        top_count=sum(1 for atom in range(1<<k) if atom & full == full)
        assert top_count==1
        print(f"k={k} moments_orders_0_to_5_preserved_by_all_atom_toggle=PASS top_flips=PASS")
    print("B27_FIXED_LEVEL_PARITY_HIERARCHY_CANNOT_DETERMINE_TOP_ATOM=PASS")

if __name__=="__main__":
    check_tate_identity()
    check_gsp_congruence_models()
    check_fixed_level_parity_nogo()
    print("ALL_I0099_TATE_LEVEL5_SELF_CHECKS_PASS")
