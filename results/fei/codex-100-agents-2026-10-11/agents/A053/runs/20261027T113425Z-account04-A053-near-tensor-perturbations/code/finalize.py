from pathlib import Path
import json,hashlib,datetime,subprocess
R=Path(__file__).resolve().parents[1];A=R.parents[1]
def load(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def save(p,o):p.write_text(json.dumps(o,indent=2)+'\n',encoding='utf-8',newline='\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
protocol=load(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'))
main=load(R/'out/CHECKS.json');replay=load(R/'out/INDEPENDENT.json');guards=load(R/'out/GUARDS.json')
assert main['status']==replay['status']==guards['status']=='PASS'
total=main['checks']+replay['checks']+guards['checks']
save(R/'out/MEMOK.json',dict(exit_code=1,stdout='WAIT: physical free 4.0 GB (need 4.0), commit free 2.9 GB (need 8.0)',
 note='Executed before contemplated core Lean job; no compiler started; previous earlier compute snapshot had more headroom, this is a later probe.'))
save(R/'out/LEAN_STATUS.json',dict(status='HELD_NO_COMPILER',reason='memok exit1',target='paired_error_cancel',
 source_sha256=sha(R/'code/PairedError.lean'),rung='Uncompiled source only; not Lean checked'))
sources=[Path('BOARD.md'),Path('claude/B11/STREAM_NOTES.md'),
 A/'runs/20261026T193442Z-account04-A053-near-tensor-perturbations/PROOF.md',
 Path('agents/A055/runs/20261027T011322Z-account04-A055-extremal-obstruction-referee/PROOF.md'),
 Path('agents/A055/runs/20261027T011322Z-account04-A055-extremal-obstruction-referee/REPORT.md'),
 Path('agents/A054/runs/20261026T222013Z-account04-A054-connectedness-alternatives/PROOF.md'),
 Path('agents/A054/runs/20261026T222013Z-account04-A054-connectedness-alternatives/REPORT.md'),
 Path('agents/A052/runs/20261027T075723Z-account04-A052-critical-source-structure/REPORT.md'),
 Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')]
save(R/'out/SOURCE_RECEIPTS.json',dict(note='Observed local bytes; prior complete campaign/manuscript baseline reads retained, no new full audit.',
 files=[dict(path=str(p),sha256=sha(p),bytes=p.stat().st_size) for p in sources]))
statement='Retain stage21 exact repair-density exclusion. Further, let F be a product of disjoint violating Boolean factors h_j, G differ from F on event E of uniform mass delta, and a finite adaptive physical query tree have hereditarily K-certified complete leaves (or the explicitly stated untouched-factor fibre eligibility). Let rho_j>0 be h_j distance to H<=KI, alpha_j its minimum directional influence, p_j probability the tree touches its block, e_j=Pr(E and touch_j), and Q_j actual original-reach first-query influence in that block. Then delta-e_j>=rho_j(1-p_j), Q_j>=alpha_j*p_j-2e_j, and total physical spent influence is at least sum_j max(0,alpha_j-max(alpha_j/rho_j,2)*delta). No error independence or single total occupation budget is assumed. For t two-bit point-defect cores at K1 this is t max(0,1/2-2delta); for three-bit point-defect cores at K2 it is t max(0,1/4-2delta). The unedited h2 boundary t/2 is attained. Ordinary certified leaves do not suffice, as z*h2 at K1 shows. This is a necessary original influence debit, not entropy payment or full FEI.'
claim=dict(claim_id='A053-TENSOR-CRITICAL-REPAIR-DENSITY',version=2,exact_statement=statement,
 hypotheses=['Uniform Boolean signs and physical coordinate-product comparison seed; entropy bits; K>=0',
 'Each selected core strictly violates K, hence rho_j>0; alpha_j may be0 with no positive debit conclusion',
 'Finite adaptive physical tree; no intermediate affine mixing or phase multiplication; no repeated queries on a path',
 'Full actual leaves retained, hereditary K-certification or precisely stated untouched-factor fibre eligibility; ordinary/averaged leaf eligibility alone insufficient'],
 statement_sha256=hashlib.sha256(statement.encode()).hexdigest(),contributors=['A053'],proof_source='PROOF.md Sections1--2; out/CHECKS.json, out/INDEPENDENT.json, out/GUARDS.json',
 proof_dependencies=['Stage21 disjoint-fibre repair count, directly reconstructed in Section1','Disjoint first-query physical cylinders and exact two-endpoint error charge','Physical influence telescope; elementary point-defect spectra'],
 review_records=[dict(reviewer='A053',kind='author analytic derivation, two separate exact finite implementations and counterguards',outcome=f'{total} exact assertions PASS; independent-agent review pending; Lean held before compiler')],
 status='AUTHOR_PROOF_EXACT_VALIDATION_PENDING_INDEPENDENT_REVIEW',supersedes=['A053-TENSOR-CRITICAL-REPAIR-DENSITY@1 (retained valid density result, extended with physical debit)'],refutes=[],
 first_unproved_line='No gap claimed in scoped debit theorem. One ORIGINAL high-K block paid from genuine nonnegative full-child reserve and unused quotient rank, with Pi/old debit retained, remains unpaid.',
 next_consumers=['A051','A052','A054','A055','A090','A094','B11','B20'])
assert set(claim)==set(protocol['required_per_run']['claim_fields']);save(R/'CLAIMS.json',[claim])
progress=dict(protocol_revision=protocol['revision'],run_id=R.name,stream='B11',packet_id='A053',gap_id='G-R-SELECT',attempt_id='A053-stage22-robust-first-query-debit',
 method='Combine disjoint no-touch repair with actual first-query pivotal errors in SAME event partition; full input-path replay; independent A055 analytic review',
 mathematical_delta='Robust necessary ORIGINAL physical influence debit for hereditary-certified near-tensor cleanup; paired error slope2 for point defects. A055 Sections1--3 tensor/occupation independently HOLD at stated scope. No universal constant gain.',
 deliverable_status='COMPLETE_LOCAL',mathematical_status='SCOPED_AUTHOR_PROOF; A055_SCOPED_ANALYTIC_REVIEW_HOLDS; FULL_FEI_OPEN',
 claim_versions_used=['A053-TENSOR-CRITICAL-REPAIR-DENSITY@1 (fibre count reconstructed)','A055 20261027T011322Z PROOF Sections1--3 (reviewed, not premise of new theorem)'],
 claims_created_or_changed=['A053-TENSOR-CRITICAL-REPAIR-DENSITY@2'],source_artifacts=['PROOF.md','out/SOURCE_RECEIPTS.json','out/CHECKS.json','out/INDEPENDENT.json','out/GUARDS.json','out/LEAN_STATUS.json'],
 next_consumers=['A051','A052','A054','A055','A090','A094','B11','B20'],
 next_action='Supply ONE high-K ORIGINAL-block entropy payment beyond near-tensor exclusions using exact nonnegative complete-child reserve and unused quotient rank; retain phase Pi, old debits and actual error occupation.',
 stagnant_substantive_attempts=0,blockers=['Universal entropy-payment supplier remains open','New theorem independent-agent review and shared adoption pending','Lean held by memok exit1; no compiler started'],packet_ids=['A053'])
assert set(progress)=={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
save(R/'PROGRESS.json',progress);(R/'PACKET_DELTA.json').write_bytes((R/'PROGRESS.json').read_bytes())
report=f'''# A053 stage22: robust first-query influence debit

## exact target, quantifiers, hypotheses and units

Every Boolean coordinate product F with selected strictly K-violating factors, every edit G of original density delta, every finite adaptive physical stopping tree whose complete actual leaves and all further physical restrictions are K-certified. Entropy bits; original physical influence. No intermediate affine mixing/phase changes. Quantify a NECESSARY spent-influence debit, retaining actual error occupation. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

Current BOARD, B11 lead notes v2, own STATUS/LEARNED and stage21 proof read first. New complete inputs: A055 20261027T011322Z REPORT and PROOF Sections1--3; A054 20261026T222013Z REPORT/PROOF Sections1--5; A052 20261027T075723Z REPORT. The unchanged old lead one-point assignment was closed in earlier stages; dispatch consumes these new complete-child objections. Protocol2026-10-11-execution-v2 field sets refreshed; previous complete campaign/registry/supplement/four-manuscript baseline reads retained, not represented as fresh full audits. out/SOURCE_RECEIPTS pins observed bytes. No outside novelty or recalled theorem premise.

Brain self-care degraded/unverified: stale owner model194h, state178.5h and dream50.9h disclosed before reliance. Personal context and consolidation reliability remain affected; none is mathematical evidence. Latest explicit continuation governs old campaign endpoints without extending schedules. Only A053 research files changed.

## complete derivation or exact first unsupported line

PROOF Sections1--2 contains the derivation. For factor j, let p_j be the probability of ever touching it and e_j the ORIGINAL joint error/touch probability. Untouched hereditary terminals require delta-e_j>=rho_j(1-p_j). The disjoint FIRST-query cylinders preserve any queried coordinate flip inside that factor. Their two endpoint error sums equal2e_j exactly, so actual first-query debit Q_j>=alpha_j p_j-2e_j. Combining on the SAME partition gives Q_j>=alpha_j-max(alpha_j/rho_j,2)delta, clipped at0; summing Q_j costs actual original spent influence. No independence, no false sum e_j<=delta, no new reference or bank. For h2,K1 the debit is t max(0,1/2-2delta); h3,K2 gives t max(0,1/4-2delta). This paired coefficient2 replaces the weaker separate-error estimate, not the previous repair radii.

The unedited h2 boundary is sharp: one fixed physical bit in each factor leaves only characters/constants and spends exactly t/2. Ordinary certification is insufficient: z*h2 has H2,I2 at K1 and a zero-query certified leaf with untouched violating descendant h2. Thus the theorem is stronger in terminal hypotheses than A055 averaged optimized eligibility and must not be substituted there without proof.

PROOF Section3 independently reconstructs A055 exact full affine/character tensor additivity, pathwise optimized deficit lower bound, original-reach occupation averaging and finite-activation scaling. These Sections1--3 HOLD unchanged at analytic scope, excluding the separate NAND32 seed certificate/giant numerical embedding. New finite greedy-basis checks support that scoped review.

FIRST UNSUPPORTED UNIVERSAL LINE: pay one ORIGINAL high-K proper block from the genuine exact nonnegative full-child reserve and unused quotient rank, including phase Pi, mixed rows and old debits. A necessary debit lower bound does not pay entropy. The residual n>>K critical source class remains open.

## executed validation with domain, arithmetic, commands and outputs

Frozen out/SPEC.json precedes python -B -X utf8 code/check_tree.py. All137 n4 Boolean edits of h2 tensor h2 with0,1,2 changed vertices; ALL65 adaptive depth<=2 physical policies including early stopping:8905 cases,720 hereditary-eligible and8185 noneligible, including520 adaptive eligible. PASS {main['checks']} exact assertions in{main['wall_seconds']:.6f}s. Node-cylinder physical edges, integer Walsh, exact integer-product entropy signs and Fraction probabilities verify full leaves, endpoint errors, no-touch repair, actual original debit, sharp boundary and missing-heredity guard.

Frozen out/SPEC_INDEPENDENT.json precedes code/independent.py: ALL17 zero/single-edit roots times65 policies, complete full-input path integration; direct character sums and complete subcube enumeration for leaf eligibility. ALL256 ordered two-bit factor pairs independently verify centered directional domination and greedy affine basis minima. PASS {replay['checks']} assertions in{replay['wall_seconds']:.6f}s. This is a separate A053 implementation, not independent-agent acceptance. code/guards.py freezes its two fixed controls before checking e_j=delta versus false delta*p_j, and sum_j e_j>delta. PASS5 further exact checks.

NEW stage total {total}; prior stage85237 is a different finite domain and predicate set, not a changed result. No float sign decisions, GPU, dimension escalation or detached worker. Primary/independent expected80/70MB, observed peak unmeasured; each actual job under55s. Core Lean scalar paired_error_cancel is saved but UNCOMPILED: memok exited1 (commit2.9GB below8GB floor), so no compiler was started. Earlier compute snapshot had more headroom; the later admission probe governs. No Lean certification or mathematical refutation follows from this hold.

## proof dependencies and changed downstream conclusions

Version2 narrowly extends the existing A053 repair-density candidate with necessary original physical query debit. Stage21 density theorem and all earlier Fourier-code bounds remain unchanged. The new proof directly reconstructs disjoint fibre repair and uses no unaccepted source theorem. A055 tensor/occupation review is independent and has no proof cycle with the new statement. Universal constant improvement0; no registered claim refuted. Full hereditary terminal scope cannot be replaced by averaged signed reserve eligibility.

## one next mathematical action and independent reviewer

A051/A052/A054/A055 supply one ORIGINAL high-K entropy payment from exact nonnegative complete-child reserve and unused quotient rank, retaining Pi and old debits. Any near-tensor continuation must account for the actual joint error occupation and show its terminal fibre eligibility. A090/A094 independently review the first-query event measurability, two endpoint charge and sharp boundary; A055 reviews the precise stronger terminal hypothesis. No message sent.

## actual persistence receipts or precise save blocker

Four exact-schema protocol files, complete proof, frozen specs, both implementations, guards, Lean source/hold receipt and outputs saved only in this A053 run. Finalizer verifies exact field sets, statement hashes, required report headings, byte-identical PROGRESS/PACKET_DELTA,20MB cap and two-line STATUS; hashes and reopens all research artifacts and rolling files. Independent acceptance, registry adoption, supervisor copies, brain ingestion and remote mirrors remain unverified. Checklist closure receipt recorded separately. No git, mail, deletion, trading access, brain-content write or other-agent research mutation. All mathematical jobs finished; existing work untouched.

## Universal bridge

C019 stopping-tree payment gains a robust necessary ORIGINAL physical influence debit for hereditary-certified near-tensor cleanup, with exact paired-error accounting and a sharp unedited point-defect boundary. A055 tensor/occupation receives scoped independent analytic acceptance. Universal constant gain is zero: the debit lower bound neither pays entropy nor selects a block on the residual n>>K genuine critical class. NEXT asks for that single original high-K invoice with exact full-child reserve, unused quotient rank, Pi and old debits, which targets the missing universal supplier rather than another automatic primitivity or phase test.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8',newline='\n')
(A/'STATUS.md').write_text(f'STATE: Stage22 saved: robust near-tensor ORIGINAL first-query influence debit;paired error slope2;A055 tensor/occupation Sections1--3 scoped HOLD;{total} exact checks PASS;FEI OPEN.\nNEXT: Fund ONE ORIGINAL high-K entropy invoice on residual n>>K critical class using exact full-child reserve/unused rank;retain Pi,old debits and joint error occupation;A090/A094 review.\n',encoding='utf-8',newline='\n')
with (A/'WORKLOG.md').open('a',encoding='utf-8',newline='') as f:f.write(f'\n2026-10-27 stage22 ({R.name}): derived robust physical first-query debit via disjoint touch/no-touch error partition, slope2 for point defects; hereditary terminal guard explicit. A055 Sections1--3 reconstructed unchanged, excluding NAND32 seed. {total} exact checks PASS; Lean held by memok before compiler. Universal entropy-payment supplier remains open.\n')
with (A/'LEARNED.md').open('a',encoding='utf-8',newline='') as f:f.write('\nStage22: For physical near-tensor cleanup with hereditary K-certified complete leaves, p_j=P(touch), e_j=P(error AND touch) satisfy delta-e_j>=rho_j(1-p_j), Q_j>=alpha_j p_j-2e_j. Thus actual original spent influence>=sum max(0,alpha_j-max(alpha_j/rho_j,2)delta). For h2 K1 and h3 K2 alpha/rho2 yields paired slope2; unedited h2 spends exactly t/2. Never replace e_j by delta*p_j or sum e_j by delta. Ordinary z*h2 K1 leaf is certified yet contains violating h2, so hereditary/fibre eligibility is essential and stronger than averaged optimized reserve. A055 full affine minimum is tensor additive; scoped occupation proof holds. Necessary debit is NOT entropy payment.\n')
assert set(load(R/'PROGRESS.json'))=={s.split(' (')[0] for s in protocol['required_per_run']['progress_fields']}
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
for field in protocol['required_per_run']['report_fields']:assert '## '+field in report
files=[p for p in R.rglob('*') if p.is_file() and p.name!='PERSISTENCE_RECEIPT.json']+[A/'STATUS.md',A/'WORKLOG.md',A/'LEARNED.md']
assert all(p.stat().st_size<20*1024*1024 for p in files)
receipt=[dict(path=str(p),sha256=sha(p),bytes=p.stat().st_size) for p in files]
save(R/'out/PERSISTENCE_RECEIPT.json',dict(protocol_fields_verified=True,compatibility_byte_identical=True,exact_checks=total,files=receipt))
for row in receipt:assert sha(Path(row['path']))==row['sha256']
print(json.dumps(dict(status='COMPLETE_LOCAL',exact_checks=total,files=len(receipt),run=str(R))))
