import json,sys,math,time
from fractions import Fraction as F
from collections import Counter
from pilot import ROOT,OLD,load,walsh
sys.path.insert(0,str(OLD/'code'))
from certify_pure import signature_interval
from cover_search import prime_factors
def signature(ks,address):
    s=Counter({2:F(6)+F(address,64)})
    for k in ks:
        if k:
            for p,e in prime_factors(k).items():s[p]-=F(k*e,64)
    return s
def main():
    start=time.monotonic();data=json.loads((ROOT/'out/heavy_cover.json').read_text());rows=load()
    best=data['best'];star=signature(best['masses'],best['address_numerator']);assert best['Q_numerator']==64
    certs=[]
    for r in data['objective_signatures']:
        d=signature(r['masses'],r['address_numerator'])
        for p,v in star.items():d[p]-=F(r['Q_numerator'],64)*v
        d={p:v for p,v in d.items() if v}
        if d:
            lo,hi=signature_interval(tuple(d.items()));assert lo>0
            certs.append({'masses':r['masses'],'Q_numerator':r['Q_numerator'],'verdict':'STRICT','positive_lower_bound':str(lo)})
        else:certs.append({'masses':r['masses'],'Q_numerator':r['Q_numerator'],'verdict':'EXACT_EQUALITY'})
    hs=[rows[i]['truth_h'].copy() for i in best['row_indices']]
    hs.sort(key=lambda h:sum(t*t for t in h),reverse=True)
    M=best['mixed_mask'];x=(M&-M).bit_length()-1
    if math.prod(h[x] for h in hs)==1:hs[0]=[-t for t in hs[0]]
    truth=[sum(hs[J][x]*(-1 if (J&y).bit_count()%2 else 1) for J in range(4))//2 for x in range(16) for y in range(4)]
    # Direct independent character sums, including inverse without integer truncation.
    assert all(sum(hs[J][x]*(-1 if (J&y).bit_count()%2 else 1) for J in range(4)) in (-2,2) for x in range(16) for y in range(4))
    W=[sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(truth)) for s in range(64)]
    assert set(truth)<= {-1,1} and sum(v*v for v in W)==4096
    masses=[F(sum(W[J+4*s]**2 for s in range(16)),4096) for J in range(4)]
    marginals=[]
    for J in range(4):
        z=sum(W[J+4*s]**2 for s in range(16));a=[W[J+4*s]**2 for s in range(16)]
        marg=[sum(a[s] for s in range(16) if s>>i&1) for i in range(4)]
        assert all(a[s]*z**3==math.prod(marg[i] if s>>i&1 else z-marg[i] for i in range(4)) for s in range(16))
        assert sum(t not in (0,z) and 2*t!=z for t in marg)==1
        marginals.append([str(F(t,z)) for t in marg])
    addressI=sum(F(sum(truth[x]!=truth[x^(1<<i)] for x in range(64)),64) for i in range(2))
    assert masses==[F(17,32),F(5,32),F(5,32),F(5,32)] and addressI==F(5,8)
    lo,hi=signature_interval(tuple(star.items()));assert lo>2 # certifies Kstar<1/2
    witness={'truth_table':truth,'bit_order':'address bits0,1; data bits2..5; masks0..63','walsh_integers':W,'slices_h':hs,'masses':list(map(str,masses)),'conditional_marginals':marginals,'Q':'1','I_address':str(addressI),'K_exact':'1/(45/8-(17*log2(17)+15*log2(5))/32)','K_interval':[str(1/hi),str(1/lo)]}
    (ROOT/'out/witness.json').write_text(json.dumps(witness,indent=2))
    out={'status':'PASS','objective_count':len(certs),'strict_count':sum(c['verdict']=='STRICT' for c in certs),'equal_count':sum(c['verdict']=='EXACT_EQUALITY' for c in certs),'K_less_than_one_half':True,'certificates':certs,'seconds':time.monotonic()-start,'independent_review':'PENDING; author direct transform is not external review'}
    (ROOT/'out/certificate.json').write_text(json.dumps(out,indent=2));print(json.dumps({k:v for k,v in out.items() if k!='certificates'}))
if __name__=='__main__':main()
