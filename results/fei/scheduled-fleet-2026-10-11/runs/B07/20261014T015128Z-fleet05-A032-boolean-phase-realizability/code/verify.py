import json,time,sys,math
from fractions import Fraction as F
from collections import Counter
from pilot import ROOT,OLD,STAGE3,affine_sign
sys.path.insert(0,str(OLD/'code'))
from certify_pure import log_interval,signature_interval
def direct(h):return [sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(h)) for s in range(len(h))]
def cube(mask,m=4):
    xs=[x for x in range(1<<m) if mask>>x&1]
    assert xs
    fixed=[(j,xs[0]>>j&1) for j in range(m) if all((x>>j&1)==(xs[0]>>j&1) for x in xs)]
    assert len(xs)==1<<(m-len(fixed))
    return fixed
def main():
    start=time.monotonic();rows=json.loads((OLD/'out/mixed_slices_m4.json').read_text())['records'];aff=0;types=Counter()
    for r in rows:
        W=direct(r['truth_h']);good,detail=affine_sign(W)
        if not good:continue
        aff+=1;h=r['truth_h'];M=r['mixed_mask'];E=r['pure_mask']
        if M and E:
            f=cube(M);ef=cube(E);lf=cube(M|E);assert len(f)==len(ef)==len(lf)+1
            assert M.bit_count()==E.bit_count()
            assert len(set(f)^set(ef))==2;types['nonfair_2_1_indicator']+=1
        elif M: cube(M);types['unit_indicator']+=1
        else: cube(E);types['double_indicator']+=1
    assert aff==1536
    covers=json.loads((ROOT/'out/heavy_cover.json').read_text());positive=[]
    for r in covers['objective_signatures']:
        if r['Q_numerator']:
            assert r['masses']==[40,8,8,8] and r['Q_numerator']==40 and r['address_numerator']==32
            positive.append(r)
    assert len(positive)==1
    truth=[-1]+[1]*7;W=direct(truth);hs=[];marg=[];masses=[];Q=F(0)
    for J in range(4):
        h=[sum(truth[y+4*x]*(-1 if (J&y).bit_count()%2 else 1) for y in range(4))//2 for x in range(2)]
        assert affine_sign(direct(h))[0];hs.append(h)
        a=[W[J]**2,W[J+4]**2];z=sum(a);p=F(a[1],z);w=F(z,64)
        masses.append(w);marg.append(p);Q+=w*int(p not in (0,F(1,2),1))
    addr=sum(masses[J]*J.bit_count() for J in range(4));data=sum(masses[J]*marg[J] for J in range(4))
    assert masses==[F(5,8),F(1,8),F(1,8),F(1,8)] and Q==F(5,8) and addr==F(1,2) and data==F(1,4)
    a,b=log_interval(5);denlo,denhi=28-5*b,28-5*a;assert denlo>10
    witness=json.loads((STAGE3/'out/witness.json').read_text());cycles=[]
    for J,h in enumerate(witness['slices_h']):
        W=direct(h);good,d=affine_sign(W)
        if not good:
            circuit=d['four_cycle'];assert math.prod(1 if W[s]>0 else -1 for s in circuit)==-1
            cycles.append({'row_label':J,'circuit':circuit,'Walsh_values':[W[s] for s in circuit],'affine_phase_sign_product_required':1,'actual_sign_product':-1})
    assert len(cycles)==2
    # Exact nonlinear common identity on both actual Boolean witnesses.
    for slices in (hs,witness['slices_h']):
        for x in range(len(slices[0])):assert len({4*h[x]**2-h[x]**4 for h in slices})==1
    out={'status':'PASS','direct_rows_checked':len(rows),'admitted_affine_rows':aff,'row_types':dict(types),'cover_signatures':len(covers['objective_signatures']),'positive_Q_signatures':1,'sharp_K_exact':'5/(28-5log2(5))','sharp_K_rational_interval':[str(F(5)/denhi),str(F(5)/denlo)],'three_bit_truth':truth,'three_bit_Walsh':direct(truth),'three_bit_slices_h':hs,'masses':list(map(str,masses)),'conditional_marginals':list(map(str,marg)),'Q':str(Q),'I_address':str(addr),'I_data':str(data),'previous_extremizer_four_cycle_obstructions':cycles,'seconds':time.monotonic()-start,'external_review':'PENDING; author alternate implementation only'}
    (ROOT/'out/validation.json').write_text(json.dumps(out,indent=2));print(json.dumps({k:v for k,v in out.items() if k not in ('sharp_K_rational_interval','previous_extremizer_four_cycle_obstructions')}))
if __name__=='__main__':main()
