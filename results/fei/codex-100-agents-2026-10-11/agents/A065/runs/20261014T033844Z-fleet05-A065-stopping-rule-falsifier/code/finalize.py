from pathlib import Path
import json,hashlib,datetime
ROOT=Path(__file__).resolve().parents[1]
AGENT=ROOT.parents[1]
RUN=ROOT.name
CAMPAIGN=Path(r'~\mop_fei100\reports\fei-2026-10-11')
protocol=json.loads((CAMPAIGN/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
validation=json.loads((ROOT/'out'/'VALIDATION.json').read_text())
replay=json.loads((ROOT/'out'/'REPLAY.json').read_text())
pilot=json.loads((ROOT/'out'/'PILOT.json').read_text())
total=validation['assertions']+replay['assertions']
next_action='Test the first non-point overlapping controller query after partial core exposure using A064 actual child continuations, inherited complete core reserves and one exclusive influence owner; freeze the small controller/core domain first.'
paths=[CAMPAIGN/'EXECUTION_PROTOCOL.json',Path(r'~\brain_workers\FEI100_20261011\BOARD.md'),Path(r'~\brain_workers\FEI100_20261011\claude\B13\STREAM_NOTES.md'),AGENT/'STATUS.md',AGENT/'runs'/'20261011T230426Z-fleet05-A065-stopping-rule-falsifier'/'RESERVE_AND_PREFIX_THEOREM.md',AGENT/'runs'/'20261011T230426Z-fleet05-A065-stopping-rule-falsifier'/'out'/'validation.json',AGENT/'runs'/'20261011T230426Z-fleet05-A065-stopping-rule-falsifier'/'out'/'PREFIX_VALIDATION.json',Path(r'~\brain_workers\FEI100_20261011\agents\A062\runs\20261014T015800Z-fleet05-A062-influence-compensator\REPORT.md'),Path(r'~\brain_workers\FEI100_20261011\agents\A064\runs\20261014T030103Z-fleet05-A064-global-debt-potential\REPORT.md')]
source_receipts=[{'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size,'scope':'read as source or recovered exact certificate; no acceptance imported'} for p in paths]
(ROOT/'out'/'SOURCE_RECEIPTS.json').write_text(json.dumps(source_receipts,indent=2)+'\n')
statement=('For the 15 explicitly defined Boolean families B05(k=2,4,6;r=2k) and AND of two bent point-splice negative events at (k,l)=(2,2),(2,4),(4,4), with independent/shared physical selectors and r=0,2 point controls, the prescribed greedy-min-D/Inf and control-first complete restriction trees have exact least nonnegative reserve Q*_root=0 at C=32609/5000. Greedy has Q*_root=0 at C=4 on all 12 AND fixtures. B05 k=6 selector-first has 0.0043362252<=Q*_root/I<=0.0043362253 at C=32609/5000 and 0.0026621595<=Q*_root/I<=0.0026621596 at C=8. Independent-selector AND(4,4),r=0 has selector-first 0.0093929846<=Q*_root/I<=0.0093929847 at C=8. The remaining 225 reserve intervals are exactly those in out/VALIDATION.json, certified using actual activation coefficient multiplicities and checked against 60 raw Boolean AND rule trees.')
claim={'claim_id':'A065-FIVE-RULE-COMPRESSED-STRESS','version':1,'exact_statement':statement,'hypotheses':['Finite listed parameter domains only','Boolean signs on uniform physical cubes; entropy in bits; ordinary influence','Bent b_k=(-1)^(x0*x1+...); splice b_k^selector flips only x=0 on selector=1','AND means conjunction of the two negative-output events','Fresh point controls except explicitly shared selector','Rules and least original-coordinate tie breaking defined in code/compressed.py','Q*_leaf=0 at actual constant leaves'],'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['fleet05/A065'],'proof_source':{'run_id':RUN,'paths':['PROOF.md','code/compressed.py','code/kernel.py','code/replay.py','out/VALIDATION.json','out/REPLAY.json']},'proof_dependencies':[],'review_records':[],'status':'AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':['Hypothetical universal zero-reserve assertion for selector-first at C=8 on the tested AND-splice class'],'first_unproved_line':None,'next_consumers':['A064','A062','A087','A094','B13','B20']}
(ROOT/'CLAIMS.json').write_text(json.dumps([claim],indent=2)+'\n')
progress={'protocol_revision':protocol['revision'],'run_id':RUN,'stream':'B13','packet_id':'A065','gap_id':'C019-OWNED-CONTROLLER-CHILD-RESERVE','attempt_id':'A065-compressed-k6-and-splice-v2','method':'Exact activation-multiplicity state quotient, integer Walsh/direct-edge arithmetic, rational logarithm intervals, full raw-polynomial Boolean replay','mathematical_delta':'225 exact reserve enclosures; B05 k6 control/greedy zero at 32609/5000 versus positive selector/min reserve; all12 AND fixtures greedy zero at4; shared-selector zero/positive differences; earlier incomplete packet results recovered without rewriting legacy runs','deliverable_status':'COMPLETE_LOCAL_ARTIFACT','mathematical_status':'FINITE_SCOPED_CERTIFICATES_PROVED_UNREVIEWED; FULL_FEI_OPEN','claim_versions_used':[],'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1}],'source_artifacts':['PROOF.md','out/VALIDATION.json','out/REPLAY.json','out/PILOT.json','out/SOURCE_RECEIPTS.json','../20261011T230426Z-fleet05-A065-stopping-rule-falsifier/out/validation.json','../20261011T230426Z-fleet05-A065-stopping-rule-falsifier/out/PREFIX_VALIDATION.json'],'next_consumers':['A064','A062','A087','A094','B13','B20'],'next_action':next_action,'stagnant_substantive_attempts':0,'blockers':['Universal inherited child-reserve payment remains unproved','Independent review and supervisor mirror/adoption pending','Prior legacy runs lacked required protocol files; preserved without retroactive completion claims'],'packet_ids':['A065']}
for name in ['PROGRESS.json','PACKET_DELTA.json']:(ROOT/name).write_text(json.dumps(progress,indent=2)+'\n')
def fmt(pair):return '0' if pair==[0.0,0.0] else f'[{pair[0]:.10f}, {pair[1]:.10f}]'
table=['| B05 k=6 rule | Q*/I, C=4 | C=6.5218 | C=8 |','|---|---:|---:|---:|']
for row in validation['cases']:
    if row['family']=='B05-k6':table.append('| '+row['rule']+' | '+' | '.join(fmt(x) for x in row['Q_over_I'])+' |')
report=f'''# exact target, quantifiers, hypotheses and units

A065 / B13 current stage {RUN}. Complete the lead v2 stopping-rule test on B05 k=6 and AND-of-bent point splices, while retaining actual terminal costs. For each listed actual Boolean family and each of five fair physical query rules, certify the least nonnegative reserve Q*_v=max(0,D_v-Cd_v+average Q*_children), with constant leaves zero, at C=4,32609/5000,8. Entropy in bits; d is ordinary physical influence. Quantifiers are ONLY the fifteen frozen families and seventy-five complete policies. No all-dimensional greedy rule theorem is claimed.

# sources actually read, revisions and theorem locators

Read BOARD.md snapshot 2026-10-14 03:35 UTC, B13 STREAM_NOTES.md v2 (2026-10-11 23:1xZ), and the existing STATUS.md before work. The exact protocol schema remains 2026-10-11-execution-v2; its report/progress/claim fields are checked by the finishing script. The lead explicitly requests B05 k6 control-first/greedy and AND-splice tests, rather than whole-path debt. Recovered original A065 v1 integer/interval outputs, prefix outputs and RESERVE_AND_PREFIX_THEOREM.md are pinned in source receipts. Those prior runs have no REPORT/CLAIMS/PROGRESS; they are preserved as legacy partial artifacts, without fabricating completion receipts.

Read A062 stage4 REPORT, arbitrary fixed-core complete-reserve preservation and fixed-core limit guard; A064 stage4 REPORT, repeated-fallback point-priority reserve and first unsupported overlapping/non-point continuation. These are consumed for target selection, not accepted as premises for this certificate. The stage's activation algebra is reconstructed completely in PROOF.md. Earlier source receipts identify supplied threshold Proposition8.9/Corollary8.10, percolation local-guard scope and archived B05 Sections2--7. No new literature/novelty assertion is made. Exact byte hashes are out/SOURCE_RECEIPTS.json.

# complete derivation or exact first unsupported line

PROOF.md gives the actual Fourier coefficient multiplicities, including the coherent constant coefficient; exact physical core/control children and influences; greedy exact-tie certification; and rigorous interval induction of Q*. Exchangeable live controls are a proved physical symmetry, while core variables retain their actual original labels. The model retains every selector and shared-selector coordinate. It neither replaces Boolean children by real vectors nor restarts a core entropy account.

At C=32609/5000, greedy and control-first have exact Q*=0 for all15 fixtures. At C=4, greedy has exact Q*=0 on all12 AND fixtures. B05 k6 has H/I in [3.7381271477,3.7381271478], I=883/262144; its selector-first positive reserve therefore reflects lost earlier credit, not a failed root FEI bound.

{chr(10).join(table)}

Independent-selector AND(4,4), r=0: selector-first Q*/I at C=6.5218 lies in [0.0493443360,0.0493443361], and at C=8 in [0.0093929846,0.0093929847], although greedy/control-first need zero even at C=4. One shared selector reduces the C=6.5218 selector-first reserve to [0.0271262190,0.0271262191] and gives zero at C=8. Thus shared physical selection changes the full bill; two independent selector budgets cannot be blindly added. All further rows are in the exact output.

First unsupported universal line: a dimension-independent bound on inherited complete child reserves at a non-point overlapping controller reveal during unfinished core exposure, financed from one unspent physical account. These finite zeros do not establish universal greedy success or a universally paid root reserve. The prior addressing prefix witness still has unpaid stopped cost at least a-C with queried influence1 and retained terminal influence a/2; that legacy obstruction is not relabeled as a new result.

# executed validation with domain, arithmetic, commands and outputs

Frozen out/FROZEN_SPEC.json preceded the primary search. Maximum physical dimension19, maximum compressed core truth-table size1024, estimated memory90MB, maximum runtime1500s. Pilot calibrated all256 three-bit cores at s=0,1,2 against raw actual spectra:768 cases, plus10 prior five-rule B05 k2/k4 comparisons. Pilot passed {pilot['assertions']} assertions in {pilot['elapsed_seconds']:.6f}s, below60s. Primary command: python -X utf8 code/compressed.py. It completed75 rule trees,225 reserve intervals, {validation['assertions']} assertions in {validation['elapsed_seconds']:.6f}s. Both commands were run from this run directory by their full local relative paths; executable main is code/compressed.py.

Separate out/REPLAY_FROZEN_SPEC.json preceded raw replay. Direct polynomial Boolean constructor, full truth tables, all12 AND fixtures, all5 rules, maximum dimension12, estimated memory200MB. Pilot passed917 assertions on10 raw trees in0.089857s. Full command: python -X utf8 code/replay.py;60 raw trees,180 reserve comparisons, {replay['assertions']} assertions in {replay['elapsed_seconds']:.6f}s. Same logarithm kernel and contributor, different Boolean constructor/spectrum/tree representation: this is self-validation, not independent external acceptance.

Primary plus raw replay totals {total} assertions; pilots excluded. Integer Walsh, direct edge counts and Fraction arithmetic verify spectra/influences;28-term rational atanh bounds with proved remainder and outward2^-70 rounding certify entropies, greedy ordering and reserve signs. Displayed decimals do not choose signs. Jobs were sequential, below300MB admission trigger, below30-minute cap, no GPU or automatic dimension escalation. No memok admission was required by these frozen estimates. Saved outputs include exact scaled integer endpoints and every visited nonconstant state.

# proof dependencies and changed downstream conclusions

The finite claims are self-contained actual Boolean expansion and finite backward induction; no unreviewed universal theorem is assumed. Prior A065 outputs provide cross-calibration only. A062/A064 latest reports guide the remaining ownership target. The lead's k4 floating calibration has been recovered as exact intervals and extended to k6; AND/shared-selector rule stress tests now have raw Boolean reproduction. Selector/min-influence local zero-payment is refuted on these examples; whole-path FEI is not. One scoped finite-certificate claim is submitted for A087/A094 review, without opening a new broad universal candidate.

# one next mathematical action and independent reviewer

{next_action} A087/A094 should audit the activation quotient, coherent empty coefficient, exact greedy ties and raw replay before adoption. This follows A062/A064's live mixed-history boundary rather than raising the independent bent dimension again.

# actual persistence receipts or precise save blocker

Saved locally: REPORT.md, CLAIMS.json, PROGRESS.json, compatible PACKET_DELTA.json, PROOF.md, executable helpers, two frozen specifications, pilots, primary and raw outputs, source receipts, and schema/hash receipts. STATUS.md is exactly two lines; WORKLOG.md is appended with the current stage; LEARNED.md records durable results and limits. Prior partial runs are untouched. Supervisor copy, remote mirrors, independent acceptance and downstream adoption remain unverified.

**Universal bridge:** C019 stopping-tree payment advances by225 certified reserve values, including a19-variable B05 k6 certificate and twelve actual AND/shared-selector fixtures: greedy/control-first eliminate the complete nonnegative bill at6.5218 throughout this finite domain, while selector-first retains strictly positive bills even at8. The actual Boolean compressed interface now supports mixed physical query orders without erasing terminal/core debt. Universal inherited child-reserve payment and non-point overlapping controller transfer remain open. NEXT targets that first unpaid mixed-history controller update with one physical owner, which is the shortest route from these controls to the universal payment gap rather than another isolated entropy-class result.
'''
(ROOT/'REPORT.md').write_text(report,encoding='utf-8')
(AGENT/'STATUS.md').write_text('STATE: A065 current stage complete:225 exact reserves, B05 k6 and12 AND/shared-selector fixtures,60 raw replays;54,431 assertions PASS; review pending; FEI OPEN.\nNEXT: Price the first non-point overlapping controller query during partial core exposure with actual child continuations, inherited complete reserves and one physical owner.\n',encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(f'\n2026-10-14 stage {RUN}: read board03:35 and B13v2; recovered incomplete legacy v1 outputs without rewriting them. Derived exact activation quotient;768 small-core calibrations and10 v1 comparisons;75 physical policies/225 intervals plus60 raw-polynomial AND replay trees; {total} main assertions PASS. B05k6 greedy/control Q=0 at6.5218, selector Q/I in[0.0043362252,0.0043362253]. All12 AND greedy Q=0 at4; independent AND4,4 selector still positive at8. No universal or unbounded-ratio claim. Saved four protocol files and exact endpoints. NEXT is overlapping/non-point mixed-history inherited-child payment.\n')
learned='''# Durable A065 facts

Q*_v=max(0,D_v-Cd_v+average Q*_children), constant leaves0, is the least nonnegative reserve for a prescribed complete physical tree. Total complete-path debt is always H-CI and cannot diagnose a bad rule without an FEI counterexample. Keep the actual terminal influence and entropy on stopping prefixes.

Addressing data-first has exclusive queried influence1 and expected unpaid stopped-prefix cost>=a-C; terminal expected influence is a/2. This invalidates prefix-only financing, not root-influence financing. Rare activation and parity-paired address masks retain that terminal debt; a coded mask phase has zero entropy drop but spends a/2 influence.

For point activation1+A_s(g-1), exact Fourier numerator families are w_T, repeated2^s for nonemptyT; w0-N, repeated2^s-1; and L+w0-N at the coherent empty coefficient, denominatorL=N2^s. Core queries commute with activation; each control query has actual children+1 and the same core with s-1 controls. Exchangeable controls can be compressed without losing physical query order or influence.

Stage20261014T033844Z:225 exact reserve intervals on15 fixed families;54,431 main assertions including60 raw Boolean replay trees. B05k6 I=883/262144,H/I in[3.7381271477,3.7381271478]. At C=6.5218 greedy/control/max needQ=0, selector/min Q/I in[0.0043362252,0.0043362253]; selector/min still positive at8. All12 AND splice fixtures greedyQ=0 at4. Independent-selector AND4,4,r0 selectorQ/I in[0.0093929846,0.0093929847] at8; shared-selector counterpart is0 at8. Finite zero reserves do not imply all-dimensional greedy success.

Greedy overlapping ratio intervals are ties only after exact prime-log-vector equality. Reuse the rigorous interval kernel; raw polynomial replay checks the compressed representation but shares the kernel and author, so it does not replace external review.

Current frontier: actual non-point/overlapping controller reveal during partial core exposure, with both child continuation reserves and one unused physical influence account. A062 fixed-core preservation and A064 point-priority payment identify this unpaid ownership step. Do not re-run larger independent bent controls without a new hypothesis or objection.
'''
(AGENT/'LEARNED.md').write_text(learned,encoding='utf-8')
fields=protocol['required_per_run']
assert set(claim)==set(fields['claim_fields'])
expected=[x.split(' (')[0] for x in fields['progress_fields']]
assert set(progress)==set(expected)
for heading in fields['report_fields']:assert ('# '+heading) in report
assert len((AGENT/'STATUS.md').read_text().splitlines())==2
assert len(validation['cases'])==75 and len(replay['rows'])==60
for x in validation['cases']:
    if x['rule'] in ['greedy-min-D-over-d','control-first']:assert x['Q_scaled'][1]==[0,0]
    if x['family'].startswith('AND-') and x['rule']=='greedy-min-D-over-d':assert x['Q_scaled'][0]==[0,0]
receipts=[{'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size} for p in ROOT.rglob('*') if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json']
assert all(r['bytes']<20*1024*1024 for r in receipts)
(ROOT/'out'/'SCHEMA_CHECK.json').write_text(json.dumps({'claims_fields_exact':True,'progress_fields_exact':True,'packet_delta_identical':(ROOT/'PACKET_DELTA.json').read_bytes()==(ROOT/'PROGRESS.json').read_bytes(),'required_report_fields_present':True,'STATUS_two_lines':True,'all_files_under_20MB':True,'assertions_primary_plus_replay':total,'external_review_pending':True},indent=2)+'\n')
(ROOT/'out'/'PERSISTENCE_RECEIPTS.json').write_text(json.dumps({'run':RUN,'scope':'local-only, no mirror/adoption receipt','files':receipts},indent=2)+'\n')
print('FINALIZED',RUN,'main assertions',total,'file receipts',len(receipts))
