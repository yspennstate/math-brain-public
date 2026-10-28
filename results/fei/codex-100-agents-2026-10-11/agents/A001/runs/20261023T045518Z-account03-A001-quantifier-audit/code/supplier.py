from common import *
import helpers
start=time.perf_counter();rows=[]
for r in range(3,9):
 t=F(1,1<<r);v=actual(2,r,(1,-1));P=spectrum(v);Q=source(2,r,F(1),(1,-1));I=totalinf(v);vv=F(1,4)+t+2*t*t
 ck(I==1+(r-3)*t and I<=F(17,16));ck(all(inf(v,j)>0 for j in range(r+1)))
 for j in range(r+1):ck(inf(v,j)==(t if j==0 or j>2 else F(1,2)-t))
 ck(F(1,4)<=vv<=F(13,32))
 Hformula=add((1,eta((F(1,2)+t)**2)),(3,eta((F(1,2)-t)**2)),(1,const(4*r*t-8*r*t*t)))
 ck(entropy(P)==Hformula)
 supplier=CE(P,Q);bound=F(19,32)*(r-1);ck(interval(add((1,supplier),(-1,const(bound))))[0]>0)
 ck(interval(add((1,supplier),(-1,const(F(19,34)*(r-1)*I))))[0]>0)
 rows.append({'r':r,'n':r+1,'I':str(I),'data_vacuum':str(vv),'entropy':rec(entropy(P)),'supplied_reference_CE':rec(supplier),'all_coordinates_relevant':True,'CE_over_I_lower':str(F(19,34)*(r-1))})
 ck(time.perf_counter()-start<55)
out={'status':'PASS','exact_assertions':helpers.count,'case_count':len(rows),'elapsed_seconds':time.perf_counter()-start,'rows':rows}
(RUN/'out/SUPPLIER_CHECK.json').write_text(json.dumps(out,indent=2),encoding='utf-8',newline='');print(json.dumps({k:v for k,v in out.items() if k!='rows'}))
