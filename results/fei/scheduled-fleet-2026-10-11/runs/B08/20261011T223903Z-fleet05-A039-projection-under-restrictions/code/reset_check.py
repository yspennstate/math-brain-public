import check as c
from fractions import Fraction as F
import json, time

start=time.perf_counter(); rows=[]
for k in [4,6,8]:
    b=[(-1)**sum(((x>>(2*j))&1)*((x>>(2*j+1))&1) for j in range(k//2)) for x in range(1<<k)]
    bp=b.copy(); bp[0]=-bp[0]
    core=[b[x>>1] if x&1==0 else bp[x>>1] for x in range(1<<(k+1))]
    r=2*k; p=F(1,1<<r)
    st={name:c.state(tab,k,r) for name,tab in [('b',b),('bprime',bp),('selector',core)]}
    for name,z in st.items():
        rem=z['d'][-1]; ae=(1-2*rem)**2; qe=(1+ae)/2; ka=ae/(1+ae)
        J=c.minus((F(1),F(1)),c.weighted(c.hiv(ka),qe))
        G=(F(0),F(0))
        for x in z['d'][:-1]: G=c.plus(G,c.minus(c.hiv(x),c.weighted(c.hiv(2*x),F(1,2))))
        re=__import__('math').prod(1-x for x in z['d'][:-1]); qa=1-re*(1-ka)
        dout=c.minus((-F(1),-F(1)),c.weighted(c.log2(qa*(1-qa)),F(1,2)))
        db=c.plus(dout,c.minus(J,G))
        rows.append({'k':k,'query':'control_'+name,'J_over_removed':c.decimal(c.div(J,(rem,rem))),'G_over_removed':c.decimal(c.div(G,(rem,rem))),'D_out_over_removed':c.decimal(c.div(dout,(rem,rem))),'Bayes_reset_over_removed':c.decimal(c.div(db,(rem,rem)))})
        c.check(J[0]>0 and G[0]>0 and db[1]<0)
    cb=c.walsh(b); cp=c.walsh(bp); parent=st['selector']; dr=parent['d'][1:]
    rd=c.product(dr[:k]); rz0=__import__('math').prod(1-x for x in dr[k:])
    hq=(F(0),F(0)); qref=F(0)
    for T in range(1<<k):
        if T:
            ga=p*cb[T]; ha=p*cp[T]; qq=(ga*ga+ha*ha)/2
            hq=c.plus(hq,c.weighted(c.eta(qq),1<<r)); qref+=rd[T]*ga*ga/(ga*ga+ha*ha)
        else:
            ga=p*(cb[0]-1); ha=p*(cp[0]-1); qq=(ga*ga+ha*ha)/2
            hq=c.plus(hq,c.weighted(c.eta(qq),(1<<r)-1))
            qref+=rd[0]*(1-rz0)*ga*ga/(ga*ga+ha*ha)
            ga+=1; ha+=1; qq=(ga*ga+ha*ha)/2
            hq=c.plus(hq,c.eta(qq)); qref+=rd[0]*rz0*ga*ga/(ga*ga+ha*ha)
    J=c.minus(hq,c.weighted(c.plus(st['b']['H'],st['bprime']['H']),F(1,2)))
    G=(F(0),F(0))
    for x,a,h in zip(dr,st['b']['d'],st['bprime']['d']):
        G=c.plus(G,c.minus(c.hiv(x),c.weighted(c.plus(c.hiv(a),c.hiv(h)),F(1,2))))
    dout=c.minus((-F(1),-F(1)),c.weighted(c.log2(qref*(1-qref)),F(1,2)))
    db=c.plus(dout,c.minus(J,G)); rem=parent['d'][0]
    rows.append({'k':k,'query':'selector','J_over_removed':c.decimal(c.div(J,(rem,rem))),'G_over_removed':c.decimal(c.div(G,(rem,rem))),'D_out_over_removed':c.decimal(c.div(dout,(rem,rem))),'Bayes_reset_over_removed':c.decimal(c.div(db,(rem,rem)))})
    c.check(J[0]>0 and G[0]>0)
out={'status':'PASS','assertions':c.COUNT,'runtime_seconds':time.perf_counter()-start,'rows':rows,'scope':'12 root reference resets, same frozen k=4,6,8 family'}
(c.ROOT/'out'/'RESET_VALIDATION.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({x:v for x,v in out.items() if x!='rows'}))
