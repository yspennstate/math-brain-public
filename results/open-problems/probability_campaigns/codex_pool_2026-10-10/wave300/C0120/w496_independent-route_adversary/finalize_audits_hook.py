import json
from pathlib import Path

root=Path(__file__).resolve().parent
path=root/'AUDIT_w495.jsonl'
existing={json.loads(s)['subject'] for s in path.read_text(encoding='utf-8').splitlines() if s.strip()}
notes={
    'w495-L1':'Mills plus two separated quantile events gives c/log m; independent-gradient indicators and Gaussian OU hypercontractivity integrate to <=2/log m. Exact hypotheses checked against primary Lemmas 3.3 and 4.1.',
    'w495-L2':'Pointwise maximum comparison and a Gaussian marginal union bound integrate to B=2r(log(2m)+1), irrespective of prefix correlations.',
    'w495-L3':'Transitive tree automorphisms give chain probabilities 1/m; Gaussian integration by parts and level indexing give first-chaos variance 2-2/m+n/m=3-2/m.',
    'w495-L4':'Centered L2 reverse triangle with B<=c n/(4 log m) yields the lower bound; Var(M)<=2Var(A)+2B<6n/log m gives the upper bound. Uniform power bound fails along L=2^r+r.',
    'w495-L5':'Fixed beta>0 gives comparison error <=2B+2(log(m)/beta)^2; transitivity gives the same first-chaos coefficients. The asymptotic threshold depends on beta. At beta=0 the mean-path-score variance is 3-2/m, so no uniform down-to-zero assertion is justified.',
}
with path.open('a',encoding='utf-8') as f:
    for subject,note in notes.items():
        if subject not in existing:
            f.write(json.dumps({'id':'w496-audit-'+subject,'subject':subject,'verdict':'KEEP','scope':'Explicit binary-tree-plus-private-chains graph family only; fixed beta for L5','independent_derivation':note,'source':'~/brain_workers/w495/ATTEMPT.md','audit_proof':'~/brain_workers/w496/AUDIT_W495_PROOF.md','remaining_gap':'A fixed-lattice polynomial chaos/overlap estimate is absent. This KEEP is not a parent-problem solution or served-model gate.','auditor':'w496','audit_date':'2026-10-10'},ensure_ascii=False)+'\n')

hook=json.loads((root/'HOOK_PROPOSAL.jsonl').read_text(encoding='utf-8'))
dest=Path('~/primary_directive/hooks1000/proposals/math-w496.jsonl')
dest.parent.mkdir(parents=True,exist_ok=True)
hook_ids=set()
if dest.exists():
    hook_ids={json.loads(s)['id'] for s in dest.read_text(encoding='utf-8').splitlines() if s.strip()}
if hook['id'] not in hook_ids:
    with dest.open('a',encoding='utf-8') as f:
        f.write(json.dumps(hook,ensure_ascii=False)+'\n')
print('peer_audit_rows',len(existing|set(notes)),'hook_proposal_saved',hook['id'])
