from check import *
import check as engine
def main():
    start=time.perf_counter();rows=json.loads((ROOT/'out/CASES.json').read_text())
    root=next(x for x in rows if (x['gate'],x['block'],x['coordinate'])==('J',0,2))
    fixed=root['children'][1]
    assert F(fixed['I_core'])==0 and fixed['H_core']==[0,0]
    assert F(fixed['I_full'])>0 and fixed['H_full'][0]>0
    old=scale(root['full_query_excess_K'],F(2));cg=core(G);g5=child(G,2,0);c5=core(g5)
    ps=[cg['p']]*6;ps[0]=c5['p'];parent=outer('J',tuple(ps));cs=[cg]*6;cs[0]=c5
    H5,I5=composed(parent,cs);q=parent['q'][0];U5=scale(c5['S'],q)
    incoming=sub(U5,old);assert incoming[0]>0
    leaf=[];hs=[];banks=[];Cs=[];margins=[]
    for b in [0,1]:
        gc=core(child(g5,0,b));cores=[cg]*6;cores[0]=gc
        op=outer('J',tuple(c['p'] for c in cores));hf,I=composed(op,cores)
        assert op['q'][0]==q
        other=(0,0)
        for l in range(1,6):other=plus(other,scale(cg['S'],op['q'][l]))
        margin=sub(other,op['C']);assert margin[0]>0
        leaf.append({'child_bit':b,'unconditional_reach':'1/4','core_bias':str(gc['p']),'S4_core':gc['S'],'selected_bank':scale(gc['S'],q),'other_bank_minus_C':margin,'H_full':hf,'I_full':str(I),'C':op['C']})
        hs.append(hf);banks.append(scale(gc['S'],q));Cs.append(op['C']);margins.append(margin)
    B=scale(plus(banks[0],banks[1]),F(1,2))
    e2=sub(sub(H5,scale(plus(hs[0],hs[1]),F(1,2))),const(4*q*c5['d'][0]));assert e2[0]>0
    total=plus(old,e2);paid=sub(scale(B,F(3,5)),total);assert paid[0]>0
    DC=sub(parent['C'],scale(plus(Cs[0],Cs[1]),F(1,2)))
    remaining=sub(B,total);identity=sub(remaining,sub(incoming,DC));assert identity[0]<=0<=identity[1]
    assert remaining[0]>0
    out={'version':'same-child-owner-continuation-v1','root_case':['J',0,2],'root_constant_core_branch_reach':'1/2','root_constant_core_branch_booked_debit':'0','unchanged_root_constant_core_full_terminal':fixed,'old_conditional_debit':old,'incoming_selected_bank':U5,'incoming_remaining_after_old_debit':incoming,'new_full_query_excess_K4':e2,'delta_C_second':DC,'grandchild_mean_bank':B,'total_old_plus_new_debit':total,'combined_cap':'3/5','combined_cap_payment_margin':paid,'final_mean_remaining_selected_bank':remaining,'no_renewal_identity_diagnostic':identity,'allocation_rule':'old leaf debit = old_D0*U_leaf/B; new leaf debit = new_excess*U_leaf/B; their conditional means are exactly old_D0 and new_excess; same owner, old debit preserved','leaves':leaf,'exact_structural_assertions_from_engine':engine.tests,'explicit_interval_assertions':11,'failed':0,'runtime_seconds':time.perf_counter()-start}
    assert out['runtime_seconds']<55
    (ROOT/'out/CONTINUATION.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'runtime_seconds':out['runtime_seconds'],'payment_margin_interval_units':paid,'old_debit_preserved':True,'combined_cap':'3/5'}))
if __name__=='__main__':main()
