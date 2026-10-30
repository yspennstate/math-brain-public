"""Fixed positive inner-bank controls at rates0 and1, no dimension search."""
from drift import *
import drift

def maximum(ps):
    best={}
    for p in ps:
        diff=sub(p,best)
        if not diff:continue
        lo,hi=iv(diff)
        if lo>0:best=p
        elif hi<0:pass
        else:raise ArithmeticError('unresolved inner hull sign')
    return best
@lru_cache(None)
def rho(t,K):
    z=spectral(t);ps=[{},sub(z['H'],{2:K*z['I']})]
    for i in range(len(t).bit_length()-1):ps.append(mean([rho(restrict(t,i,b),K) for b in [0,1]]))
    return maximum(ps)
def components(z,K):return add(*(times(rho(t,K),q) for t,q in zip(z['ts'],z['q'])))
def bank(z,K):return add(z['C'],{2:6*z['I']},components(z,K))
def main():
    start=time.perf_counter();p=compose((g(3),g(2),g(2)));records=[]
    for K in [F(0),F(1)]:
        root=bank(p,K);nonnegative(root);nonnegative(add(root,{2:K*p['I']},times(p['H'],-1)))
        for j in range(3):
            for i in range(p['ns'][j]):
                kids=[]
                for b in [0,1]:
                    ts=list(p['ts']);ts[j]=restrict(ts[j],i,b);kids.append(compose(tuple(ts),p['outer']))
                ck(all(k['q'][j]==p['q'][j] for k in kids))
                for m in range(3):
                    if m!=j:ck(sum(k['q'][m] for k in kids)/2==p['q'][m])
                paid=sub(components(p,K),mean([components(k,K) for k in kids]));nonnegative(paid)
                bs=[bank(k,K) for k in kids];surplus=sub(root,mean(bs));nonnegative(surplus)
                ac=[add(b,surplus) for b in bs];ck(mean(ac)==root)
                for k,a in zip(kids,ac):nonnegative(a);nonnegative(add(a,{2:K*k['I']},times(k['H'],-1)))
                records.append(dict(K=str(K),core=j,coordinate=i,weighted_inner_bank=rec(components(p,K)),weighted_inner_release=rec(paid),whole_envelope_surplus=rec(surplus),child_credit=[rec(a) for a in ac]))
        ck(time.perf_counter()-start<55)
    out=dict(verdict='PASS',rates=['0','1'],query_rows=len(records),checks=drift.CHECKS,nonzero_inner_banks=True,runtime_seconds=time.perf_counter()-start,rows=records)
    save('INNER_BANK_CONTROLS.json',out);print(json.dumps({k:v for k,v in out.items() if k!='rows'}))
if __name__=='__main__':main()
