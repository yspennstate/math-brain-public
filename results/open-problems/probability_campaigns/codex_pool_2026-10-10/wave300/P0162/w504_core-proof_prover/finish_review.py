"""Record the actual referee verdict and finalize this worker's review packet."""
from __future__ import annotations
import ast
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REFEREE = Path('~/brain_workers/w506/REVIEW_PACKET.md')


def save(path, value):
    path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')


def main():
    referee = REFEREE.read_text(encoding='utf-8')
    for claim in ['C001','C002','C003','C004']:
        assert re.search(r'\*\*'+claim+r', KEEP',referee), claim
    assert 'C005' in referee and 'unproved' in referee
    overlay = Path('~/math-brain-build/src/math_brain/overlay.py')
    tree = ast.parse(overlay.read_text(encoding='utf-8'))
    assignment = next(node for node in tree.body if isinstance(node,ast.Assign)
                      and any(isinstance(t,ast.Name) and t.id=='IDENTIFIER_RE' for t in node.targets))
    pattern = re.compile(ast.literal_eval(assignment.value.args[0]))
    measurement = json.loads((ROOT/'measurements.json').read_text(encoding='utf-8'))
    patch = json.loads((ROOT/'patch_validation.json').read_text(encoding='utf-8'))
    assert measurement['status']==patch['status']=='PASS'

    rows = [json.loads(line) for line in (ROOT/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if line]
    receipts = [json.loads(line) for line in (ROOT/'AUDIT_RECEIPTS.jsonl').read_text(encoding='utf-8').splitlines() if line]
    for row in rows:
        suffix = row['id'].rsplit('-',1)[-1]
        if suffix in ['C001','C002','C003','C004']:
            row['status']='independently checked proof'
            row['independent_reviewer']={'agent':'w506','verdict':'KEEP','receipt':str(REFEREE),
                                        'scope':'Exact identity / conditional reduction / explicitly defined family only'}
            row['remaining_gap']=row['remaining_gap'].replace('Independent check pending. ','').replace('independent verification is pending.','independent verification by w506 returned KEEP.')
            receipts.append({'claim_id':row['id'],'reviewer':'w506','verdict':'KEEP','receipt':str(REFEREE),
                             'scope':row['scope'],'full_P0162_proof':False})
    assert next(r for r in rows if r['id'].endswith('C005'))['status']=='conjecture'
    assert next(r for r in rows if r['id'].endswith('C006'))['status']=='proved special case'
    (ROOT/'CLAIMS.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows),encoding='utf-8')
    (ROOT/'AUDIT_RECEIPTS.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in receipts),encoding='utf-8')

    # Preserve the initial draft and publish a reviewed revision with identical
    # logical names. The integrator's documented supersedes flag allows revisions.
    original = json.loads((ROOT/'bundle_001.json').read_text(encoding='utf-8'))
    bundle = json.loads(json.dumps(original))
    bundle['bundle_slug']='p0162-adaptive-coordinate-reviewed-draft-20261010-v2'
    proofs = {
        'restriction-identity': '''Put u_T and v_T for the restriction coefficients. Walsh restriction gives fhat(T)=(u_T+v_T)/2 and fhat(T union {i})=(u_T-v_T)/2, so the corresponding probabilities are w_T(1-q_T) and w_T q_T. Thus H(f)=H(w)+sum w_T h_2(q_T). The auxiliary joint law (B,T) with probabilities u_T^2/2 and v_T^2/2 has uniform branch marginal by Parseval. Its entropy is both 1+[H(f_i^+)+H(f_i^-)]/2 and H(w)+sum w_T h_2(p_T). Subtracting gives the stated equality; summing selector-present probabilities gives Inf_i=sum w_T q_T. Since sum w_T=1 and binary entropy lies in [0,1], the defect lies in [0,2]. No independence of branch and Fourier index is assumed. Independently checked by w506, KEEP C001.''',
        'adaptive-family': '''Write a=2^(-m/2), t=a^2. A two-bit Walsh transform of (-1)^(b_1 b_2) is (1,1,1,-1)/2. Tensoring pairs gives ghat_m(s)=a epsilon_s, with sign weights (1+epsilon a)/2. The point indicator at zero has every coefficient t. Hence Fhat_m(s,0)=a epsilon_s-t and Fhat_m(s,1)=t. Direct edge counting gives Inf_j(F_m)=1/2+t for each base coordinate: the exceptional flip increases h_m=g_m-2*1_0's j-influence by 2t, and F_m averages g_m and h_m. Define L(d)=sum_{epsilon=+/-1}[(1+epsilon d)/2](1-epsilon a)^2 log_2[(1-epsilon a)^2], with zero logarithmic terms zero. The full entropy is m(1+t)-L(a). When b_j=1 there is no exceptional flip, one partner parity and m-2 quadratic-core bits, giving entropy m-2. When b_j=0 there are m-2 core bits and two controls (partner and z); the zero-control block has coefficients 2a epsilon-2t with sign weights (1+2epsilon a)/2, and each other control block U has coefficients -2t*(-1)^1_{z in U}; their absolute values are 2t. Their masses are 1-3t,t,t,t, giving entropy m-2+3mt-L(2a). Thus Delta_j=2-(m/2)t-L(a)+L(2a)/2. Algebra gives L(2a)-2L(a)=-[R(1-a)+R(1+a)], R(u)=u^2 log_2 u. For a<=1/2, R''=(2ln u+3)/ln 2>0 on [1/2,3/2]; Jensen gives R(1-a)+R(1+a)>=0. Consequently Delta_j<=2-(m/2)t<4(1/2+t). At m=2 the core has zero variables and the positive sign has weight one, so the same calculation applies. Independently checked by w506, KEEP C003, with separate algebra and truth tables at m=2,4,6,8.''',
        'family-fei': '''The quadratic function has influence 1/2 in every base coordinate. Because its values at zero and each unit vector are both +1, flipping only the value at zero increases each restriction influence by 2t. Averaging over the selector therefore gives base influences 1/2+t and selector influence t, so I=m/2+(m+1)t. In the Fourier spectrum the selector-present slice consists of 2^m coefficients t, so its total probability is t. Conditional on presence or absence there are at most 2^m possible base indices. The entropy chain rule gives H<=m+h_2(t), without an independence assumption. The inequality -(1-t)ln(1-t)<=t and log_2(1/t)=m give h_2(t)<=mt+t/ln 2. Since m>=2, m+1/ln 2<=2(m+1), proving H<=2I. Independently checked by w506, KEEP C004. This proof uses no closure of the family under arbitrary restrictions.'''
    }
    for entry in bundle['entries']:
        entry['supersedes_existing']=True
        entry['assumptions']=[s for s in entry['assumptions'] if not s.startswith('Review-only DRAFT')]
        entry['source']['revision']='independently-reviewed-special-cases-20261010-v2'
        if entry['key'] in proofs:
            entry['kind']='lemma'
            entry['proof_text']=proofs[entry['key']]
            entry['statement']=entry['statement'].replace('Review-only DRAFT of a worker-derived identity, not an accepted FEI proof.','Draft of an exact identity independently checked by w506; it is not a full FEI proof.')
            entry['statement']=entry['statement'].replace('Review-only DRAFT of a proved-by-worker special case pending independent check; no novelty or full FEI claim.','Draft special-case lemma independently checked by w506; no novelty or full FEI claim.')
            entry['statement']=entry['statement'].replace('Review-only DRAFT of a proved-by-worker special case pending independent check.','Draft special-case lemma independently checked by w506.')
        else:
            assert entry['kind']=='concept' and entry['proof_text'] is None
            entry['source']['revision']='conjectural-input-with-reviewed-context-20261010-v2'
        assert all(pattern.fullmatch(entry[field]) for field in ['namespace','logical_name'])
        assert entry['source']['license']=='owner-own-work'
        assert entry['kind']=='concept' or bool(entry['proof_text'])
    keys={e['key'] for e in bundle['entries']}
    assert all(r['from_key'] in keys and r['to_key'] in keys for r in bundle['relations'])
    save(ROOT/'bundle_002.json',bundle)
    inbox=Path('~/math-brain-inbox/w504')
    part=inbox/'bundle_002.part'
    dest=inbox/'bundle_002.json'
    assert not part.exists() and not dest.exists()
    save(part,bundle)
    part.rename(dest)
    save(ROOT/'bundle_validation.json',{'status':'PASS','scope':'Local fields, proof-text, relation-end, license and actual integrator identifier checks; no ingestion performed',
                                      'entries':4,'relations':3,'reviewed_lemma_entries':3,'conjectural_concept_entries':1,
                                      'identifier_pattern_source':str(overlay),'unreviewed_theorem_entries':0,'formal_proof_check':False})
    submission=json.loads((ROOT/'BRAIN_SUBMISSION.json').read_text(encoding='utf-8'))
    submission['initial_draft_path']=submission['draft_path']
    submission['draft_path']=str(dest)
    submission['submitted']={'state':'reviewed-revision-submitted-as-DRAFT','unique_entries':4,'relations':3,'draft_files':2}
    submission['reviewed']={'state':'KEEP-C001-C004; C005 conjectural; C006 review pending','reviewer':'w506','mathematical_keeps_recorded':4,'receipt':str(REFEREE),
                            'reviewed_lemma_entries':3,'source_row_keep':True}
    submission['promotion']={'reviewed_special_cases':'three lemma entries with full proof_text','unproved_input':'one concept entry; never promoted to theorem','full_P0162_proof':False}
    save(ROOT/'BRAIN_SUBMISSION.json',submission)
    source_status=json.loads((ROOT/'SOURCE_STATUS.json').read_text(encoding='utf-8'))
    source_status['independent_math_review']={'reviewer':'w506','kept':['C001','C002 (conditional)','C003 (family only)','C004 (family only)'],'receipt':str(REFEREE),'C005':'unproved','C006':'review pending'}
    save(ROOT/'SOURCE_STATUS.json',source_status)
    save(ROOT/'FINAL_VALIDATION.json',{'status':'PASS','checks':['bounded numerical run','git apply --check in own fixture','actual integrator identifier regex','required artifacts','seven claim rows','four unique brain entries','full proof_text for reviewed lemmas','three resolved local relations','successful statement and proof handoffs','claim-specific referee KEEPs recorded'],
                                     'math_review':'C001-C004 KEEP by w506; C005 unproved; C006 pending','ingestion':'not-observed','retrieval':'not-tested','formal_theorem_compiled':False})
    report=(ROOT/'REPORT.md').read_text(encoding='utf-8')
    report=report.replace('Independent mathematical review by w506 is pending.','w506 independently kept C001-C004 after algebra and truth-table checks at m=2,4,6,8. C002 is conditional and C003/C004 concern this family only; C005 remains unproved, and C006 still awaits a narrow check.')
    report=report.replace('Four review-only concept entries and three supported relations were published at '+str(inbox/'bundle_001.json')+'. Submission is recorded in BRAIN_SUBMISSION.json; review is pending, ingestion is not observed, and retrievability is not tested.',
                          'Four unique entries and three relations were submitted, followed by a reviewed revision at '+str(dest)+': three independently checked lemmas with complete proofs and one conjectural concept. C001-C004 are independently reviewed; ingestion is not observed and retrievability is not tested. Separate states are in BRAIN_SUBMISSION.json.')
    report=report.replace("NEXT: Independently check C003's two restricted spectra and Jensen step, then test a coordinate-averaged defect bound in the all-small-influence regime against balanced-composition counterexamples.",
                          'NEXT: Independently check C006\'s small-influence localization, then validate ingestion of the reviewed special-case lemmas while keeping C005 conjectural.')
    (ROOT/'REPORT.md').write_text(report,encoding='utf-8')
    attempt=(ROOT/'ATTEMPT.md').read_text(encoding='utf-8')
    attempt=attempt.replace('Review requested from w506 for C001--C004 and C006; C005 remains conjectural.',
                            'w506 returned independent KEEP verdicts for C001--C004; C002 is conditional and C003/C004 are family-only. C006 still awaits a narrow check; C005 remains conjectural.')
    attempt=attempt.replace('Draft brain entries remain concept material until review; submitted, reviewed, ingested, and retrievable are tracked separately.',
                            'The reviewed revision contains three lemma drafts with full proof text and one conjectural concept; submitted, reviewed, ingested, and retrievable are tracked separately.')
    (ROOT/'ATTEMPT.md').write_text(attempt,encoding='utf-8')
    (ROOT/'REVIEW_PACKET.md').write_text('''# Final review packet

w506 independently kept w504 C001-C004. Receipt: ~/brain_workers/w506/REVIEW_PACKET.md. C001 is the exact restriction identity; C002 is a conditional reduction; C003 is the base-coordinate special case; C004 is FEI constant 2 for the explicit family. The referee checked algebra and independent truth tables at m=2,4,6,8. Those KEEPs do not prove C005 or the full FEI conjecture. C006's transparent small-influence localization remains pending a narrow independent check.

Exact assumptions and prior digest: STATEMENT.md, SOURCE_STATUS.json, ATTEMPT.md. Written proof: PROOF.md. Current claim statuses: CLAIMS.jsonl. Audit receipts: AUDIT_RECEIPTS.jsonl. Numerical command: python -X utf8 verify_adaptive.py --gate adaptive-n13-cpu20. Our run passed 30 base-coordinate and 64 identity-coordinate checks, with maximum residual 7.460698725481052e-14. This is numerical verification, not a formal theorem receipt.

The original draft is preserved as bundle_001.json. The reviewed revision bundle_002.json has three lemma entries with full proofs and one explicitly conjectural concept, using the documented supersedes_existing flag. Publication, independent review, ingestion, and retrieval are separate in BRAIN_SUBMISSION.json. The validating coordinator performs integration.

The new research-note patch passes git apply --check in the worker-owned fixture. REPORT.md gives the reviewer's application command. No novelty or full FEI claim is made. The hardest open input remains a uniform suitable-coordinate bound in the all-small-influence regime; neither the conditional reduction nor the explicit family supplies it.

NEXT: Check C006's bound Delta_i<=2 and the constant max(K_0,32), then validate the reviewed bundle while keeping its coordinate-selection input conjectural.
''',encoding='utf-8')
    handoff=json.loads((ROOT/'HANDOFF.json').read_text(encoding='utf-8'))
    handoff['independent_mathematical_review']='C001-C004 KEEP by w506; C006 pending; C005 conjectural'
    save(ROOT/'HANDOFF.json',handoff)
    status=(ROOT/'STATUS.md').read_text(encoding='utf-8')
    assert status.startswith('STATE: WORKING')
    status=status.replace('STATE: WORKING','STATE: NEEDS_REVIEW',1)
    lines=status.splitlines()
    lines[1]="NEXT: Independently check C006's small-influence localization; validating coordinator ingests reviewed lemmas without promoting C005."
    status='\n'.join(lines)+'\n'
    status+='2026-10-10: w506 independently kept C001-C004; audit receipts and claim statuses updated. C005 stays conjectural; C006 awaits review.\n'
    status+='2026-10-10: Published reviewed DRAFT revision bundle_002.json with three proved, independently checked lemma entries and one conjectural concept. Local schema/identifier/proof-text checks and patch check PASS. Ingestion unobserved, retrieval untested. STATE: NEEDS_REVIEW; task deliverables finished and measured.\n'
    (ROOT/'STATUS.md').write_text(status,encoding='utf-8')
    print(json.dumps({'state':'NEEDS_REVIEW','independent_keeps':['C001','C002 conditional','C003 family','C004 family'],
                      'numeric_coordinate_checks':94,'reviewed_draft':str(dest),'unique_entries':4,'reviewed_lemmas':3,
                      'conjectural_input_entries':1,'full_FEI_proof':False,'ingestion':'not-observed','retrieval':'not-tested'}))


if __name__=='__main__':
    main()
