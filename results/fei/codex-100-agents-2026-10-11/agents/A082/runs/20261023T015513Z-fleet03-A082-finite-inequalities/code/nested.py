from pathlib import Path
import time,sys,json
import exact as E
from exact import F
ROOT=Path(__file__).resolve().parents[1]
def main():
 start=time.perf_counter();pilot='--pilot' in sys.argv;count=0
 for code in range(16 if pilot else 256):
  f=tuple(-1 if x<8 and code>>x&1 else 1 for x in range(16));P=E.spectrum(f)
  for kind,S in enumerate(E.references(P)):
   c=E.ce(P,S)
   for j in range(4):
    Sj=E.marginal(S,j);Bj=E.erasure(f,j)
    for v in (0,1):
     g=E.child(f,j,v);sibling=E.child(f,j,1-v)
     if len(set(g))==1 or len(set(sibling))==1:continue
     G=E.spectrum(g);C=E.calibrate(Sj,G[0])
     before=E.add(Bj,E.scale(E.add(E.ce(G,C),E.ce(E.spectrum(sibling),Sj)),F(1,2)))
     E.ck(E.nonpositive(E.sub(before,c)))
     for k in range(3):
      O=E.marginal(Sj,k);current=E.marginal(C,k);Bk=E.erasure(g,k)
      for u in (0,1):
       gg=E.child(g,k,u);oldgrand=E.child(g,k,1-u)
       if len(set(gg))==1 or len(set(oldgrand))==1:continue
       PP=E.spectrum(gg);target=E.calibrate(O,PP[0])
       # All three full terminals and both executed erasures remain.
       cost=E.add(Bj,E.scale(Bk,F(1,2)))
       cost=E.add(cost,E.scale(E.ce(E.spectrum(sibling),Sj),F(1,2)))
       cost=E.add(cost,E.scale(E.add(E.ce(PP,target),E.ce(E.spectrum(oldgrand),current)),F(1,4)))
       delta=E.sub(cost,c);lo,hi=E.interval(delta);count+=1
       if lo>0:
        base=E.add(Bj,E.scale(Bk,F(1,2)))
        base=E.add(base,E.scale(E.ce(E.spectrum(sibling),Sj),F(1,2)))
        base=E.add(base,E.scale(E.add(E.ce(PP,current),E.ce(E.spectrum(oldgrand),current)),F(1,4)))
        E.ck(E.nonpositive(E.sub(base,c)))
        save=dict(status='EXACT_COUNTEREXAMPLE_TO_UNPROVED_NESTED_EXTENSION',family_code=code,reference_kind=kind,truth_table=f,root_source_reference=list(map(str,S)),root_spectrum=list(map(str,P)),gamma='1',first_query=j,first_outcome=v,second_query_residual_index=k,second_outcome=u,first_fresh_reference=list(map(str,C)),second_original_marginal=list(map(str,O)),second_fresh_reference=list(map(str,target)),second_inherited_reference=list(map(str,current)),first_retained_sibling=sibling,second_retained_sibling=oldgrand,reset_child=gg,excess_prime_log=E.serial_form(delta),excess_lower=str(lo),excess_upper=str(hi),excess_display=float((lo+hi)/2),cases_visited=count,assertions=E.ASSERTIONS,elapsed_seconds=time.perf_counter()-start,scope='Not a refutation of A096 v1, which excludes nested original-source returns; not an FEI counterexample')
        (ROOT/'out/NESTED_WITNESS.json').write_text(json.dumps(save,indent=2),encoding='utf-8');print(json.dumps({k:save[k] for k in ['status','family_code','reference_kind','first_query','first_outcome','second_query_residual_index','second_outcome','excess_display','cases_visited','elapsed_seconds']}));return
  if time.perf_counter()-start>60:raise RuntimeError('60-second frozen cap reached; untested histories remain')
 out=dict(status='NO_COUNTEREXAMPLE_ON_FROZEN_DOMAIN',pilot=pilot,cases_visited=count,assertions=E.ASSERTIONS,elapsed_seconds=time.perf_counter()-start)
 (ROOT/('out/NESTED_PILOT.json' if pilot else 'out/NESTED_SEARCH.json')).write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
if __name__=='__main__':main()
