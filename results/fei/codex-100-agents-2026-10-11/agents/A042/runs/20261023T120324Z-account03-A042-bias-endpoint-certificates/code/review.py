import argparse,json
from fractions import Fraction as F
import check as helper
from check import ROOT,ck,spectrum,stats,KL,plus,cell

def all_reference(sp):
    w=sum(z['P'] for s,z in sp.items() if s); Z=sum(z['W'] for s,z in sp.items() if s)
    return {s:(z['P'] if not s else w*z['W']/Z if w else F(0)) for s,z in sp.items()}
def one(mask,p,ks):
    m=len(ks); es=tuple(F(1,2**k) for k in ks); e=F(1)
    for ej in es: e*=ej
    g=tuple(1 if mask>>s&1 else -1 for s in range(4))
    sp=spectrum(g,p); st=stats(sp); V=st['V']; a=(1-sp[0]['c'])/2
    table=tuple(g[x>>m] if (x&((1<<m)-1))==(1<<m)-1 else 1 for x in range(1<<(m+2)))
    sf=spectrum(table,es+p); ft=stats(sf)
    L=sum(1-ej for ej in es); D=sum(1-ej+ej*k for ej,k in zip(es,ks)); K=sum(ks)
    ck(ft['I']-ft['V']==e*(st['I']-V)+e*(4*a*L-4*a*a*(1-e)))
    if a==0:
        ck(ft['V']==ft['Jh']==ft['J1']==0); return
    ja=cell(a); b=F(1,4**ja)
    jobill=e*(4*a*D+4*a*a*(ja-1)*(1-e)-4*a*a*e*K)
    ck(ft['Jh']+ft['J1']==e*(st['Jh']+st['J1'])+jobill)
    ck(jobill<=3*e*(4*a*L-4*a*a*(1-e)))
    Zg=sum(z['W'] for T,z in sp.items() if T)
    Zf=sum(z['W'] for s,z in sf.items() if s)
    ck(Zf==e*Zg+4*b*e*(1-e))
    nu={}
    for U in range(1<<m):
        val=F(1)
        for j,ej in enumerate(es): val*=1-ej if U>>j&1 else ej
        nu[U]=val
    ck(sum(nu.values())==1)
    for T,z in sp.items():
        if not T: continue
        for U in range(1<<m):
            zz=sf[(T<<m)|U]
            ck(zz['P']==e*nu[U]*z['P'])
            if z['P']: ck(zz['j']==z['j']+U.bit_count()+sum(ks[j] for j in range(m) if not U>>j&1))
    for U in range(1,1<<m):
        zz=sf[U]; ck(zz['P']==4*a*a*e*nu[U])
        ck(zz['j']==ja+U.bit_count()-1+sum(ks[j] for j in range(m) if not U>>j&1))
    qf=all_reference(sf); ck(sum(qf.values())==1)
    if not V:
        ck(a==1); ck(all(qf[s]==z['P'] for s,z in sf.items())); return
    sg=all_reference(sp)
    outertable=tuple(-1 if (x&((1<<m)-1))==(1<<m)-1 and not x>>m&1 else 1 for x in range(1<<(m+1)))
    outer=spectrum(outertable,es+(1-a,)); qo=all_reference(outer)
    qt={0:sf[0]['P']}
    for s in range(1<<(m+2)):
        if not s: continue
        U=s&((1<<m)-1); T=s>>m
        qt[s]=qo[U|1<<m]*sg[T]/V if T else qo[U]
    ck(sum(qt.values())==1)
    ck(KL(sf,qt)==plus((KL(outer,qo),1),(KL(sp,sg),e)))
    w=ft['V']; s=4*a*a*e*(1-e)/w; t=4*b*e*(1-e)/Zf
    for label,z in sf.items():
        if not z['P']: continue
        T=label>>m
        if not label: ck(qf[label]==z['P']); continue
        if not T: ck(z['P']/qf[label]==s/t)
        else: ck(z['P']/qf[label]==(1-s)/(1-t)*(sp[T]['P']/V)/(sp[T]['W']/Zg))

if __name__=='__main__':
    parser=argparse.ArgumentParser(); parser.add_argument('--pilot',action='store_true'); args=parser.parse_args()
    laws=((F(1,2),F(1,2)),(F(1,3),F(2,5)))
    vectors=((1,),(2,),(1,1),(2,1),(1,1,1),(1,2,1))
    total=0
    for p in laws[:1] if args.pilot else laws:
        for ks in vectors[:1] if args.pilot else vectors:
            for mask in range(16): one(mask,p,ks); total+=1
    result={'status':'PASS','cases':total,'exact_assertions':helper.CHECKS,'runtime_seconds':helper.time.perf_counter()-helper.START,'source_code_copied_or_run':False,'arithmetic':'Fraction physical transform and prime-log full ordinary KL'}
    (ROOT/'out'/('REVIEW_PILOT.json' if args.pilot else 'REVIEW_CHECKS.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))
