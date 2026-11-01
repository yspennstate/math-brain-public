from pathlib import Path
import json,time,sys
import exact as E
from exact import F
ROOT=Path(__file__).resolve().parents[1]
def run_tree(f,S,Q,D,shape):
 leaves=[];B={}
 def visit(g,s,q,d,w,depth,path):
  nonlocal B
  stop=depth==2 or (depth==1 and (shape==0 or (shape==1 and path[-1]==1)))
  if stop:
   p=E.spectrum(g);fresh=E.calibrate(s,p[0])
   E.ck(sum(s)==sum(q)==sum(fresh)==1)
   E.ck(all(x>=y for x,y in zip(s,d)))
   E.ck(E.nonpositive(E.sub(E.ce(p,fresh),E.ce(p,d))))
   leaves.append((p,s,q,d,fresh,w,path));return
  j=0 if depth==0 else (path[-1]%(len(g).bit_length()-1))
  B=E.add(B,E.scale(E.erasure(g,j),w))
  for v in (0,1):visit(E.child(g,j,v),E.marginal(s,j),E.marginal(q,j),E.marginal(d,j),w/2,depth+1,path+(v,))
 visit(f,S,Q,D,F(1),0,())
 return B,leaves
def main():
 t=time.perf_counter();pilot='--pilot' in sys.argv;n=2 if pilot else 3
 instances=policies=nonconstant=positive=0
 codes=list(range(1<<(1<<n))) if pilot else list(range(32))+[85,90,105,150,165,170,240,255]
 for code in codes:
  f=tuple(-1 if code>>x&1 else 1 for x in range(1<<n));p=E.spectrum(f);m=p[0]
  for S in E.references(p):
   D=tuple(s if x else F(0) for s,x in zip(S,p));E.ck(D[0]==m);c=E.ce(p,D)
   for gamma in (F(1,2),F(1)):
    L=E.scale(E.logform(gamma),-1);base=tuple(m if i==0 else gamma*D[i] for i in range(len(D)));rem=1-sum(base)
    for fill in (0,1):
     if fill==0:Q=(base[0]+rem,)+base[1:]
     else:Q=tuple(v+rem/len(base) for v in base)
     E.ck(sum(Q)==1);E.ck(Q[0]>=m);E.ck(all(Q[i]>=gamma*D[i] for i in range(1,len(D))))
     instances+=1
     for shape in range(3):
      B,leaves=run_tree(f,S,Q,D,shape)
      virtual=B
      for pp,ss,qq,dd,ff,w,path in leaves:virtual=E.add(virtual,E.scale(E.ce(pp,dd),w))
      E.ck(E.nonpositive(E.sub(virtual,c)))
      E.ck(sum(w*(1-pp[0]) for pp,ss,qq,dd,ff,w,path in leaves)<=1-m)
      old=B;changes=[];weights=[]
      for pp,ss,qq,dd,ff,w,path in leaves:
       oc=E.ce(pp,qq);nc=E.ce(pp,ff);old=E.add(old,E.scale(oc,w));changes.append(E.scale(E.sub(nc,oc),w))
       weights.append(w*((1-m)+m*(1-pp[0])))
       E.ck(E.nonpositive(E.sub(E.sub(oc,E.ce(pp,dd)),E.scale(L,((1-m)+m*(1-pp[0]))))))
       if pp[0]!=1:nonconstant+=1
       if E.interval(E.sub(nc,oc))[0]>0:positive+=1
      for mask in range(1<<len(leaves)):
       cost=old;weight=F(0)
       for i in range(len(leaves)):
        if mask>>i&1:cost=E.add(cost,changes[i])
        else:weight+=weights[i]
       E.ck(E.nonpositive(E.sub(cost,E.add(c,E.scale(L,weight)))))
       E.ck(E.nonpositive(E.sub(cost,E.add(c,E.scale(L,1-m*m)))))
       policies+=1
  if time.perf_counter()-t>60:raise RuntimeError('frozen 60-second compute cap reached; no exhaustive claim')
 out=dict(status='PASS',dimension=n,boolean_tables=len(codes),truth_table_codes=codes,source_floor_instances=instances,tree_frontier_policies=policies,nonconstant_terminal_occurrences=nonconstant,positive_reset_occurrences=positive,assertions=E.ASSERTIONS,elapsed_seconds=time.perf_counter()-t,arithmetic='exact prime-log equalities and rational24-term atanh intervals with outward2^-100 rounding')
 (ROOT/('out/REVIEW_PILOT.json' if pilot else 'out/REVIEW_CHECK.json')).write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
if __name__=='__main__':main()
