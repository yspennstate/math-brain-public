from raw_audit import *
import raw_audit as engine
def mul(a,b):
    z=[x*y for x in a for y in b];return min(z)//Q,-(-max(z)//Q)
def div(a,b):
    assert b[0]>0
    z=[F(x*Q,y) for x in a for y in b];return min(z).numerator//min(z).denominator,-(-max(z).numerator//max(z).denominator)
def main():
    start=time.perf_counter();ass=(-1,)*6;reach=F(1);a=rho(ass,63);rootA=a
    def S(ass):
        _,h,i,_,_=data(ass);return sub(scale((Q,Q),i),h)
    D=plus(S(ass),a);labels=[D];rows=[];leaves=[]
    for step,coord in enumerate((3,4,5,0)):
        mask=1<<coord if step<3 else sum(1<<i for i,v in enumerate(ass) if v<0)
        cs=kids(ass,mask,coord);rc=[rho(*c) for c in cs];u=[rho(c[0],sum(1<<i for i,v in enumerate(c[0]) if v<0)) for c in cs]
        avg=scale(plus(*rc),F(1,2));baseline=[plus(a,sub(r,avg)) for r in rc]
        n=[(max(0,z[0]),max(0,z[1])) for z in (sub(uu,cc) for uu,cc in zip(u,baseline))]
        # Two equal-weight siblings: f0=n0-n1,f1=n1-n0 is the sharp repair.
        flow=[sub(n[0],n[1]),sub(n[1],n[0])]
        if step<3:
            ck(sub(u[0],baseline[0])[0]>0);ck(n[1]==(0,0));credits=[u[0],sub(scale(a,F(2)),u[0])]
        else:
            ck(n==[(0,0),(0,0)]);credits=baseline
        childS=[S(c[0]) for c in cs];ds=[plus(s,z) for s,z in zip(childS,credits)];T=scale(plus(*ds),F(1,2));ck(T[0]>0)
        e=sub(scale(plus(*childS),F(1,2)),S(ass));alllabels=labels+[e];kernels=[div(d,T) for d in ds]
        outgoing=[[mul(L,k) for L in alllabels] for k in kernels]
        for d in ds:ck(d[0]>=0)
        for credit in credits:ck(credit[0]>=0)
        leaves.append({'path':[(i,0) for i in (3,4,5)[:step]]+[(coord,1)],'reach':str(reach/2),'assignment':cs[1][0],'H':data(cs[1][0])[1],'I':str(data(cs[1][0])[2]),'credit':credits[1],'debit':ds[1],'booked_labels':outgoing[1]})
        rows.append({'original_coordinate':coord,'reach':str(reach),'incoming_credit':a,'old_labels':labels,'e':e,'T':T,'local_baseline':baseline,'full_envelope_requirements':u,'minimum_credit_rerouting':flow,'credits':credits,'debits':ds,'child_label_kernels':kernels,'outgoing_booked_labels':outgoing,'outside_new_credit':0})
        ass=cs[0][0];a=credits[0];labels=outgoing[0];reach/=2
    leaves.append({'path':[(3,0),(4,0),(5,0),(0,0)],'reach':str(reach),'assignment':ass,'H':data(ass)[1],'I':str(data(ass)[2]),'credit':a,'debit':plus(S(ass),a),'booked_labels':labels})
    ck(sum(F(l['reach']) for l in leaves)==1)
    weighted=(0,0)
    for l in leaves:weighted=plus(weighted,scale(l['credit'],F(l['reach'])))
    ck(weighted[0]<=rootA[1] and rootA[0]<=weighted[1])
    result={'version':'actual-minimum-reroute-path-v1','rows':rows,'leaves':leaves,'initial_credit':rootA,'terminal_credit_mean_interval':weighted,'identity_status':'Exact by conditional-mean proof; interval overlap is diagnostic only.','nonnegative_credit_owner_transport':'each original owner L sends L*credit_child/credit_parent, including two original owners A/3 and2A/3; zero-parent owners vanish','runtime_seconds':time.perf_counter()-start,'checks':engine.checks,'outside_new_credit':0}
    (ROOT/'out/REPAIRED_POLICY.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps({k:result[k] for k in ['version','runtime_seconds','checks','outside_new_credit']}))
if __name__=='__main__':main()
