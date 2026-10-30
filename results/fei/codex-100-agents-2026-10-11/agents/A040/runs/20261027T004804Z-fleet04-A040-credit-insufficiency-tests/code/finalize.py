from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1]; A=R.parent.parent; BASE=A.parent.parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def put(p,v):p.write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
main=json.loads((R/'out/CHECK.json').read_text(encoding='utf-8'))
audit=json.loads((R/'out/AUDIT.json').read_text(encoding='utf-8'))
assert main['status']==audit['status']=='PASS'
assert main['runtime_seconds']<55 and audit['runtime_seconds']<55
assert main['helper_sha256']==sha(R/'code/check.py')
assert audit['helper_sha256']==sha(R/'code/audit.py')
spec=json.loads((R/'out/FROZEN_SPEC.json').read_text(encoding='utf-8'))
assert spec['helper_sha256']==sha(R/'code/check.py')
failed=json.loads((R/'out/MAIN_FAILURE.json').read_text(encoding='utf-8'))
assert failed['sha256']==sha(R/'out/MAIN_FAILED_HELPER.py')
sources=[]
def source(p,scope):
    p=Path(p); sources.append({'path':str(p),'sha256':sha(p),'scope':scope})
source(BASE/'BOARD.md','current intake; full board was read into a truncated tool output; relevant B08/B10 and neighboring source-supplier lines reread separately')
source(BASE/'claude/B08/STREAM_NOTES.md','v2 2026-10-11; completed old minimum-ratio target is not repeated')
source(A/'LEARNED.md','full durable stage history at intake')
source(A/'runs/20261023T132348Z-fleet03-A040-credit-insufficiency-tests/PROOF.md','stage10 sections1-4: original proposed sufficient charge and actual family')
for agent,run in [('A039','20261026T214918Z-fleet04-A039-projection-under-restrictions'),('A049','20261026T221646Z-fleet04-A049-minimal-falsifier-extraction'),('A050','20261023T132645Z-fleet03-A050-repair-with-scope')]:
    for f in ['PROOF.md','CLAIMS.json']:
        p=BASE/'agents'/agent/'runs'/run/f
        source(p,'PROOF read in full; CLAIMS byte pin/intake only' if f=='PROOF.md' else 'claim metadata pin, not new independent acceptance')
campaign=Path(r'math-open-problems/reports\fei-2026-10-11')
for f in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']:
    source(campaign/f,'execution protocol full read; other campaign baselines relevant sections refreshed, not a new complete source audit')
for p in (BASE/'context').glob('*.txt'):source(p,'prior accepted paper baseline; selected entropy/restriction/relative-entropy/singularity excerpts reread; explicit cp1252 decoding')
put(R/'out/SOURCE_RECEIPTS.json',{'recorded_at':now,'sources':sources})
statement=('For every integer r>=3, let G and its support-matched activated full-spike reference be as in PROOF section2 with alpha=r^-2, and prescribe first physical query j. Let K=D(P_G||Q_G), O its coherent outcome KL, X=chi2(erased Q_G||erased P_G), V the exact erased score variance, beta=1-alpha, and C_V=2XV/[beta(2-beta)ln2], C_eta=2X Inf_j(G)(1-Inf_j(G))/[beta(2-beta)ln2]. Then O<=C_V<=C_eta, C_V/O~7*2^r/9, C_eta/O~10*2^r/9, C_V/K~7*2^r/(100r^2), C_eta/K~2^r/(10r^2), while O/K~9/(100r^2). Thus no absolute multiple of the SAME original KL can bound these surrogate sums over every finite prescribed physical tree, even at its first node; this does not refute existential coordinate selection, exact inherited-reference KL payment, an influence-surplus payer, or FEI.')
claim={'claim_id':'A040-CHI2-SURROGATE-ORIGINAL-KL-OVERPRICE','version':1,'exact_statement':statement,
       'hypotheses':['actual Boolean family G specified in PROOF.md section2','integer r>=3; alpha=r^-2','query j required first; own-outcome normalization; matching support','surrogate payer is original KL K, not arbitrary larger influence surplus'],
       'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),'contributors':['A040'],
       'proof_source':str(R/'PROOF.md'),'proof_dependencies':[],
       'review_records':[{'reviewer':'A040','type':'separate direct-Walsh/prime-log implementation; not independent peer review','result':'PASS 146 assertions; full analytic asymptotics reread against exact formulas'}],
       'status':'PROVED_LOCALLY_REVIEW_PENDING','supersedes':[],'refutes':['A040 stage10 proposed cumulative chi-square variance charge from same original KL, for arbitrary prescribed policies'],
       'first_unproved_line':'No gap claimed for the stated asymptotic obstruction. Universal noncircular influence-priced original supplier and necessary terminal-policy payment remain open; Lean and external review pending.',
       'next_consumers':['A049','A050','A039','A088','A094']}
put(R/'CLAIMS.json',{'claims':[claim]})
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':R.name,'stream':'B08','packet_id':'A040',
          'gap_id':'G-R-MISMATCH','attempt_id':'A040-stage11-chi2-surrogate-overprice',
          'method':'Exact actual-Boolean Fourier-row derivation and asymptotic comparison; independent representation check; consume inherited original-KL telescope without duplicate acceptance',
          'mathematical_delta':'Retire proposed surrogate payment: exact-variance chi2 price/original KL ~7*2^r/(100r^2), while actual outcome/original KL ~9/(100r^2). Exact inherited-reference cumulative invoice remains paid. FEI unchanged.',
          'deliverable_status':'COMPLETE_LOCAL','mathematical_status':'NARROW_OBSTRUCTION_PROVED_LOCALLY; FULL_FEI_OPEN',
          'claim_versions_used':['A040 stage10 PROOF sections1-3 (own source; family reconstructed)','A050-FIXED-PROFILE-ZERO-COST-REPAIR@1 sections1-3 (context; A049 reconstruction read, no new acceptance)'],
          'claims_created_or_changed':[claim['claim_id']+'@1'],
          'source_artifacts':['PROOF.md','out/SOURCE_RECEIPTS.json','out/FROZEN_SPEC.json','out/AUDIT_SPEC.json','out/CHECK.json','out/AUDIT.json'],
          'next_consumers':claim['next_consumers'],
          'next_action':'A049/A050 specify a USEFUL NECESSARY terminal profile; compare its EXACT excess invoice against SAME diminished original owner after old bills and both full terminals, or supply noncircular arbitrary-core initial O(I) source. Do not demand generic chi2 majorants.',
          'stagnant_substantive_attempts':0,
          'blockers':['External independent review/mirror unverified','Lean admission HELD below 5500 MB; no compiler ran','Arbitrary-core original entropy/source price and sufficient terminal surplus unpaid'],
          'packet_ids':['A040']}
put(R/'PROGRESS.json',progress); put(R/'PACKET_DELTA.json',progress)
report=f'''# A040 stage11: the proposed chi-square bill overprices a paid history

## exact target, quantifiers, hypotheses and units

For every integer r>=3 use the actual Boolean activated rare-j family in PROOF section2, alpha=1/r^2, matching-support reference and prescribed first query j. All information is in bits. The exact-variance sufficient charge C_V divided by original KL is asymptotic to 7*2^r/(100r^2); C_V divided by the actual outcome invoice is asymptotic to 7*2^r/9. Thus even the first surrogate charge cannot be paid by a universal multiple of original KL, although the entire inherited-reference true invoice is bounded by that original KL. This is a quantified obstruction to the proposed majorant, not unpaid actual entropy, an existential-policy refutation, or an FEI counterexample.

## sources actually read, revisions and theorem locators

Read machine AGENTS and full execution protocol v2; refreshed campaign status/registry/B08 plan sections, supplement baseline excerpts, current BOARD, B08 STREAM_NOTES v2, own STATUS/LEARNED/recent WORKLOG and stage10 PROOF/REPORT. Source bytes and exact scopes are pinned in out/SOURCE_RECEIPTS.json. Read A039 20261026T214918 PROOF in full, A049 20261026T221646 PROOF in full (section4 reconstructs A050), and A050 20261023T132645 PROOF in full, especially sections1-3. These newer sources supersede the old NEXT's missing cumulative-outcome accounting: inherited-reference exact payment is already closed conditional on its supplier. No duplicate independent acceptance is claimed. The four supplied paper-text baselines were consulted through relevant excerpts, explicitly decoded cp1252 after a strict UTF8 decode failed; this is not a new full-paper review. No paper theorem is a dependency of the new asymptotic proof. Brain recall returned weak/unrelated results and no amortization theorem; none was used as proof. Wake flagged stale personal notes, reported to owner; those notes were excluded.

## complete derivation or exact first unsupported line

PROOF sections2-3 give every row of the actual Boolean spectrum, exact V, X, outcome bias t, original K, and all four asymptotic ratios. The r>=3 denominators are positive, reference mass and support match, all physical outcomes are retained, alpha is fixed once for each r, and no infinite-time stopping is used. The key coefficient is V~7*2^-r/20, independently checked through direct character sums. The actual outcome/original KL tends to zero as 9/(100r^2). The sufficient Cauchy majorant loses the exponential factor because X~alpha^2*4^r/20. The original proposed target was too strong for arbitrary prescribed histories; this is a correction to A040's NEXT, not a failure of A050's exact telescope. First unsupported universal line: useful arbitrary-core ORIGINAL source cross entropy at O(I), plus a stopping frontier with enough full entropy surplus or a necessary stronger profile whose ACTUAL conversion can be paid from the same unused owner. No universal constant improves. Rung: analytic proof plus exact finite certificates; external review and Lean pending.

## executed validation with domain, arithmetic, commands and outputs

Frozen specifications precede execution. Commands: python -X utf8 code/check.py --pilot; python -X utf8 code/check.py; python -X utf8 code/audit.py. Successful pilot:41 assertions,0.284612 seconds. Final main:{main['checks']} assertions,{main['runtime_seconds']:.6f} seconds: full Walsh transforms at r3,4,5 (n6,7,8), alpha1/6 and1/r^2, plus grouped r3,4,8,16,32,64,128. Exact Fraction laws and independent child spectra; 90-term atanh log enclosures with proved remainder and outward2^-160 rounding. Audit:{audit['checks']} assertions,{audit['runtime_seconds']:.6f} seconds: independent DIRECT character sums r3,4 at alpha1/r^2, exact prime-log KL chain identities, five rational coefficient fixtures throughr128; no main-helper imports. Nonpilot total285 assertions. Finite tests check formulas; the all-r theorem follows from the displayed analytic expansions.

Two failures are preserved: pilot wrongly asserted the crossing already at r8; only that auxiliary sign condition moved to frozen r>=16, with no domain change. Main reached Fraction serialization beyond Python's4300-digit limit; outward160-bit rounding fixed the exported enclosure without disabling the guard. Original failed helpers/hashes and diagnoses are retained. The source-read strictUTF8 failure was resolved by explicitly identifying cp1252 paper extracts. Lean setup returned SETUP_UNVERIFIED because available memory was below5500MB; no compiler started, no proof claimed, no unchanged retry. Estimated jobs70MB/35MB, measured compute under55sec; no >300MB job or memok gate needed, no GPU, detached process, dimension escalation or load shedding.

## proof dependencies and changed downstream conclusions

The new surrogate obstruction is self-contained; stage10's family was reconstructed from actual Boolean truth tables and complete coefficients. A050/A049's exact original-KL account is consumed as established conditional context, not added as a second new broad candidate. Full source CE=H+K remains in the ledger, along with old debits, old conversions and BOTH complete terminals. The five positive posterior-credit asymptotics are retained from stage10, not relabeled as newly checked here. Retire only chi-square-majorant payment from original KL for arbitrary prescribed policies; useful selected-policy payment, a larger legitimate influence payer and FEI remain open.

## one next mathematical action and independent reviewer

A049/A050 should state ONE necessary useful terminal profile and compare its exact excess conversion with the ACTUAL unused original margin after old bills and both full terminals. A039/A088/A094 can reconstruct the new rational V formula and asymptotic coefficients. No peer messages were sent; these files are the source-bound supervisor handoff. Another generic positive-KL lemma or optional-profile loop would not address the source/terminal bottleneck.

## actual persistence receipts or precise save blocker

All four required protocol artifacts, PROOF, code/out, failed-helper records and the three rolling files are written only under A040. code/finalize.py checks protocol field sets, identical compatibility delta, exact claim and helper hashes, two-line STATUS and file-size limits, then writes out/LOCAL_RECEIPT.json. Source trees and other-agent folders were read-only. No git, mail, messages, deletion, brain writes or trading paths were used. Supervisor copy, remote publication, peer acceptance and mirror verification are unverified. No research job remains after collection; no process was stopped. Critical memory state was observed and reported; unrelated existing work remains untouched.

Universal bridge: This stage moves C024 history transfer and C019 stopping-tree payment by removing an unnecessary surrogate invoice: even the exact-variance chi-square price can exceed the whole original KL by ~7*2^r/(100r^2), while exact inherited-reference outcome charges remain paid. The FEI constant improves by zero. What remains is the arbitrary-core influence-priced initial source and a useful stopping frontier or necessary profile whose exact additional invoice fits the SAME depleted original owner with full terminals. That exact-invoice comparison is the shortest next route because the new A050/A049 source already pays inherited normalizers; insisting on this exponentially overlarge majorant would reject histories whose actual invoice is already covered.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8',newline='\n')
status='STATE: Stage11 saved: exact-variance chi2 surrogate/original KL ~7*2^r/(100r^2), true outcome/K ~9/(100r^2); 139+146 exact checks PASS; inherited payment intact; FEI OPEN.\nNEXT: A049/A050 necessary profile EXACT invoice from SAME unused owner/full terminals or arbitrary-core ORIGINAL O(I) source; retire generic chi2-majorant demand. Pilot crossing and serializer fixed/preserved; Lean admission HELD, no retry.\n'
(A/'STATUS.md').write_text(status,encoding='utf-8',newline='\n')
lesson=f'\n{now} Stage11: On SAME actual rare-j G_r, alpha=r^-2, V~7d/20 and chi2~alpha^2/(20d^2). Exact-variance sufficient C_V/K~7*2^r/(100r^2), C_V/O~7*2^r/9, but true O/K~9/(100r^2). A050 inherited exact cumulative outcome payment <=ORIGINAL KL survives. Hence retire our stage10 arbitrary-prescribed-history chi2-budget NEXT; a too-large sufficient majorant is not actual unpaid entropy. Selected-policy avoidance, larger original influence surplus and FEI are not refuted. Need ONE useful necessary profile exact invoice/full terminals or noncircular initial supplier. Main139+audit146 PASS; finite checks support analytic all-r proof. Pilot crossing starts only at tested r>=16; outward160-bit log bounds avoid Fraction serialization limits. Lean admission HELD; no unchanged retry.\n'
with (A/'LEARNED.md').open('a',encoding='utf-8',newline='\n') as f:f.write(lesson)
with (A/'WORKLOG.md').open('a',encoding='utf-8',newline='\n') as f:f.write(f'\n{now} [{R.name}] Consumed new A039/A049/A050 source proofs; retired own overstrong cumulative chi2-surrogate target via actual all-r Boolean asymptotics. Final main139/4.968s + separate audit146/.012s PASS; successful pilot41 separate. Preserved pilot auxiliary crossing error and main Fraction export failure; repaired without domain expansion. Explicit cp1252 paper reads after strictUTF8 failure. Lean admission held; no compiler/retry. Full FEI/source price/terminal eligibility open. All artifacts/rolling files saved A040 only; no process stopped, detached job, git, message or brain write.\n')
protocol=json.loads((campaign/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))['required_per_run']
assert set(claim)==set(protocol['claim_fields'])
pf=[s.split(' (')[0] for s in protocol['progress_fields']]
assert set(progress)==set(pf)
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
for heading in protocol['report_fields']:assert '## '+heading in report
assert report.rstrip().split('\n')[-1].startswith('Universal bridge:')
for p in R.rglob('*'):
    if p.is_file(): assert p.stat().st_size<20*1024*1024,str(p)
receipt={'created_at':now,'status':'PASS_LOCAL_ONLY','claims_sha256':sha(R/'CLAIMS.json'),
         'files':{str(p.relative_to(R)):sha(p) for p in R.rglob('*') if p.is_file() and p.name!='LOCAL_RECEIPT.json'},
         'rolling':{name:sha(A/name) for name in ['STATUS.md','LEARNED.md','WORKLOG.md']},
         'external_review':'UNVERIFIED','mirror':'UNVERIFIED'}
put(R/'out/LOCAL_RECEIPT.json',receipt)
print(json.dumps({'status':'PASS_LOCAL','assertions':main['checks']+audit['checks'],'run':R.name,'files':len(receipt['files'])}))
