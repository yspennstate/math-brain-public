import argparse,json,time
from fractions import Fraction as F
from pathlib import Path
import core as c
from check_endpoint import seed_stats
R=Path(__file__).resolve().parents[1]
def table(mask):return tuple(1 if mask>>s&1 else -1 for s in range(4))
def case(g,h,p):
    ch,st,_,_,_=seed_stats(h,p[:2]);w=st['V']
    q=(1+ch[0]['c'])/2
    go,gt,_,_,_=seed_stats(g,(q,p[2]))
    root_table=tuple(g[((h[s&3]+1)//2)+2*((s>>2)&1)] for s in range(8))
    root,rt,_,_,_=seed_stats(root_table,p)
    inf=sum(z['P'] for s,z in go.items() if s&1);a=inf/w
    s1=go[1]['P'];b=(inf-s1)/w
    T=s1/w*st['M']*(go[1]['j'] or 0)+b*st['J1']
    V={}
    if s1:c.logadd(V,2**go[1]['j']*abs(go[1]['c']),-2*s1/w*st['M'])
    V=c.plus((V,1),(st['L1'],b))
    C1=Chi=F(0)
    qg=c.paid_reference(go,gt);qh=c.paid_reference(ch,st);qt={0:root[0]['P']}
    for S,z in root.items():
        if not S:continue
        child=S&3;outer=(1 if child else 0)+(2 if S&4 else 0)
        qt[S]=qg[outer]*(qh[child]/w if child else 1)
        if not z['P']:continue
        local=go[outer]['j']+(ch[child]['j'] if child else 0)
        kappa=z['j']-local;c.ck(kappa>=0)
        if S.bit_count()==1:C1+=z['P']*kappa
        else:Chi+=z['P']*kappa
    c.ck(rt['I']-rt['V']==gt['I']-gt['V']+a*(st['I']-st['V']))
    c.ck(rt['J1']==gt['J1']+a*st['J1']-T+C1)
    c.ck(c.plus((c.ln4(C1),1),(rt['L1'],1),(V,1))==c.plus((gt['L1'],1),(st['L1'],a)))
    c.ck(rt['Jh']==gt['Jh']+a*st['Jh']+T+Chi)
    c.ck(c.plus((c.ln4(Chi),1),(rt['Lh'],1))==c.plus((gt['Lh'],1),(st['Lh'],a),(V,1)))
    c.ck(sum(qt.values())==1)
    c.ck(c.KL(root,qt)==c.plus((c.KL(go,qg),1),(c.KL(ch,qh),a)))
    Rtree=gt['R']+a*st['R'];Delta=rt['I']-rt['V']
    Ctree=2*Delta-Rtree
    B0=Ctree-gt['J1']-a*st['J1']
    c.ck(T+rt['J1']+B0==Ctree+C1)
    return C1>0
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--pilot',action='store_true');args=ap.parse_args()
    total=positive=0
    laws=((F(1,2),)*3,(F(1,3),F(3,5),F(3,4)))
    for p in laws[:1] if args.pilot else laws:
        for hm in ([1] if args.pilot else range(1,15)):
            for gm in range(16):positive+=case(table(gm),table(hm),p);total+=1
    result={'status':'PASS','cases':total,'nonzero_singleton_carry_cases':positive,'exact_assertions':c.CHECKS,'runtime_seconds':time.perf_counter()-c.START,'arithmetic':'Fraction physical composition and canonical prime-log identities'}
    (R/'out'/('REVIEW_PILOT.json' if args.pilot else 'REVIEW_CHECKS.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result))
