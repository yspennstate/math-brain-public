"""Independent physical truth-core reconstruction of the new A089 terminal signs.
Does not execute A089's implementation or accept its whole-history allocations.
"""
from bridge import *
from itertools import product
import hashlib

def truth_core(fixed):
    free=[j for j in range(6) if j not in fixed]
    truth=[]
    for x in range(1<<len(free)):
        original=sum(v<<j for j,v in fixed.items())+sum(((x>>i)&1)<<j for i,j in enumerate(free))
        truth.append(-1 if original in {0,1,2} else 1)
    N=len(truth);ww=ar.fwht(truth);hg=ar.entropy(ww)
    influence=sum(Q(2*sum(truth[x]!=truth[x|(1<<j)] for x in range(N) if not(x>>j&1)),N) for j in range(len(free)))
    spectral=sum(Q(w*w,N*N)*i.bit_count() for i,w in enumerate(ww))
    ar.ck(influence==spectral and sum(w*w for w in ww)==N*N)
    return Q(truth.count(-1),N),influence,hg

def main():
    start=time.perf_counter()
    source=ROOT.parent.parent.parent/'A089/runs/20261022T225420Z-fleet03-A089-repair-specialist'
    spec={'helper':'own arithmetic.py + block_reveal.outer; direct original-six-bit truth restrictions',
      'family':'same actual J(g_6^6), block0 bits2,0,3 fixed zero; block1 bit0=b; block0 original4,5 independently unset/0/1',
      'domain':{'b':[0,1],'bit4':[None,0,1],'bit5':[None,0,1]},'case_count':18,'symmetry':'none',
      'arithmetic':'exact FWHT and direct physical edge influence; exact occupied-set chain rule; directed rational logs',
      'memory_estimate_mb':100,'maximum_runtime_seconds':55,
      'source_sha256':{name:hashlib.sha256((source/name).read_bytes()).hexdigest() for name in ['REPORT.md','CLAIMS.json']},
      'scope':'generic signed-capacity theorem on positive-weight support and all18 physical S signs only; source four coupled order histories NOT independently accepted here'}
    (ROOT/'out/REVIEW_SIGNED_SPEC.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
    base=truth_core({});rows=[]
    for b,x,y in product([0,1],[None,0,1],[None,0,1]):
        fixed={2:0,0:0,3:0}
        for j,v in [(4,x),(5,y)]:
            if v is not None:fixed[j]=v
        cores=[truth_core(fixed),truth_core({0:b})]+[base]*4
        C,q,masses=outer([c[0] for c in cores]);hh=C.copy();ii=Q(0)
        for j,c in enumerate(cores):hh=ar.add(hh,c[2],q[j]);ii+=q[j]*c[1]
        ss=ar.add({2:4*ii},hh,Q(-1));bounds=iv(ss)
        negative=(x==0 and y==0)
        ar.ck(bounds[1]<0 if negative else bounds[0]>0)
        row={'b':b,'bit4':x,'bit5':y,'I':str(ii),'S':val(ss),'negative':negative}
        if negative:
            A=ineg(bounds);lo,hi=([Q(55,1000),Q(56,1000)] if b==0 else [Q(45,1000),Q(46,1000)])
            ar.ck(lo<A[0]<=A[1]<hi);row['subsidy']=saveiv(A)
        rows.append(row)
        (ROOT/'out/REVIEW_SIGNED.json').write_text(json.dumps({'spec':spec,'rows':rows,'checks':ar.checks,'seconds':time.perf_counter()-start},indent=2)+'\n',encoding='utf-8')
    assert time.perf_counter()-start<55
    print(json.dumps({'states':len(rows),'negative_states':[{k:r[k] for k in ['b','S','subsidy']} for r in rows if r['negative']],'checks':ar.checks,'seconds':time.perf_counter()-start}),flush=True)

if __name__=='__main__':main()
