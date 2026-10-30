from check import R, require, walsh, ce, combine, bounds, BASE
import check
import json, time

start=time.perf_counter(); results=[]
for k in (4,6,8,10,12):
    delta=R(1,1<<k); e=R(1,1<<(k//2))
    hb={}; hbp={}; hh={}; bz={}
    for sigma in (1,-1):
        count=((1<<k)+sigma*(1<<(k//2)))//2
        a=(sigma*e-delta)**2; b=delta**2; q=a+b
        hb=combine((1,hb),(count,ce([delta],[delta])))
        t=(sigma*e-2*delta)**2
        hbp=combine((1,hbp),(count,ce([t],[t])))
        hh=combine((1,hh),(count,ce([a,b],[a,b])))
        bz=combine((1,bz),(count,ce([a,b],[a/q,b/q])))
        require(a>=R(9,16)*delta)
    extra=combine((1,hh),(-R(1,2),hb),(-R(1,2),hbp))
    credit=combine((1,extra),(-1,bz))
    require(bounds(credit)[0]>=0)
    target={2:delta*k}
    check.addlog(target,R(16,9),-delta)
    require(bounds(combine((1,bz),(-1,target)))[0]>0)
    if k in (4,6):
        table=[(-1)**sum(((x>>j)&1)*((x>>(j+1))&1) for j in range(0,k,2)) for x in range(1<<k)]
        flip=list(table); flip[0]=-flip[0]
        ab=walsh(table); af=walsh(flip)
        require(all(y==x-2*delta for x,y in zip(ab,af)))
        require(all(x*x==delta for x in ab))
        mux=table+flip; p=[x*x for x in walsh(mux)]
        require(not combine((1,ce(p,p)),(-1,hh)))
    lo,hi=bounds(extra)
    results.append({'k':k,'influence_selector':str(delta),'delta_over_selector_interval':[str(lo/delta),str(hi/delta)],'analytic_lower':'k-log2(16/9)'})
out={'status':'PASS','cases':5,'assertions':check.checks,'seconds':time.perf_counter()-start,'results':results}
(BASE/'out'/'BOUNDARY_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='results'}))
