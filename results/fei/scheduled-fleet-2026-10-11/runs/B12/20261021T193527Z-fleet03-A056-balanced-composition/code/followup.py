import shared as sh
from prior import *

def main():
 start=time.perf_counter();nr=nt=both=0;records=[]
 for uc,vc in [(1,16),(2,1),(105,150),(23,113),(7,31),(128,127),(85,51),(3,63)]:
  u,v=table(3,uc),table(3,vc)
  s=State(u,v,phase_ref(u,True),phase_ref(v,True),2,1)
  for i in range(3):
   rec,cs=sh.shared(s,i);nr+=1
   for kind in ['A','B','z']:
    leaves=[]
    for c in cs:leaves.extend(transport(c,kind))
    nt+=1;both+=all(c.I>0 for c in leaves)
    terminal={};remaining=Q(0);debt={}
    for c in leaves:
     terminal=add(terminal,c.CE,Q(1,4));debt=add(debt,c.debt,Q(1,4));remaining+=c.I/4
    margin=add({2:7*remaining},terminal,-1)
    assert nonnegative(margin)
    # The already-spent shared query and next query are literal physical
    # influence debits, retained against the SAME original root.
    spent=edge_inf(s.f,i)+sum(edge_inf(c.f,c.index(kind)) for c in cs)/2
    assert s.I==spent+remaining
    assert nonnegative(add(s.CE,terminal,-1))
    records.append({'u':uc,'v':vc,'shared':i,'next':kind,'spent_influence':str(spent),'remaining_influence':str(remaining),'full_terminal_KL':ser(debt),'same_rate7_terminal_margin':ser(margin)})
 result={'status':'PASS','shared_first_queries':nr,'two_step_histories':nt,'all_four_terminals_nonconstant':both,'assertion_scope':'inherited refined shared calibration; prior private/selector closure; same original influence telescope and complete terminal7I including nonzero KL','runtime_seconds':time.perf_counter()-start,'records':records}
 (R/'out/followup.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({k:v for k,v in result.items() if k!='records'},indent=2))
if __name__=='__main__':main()
