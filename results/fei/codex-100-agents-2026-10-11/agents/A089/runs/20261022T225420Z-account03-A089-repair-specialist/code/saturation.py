"""All restrictions of two remaining active bits on a twice-saturated account."""
from mixed import *
import mixed as ledger
from itertools import product
def restrict_original(truth,assign,original_labels):
    out=truth;labels=list(original_labels)
    for label,bit in sorted(assign.items(),reverse=True):
        index=labels.index(label);out=child(out,index,bit);labels.pop(index)
    return out,labels
def main():
    start=time.perf_counter();root=profile([G]*6);first,e1,_=query(root,0,2)
    D0=scale(e1,F(2));second,e2,_=query(first[0],0,0)
    U2=[owners(c,0)['U'] for c in second];B2=avg(U2);T2=plus(D0,e2)
    Dsecond0=mul(div(T2,B2),U2[0]);third,e3,_=query(second[0],0,1)
    B3=avg([owners(c,0)['V'] for c in third]);tau=sub(plus(Dsecond0,e3),B3)
    sat=third[0];parked=third[1];parkedD=scale(tau,F(2));parkedR=sub(parked['S'],parkedD)
    test(parkedD[0]>0)
    prior=json.loads((PRIOR/'out/REPAIRED_CASES.json').read_text(encoding='utf-8'))
    priorD=next(r for r in prior if r['second_bit']==0 and r['third_original_coordinate']==3)['total_booked_leaf_debits'][1]
    test(parkedD[0]<=priorD[1] and priorD[0]<=parkedD[1])
    test(parkedR[0]>0);anchors,e4,_=query(sat,1,0)
    test(all(c['S'][0]>0 for c in anchors));rows=[]
    for b,anchor in enumerate(anchors):
      for pattern in product([-1,0,1],repeat=2):
        assigns={k:v for k,v in zip([4,5],pattern) if v>=0}
        ct,labels=restrict_original(anchor['truths'][0],assigns,[1,4,5]);ts=list(anchor['truths']);ts[0]=ct;p=profile(ts)
        row={'anchor_bit_b':b,'assignment':{str(k):v for k,v in assigns.items()},'remaining_original_core0_labels':labels,
          'H_full':p['H'],'I_full':str(p['I']),'S4_full':p['S'],'negative_full_slack':p['S'][1]<0,
          'positive_full_slack':p['S'][0]>0,'core0_negative_points':[i for i,v in enumerate(ct) if v==-1],
          'core0_dimension':(len(ct)-1).bit_length(),'core0_influence':str(p['cores'][0]['I'])}
        rows.append(row)
        (ROOT/'out/SATURATION_STATES.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8')
        test(time.perf_counter()-start<55)
    # Completion of both active bits: exactly four equiprobable full leaves in each anchor.
    completions=[]
    for b in [0,1]:
        leaves=[x for x in rows if x['anchor_bit_b']==b and len(x['assignment'])==2]
        test(len(leaves)==4)
        subsidy=avg([negative_cost(x['S4_full']) for x in leaves])
        positive_slack=avg([positive(x['S4_full']) for x in leaves])
        # Each anchor has unconditional root reach1/16, parked sibling1/8.
        parked_charge=scale(subsidy,F(1,2))
        completions.append({'b':b,'negative_leaves':sum(x['negative_full_slack'] for x in leaves),
          'mean_minimum_terminal_subsidy':subsidy,'mean_positive_terminal_slack':positive_slack,
          'charge_to_parked_sibling_if_this_anchor_only':parked_charge,
          'parked_remainder_after_charge':sub(parkedR,parked_charge)})
    # If both b anchors are completed, sum their reach-weighted charges to the same old parked remainder.
    totalpark=scale(plus(completions[0]['mean_minimum_terminal_subsidy'],completions[1]['mean_minimum_terminal_subsidy']),F(1,2))
    result={'version':'saturated-point-two-bit-v1','labelled_states':len(rows),
      'engine_assertions':engine.tests,'explicit_recorded_predicates_including_runtime':ledger.explicit,
      'negative_states':sum(x['negative_full_slack'] for x in rows),'runtime_seconds':time.perf_counter()-start,
      'old_parked_full_S4':parked['S'],'old_parked_booked2tau':parkedD,'old_parked_unused_remainder':parkedR,
      'completion_accounts':completions,'both_anchor_charge_to_same_parked_remainder':totalpark,
      'same_parked_remainder_after_both':sub(parkedR,totalpark),
      'parked_subsidy_interpretation':'Feasible but unnecessary fallback; COUPLED_TERMINAL_REPAIR uses own positive sibling, no new parked draw',
      'display_states':[{'b':r['anchor_bit_b'],'a':r['assignment'],'S':show(r['S4_full'])} for r in rows]}
    (ROOT/'out/SATURATION_SUMMARY.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result))
if __name__=='__main__':main()
