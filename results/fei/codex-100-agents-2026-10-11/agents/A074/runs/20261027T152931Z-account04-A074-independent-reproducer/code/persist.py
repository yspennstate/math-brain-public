from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
R=Path(__file__).resolve().parents[1];A=R.parent.parent
S=Path('agents/A072/runs/20261027T083832Z-account04-A072-exact-walsh-engine')
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def digest(c):return hashlib.sha256(json.dumps({k:c[k] for k in ('exact_statement','hypotheses')},sort_keys=True,separators=(',',':'),ensure_ascii=False).encode('utf-8')).hexdigest()
pilot,main,audit=(read(R/f'out/{x}.json') for x in ('PILOT','MAIN','AUDIT'))
assert pilot['status']==main['status']==audit['status']=='PASS'
assert main['actual_circuits']==8960 and main['positive_influence_rows']==7200 and main['equality_rows']==128
assert audit['rows']==8960 and audit['equality_representatives']==128
c=next(x for x in read(S/'CLAIMS.json') if x['claim_id']=='A072-EXACT-THREE-BIT-FULL-DRIFT-MAXIMUM')
source_digest=c['statement_sha256']
assert hashlib.sha256(c['exact_statement'].encode('utf-8')).hexdigest()==source_digest=='a559d3434d1645bb43c8b019a0bb315067bab9414791cc1b74889695a2446833'
c['statement_sha256']=digest(c)
assert c['statement_sha256']=='a1fba9c85283811e6060686b836193a0ad8858377c968443aed720b50b1c07d4'
write(R/'out/HASH_NORMALIZATION.json',{'source_statement_only_sha256':source_digest,'local_statement_and_ordered_hypotheses_sha256':c['statement_sha256'],'mathematical_statement_changed':False,'hypotheses_changed':False,'version_changed':False,'first_persistence_attempt':'ABORTED before claim/report writes on strict canonical-digest assertion; no mathematical rerun','reason':'Source uses statement-only hash; local protocol-compatible convention hashes compact sorted JSON of statement plus ordered hypotheses.'})
stamp=datetime.now(timezone.utc).isoformat();count=main['checks']+audit['checks']
c['review_records'].append({'reviewer':'A074','independent_reviewer':True,'verdict':'HOLDS_UNCHANGED_SCOPE','method':'Different complete enumeration:35 oriented edge-count profiles, all256 gates, actual full parent/child entropy via bitset characters. Coverage of all768 core/query pairs. Exact prime-power signs plus separate rational-log sign audit and literal direct-character witness. No source code imported or run.','evidence':['PROOF.md','out/FROZEN_SPEC.json','out/MAIN.json','out/main_COVERAGE.json','out/AUDIT.json'],'scope':'Entire finite maximum3log2(3)-4, arbitrary selected gate input/query coordinate by relabeling, positive and zero influence boundaries, and literal Boolean1/2-rate refutation; no arbitrary-dimensional upper bound.','source_claim_file_sha256':sha(S/'CLAIMS.json'),'source_statement_only_sha256':source_digest,'metadata_normalization':'Only statement_sha256 normalized to compact statement+ordered-hypotheses JSON convention; mathematical statement/hypotheses/version unchanged.'})
c['status']='INDEPENDENTLY_ACCEPTED_UNCHANGED_SCOPE'
c['proof_source']=[str(S/'CLAIMS.json'),str(S/'REVIEW.md'),str(S/'out/FULL_CERTIFICATE.json'),'PROOF.md','code/census.py','code/audit.py','out/MAIN.json','out/AUDIT.json']
write(R/'CLAIMS.json',[c])
write(R/'out/LEAN_ATTEMPT.json',{'command':'python -X utf8 lean_check.py --core --stmt example : (9 : Nat) > 8 := by decide','exit_code':1,'output':'RUNTIME_UNVERIFIED in122.4s','source_sha256':'ccd986add362d52a8b3dd22ca1d2e2ae592d17cabe06bbd4403ca96cec3d39cf','translation_fidelity':'UNVERIFIED','scope':'No Lean certification claimed; exact integer sign is independently checked in Python.'})
next_action='A075/A080/A084/A089: fund an INITIAL arbitrary OUTER/core bank on the correlated multi-output or paid-history interface from SAME unused original influence; A072/A092 inspect this independent finite acceptance. No coefficient<=1/2 shortcut or summary-only reset.'
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':R.name,'stream':'B15','packet_id':'A074','gap_id':'C019-INHERITED-SIGNED-CHILD-ELIGIBILITY','attempt_id':'A074-independent-exact-full-drift-maximum','method':'Consume A072 pending finite certificate through oriented-edge enumeration and independent full spectra, not producer signature replay','mathematical_delta':'A072-EXACT-THREE-BIT-FULL-DRIFT-MAXIMUM@1 independently accepted unchanged. Exact maximum3log2(3)-4 over complete stated domain; literal five-bit witness refutes universal1/2 full-drift rate. Initial-source payment/full FEI OPEN.','deliverable_status':'COMPLETE_LOCAL_ARTIFACT','mathematical_status':'FINITE_CERTIFICATE_INDEPENDENTLY_ACCEPTED; FULL_FEI_OPEN','claim_versions_used':['A072-EXACT-THREE-BIT-FULL-DRIFT-MAXIMUM@1','A075-WHOLE-ROW-SIGNED-COMPOSITION-DRIFT@1 exact cancellation, prior A074 acceptance'],'claims_created_or_changed':[{'claim_id':c['claim_id'],'version':1,'change':'independent acceptance only; exact statement, hypotheses and digest unchanged'}],'source_artifacts':['PROOF.md','out/INTAKE.json','out/SOURCE_PINS.json','out/FROZEN_SPEC.json','code/census.py','code/audit.py','out/MAIN.json','out/main_COVERAGE.json','out/AUDIT.json','out/LEAN_ATTEMPT.json'],'next_consumers':['A071','A072','A075','A080','A084','A089','A092','B15','B20'],'next_action':next_action,'stagnant_substantive_attempts':0,'blockers':['INITIAL arbitrary-core influence-priced original source is unpaid; finite maximum is not a universal upper bound.','Brain personal-context self-care degraded/unverified; no affected note used as mathematical evidence.','Guarded Lean attempt runtime unverified.','Supervisor mirror/downstream adoption unverified.'],'packet_ids':['A074']}
progress['claims_created_or_changed'][0]['change']='Independent mathematical acceptance only; statement/hypotheses/version unchanged; source statement-only hash normalized to local statement+ordered-hypotheses digest, with both retained in out/HASH_NORMALIZATION.json.'
write(R/'PROGRESS.json',progress);write(R/'PACKET_DELTA.json',progress)
report=f'''# exact target, quantifiers, hypotheses and units

A072-EXACT-THREE-BIT-FULL-DRIFT-MAXIMUM@1 HOLDS unchanged, digest {c['statement_sha256']}. For every3-input Boolean gate, every3-bit Boolean queried core and two fresh independent uniform dictators, the maximum of full signed correction drift divided by positive physical query influence is exactly3log2(3)-4. The queried core can occupy any gate slot and any of its coordinates can be queried. Constants/dummies and zero influence are checked separately. All entropy uses complete squared Fourier spectra in bits. This is an independently certified finite maximum and an actual Boolean refutation of universal drift rate1/2. Full FEI remains OPEN.

# sources actually read, revisions and theorem locators

Read current BOARD supervisor2026-10-27 15:26UTC, B15 leadv2, own STATUS and prior A074 result. The original B15 census direction is complete; dispatch consumes A072's new pending certificate explicitly addressed to A074/A092. Read source run20261027T083832Z A072 CLAIMS, REVIEW, FULL_CERTIFICATE and HALF_RATE_COUNTEREXAMPLE; the target is the second claim. A084 sharp scalar and A089 corrected-owner proof/claims were read for current scope and sign conventions; they are not newly accepted by this stage. The accepted A075 complete-row cancellation is reconstructed for the coverage reduction in PROOF.md. Protocol revision2026-10-11-execution-v2 and exact required schemas were reread. Historical campaign/paper intake remains background; no new literature premise is used. out/INTAKE.json and SOURCE_PINS.json preserve revisions and hashes; PRIOR_STATUS.md preserves the starting NEXT. No producer executable was imported or run.

Brain self-care remains degraded/unverified: the owner-model, state-of-mind and latest dream records are stale. This was disclosed at the first update; no affected personal-context note supports mathematics. Current compute intake reported statusok,9826MB available and3.6GB free; this is a snapshot, not a resource guarantee. No new heavy job, GPU, remote or detached work, process shedding, trading access, git, mail or research-brain write occurs. Research outputs stay inside A074. System-required checklist effects are separate. Stale/unmatched signed contracts are not used to authorize irreversible action.

# complete derivation or exact first unsupported line

PROOF.md derives the35-profile reduction from oriented edge counts(a,b,c,e) summing4: mu=(a-e)/4,t=(b-c)/4,d=(b+c)/4. The complete-row identity shows the drift depends only on these values and h. Physical/query and gate-slot relabeling are explicit; both signs and all35 profiles remain. All768 literal core/query pairs map onto these profiles. Thus8960 actual representative circuits cover589824 literal gate/core/query/slot rows before reduction. Each representative is an actual Boolean function, with explicit full parent and both complete child truth tables.

Every gap[3log2(3)-4]*Inf-drift is an exact prime-log form. All are nonnegative by integer-product certificates;128 positive-influence representatives give exact equality. The independent artifact audit verifies40 distinct gap forms by directed rational logarithm bounds, all8960 distinct keys and3 deliberately forged drifts. This establishes the finite upper bound and its attainment without floating signs. It uses no universal entropy or sharp scalar premise.

The literal source witness hmask7 in slot2,gmask3,corequery1 gives physical truthmask16579836 with dummy bit0. Its direct-character Walsh vector equals every source integer. Parent H=6-(27/16)log2(3), inner H=2, q=3/4, child H values4-(9/8)log2(3) and2, inner child H=0,0. Therefore drift=(9/8)log2(3)-3/2, influence3/8, ratio3log2(3)-4>1/2 (strict sign reduces to9>8). This witness has bounded H/I; it is not an FEI disproof. First unsupported universal line: INITIAL arbitrary-core bank or rho_K payment from SAME unused original O(I) source, including old debits and both full terminals.

# executed validation with domain, arithmetic, commands and outputs

Frozen helper A074-oriented-edge-histogram-v1 precedes the pilot and main. A pilot-output chunk omission was fixed before ANY pilot calculation; the earlier freeze is preserved and the active helper hash was refrozen. No mathematical failure or rerun is hidden. Fixed domain all35 oriented profiles x all256 gates=8960; no automatic dimension increase. Pilot560 circuits passed{pilot['checks']} checks in{pilot['elapsed_seconds']:.3f}s. Main8960 circuits (7200 positive,1760 zero physical influence) passed{main['checks']} checks in{main['elapsed_seconds']:.3f}s. It finds128 equality representatives. The audit gives6912 equality rows after restoring literal core/query multiplicities and all three selected slots; this is a different count convention from the producer's192 signature rows.

Every full spectrum uses negative-set bitset characters and integer inverse/Parseval checks; direct physical edges match spectral influence. Complete actual parent and child entropies compute correction drift directly. Fractions/prime-log forms establish identities and LCM-cleared integer powers certify signs. Sixteen560-row main chunks are saved immediately. The separate rational-log auditor uses48 positive-atanh terms with a proved geometric remainder after dyadic reduction; zeros are symbolic and ambiguous strict signs would abort. All40 distinct gap profiles pass. Source witness uses literal direct character summation instead of bitset spectra. Audit{audit['checks']} checks pass in{audit['seconds']:.3f}s. Total nonpilot exact checks={count}; pilot is excluded.

Commands: python -X utf8 code/census.py freeze; census.py pilot; census.py main; code/audit.py; code/persist.py, from the run with appropriate paths. Frozen pilot cap55s/main180s, estimated memory120MB, peak unmeasured. No expected>300MB job, hence no memok admission required. Arithmetic signs are exact throughout. A guarded core Lean attempt for the elementary9>8 sign returned exit1,RUNTIME_UNVERIFIED in122.4s, with translation fidelity unverified; out/LEAN_ATTEMPT.json records it. The achieved rung is an independent exact finite certificate with analytic coverage proof, not Lean certification or all-dimensional FEI.

# proof dependencies and changed downstream conclusions

Elementary character orthogonality, physical edge counting, complete Fourier restriction algebra and the35-profile coverage argument suffice. A075's previously accepted whole-row identity is rederived; the source's A084 dependency is needed only for that identity, not its sharp continuum constant. Exact statement, hypotheses, version and contributors are unchanged. The source digest{source_digest} hashes the statement only; the local digest{c['statement_sha256']} hashes compact sorted JSON of statement plus ordered hypotheses. out/HASH_NORMALIZATION.json preserves both conventions and the initial persistence assertion failure. Only local hash metadata is normalized; no mathematical calculation was rerun and no peer file was changed. CLAIMS.json adds A074's independent HOLDS_UNCHANGED_SCOPE review. No mathematical repair or new broad candidate is introduced. Any universal full-drift coefficient must now independently satisfy kappa>=3log2(3)-4;1/2 is unavailable. No universal upper bound sharper than the existing supplied-bank theory, no INITIAL influence price and no new FEI constant are asserted.

# one next mathematical action and independent reviewer

{next_action}

# actual persistence receipts or precise save blocker

The four protocol files, complete PROOF, source/freeze receipts, coverage, pilot/main chunks, exact audit and reproducible code are saved locally. PERSISTENCE checks exact schema fields, unchanged claim digest, critical immutable source hashes, PROGRESS/PACKET_DELTA byte identity, all file sizes/hashes and rolling files. STATUS has two lines; WORKLOG and LEARNED append dated results. Each file stays below20MB. Supervisor copying, remote mirrors and downstream use remain unverified. Checklist closure for T-20261027-088 and the prior completed T-20261027-005 is attempted only after local persistence; out/CHECKLIST_CLOSURE.json records actual success or failure. No shared-lock surgery is authorized.

# Universal bridge

C019 stopping-tree payment advances by independent exact acceptance of the finite full-drift maximum3log2(3)-4 and its literal Boolean1/2-rate counterexample, closing A072's pending certificate through a different complete enumeration and full-spectrum implementation. This places a rigorous lower constraint on any pointwise local reserve shortcut while preserving the distinction from A084's exceptional-row upper price. INITIAL arbitrary-core source payment remains completely unpaid; the next step is an original-owner paid-history or correlated multi-output supplier, retaining all old labels and full siblings. That targets the precise full-FEI bottleneck rather than escalating another finite search or treating the certified local maximum as a universal upper bound.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8')
(A/'STATUS.md').write_text('STATE: A074 stage saved: A072 exact3-bit full-drift max3log2(3)-4 independently HOLDS;8960 representative circuits/128 equalities;literal1/2-rate counterexample;FEI OPEN.\nNEXT: A075/A080/A084/A089 fund INITIAL arbitrary OUTER/core bank from SAME unused influence on paid-history/correlated multi-output interface;A072/A092 audit finite acceptance.\n',encoding='utf-8')
if R.name not in (A/'WORKLOG.md').read_text(encoding='utf-8'):
 with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(f'\n## {stamp}: {R.name}\nIndependent unchanged acceptance of A072-EXACT-THREE-BIT-FULL-DRIFT-MAXIMUM@1. Different35 oriented-edge profile enumeration,8960 representatives,7200 positive/1760 zero,128 exact equality representatives; main{main["checks"]}+audit{audit["checks"]}={count} nonpilot checks. Literal5bit mask16579836 reconstructed by direct characters;ratio3log2(3)-4>1/2. Full FEI/INITIAL original source remain open; Lean runtime unverified. No source executable run, no git/brain research write.\n')
if R.name not in (A/'LEARNED.md').read_text(encoding='utf-8'):
 with (A/'LEARNED.md').open('a',encoding='utf-8') as f:f.write(f'\n## {stamp}: {R.name}\nThe finite complete-drift maximum for3bit outer/queried core plus2fresh dictators is exactly3log2(3)-4, independently accepted A072@1 digest{c["statement_sha256"]}. All3bit core queries reduce to35 ordered (++,+-,-+,--) count profiles summing4, not merely a floating bias grid:mu=(a-e)/4,t=(b-c)/4,d=(b+c)/4; the full-row identity proves arrangement invariance. Enumerate35x256 actual full spectra for exact finite coverage.128 representative equality rows restore to6912 literal rows with all slots; producer192 signatures are another count convention. Source truthmask16579836 has drift9log2(3)/8-3/2 andInf3/8, excluding universal1/2 full-drift rate. No all-dimensional upper bound or FEI counterfamily follows. NEXT must pay INITIAL arbitrary outer/core original source, not rerun this closed census.\n')
protocol=read(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'))['required_per_run']
assert set(c)==set(protocol['claim_fields']) and digest(c)==c['statement_sha256']
assert set(progress)=={f.split(' (')[0] for f in protocol['progress_fields']}
assert all('# '+field in report for field in protocol['report_fields'])
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
for pin in read(R/'out/SOURCE_PINS.json'):
 if str(S) in pin['path']:assert sha(Path(pin['path']))==pin['sha256']
receipt={'status':'PASS','saved_at':stamp,'claim_digest':'CANONICAL_NORMALIZED_MATHEMATICS_UNCHANGED','protocol_fields':'PASS','critical_sources':'PASS','progress_delta_identity':True,'nonpilot_checks':count,'full_fei':'OPEN','mirror':'UNVERIFIED','files':[],'rolling_files':[]}
for p in sorted(R.rglob('*')):
 if p.is_file() and p.name!='PERSISTENCE.json':
  assert p.stat().st_size<20*1024*1024
  receipt['files'].append({'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)})
for n in ('STATUS.md','WORKLOG.md','LEARNED.md'):receipt['rolling_files'].append({'path':n,'sha256':sha(A/n)})
write(R/'out/PERSISTENCE.json',receipt)
assert all(sha(R/x['path'])==x['sha256'] for x in receipt['files'])
print(json.dumps({'status':'PASS','files':len(receipt['files']),'nonpilot_checks':count,'review':'HOLDS_UNCHANGED','full_fei':'OPEN'}))
