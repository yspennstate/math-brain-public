"""Prepare local review material. Submission is separate and requires the mesh lease."""
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re

base=Path(__file__).resolve().parent
now=datetime.now(timezone.utc).isoformat()
attempt=(base/'ATTEMPT.md').read_text(encoding='utf-8')
checks=json.loads((base/'MATH_CHECKS.json').read_text(encoding='utf-8'))
assert checks['status']=='PASS', 'Do not report unpassed checks'

source_status={
 'candidate_id':'C0056','title':'Extended states for the three-dimensional Anderson model at weak disorder',
 'checked_at_utc':now,'current_openness':'UNKNOWN','parent_result':'NOT_PROVED',
 'historical_record':{'date':'2026-09-07','tier':5,'status':'attempted_unsolved',
   'path':'~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907/problems.jsonl',
   'line':56,'source_id':'bourgade_band_icm_2018','primary_locator':'section 2.1, printed page 7, equation (2.1)',
   'source_hash_from_intake_not_independently_recomputed':'b8b15c02ac7b675471097e9c499a6d588cfd7b0c591c49b0135f2a42eaedddb0'},
 'primary_source':{'author':'Paul Bourgade','title':'Random band matrices','arxiv':'1807.03031',
   'url':'https://math.nyu.edu/~bourgade/papers/ICMProceedings.pdf',
   'model':'H_RS=Delta+lambda V on l2(Z^d); iid centered variance-one real site potentials',
   'statement_recovered':True,'goals':['infinite-volume absolutely continuous spectrum at weak disorder in d=3',
      'separate finite periodic-box GOE bulk microscopic statistics'],
   'quote_location':'STATEMENT_TO_ADVERSARY.md; one short primary-source quote',
   'exact_law_and_all_target_quantifiers_prescribed_by_survey':False},
 'lane_specialization':{'model':'H_g=A+gV on l2(Z^3); A nearest-neighbor adjacency; iid V uniform[-1,1]',
   'variance_normalization':'variance-one uniform potential is sqrt(3)V, so g=sqrt(3)lambda',
   'quantifiers':'There exist deterministic I nonempty open inside(-6,6), g0>0; for each fixed 0<g<g0 an almost-sure spectral conclusion. No common event for every coupling asserted.',
   'target':'nonzero ac component; pure ac is a stronger sufficient target',
   'GOE_target':'periodic-box point process unfolded by volume times positive density of states; no proof here'},
 'recent_primary_claim':{'date':'2026-09-23','author':'OpenAI','title':'Absolutely Continuous Spectrum for Weak-Disorder Anderson Models in Dimensions at Least Three',
   'url':'https://github.com/openai/math/tree/main/preprints/Absolutely-Continuous-Spectrum-for-Weak-Disorder-Anderson-Models-in-Dimensions-at-Least-Three-September-23-2026',
   'checked_sections':'README; introduction model and main theorem; scope paragraph',
   'claimed_model':'nearest-neighbor Z^d, iid uniform[-1,1], each fixed sufficiently small positive coupling',
   'claimed_conclusion':'purely ac spectrum and nonzero weight on an open interval for each fixed d>=3',
   'GOE_theorem_in_checked_introduction':False,'proof_independently_verified':False,
   'status':'CLAIM_FOUND_NOT_CERTIFIED; not used as an established theorem'},
 'established_input':{'authors':'Combes, Germinet, Klein','arxiv':'0804.3202v3',
   'url':'https://arxiv.org/pdf/0804.3202','locator':'equations (1.4),(2.7); Remark 2.2(i)',
   'assumptions':'deterministic self-adjoint finite-volume hopping; independent diagonal site laws with densities bounded by R',
   'statement':'E[n_Q(n_Q-1)] <= (R |Q| N)^2 for each bounded interval Q',
   'our_R':'1/(2g)','source_statement_checked':True,'not_an_eigenvector_mark_estimate':True},
 'owner_solved_or_retired_check':{'scoped_records':['original C0056 intake/attempt','H/I exact-ID searches','Lean ranking annotation','Team O board','read-only population store'],
   'current_retirement_decision_verified':False,'reason':'No verified owner retirement decision located in the scoped named material; current public proof claim is not an audit.'},
 'store_snapshot':{'path':'~/math-brain-build/local/population/brain.sqlite3','mode':'ro',
   'scoped_evidence':'STORE_C0056_CARDS.json','existing_problem_truth_status':'unverified',
   'existing_problem_logical_id':'math:probability.random-matrices:open-problem-c0056-extended-states-for-the-three-dimensional-anderson-model-at-weak-disor'},
 'served_identity':{'worker':'w483','native_thread_id':os.environ.get('CODEX_THREAD_ID'),
   'requested_model':'gpt-6.1-sol','requested_reasoning':'max','requested_service_tier':'Fast',
   'response_side_served_model_evidence':None,'served_model_status':'UNKNOWN','served_tier_status':'UNKNOWN',
   'note':'Requested settings, worker label and turn context do not prove served identity.'},
 'independent_review':{'referee':'w485','review_of_referee_own_new_results':'w488','status':'PENDING',
   'different_model_gate_passed':False,'different_account_gate_passed':False},
 'brain_states':{'prepared':True,'submitted':False,'reviewed':False,'ingested':False,'retrievable':False}
}
(base/'SOURCE_STATUS.json').write_text(json.dumps(source_status,indent=2,ensure_ascii=False),encoding='utf-8')

statements={
 'L1':('For any finite positive Borel measure nu on R and eta>0, ||P_eta*nu||_2^2 equals the nu-by-nu integral of P_(2eta)(s-t), and equals (2pi)^-1 integral exp(-2eta|u|)|nu_hat(u)|^2 du; finite atomic measures give the full nonnegative weighted eigenvalue-pair sum.',
       ['nu finite positive Borel','P_eta(t)=eta/[pi(t^2+eta^2)]','Fourier transform nu_hat(u)=integral exp(-iuE)nu(dE)']),
 'L2':('For a measurable random finite positive measure with uniformly bounded mass, sup_(0<eta<=1) E||P_eta*nu||_2^2 is finite iff nu has an almost-sure L2 density f with E||f||_2^2 finite; the supremum equals that expectation. For countably many cutoffs covering a lattice energy interval, stationary local bounds imply pure ac restriction, with nonzero weight a separate obligation.',
       ['measurable random finite positive measure','uniformly bounded mass','stationarity and countable lattice basis for the lattice consequence']),
 'L3':('If finite-volume positive local measures of mass at most one obey E C_nuL(r)<=A r+B/N_L for every r>0 with volume-independent A,B, then E||P_eta*nu_L||_2^2 <= A/2+B/(2pi eta N_L). Here C_nu(r) is the same-measure pair mass at energy separation at most r.',
       ['A,B finite and independent of volume,r','N_L->infinity','all r>0 covered','nu_L mass at most one']),
 'L4':('For bounded iid-uniform nearest-neighbor lattice operators, local cutoff spectral measures of expanding Dirichlet cubes have smoothed L2 second moments converging to the infinite-volume moment at each fixed eta>0. The L3 bound therefore passes first in volume, then in eta, to the L2 criterion.',
       ['H=A+gV, fixed g>=0','bounded potential |V|<=1','fixed site inside expanding Dirichlet cubes','continuous compactly supported real cutoff']),
 'L5':('Real symmetric finite matrices with all eigenvector squared components and IPR equal to 1/N can have local measures converging to singular-continuous Cantor measure. With N=2^k and eta=N^-1/2, the diagonal smoothing contribution is 1/(2pi sqrt(N))->0, while the full second moment is at least N^((1-log(2)/log(3))/2)/(5pi)->infinity.',
       ['Walsh-basis matrix of multiplication by truncated fair ternary digit sum','abstract nonlocal matrices; not iid Anderson operators','countable infinite Walsh basis for the multiplication-operator limit']),
 'L6':('For finite-volume Anderson matrices with site-density bound R and cutoff support length W>0, if E sum_j a_j^2<=D/N and E[a_j a_k | all ordered eigenvalues]<=K/N^2 for j!=k uniformly in volume, then E C_nuL(r)<=max(18KR^2W,1/W)r+D/N for every r>0. The conditional mark hypothesis is explicitly UNPROVED for the target.',
       ['independent bounded-density diagonal site laws; deterministic self-adjoint hopping','simple ordered eigenvalues','a_j=chi(E_j)^2|phi_j(x)|^2, 0<=chi<=1','D,K independent of volume','conditional mark hypothesis, not mere unconditional moments or IPR']),
 'L7':('The free adjacency operator on Z3 has local density f1*f1*f1, f1(s)=1/[pi sqrt(4-s^2)] on(-2,2); its squared L2 norm is bounded by B(1/2,1/4)^2/(2pi^3). This calibrates the cutoff smoothing criterion at zero disorder only.',
       ['g=0','normalized Haar Fourier measure on torus','0<=chi<=1 for cutoff consequence']),
 'L8':('If X is uniform[0,1] and nu_X=delta_X, its averaged measure has bounded density one while each quenched measure is pure point and E||P_eta*nu_X||_2^2=1/(2pi eta). A bounded first averaged density alone does not prove quenched ac.',
       ['abstract one-dimensional random atom measure','not an Anderson counterexample'])
}
existing=[json.loads(s) for s in (base/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if s.strip()]
existing_ids={r['id'] for r in existing}
new=[]
for label,(statement,assumptions) in statements.items():
    claim_id='w483-'+label
    if claim_id in existing_ids:
        continue
    section=re.search(r'(?ms)^'+label+r'\..*?(?=^L\d+\.|^Single hardest gap\.|\Z)',attempt).group(0)
    new.append({'id':claim_id,'candidate_id':'C0056','statement':statement,'assumptions':assumptions,
      'source':'owner-own-work: ATTEMPT.md '+label+('; Combes-Germinet-Klein arXiv:0804.3202v3 (1.4),(2.7)' if label=='L6' else ''),
      'proof_or_counterexample':section,'independent_reviewer':'w485','review_status':'PENDING',
      'remaining_gap':'No gap in the stated auxiliary argument identified by author; independent check pending. Parent marked-pair estimate and GOE limit not proved.'+(' The conditional mark hypothesis itself is UNPROVED.' if label=='L6' else ''),
      'status':'proved special case','scope':'author-proved auxiliary statement, not independently checked parent proof',
      'formal_check':False})
gap_id='w483-G001'
if gap_id not in existing_ids:
    new.append({'id':gap_id,'candidate_id':'C0056','statement':'At each fixed sufficiently small nonzero g, cutoff local measures of nearest-neighbor iid-uniform Z3 Dirichlet restrictions satisfy E C_nuL(r)<=A(g,chi)r+B(g,chi)/|Lambda_L| uniformly in r,L.',
      'assumptions':['H=A+gV on Z3','iid V uniform[-1,1]','fixed nonzero small g','cutoff supported inside a nonempty free-band interval'],
      'source':'owner-own-work: ATTEMPT.md Single hardest gap; GAP.md',
      'proof_or_counterexample':'No proof. L6 supplies a sufficient conditional mark estimate, which is also unproved.',
      'independent_reviewer':'w485','review_status':'PENDING','remaining_gap':'Prove the marked-pair bound for the true random lattice operator; nonzero weight and GOE remain separate obligations.',
      'status':'conjecture','scope':'unproved sufficient strengthening; no novelty claim'})
with (base/'CLAIMS.jsonl').open('a',encoding='utf-8') as stream:
    for row in new:
        stream.write(json.dumps(row,ensure_ascii=False)+'\n')

own_source={'source_id':'owner-probability300-w483-c0056-20261010',
            'url':(base/'ATTEMPT.md').as_uri(),'revision':'author-draft-2026-10-10-v1',
            'license':'owner-own-work (campaign mathematics; unreviewed DRAFT concepts)', 'excerpt':None}
def entry(key,logical,title,statement,assumptions):
    return {'key':key,'namespace':'probability.random-operators','logical_name':logical,
            'kind':'concept','title':'DRAFT: '+title,
            'statement':'UNREVIEWED DRAFT, not a solution of C0056. '+statement,
            'proof_text':None,'assumptions':assumptions,'domain':'spectral theory and probability',
            'source':dict(own_source)}
entries=[
 entry('pair-calculus','local-spectral-measure-poisson-pair-calculus','Local spectral-measure Poisson pair calculus',statements['L1'][0]+' The annealed uniform L2 criterion in L2 is stronger than mere absolute continuity.',statements['L1'][1]),
 entry('pair-route','anderson-cutoff-weighted-pair-concentration-route','Conditional weighted-pair route to absolute continuity',statements['L3'][0]+' For bounded lattice Dirichlet approximations, take volume to infinity at each fixed eta before sending eta to zero; the result gives pure ac on covered cutoff windows if the displayed unproved bound holds.',statements['L3'][1]+statements['L4'][1]),
 entry('mark-gap','anderson-conditional-eigenvector-mark-moment-gap','Missing conditional eigenvector mark estimate',statements['L6'][0]+' Minami-type unweighted eigenvalue counts do not supply the mark assumption.',statements['L6'][1]),
 entry('cantor-obstruction','flat-walsh-eigenvectors-cantor-spectral-obstruction','Flat eigenvectors with singular continuous spectral limit',statements['L5'][0]+' The abstract counterexample refutes an IPR-only inference, not the Anderson conjecture.',statements['L5'][1]),
 entry('free-calibration','free-three-dimensional-adjacency-l2-density-calibration','Zero-disorder spectral-density calibration',statements['L7'][0],statements['L7'][1]),
 entry('scope-guard','c0056-ac-goe-separate-obligations-current-status-guard','Separate C0056 spectral and GOE obligations','The recovered Bourgade 2018 section 2.1 target combines weak-disorder ac spectrum on Z3 with a separate periodic-box GOE microscopic-statistics goal. The explicit uniform[-1,1] slice here has fixed-coupling quantifiers. A September 23, 2026 primary preprint claims the spectral part, but it is not independently certified in this packet. Current openness is UNKNOWN. This route proves neither parent goal; existence of an ac component, purity, nonzero spectral weight, and GOE statistics are distinct assertions.', ['primary statement recovery in STATEMENT_TO_ADVERSARY.md','public preprint statement is a claim, not an accepted input','no GOE limit proved'])
]
existing_problem=source_status['store_snapshot']['existing_problem_logical_id']
relations=[
 {'from_key':'pair-route','to_key':'pair-calculus','kind':'depends_on','rationale':'The conditional concentration bound is integrated against the exact Poisson pair kernel before the fixed-eta volume limit.'},
 {'from_key':'mark-gap','to_key':'pair-route','kind':'depends_on','rationale':'The explicitly unproved conditional mark bounds plus the established count inequality would yield the weighted pair estimate.'},
 {'from_key':'cantor-obstruction','to_key':'pair-calculus','kind':'semantic_association','rationale':'The exact kernel sum has diverging cross terms despite a vanishing diagonal in the flat Walsh example.'},
 {'from_key':'cantor-obstruction','to_key':'mark-gap','kind':'semantic_association','rationale':'An IPR bound alone cannot replace the required marked-pair control; the example makes no statement about iid lattice geometry.'},
 {'from_key':'free-calibration','to_key':'pair-calculus','kind':'specializes','rationale':'At g=0 the free Z3 local density satisfies the smoothing criterion with an explicit finite constant.'},
 {'from_key':'scope-guard','to_existing_logical':existing_problem,'kind':'cites','rationale':'The read-only source node and Bourgade p7 both retain AC and a separate GOE obligation.'},
 {'from_key':'pair-route','to_key':'scope-guard','kind':'semantic_association','rationale':'Even proving this sufficient pure-ac criterion would leave GOE statistics and the independent review gates unresolved.'}
]
bundle={'spec':'mathbrain-draft-v1','author_agent':'w483','bundle_slug':'probability-c0056-independent-spectral-pair-route-w483-001','entries':entries,'relations':relations}
(base/'DRAFT_bundle_001.json').write_text(json.dumps(bundle,indent=2,ensure_ascii=False),encoding='utf-8')

entry_by_key={e['key']:e for e in entries}
store_cards=json.loads((base/'STORE_C0056_CARDS.json').read_text(encoding='utf-8'))
problem_card=next(r for r in store_cards if r['title'].startswith('Open problem:'))
with (base/'RELATION_EVIDENCE.jsonl').open('w',encoding='utf-8') as stream:
    for i,rel in enumerate(relations,1):
        target=entry_by_key[rel['to_key']]['statement'] if 'to_key' in rel else problem_card['body']
        stream.write(json.dumps({'id':'w483-E'+str(i),'relation':rel,
          'from_card_quote':entry_by_key[rel['from_key']]['statement'],'to_card_quote':target,
          'source':'ATTEMPT.md and STORE_C0056_CARDS.json','status':'DRAFT_PENDING_INDEPENDENT_REVIEW'},ensure_ascii=False)+'\n')

hooks=[
 {'id':'spectral-pairs-w483-01','area':'math','event':'PostToolUse',
  'cue':'A delocalization proof infers quenched absolute continuity solely from IPR decay, flat finite-volume eigenvectors, or the diagonal smoothing contribution.',
  'fire_when':'The Walsh-Cantor sequence has IPR=1/N and diagonal 1/(2pi sqrt(N))->0; a proof claims these alone imply absolute continuity.',
  'silent_when':'A full weighted eigenvalue-pair bound uniform in eta is proved, or flatness is explicitly only a numerical diagnostic.',
  'text':'Before inferring absolute continuity from IPR or flat eigenvectors, bound the full weighted eigenvalue-pair sum. Cross terms can diverge while the diagonal vanishes. Record the volume and smoothing limits.',
  'evidence':'~/brain_workers/w483/ATTEMPT.md L5; MATH_CHECKS.json: N=256, diagonal=0.00994718, full moment=0.76837691, cross fraction=98.7054%.',
  'proposer':'w483'},
 {'id':'spectral-averaging-w483-02','area':'math','event':'PostToolUse',
  'cue':'A proof concludes almost-sure absolute continuity solely from a bounded disorder-averaged local spectral density or first-moment spectral averaging.',
  'fire_when':'X uniform[0,1], nu_X=delta_X: bounded averaged density one is used to assert quenched absolute continuity.',
  'silent_when':'The proof additionally establishes a quenched regularity criterion or a valid rank-one exceptional-set argument with all hypotheses, or leaves this step open.',
  'text':'A bounded averaged density alone does not imply quenched absolute continuity: a uniformly located random atom has that averaged density. State the additional quenched regularity or exceptional-set argument.',
  'evidence':'~/brain_workers/w483/ATTEMPT.md L8; MATH_CHECKS.json: second moment doubles at each halving of eta despite averaged density at most one. Calibration duplicates a core-lane trap, not a new theorem.',
  'proposer':'w483'}
]
(base/'HOOK_PROPOSALS.jsonl').write_text(''.join(json.dumps(h,ensure_ascii=False)+'\n' for h in hooks),encoding='utf-8')

files=['STATEMENT_TO_ADVERSARY.md','ATTEMPT.md','GAP.md','CLAIMS.jsonl','SOURCE_STATUS.json','PRIOR_ATTEMPT_DIGEST.md','MATH_CHECKS.json','COMPUTE_GATE.json','RELATION_EVIDENCE.jsonl','DRAFT_bundle_001.json']
packet={'candidate_id':'C0056','author_agent':'w483','created_at_utc':now,'role':'independent-route prover',
 'referee':'w485','independent_referee_for_referee_new_results':'w488',
 'statement_first_delivery':{'confirmed':True,'message_id':'msg-69b6caa21e','to':'w484','topic':'probability300/C0056/statement','peer_acknowledged':False},
 'served_identity':source_status['served_identity'],'review_status':'READY_FOR_REFEREE',
 'KEEP_scope_requested':'L1-L8 only, as scoped auxiliary arguments. Do not mark C0056 solved or certify the unproved mark hypothesis.',
 'hardest_gap':'Uniform marked-pair concentration for actual fixed-g Z3 operator; L6 conditional marks unproved.',
 'separate_gap':'GOE local statistics; nonzero weight must also be established if a pure-ac criterion is proved.',
 'numerical_receipt':'six PASS checks; no formalization or trusted-axiom certificate',
 'brain_states':dict(source_status['brain_states']),
 'file_hashes':{f:{'path':str(base/f),'sha256':hashlib.sha256((base/f).read_bytes()).hexdigest()} for f in files},
 'hash_note':'File transfer hashes only. No canonical bundle digest, source manifest, seal or release MAC generated.',
 'next':'Referee checks L1-L8 and especially L6 conditional measurability/constants; coordinator validates concept-only DRAFT after review.'}
(base/'REVIEW_PACKET.json').write_text(json.dumps(packet,indent=2),encoding='utf-8')

latest=checks['checks'][2]['evidence']['rows'][-1]
report=f'''C0056 remains unproved in this packet. I recovered the source and separated its absolutely-continuous-spectrum goal from periodic-box GOE statistics. Current openness is UNKNOWN because a recent primary preprint claims the spectral part and no independent certification or owner retirement decision was verified.

ATTEMPT.md contains eight scoped auxiliary arguments. The substantive route converts a weighted nearby-eigenvalue-pair estimate into a quenched L2 density criterion. The verified Minami counting theorem becomes sufficient only after an explicitly UNPROVED conditional eigenvector-moment hypothesis. The Cantor/Walsh example shows why vanishing IPR and a vanishing diagonal term alone fail. L8 is a calibration trap also present in the core lane; no novelty is claimed.

Measurement command: {checks['command']}. All {checks['check_count']} deterministic sanity checks passed in {checks['elapsed_compute_seconds']:.5f} seconds of compute after a fresh resource gate. The independent energy quadrature differs from the exact pair formula by 2.64e-7. In the flat Cantor example, N=4 to 256 reduces the diagonal from 0.0795775 to {latest['diagonal']:.7f}, while the full smoothed moment rises from 0.2659547 to {latest['S']:.7f}; cross terms contribute {100*latest['off_diagonal_fraction']:.4f}% at N=256. The analytic lower bound proves divergence for the full sequence. These checks are not a formal proof receipt.

Prepared: 8 auxiliary claim rows plus the explicit conjectural gap, 6 concept-only draft entries, 7 proposed relations with both ends quoted, and 2 hook proposals with fire/silent cases. All review, ingestion and retrievability states remain separate. No live store or recall setting was changed; no measured improvement to deployed recall is claimed.

Apply: the validating coordinator reviews DRAFT_bundle_001.json / the submitted inbox copy, keeps it as unreviewed concept material until the required independent checks pass, and performs the canonical integration ceremony. No code patch is required for this research packet, and I did not run integrate_drafts.py against the live store.

Risks and limits: L6's marked-eigenvector estimate could fail even when an ac component exists; this route is a sufficient strengthening. The counterexamples use abstract nonlocal operators and do not refute the Anderson conjecture. Current public-proof status and response-side served-model identity are uncertified. GOE statistics and nonzero spectral weight are not proved.

NEXT: w485 checks the exact auxiliary statements and L6's conditional sigma-field and constants; a future proof step must establish the marked-pair estimate for the true Z3 operator.
'''
(base/'REPORT.md').write_text(report,encoding='utf-8')
print(json.dumps({'prepared_entries':len(entries),'relations':len(relations),'new_claim_rows':len(new),'checks':checks['status'],'packet':str(base/'REVIEW_PACKET.json')},ensure_ascii=False),flush=True)
