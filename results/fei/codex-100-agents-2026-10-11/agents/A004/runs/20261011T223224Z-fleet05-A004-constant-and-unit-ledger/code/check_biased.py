from check_ledger import F, ck, add, mul, log, entropy, upper, ln_interval, ROOT
import check_ledger as L
from itertools import product
import json,time
def main():
    start=time.perf_counter(); cases=0; gate_checks=0; examples=[]
    biases=[F(1,2),F(1,4),F(1,8),F(1,1024)]
    for ps in product(biases,repeat=2):
        weights=[mathprod(ps[i] if x>>i&1 else 1-ps[i] for i in range(2)) for x in range(4)]
        for mask in range(16):
            t=[1 if mask>>x&1 else -1 for x in range(4)]
            probs=[]; indicator=[]; scales=[]
            for s in range(4):
                moment=sum((weights[x]*t[x]*mathprod(F((x>>i)&1)-ps[i] for i in range(2) if s>>i&1) for x in range(4)),F(0))
                norm=mathprod(ps[i]*(1-ps[i]) for i in range(2) if s>>i&1)
                probs.append(moment*moment/norm)
                gm=sum((weights[x]*F(t[x]+1,2)*mathprod(F((x>>i)&1)-ps[i] for i in range(2) if s>>i&1) for x in range(4)),F(0))
                indicator.append(gm*gm/norm); scales.append(4**s.bit_count()*norm)
            ck(sum(probs)==1)
            pivotal=[sum((weights[x] for x in range(4) if t[x]!=t[x^(1<<i)]),F(0)) for i in range(2)]
            spectral=[sum((probs[s] for s in range(4) if s>>i&1),F(0)) for i in range(2)]
            for i in range(2):
                ck(spectral[i]==4*ps[i]*(1-ps[i])*pivotal[i])
                resampled=sum((weights[x]*((1-ps[i]) if x>>i&1 else ps[i]) for x in range(4) if t[x]!=t[x^(1<<i)]),F(0))
                ck(resampled==spectral[i]/2)
            ck(all(probs[s]==4*indicator[s] for s in range(1,4)))
            v=1-probs[0]; it=sum(spectral); deficit=it-v; ck(deficit>=0)
            corrected=add(*(mul(probs[s],log(scales[s]/probs[s])) for s in range(1,4) if probs[s]))
            ck(all(probs[s]<=scales[s] for s in range(1,4)))
            H=entropy(probs)
            ck(corrected==add(entropy(probs[1:]),*(mul(spectral[i],log(4*ps[i]*(1-ps[i]))) for i in range(2))))
            if mask in (6,9):
                upper(corrected,2/ln_interval(F(2))[1]*deficit); gate_checks+=1
            if mask in (1,7,8,14):
                upper(corrected,(2+4/ln_interval(F(2))[1])*deficit); gate_checks+=1
            if mask==10:
                ck(not corrected and deficit==0)
                if ps[0]!=F(1,2): ck(L.bounds(H)[0]>0)
                examples.append({'p':str(ps[0]),'spectral_influence':str(spectral[0]),'pivotal_influence':str(pivotal[0]),'deficit':str(deficit),'corrected_entropy':0,'ordinary_entropy':{str(k):str(c) for k,c in H.items()}})
            cases+=1
    out={'status':'PASS','cases':cases,'gate_inequality_certificates':gate_checks,'assertions':L.checks,'runtime_seconds':time.perf_counter()-start,'biased_dictator_records':examples,'scope':'Finite normalization and gate calibration; not arbitrary weighted-threshold FEI+'}
    (ROOT/'out'/'biased_validation.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8'); print(json.dumps({k:out[k] for k in ['status','cases','assertions','runtime_seconds']}))
def mathprod(xs):
    out=F(1)
    for x in xs:out*=x
    return out
if __name__=='__main__':main()
