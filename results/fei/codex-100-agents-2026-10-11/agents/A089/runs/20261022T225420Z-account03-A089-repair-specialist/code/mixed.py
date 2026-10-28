"""Other-core query after actual sibling transfer. Preserve all ancestor labels."""
from check import *
import check as engine
from third_query import mul,div,avg
ROOT=Path(__file__).resolve().parents[1]
PRIOR=ROOT.parent/'20261021T154748Z-account03-A089-repair-specialist'
explicit=0
def test(b):
    global explicit
    assert b;explicit+=1
def show(iv):return [float(F(x,Q)) for x in iv]
def positive(iv):return (max(0,iv[0]),max(0,iv[1]))
def negative_cost(iv):return (max(0,-iv[1]),max(0,-iv[0]))

def profile(truths):
    cs=[core(t) for t in truths];op=outer('J',tuple(c['p'] for c in cs));hf,I=composed(op,cs)
    return {'truths':tuple(truths),'cores':cs,'op':op,'H':hf,'I':I,'S':sub(const(4*I),hf)}
def query(p,j,i):
    cs=[]
    for b in [0,1]:
        ts=list(p['truths']);ts[j]=child(ts[j],i,b);cs.append(profile(ts))
    q=p['op']['q'][j];d=q*p['cores'][j]['d'][i]
    test(p['I']-(cs[0]['I']+cs[1]['I'])/2==d)
    for l in range(6):test((cs[0]['op']['q'][l]+cs[1]['op']['q'][l])/2==p['op']['q'][l])
    test(cs[0]['op']['q'][j]==cs[1]['op']['q'][j]==q)
    e=sub(sub(p['H'],avg([c['H'] for c in cs])),const(4*d))
    return cs,e,d
def owners(p,j):
    U=scale(p['cores'][j]['S'],p['op']['q'][j]);M=sub(p['S'],U)
    V=sub(U,negative_cost(M));W=positive(M)
    return {'U':U,'M':M,'V':V,'W':W}
def retain(p,reach,debit,label):
    return {'history':label,'reach':reach,'H_full':p['H'],'I_full':str(p['I']),'full_S4':p['S'],'booked_debit':debit,'remaining':sub(p['S'],debit),'core_means':[str(1-2*c['p']) for c in p['cores']]}
def incoming():
    root=profile([G]*6);first,e1,_=query(root,0,2)
    D0=scale(e1,F(2));second,e2,_=query(first[0],0,0)
    U2=[owners(c,0)['U'] for c in second];B2=avg(U2);T2=plus(D0,e2)
    Ds=[mul(div(T2,B2),u) for u in U2]
    third,e3,_=query(second[0],0,1) # current1=original3
    own3=[owners(c,0) for c in third];B3=avg([o['V'] for o in own3]);T3=plus(Ds[0],e3)
    tau=sub(T3,B3);test(tau[0]>0)
    D=scale(tau,F(2));parent=third[1]
    test(parent['cores'][0]['I']==0 and parent['I']>0)
    test(sub(parent['S'],D)[0]>0)
    saved=json.loads((PRIOR/'out/REPAIRED_CASES.json').read_text(encoding='utf-8'))
    old=next(r for r in saved if r['second_bit']==0 and r['third_original_coordinate']==3)
    sourceD=old['total_booked_leaf_debits'][1]
    test(D[0]<=sourceD[1] and sourceD[0]<=D[1])
    source=(retain(first[1],'1/2',(0,0),'root original2=1'),
      retain(second[1],'1/4',Ds[1],'root original2=0,original0=1'),
      retain(third[0],'1/8',third[0]['S'],'root original2=0,original0=0,original3=0; selected capacity fully spent'),
      retain(parent,'1/8',D,'root original2=0,original0=0,original3=1; other owner charged2tau'))
    (ROOT/'out/INCOMING_FRONTIER.json').write_text(json.dumps({'root_excess':e1,'second_excess':e2,'third_excess':e3,'same_tau':tau,'incoming_same2tau':D,'leaves':source,'full_reach_sum':'1','no_rate_change':True},indent=2)+'\n',encoding='utf-8')
    return parent,D
def main():
    start=time.perf_counter();parent,D=incoming();rows=[]
    cases=[(1,0),(1,2)] if '--pilot' in sys.argv else [(j,i) for j in range(1,6) for i in range(6)]
    for j,i in cases:
        cs,e,d=query(parent,j,i);T=plus(D,e);os=[owners(c,j) for c in cs]
        B=avg([o['V'] for o in os]);W=avg([o['W'] for o in os]);tau=positive(sub(T,B))
        remaining=sub(plus(B,W),T)
        identity=sub(remaining,sub(parent['S'],D));test(identity[0]<=0<=identity[1])
        row={'block':j,'coordinate':i,'physical_influence':str(d),'unchanged_incoming2tau':D,
          'new_signed_excess':e,'required_old_plus_new_T':T,'corrected_mean_selected_B':B,
          'mean_other_W':W,'minimum_new_other_draw':tau,'mean_remaining_after_debits':remaining,
          'no_reset_identity_diagnostic':identity,'corrected_V_nonnegative':all(o['V'][0]>=0 for o in os),
          'T_nonnegative':T[0]>=0,'children_full_nonnegative':all(c['S'][0]>=0 for c in cs),
          'other_capacity_sufficient':sub(W,tau)[0]>=0,
          'children':[dict(retain(c,'1/16',(0,0),'new mixed-query child; debit allocation pending'),**o) for c,o in zip(cs,os)]}
        rows.append(row)
        (ROOT/'out'/('PILOT_CASES.json' if '--pilot' in sys.argv else 'MIXED_CASES.json')).write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8')
        test(time.perf_counter()-start<55)
    result={'version':'spent-sibling-mixed-query-v1','cases':len(rows),'engine_assertions':engine.tests,
      'explicit_recorded_predicates':explicit,'runtime_seconds':time.perf_counter()-start,'scale_bits':192,
      'failed_V':sum(not x['corrected_V_nonnegative'] for x in rows),'negative_T':sum(not x['T_nonnegative'] for x in rows),
      'negative_child_full':sum(not x['children_full_nonnegative'] for x in rows),
      'failed_other_capacity':sum(not x['other_capacity_sufficient'] for x in rows),
      'display':[{'j':x['block'],'i':x['coordinate'],'e':show(x['new_signed_excess']),
        'T':show(x['required_old_plus_new_T']),'B':show(x['corrected_mean_selected_B']),
        'draw':show(x['minimum_new_other_draw']),'remaining':show(x['mean_remaining_after_debits'])} for x in rows]}
    (ROOT/'out'/('PILOT.json' if '--pilot' in sys.argv else 'MIXED_SUMMARY.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))
if __name__=='__main__':main()
