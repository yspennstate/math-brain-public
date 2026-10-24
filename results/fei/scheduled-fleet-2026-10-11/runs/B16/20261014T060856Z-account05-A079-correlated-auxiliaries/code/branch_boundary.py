"""Explicit fixed n=4, independent exact nonproduct two-branch census."""
import itertools,json,time
from pathlib import Path
from fractions import Fraction as Q
from check import walsh,product_info,actual_fixture
ROOT=Path(__file__).resolve().parents[1]

def main():
    start=time.perf_counter(); gates=0; pairs=0; nonflat=[]; hist={}; first=None; assertions=0; equalities=0
    for code in range(32768):
        g=[1]+[1 if (code>>(x-1))&1 else -1 for x in range(1,16)]
        W=walsh(g)
        if product_info(W) is not None: continue
        admitted=False
        for bit in range(4):
            branches=[[W[s] for s in range(16) if ((s>>bit)&1)==b] for b in (0,1)]
            info=[product_info(a) for a in branches]
            if any(t is None for t in info): continue
            admitted=True; pairs+=1
            assert all(t[1]==0 for t in info); assertions+=1
            assert sum(v*v for v in branches[0])==128; assertions+=1
            H=Q(2+info[0][0]+info[1][0],2)
            I=Q(sum(v*v*s.bit_count() for s,v in enumerate(W)),256)
            assert H<=2*I; assertions+=1
            equalities+=(H==2*I)
            flat=len(set(abs(v) for v in W if v))==1
            if not flat:
                nonflat.append((code,bit))
                key=tuple(sorted(tuple(sorted((abs(v),a.count(v)+a.count(-v)))) for a in branches for v in set(abs(x) for x in a if x)))
                hist[str(key)]=hist.get(str(key),0)+1
                if first is None: first=(code,bit,g,W,branches,info)
        gates+=admitted
    result={'status':'PASS','actual_four_bit_gates_mod_output_sign':32768,
            'nonproduct_two_product_branch_gate_count':gates,'admitted_gate_branch_pairs':pairs,
            'nonflat_gate_branch_pair_count':len(nonflat),'nonflat_magnitude_histogram':hist,
            'all_admitted_branches_are_fair_products':True,
            'branch_probability_half_exact_checks':pairs,'H_equals_2I_pair_count':equalities,
            'assertions':assertions}
    if first:
        code,bit,g,W,branches,info=first
        F=[g[x>>2] for x in range(64)]
        rows,I=actual_fixture(F)
        assert product_info(rows[0][1]) is None
        branch_norms=[sum(v*v for v in a) for a in branches]
        p=[Q(v*v,256) for v in W]
        q=Q(branch_norms[1],256)
        degrees=[Q(sum(v*v*s.bit_count() for s,v in enumerate(a)),sum(v*v for v in a)) for a in branches]
        result['first_nonflat']={'code':code,'branch_coordinate':bit,'data_truth':g,'raw_data_Walsh':W,
            'branch_coefficients':branches,'branch_fair_nonfair_counts':[[a[0],a[1]] for a in info],
            'branch_probability':str(q),'branch_mean_degrees':[str(d) for d in degrees],
            'I':str(I),'H':'3','H_half':'2log2(3)','signed_address_gap':'-2log2(3)',
            'address_masses':['1','0','0','0'],
            'full_frequency_probabilities':[str(t) for t in p]}
        (ROOT/'out'/'nonflat_truth.json').write_text(json.dumps(F),encoding='utf-8')
    result['seconds']=time.perf_counter()-start
    (ROOT/'out'/'branch_boundary.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
