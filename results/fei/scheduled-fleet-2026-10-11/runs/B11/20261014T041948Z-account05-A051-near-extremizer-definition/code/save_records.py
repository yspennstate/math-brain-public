from pathlib import Path
import hashlib,json,datetime
ROOT=Path(__file__).resolve().parent.parent
AGENT=ROOT.parent.parent;BASE=AGENT.parent.parent
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(name,x):(ROOT/name).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
statement=('For finite uniform-cube Boolean signs define T=sum_i O_i+sum_(i<j)R_ij from the actual signed merging refunds, '
 'and Theta=T/I for nonconstants. T and I are additive under disjoint tensor products. For a fixed nonconstant k-bit seed h '
 'with mean mu, balanced activation F of m disjoint copies at p=2^-r, r>=1, retains exactly pmT(h) on core coordinates. '
 'Its nonnegative remaining diagnostic E obeys E<=p+8pmk mu^(2m)+(64 binom(r,2)+14r)p^2. '
 'If r is least with2^r>=(m+1)^4 then T(F_m)->0, Theta(F_m)->Theta(h), with the explicit finite error in proof section4. '
 'For K>=4 its complete control/balance physical-child bank satisfies D_K(F)+S_B<-p and D_K(F)<pmD_K(h). '
 'If D_K(F)>0 then D_K(h)>0, S_B<0 and T(F)/D_K(F)>=T(h)/D_K(h); the wrapper is not dimension-minimal. '
 'A distance-three coded spectral law instead has T=I, Theta=1. A one-point edit on N bits at p=2^-N gives '
 '|T(edited)-I(coded)|<=4N sqrt(p)+16 binom(N,2)p and |I(edited)-I(coded)|<=2Np. '
 'Thus the logarithmic-redundancy hardness-preserving code/edit sequence of the consulted A005 construction has Theta->1. '
 'These are transport and eligibility statements, not a reserve-relative selected-block theorem or full FEI bound.')
claim={'claim_id':'A051-RELATIVE-DEFECT-REDUCTION-TRANSPORT','version':1,'exact_statement':statement,
 'hypotheses':['Finite uniform-cube Boolean signs; entropy in bits; actual signed Fourier-face refunds with zero denominators assigned zero',
 'Theta is defined only for nonconstant functions; tensor factors may be constant for the unnormalized identities',
 'Activation seed fixed and nonconstant, m>=1,r>=1,p=2^-r; finite no-decrease uses K>=4 and positive activated deficit',
 'The coding assertion requires minimum spectral distance3 before surgery; code/edit limiting ratio statement uses the actual systematic construction and counted tag influences',
 'Child reserves have their actual sign; wrappers are not declared critical; no global optimizer or universal paid block is assumed'],
 'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['account05/A051'],
 'proof_source':{'path':str(ROOT/'RELATIVE_TRANSPORT.md'),'sha256':digest(ROOT/'RELATIVE_TRANSPORT.md'),'locator':'Sections1--7; six CASE certificates, SUMMARY, INDEPENDENT_REPLAY and CODE_GUARD'},
 'proof_dependencies':[],'review_records':[],'status':'AUTHOR_PROVED_NARROW_TRANSPORT_EXACTLY_REPLAYED_PENDING_INDEPENDENT_AGENT_REVIEW',
 'supersedes':[],'refutes':['Balanced tensor activation erases T relative to a positive fixed-K deficit at K>=4',
 'All actual campaign reductions preserve Theta (distance-three coding instead produces Theta=1)'],
 'first_unproved_line':None,'next_consumers':['claude/B11','A052','A053','A055','A005','A090','A094','B20']}
save('CLAIMS.json',[claim])
s52=BASE/'agents/A052/runs/20261014T015635Z-account05-A052-critical-source-structure'
s55=BASE/'agents/A055/runs/20261014T033719Z-account05-A055-extremal-obstruction-referee'
s05=BASE/'agents/A005/runs/20261014T031720Z-account05-A005-noncircular-endpoint-referee'
sources=[Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json'),BASE/'BOARD.md',BASE/'claude/B11/STREAM_NOTES.md',
 s52/'REPORT.md',s52/'CLAIMS.json',s52/'SIGNED_PAIR_PROOF.md',s52/'DEPENDENCY_REVIEW.md',s55/'REPORT.md',s55/'PROOF.md',s05/'REPORT.md',s05/'DERIVATION.md',
 AGENT/'runs/20261014T012634Z-account05-A051-near-extremizer-definition/TWO_BIT_RESERVE.md',
 AGENT/'runs/20261014T012634Z-account05-A051-near-extremizer-definition/code/exact_tools.py',
 AGENT/'runs/20261014T012634Z-account05-A051-near-extremizer-definition/code/independent_arithmetic.py']
save('out/SOURCE_MANIFEST.json',[{'path':str(p),'bytes':p.stat().st_size,'sha256':digest(p)} for p in sources])
save('out/REVIEW_RECORDS.json',[
 {'claim_id':'A052-SIGNED-PAIR-ORIENTATION-REFUND','version':1,'statement_sha256':'0d5d1b3a63e30b4dd8764721c26540119443affc0750d61c11e42b7931ef71c7',
 'reviewer':'account05/A051','verdict':'HOLDS_NEW_ALGEBRA_AND_GUARDED_ORIENTATION_SUBSTITUTION',
 'scope':'New signed/refund identity and orientation comparison; guarded scalar premise independently reviewed in stage4. Bank insertion checked as an application, not independent re-review of authored A051 premise.',
 'review_source':str(ROOT/'REVIEW_A052.md'),'review_sha256':digest(ROOT/'REVIEW_A052.md'),'repair_supplied':False,
 'contributor_conflict_on_new_claim':False,'authored_prior_bank_premise':True,'independent_full_chain_reconstruction_claimed':False},
 {'claim_id':'A051-TWO-BIT-CRITICAL-PHASE-RESERVE','version':1,'statement_sha256':'25d00942803b7fd8918a198dc313101701674dc04a88f5919f6624bf28288e09',
 'reviewer':'account05/A052','verdict':'SOURCE_BOUND_INDEPENDENT_ACCEPTANCE_CONSUMED',
 'review_source':str(s52/'DEPENDENCY_REVIEW.md'),'review_sha256':digest(s52/'DEPENDENCY_REVIEW.md'),'registry_adoption_verified':False}])
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':ROOT.name,'stream':'B11','packet_id':'A051',
 'gap_id':'B11-UNIVERSAL-PROPER-BLOCK-SELECTION','attempt_id':'A051-stage5-relative-transport-and-eligibility',
 'method':'Source-scoped dependency review; exact tensor/activation relative diagnostic transport; finite high-K negative-child-bank obstruction; independent polynomial/variance replay; different near-code endpoint guard',
 'mathematical_delta':'T tensor-adds; balanced activation retains pmT(seed) exactly, Theta tends to seed with explicit O(logm/m) error, and positive K>=4 deficit cannot lower T/D_K. Full control/balance bank is<-p. Distance-three code instead has Theta=1 and puncture tends to1. No critical eligibility is manufactured.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACTS; supervisor mirrors unverified',
 'mathematical_status':'RELATIVE_REDUCTION_TRANSPORT_AND_FINITE_ELIGIBILITY_OBSTRUCTION_PROVED; CRITICAL_SELECTED_BLOCK_PAYMENT_AND_FEI_OPEN',
 'claim_versions_used':['A052-SIGNED-PAIR-ORIENTATION-REFUND@1 (new algebra and guarded substitution reviewed at explicit scope)',
 'A055-GLOBAL-ORIENTATION-REFUND-RIGIDITY@1 (source diagnostic/admission consumed; transport proof rederives needed facts)',
 'A051-TWO-BIT-CRITICAL-PHASE-RESERVE@1 (A052 independent acceptance consumed)',
 'A005 stage4 systematic-code-and-edit admission, DERIVATION sections1--4 (source context; relative diagnostic independently derived)'],
 'claims_created_or_changed':['A051-RELATIVE-DEFECT-REDUCTION-TRANSPORT@1','A052-SIGNED-PAIR-ORIENTATION-REFUND@1 scoped local review','A051-TWO-BIT-CRITICAL-PHASE-RESERVE@1 acceptance consumed'],
 'source_artifacts':['RELATIVE_TRANSPORT.md','REVIEW_A052.md','out/SOURCE_MANIFEST.json','out/REVIEW_RECORDS.json','out/SUMMARY.json','out/INDEPENDENT_REPLAY.json','out/CODE_GUARD.json','out/REPLAY_ATTEMPT1.json'],
 'next_consumers':['claude/B11','A052','A053','A055','A005','A090','A094','B20'],
 'next_action':'Compare signed parity cost minus merging refunds with actual D+S_pair and retained phase margin on genuine minimal K-witnesses; use exact activation/core and code/orientation ledgers as eligibility guards, not root-only smallness or D normalization.',
 'stagnant_substantive_attempts':0,
 'blockers':['No universal reserve-relative pair/larger-block selection theorem','Root-hardness reductions retain a negative physical-child reserve and cannot be granted criticality','New transport claim awaits independent-agent review; external mirrors/registry adoption unverified'],
 'packet_ids':['A051']}
save('PROGRESS.json',progress);save('PACKET_DELTA.json',progress)
(AGENT/'STATUS.md').write_text('STATE: A051 stage5 saved: T tensor-adds; activated core pmT exact, Theta->seed; K>=4 positive activation deficit cannot reduce T/D and full child bank<-p; code Theta->1;24812 exact main+87 code checks; FEI OPEN.\nNEXT: A052/A055 compare signed parity-minus-refund cost with actual critical D+S_pair/phase margin and one influence owner; retain activation core and code orientation; A090/A094 review transport and finite eligibility obstruction.\n',encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write('\n2026-10-14 04:19 UTC stage ('+ROOT.name+'): Read updated BOARD/B11/status and A052 signed pair, A055 global diagnostic, A005 same-C code endpoint. Scoped review accepts A052 new algebra/guarded substitution; authored A051 bank premise not re-reviewed independently. Proved exact T tensor additivity and activation core pmT, nonnegative wrapper bound and finite Theta error. At K>=4 full control/balance D+S<-p and positive D cannot lower T/D below seed ratio. Consumed code endpoint: Theta=1 before edit and ->1 after, through orientation rather than refunds. Pilot1616+562 and independent polynomial/physical-child replay22634 checks passed; code guards14+73 passed. Initial replay sign convention failed, persisted diagnosis and corrected polynomial to actual unchanged truth signs; all final checks pass. Original spec omitted n10 from explicit list although frozen formula already implied it; saved correction, no domain escalation. Complete schema/hash/size records and rolling files saved locally. No universal block payment, global optimizer, independent acceptance of new theorem or remote mirror claimed.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('''
- Relative diagnostic transport (stage5): T=sum O_i+sum R_ij tensor-adds exactly; I tensor-adds, so Theta=T/I is a weighted tensor average and invariant under powers. Cross-factor faces are rank one and refund zero. A balancing character contributes T=I=1.
- Balanced activation of m seed copies with mean mu and r controls, p=2^-r, retains EXACT core pmT(seed). Nonnegative wrapper E<=p+8pmk mu^(2m)+(64 binom(r,2)+14r)p^2. For r minimal with2^r>=(m+1)^4, absolute T->0 while Theta->Theta(seed), with explicit O(logm/m) error. Absolute-neighborhood hardness admission is not relative defect erasure by this mechanism.
- Strong finite eligibility obstruction: H(F)=pmH(seed)+4rp+A(p), A(p)<3p. For EVERY K>=4, D_K(F)+S_control,z<-p and D_K(F)<pmD_K(seed). Positive root deficit forces seed violation and negative complete child reserve. Hence T(F)/D_K(F)>=T(seed)/D_K(seed). Normalizing by positive root D alone does not replace the genuinely critical D+S bank.
- Different reduction, different relative ledger: minimum-distance3 coded spectra have beta_i=0, O_i=Inf_i and all pair refunds0, hence Theta=1 exactly. One-point surgery gives |T(edited)-I(coded)|<=4N sqrt(p)+16 binom(N,2)p and |I(edited)-I(coded)|<=2Np. A005 logarithmic code/edit admission tends to Theta1 while preserving seed ratio, with hard physical children retained. Do not assert Theta invariant under coding or discard orientation when refunds vanish.
- Stage5 exact pilot1616+562 checks and independent polynomial/separate-variance replay22634 pass;87 code-guard checks pass. A failed polynomial inverse check caught the opposite balancing-character convention; corrected explicit epsilon sign before acceptance, truth family unchanged. Source A052 new comparison reviewed with authored-bank scope caveat; A052 independent acceptance of prior A051 two-bit bank consumed. Uniform reserve-relative selection and full FEI remain open.
''')
protocol=json.loads(Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json').read_text())
assert set(progress)=={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
assert len((AGENT/'STATUS.md').read_text().splitlines())==2
report=(ROOT/'REPORT.md').read_text();assert all('# '+h in report for h in protocol['required_per_run']['report_fields'])
assert report.rsplit('\n## ',1)[1].startswith('Universal bridge\n')
pilot=json.loads((ROOT/'out/SUMMARY.json').read_text());replay=json.loads((ROOT/'out/INDEPENDENT_REPLAY.json').read_text());guard=json.loads((ROOT/'out/CODE_GUARD.json').read_text())
assert pilot['assertions']+pilot['helper_assertions']+replay['assertions']==24812
assert guard['assertions']+guard['diagnostic_internal_assertions']+guard['independent_internal_assertions']==87
receipt={'schema':'PASS','byte_identical_delta':True,'report_fields':'PASS','main_exact_assertions':24812,'credited_code_guard_assertions':87,
 'new_independent_agent_review':'PENDING','remote_mirror_verified':False}
save('out/HANDOFF_CHECK.json',receipt)
files=[p for p in sorted(ROOT.rglob('*')) if p.is_file() and '__pycache__' not in p.parts and p.name!='ARTIFACT_MANIFEST.json']
assert all(p.stat().st_size<20_000_000 for p in files)
save('out/ARTIFACT_MANIFEST.json',{'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'files':[{'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':digest(p)} for p in files],
 'rolling':[{'path':str(p),'bytes':p.stat().st_size,'sha256':digest(p)} for p in [AGENT/'STATUS.md',AGENT/'WORKLOG.md',AGENT/'LEARNED.md']],
 'all_files_under_20MB':True,'external_mirror_verified':False})
print(json.dumps({**receipt,'run':ROOT.name,'files_saved':len(files),'claim_hash':claim['statement_sha256']}))
