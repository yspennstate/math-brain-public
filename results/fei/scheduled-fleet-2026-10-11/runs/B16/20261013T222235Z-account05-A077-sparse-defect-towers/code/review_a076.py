import check as c
from fractions import Fraction as F
import json,time,hashlib
def main():
    start=time.perf_counter();cores=roots=trees=0
    for n in range(4):
        for mask in range(1<<(1<<n)):
            g=tuple(1 if mask>>x&1 else -1 for x in range(1<<n));a=c.spectrum(g);mu=a[0]
            for sign in [-1,1]:
                h=(sign,)*len(g);kinds=('X',)*n;f=c.wrap(g,h)
                rows=c.node(g,h,kinds)
                for i,(D,j,inh) in enumerate(rows):
                    ai=a[1<<i]
                    c.ck(c.nonneg(c.add(c.constant(abs(ai)),c.scale(D,-1))))
                    c.ck(c.nonneg(c.add(D,c.constant(abs(mu*ai)))))
                    c.ck(j==c.inf(g,i)/2)
                bx=c.add(c.scale(c.Phi((1+mu)**2,(1-mu)**2),F(1,4)),c.constant((1-mu*mu)/2))
                c.ck(c.B(f,0)==bx)
                c.ck(c.nonneg(c.add(c.constant(1-mu*mu),c.scale(bx,-1))))
                c.ck(1-mu*mu<=4*c.inf(f,0))
                R=c.add(c.constant(1-mu*mu),c.phi((1+mu)**2/4),c.phi((1-mu)**2/4),c.scale(c.phi(mu*mu),F(-1,2)))
                c.ck(c.H(f)==c.add(c.scale(c.H(g),F(1,2)),R))
                c.ck(c.scale(c.add(c.H(c.restrict(f,0,0)),c.H(c.restrict(f,0,1))),F(1,2))==c.scale(c.H(g),F(1,2)))
                for policy in ['first','last','partial']:
                    correction,inh,spent,leafI,leafH,leafcore,leafR=c.tree(g,h,kinds,policy)
                    c.ck(c.nonneg(c.add(c.constant(2*spent),c.scale(correction,-1))))
                    c.ck(c.nonneg(c.add(c.constant(2*spent),correction)))
                    c.ck(leafH==c.add(leafcore,leafR));trees+=1
                roots+=1
            cores+=1
    out={'helper_version':'A077-review-shift-v1','cores':cores,'wrappers':roots,'trees':trees,'assertions':c.COUNT,'elapsed_seconds':time.perf_counter()-start,'scope':'A076 stage-3 equations (1)-(8) only','verdict':'HOLDS_AT_REVIEWED_SCOPE_NO_REPAIR','author_code_used':False}
    p=c.ROOT/'out/review_a076.json';p.write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps(out));print('sha256',hashlib.sha256(p.read_bytes()).hexdigest())
if __name__=='__main__':main()
