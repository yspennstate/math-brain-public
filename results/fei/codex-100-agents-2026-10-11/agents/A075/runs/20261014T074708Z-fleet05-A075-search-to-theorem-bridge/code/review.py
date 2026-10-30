from block_reveal import *
def main():
    start=time.perf_counter();rows=[]
    for tag,truth in [('h',H),('J',J)]:
        for j in range(6):
            witnesses=[x for x in range(64) if not(x>>j&1) and truth[x]!=truth[x^(1<<j)]]
            ar.ck(len(witnesses)>0)
            r=min(x.bit_count() for x in witnesses)
            if tag=='h':ar.ck(sum(x.bit_count()==1 for x in witnesses)==4)
            else:ar.ck(r==(1 if j==0 else 2 if j==4 else 0))
            rows.append({'gate':tag,'direction':j,'minimum_weight':r,'minimum_weight_witnesses':[x for x in witnesses if x.bit_count()==r]})
    ar.ck(Q(15,16)**4>Q(3,4));ar.ck(Q(80,99)<1)
    source=Path(r'~\brain_workers\FEI100_20261011\agents\A084\runs\20261014T061132Z-fleet05-A084-continuum-parameters')
    claim=json.loads((source/'CLAIMS.json').read_text())[0]
    out={'reviewer':'A075','claim_id':claim['claim_id'],'version':claim['version'],'statement_sha256':claim['statement_sha256'],'verdict':'HOLDS_AT_UNCHANGED_FIRST_QUERY_SCOPE','method':'Independent two-section differentiation and tent-kernel reconstruction in own PROOF.md Section 5; direct fixed-table pivotal witnesses supply separate analytic lower bounds, avoiding source scalar fixtures. Exact composition/physical affine averaging retained.','first_unsupported_extension':'Replacing identical rare starting cores by arbitrary later heterogeneous histories, or paying inherited DeltaH(core), is outside this accepted theorem.','witnesses':rows,'checks':ar.checks,'runtime_seconds':time.perf_counter()-start}
    assert out['runtime_seconds']<55
    (ROOT/'out/INDEPENDENT_REVIEW_A084.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='witnesses'}))
if __name__=='__main__':main()
