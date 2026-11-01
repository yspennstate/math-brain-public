"""Prepare worker-local review files; publish only explicitly authorized drafts/hooks."""
import argparse
import hashlib
import json
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parent
REPO=Path('~/<private-repo>')
INTAKE=REPO/'06_math_research/probability_1000_intake_claude_20260907'
MODERN='https://arxiv.org/html/2405.20308v2'
RV='https://websites.umich.edu/~rudelson/papers/rv-ICM2010.pdf'

def write_json(path, obj):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

def find_line(path, match):
    with path.open(encoding='utf-8-sig') as stream:
        for number,line in enumerate(stream,1):
            if match(line):
                return number,line.rstrip('\r\n')
    raise ValueError(f'Expected scoped row missing: {path}')

def own_source(key):
    return {'source_id':'owner-probability300:w564-C0029:'+key,
            'url':'urn:owner-work:probability300:w564:C0029:'+key,
            'revision':'author-draft-2026-10-10-v1',
            'license':'owner-own-work; unreviewed mathematical reduction or refuted route; no theorem promotion',
            'excerpt':None}

def entry(key,logical,title,statement,assumptions):
    return {'key':key,'namespace':'probability.random-matrices','logical_name':logical,
            'kind':'concept','title':title,'statement':statement,'proof_text':None,
            'assumptions':assumptions,'domain':'probability theory','source':own_source(key)}

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--submit',action='store_true')
    args=parser.parse_args()
    verification=json.loads((ROOT/'evidence/verification.json').read_text(encoding='utf-8'))
    assert verification['counts']['exact_mismatches']==0
    attempt_path=INTAKE/'attempts.jsonl'
    number,old=find_line(attempt_path,lambda line:'"attempt_id": "C0029-A001"' in line)
    old_record=json.loads(old)
    corrected_key=('For iid standard real Gaussian G_n, for each fixed t>=0, '
        'P(sqrt(n) s_min(G_n)<=t) tends to 1-exp(-t-t^2/2) as n tends to infinity. '
        'For finite n the CDF is not this limiting expression; the uniform Gaussian bound is P(sqrt(n) s_min(G_n)<=t)<=t.')
    corrected_result=('The coefficient one in the limiting Gaussian hard-edge law motivates the conjecture. '
        'The identity 1-exp(-t-t^2/2) is a fixed-t n-to-infinity limit, not the exact finite-n Gaussian CDF '
        '(already n=1 has CDF erf(t/sqrt(2))). An additive polynomial universality error does not cover exponentially '
        'small t. Sah-Sahasrabudhe-Sawhney arXiv:2405.20308v2, Theorems 1.1 and 1.2, extend comparison to such scales '
        'with a multiplicative 1+O((log n)^(-1/16)) loss and exponential additive error; they do not remove the loss. '
        'No exact coefficient-one proof is obtained by this attempt. Scope correction drafted by w564; independent review pending.')
    new_record=dict(old_record)
    new_record.update(key_identity=corrected_key,result=corrected_result,
        obstruction='The exact coefficient one for iid Rademacher matrices remains unproved by this attempt; a positive o(t) loss cannot be dropped.',
        scope_correction_sources=[RV+' (Theorem 3.1 and equation 3.2)',MODERN+' (Theorems 1.1-1.2)'],
        scope_correction_review='w566 pending; no independent proof receipt')
    new=json.dumps(new_record,ensure_ascii=False)
    bundle_path=INTAKE/'brain_bundle_C004b.json'
    bnumber,bold=find_line(bundle_path,lambda line:'"statement": "ATTEMPT RECORD' in line and
        'Edelman' in line and 'Spielman' not in line and 'small-ball regime' in line)
    prefix=bold[:len(bold)-len(bold.lstrip())]
    new_statement=('CORRECTED ATTEMPT RECORD, independent review pending. C0029 concerns iid Rademacher entries and the exact '
        'coefficient-one inequality P(sqrt(n) s_min(B_n)<=t)<=t+q^n. '+corrected_key+' '+corrected_result)
    bnew=prefix+'"statement": '+json.dumps(new_statement,ensure_ascii=False)+','
    hunks=[]
    for path,lineno,before,after in ((attempt_path,number,old,new),(bundle_path,bnumber,bold,bnew)):
        rel=path.relative_to(REPO).as_posix()
        hunks.append(f'--- a/{rel}\n+++ b/{rel}\n@@ -{lineno} +{lineno} @@\n-{before}\n+{after}\n')
    patch=ROOT/'patches/01_gaussian_limit_scope.diff'
    patch.parent.mkdir(exist_ok=True)
    patch.write_text(''.join(hunks),encoding='utf-8')
    write_json(ROOT/'evidence/source_rows.json',{
        'attempt_id':'C0029-A001','live_path':str(attempt_path),'line':number,
        'old_key_identity':old_record['key_identity'],'corrected_key_identity':corrected_key,
        'published_source_quote':'for every fixed ε ≥ 0 one has; as n → ∞',
        'published_source':RV,'locator':'Theorem 3.1, p.9; finite-n bound equation (3.2)',
        'old_card_logical':'math:probability.random-matrices:attempt-c0029-spielman-teng-conjecture-on-the-least-singular-value-of-bernoulli-matr',
        'old_card_line':bnumber,'source_snapshots':'Only matched C0029 rows; no store export.',
        'mathematical_review':'pending; a hash or patch check is not a mathematical proof'})
    digest=(
        '# Prior-attempt and source digest\n\n'
        'The dated ranking row 428 and Lean annotated row 470 label C0029 attempted_un and “constant one”. '
        'The exact intake row (problems.jsonl:29) is unreviewed, gives all large n and all small t, and records '
        'a 7 September scope correction that the 2025 coefficient 1+o(1) is distinct from coefficient one. '
        'The modern primary statement in arXiv:2405.20308v2 equation (2) is the uniform Rademacher inequality in STATEMENT.md.\n\n'
        'C0029-A001 (attempts.jsonl:23) tried Gaussian comparison and found the exponential-scale error gap. '
        'Its “exact law” is incorrect at finite n. Rudelson-Vershynin, ICM 2010, Theorem 3.1 (p.9), says '
        '“for every fixed ε ≥ 0 one has” and “as n → ∞”; its equation (3.2) separately gives the finite-n upper bound. '
        'The n=1 analytic CDF is erf(t/sqrt(2)), with derivative sqrt(2/pi) rather than 1 at t=0. '
        'evidence/verification.json also measures the mismatch at t=1. The card at-c0029 in brain_bundle_C004b.json repeats '
        'the finite-n misstatement; patches/01_gaussian_limit_scope.diff corrects both matching rows without editing live files.\n\n'
        'No C0029/Spielman-Teng record was returned by the targeted searches in probability_1000_attempts_H_20260912 '
        'or probability_1000_attempts_I_20260914. The D/E/F/G/H/I intake searches returned only the F dedup index, '
        'which is not a proof. No formal theorem or trusted-axiom receipt for C0029 was found in the cited Lean folder. '
        'Team O’s named board has no C0029 row; the prepared Probability300 board puts w564–w575 on this target.\n\n'
        'Primary literature checked: arXiv:2405.20308v2 (latest listed revision 8 January 2025), its GAFA 2025 publication, '
        'and the author publication page. Theorem 1.1 retains C_xi(log n)^(-1/16) in the coefficient; Theorem 1.2 retains '
        'the same comparison loss. This does not certify 2026 openness. Original ICM 2002 paper URL recovered from the '
        'authors’ page: https://www.cs.yale.edu/homes/spielman/PAPERS/icm.pdf ; text extraction did not recover the exact '
        'line, so original-source verbatim verification is not claimed. No complete owner solved/retired clearance was '
        'available from the cited exact-ID records. Current openness stays UNKNOWN.\n\n'
        'Brain recall was bounded by 60 seconds and timed out. The cited fallback scar '
        'perceptron_proof_open_gaps_fleet_2026_07_12 warns that passed subchecks do not close other proof gaps. '
        'L1/L2/L3 are author-written local proofs; H is the single remaining, equivalent parent gap.\n')
    (ROOT/'PRIOR_ATTEMPTS.md').write_text(digest,encoding='utf-8')
    entries=[
        entry('schur','exact-row-extension-least-singular-threshold','Exact row-extension threshold (draft proof)',
            'DRAFT, author proof pending independent review. Let n>=2, r>=0, D be a real (n-1)-by-n matrix, and A append X^T. If d=s_min(D)<=r, then s_min(A)<=r. If d>r, choose unit kernel v and orthonormal right singular pairs (v_i,s_i). Exactly s_min(A)<=r iff |<v,X>|^2<=r^2(1+sum_i <v_i,X>^2/(s_i^2-r^2)). This is a Schur-complement identity, not the coefficient-one conjecture.',
            ['Real matrices; n>=2; r>=0','Use the cone formula only when d>r; deficient rank is handled separately']),
        entry('replacement','signed-row-replacement-gap-for-spielman-teng','Signed replacement estimate still missing',
            'UNPROVED INPUT. Let D_k have k-1 iid standard Gaussian rows and n-k iid sign rows, all independent, and let Q_mu(D,r) be the exact row-extension probability. The algebraic identity p_sign(epsilon)-F_n(epsilon)=sum_k E(Q_sign(D_k,r)-Q_Gaussian(D_k,r)), r=epsilon/sqrt(n), is proved in the draft; deficient-skeleton terms cancel. The missing estimate sum_k E(Q_sign-Q_Gaussian)<=epsilon-F_n(epsilon)+q^n, uniformly for one q<1, is equivalent to the coefficient-one conjecture and is not proved.',
            ['n>=2; 0<=epsilon<1','Mutually independent mixed rows; F_n is the finite-n real Gaussian CDF']),
        entry('obstruction','flat-hadamard-skeleton-obstructs-pointwise-gaussian-replacement','Flat Hadamard obstruction (draft proof)',
            'DRAFT COUNTEREXAMPLE, review pending. For n=2^m>=2 delete the all-ones row of a Sylvester Hadamard matrix to get D. All chosen singular directions are flat. At r=1/[8(n+1)], an independent sign row has conditional small-singular probability binomial(n,n/2)/2^n>=1/(n+1), while a Gaussian row has probability <=2r. Their difference is >=3/[4(n+1)]. Flatness alone does not imply pointwise Gaussian domination. This does not refute an average over iid random skeletons or estimates imposing large arithmetic LCD.',
            ['Deterministic Sylvester Hadamard skeleton','Independent product sign or standard Gaussian last row']),
        entry('shortcut','refuted-flatness-only-gaussian-row-domination','Refuted shortcut: flatness gives domination',
            'REFUTED ROUTE. The proposed statement that every rectangular sign skeleton with flat kernel and flat orthonormal singular directions obeys Q_sign(D,r)<=Q_Gaussian(D,r)+exp(-cn) uniformly for some c>0 is false. The Hadamard family gives a positive threshold with excess >=3/[4(n+1)]. Orthogonal sign projections are not generally independent, because their squared norms sum to the deterministic value n.',
            ['This is a failed proof route, not an accepted theorem','No arithmetic or typical-spectrum hypotheses are imposed in the refuted route']),
        entry('gaussian-scope','finite-real-gaussian-cdf-versus-hard-edge-limit','Gaussian finite-n scope correction (draft)',
            'DRAFT SCOPE CORRECTION, review pending. For an iid standard real Gaussian n-by-n G_n and each fixed t>=0, P(sqrt(n) s_min(G_n)<=t) converges as n->infinity to 1-exp(-t-t^2/2). The limiting expression is not the finite-n CDF: for n=1 the CDF is erf(t/sqrt(2)), with derivative sqrt(2/pi) at zero. The finite-n bound P(sqrt(n) s_min(G_n)<=t)<=t is separate. The old C0029-A001 attempt incorrectly used equality for finite n. Supporting primary source: Rudelson-Vershynin ICM 2010, Theorem 3.1 and equation (3.2).',
            ['Real Gaussian entries iid N(0,1)','The asymptotic statement fixes t before letting n tend to infinity'])]
    relations=[{'from_key':'replacement','to_key':'schur','kind':'depends_on',
        'rationale':'The exact replacement identity uses the exact row-extension event: schur states “Exactly s_min(A)<=r iff ...”; replacement states “sum_k E(Q_sign-Q_Gaussian)”. Neither asserts the missing inequality.'},
        {'from_key':'obstruction','to_key':'shortcut','kind':'refutes',
         'rationale':'obstruction gives excess “>=3/[4(n+1)]” on flat Hadamard skeletons; shortcut proposes excess “<=exp(-cn)” uniformly. Polynomial excess eventually exceeds any such exponential.'}]
    bundle={'spec':'mathbrain-draft-v1','author_agent':'w564','bundle_slug':'c0029-exact-row-extension-and-refuted-shortcut-v1',
            'entries':entries,'relations':relations}
    local_bundle=ROOT/'review/bundle_001.json'
    write_json(local_bundle,bundle)
    # Shape validation, not integrator execution and not mathematical review.
    keys={e['key'] for e in entries}
    assert len(keys)==len(entries)
    for e in entries:
        assert e['kind']=='concept' and e['proof_text'] is None
        assert e['source']['license'].startswith('owner-own-work')
    assert all(r['from_key'] in keys and r['to_key'] in keys for r in relations)
    hook={'id':'c0029-w564-01','area':'math','event':'PreToolUse',
          'cue':r'(?is)(?=.*(?:Rademacher|Bernoulli|sign[- ]row))(?=.*(?:orthogonal|flat))(?=.*(?:independent|Gaussian comparison)).*',
          'fire_when':'A proof treats orthogonal sign-row projections as independent or asserts pointwise Gaussian comparison from flatness alone.',
          'silent_when':'A proof uses independent orthogonal Gaussian projections, or states an averaged sign comparison as an unproved input.',
          'text':'Orthogonal sign projections need not be independent. A flat Hadamard skeleton has a polynomial singularity atom. Keep the numerator and random threshold jointly; pointwise Gaussian replacement needs more hypotheses. An averaged estimate remains a separate gap.',
          'evidence':'~/brain_workers/w564/ATTEMPT.md L3; evidence/verification.json; scar perceptron_proof_open_gaps_fleet_2026_07_12',
          'proposer':'w564'}
    assert len(hook['text'])<=300
    fire=['Flat orthogonal projections of a Rademacher row are independent.',
          'Assert pointwise Gaussian comparison for every flat Bernoulli skeleton.']
    silent=['Gaussian orthogonal projections are independent.',
            'The Rademacher signed average remains unproved.',
            'Read SOURCE_STATUS for C0029.']
    regex=re.compile(hook['cue'])
    assert all(regex.search(s) for s in fire)
    assert not any(regex.search(s) for s in silent)
    (ROOT/'review/hooks.jsonl').write_text(json.dumps(hook,ensure_ascii=False)+'\n',encoding='utf-8')
    validation={'bundle_entries':len(entries),'relations':len(relations),'all_entries_concepts':True,
                'license_prefix_check':'owner-own-work','hook_fire_controls':len(fire),'hook_silent_controls':len(silent),
                'integrator_run':False,'mathematical_review':'pending','served_model_receipt':'unavailable'}
    write_json(ROOT/'evidence/draft_validation.json',validation)
    if args.submit:
        inbox=Path('~/math-brain-inbox/w564')
        inbox.mkdir(parents=True,exist_ok=True)
        final=inbox/'bundle_001.json'
        if final.exists():
            if json.loads(final.read_text(encoding='utf-8'))!=bundle:
                raise SystemExit('Existing authorized draft differs; refusing overwrite.')
        else:
            part=inbox/'bundle_001.part'
            with part.open('x',encoding='utf-8') as stream:
                json.dump(bundle,stream,indent=2,ensure_ascii=False)
                stream.write('\n')
            part.rename(final)
        hook_path=Path('~/primary_directive/hooks1000/proposals/math-w564.jsonl')
        prior=hook_path.read_text(encoding='utf-8') if hook_path.exists() else ''
        if not any(json.loads(line).get('id')==hook['id'] for line in prior.splitlines() if line.strip()):
            with hook_path.open('a',encoding='utf-8') as stream:
                stream.write(json.dumps(hook,ensure_ascii=False)+'\n')
    lifecycle={'prepared':True,'submitted':bool(args.submit),'reviewed':False,'ingested':False,'retrievable':False,
               'bundle_path':'~/math-brain-inbox/w564/bundle_001.json' if args.submit else str(local_bundle),
               'hook_submitted':bool(args.submit),'live_store_writes':False,
               'scope':'Five concept drafts only; no parent proof promotion.'}
    write_json(ROOT/'review/lifecycle.json',lifecycle)
    status=json.loads((ROOT/'SOURCE_STATUS.json').read_text(encoding='utf-8'))
    status.update(original_source={'title':'Smoothed Analysis of Algorithms, ICM 2002','url':'https://www.cs.yale.edu/homes/spielman/PAPERS/icm.pdf',
                                  'verified':'Author page and PDF recovered; exact original line not recovered by machine text extraction.'},
                  prior_attempts='PRIOR_ATTEMPTS.md; exact C0029-A001 scope correction drafted.',
                  owner_solved_retired_check='No full clearance; exact intake and cited later folders yielded no solved certificate. Openness stays UNKNOWN.',
                  brain_bundle=lifecycle)
    status['primary_sources'].append({'url':RV,'authors':['Mark Rudelson','Roman Vershynin'],'version':'ICM 2010 survey',
        'locations':['Theorem 3.1, p.9','Equation (3.2), p.9'],'finding':'Gaussian expression is a fixed-t n-to-infinity limit, while <=epsilon holds separately at finite n.'})
    write_json(ROOT/'SOURCE_STATUS.json',status)
    claims_path=ROOT/'CLAIMS.jsonl'
    claims=claims_path.read_text(encoding='utf-8')
    correction={'claim_id':'w564-C0029-S1','status':'proved special case',
        'statement':'C0029-A001 incorrectly labels 1-exp(-t-t^2/2) as the finite-n real Gaussian CDF; it is a fixed-t large-n limit. The n=1 CDF is erf(t/sqrt(2)).',
        'assumptions':['iid real N(0,1) entries','t fixed for the limiting source statement'],
        'source':RV+'; Theorem 3.1 and equation 3.2; local source rows in evidence/source_rows.json',
        'proof_or_counterexample':'At n=1, s_min=|Z|. Its CDF derivative at zero is sqrt(2/pi), unlike derivative 1 of the stated limiting expression; measured t=1 discrepancy in evidence/verification.json.',
        'independent_reviewer':'w566 pending; statement correction needs the review gate',
        'remaining_gap':'Source/card correction is prepared only; current openness and H remain unresolved.'}
    if correction['claim_id'] not in claims:
        with claims_path.open('a',encoding='utf-8') as stream:
            stream.write(json.dumps(correction,ensure_ascii=False)+'\n')
    files=['STATEMENT.md','ATTEMPT.md','PRIOR_ATTEMPTS.md','CLAIMS.jsonl','SOURCE_STATUS.json',
           'verify_packet.py','run_checks.py','evidence/verification.json','evidence/compute_gate.json',
           'evidence/source_rows.json','evidence/draft_validation.json','patches/01_gaussian_limit_scope.diff',
           'review/bundle_001.json','review/hooks.jsonl','review/lifecycle.json']
    manifest={name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in files}
    write_json(ROOT/'review/packet_hashes.json',manifest)
    print(json.dumps({'lifecycle':lifecycle,'validation':validation,
                     'diagnostic_counts':verification['counts'],'review_hashes':'review/packet_hashes.json'},indent=2))

if __name__=='__main__':
    main()
