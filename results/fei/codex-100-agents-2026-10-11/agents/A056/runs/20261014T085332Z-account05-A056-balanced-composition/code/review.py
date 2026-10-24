from check import *
def test(uc,vc,r,s,xpresent):
 u,v=table(2,uc),table(2,vc);p=Q(1,1<<r);q=Q(1,1<<s);a=1-mean(u);b=1-mean(v)
 f=[]
 for x in range(1<<(4+r+s+xpresent)):
  A=((x>>4)&((1<<r)-1))==0;B=((x>>(4+r))&((1<<s)-1))==0
  f.append(1 if xpresent and (x>>(4+r+s)) else u[x&3] if A else v[(x>>2)&3] if B else 1)
 f=tuple(f);i=4+r;w=Q(1,2) if xpresent else Q(1)
 d=w*(1-p)*q*b;kap=w*(1-p)*q*variance(v)
 assert edge_inf(f,i)==d
 if xpresent:
  Z=p*a+(1-p)*b*q
  residual=add({2:b*b*q*(1-2*q)*(1-p)/2},ep((1-Z/2)**2,d*d))
  residual=add(residual,ep((Z/2)**2,d*d));residual=add(residual,ep((a-b*q)**2,(b*q)**2),p*(1-p)/2)
 else:
  residual=add({2:b*b*q*(1-2*q)*(1-p)},ep((1-a*p-b*q*(1-p))**2,(b*q*(1-p))**2))
  residual=add(residual,ep((a-b*q)**2,(b*q)**2),p*(1-p))
 assert add(erasure(f,i),{2:-kap})==residual
 assert nonnegative(residual) and nonnegative(add({2:6*d},residual,-1))
def main():
 start=time.perf_counter();pilot='--pilot' in sys.argv;n=0
 for uc,vc in ([(7,1)] if pilot else [(u,v) for u in range(16) for v in range(16)]):
  for r in [1,2]:
   for s in [1,2]:
    for x in [False,True]:test(uc,vc,r,s,x);n+=1
 result={'source_claim':'A057-ALL-ORDER-TWO-EVENT-CONTROLLER-PAYMENT@1','review_scope':'Section1 equations1-2 erasure portion and Section3 equation4; NOT entire theorem','cases':n,'pilot':pilot,'arithmetic':'Fraction and prime-log exact identity; rational logarithm intervals','result':'ALL PASS','seconds':time.perf_counter()-start}
 (R/'out'/('review_pilot.json' if pilot else 'review.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
