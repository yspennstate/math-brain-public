"""Prepare local drafts and exact scope patches; do not touch live data."""
from __future__ import annotations
import difflib
import hashlib
import json
from pathlib import Path
import time

ROOT=Path(__file__).resolve().parent
LIVE_REPO=Path('~/<private-repo>')
REL='06_math_research/probability_1000_intake_claude_20260907/problems.jsonl'

def save(name: str, value: dict | list) -> None:
    (ROOT/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

def own_source() -> dict:
    return {'source_id':'owner-c0120-w492-20261010','url':'owner-own-work://C0120/w492/ATTEMPT.md',
            'revision':'author-written-20261010-v1','license':'owner-own-work','excerpt':None}

def main() -> None:
    original_line=None
    line_number=None
    with (LIVE_REPO/REL).open(encoding='utf-8-sig') as f:
        for number,line in enumerate(f,1):
            if 'C0120' in line:
                row=json.loads(line)
                if row.get('problem_id')=='C0120':
                    original_line=line.rstrip('\r\n')
                    line_number=number
                    break
    assert original_line is not None
    original=json.loads(original_line)
    corrected=dict(original)
    corrected['statement']=('In the Gaussian zero-temperature model of arXiv:0810.4221v2 Section 8, '
      'let g_v be iid N(0,1) on Z_+^2 and M_n=max_p sum_{v in p} g_v, where p has n vertices, '
      'starts at the origin, moves up or right, and has unrestricted endpoint. Theorem 8.1 proves '
      'Var(M_n)<=C n/log n. A precise power-improvement formulation of Section 12(3) asks whether '
      'there exist epsilon>0,C<infinity,n_0 such that Var(M_n)<=C n^(1-epsilon) for all n>=n_0. '
      'This formulation is a scoped reading of the exponent question; the cited theorem is not '
      'a positive-temperature log-Z bound in general dimension.')
    corrected['status_search']=('Current openness UNKNOWN as of 2026-10-10. The 2008 source and '
      '2026-09-07 ranking do not certify present status. w492 source-scope audit finds that '
      'the attached source concerns a Gaussian 1+1 zero-temperature/free-endpoint maximum; '
      'positive-temperature/general-dimension variants require separate sources. Independent '
      'source-statement correction review pending; no novelty or solved-parent claim.')
    (ROOT/'source_records').mkdir(exist_ok=True)
    save('source_records/C0120_original.json',original)
    save('source_records/C0120_corrected.json',corrected)
    after=json.dumps(corrected,ensure_ascii=False,sort_keys=True)
    patch=(f'--- a/{REL}\n+++ b/{REL}\n@@ -{line_number} +{line_number} @@\n'
           f'-{original_line}\n+{after}\n')
    (ROOT/'patches').mkdir(exist_ok=True)
    (ROOT/'patches/01_c0120_source_scope.diff').write_text(patch,encoding='utf-8')
    ids=[('claim_2b6b7c1da300a8ed1c28367cabd584f2c02769a03a64ed519cf081b1af04693d',
      'math:probability.gaussian:open-problem-c0120-fluctuation-exponent-of-directed-polymers-beyond-the-logarithmic-impro',
      'sha256:578853e3b2073e0e1a4e864c29ebf3c5a2b0fa5b2a359fdbc9cc0d700aae250d'),
      ('claim_7891e285a213a1ead9b1e54b02b29177a06d86c6f3df76b6447ca94dbe6add7f',
      'math:probability.gaussian:attempt-c0120-fluctuation-exponent-of-directed-polymers-beyond-the-logarithmic-impro',
      'sha256:5bc0c0da0d1afa02a94a9c12b84177809508300e827cfbe8563403d6f6bf367a')]
    corrections={'worker':'w492','candidate':'C0120','status':'DRAFT source correction; independent review pending',
      'primary_source':'https://arxiv.org/pdf/0810.4221v2',
      'observed_export':'~/math-brain-build/export/population/nodes.jsonl',
      'rows':[{'claim_id':i,'logical_id':logical,'observed_digest':digest,
          'required_action':'Add an explicit source-scope correction preserving the dated historical record; do not declare solved.',
          'correct_scope':'Gaussian 1+1 zero-temperature n-vertex quadrant paths, origin included, free endpoint; Var(M_n).'}
          for i,logical,digest in ids],
      'live_changes_applied':0,'source_statement_claude_review_required':True}
    save('STORE_CORRECTIONS.json',corrections)
    status=json.loads((ROOT/'SOURCE_STATUS.json').read_text(encoding='utf-8'))
    status.update({'exact_target_recovered':True,'current_openness':'UNKNOWN',
      'primary_source':{'id':'arxiv:0810.4221v2','url':'https://arxiv.org/pdf/0810.4221v2',
      'version_date':'2008-12-16','model_locator':'Section 8, printed pp. 37-38',
      'question_locator':'Section 12(3), printed p. 59','whole_source_hash_verified':False,
      'reason':'Targeted primary-text reading verified scope; older intake PDF digest was not independently recomputed.'},
      'exact_model':{'dimension':'1+1','disorder':'iid standard Gaussian site weights',
      'temperature':'zero','observable':'M_n=max path sum','path_vertices':'n including origin',
      'start':'(0,0)','endpoint':'free','steps':['(1,0)','(0,1)']},
      'precise_session_target':'There exist epsilon>0,C,n_0<infinity: Var(M_n)<=C n^(1-epsilon) for all n>=n_0.',
      'hardest_gap':'G1: D_n(floor n^a)<=C n^(1-b) for some a,b>0 uniformly for large n.',
      'owner_prior_work_check':{'status':'targeted only, not exhaustive',
      'intake_attempt':'C0120-A001 is attempted_unsolved',
      'H_I_scans':'No C0120 proof match in targeted md/json/jsonl/lean scan',
      'Lean_scan':'Ranking row only, no relevant verified theorem found',
      'Team_O_board':'No C0120 row found','canonical_export_matching_cards':2,
      'retired_or_solved_c0120_evidence_found':False},
      'recall':{'status':'timeout at 60 seconds','receipt':'recall_receipt.json',
      'fallback_slug':'perceptron_proof_open_gaps_fleet_2026_07_12'},
      'brain_states':{'prepared':True,'submitted':False,'reviewed':False,'ingested':False,'retrievable':False}})
    save('SOURCE_STATUS.json',status)
    entries=[]
    def entry(key,logical,title,statement,assumptions,kind='concept'):
        entries.append({'key':key,'namespace':'probability.gaussian','logical_name':logical,
          'kind':kind,'title':title,'statement':statement,'proof_text':None,
          'assumptions':assumptions,'domain':'probability theory','source':own_source()})
    model='iid N(0,1) site weights on Z_+^2; n-vertex up/right paths from the origin with free endpoint; M_n is the maximum path sum including the origin.'
    entry('model','c0120-gaussian-ground-state-free-endpoint-model','C0120 exact Gaussian ground-state scope',
      'Scope definition for C0120: '+model+' The attached 2008 source proves Var(M_n)<=C n/log n; '
      'the session asks for Var(M_n)<=C n^(1-epsilon) for some epsilon>0. Current openness UNKNOWN; no solution claim.',[], 'definition')
    entry('spectral','c0120-gaussian-hermite-gradient-energy-draft','Gaussian polymer gradient spectral identity (draft)',
      '[DRAFT: author analytic proof; independent review pending.] For the exact Gaussian ground-state model, '
      'write a_k=||Proj_k(M_n-E M_n)||_2^2 in normalized Gaussian Hermite chaos. Then sum k a_k=n, '
      'Var(M_n)=sum a_k, and Q_n(t)=E|P(g) intersect P(g^t)|=sum k a_k exp(-(k-1)t).',
      [model,'t>=0; g^t=exp(-t)g+sqrt(1-exp(-2t))g_prime with independent g_prime'])
    entry('reduction','c0120-low-degree-spectral-escape-reduction-draft','Polynomial spectral escape variance reduction (draft)',
      '[DRAFT: conditional reduction; input unproved.] In the exact Gaussian ground-state model let '
      'D_n(K)=sum_{k<=K} k||Proj_k(M_n-E M_n)||_2^2. For integer K>=1, '
      'Var(M_n)<=D_n(K)+n/(K+1) and D_n(K)<=K Var(M_n). If a,b>0 and '
      'D_n(floor n^a)<=C n^(1-b) uniformly for large n, then '
      'Var(M_n)<=(C+1)n^(1-min(a,b)). A variance power epsilon gives D_n(floor n^(epsilon/2))<=C n^(1-epsilon/2).',
      [model,'Normalized total-degree Gaussian Hermite chaos','All conditional bounds are uniform for sufficiently large n'])
    entry('gap','c0120-polynomial-low-degree-spectral-mass-open-input','C0120 unproved polynomial spectral mass input',
      '[UNPROVED INPUT G1.] For the exact Gaussian quadrant/free-endpoint maximum M_n, seek constants '
      'a,b>0,C,n_0<infinity such that sum_{k<=floor n^a} '
      'k||Proj_k(M_n-E M_n)||_2^2<=C n^(1-b) for every n>=n_0. '
      'The conditional reduction is proved by its author; this premise is not proved. '
      'The known n/log n variance estimate supplies only D_n(K)<=C K n/log n.',[model])
    entry('noise','c0120-gaussian-noise-spectral-cutoff-bridge-draft','Noise overlap to Hermite cutoff bridge (draft)',
      '[DRAFT: author analytic proof; independent review pending.] In the exact Gaussian ground-state model '
      'and notation D_n(K),Q_n(t) above, for integer K>=1 and t>=0, '
      'Q_n(t)<=D_n(K)+n exp(-Kt), and D_n(K)<=exp((K-1)t)Q_n(t). '
      'These inequalities do not supply a polynomial decorrelation rate.',[model,'OU coupling and normalized Hermite chaos as in the spectral identity'])
    entry('generic','gaussian-path-small-influence-power-variance-inference-invalid','Small-influence power variance inference has a scope gap',
      '[REFUTED GENERIC ROUTE; not a refutation of C0120.] Gaussianity, fixed path length n, '
      'squared gradient norm n, and nonroot vertex marginal influences at most 1/n do not '
      'alone imply a uniform O(n^(1-epsilon)) variance bound with any fixed epsilon>0 '
      'over arbitrary directed path families. Additional graph-specific information is needed.',
      ['Path family on an arbitrary directed acyclic graph','Independent standard Gaussian vertex weights'])
    entry('corridor','parallel-gaussian-corridor-logarithmic-variance-obstruction-draft','Parallel Gaussian corridors: logarithmic obstruction (draft)',
      '[DRAFT: author analytic proof; independent review pending.] A common root with m disjoint '
      'corridors of n-1 vertices has maximum T=g_0+sqrt(n-1) max_{j<=m}G_j. For n>=2,m>=8, '
      'its squared gradient norm equals n and each nonroot influence is 1/m, while '
      '1+c(n-1)/log(2m)<=Var(T)<=1+2(n-1)/log m with '
      'c=(1-exp(-exp(-3/2)*log(2)/10))/4>0. Setting m=n refutes the generic inference; '
      'the graph is not the C0120 quadrant lattice.',
      ['All g_0,G_j independent standard normal','Independent standard Gaussian site weights along disjoint corridors',
       'Gaussian hypercontractivity for upper bound; elementary Mills bounds for lower bound'])
    entry('scope','c0120-max-versus-log-partition-source-scope-correction-draft','C0120 source scope correction (draft)',
      '[DRAFT SOURCE CORRECTION; independent statement review pending.] The C0120 citation '
      'arXiv:0810.4221v2 Section 8 and Section 12(3) concerns a zero-temperature Gaussian maximum '
      'in 1+1 dimensions with free endpoint. The intake and its two exported cards replace '
      'this by Var(log Z_n) in general dimension; that broader attribution is unsupported '
      'by the cited Theorem 8.1. Preserve their historical record and add the exact source scope.',
      ['Primary source version v2 dated 2008-12-16','Scope comparison of named intake row and two exported C0120 cards'])
    relations=[{'from_key':'spectral','to_key':'model','kind':'depends_on','rationale':'The weak-gradient energy n uses n equal-length paths and the exact source model.'},
      {'from_key':'reduction','to_key':'spectral','kind':'depends_on','rationale':'The tail bound uses total Hermite gradient energy n.'},
      {'from_key':'gap','to_key':'reduction','kind':'semantic_association','rationale':'G1 is the unproved premise sufficient for the conditional reduction; no proof edge is asserted.'},
      {'from_key':'noise','to_key':'spectral','kind':'depends_on','rationale':'Both cutoff inequalities follow termwise from the nonnegative overlap series.'},
      {'from_key':'corridor','to_key':'generic','kind':'refutes','rationale':'At m=n, influence 1/n coexists with variance at least c(n-1)/log(2n), contradicting every fixed power gain in the generic graph class.'},
      {'from_key':'scope','to_key':'model','kind':'cites','rationale':'The model node states the recovered primary-source conventions.'},
      {'from_key':'scope','to_existing_logical':ids[0][1],'kind':'cites','rationale':'Named exported problem card is the first exact source-scope correction target.'},
      {'from_key':'scope','to_existing_logical':ids[1][1],'kind':'cites','rationale':'Named exported historical attempt card is the second exact source-scope correction target.'}]
    bundle={'spec':'mathbrain-draft-v1','author_agent':'w492',
      'bundle_slug':'c0120-gaussian-spectral-scope-w492-001','entries':entries,'relations':relations}
    save('bundle_001.json',bundle)
    hook={'id':'math-w492-c0120-scope-01','area':'math','event':'stage-start',
      'cue':'probability candidate source verification with log Z versus a ground-state maximum',
      'fire_when':'An intake claims a general-dimension log-Z variance bound while its cited source defines a Gaussian 1+1 maximum.',
      'silent_when':'The observable, temperature, dimension, path length and endpoint convention already match the primary source.',
      'text':'Before a variance proof, match observable, disorder, temperature, dimension and endpoint to the primary source. A cited maximum bound cannot silently become a log-Z theorem; save the scope correction and keep the rate premise explicit.',
      'evidence':'w492-S1.2; STATEMENT.md; STORE_CORRECTIONS.json; perceptron_proof_open_gaps_fleet_2026_07_12',
      'proposer':'w492'}
    (ROOT/'HOOK_PROPOSAL.jsonl').write_text(json.dumps(hook,ensure_ascii=False)+'\n',encoding='utf-8')
    hookrel='primary_directive/hooks1000/proposals/math-w492.jsonl'
    hookdiff='--- /dev/null\n+++ b/'+hookrel+'\n@@ -0,0 +1 @@\n+'+json.dumps(hook,ensure_ascii=False)+'\n'
    (ROOT/'patches/02_c0120_scope_hook.diff').write_text(hookdiff,encoding='utf-8')
    packet={'worker':'w492','candidate':'C0120','referee':'w494','independent_referee_for_referee':'w497',
      'status':'READY_FOR_REVIEW','parent_problem_solved':False,'current_openness':'UNKNOWN','novelty':'UNKNOWN',
      'statement_first_delivery':{'recipient':'w493','message_id':'msg-c517d1fc6b','inserted':1},
      'claims':['w492-L1','w492-L2','w492-L3','w492-L4'],'source_correction':'w492-S1.2',
      'hardest_gap':'w492-G1: polynomial low-degree Hermite gradient spectral escape in the actual quadrant model.',
      'review_questions':['Check the weak-gradient/Hermite spectral identities, all constants and cutoff exponents.',
       'Check Mills-ratio corridor obstruction and whether its scope is kept separate from the actual lattice.',
       'Review the max/log-Z source correction; route a theorem/source statement correction to Claude.',
       'Keep only finite/conditional lemmas; do not upgrade G1 or assert a solved parent problem.'],
      'served_identity':status['served_model_evidence'],
      'formal_check':{'performed':False,'receipt':None,'admitted_placeholders_counted':False},
      'different_model_review_gate':'not established; requested settings and peer identifiers are not served-model evidence',
      'bundle':'bundle_001.json','brain_submission_policy':'all proof claims remain concept/DRAFT pending review',
      'files':{}}
    for name in ['STATEMENT.md','ATTEMPT.md','CLAIMS.jsonl','SOURCE_STATUS.json','STORE_CORRECTIONS.json',
       'CHECK_RECEIPT.json','COMPUTE_GATE.json','check_corridor.py','bundle_001.json',
       'patches/01_c0120_source_scope.diff','patches/02_c0120_scope_hook.diff']:
        data=(ROOT/name).read_bytes()
        packet['files'][name]={'path':str(ROOT/name),'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data)}
    save('REVIEW_PACKET.json',packet)
    print(json.dumps({'packet':str(ROOT/'REVIEW_PACKET.json'),'entries':len(entries),
      'relations':len(relations),'source_corrections':len(ids),'live_changes':0}))

if __name__=='__main__':
    main()
