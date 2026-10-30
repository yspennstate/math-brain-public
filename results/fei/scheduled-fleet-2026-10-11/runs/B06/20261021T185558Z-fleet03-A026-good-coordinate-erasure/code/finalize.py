from pathlib import Path
import json,hashlib,datetime,re
R=Path(__file__).resolve().parents[1];A=R.parent.parent
def read(p):return p.read_text(encoding='utf-8-sig')
def save(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
v=json.loads(read(R/'out/VALIDATION.json'));ind=json.loads(read(R/'out/INDEPENDENT.json'))
assert v['status']==ind['status']=='PASS'
assert v['ordered_branch_pairs']==272 and v['physical_coordinate_rows']==528 and v['assertions']==2790
assert ind['assertions']==103
base=Path(r'~\mop_fei100');globalroot=A.parent.parent
source_paths=[]
for folder,globs in [(base/'reports/fei-2026-10-11',['README.md','CURRENT_STATUS.md','EXECUTION_PROTOCOL.json','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','*.tex']),(base/'research_pushes/2026-10-11-full-fei-100-agents',['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md','sources/*.md']),(globalroot/'context',['*.txt'])]:
 for glob in globs:source_paths.extend(folder.glob(glob))
source_paths += [globalroot/'BOARD.md',globalroot/'claude/B06/STREAM_NOTES.md']
for who,run in [('A026','20261014T075434Z-fleet05-A026-good-coordinate-erasure'),('A027','20261014T104101Z-fleet05-A027-block-selection'),('A028','20261014T051435Z-fleet05-A028-stopping-tree-payment'),('A003','20261014T050612Z-fleet05-A003-minimal-target-formulation'),('A004','20261014T054158Z-fleet05-A004-constant-and-unit-ledger')]:
 for name in ['REPORT.md','PROOF.md','DERIVATION.md','CLAIMS.json']:
  p=globalroot/'agents'/who/'runs'/run/name
  if p.exists():source_paths.append(p)
sources=[];excerpts=[]
for p in source_paths:
 raw=p.read_bytes()
 try:s=raw.decode('utf-8-sig');enc='utf-8-sig'
 except UnicodeDecodeError:s=raw.decode('cp1252');enc='cp1252 legacy source, explicit fallback after UTF-8 failed'
 sources.append({'path':str(p),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'encoding':enc,'scope':'source text scan; report/proof passages read as cited; not blanket independent acceptance'})
 if p.suffix=='.txt' or p.parent.name=='sources':
  lines=s.splitlines();hits=[i for i,l in enumerate(lines) if re.search('Jensen|restriction|erasure|shared.data|isospectral',l,re.I)]
  excerpts.append({'path':str(p),'hits':[{'line':i+1,'context':'\n'.join(lines[max(0,i-2):i+4])} for i in hits[:10]]})
save(R/'out/SOURCE_MANIFEST.json',sources);save(R/'out/SOURCE_EXCERPTS.json',excerpts)
lean={'status':'RUNTIME_UNVERIFIED','seconds':120.2,'source_sha256':'57dd2bdf1193043cff1d13e4ca1ba7792db702e4534356730e3e79bb910da3d0','statement':'example (x a d : ℚ) (hx : x ≤ 1 / 8) (ha : a ≤ 11 / 4) (hd : d ≤ 3 / 32) : x + a + d < 3 := by linarith','scope':'only proposed rational bookkeeping core; no compiler acceptance or fidelity acceptance'}
save(R/'out/LEAN_RECEIPT.json',lean)
prior=json.loads(read(A/'runs/20261014T075434Z-fleet05-A026-good-coordinate-erasure/CLAIMS.json'))
oldclaims=prior if isinstance(prior,list) else prior['claims']
old=next((x for x in oldclaims if 'information' in x['exact_statement'].lower()),oldclaims[0])
extension=(' For every independent balanced Boolean encoder h and every finite adaptive data-only stopping tree on shared Boolean branches G,H, H(F)=T+J+B+delta H(h), and the signed data debit after booking future B+e delta is J_root-E J_leaf<=1 bit for any fixed e. '
 'For even m>=4, G is the point sign on m+1 data bits and H is a quadratic bent sign on m bits with a dummy j; h=Maj3. At j, D_JS/I_j(F)>=m-6 and the carried A028 boundary release equals I_j(F), so no finite local fixed influence price plus that release pays this booked bill. A common fresh dictator makes all four original j-child branches nonconstant without changing the obstruction. '
 'Every bent-block coordinate at the original root has true B_i(F)<=4 I_i(F); hence this is not an existential-selection refutation. For all even m>=6, the SAME original price-four terminal surplus pays all finite adaptive DATA-ONLY histories, complete remaining encoder entropy and full terminals, with margin at least7/64 bit. No bank renewal or universal unused-terminal-surplus assertion is made.')
statement=old['exact_statement']+' Stage17 extension:'+extension
claim={k:old.get(k) for k in ['claim_id','version','exact_statement','hypotheses','statement_sha256','contributors','proof_source','proof_dependencies','review_records','status','supersedes','refutes','first_unproved_line','next_consumers']}
claim.update(version=int(old['version'])+1,exact_statement=statement,statement_sha256=hashlib.sha256(statement.encode()).hexdigest(),hypotheses=['Uniform physical cubes; actual Boolean signs; bits and ordinary influence','Encoder and data cubes independent; encoder balanced and not queried in the DATA-ONLY history','Same original source terminal account; signed debits include refunds; all full terminal entropies retained','Counterfamily: even m>=4; all-history terminal payment: even m>=6; common-dictator lift optional'],contributors=['A026 (original reserve and stage17 extension)'],proof_source={'prior':str(A/'runs/20261014T075434Z-fleet05-A026-good-coordinate-erasure/PROOF.md'),'extension':str(R/'DERIVATION.md'),'selection_audit':str(R/'SELECTION_AND_AUDIT.md'),'validation':str(R/'out/VALIDATION.json'),'independent_finite_reconstruction':str(R/'out/INDEPENDENT.json')},proof_dependencies=[{'claim':old['claim_id'],'version':old['version'],'scope':'retained previous statement; new derivation uses its shadow notation and actual bank setup'},{'source':'A028 stage5 DERIVATION equations7,9','scope':'boundary reserve definition; release at the fixture also recomputed physically'}],review_records=[],status='AUTHOR_PROOF_EXACT_CHECKS_INDEPENDENT_REVIEW_PENDING',supersedes=[{'claim_id':old['claim_id'],'version':old['version'],'scope':'adds signed data-debit clause, retaining prior conclusions'}],refutes=['Universal fixed C payment of the signed booked DATA debit by C times actual query influence plus A028 boundary release'],first_unproved_line='For arbitrary terminals and mixed encoder/data histories, select an actual physical query/tree whose complete signed J loss, future erasure and both full terminal debts are funded by genuinely unused SAME original influence/child surplus.',next_consumers=['A003','A004','A027','A028','A087','A094','A096'])
claim['hypotheses'] = list(old.get('hypotheses', [])) + ['Stage17 extension only: '+x for x in claim['hypotheses']]
save(R/'CLAIMS.json',[claim])
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':R.name,'stream':'B06','packet_id':'A026','gap_id':'C018-C019-SAME-OWNER-SIGNED-DATA-PAYMENT','attempt_id':'A026-stage17-signed-JS-booked-data','method':'Exact balanced-sector decomposition; signed JS telescope; all-dimensional point/bent obstruction; same-source terminal payment; exact finite independent representations','mathematical_delta':'Identifies actual booked signed DATA debit as JS decrease; refutes every finite local influence-plus-release price on actual Boolean family, while selecting a good root coordinate and paying all DATA-only histories from the original supplied surplus for even m>=6. Full FEI remains OPEN.','deliverable_status':'COMPLETE_LOCAL','mathematical_status':'SCOPED_AUTHOR_PROOF_AND_EXACT_FINITE_CERTIFICATES_FULL_FEI_OPEN','claim_versions_used':[{'claim_id':old['claim_id'],'version':old['version']},'A028-UNBALANCED-ACTIVATION-STOPPING-PAYMENT@5 (reserve clause only)'],'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':claim['version']}],'source_artifacts':['DERIVATION.md','SELECTION_AND_AUDIT.md','FROZEN_SPEC.json','INDEPENDENT_SPEC.json','code/check.py','code/independent.py','out/VALIDATION.json','out/INDEPENDENT.json','out/SOURCE_MANIFEST.json','out/LEAN_RECEIPT.json'],'next_consumers':claim['next_consumers'],'next_action':'A028/A087/A094 independently reconstruct the all-m signed-JS local-price obstruction; seek a signed, policy-selected SAME-bank payment using actual terminal surplus for non-bent unequal branches, not a fixed local release rule.','stagnant_substantive_attempts':0,'blockers':['Universal unused child-surplus/selection lemma unresolved','Independent analytic review and supervisor adoption/mirror unverified','Lean arithmetic probe timed out; no Lean-checked claim'],'packet_ids':['A026']}
save(R/'PROGRESS.json',progress);(R/'PACKET_DELTA.json').write_bytes((R/'PROGRESS.json').read_bytes())
report='''# A026 stage17: the booked DATA bill is a signed JS debit

Full FEI remains OPEN. The actual signed debit after booking future true shadow erasure is exactly a decrease of branch spectral Jensen–Shannon divergence. No finite local influence price plus the released boundary reserve pays this bill at every coordinate. Its signed cumulative price nevertheless telescopes, and a supplied terminal surplus can pay it once.

## exact target, quantifiers, hypotheses and units

For every independent balanced Boolean encoder held intact, and arbitrary shared Boolean data branches, identify and transport the booked DATA debit through every finite adaptive data-only stopping tree. Give an actual all-dimensional local-price obstruction, keep full terminals, and distinguish this from existential good-coordinate selection. Entropy is in bits and influence counts actual uniform physical flips. The point/bent obstruction uses even m>=4; its same-original-account history payment uses even m>=6. Querying inside the encoder is outside the theorem.

## sources actually read, revisions and theorem locators

Read full execution protocol v2, own STATUS/LEARNED/WORKLOG, BOARD B06 and current cross-stream reports, and B06 STREAM_NOTES v2. A026's substantive saved frontier was stage6; the ten later marker-only folders do not supply new mathematics. Read A026 stage6 PROOF sections1-6 and its actual control checker; A028 stage5 DERIVATION sections1,4,6,7; A027 stage6 signed-band direction; A003/A004 stage5 terminal-owner reports. The mandated campaign files, registry texts, plan, supplemental sources and four paper texts were scanned and source-pinned with relevant restriction/erasure locators in SOURCE_EXCERPTS. That intake is not an independent full-paper theorem audit. A strict UTF-8 intake initially stopped on a legacy non-UTF8 source; final intake explicitly records cp1252 fallback where needed, with raw-byte hashes unchanged. Read math-brain card claim_6e7bc03dfac275446242fa9ea2b79a1b9d6fc1c3be4040dbd7ec3a51056a36c3 as an unreviewed lead; its exact restriction identity was checked by direct spectra rather than treated as authority. No new literature-priority claim is made.

## complete derivation or exact first unsupported line

DERIVATION sections1-3 prove H(F)=T+J+B+delta H(h), the exact booked DATA debit D=J-E J_child, and the signed all-history telescope. The explicit point/bent family has physical query influence t/2 and boundary release t/2, while D>=t(m/2-3). Thus D/I_j>=m-6. The lower bound uses a controlled scalar second derivative, positive denominators and an explicit log remainder estimate; finite examples are not the all-m proof. A common-dictator lift preserves the obstruction and makes all four original branch children nonconstant. For the original family every bent-block coordinate is an actual good root coordinate with B_i<=4I_i; there is no refutation of C018 existential selection. True decrement also contains JS_i and is not identified with B_i.

The SAME original price-four terminal account has surplus at least m/2. The exact disagreement is (1-2^(-m/2)+2^-m)/2, not the small point parameter 2^-m. Accounting for both full terminals, future erasure, signed data debit and remaining Maj3 entropy leaves at least m/2-3+2^(-m/2)-2^-m, hence at least7/64 bit for all even m>=6 and every adaptive DATA-only history. Signed refunds are retained and no positive-part summation or renewed descendant bank is allowed. First unsupported universal line: obtaining such UNUSED terminal surplus and selecting a payable physical history for arbitrary branches and mixed encoder/data restrictions.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC preceded the pilot. Run python -X utf8 code/check.py --pilot, then code/check.py, from this run directory. Pilot:16 ordered one-bit pairs,96 assertions,PASS in0.224s. Main:272 ordered pairs through two data bits,528 physical coordinate rows,three actual point/bent roots m=2,4,6,five symbolic spectrum fixtures m=4,6,8,10,12,and three adaptive stopped DATA histories;2790 assertions,PASS in0.452s. Integer Walsh, independent physical flip counts, exact Fraction prime-log identities and outward atanh intervals certify the identities and signs. Full future encoder correction is present and both terminal functions are retained at every leaf.

Run python -X utf8 code/independent.py:103 exact direct-character-sum, common-dictator lift, parameter-bound and hypothesis-guard checks,PASS in0.020s. It imports no core helper. Balance and disjointness have explicit failing examples if omitted. This is independent finite representation reconstruction, not independent analytic acceptance. The Lean rational-bookkeeping probe returned RUNTIME_UNVERIFIED after120.2s and was not retried. Fraction verifies the same rational endpoint95/32<3. Rung: analytic author proof plus exact finite validation; no Lean-checked theorem. Arithmetic checks were estimated at180MB or less and capped55s; no >300MB arithmetic job was planned, and peak RAM was not measured. Lean-helper peak memory was not measured. No GPU, background task or automatic dimension escalation was used. Compute-state read reported status ok; no running work was stopped. The Lean probe's120.2s wait was in its bounded helper, not a successful mathematical check.

## proof dependencies and changed downstream conclusions

This narrowly extends the existing A026 disagreement-information candidate, retaining its previous statement, rather than opening another broad candidate at the review cap. A028's source bank conservation remains accepted only at the previously reviewed clause. Its price-three AND2 guard concerns a different bill; this stage's unbounded price concerns the bill AFTER future true erasure is booked. The two numbers do not conflict. A028/A027/A003/A004 must preserve a nonlocal signed J account or charge genuine child surplus; a fixed local influence-plus-release repair is insufficient. No universal FEI constant improves, no all-coordinate obstruction is promoted to an existential refutation, and no acceptance or downstream adoption is inferred.

## one next mathematical action and independent reviewer

A087 and A094 should independently reconstruct the exact JS debit, the all-m Phi bound and the nonconstant lifted terminals. A028 should replace its proposed fixed local repair for this booked bill by one signed whole-history balance. Next price one non-bent unequal-branch actual history from a supplied UNUSED same-source terminal surplus, retaining both reference/entropy terminal debts; the missing objective is a structural source for that surplus rather than another fixed-family dimension sweep.

## actual persistence receipts or precise save blocker

The four protocol files, derivation, audit, frozen specifications, self-contained copied arithmetic helper, code and exact outputs are saved only inside A026. PACKET_DELTA equals PROGRESS byte-for-byte. Rolling STATUS has exactly two lines; WORKLOG and LEARNED record this result and its limits. PERSISTENCE_RECEIPT checks schemas, statement hash, required report fields, sizes and file hashes. Local save is verified; independent review, supervisor copying, canonical adoption and remote mirrors remain unverified. No git, mail, trading system or other agent folder was modified.

## Universal bridge

This stage moves C018/C019/C024 by identifying the ACTUAL booked data-query bill as a signed JS difference and transporting it across every data-only adaptive history without renewal. The explicit Boolean family proves that no fixed local query-influence price plus released boundary bank can fund that bill, while retaining good actual root coordinates and full certified nonconstant terminals. The same original terminal account pays every such history for even m>=6 with margin>=7/64, so local-price failure need not imply failure of nonlocal payment. Universal improvement is zero: an unused-surplus theorem and selected history for arbitrary terminals remain open. NEXT seeks that source-owned signed surplus on unequal non-bent branches because another local constant, reserve envelope or isolated root-class calculation cannot repair the demonstrated obstruction.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8')
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
(A/'STATUS.md').write_text('STATE: Stage17 saved: signed DATA debit=JS drop; no fixed local influence+release price; same-owner all-history point/bent payment m>=6;2790+103 exact checks PASS; FEI OPEN.\nNEXT: A028/A087/A094 review all-m debit obstruction; source unused SAME terminal surplus for selected non-bent unequal-branch history with both full terminals.\n',encoding='utf-8')
for name,txt in [('WORKLOG.md',f'\n{stamp} | Stage17 {R.name}: balanced-sector identity identifies actual booked DATA debit as Jroot-EJleaf. Explicit point/bent D/I>=m-6 refutes any fixed local influence+boundary-release price, even with common-dictator nonconstant children; root bent coordinates remain good at4. Same original price-four surplus pays ALL data-only histories for even m>=6 with full margin>=7/64. Main2790 checks0.452s; independent direct-character103 checks0.020s PASS. Lean bookkeeping timed out120.2s; no formal claim. Marker-only stages7-16 supplied no new results.\n'),('LEARNED.md','\nStage17 durable update: for independent BALANCED intact h, H(A+hD)=avg H(G,H)+JS(PG,PH)+Bshadow+delta H(h). After booking future B+e delta, each actual DATA debit is exactly Jparent-average Jchild; any finite adaptive DATA-only history costs Jroot-EJleaf<=1 SIGNED bit. Never sum positive parts or query h under this identity. Point G on m+1 and bent H on m with dummy j give D/Ij>=m-6, releaseR=Ij; local fixed-price repair fails, not existential B selection (every bent-block coordinate has B<=4I). A common dictator preserves J/B and makes all four original j-child terminals nonconstant. Actual disagreement is (1-2^(-m/2)+2^-m)/2, NOT2^-m. Original S4>=m/2 pays full retained history+terminals for even m>=6, margin>=7/64; this is supplied bent surplus, not universal spare slack. Full FEI OPEN; next source a genuine unused signed terminal reserve.\n')]:
 with (A/name).open('a',encoding='utf-8') as f:f.write(txt)
protocol=json.loads(read(base/'reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'))['required_per_run']
pf=set(x.split(' (')[0] for x in protocol['progress_fields']);cf=set(protocol['claim_fields'])
assert set(progress)==pf and set(claim)==cf
for field in protocol['report_fields']:assert '## '+field in report
assert len(read(A/'STATUS.md').splitlines())==2
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
files=[]
for p in R.rglob('*'):
 if p.is_file() and '__pycache__' not in p.parts:
  assert p.stat().st_size<20_000_000
  files.append({'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)})
save(R/'out/PERSISTENCE_RECEIPT.json',{'status':'PASS','time_utc':stamp,'schema_checks':'exact claim/progress fields; all seven report fields; identical packet delta; two-line status','files':files,'rolling':[{'path':str(A/n),'sha256':sha(A/n)} for n in ['STATUS.md','WORKLOG.md','LEARNED.md']],'remote_mirror':'UNVERIFIED','independent_analytic_review':'PENDING'})
print(json.dumps({'status':'PASS','claim_id':claim['claim_id'],'version':claim['version'],'files':len(files),'main_assertions':v['assertions'],'independent_assertions':ind['assertions'],'full_FEI':'OPEN'}))
