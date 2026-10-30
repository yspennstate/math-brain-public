from pathlib import Path
import json,hashlib,datetime

r=Path(__file__).resolve().parent.parent;a=r.parent.parent
protocol_path=Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
protocol=json.loads(protocol_path.read_text(encoding='utf-8'))
old=json.loads((a/'runs/20261021T220645Z-fleet03-A037-conditional-credit-ledger/PROGRESS.json').read_text(encoding='utf-8'))
main=json.loads((r/'out/CHECK.json').read_text(encoding='utf-8'));audit=json.loads((r/'out/AUDIT.json').read_text(encoding='utf-8'));formal=json.loads((r/'out/LEAN.json').read_text(encoding='utf-8'))
assert main['status']==audit['status']=='PASS'
now=datetime.datetime.now(datetime.timezone.utc).isoformat();rid=r.name
cid='A037-SECOND-FACTOR-RESET-SAME-OWNER'
statement=('For every m>=1,r>=2 disjoint width-r point-defect tensor h, take F_h=(-1)^a on x=0, h on x=b=1, +1 otherwise, with the initial7/8 correlated sector reference of A036-PAID-CORRELATED-MIXED-RESET@1. Query b, any adaptive fresh data-only prefix in b1, and x at selected leaves. ACTUALLY exercise the first5/6 tensor-core reset on x1 and matching character reset on x0, recording its complete signed amount sigma1 and retaining all complementary terminals. At any subset of these already reset x1 leaves, query one fresh bit in one surviving width>=2 point factor and ACTUALLY reset ONLY that factor to its4/5 formula on the active smaller point child, matching constant/character children, while all unqueried factor references remain the paid5/6 laws. The complete second signed reset satisfies sigma2<=log2(5/4)/8<1/24 bit. With A0=KL(initial source),e=H0-EHleaf-4(I0-EIleaf),S=4EIleaf-EHleaf, and a SAME old booking0<=omega<=1/4, S-[A0+e+sigma1+sigma2]_+-omega>17/24. Every terminal entropy, reference KL, normalization and complementary branch is retained. A declared m2r3 history has a positive second reset and two unequal nonconstant children. Changing all unqueried references too invalidates the dimension-independent second-reset cap: the actual32-factor width2 family has global extra31log2(3125/3024)/16>1/24. Full FEI, an a-branch continuation and arbitrary-core supplier remain open.')
claim={'claim_id':cid,'version':1,'exact_statement':statement,'hypotheses':['Uniform actual F_h and the fixed initial correlated7/8 lift; no older canonical source is retired','b-first, data-only adaptive prefix, selected x exposures with both children retained; first5/6 reset actually booked','Second query is inside the separated x1 product core, in one surviving width>=2 point factor','Second destination changes ONLY that queried factor to4/5; all other paid5/6 references remain unchanged','Signed original influence/query account remains owned; old omega<=1/4 subtracted once; all complementary terminals remain'],
 'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),'contributors':['A037'],
 'proof_source':{'run_id':rid,'files':['PROOF.md','code/check.py','out/CHECK.json','code/audit.py','out/AUDIT.json','out/SCOPE_GUARD.json']},
 'proof_dependencies':[{'claim_id':'A036-PAID-CORRELATED-MIXED-RESET','version':1,'statement_sha256':'67e3a2341590fc2a8f93ee751fdab23e9dfe8b49990d9c7a555a215bfb53a21a','scope':'x-only source/first-reset interface reconstructed in PROOF Sections1,4; no independent acceptance of full a-interface asserted'}],
 'review_records':[],'status':'AUTHOR_PROVED_EXACT_CERTIFICATES_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[],
 'first_unproved_line':None,'next_consumers':['A036','A038','A039','A050','A088','A094']}
(r/'CLAIMS.json').write_text(json.dumps([claim],indent=2)+'\n',encoding='utf-8')
progress={'protocol_revision':protocol['revision'],'run_id':rid,'stream':'B08','packet_id':'A037','gap_id':old['gap_id'],'attempt_id':rid,
 'method':'Consume paid correlated first reset; factorize actual next data kernel; cancel unchanged spectator KL exactly; pay second prescribed stronger factor reset from same signed original owner',
 'mathematical_delta':'All-m/r and all declared adaptive-prefix theorem: actually exercised second reset sigma2<1/24; SAME source with first sigma1 and oldquarter retains>17/24. Positive debit/unequal nonconstant fixture certified. Reset-all-factors cap extension refuted exactly.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACT_REVIEW_PENDING','mathematical_status':'ANALYTIC_PROOF_EXACT_FINITE_CERTIFICATES_FULL_FEI_OPEN',
 'claim_versions_used':[{'claim_id':'A036-PAID-CORRELATED-MIXED-RESET','version':1,'scope':'x-only interface independently reconstructed locally'}],
 'claims_created_or_changed':[{'claim_id':cid,'version':1}],'source_artifacts':['PROOF.md','out/FROZEN_SPEC.json','out/CHECK.json','out/AUDIT_SPEC.json','out/AUDIT.json','out/SCOPE_GUARD.json','out/LEAN.json','out/SOURCES_READ.json'],
 'next_consumers':claim['next_consumers'],
 'next_action':'Carry the paid a-branch5/6 reference through one actual data query and queried-factor4/5 reset; retain sigma1, oldquarter and both full terminals; identify and pay the controller/core conditional-KL correction from SAME unused owner.',
 'stagnant_substantive_attempts':0,
 'blockers':['Nonseparated a-branch factor cancellation and arbitrary-core supplier remain unpaid','Independent review/shared adoption unobserved','Checklist working update failed: shared lock held too long','Formal scalar target admission/result recorded separately; no entropy formal verification'],
 'packet_ids':['A037']}
for n in ['PROGRESS.json','PACKET_DELTA.json']:(r/n).write_text(json.dumps(progress,indent=2)+'\n',encoding='utf-8')
report=f'''# A037: a second prescribed reset after an actually paid first reset

Full FEI remains OPEN. For every point-tensor size m>=1 and width r>=2, a next data query in the already converted x branch admits a stronger prescribed queried-factor reset with global charge <1/24 bit. The SAME original source, first reset sigma1 and old quarter booking retain >17/24. This is an analytic proof with exact finite certificates; independent review is pending.

## exact target, quantifiers, hypotheses and units

Use the actual uniform Boolean F_h=(-1)^a at x0, h at x=b=1, +1 otherwise, with h a product of m disjoint width-r point defects. Begin with A036's initial correlated7/8 sector reference. Query b, any adaptive data-only prefix in b1, then x at selected data leaves, and ACTUALLY exercise its paid5/6 core reset. Both x children, the b0 branch and every complementary terminal remain. At selected reset x1 cores, query one fresh bit in one surviving point factor and ACTUALLY replace only that factor by the4/5 formula after the outcome; constant/character children match exactly. Every unqueried factor keeps its already paid5/6 reference. Bits are the units of H, CE and KL.

Let sigma1,sigma2 be the complete signed new-minus-old reference KLs of those two real conversions. At every allowed final frontier, sigma2<1/24 and S-[A0+e+sigma1+sigma2]_+-omega>17/24 for any SAME prior0<=omega<=1/4. Here S=4EI_leaf-EH_leaf and e=H0-EH_leaf-4(I0-EI_leaf). This scope requires the separated x1 product core; it excludes an a-child data query and replacing all spectator references.

The new source is the supplied correlated7/8 lift from A036, rather than the full coordinate-product source in A037's previous stage or the earlier occupancy M. No owed source is converted for free. The finite history uses two unequal nonconstant physical children and positive second resets, so this goes beyond another delayed diagnostic conversion.

## sources actually read, revisions and theorem locators

Read BOARD.md at stage start, B08 STREAM_NOTES.md v2, own STATUS/LEARNED and previous saved run20261021T220645Z. Read EXECUTION_PROTOCOL.json required fields and its unchanged revision {protocol['revision']}; the full protocol was read earlier in this conversation. The board's new useful dependency supersedes the prior canonical-source NEXT: A047/A050 identify a universal price obstruction for the full singleton source, and A036 now pays a nonmatching correlated reset after a mixed exposure.

Read A03620261023T001719Z PROOF.md in full and REPORT/CLAIMS, especially equations(1)-(4): initial7/8 price, paid5/6 destination and the source-inclusive signed identity. Read A05020261022T232833Z PROOF.md Sections1-5 and report for calibration, actual coherent inheritance, retained b0 terminal and mixed-pair eligibility. Read A036/A038/A039/A050 rolling lessons. The new proof reconstructs the exact x-only source/first-reset interface; no full independent acceptance of A036's a-branch theorem is asserted. Source byte pins are in out/SOURCES_READ.json. No peer helper was imported or executed. Own exact.py is copied from the previous A037 stage.

Prior campaign/manuscript reading remains prior-stage provenance; no literature theorem is a mathematical premise here. The lead's original k2 benchmark is already closed in an earlier substantive A037 run; its warning against repeated generic KL/point-defect class bounds remains in force. The present application concerns actual second reference expenditure, not a new claim that point defects satisfy FEI.

Wake reports brain self-care degraded/unverified because owner-model and state-of-mind notes are stale (about88/73hours). This warning was reported before relying on notes; current instructions and campaign files governed. The checklist working update failed on a shared lock and no lock was changed. Snapshot physical RAM was about2.2GB and disk24.8GB; concurrent Claude/render/Python work was left running. No personal-context note is a proof premise.

## complete derivation or exact first unsupported line

PROOF.md contains the complete all-parameter derivation. The reconstructed original source margin is M0=4I0-CE0>1+2Pr(h=-1)+3m2^-r/10. Its first ACTUAL reset satisfies sigma1<11m2^-r/40 by the original factor variances, leaving M0-sigma1>1. No new root account is issued at this frontier.

In the separated x1 core, both actual spectrum and paid reference are products. The next coherent data kernel depends only on the queried point factor. Its inherited children are the predicted queried-factor reference times the SAME spectator reference. The fresh second law changes only the queried factor, so all spectator KL costs cancel EXACTLY in the new-minus-old reset. Dropping only the queried factor's nonnegative inherited KL leaves a fresh bill bounded by log2(5/4)/2 per selected core node: only one physical outcome has a nonconstant point factor. Selected x1 cores have total reach<=1/4, hence sigma2<=log2(5/4)/8<1/24. The last strict sign is the exact integer125<128.

All complete final frontiers have S>=2: b0 contributes1, exposed x0 characters contribute their half-pair reserve, and point-tensor data cores have nonnegative certified surplus. The two paid resets telescope with the original A0 as A0+sigma1+sigma2=total erasure+total outcomeKL+full current terminalKL. Algebra then gives S-[A0+e+sigma1+sigma2]_+=min(S,M0-sigma1-sigma2)>23/24. Subtracting the OLD quarter ONCE leaves>17/24. The earlier>=3/4 and new>17/24 margins describe different frontiers; their difference1/24 is the allowance for this additional reset, not unexplained numerical drift.

The queried-factor-only hypothesis is substantive. If all31 untouched width2 factors of a32-factor core are also changed5/6 to4/5, each adds exactly log2(3125/3024)/4 KL. The full global second reset is31log2(3125/3024)/16>31/512>1/24. Exact integers3125^32>2*3024^32 certify the bound. This actual Boolean tensor countercontrol refutes extending the constant new reset-price cap to resetting every factor; it does not refute FEI or assert exhaustion of that larger tensor's original owner.

FIRST UNSUPPORTED UNIVERSAL LINE: after the paid a exposure the controller and core remain coherent, so unchanged-factor cancellation need not hold. Price the resulting conditional controller/core reference correction from the SAME diminished original bank with both terminals and sigma1/omega retained, or supply an arbitrary-core correlated reference certificate. Neither a canonical source conversion nor arbitrary-core FEI is proved here.

## executed validation with domain, arithmetic, commands and outputs

out/FROZEN_SPEC.json precedes execution. From A037:

    python -X utf8 -B runs/{rid}/code/check.py --pilot
    python -X utf8 -B runs/{rid}/code/check.py
    python -X utf8 -B runs/{rid}/code/audit.py

Pilot(1,3), three declared policies:566checks PASS,.121370s. Main four roots(1,3),(2,2),(2,3),(3,2), three policies each: {main['ledger_checks']} exact/interval checks PASS in {main['runtime_seconds']:.6f}s. Maximum9physical bits. All histories use b, the first data bit, x at both data-frontier leaves, real5/6 reset, then first/last eligible-factor data query on all core children or last factor only under data0, and real4/5 queried-factor reset. No symmetry quotient, random search or automatic dimension growth. The tentative scalar widths2..12 listed in the main spec were not separately enumerated; the independent audit domain is widths2..5 only.

Exactly {main['positive_second_resets']} of the12 main transactions have strictly positive second signed debit. The (2,3) last-factor policies include a pair with two unequal nonconstant children. Full terminal H,I,S4, current KL and normalized reference masses, old sigma1, actual sigma2, rootA0, total erasure/outcomes and oldquarter are saved for every policy. Integer Walsh agrees with direct physical-edge influence counts. Fraction coherent normalizers and exact likelihood factorization support the KL chain; forty-term atanh intervals with rigorous tails and directed2^-160 rounding certify signs. Interval overlap diagnoses algebraic identities only; it is not their proof.

Independent code/audit.py imports neither main checker nor interval helper. It uses literal character sums, Fraction atomwise posterior products, exact prime-log cancellation and separate sixty-term Fraction logarithms. Eight declared factor/spectator cases (queried widths2..5, spectator widths2,3) produce {audit['checks']} checks PASS in {audit['runtime_seconds']:.6f}s. The unchanged spectator KL cancels EXACTLY; width3 reset signs are independently positive. This is a second representation/implementation by A037, not external independent review. The32-factor scope guard is analytic tensor arithmetic with a separately frozen exact-integer certificate, not a huge truth-table job.

Main and audit estimates90MB/50MB; actual peaks unmeasured. Each research job is below55s, no GPU or detached job. Formal scalar source code/Bank.lean states only24-unit owner minus6-unit prior and1-unit second charge leaves17units. Fresh memok receipt and formal result: {formal['status']}, memok exit {formal['memok_exit']}. No entropy theorem is formalized or labelled Lean-checked. Existing running work was not stopped or throttled. No git, mail, brain writes, foreign-folder mutations, trading access or deletion. The current user campaign endpoint2026-10-23T14:49Z governs over the obsolete protocol date; no schedule was changed.

## proof dependencies and changed downstream conclusions

Named source interface: A036-PAID-CORRELATED-MIXED-RESET@1, exact statement hash67e3a2341590fc2a8f93ee751fdab23e9dfe8b49990d9c7a555a215bfb53a21a. PROOF Sections1,4 reconstruct its source/first-reset price at x-only scope from point spectra, complete lift and conditional variance; full a-branch acceptance is not inferred. The new factor-product cancellation and second cost are proved independently. This is a scoped continuation of an existing source/history candidate, not a new broad FEI hypothesis.

A036/A039/A050 can now carry an ACTUALLY reset x core through one more actual data query and prescribed correlated replacement with sigma1 and the prior quarter still booked. Unqueried references remain the paid5/6 laws. Consumers cannot reset all factors and reuse the<1/24 cap, apply x factorization to an a child, renew the>=3/4 first frontier, or discard complementary entropy/KL terminals. No universal FEI constant improves.

## one next mathematical action and independent reviewer

Next: expose one data coordinate after the paid a exposure and its5/6 correlated reset. Keep the actual incoming coherent law, first sigma1, oldquarter and both complete child references. Separate the queried-factor cancellation from the conditional controller/core correction and pay that correction from the SAME unused owner. A036/A050 should reconstruct the inheritance; A088/A094 should review product cancellation, the factors1/2 and1/4, and once-only signed ownership. No messages were sent.

## actual persistence receipts or precise save blocker

Saved REPORT, CLAIMS, PROGRESS, PACKET_DELTA, full PROOF, self-contained main and independent audit code, own interval primitives, frozen specs, exact outputs, scope-guard certificate, formal source/admission result and source hashes, all inside A037. STATUS has two lines; WORKLOG/LEARNED append this stage. out/PERSISTENCE.json verifies exact protocol keys, statement hash, identical progress/delta, artifact hashes and files below20MB. Shared checklist lock failure is recorded separately; local research saving succeeded. Supervisor copying, mirrors, brain ingestion, adoption and independent acceptance remain unobserved.

Universal bridge: This moves C024 history transfer and C019 stopping-tree payment by paying a second actually prescribed positive reset after A036's already paid mixed x exposure, through a real data query with unequal nonconstant children. The all-m/r proof costs<1/24 from the SAME original owner, keeps first sigma1 and oldquarter, retains all terminal costs and guarantees>17/24 remaining. The universal constant improves by zero. Nonseparated a-child conditional-reference correction and arbitrary-core suppliers remain unpaid; NEXT targets precisely where the factor cancellation fails in this same diminished-account history, the shortest route toward universal payment rather than another point-tensor entropy bound.
'''
(r/'REPORT.md').write_text(report,encoding='utf-8')
(a/'STATUS.md').write_text('STATE: A037 second actual correlated factor reset paid all-m/r after x exposure; charge<1/24, SAME owner with oldquarter/firstsigma retains>17/24; 6717+67 checks PASS; FEI OPEN, review pending.\nNEXT: Carry paid a-child coherent5/6 reference through one data query/4/5 factor reset; pay conditional controller correction from SAME diminished owner, both terminals retained; A088/A094 review.\n',encoding='utf-8')
entries={
 'WORKLOG.md':f'\n## {now} — {rid}\nConsumed A036 paid first correlated reset. Proved all-m/r next-data queried-factor-only reset sigma2<1/24, SAME owner with oldquarter/sigma1 retains>17/24. Main6717checks/12histories/3positive debits and independent67checks PASS. Exact32-factor scope guard refutes resetting every spectator under the same constant cap. Formal {formal["status"]}; checklist working lock failure recorded. FEI OPEN.\n',
 'LEARNED.md':'\n## Second paid correlated reset after x (20261023T014602Z)\n- After A036 first ACTUAL5/6 reset, separated x1 core p and q are tensor products. A data kernel in one point factor leaves every other PAID reference unchanged. Those spectator KLs cancel EXACTLY in new-minus-old reset; never recharge them as fresh tensor KL.\n- A second4/5 reset ONLY on the queried factor costs<=log2(5/4)/2 per eligible core node: inactive child matching, active half has variance<=1. Total physical reach<=1/4 gives global sigma2<=log2(5/4)/8<1/24.\n- Original7/8 source headroom minus first sigma1 exceeds1. Full x/data frontier S>=2. Signed identity with BOTH actual resets gives remaining>17/24 after SAME oldquarter. Earlier3/4 and new17/24 refer to different frontiers; difference1/24 is the new charge allowance.\n- (m,r)=(2,3) raw fixture exercises positive second debit with unequal nonconstant data children. General proof is all-m/r/adaptive-prefix, finite12histories are verification only.\n- Queried-factor-only is essential to the constant cap: each untouched width2 factor reset5/6->4/5 costs c=log2(3125/3024)/4>1/128.32-factor actual Boolean tensor at reach1/4 has second extra31log2(3125/3024)/16>1/24. This refutes the local cap extension, not FEI or full source payment.\n- Nonseparated a child has coherent controller/core coupling; this product cancellation cannot be imported without paying its conditional KL correction. No owed canonical reference is retired by the supplied correlated lift.\n'}
for n,t in entries.items():
 with (a/n).open('a',encoding='utf-8') as f:f.write(t)
assert set(progress)==set(x.split(' (')[0] for x in protocol['required_per_run']['progress_fields'])
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
assert (r/'PROGRESS.json').read_bytes()==(r/'PACKET_DELTA.json').read_bytes()
assert len((a/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
assert all('## '+x in report for x in protocol['required_per_run']['report_fields'])
files=[]
for p in sorted(r.rglob('*')):
 if p.is_file() and p.name!='PERSISTENCE.json':
  b=p.read_bytes();assert len(b)<20_000_000
  files.append({'path':str(p.relative_to(r)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
receipt={'status':'PASS','saved_at':now,'protocol_keys_exact':True,'progress_delta_identical':True,'statement_hash_verified':True,'status_two_lines':True,'files_under20MB':True,'artifacts':files,'independent_acceptance_and_mirrors':'UNVERIFIED'}
(r/'out/PERSISTENCE.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'PASS','artifacts':len(files),'main_checks':main['ledger_checks'],'audit_checks':audit['checks'],'formal':formal['status']}))
