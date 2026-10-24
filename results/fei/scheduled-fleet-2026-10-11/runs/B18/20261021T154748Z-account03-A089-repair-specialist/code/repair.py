"""Correct selected capacity after outer debit; minimal sibling transfer."""
from third_query import *
def main():
    start=time.perf_counter();rows=json.loads((ROOT/'out/THIRD_QUERY_CASES.json').read_text(encoding='utf-8'))
    out=[];checks=0
    def test(b):
        nonlocal checks
        assert b;checks+=1
    for r in rows:
        vs=[];ws=[]
        for c in r['leaves']:
            M=c['untouched_other_M'];U=c['selected_U']
            cost=(max(0,-M[1]),max(0,-M[0]))
            V=sub(U,cost);W=(max(0,M[0]),max(0,M[1]))
            test(V[0]>=0);test(W[0]>=0)
            test(sub(plus(V,W),c['full_S4'])[0]<=0<=sub(plus(V,W),c['full_S4'])[1])
            vs.append(V);ws.append(W)
        B=avg(vs);W=avg(ws);T=r['old_plus_new_debit'];need=sub(T,B)
        tau=(max(0,need[0]),max(0,need[1]));test(T[0]>0)
        test(sub(W,tau)[0]>0)
        test(sub(plus(B,W),T)[0]>0)
        fail=need[0]>0
        if fail:
            ratio=div(tau,W);test(ratio[0]*4>Q);test(ratio[1]*50<13*Q)
            # V_1=0 and W_0=0: all selected capacity used, sole surplus on constant-core sibling.
            test(vs[1]==(0,0));test(ws[0]==(0,0))
            booked=[vs[0],scale(tau,F(2))]
            remain=[(0,0),sub(ws[1],booked[1])]
            test(remain[1][0]>0)
        else:
            test(sub(B,T)[0]>0);ratio=(0,0)
            theta=div(T,B)
            booked=[mul(theta,v) for v in vs]
            remain=[sub(plus(v,w),d) for v,w,d in zip(vs,ws,booked)]
            test(all(x[0]>0 for x in remain))
        test(sub(avg(booked),T)[0]<=0<=sub(avg(booked),T)[1])
        old_labels=[mul(div(r['incoming_debit'],T),d) for d in booked]
        new_labels=[mul(div(r['full_query_excess'],T),d) for d in booked]
        test(sub(avg(old_labels),r['incoming_debit'])[0]<=0<=sub(avg(old_labels),r['incoming_debit'])[1])
        test(sub(avg(new_labels),r['full_query_excess'])[0]<=0<=sub(avg(new_labels),r['full_query_excess'])[1])
        item={'second_bit':r['second_bit'],'third_original_coordinate':r['original_coordinate'],
         'incoming_debit':r['incoming_debit'],'new_full_K4_excess':r['full_query_excess'],
         'old_plus_new_T':T,'corrected_selected_V':vs,'other_positive_W':ws,
         'corrected_mean_selected_B':B,'corrected_selected_only_fails':fail,
         'minimal_transfer_tau':tau,'mean_other_W':W,'fraction_other_spent':ratio,
         'total_booked_leaf_debits':booked,'old_booked_labels':old_labels,'new_booked_labels':new_labels,'full_remaining_leaf_banks':remain,
         'unconditional_leaf_reach':'1/8','retained_other_root_branches':'root bit2=1 reach1/2; opposite second child reach1/4 with its prior debit unchanged'}
        out.append(item)
        (ROOT/'out/REPAIRED_CASES.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    test(sum(x['corrected_selected_only_fails'] for x in out)==3)
    result={'version':'minimal-sibling-transfer-v1','cases':len(out),'exact_explicit_predicates':checks,
     'failed_selected_only':3,'transferred_fraction_interval':'(1/4,13/50)',
     'runtime_seconds':time.perf_counter()-start,'failed':0,
     'displays':[{'b':x['second_bit'],'i':x['third_original_coordinate'],
       'B':display(x['corrected_mean_selected_B']),'T':display(x['old_plus_new_T']),
       'tau':display(x['minimal_transfer_tau']),'W':display(x['mean_other_W']),
       'tau/W':display(x['fraction_other_spent'])} for x in out]}
    test(result['runtime_seconds']<55)
    (ROOT/'out/REPAIR_SUMMARY.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))
if __name__=='__main__':main()
