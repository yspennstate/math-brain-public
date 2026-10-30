from pathlib import Path
import json, hashlib, datetime
R=Path(__file__).resolve().parents[1]; HOME=R.parents[1]
incoming=Path(r'agents\A039\runs\20261026T214918Z-fleet04-A039-projection-under-restrictions')
protocol=Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
check=read(R/'out/CHECK.json'); assert check['status']=='PASS'
pilot=read(R/'out/PILOT.json'); assert pilot['status']=='PASS'
claim=read(incoming/'CLAIMS.json')[0]
assert hashlib.sha256(claim['exact_statement'].encode('utf-8')).hexdigest()==claim['statement_sha256']
original_sha=claim['statement_sha256']
review={'reviewer':'A036','verdict':'HOLDS_AT_STATED_SCOPE','statement_sha256':original_sha,'independent_of_producer_code':True,'evidence':['PROOF.md','out/CHECK.json','out/PILOT.json'],'scope':'Independent reconstruction of A039 moving-anchor extension, full-terminal algebra, majority upper-bank obstruction. Concrete original-source assumptions remain explicit A036 stage21 dependencies; this is not an independent acceptance of A036 own source proof or full FEI. No substantive repair to A039 statement.','known_harness_failure':'PILOT_ATTEMPT1.json: rational envelope is equality, strictness comes from ell<4/15.','checks':check}
write(R/'out/REVIEW.json',review)
claim['review_records'].append({'reviewer':'A036','status':'INDEPENDENT_RECONSTRUCTION_HOLDS_AT_STATED_SCOPE','proof':'PROOF.md','evidence':'out/REVIEW.json','source_application_scope':'Original source inequalities remain A036 dependency, not independent acceptance of own work.'})
claim['status']='INDEPENDENT_RECONSTRUCTION_HOLDS_SOURCE_APPLICATION_CONDITIONAL'
write(R/'CLAIMS.json',[claim])
sources=[protocol,incoming/'PROOF.md',incoming/'REPORT.md',incoming/'CLAIMS.json',HOME/'LEARNED.md',Path(r'BOARD.md'),Path(r'claude\B08\STREAM_NOTES.md')]
base=protocol.parent
sources += [base/n for n in ['README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json']]+list(base.glob('*.tex'))
supp=Path(r'math-open-problems/research_pushes\2026-10-11-full-fei-100-agents')
sources += [supp/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]+list((supp/'sources').glob('*.md'))
sources += list(Path(r'context').glob('*.txt'))
sources += list((HOME/'runs/20261023T135330Z-fleet03-A036-reference-law-divergence').glob('PROOF.md'))
manifest=[]
for p in sources:
 if not p.exists():continue
 b=p.read_bytes()
 try:s=b.decode('utf-8-sig');enc='utf-8-sig'
 except UnicodeDecodeError:s=b.decode('cp1252');enc='cp1252 (PDF extracted original bytes)'
 manifest.append({'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'encoding':enc,'lines_read':len(s.splitlines())})
write(R/'out/SOURCES.json',manifest)
lean=read(R/'out/LEAN_STATUS.json') if (R/'out/LEAN_STATUS.json').exists() else {'status':'UNVERIFIED','reason':'attempt has not returned; do not infer proof'}
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':R.name,'stream':'B08','packet_id':'A036','gap_id':'G-ORIGINAL-ARBITRARY-CORE-SOURCE','attempt_id':'A036-stage22-review-A039-moving-anchor','method':'Independent analytic reconstruction; exact rational physical channels, prime-log telescopes and bounded finite exhaustive verification.','mathematical_delta':'A039 moving-anchor absorption independently HOLDS unchanged at stated scope. All singleton-anchor physical queries paid by same original bank; supplied-source full-terminal recovery >53/32 after oldquarter. Majority obstruction applies only to n*a upper bank. Initial arbitrary-core source remains unpaid.','deliverable_status':'COMPLETE_LOCAL','mathematical_status':'SCOPED_REVIEW_HOLDS_FULL_FEI_OPEN','claim_versions_used':['A039-MOVING-ANCHOR-ABSORPTION@1','A036-CHARACTER-ANCHORED-NORMALIZED-DIVERGENCE-BANK@1 original source only'],'claims_created_or_changed':['A039-MOVING-ANCHOR-ABSORPTION@1: independent review record only; statement unchanged'],'source_artifacts':['PROOF.md','out/SOURCES.json','out/REVIEW.json','out/CHECK.json','out/PILOT.json','out/LEAN_STATUS.json'],'next_consumers':['A039','A048','A050','A088','A094'],'next_action':'Price one useful arbitrary-core ORIGINAL reference/decomposition and full terminal entropy from SAME unused O(I) capacity; sharper actual selected-policy price, not majority-divergent n*a upper bank or a free new anchor.','stagnant_substantive_attempts':0,'blockers':['Universal arbitrary-core initial source and full terminal payment unpaid','Independent review of original A036 source chain remains separate','Supervisor mirror/adoption unverified'],'packet_ids':['A036']}
write(R/'PROGRESS.json',progress);write(R/'PACKET_DELTA.json',progress)
stats=check['stats']
report=f'''# A036 stage22: moving-anchor extension independently holds

## exact target, quantifiers, hypotheses and units

Review A039-MOVING-ANCHOR-ABSORPTION@1 for every actual finite uniform Boolean cube, every nonempty initial character J, every alpha in(0,1), and every finite adaptive physical restriction tree with arbitrary stopping. Project the original anchor only; reset both children after each query; after absorption use exact spectra while retaining full entropy. All units are bits. Target is normalized divergence payment with a separate recovery implication. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

Current BOARD2026-10-27 03:41UTC, B08 lead notesv2, own STATUS/LEARNED and stage21 REPORT/PROOF, A03920261026T214918Z REPORT/PROOF sections1-6 and CLAIMS read. Incoming statement SHA256 {original_sha}. Protocol2026-10-11-execution-v2 read in full. Current campaign registries, plan, supplement and sources consulted for route scope; four manuscript text versions read in explicit cp1252 where UTF8 decoding fails. No manuscript theorem is assumed in the proof. Source bytes/encodings pinned in out/SOURCES.json. Earlier detailed corpus is inherited from21 stages, not re-certified. One batched math-recall query found no direct new moving-anchor premise; unrelated hits were excluded. Explicit current continuation governs the old campaign end date. Brain wake reports stale personal-context/dream notes; none is a mathematical premise.

## complete derivation or exact first unsupported line

PROOF.md independently reconstructs complete q, erased-spectrum coherent channel, r_y>=beta/2, fair ghost fallback, actual signed resets and the decreasing B=(n-1)(1-p(J)) bank. Inside-anchor restriction is checked separately; the last-anchor reset is nonpositive and subsequent exact resets cost zero. The actual ledger keeps sum erasure/queryKL + sum outcomeKL + E full terminalKL equal to initialKL+signed conversions. This avoids the board's query-KL omission.

Finite Jensen/one-atom partition separately bounds terminal entropy even after the anchor is empty. On A036's unchanged original supplied mod3 source, the inclusive divergence cost is <1/64, full terminal surplus >61/32, and SAME-owner signed recovery after the retained oldquarter is >53/32. The protected >673/256 bound is not reused: absorption removes its terminal influence lower bound. The changed constant is a changed policy scope, not numerical drift. No free anchor replacement occurs. Majority independently refutes only universal pricing of this n*a upper bound; actual selected-policy cost is not refuted. Collision T=L/Z=H(v/Z)-log2Z is preserved and raw-L payment remains retired.

FIRST UNSUPPORTED UNIVERSAL LINE: a useful arbitrary-core ORIGINAL reference/decomposition whose complete source and terminal bills are paid by O(I) unused original capacity. This review does not resolve it. Proof rung: analytic proof independently reconstructed at the stated scope; formal entropy/KL proof is not claimed.

## executed validation with domain, arithmetic, commands and outputs

Frozen out/FROZEN_SPEC.json precedes the pilot and records a main-runtime amendment before the main job. Pilot:272 local queries and216 tree roots,14131 assertions PASS,3.607s. Main:ALL Boolean functions n1..3, ALL anchors including empty, ALL physical coordinates, alpha1/6 and1/2; {stats['queries']} local queries, {stats['inside']} inside-anchor cases, {stats['absorption']} absorption cases, {stats['ghost_rows']} ghost-row occurrences; {stats['trees']} complete/stopped adaptive tree roots; {check['checks']} exact assertions PASS in {check['seconds']:.3f}s. No symmetry reductions or floating sign tests. Literal Walsh sums and exact Fraction normalizers are independent of A039's implementation; prime-valuation log words cancel the full ledger exactly; outward rational atanh intervals certify signs. Only own previous interval arithmetic is imported. Commands: python -X utf8 -B code/check.py --pilot; python -X utf8 -B code/check.py.

The first pilot failed an overly strict harness envelope: (6*10/1024)*(4/15) EQUALS1/64. out/PILOT_ATTEMPT1.json preserves this; strictness follows from the independently checked integer inequality6^15<16*5^15. The source proof is unchanged. Main memory estimate120MB, arithmetic runtime cap240s, no GPU, no automatic dimension escalation, no >300MB arithmetic job. Fresh memok returned0 before the separate scalar Lean attempt. Actual formal-check outcome: {json.dumps(lean,ensure_ascii=False)}. A scalar pass alone would not certify the entropy theorem.

## proof dependencies and changed downstream conclusions

A039 statement, hypotheses and contributor remain unchanged; CLAIMS.json adds only A036's scoped independent review. A036 is not an independent reviewer of its own original supplier proof; that concrete application retains the explicit stage21 dependency. New anchor-release proof supplies exactly the requested stage21 missing query, without introducing a new broad candidate. Universal constant improves by zero. The majority guard excludes the crude initial upper-bank route, not FEI or useful alternative suppliers.

## one next mathematical action and independent reviewer

A039/A048/A050 should price an actual useful arbitrary-core ORIGINAL source or selected policy with full terminals, retaining all old bills and accumulated queryKL. No more optional anchor/reset histories of the supplied family are needed. A088/A094 independently review the complete source chain; this stage's acceptance covers the extension and conditional recovery algebra only. This is the shortest route because normalized transport including anchor absorption is now source-complete and independently reconstructed.

## actual persistence receipts or precise save blocker

All four protocol artifacts, proof, independent code, frozen spec, source manifest, preserved failed pilot and PASS outputs are inside A036. Rolling STATUS has exactly two lines; WORKLOG and LEARNED record the stage. code/finalize.py rereads exact protocol field sets, incoming unchanged statement hash, complete result receipts, packet-delta equality, report headings and20MB cap, then writes out/PERSISTENCE.json with hashes. No git, messages, brain write, remote publication or other-agent edit. Supervisor mirror/adoption is unverified. Current computational receipts support artifact completion only, not a claim that FEI is solved.

Universal bridge: C019 stopping-tree payment and C024 history transfer move by independently accepting A039's closure of the singleton-anchor-query gap: ALL physical queries use the SAME decreasing initial bank, including the last anchor query, while full terminal entropy and old debits remain. The supplied original source retains >53/32 after the oldquarter under this broader policy; the protected bound was larger because it retained nonempty terminal influence. The universal FEI constant improves by zero. The exact unpaid step is useful arbitrary-core initial source/terminal payment from O(I) unused original capacity. Pricing that source or a genuinely sharper necessary selected policy is the shortest NEXT; another supplied-family reset history would not address it.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8',newline='\n')
state='STATE: A036 stage22 COMPLETE_LOCAL: A039 moving-anchor absorption independently HOLDS unchanged; ALL physical queries SAME original bank; supplied-source recovery>53/32 after oldquarter; exact checks PASS; FEI OPEN.\nNEXT: A039/A048/A050 price useful arbitrary-core ORIGINAL source/selected policy and full terminals from SAME unused O(I); majority-divergent n*a upper bank is not payment; A088/A094 full-chain review.\n'
(HOME/'STATUS.md').write_text(state,encoding='utf-8',newline='\n')
lesson='\n2026-10-27 stage22: A039-MOVING-ANCHOR-ABSORPTION@1 independently HOLDS unchanged. Project J through ALL physical queries; use q=p after absorption and keep entropy. B=(n-1)(1-pJ) pays signed resets; inclusive KL<=ell*n*(1-pJ), with all query/outcome/full-terminal KL explicit. Singleton needs no extra original bank; larger J adds (|J|-1)*a over protected bank. SAME supplied-source recovery>53/32 after oldquarter replaces protected>673/256 because terminal nonempty influence is lost. Majority makes n*(1-pJ)/I unbounded, only for this crude upper price. Exact envelope at N10 is1/64; strictness is ell<4/15. Original arbitrary-core useful source and complete terminal payment remain OPEN.\n'
with (HOME/'LEARNED.md').open('a',encoding='utf-8',newline='\n') as f:f.write(lesson)
with (HOME/'WORKLOG.md').open('a',encoding='utf-8',newline='\n') as f:f.write('\n2026-10-27 stage22: Read live dependencies; independently reconstructed A039 release, ghost/normalizer/queryKL/full-terminal ledger and majority guard. Pilot strict-envelope harness repaired with failed receipt preserved. Main exact finite checks PASS. Scoped review saved; original-source universal price remains unpaid. No research jobs detached or other workloads stopped.\n')
proto=read(protocol)['required_per_run'];assert set(claim)==set(proto['claim_fields'])
assert set(progress)=={s.split(' (')[0] for s in proto['progress_fields']}
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert len((HOME/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
assert all(('## '+h) in report for h in proto['report_fields'])
assert claim['exact_statement']==read(incoming/'CLAIMS.json')[0]['exact_statement']
assert claim['hypotheses']==read(incoming/'CLAIMS.json')[0]['hypotheses']
assert claim['contributors']==read(incoming/'CLAIMS.json')[0]['contributors']
files=[p for p in R.rglob('*') if p.is_file()]
assert all(p.stat().st_size<20*1024**2 for p in files)
write(R/'out/PERSISTENCE.json',{'status':'PASS','protocol_field_sets':'exact','source_statement':'unchanged','packet_delta':'byte_identical','files':[{'path':str(p.relative_to(R)),'sha256':sha(p),'bytes':p.stat().st_size} for p in files]})
print(json.dumps({'status':'PASS','files':len(files),'assertions':check['checks'],'queries':stats['queries'],'trees':stats['trees'],'review':'HOLDS_AT_STATED_SCOPE','full_FEI':'OPEN'}))
