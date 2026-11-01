from rootlaw import check,F,OUT
import json,time
start=time.monotonic(); rows=[]
for m in range(2,9):
    P,I,v,D,K,q,h=check(m+1,[(0,i) for i in range(1,m+1)],[F(1,m)]*m)[1]
    caps={T:F(4)**(1-T.bit_count())/T.bit_count()**T.bit_count() for T in h}
    for T in h:
        physical=F(1,4*m)**T.bit_count()/D
        assert physical<=caps[T]
    remaining=F(1); p={T:F(0) for T in h}; threshold=None
    for T in sorted(h,key=h.get,reverse=True):
        p[T]=min(caps[T],remaining); remaining-=p[T]
        if remaining==0: threshold=h[T]; break
    assert remaining==0
    primal=sum(p[T]*h[T] for T in h)
    dual=threshold+sum(caps[T]*max(h[T]-threshold,0) for T in h)
    assert primal==dual and primal>=v
    assert primal-v<I/6
    rows.append({'m':m,'I':str(I),'uncapped_Gamma':str(max(h.values())-v),'capped_Gamma':str(primal-v),'capped_Gamma_over_I':str((primal-v)/I),'threshold':str(threshold),'LP_primal_equals_dual':True})
    assert time.monotonic()-start<60
result={'rows':rows,'elapsed_seconds':time.monotonic()-start,'verdict':'PASS all physical-law caps and exact LP primal-dual equality'}
(OUT/'caps.json').write_text(json.dumps(result,indent=2)); print(json.dumps(result,indent=2))
