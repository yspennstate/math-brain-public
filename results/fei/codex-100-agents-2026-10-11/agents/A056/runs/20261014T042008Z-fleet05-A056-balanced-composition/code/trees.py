from check import *
def step(c,g,h,rg,rh,dims,i):
 f=family(c,g,h,dims);Z=reference(c,g,h,rg,rh,dims);ff,refs,E,O=lift(f,Z,i,zero_kernel(c,g,h,dims,i))
 states=tuple(children(c,g,h,rg,rh,dims,i));release=add(E,O);debt={}
 for j,child in enumerate(states):
  cc,gg,hh,rr,ss,dd=child;new=reference(cc,gg,hh,rr,ss,dd)
  inherited,C=cal(probs(ff[j]),refs[j],labels(dd));assert inherited==new
  release=add(release,C,Q(1,2));debt=add(debt,kl(probs(ff[j]),new),Q(1,2))
 assert kl(probs(f),Z)==add(release,debt)
 return states,release,debt
def main():
 start=time.perf_counter();count=0
 cs=[tuple((1-v)//2 for v in table(1,k)) for k in range(4)]+[(1,0,0,0),(0,1,1,1)]
 for c in cs:
  dims=(len(c).bit_length()-1,1,1,1)
  for gc,hc in [(6,12),(7,1),(12,10),(0,15)]:
   g=table(2,gc);h=table(2,hc)
   for weighted in [False,True]:
    rg=seed(g,1,weighted);rh=seed(h,1,weighted);rootdebt=kl(probs(family(c,g,h,dims)),reference(c,g,h,rg,rh,dims))
    for policy in range(4):
     i=0 if policy==0 else 1 if policy==2 else sum(dims)-1
     states,r0,_=step(c,g,h,rg,rh,dims,i);total=r0;leaves={}
     for j,state in enumerate(states):
      dd=state[-1]
      ii=sum(dd)-1 if j==0 and policy in [0,2] else 0 if (policy==0 or j==0) else dd[1] if policy==1 else sum(dd)-dd[0]-1 if policy==3 else 0
      _,r1,d1=step(*state[:-1],dd,ii)
      total=add(total,r1,Q(1,2));leaves=add(leaves,d1,Q(1,2))
     assert rootdebt==add(total,leaves);count+=1
 result={'helper_version':'A056-history-stopped-v1','stopped_trees':count,'physical_reference_transports':3*count,'actual_terminal_references':4*count,'result':'ALL PASS','seconds':time.perf_counter()-start}
 (R/'out/trees.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
