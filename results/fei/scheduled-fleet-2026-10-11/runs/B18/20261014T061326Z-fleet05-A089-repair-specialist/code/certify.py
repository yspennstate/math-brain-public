from check import *
def main():
    start=time.perf_counter();records=json.loads((ROOT/'out/CASES.json').read_text());checks=0
    best=max(records,key=lambda x:x['fraction_of_bank_spent_interval'][0])
    for row in records:
        if row is not best:assert row['fraction_of_bank_spent_interval'][1]<best['fraction_of_bank_spent_interval'][0];checks+=1
    assert (best['gate'],best['block'],best['coordinate'])==('J',0,2);checks+=1
    assert best['fraction_of_bank_spent_interval'][0]*3>Q;checks+=1
    assert best['fraction_of_bank_spent_interval'][1]*5<2*Q;checks+=1
    cg=core(G);op=outer('h',(cg['p'],)*6);hf,I=composed(op,[cg]*6)
    failed=sub(const(4*I),hf);assert failed[1]<0;checks+=1
    out={'failed_statement':'All eight source cases have a fully certified dedicated queried-child S4 owner after outer bills are paid','actual_counterexample':'h(g^6), g=-1 on {0,1,2} in six bits;36 actual physical inputs','scale_bits':192,'core_S4_interval':cg['S'],'parent_C_interval':op['C'],'parent_I':str(I),'parent_H_interval':hf,'parent_S4_interval':failed}
    (ROOT/'out/FAILED_OWNER.json').write_text(json.dumps(out,indent=2)+'\n')
    source=Path(r'~\brain_workers\FEI100_20261011\agents\A072\runs\20261014T044904Z-fleet05-A072-exact-walsh-engine\out')
    accepted=[]
    for row in records:
        src=json.loads((source/f"boundary_case_{row['gate']}_{row['block']}_{row['coordinate']}.json").read_text())
        lo,hi=[F(x) for x in src['delta_C_bounds']]
        mine=row['delta_C'];assert F(mine[0],Q)<=hi and F(mine[1],Q)>=lo;checks+=1
        sign='POSITIVE' if mine[0]>0 else 'NEGATIVE' if mine[1]<0 else 'UNRESOLVED'
        assert sign==src['delta_C_sign'];checks+=1
        rate=F(row['rate']);influence=F(row['physical_influence'])
        e4=plus(row['full_query_excess_K'],const((rate-4)*influence))
        assert e4[0]>0;checks+=1
        accepted.append({'gate':row['gate'],'block':row['block'],'coordinate':row['coordinate'],'curvature_sign':sign,'full_K4_excess_interval':e4})
    result={'sharp_case':['J',0,2],'sharp_fraction_exact_definition':'e/B with e=H(J(g^6))-[H(F|x_(0,2)=0)+H(F|x_(0,2)=1)]/2-4Inf_(0,2), B=q_0*[S4(g|x2=0)+S4(g|x2=1)]/2; all functions and rational biased masses specified in CASES.json','sharp_fraction_interval':best['fraction_of_bank_spent_interval'],'sharp_lower':'1/3','certified_upper':'2/5','independent_A072_scope':accepted,'exact_assertions_passed':checks,'failed':0,'runtime_seconds':time.perf_counter()-start}
    assert result['runtime_seconds']<55
    (ROOT/'out/SHARP_PAYMENT_AND_REVIEW.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'sharp_case':result['sharp_case'],'assertions':checks,'source_curvature_counts':{s:sum(x['curvature_sign']==s for x in accepted) for s in ['POSITIVE','NEGATIVE']},'runtime_seconds':result['runtime_seconds']}))
if __name__=='__main__':main()
