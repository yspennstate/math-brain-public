from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
root=Path(__file__).resolve().parents[1]
agent=root.parents[1];team=agent.parents[1]
base=Path(r'math-open-problems/reports\fei-2026-10-11')
protocol=json.loads((base/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
sha=lambda b:hashlib.sha256(b).hexdigest()
now=datetime.now(timezone.utc).isoformat()
def dump(name,data):
    (root/name).write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='')
sources=[]
def read(p,scope):
    b=p.read_bytes();t=b.decode('utf-8-sig')
    sources.append(dict(path=str(p),sha256=sha(b),bytes=len(b),scope=scope))
    return t
read(base/'EXECUTION_PROTOCOL.json','full protocol schema and rules; current revision')
read(team/'BOARD.md','stage-start B09 and current cross-agent frontier')
read(team/'claude/B09/STREAM_NOTES.md','lead v2; initial address target already completed in prior stages')
read(agent/'runs/20261026T220625Z-fleet04-A044-non-symmetric-gate-classes/PROOF.md','previous equality result and exception-aware supplier caveat')
for who,run in [('A041','20261027T041724Z-fleet04-A041-weighted-threshold-fei'),
                ('A042','20261027T072918Z-fleet04-A042-bias-endpoint-certificates'),
                ('A045','20261027T005611Z-fleet04-A045-biased-realizability-referee')]:
    read(team/'agents'/who/'runs'/run/'PROOF.md','complete current dependency/context proof read; no claim adoption in this run')
rr=team/'agents/A043/runs/20261027T111611Z-fleet04-A043-prime-gate-decomposition'
read(rr/'PROOF.md','complete independent reconstruction of prime completion and fixed-n/dyadic transfer')
cc=json.loads(read(rr/'CLAIMS.json','exact source version and statement pin'))
sourceclaim=next(c for c in cc if c['claim_id']=='A043-PRIME-SELECTOR-COMPLETION')
assert sourceclaim['statement_sha256']=='cdd7a55e150fc3d3ce086809136270f3eff0c1a2ea2dc9de99592754946971cf'
sourceclaim['review_records'].append(dict(reviewer='A044/fleet04',outcome='HOLDS_SCOPED',
    source_statement_sha256=sourceclaim['statement_sha256'],source_proof_sha256=sha((rr/'PROOF.md').read_bytes()),
    review_source=str(root/'PROOF.md'),scope='Original essential-core prime completion, exact centered coefficients, fixed-n continuous entropy limits and one-scale dyadic guard; no arbitrary-core supplier accepted; source checker counts not adopted',
    independent_validation=['out/CHECK.json','out/INDEPENDENT.json'],source_mutation='none'))

statement=('For any finite Boolean faces f,q under a fixed interior independent core product law and a distinct '
 'selector of bias e down to0, let G=f on selector0,q on selector1, and let d be the mass of high core atoms '
 'with |a_S|=2^-k,k>=1, and a_S(b_S-a_S)>0. For upper dyadic rounding, lim Jhi(G)=Jhi(f)-ln4*d. '
 'For complete singleton-preserving high references with high mass M, rounded weight Z, mantissa Lhi, '
 'n=Mln(Z/M),K=KL(P||Q)=n-Lhi, the limits are Z+3d,Lhi+ln4*d,n+Mln(1+3d/Z), '
 'K+Mln(1+3d/Z)-ln4*d, respectively; M=0 is treated by zero charges. '
 'Thus Jhi+n-K transports exactly with both full endpoint reference laws. On fair cores, zero-jump '
 'input-reflected T2^n completion is equivalent to the dangerous-set parity equations and forbidden-face exclusions. '
 'Every essential fair3- or4-bit core admits such an eligible zero-jump completion. For the essential fair5-bit '
 'core positive only at00000, every one of32 reflected T2^5 faces is eligible and gives a prime6-bit completion; '
 'outward-atom counts by reflection weight r=0..5 are6,5,10,9,6,5, so minimum lost mass is5/256. '
 'The best limit is99ln4/256 versus seed104ln4/256; its full limiting KL is '
 '[26ln(41/26)-5ln4]/256>0. No reflection in this stated completion class eliminates that jump; '
 'no other completion class or universal FEI payment is excluded.')
cid='A044-EXACT-PRIME-BOUNDARY-JUMP-AND-FULL-KL-TRANSPORT'
new=dict(claim_id=cid,version=1,exact_statement=statement,
    hypotheses=['Actual finite Boolean sign faces; fixed interior independent core product law; distinct independent physical selector',
    'Natural logs and upper dyadic convention; normalized physical centered coefficients; high means |S|>=2',
    'Complete references preserve actual empty and singleton masses; ordinary full KL and both full terminal laws retained',
    'M=0 treated by zero charges before division; all boundary limits fixed finite core dimension',
    'Reflection/parity and low-dimensional existence statements require fair core inputs; the five-bit obstruction is only for input-reflected T2^5 faces',
    'Prime completion requires essential core n>=3 and excluded faces f,-f and single-input reflections of f'],
    statement_sha256=sha(statement.encode()),contributors=['A044/fleet04'],proof_source=dict(path='PROOF.md',sha256=sha((root/'PROOF.md').read_bytes())),
    proof_dependencies=[dict(claim_id=sourceclaim['claim_id'],version=sourceclaim['version'],statement_sha256=sourceclaim['statement_sha256']),
                        'Direct physical coefficient/label expansion; finite termwise limits; ordinary KL identity; direct threshold coefficients and parity count'],
    review_records=[],status='AUTHOR_ANALYTIC_PROOF_WITH_EXACT_CERTIFICATES_PENDING_INDEPENDENT_REVIEW',supersedes=[],
    refutes=['Unregistered proposed repair: choose an admissible input-reflected threshold completion to make Jhi continuous for every essential fair core'],
    first_unproved_line='No gap asserted in the stated fixed-n exact transfer. Original dimension-independent arbitrary-core influence price remains unpaid; no full FEI resolution or uniform continuity modulus is claimed.',
    next_consumers=['A043','A045','A041','A042','A091','B09 lead'])
dump('CLAIMS.json',[sourceclaim,new])
dump('out/SOURCE_RECEIPTS.json',dict(observed_at=now,sources=sources))
main=json.loads((root/'out/CHECK.json').read_text(encoding='utf-8'))
ind=json.loads((root/'out/INDEPENDENT.json').read_text(encoding='utf-8'))
assert main['status']==ind['status']=='PASS'
nextaction=('A043/A045/A091 independently audit exact jump/full-KL transport; then supply an ORIGINAL O(I(core)) '
 'high-sector reference/source price surviving prime completion and the forced dyadic transfer, with previous '
 'singleton/import/carry debits and BOTH full endpoint laws retained. Choosing a reflection or taking a limit is not that price.')
progress=dict(protocol_revision=protocol['revision'],run_id=root.name,stream='B09',packet_id='A044',
    gap_id='FEI-B09-ARBITRARY-PRIME-HIGH-SCALE-ORIGINAL-PAYER',attempt_id='A044-substantive11-exact-prime-boundary-transport',
    method='Independent A043 review; exact directional dyadic/reference limit; parity feasibility; exhaustive small cores and all reflection witness',
    mathematical_delta='Exact lost high-scale mass and full KL conversion; all fair3/4-bit cores admit zero-jump completion but a fair5-bit point core forces minimum5/256 outward mass for all32 threshold reflections; no arbitrary-core price supplied.',
    deliverable_status='COMPLETE_LOCAL',mathematical_status='RESTRICTED_AUTHOR_PROOF; COMPLETION_REPAIR_OBSTRUCTION; FULL_FEI_OPEN',
    claim_versions_used=[dict(claim_id=sourceclaim['claim_id'],version=sourceclaim['version'],statement_sha256=sourceclaim['statement_sha256'])],
    claims_created_or_changed=[sourceclaim['claim_id'],cid],source_artifacts=['PROOF.md','out/CHECK.json','out/INDEPENDENT.json','out/SOURCE_RECEIPTS.json','out/LEAN_ADMISSION.json'],
    next_consumers=['A043','A045','A041','A042','A091','B09 lead'],next_action=nextaction,stagnant_substantive_attempts=0,
    blockers=['Universal original arbitrary-core high-sector price unpaid','New exact transport pending independent review','Lean admission memok exit1; scaffold is not compiled','Supervisor remote mirroring/adoption unobserved'],packet_ids=['A044'])
dump('PROGRESS.json',progress);dump('PACKET_DELTA.json',progress)
report=f'''## exact target, quantifiers, hypotheses and units

Consume A043's new arbitrary-core prime completion and make its high-scale boundary transfer exact, including both complete reference laws and ordinary KL. Every finite Boolean core/face at every fixed interior product law; rare selector e down to0; natural entropy units. Fair-input restrictions apply only to the reflection feasibility and first-unavoidable-five-bit obstruction. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

Stage-start BOARD.md dated2026-10-27 14:34UTC B09 section, lead STREAM_NOTES.md v2, own STATUS and previous proof; current protocol v2. Complete new proofs read: A041 run20261027T041724Z, A042 run20261027T072918Z, A045 run20261027T005611Z, and A043 run20261027T111611Z. A043 prime theorem, exact coefficient equations(1)-(2), fixed-n entropy limits(3), and dyadic guard(4) are independently reconstructed in PROOF.md sections1-3; exact source claim hash is pinned. Other new stream proofs supply context, not accepted premises. Historical campaign/paper sources were read in earlier stages and are not fresh premises. out/SOURCE_RECEIPTS.json pins actual sources. The lead's initial address task is already completed; this stage follows its review-first rule and the current unpaid universal supplier.

## complete derivation or exact first unsupported line

PROOF.md gives the exact outward-dyadic mass d and proves lim Jhi(G)=Jhi(f)-ln4*d. The same complete flat reference has limiting rounded high weight Z+3d, mantissa Lhi+ln4*d, and full KL K+Mln(1+3d/Z)-ln4*d. Thus Jhi+n-K transports exactly; the signed correction is never credited twice. A fair-core reflection has zero jump precisely when its dangerous-set parity constraints are feasible and a solution survives the forbidden-face exclusions. Every essential fair3/4-bit core has such a completion, but the fair5-bit point core forces counts6,5,10,9,6,5 by reflection weight. Its best completion loses5ln4/256 of rounded charge; both entropy and the retained core price survive in the full reference/KL account. The exact source claim HOLDS at its original scope. First unsupported universal line: fund the arbitrary retained core high entropy from SAME unused original influence after all earlier debits; exact transfer and reflection selection do not pay it.

## executed validation with domain, arithmetic, commands and outputs

Frozen specs preceded execution. Main: python -X utf8 code/check_stage.py, run-relative. All256 ternary and65,536 quaternary labelled tables, with218 and64,594 essential cores respectively, each has an eligible zero-jump reflection. Every selected ternary completion is checked prime by direct cofactor rows (218 checks); quaternary completion primeness relies on the analytic source theorem, not an unexecuted census. All32 reflected five-bit point-core faces are eligible and their six-bit completions are directly checked prime. Added96 actual biased fixtures: all32 faces at e=1/16,1/256,1/4096, checking direct rational physical transforms, exact coefficient factorization, Parseval, influence, complete reference normalization/ratios and exact quadratic rounded-scale formulas. PASS {main['assertions']} assertions in {main['seconds']:.4f}s. Independent: python -X utf8 code/check_independent.py, direct physical coefficient sums for all32 faces, literal GF2 inconsistency, four strictly positive full-KL corrections checked with40-term rational range-reduced atanh intervals and proved geometric tails. PASS {ind['checks']} checks in {ind['seconds']:.4f}s. Main frozen core count65,824 plus separately frozen96 biased fixtures totals65,920 cases; no automatic dimension escalation, no floating-point sign decision. Jobs estimated<=70MB and bounded55s. Fresh memok exited1 (commit free7.1GB<8.0GB), so Lean was not launched; code/JumpParity.lean is an uncompiled scaffold only. Rung: analytic proof with exact certificates, pending independent review, not Lean-checked.

## proof dependencies and changed downstream conclusions

The copied A043-PRIME-SELECTOR-COMPLETION@1 record adds a scoped independent HOLDS review without changing its statement/version; source certificate counts are not adopted and no shared registry changes. The new exact jump strengthens its one-scale guard, and the reference formula retains both full endpoints. The five-bit witness refutes only the unregistered universal zero-jump-reflection repair in this specified threshold-face completion class. It does not refute A043's theorem, other completion classes, any correct entropy continuity statement, or FEI. New prime gates still contain the unpaid original core; no depth/fan-in FEI constant changes. Prior singleton imports/carries and S_tree retain their owners.

## one next mathematical action and independent reviewer

{nextaction}

## actual persistence receipts or precise save blocker

All four protocol files, proof, frozen specs, checkers, exact outputs and source pins are saved locally. PROGRESS.json and PACKET_DELTA.json are identical with packet_ids=[A044]. Rolling STATUS has two lines; WORKLOG and LEARNED append this stage. out/PERSISTENCE.json rereads/hashes every artifact and checks exact schemas and source pins. No shared source, other agent folder, brain store, trading path or external system was modified; no git, message, worker, GPU or remote/background job was used. Supervisor mirroring and new independent review are unobserved. Brain self-care remains degraded/unverified (stale owner-context and dream notes); these are not mathematical premises. The fresh compute snapshot was read and no existing work was stopped, suspended or throttled; no stage job remains running.

**Universal bridge:** This stage moves C020 whole-set witness cost by making the arbitrary-core prime boundary's rounded-scale and full-reference transfer exact: the lost charge is ln4 times the actual outward dyadic mass, with its precise signed normalizer/KL replacement and BOTH full terminals retained. Reflection can remove that charge for every fair3/4-bit core, but an explicit fair5-bit core forces at least5ln4/256 across all32 allowed threshold faces, closing the universal zero-jump selection repair. This is an endpoint-accounting improvement, not original-source payment: arbitrary-core high entropy and full FEI remain OPEN. The shortest NEXT is a noncircular original O(I(core)) high-sector source surviving this now-exact transfer, rather than another reflection search, isolated gate class or continuity limit that leaves the same core unpaid.
'''
(root/'REPORT.md').write_text(report,encoding='utf-8',newline='')
(agent/'STATUS.md').write_text('STATE: A044 stage22 saved: A043 prime completion independently HOLDS; exact dyadic/full-KL transport; unavoidable5/256 jump for all32 five-bit faces;79755+38 checks PASS;FEI OPEN.\nNEXT: A043/A045/A091 review jump/reflection/full-terminal account; pay arbitrary retained-core high entropy from ORIGINAL O(I) source after imports/carries/BOTH KL terminals; no zero-jump shortcut.\n',encoding='utf-8',newline='')
with (agent/'WORKLOG.md').open('a',encoding='utf-8',newline='') as f:
    f.write(f'\n## {now} — stage22 exact prime-boundary transport\nA043 completion independently HOLDS. Exact high-scale limit loses ln4*d; full-reference Z/L/K shifts preserve entropy with both terminals. Fair3/4-bit cores all have zero-jump reflected completions; a fair5-bit point core forces min5/256 outward mass over all32 reflected threshold faces. Main79755 assertions/6.33s, independent38 checks/0.13s PASS. Lean admission HELD (memok exit1), scaffold not compiled. Full FEI OPEN; NEXT: original arbitrary-core O(I) source after old debits.\n')
with (agent/'LEARNED.md').open('a',encoding='utf-8',newline='') as f:
    f.write('\n## Stage22 — unavoidable dyadic prime-boundary transfer\nFor G=(f,q) with selector e->0, outward high dyadic atoms d have a(b-a)>0; exact lim Jhi=Jhi(f)-ln4*d. Complete reference Zlim=Z+3d,Llim=L+ln4*d,nlim=n+Mln(1+3d/Z),Klim=K+Mln(1+3d/Z)-ln4*d; signed full KL replaces its old law, never free credit. Zero jump under fair reflected T2 faces is a GF2 character compatibility problem plus forbidden-face exclusions. All essential fair3/4-bit cores admit an eligible zero-jump face; fair5-bit point-positive core has outward counts6,5,10,9,6,5 by reflection weight, min5/256, every face eligible/prime. Best Jhi limit99ln4/256 vs seed104ln4/256; limiting fullKL=[26ln(41/26)-5ln4]/256>0. The forced jump is harmless to entropy but cannot be discarded in a rounded supplier; other completion classes and universal FEI remain open.\n')
expected=set(protocol['required_per_run']['claim_fields'])
assert set(sourceclaim)==set(new)==expected
expected=set(protocol['required_per_run']['progress_fields']);expected.remove('packet_ids (one primary ID, for compatibility)');expected.add('packet_ids')
assert set(progress)==expected
assert (root/'PROGRESS.json').read_bytes()==(root/'PACKET_DELTA.json').read_bytes()
assert len((agent/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
for field in protocol['required_per_run']['report_fields']:assert '## '+field in report
for s in sources:assert sha(Path(s['path']).read_bytes())==s['sha256']
artifacts=[]
for p in root.rglob('*'):
    if p.is_file() and p.name!='PERSISTENCE.json':
        assert p.stat().st_size<20_000_000
        artifacts.append(dict(path=str(p.relative_to(root)),bytes=p.stat().st_size,sha256=sha(p.read_bytes())))
dump('out/PERSISTENCE.json',dict(at=now,status='PASS',schema_check='PASS',source_pins_unchanged=True,artifacts=artifacts,
     rolling=[dict(path=str(agent/n),sha256=sha((agent/n).read_bytes())) for n in ['STATUS.md','WORKLOG.md','LEARNED.md']],
     mirror='not observed',independent_review='new claim pending',formal='not run; admission held'))
print(json.dumps(dict(status='SAVED_AND_VALIDATED',claims=2,artifacts=len(artifacts),sources=len(sources))))
