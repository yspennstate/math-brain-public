from pathlib import Path
from fractions import Fraction
import json,hashlib,datetime,sys
R=Path(__file__).resolve().parents[1]
OWN=R.parents[1]
def save(name,o):
    (R/name).write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(name):return json.loads((R/name).read_text(encoding='utf-8'))
check=read('out/CHECK.json') if (R/'out/CHECK.json').exists() else read('out/PILOT.json')
review=read('out/REVIEW_MIXED.json')
fixture=read('out/PATH_CHILD.json')
assert check['status']==review['status']==fixture['status']=='PASS'
# A tiny core-Lean arithmetic translation, never a certificate for all FEI steps.
formal_source='import Lean.Elab.Tactic.Omega\n\ntheorem weak_child_int (p c d q : Int) (hp : 4*p <= d) (hc : c <= p) (hq : q = p+c) : 2*q <= d := by omega\n'
lp=R/'code/WeakChild.lean'
lp.write_text(formal_source,encoding='utf-8')
sys.dont_write_bytecode=True
sys.path.insert(0,r'~\.claude\dreaming')
try:
    import lean_check
    lr=lean_check.check_source(lp.read_bytes(),target='weak_child_int',reviewed_sha256=sha(lp),timeout=25,source_path=lp,output_root=R/'out/lean',use_mathlib=False)
except Exception as exc:
    lr={'status':'NOT_VERIFIED','detail':str(exc)}
save('out/LEAN.json',lr)
lean_status=lr.get('result',lr).get('status','UNKNOWN')
supplement="""

## 5. Arbitrary-seed admission and a genuinely different child resource
The zero-character-release endpoint is SAME-K FEI-hard. For each fixed nonconstant seed f, reuse the explicit balanced tensor activation: g_t=z product of t independent seed copies, k=max(2,ceil(sqrt(t))), p=2^-k, and F_t=1 off the active control point, F_t=g_t on it. Then max influence<=p<=1/4, every tau_i=0 EXACTLY, I=p(1+tI(f)+k)->0, and
H=p tH(f)+(4p-2p^2)k-(1-p)^2 log2((1-p)^2).
Thus H(F_t)/I(F_t)->H(f)/I(f). This uses the previous A005 finite activation ledger, not an assumed FEI bound. It admits each fixed seed into the endpoint but does not admit violating seeds into genuine minimal witnesses.

The separately frozen N11 certificate uses the actual A052 m3 path address seed h with C=(0,1,3,6,12,24,48,32), then k2 point activation. It has full affine spectral span, is affine influence-minimal, has mean25/32, I=19/16, and maximum influence7/32<=1/4. Every original physical child's character release is zero, but its total expected full-affine child release is POSITIVE (the exact value and all22 child transforms are in out/PATH_CHILD.json). The certificate constructs actual transformed Boolean children, checks entropy-preserving coefficient permutations, and verifies every root affine-minimum inequality using independent physical translations.

For clarity, affine minimum is certified by a cheapest independent parity basis. The finite exchange argument is elementary: after k greedy choices, any minimum-cost basis can be modified to include them, by replacing a row of its fundamental circuit outside the preceding greedy span. That row has cost at least the chosen cheapest available row. The replacement is independent and does not raise total cost; induction proves optimality. Output translation centers each chosen parity at its majority independently. All sampled affine transforms preserve the multiset of squared coefficients.

This N11 root is NOT critical. The original data directions2 and3 have no Fourier support edges, as in the path proof. Activation adds control-only coefficients on data label0, which already belongs to the code, and adds no new data label. Hence no such support edge is introduced: the four actual queried children retain the complete nonzero squared spectrum while their influence decreases by1/16. Their ratio exceeds the root ratio. This exact physical-descendant exclusion prevents calling the positive affine release a paid minimal-witness bank.

The analytic conclusions reach an author-checked proof with exact finite validation; independent review remains pending. A055's genuine K2 mixed-refund control is independently accepted at DERIVATION Sections2--3 only. Its low-K example is not extrapolated to high K.
"""
proof=R/'DERIVATION.md'
text=proof.read_text(encoding='utf-8')
if '## 5. Arbitrary-seed' not in text:
    proof.write_text(text+supplement,encoding='utf-8')
statement='For every finite uniform Boolean sign f, write p_j=Inf_j(f), c_ij=sum_{T off i,j in T} fhat(T)fhat(T+i), and tau_i=E_b[I(f_i=b)-min_U I(chi_U f_i=b)]. Then the child marginals are p_j+/-2c_ij and tau_i=(1/2)sum_{j!=i}[(2p_j+4c_ij-1)_+ +(2p_j-4c_ij-1)_+]. If p_j<=1/2 this equals sum_{j!=i}(p_j+2abs(c_ij)-1/2)_+. If max p_j<=1/4, every tau_i=0. For all K>=0, with D=H-KI, S_i^char=E_b[K min_U I(chi_U child)-H(child)], DTC=H-sum_i B_i, and JS_i=H-EH(child)-B_i, the exact SAME-bank identity DTC+(n-1)D+sum_i S_i^char+K sum_i tau_i=sum_i JS_i holds. On a least-essential-dimensional positive K-violator, all S_i^char>=0, so (n-1)D+K sum_i tau_i<=2I/ln2; if K>=2+3/ln2 all tau_i vanish. The rare/weak zero-release endpoint still admits every nonconstant Boolean seed with H/I preserved in the limit. A fixed N11 weak full-span affine-minimal Boolean root has zero character child release but strictly positive full-affine child release, without being critical.'
claim={
 'claim_id':'A005-CONDITIONAL-CHARACTER-BANK-VACUITY','version':1,
 'exact_statement':statement,
 'hypotheses':['Finite uniform cubes; actual Boolean signs, normalized real Walsh coefficients, entropy bits','All ratios only for nonconstant seeds; continuous zero entropy terms','Full character optimization is over actual physical child variables; no branch transform is silently a parent relabelling','Critical conclusions require least essential dimension among positive fixed-K violators, K>=0; no child is assumed critical','High-K threshold is exact 2+3/ln2; inclusive p_j=1/4 is allowed in the vanishing statement','The named N11 certificate is a deliberate fixed source-bound construction, not an exhaustive dimension escalation or FEI counterexample'],
 'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),
 'contributors':['account03/A005'],'proof_source':['DERIVATION.md Sections1--5','code/check.py','out/CHECK.json' if not check.get('pilot') else 'out/PILOT.json','code/path_child.py','out/PATH_CHILD.json'],
 'proof_dependencies':['Elementary physical restriction, Parseval and character modulation identities','Established scalar JS<=2Inf_i/ln2, reproduced by the coefficient-series explanation in REVIEW.md','Previous A005 balanced tensor activation formula; re-instantiated explicitly','A052 fixed path addressing construction, instantiated and independently checked; no criticality premise imported'],
 'review_records':[],'status':'AUTHOR_PROOF_EXACT_CERTIFICATES_PENDING_INDEPENDENT_REVIEW',
 'supersedes':[],'refutes':[],'first_unproved_line':None,
 'next_consumers':['A051','A052','A055','A002','A090','A094','B20']}
save('CLAIMS.json',[claim])
reviewtext="""# Scoped independent review and scalar dependency

HOLDS: A055-CRITICAL-MIXED-REFUND-OBSTRUCTION@1, DERIVATION Sections2--3 only. Exact source statement hash82bc4abb6ae28403f2008fbc7dcb9922ca30d6f9c002e63026930189e0dd53cd identifies the bundled source, not an acceptance of its entire bundled n4 census. Separate direct characters on all256 three-bit tables give exactly three spectral profiles, with minimum influences0,1,3/4. These certify point3 global D2 maximality. All22 lower-dimensional signs have D2<=0, checked by their character/bent profiles. The actual opposite-vertex mixed edits have zero crossing edges and T=6-(9/4)log2(3)>12/5 by243<256. No source repair is supplied and no high-K extrapolation accepted.

For completeness the JS bound used in the new universal consequence is independent of FEI. In a real spectral pair (a,b), set q=a^2+b^2, r=2ab/q when q>0. Its natural-unit JS contribution is q times j(r), where j(r)=((1+r)ln(1+r)+(1-r)ln(1-r))/2. For |r|<1 the even series coefficient at r^(2k) is1/[2k(2k-1)]. In 1-sqrt(1-r^2) that coefficient is a_k/(2k-1), a_k=binom(2k,k)/4^k>=1/(2k). The latter follows from a_1=1/2 and a_(k+1)=a_k(2k+1)/(2k+2). Coefficient comparison and continuity/monotone convergence at |r|=1 give j(r)<=1-sqrt(1-r^2). Thus the pair contribution in bits is <=2min(a^2,b^2)/ln2. Sum pairs to get JS_i<=2p_i/ln2, with q=0 contributing0. Booleanity normalizes both physical child spectra; no independence of spectral coordinates is assumed.
"""
(R/'REVIEW.md').write_text(reviewtext,encoding='utf-8')
save('SCOPE_VERDICTS.json',{'A055':{'claim_id':'A055-CRITICAL-MIXED-REFUND-OBSTRUCTION','version':1,'statement_sha256':'82bc4abb6ae28403f2008fbc7dcb9922ca30d6f9c002e63026930189e0dd53cd','verdict':'HOLDS_AT_DERIVATION_SECTIONS2_3_ONLY','reconstruction':'code/review_mixed.py; out/REVIEW_MIXED.json; REVIEW.md','contributor_conflict':False,'excluded':'n4 one-sign census, universal high-K payment'},'new_character_only_repair':{'verdict':'VACUOUS_ON_HIGH_K_MINIMAL_WITNESSES','threshold':'K>=2+3/ln2','not_refuted':'Full affine child optimization or genuine critical pair selection'}})
next_action='A052/A051 test full-affine child-basis release against the selected proper-pair signed interaction using the SAME unused D+S_pair bank and full terminals; character-only release is identically zero at high K. A055/A094 review the new identity and N11 noncritical scope.'
p={'protocol_revision':'2026-10-11-execution-v2','run_id':R.name,'stream':'B01','packet_id':'A005','gap_id':'G-R-SELECT','attempt_id':'A005-conditional-character-bank-1','method':'Scoped independent critical-counterexample review; exact child reserve identity and high-K mechanism exclusion; fixed full-affine child certificate','mathematical_delta':'Character-only child release vanishes on all pmax<=1/4 roots and all least-dimensional K-violators at K>=2+3/ln2; exact one-bank identity and arbitrary-seed admission. A named weak affine-minimal root has positive full-basis release but fails descendant criticality.','deliverable_status':'COMPLETE_LOCAL','mathematical_status':'SCOPED_AUTHOR_PROOF_REVIEW_PENDING_FULL_FEI_OPEN','claim_versions_used':['A055-CRITICAL-MIXED-REFUND-OBSTRUCTION@1 (Sections2--3 independently accepted)','A052 path code construction (fixed instance independently reconstructed)','Previous A005 balanced activation formula (explicit instance)'],'claims_created_or_changed':[claim['claim_id']+'@1'],'source_artifacts':['DERIVATION.md','REVIEW.md','SCOPE_VERDICTS.json','out/SOURCE_MANIFEST.json','out/FROZEN_SPEC.json','out/FROZEN_REVIEW.json','out/FROZEN_PATH_CHILD.json','out/FAILED_V1_FULL.json','out/PILOT.json','out/CHECK.json' if not check.get('pilot') else 'out/PILOT.json','out/PATH_CHILD.json','out/REVIEW_MIXED.json','out/LEAN.json'],'next_consumers':['A051','A052','A055','A090','A094','B20'],'next_action':next_action,'stagnant_substantive_attempts':0,'blockers':['Full-affine selected-pair payment from genuine criticality remains open; named positive-release root is noncritical','Independent review, registry adoption, supervisor copy and remote mirrors unverified'],'packet_ids':['A005']}
save('PROGRESS.json',p);save('PACKET_DELTA.json',p)
total=check['assertions']+review['assertions']+fixture['assertions']
report=f"""# exact target, quantifiers, hypotheses and units

A005/B01 current stage: audit whether optimizing the character phases of physical children creates a new reserve for universal critical pair payment. Every theorem is for actual Boolean signs on finite uniform cubes; H and JS in bits, influence unnormalized sum of directional influences. Exact critical threshold is K>=2+3/ln2. Full FEI remains OPEN. The current owner campaign end23October2026 14:49UTC governs over the historical protocol clock.

# sources actually read, revisions and theorem locators

Protocol2026-10-11-execution-v2 and current board22October23:09UTC, B01 STREAM_NOTESv1, own STATUS and prior stage were read. New substantive sources: A055 current REPORT and DERIVATION Sections1--4; A051 REPORT and AFFINE_SELECTION Sections1--6; A052 REPORT and PATH_CODE_PROOF Sections1--5; A002 REPORT. Source receipts pin bytes in out/SOURCE_MANIFEST.json. These replace no earlier full-paper audit; no new paper theorem or external web premise is used. A055's independent HOLDS review of the prior A005 refund reduction is consumed at its stated analytic scope. Brain wake reports stale owner-model/state notes; current owner instructions, not those notes, govern. The required read-only useless-work scan reported duplicate/idle candidates outside A005; none was safely attributable as own finished work, so none was stopped.

# complete derivation or exact first unsupported line

DERIVATION Sections1--5 prove the exact conditional character-release formula, SAME-bank identity and inclusive1/4 vanishing. A minimal K-violator has nonnegative optimized child reserves; the entropy/channel scalar bound forces pmax<exp(3)2^-K. Thus all character releases are exactly zero once K>=2+3/ln2. Arbitrary fixed seeds still enter the rare zero-release class with their H/I ratio preserved by the explicit balanced tensor activation. This repairs no terminal debt. A separate fixed N11 path-activation certificate has zero character release but total expected full-affine child release {fixture['full_affine_child_release']}; it has mean25/32, I19/16, max influence7/32, full span and affine minimality, yet fails actual descendant ratio-criticality. The root is not an admitted critical counterexample. First unsupported line: pay a selected proper-pair interaction from genuinely unused full-affine child surplus on actual minimal sources, keeping mixed T and every terminal in the SAME original account.

# executed validation with domain, arithmetic, commands and outputs

All specs precede jobs. Commands from A005: python -X utf8 runs/{R.name}/code/check.py --pilot, then without --pilot; code/review_mixed.py; code/path_child.py. Pilot278 tables/8928 assertions PASS. Primary final job: {check['roots']} labelled roots, {check['assertions']} assertions, {check['seconds']:.3f}s PASS; it checks all child marginals and release formulas, with exact prime-log bank identities through3bits. Mixed replay: {review['assertions']} exact assertions; fixed path/22 children: {fixture['assertions']} exact assertions, {fixture['seconds']:.3f}s. Total final assertions {total}, pilot excluded when the full primary job completed. Primary affine-minimal counts {check['affine_minimal_counts']}; weak counts {check['weak_counts']}. No whole-cube claim beyond the stated frozen domains. Original v1 full job hit its55s cap and established no completed n4 result; out/FAILED_V1_FULL records it. Equivalent integer FWHT parity costs and doubled integer positive-part arithmetic replaced repeated rational work, with the same dimension/runtime cap and pilot rerun before the final job. Arithmetic is integer Walsh/direct physical translations, Fraction and canonical prime-log identities, with exact integer strict signs. Named N11 is a deliberate source-bound fixed certificate, not an automatic exhaustive dimension escalation. RAM estimates30--100MB, peak unmeasured; no GPU, detached job or >300MB job. Core-Lean scalar attempt: {lean_status}. This concerns only a scaled integer inequality, not the full mathematical theorem; no unverified formal certification is claimed.

# proof dependencies and changed downstream conclusions

REVIEW.md independently accepts A055 DERIVATION Sections2--3, including actual finite maximality and zero-crossing mixed refund, without repair; its n4 one-sign census is not accepted through this replay. The JS scalar bound is reproduced with a convergent positive-coefficient series and its boundary cases. New theorem has an author-checked analytic proof and exact finite certificates, pending independent review. No universal FEI constant improves. The concrete change is that character-only child optimization is proved unable to contribute in the universal high-K critical regime. Full affine basis optimization is strictly different, but its positive named example does not meet critical child eligibility.

# one next mathematical action and independent reviewer

{next_action}

# actual persistence receipts or precise save blocker

Four protocol files, proof, scoped review, frozen specs, code and exact outputs saved only under A005. Finalizer checks exact required fields, byte-identical compatibility copy, statement hash and20MB cap; out/PERSISTENCE_RECEIPT.json hashes every run artifact except itself plus rolling files. STATUS has two lines; WORKLOG/LEARNED updated. Supervisor copy, private remote mirror, registry adoption and independent acceptance remain unverified; no local save blocker.

## Universal bridge

C019 stopping-tree payment through B11 critical-source selection: this stage rules out character-only optimized child reserves as a new resource at every K>=2+3/ln2, with an exact original-account identity and SAME-K arbitrary-seed admission to the rare zero-release endpoint. It also supplies an actual weak affine-minimal positive full-basis release certificate while preserving its failed criticality. Zero universal constant gain is claimed. The remaining bridge is full-affine child eligibility versus the original signed proper-pair debt, with mixed refunds and complete terminals retained. NEXT addresses that universal unpaid transfer; another character-only repair or qualitative weak-root admission is now provably vacuous in the hard regime.
"""
(R/'REPORT.md').write_text(report,encoding='utf-8')
fields=json.loads(Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))['required_per_run']
assert set(claim)==set(fields['claim_fields'])
pf=set(fields['progress_fields']);pf.remove('packet_ids (one primary ID, for compatibility)');pf.add('packet_ids')
assert set(p)==pf
for h in fields['report_fields']:assert '# '+h in report
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
(OWN/'STATUS.md').write_text(f'STATE: A005 current stage saved: character-only child reserve zero for high-K critical roots; full-affine release{fixture["full_affine_child_release"]} on weak N11 noncritical root;{total} exact assertions PASS; FEI OPEN.\nNEXT: A052/A051 pay original proper-pair interaction from SAME unused full-affine child bank with mixed T/full terminals; A055/A094 review identity and critical exclusion.\n',encoding='utf-8')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (OWN/'WORKLOG.md').open('a',encoding='utf-8',newline='') as f:
    f.write(f'\n{now} {R.name}: exact conditional-character release and SAME bank; tau=0 if pmax<=1/4, hence high-K minimality threshold2+3/ln2. Fixed weak/full-span/affine-minimal N11 has full-basis release{fixture["full_affine_child_release"]} but zero character release; noncritical scope retained. A055 actual K2 mixed guard independently HOLDS. Final{total} assertions PASS; v1 cap failure saved; Lean{lean_status}. Universal payment open.\n')
with (OWN/'LEARNED.md').open('a',encoding='utf-8',newline='') as f:
    f.write(f'\n{now} Conditional-character bank: p_j(child)=p_j+/-2c_ij, 2abs(c_ij)<=p_j. At pmax<=1/4 every child marginal<=1/2, so child character release is exactly0. DTC+(n-1)D+sum S_char+Ksum tau=sum JS<=2I/ln2 on minimal positive K-witnesses; K>=2+3/ln2 forces this zero-release regime. This is reallocation, not new payment. Arbitrary seed rare activation still has tau0 and preserves H/I. A fixed A052 path m3/k2 activation N11 gives full-affine child release{fixture["full_affine_child_release"]}>0 while character release0, full span and affine minimality; it is excluded from criticality by entropy-preserving data2/3 physical children with influence reduced1/16. A055 point3/K2 mixed control independently accepted Sections2--3 only. Do not count full-affine release again as unused original reserve.\n')
entries=[]
for q in sorted(R.rglob('*')):
    if q.is_file() and q.name!='PERSISTENCE_RECEIPT.json':
        assert q.stat().st_size<20_000_000
        entries.append({'path':str(q.relative_to(R)),'bytes':q.stat().st_size,'sha256':sha(q)})
for name in ['STATUS.md','WORKLOG.md','LEARNED.md']:
    q=OWN/name;entries.append({'path':str(q),'bytes':q.stat().st_size,'sha256':sha(q)})
save('out/PERSISTENCE_RECEIPT.json',{'status':'LOCAL_VERIFIED','at_utc':now,'files':entries,'independent_review':'PENDING','remote_copy':'UNVERIFIED'})
print(json.dumps({'status':'LOCAL_COMPLETE','final_assertions':total,'files_hashed':len(entries),'lean':lean_status,'full_affine_child_release':fixture['full_affine_child_release']}))
