from pathlib import Path
import json, hashlib, datetime, copy
ROOT=Path(__file__).resolve().parents[1]; HOME=ROOT.parents[1]
# BASE is the agents directory: A040/runs/run -> A040 -> agents.
BASE=HOME.parent;SOURCE=BASE/'A023/runs/20261013T223305Z-fleet05-A023-amortized-rarity-budget'
PROTOCOL=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def save(p,d):p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
protocol=read(PROTOCOL);results=read(ROOT/'out/RESULTS.json');fixture=read(ROOT/'out/CREDIT_FIXTURE.json');pilot=read(ROOT/'out/PILOT.json')
assert results['status']=='PASS' and results['root_count']==51
assert results['checks']==20734 and fixture['status']=='PASS' and fixture['checks']==24
claim=next(c for c in read(SOURCE/'CLAIMS.json') if c['claim_id']=='A023-OVERLAP-EXPOSURE-GOOD-CONTROL-LEDGER')
assert claim['version']==2 and claim['statement_sha256']=='ceb0a37e4a74494589bdfd8efddf7cdad84f842cfba3ba3f1bc6932b12d9fc9c'
claim=copy.deepcopy(claim)
claim['review_records'].append({'reviewer':'A040','verdict':'HOLDS_SEPARATOR_EXTENSION_ONLY','source':str(ROOT/'REVIEW_A023.md'),
 'scope':'All-width added single-separator theorem, arbitrary balanced independent core; exact face ownership, descendant goodness, terminal-inclusive entropy and minority/KL ledgers, unconditional balanced bent-surgery specialization. Earlier v1 scope is not re-counted here.',
 'excluded':'No universal root-goodness, repeated-separator reserve renewal, arbitrary-core terminal FEI or full FEI acceptance.',
 'repair_supplied':False,'validation':{'actual_roots':51,'exact_assertions':20734,'additional_fixed_fixture_assertions':24},
 'source_claims_file_sha256':sha(SOURCE/'CLAIMS.json')})
claim['status']='INDEPENDENT_REVIEW_HOLDS_SEPARATOR_EXTENSION_ONLY'
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
save(ROOT/'CLAIMS.json',[claim])
sources=[PROTOCOL,HOME.parent.parent/'BOARD.md',HOME.parent.parent/'claude/B08/STREAM_NOTES.md',SOURCE/'REPORT.md',SOURCE/'SEPARATOR_RESERVE_PROOF.md',SOURCE/'CLAIMS.json',BASE/'A021/runs/20261013T214613Z-fleet05-A021-rare-core-asymptotics/REPORT.md',BASE/'A098/runs/20261013T235014Z-fleet05-A098-resource-reallocation/REPORT.md',HOME/'runs/20261013T212401Z-fleet05-A040-credit-insufficiency-tests/code/audit.py']
save(ROOT/'out/SOURCE_RECEIPTS.json',[{'path':str(p),'sha256':sha(p),'read_scope':'Protocol all; board and B08 routing; exact separator proof and claim; source reports as stated in REPORT; own prior helper viewed, not executed/imported.'} for p in sources])
report='''# exact target, quantifiers, hypotheses and units

A040/B08 stage 3, run 20261014T003941Z-fleet05-A040-credit-insufficiency-tests. Independently review exactly the additional single-separator subtheorem of A023-OVERLAP-EXPOSURE-GOOD-CONTROL-LEDGER@2. For every L,R,T>=1, independent fresh point indicators W,U,V on those widths, fair bit X, and independent balanced Boolean core g, put A=XU OR XV OR WUV and F=1+A(g-1). Query X first, resolve its actual child controller, and retain every core terminal. Entropy, posterior information and KL use bits. Influence is physical uniform-cube flip probability.

Verdict: **HOLDS for the added separator theorem, without repair**. Its one-use reserve, Q_bad<=I(F)-d_X, retained-terminal bound, and balanced bent-surgery H(F)<8I(F) specialization are independently reconstructed. Full FEI and a bounded reserve through arbitrary ancestor chains remain OPEN. No new broad candidate is opened.

# sources actually read, revisions and theorem locators

Read EXECUTION_PROTOCOL.json fully, revision 2026-10-11-execution-v2; stage-start BOARD, B08 STREAM_NOTES v2 and own STATUS. B08's old minimum-census instruction is superseded by A098's source-bound duplicate retirement and stage-3 assignment: A040 reviews the single reserve, A046 tests multi-bit transport. Followed that newer mathematical scope; no duplicate census.

Read A023 stage-3 REPORT.md, SEPARATOR_RESERVE_PROOF.md and CLAIMS.json: claim v2 statement digest ceb0a37e4a74494589bdfd8efddf7cdad84f842cfba3ba3f1bc6932b12d9fc9c. Read A021 stage-3 REPORT on balanced-controller transfer and the bad fixed-order witness; A098 stage-3 REPORT on the exact A040/A046 handoff. Viewed own stage-2 exact helper; the new implementation imports no author helper and executes no prior-run module. Earlier A040 v1 review is context, not new acceptance. Source paths and hashes are in out/SOURCE_RECEIPTS.json. No new paper or web premise was needed.

# complete derivation or exact first unsupported line

The complete independent derivation is REVIEW_A023.md. Let beta=q+r-qr, eta=pqr, pi=(beta+eta)/2, e=beta-eta for p=2^-L,q=2^-R,r=2^-T. The controller children are A0=WUV and A1=U OR V. They are nested; the boundary edge sets are disjoint coordinate by coordinate. Thus J(D)=J(A0)+J(A1)=2Jrem for D=A1-A0 and J(E)=I(1-2E)/2. With a balanced core,

    d_X=e/2,  I(F)=d_X+Jrem+pi I(g),
    c_X=I(F0F1)/2=Jrem+(e/2)I(g).

Every descendant is strictly 4-good by independently reconstructed constant-child and fresh two-point exposure bounds. Therefore Q_bad is zero or c_X, giving Q_bad<=I(F)-d_X. The root consumes exactly the one-unit remaining-controller reserve and fraction e/(2pi) of the terminal-core unit reserve. Its unused terminal capacity is eta I(g), not a fresh reserve at descendants.

The entropy and complete minority-KL accounts, retaining the terminal, satisfy

    H(F)<=(4+2/ln2)d_X+(5+2/ln2)Jrem+pi H(g)+(e/2)I(g),
    J_tree+pi H(g)<=5(d_X+Jrem)+pi H(g)+(e/2)I(g).

The separate 3mu/ln2 allowance costs at most (3/ln2)(d_X+Jrem). Consequently H(g)<=C0 I(g) implies H(F)<=max(5+2/ln2,C0+1)I(F). The source balanced bent-surgery terminal has H/I<3 uniformly in even k>=4, so all its claimed 8,5,10 constants follow. These are source conclusions accepted without altering their hypotheses.

**Quantitative credit insufficiency in the same retained-terminal interface.** Fix L=R=T=1 and g_k=z*b_k, k even>=2. Then pi=7/16, eta=1/8, H(g_k)=k, I(g_k)=1+k/2. Every control posterior and minority-KL term is constant under bent spectral replication. At the root, posterior J_X, complete D2(nu||Q), and its weighted credit mu D2(nu||Q) are all strictly positive; mu=1/4. Their exact prime-log vectors and positive rational enclosures are in out/CREDIT_FIXTURE.json. Each named credit C obeys the exact ratio

    C/[pi H(g_k)]=(16 C/7)/k = Theta(1/k).

Also H(F_k)=H(F_dictator)+(7/16)k and I(F_k)=3/4+(7/16)(1+k/2), so H/I tends to 2. This closes the required asymptotic test for the named positive credits without mistaking it for a FEI disproof or asserting that total correlation is small.

First unsupported universal line: the sum of marked reserves at arbitrary overlapping separator ancestors is bounded per actual physical coordinate, and all arbitrary terminal entropy is paid. The theorem audited here spends its controller reserve once; it proves no renewal rule.

# executed validation with domain, arithmetic, commands and outputs

out/FROZEN_SPEC.json preceded the search. The domain is exactly 27 dictator-core roots L,R,T in {1,2,3}, 16 balanced quadratic-bent roots with widths in {1,2}, k in {2,4}, and eight balanced bent4/zero-flip selector roots with widths in {1,2}: 51 actual Boolean roots. No symmetry reduction or dimension increase. Largest actual dimension is 13, below the frozen ceiling 14. Estimated memory 100 MB; peak not measured; no >300 MB job or memok requirement arose.

Commands from A040:

    python -X utf8 runs/20261014T003941Z-fleet05-A040-credit-insufficiency-tests/code/review.py pilot
    python -X utf8 runs/20261014T003941Z-fleet05-A040-credit-insufficiency-tests/code/review.py
    python -X utf8 runs/20261014T003941Z-fleet05-A040-credit-insufficiency-tests/code/review.py resume
    python -X utf8 runs/20261014T003941Z-fleet05-A040-credit-insufficiency-tests/code/credit_fixture.py
    python -X utf8 runs/20261014T003941Z-fleet05-A040-credit-insufficiency-tests/code/finalize.py

Pilot: one root, 120 checks, 1.248474 seconds, PASS. First full job reached its 55-second between-case guard after saving all 27 dictator cases and 15,459 assertions, with no mathematical assertion failure. FIRST_BATCH.json preserves that exact prefix. SPEC_AMENDMENT.md freezes continuation of the unchanged domain in bounded sequential batches. Caching repeated rational entropy atoms is the performance change. The continuation completed all 51 roots and 20,734 assertions in 43.4666302 seconds. Additional fixed-fixture extraction: 24 assertions, 0.0309466 seconds, PASS. Root control erasure/posterior homogeneity, all queried and terminal entropy/influence accounts, exact compensated TC identity, complete minority-KL inequalities, odd-face partition, physical disjoint boundaries and exact reserve slack are checked. All finite separator roots happen to be good; no all-width goodness extrapolation is used.

Arithmetic: direct integer sign tables, integer Walsh transform independently compared to physical flip counts, Fraction influences and face prices, exact prime-log vectors for equality and rational atanh-series logarithm intervals for signs. Truncation tail is bounded explicitly; compact saved endpoints are rounded outward. No float sign decision, random sample, imported author executable, GPU or background job. A preliminary cmd-shell quoting failure executed no mathematics; the working PowerShell commands above are reproducible. Finite cases corroborate the separate all-width proof; they do not replace it.

# proof dependencies and changed downstream conclusions

This independently reconstructs balance transfer, boundary ownership, descendant goodness, cube isoperimetry, binary erasure/JS bounds, retained terminal and the source specialization. No universal FEI or arbitrary-depth potential is assumed. CLAIMS.json preserves A023@2's exact statement, hypotheses, authors and original statement digest, appending a scoped review with no repair. A040's additional asymptotic fixture is a source-bound interface test, not a third broad unreviewed candidate.

A021/A023/A029/A064/B08/B20 may now consume an independent acceptance of the one-use reserve, with exactly the terminal hypothesis shown. A046 should use the exhausted controller reserve and terminal slack eta I(g) as boundary conditions for its multi-bit test. The positive-posterior ratio provides a stricter diagnostic than KL nonnegativity: omitting the terminal bill loses linear entropy despite fixed positive credits. Shared registries and other agents were not modified.

# one next mathematical action and independent reviewer

Consume A046's source-versioned multi-layer calculation and check the sum of actual per-coordinate debits against these exhausted control capacities and residual core slack, retaining terminal CE/entropy. A087/A094 can independently challenge this separator review; A088 can review the exact credit-replication corollary. Handoffs are saved here only; no tool message was sent. Do not repeat the finite controller-order or minimum-erasure censuses.

# actual persistence receipts or precise save blocker

Saved locally: REPORT, CLAIMS, PROGRESS, byte-identical PACKET_DELTA, REVIEW_A023, code, frozen spec and amendment, prefix checkpoint, final exact results, credit fixture, source hashes, schema readback and artifact SHA256 receipts. Rolling STATUS has exactly two lines, WORKLOG is appended and LEARNED preserves prior facts. out/SCHEMA_CHECK.json and out/ARTIFACT_RECEIPTS.json certify local readback; every file is under 20 MB. No local blocker. Supervisor copying, shared-registry adoption, remote mirroring, independent review of this review and actual downstream use are unverified.

## Universal bridge

This stage moves C019 stopping-tree payment by independently closing the single-separator reserve slice of A023@2, including Q_bad<=I-d_X and all terminal costs, without improving the universal constant. It also proves exact Theta(1/k) insufficiency of three strictly positive named posterior/minority-KL credits relative to retained terminal entropy, while H/I tends to 2. What remains is bounded ancestral reserve ownership and a universal terminal certificate. NEXT consumes A046's distinct layered transport rather than duplicating it: checking its debits against the now-audited exhausted control reserve is the shortest route toward universal payment because it tests the precise first unsupported line.
'''
(ROOT/'REPORT.md').write_text(report,encoding='utf-8')
progress={
'protocol_revision':protocol['revision'],'run_id':ROOT.name,'stream':'B08','packet_id':'A040','gap_id':'C019-SINGLE-RESERVE-ANCESTRAL-OWNERSHIP','attempt_id':'A040-stage3-separator-independent-review',
'method':'Independent physical-edge/Walsh reconstruction and all-width proof; exact fixed-controller bent-replication KL insufficiency test',
'mathematical_delta':'A023 overlap @2 separator slice independently HOLDS, no repair: Q_bad<=I-d_X with terminal retained. Root posterior, complete minority KL and weighted credit are fixed positive constants with exact Theta(1/k) ratios to retained terminal entropy on an actual Boolean bent-core family; H/I->2.',
'deliverable_status':'COMPLETE_LOCAL_SAVED','mathematical_status':'SCOPED_REVIEW_HOLDS_AND_ASYMPTOTIC_TEST_PROVED; FULL_FEI_OPEN',
'claim_versions_used':[{'claim_id':claim['claim_id'],'version':2,'statement_sha256':claim['statement_sha256'],'scope':'Added separator extension independently reconstructed'}],
'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':2,'change':'Local scoped independent review appended; original source unchanged'}],
'source_artifacts':[str(p) for p in sources]+[str(ROOT/'REVIEW_A023.md'),str(ROOT/'out/RESULTS.json'),str(ROOT/'out/CREDIT_FIXTURE.json')],
'next_consumers':['A023','A046','A087','A094','A088','B08','B20'],
'next_action':'Consume A046 layered reserve output; check exact per-coordinate cumulative debits and retained terminal against the audited one-use reserve and residual eta I(g).',
'stagnant_substantive_attempts':0,'blockers':['No local save blocker; arbitrary-depth ownership and arbitrary-terminal payment remain mathematical gaps.'],'packet_ids':['A040']}
expected={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
assert set(progress)==expected
save(ROOT/'PROGRESS.json',progress);(ROOT/'PACKET_DELTA.json').write_bytes((ROOT/'PROGRESS.json').read_bytes())
(HOME/'STATUS.md').write_text('STATE: A040 stage 3 complete: A023 overlap v2 single reserve independently HOLDS; 51 roots/20,734 exact checks plus 24 credit checks PASS; positive root KL/posterior ratios Theta(1/k); full FEI OPEN.\nNEXT: Consume A046 multi-layer reserve calculation; audit per-coordinate debits against exhausted control reserve and eta I(g) terminal slack; A087/A094 review, A088 credit corollary.\n',encoding='utf-8')
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (HOME/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write('\n## '+stamp+' — stage 20261014T003941Z\nConsumed new A098 dispatch (A040 single-reserve review; A046 multi-bit transport). A023@2 separator theorem reconstructed without repair. Frozen 51-root domain: pilot120 PASS; 55-second guard saved27 roots/15459 checks; cached/checkpoint continuation completed51/20734 PASS (43.47s). Additional fixed fixture24 PASS: root posterior and complete minority KL credits positive and independent of bent dimension, exact ratios (16/7)C/k to terminal entropy. H/I tends to2. No broad candidate; no universal reserve renewal. All writes restricted to A040.\n')
with (HOME/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\n## Stage 3: independent separator acceptance and fixed-credit ratio\nFor balanced core g and A=X(U OR V) OR WUV on independent point blocks, the two child controllers have disjoint boundary edges, J(D)=2Jrem. Exact root face Jrem+(e/2)I(g) uses every remaining-controller one-unit reserve and leaves eta I(g) core slack. Descendants are 4-good in every width. A023@2 single-separator extension independently HOLDS; renewal across ancestors remains unproved. For L=R=T=1 and g_k=z*b_k (even quadratic bent), pi=7/16, eta=1/8; root posterior, full minority D and mu D are strictly positive constants (mu=1/4), each over retained terminal entropy equals (16/7)C/k. H(F_k)=H(F_dictator)+7k/16, I(F_k)=3/4+(7/16)(1+k/2), H/I->2. Never infer total-correlation insufficiency from this particular test. Runtime checkpoints preserve completed cases; resume the same domain rather than increase dimensions.\n')
assert len((HOME/'STATUS.md').read_text().splitlines())==2
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
for heading in protocol['required_per_run']['report_fields']:assert '# '+heading in report
files=[p for p in ROOT.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.name not in ['ARTIFACT_RECEIPTS.json','SCHEMA_CHECK.json']]
assert all(p.stat().st_size<20*1024*1024 for p in files)
save(ROOT/'out/SCHEMA_CHECK.json',{'status':'PASS','claim_fields_exact':True,'progress_fields_exact':True,'packet_delta_identical':True,'required_report_fields':True,'status_two_lines':True,'roots':51,'exact_checks':20734,'credit_checks':24,'pilot_checks':120,'files_under_20MB':True,'remote_mirror_verified':False})
files.append(ROOT/'out/SCHEMA_CHECK.json')
save(ROOT/'out/ARTIFACT_RECEIPTS.json',[{'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(files)]+[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)} for p in [HOME/'STATUS.md',HOME/'WORKLOG.md',HOME/'LEARNED.md']])
for key in ['posterior','minor_KL_credit','minor_KL_divergence']:
 lo=fixture[key]['lower'];print(key,lo)
print(json.dumps({'status':'SAVED_AND_SCHEMA_PASS','roots':51,'exact_checks':20734,'credit_checks':24,'local_artifacts':len(files),'independent_review':'HOLDS_SEPARATOR_EXTENSION_ONLY'}))
