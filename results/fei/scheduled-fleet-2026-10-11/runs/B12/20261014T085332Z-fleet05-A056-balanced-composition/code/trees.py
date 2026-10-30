from check import *
from itertools import permutations
def main():
 start=time.perf_counter();count=trans=0
 for uc,vc in [(6,12),(7,1),(12,10),(0,15)]:
  u,v=table(2,uc),table(2,vc)
  for weighted in [False,True]:
   ru,rv=phase_ref(u,weighted),phase_ref(v,weighted)
   for na in [1,2]:
    for nb in [1,2]:
     root=State(u,v,ru,rv,na,nb)
     for first,second in permutations(['A','B','z'],2):
      children=transport(root,first);trans+=1
      leaves=[];spent=edge_inf(root.f,root.index(first))
      for bit,c in enumerate(children):
       # The failing branch stops immediately in half of the policies;
       # the passing branch always continues, so these are actual adaptive frontiers.
       if bit==1 and first!='z':leaves.append((Q(1,2),c))
       else:
        spent+=edge_inf(c.f,c.index(second))/2
        leaves.extend((Q(1,4),d) for d in transport(c,second));trans+=1
      terminal={};refund={};terminalI=Q(0);wa=wb=Q(0);debt={}
      for w,l in leaves:
       terminal=add(terminal,l.CE,w);refund=add(refund,l.L,w);debt=add(debt,l.debt,w)
       terminalI+=w*l.I;wa+=w*l.pi*l.a;wb+=w*(1-l.pi)*l.b
       assert l.ru==ru and l.rv==rv
      assert wa==root.pi*root.a and wb==(1-root.pi)*root.b
      assert root.I==spent+terminalI
      rhs=add(add({2:7*spent},terminal),refund);rhs=add(rhs,root.L,-1)
      assert rhs==root.CE
      assert nonnegative(add({2:7*terminalI},terminal,-1))
      assert nonnegative(add(root.debt,debt,-1))
      count+=1
 result={'helper_version':'A056-fixed-phase-stopped-v1','adaptive_stopped_trees':count,'physical_transports':trans,'source_seed_identity':'original Ru,Rv retained at every leaf','actual_terminal_price':'CE_leaf <= 7 I_leaf checked','signed_ledger':'exact equality, no positive-part clipping','assertions':'ALL PASS','seconds':time.perf_counter()-start}
 (R/'out/trees.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
