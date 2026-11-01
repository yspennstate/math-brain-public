from arithmetic import *
R=Path(__file__).resolve().parents[1]
def rv(c,u,v):
 p=Q(sum(c),len(c));return add(scale(phi(p),variance(u)),phi(1-p),variance(v))
def root(c,u,v):return tuple(u[(x>>2)&1] if c[x&3] else v[(x>>3)&1] for x in range(16))
def main():
 start=time.perf_counter();cnt=0;sharp=None
 for cc in range(16):
  c=tuple((1-z)//2 for z in table(2,cc));p=Q(sum(c),4)
  for uc in range(4):
   u=table(1,uc)
   for vc in range(4):
    v=table(1,vc);F=root(c,u,v);reserve=rv(c,u,v)
    for i in range(4):
     if i<2:
      cs=[restrict(c,i,b) for b in [0,1]];child=add(rv(cs[0],u,v),rv(cs[1],u,v),Q(1));child=scale(child,Q(1,2))
      L=add(reserve,child,-1);assert sign(L)>=0;assert sign(add({2:2*edge_inf(F,i)},L,-1))>=0
      if L=={2:Q(1)} and edge_inf(F,i)==Q(1,2):sharp={'controller_code':cc,'u_code':uc,'v_code':vc,'release':ser(L),'query_influence':'1/2','ratio':'2'}
     else:
      uu=u if i==2 else v;other=v if i==2 else u;q=p if i==2 else 1-p
      us=[restrict(uu,0,b) for b in [0,1]]
      child=add(rv(c,us[0],other),rv(c,us[1],other)) if i==2 else add(rv(c,other,us[0]),rv(c,other,us[1]))
      L=add(reserve,scale(child,Q(1,2)),-1);assert L==scale(phi(q),spectrum(uu)[1]**2)
     cnt+=1
 assert sharp
 result={'claim_id':'A057-INTERLEAVED-SELECTOR-RESERVE','version':1,'scope':'Section1 release/telescope only; independent of A056 upstream cap premise','verdict':'ACCEPT_SCOPED_WITHOUT_REPAIR','roots':256,'exact_release_checks':cnt,'sharp_fixture':sharp,'result':'ALL PASS','seconds':time.perf_counter()-start}
 (R/'out/review_release.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
