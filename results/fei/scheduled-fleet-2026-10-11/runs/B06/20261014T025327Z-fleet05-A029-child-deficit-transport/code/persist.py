import copy,datetime,hashlib,json
from pathlib import Path
RUN=Path(__file__).resolve().parents[1];AGENT=RUN.parents[1];TEAM=AGENT.parents[1]
PROTOCOL=Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
SRC=TEAM/'agents/A023/runs/20261014T022245Z-fleet05-A023-amortized-rarity-budget'
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
def dump(p,v):p.write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
protocol=json.loads(PROTOCOL.read_text(encoding='utf-8'))
checks=json.loads((RUN/'out/checks.json').read_text());group=json.loads((RUN/'out/grouping.json').read_text())
assert checks['status']==group['status']=='PASS'
assert checks['pair_cases']==768 and checks['triple_cases']==16384 and group['cases']==4080
sourceclaims=json.loads((SRC/'CLAIMS.json').read_text())
c=copy.deepcopy(next(c for c in sourceclaims if c['claim_id']=='A023-OVERLAP-EXPOSURE-GOOD-CONTROL-LEDGER'))
assert c['version']==3 and c['statement_sha256']=='32444a38f9d32b7d226f04c6322d4a7ea0a271e808d5a3e5da35cdef76e5605c'
c['review_records'].append({'reviewer':'fleet05/A029','source':str(RUN/'REVIEW_A023.md'),'verdict':'HOLDS_WHOLE_POINT_BLOCK_CLAUSE_ONLY','scope':'All-dimensional arbitrary-shared-data whole-block erasure, entropy, genuine-minority/full allowances, explicit terminal-coordinate owners and certified-child-rate consequence','excluded':'Earlier overlap/separator clauses, unconditional bent-edit/activation application, source computation receipts and whole bundled acceptance','repair_supplied':False,'validation':'768 ordered shared-core pairs,16384 nested triples,248751 exact assertions; separate grouping checker4080 cases28816 assertions'})
c['status']='INDEPENDENT_SCOPED_ACCEPTANCE_WHOLE_BLOCK_ONLY_OTHER_CLAUSES_PENDING'
dump(RUN/'CLAIMS.json',[c])
used=[{'claim_id':c['claim_id'],'version':3,'statement_sha256':c['statement_sha256'],'status':'INDEPENDENTLY_RECONSTRUCTED_WHOLE_BLOCK_CLAUSE_ONLY'}, {'claim_id':'B06-R2','version':'STREAM_NOTES v2,2026-10-11 23:26Z','status':'ACCEPTED_BASELINE_NOT_REPROVED'}]
nextaction='At three genuinely distinct shared cores, prove or refute payment of the exact hierarchical surcharge from unused signed terminal deficits after future-control debit; preserve original terminal weights. A023/A087/A094 review DERIVATION.'
progress={'protocol_revision':protocol['revision'],'run_id':RUN.name,'stream':'B06','packet_id':'A029','gap_id':'G-R-MISMATCH','attempt_id':'A029-child-deficit-transport-04','method':'Independent source-bound A023 whole-block review; exact nested physical-child owner accounting and grouped-event refund','mathematical_delta':'A023@3 whole-block scoped HOLDS; two-level signed condition keeps all3 core deficits; exact data surcharge2a(1-a)b(1-b)I12 and future-control debit; grouping refund pays both redundancy parts on constant-failure chains;248751+28816 exact assertions PASS','deliverable_status':'COMPLETE_LOCAL_SAVED','mathematical_status':'DEPENDENCY_SCOPED_REVIEW_HOLDS_NESTED_APPLICATION_CHECKED_UNIVERSAL_PAYMENT_OPEN','claim_versions_used':used,'claims_created_or_changed':[{'claim_id':c['claim_id'],'version':3,'change':'LOCAL_SOURCE_BOUND_SCOPED_REVIEW_RECORD_ONLY_NO_SHARED_MODIFICATION'}],'source_artifacts':['REPORT.md','DERIVATION.md','REVIEW_A023.md','SPEC.json','VERIFY_SPEC.json','code/check.py','code/verify_grouping.py','out/checks.json','out/grouping.json','out/chains.json'],'next_consumers':['A023','A027','A028','A030','A064','A087','A094','B06 lead','B20'],'next_action':nextaction,'stagnant_substantive_attempts':0,'blockers':['Symmetric pairwise R_star has not been proved to pay actual nested entropy; hierarchy surcharge and future-control debit cannot be deleted','General terminal-core deficit certificate remains unproved','Independent review of new nested application and remote copying/adoption unverified'],'packet_ids':['A029']}
dump(RUN/'PROGRESS.json',progress);dump(RUN/'PACKET_DELTA.json',progress)
report=f'''# exact target, quantifiers, hypotheses and units

A029/B06 stage4, run {RUN.name}. Review the new dependency A023-OVERLAP-EXPOSURE-GOOD-CONTROL-LEDGER@3 at its arbitrary-shared-data whole-point-block clause ONLY, then apply it to the first nested physical-child split. All signs Boolean, every cube uniform, entropy bits, influence ordinary. Fresh disjoint point blocks A,B have arbitrary positive widths r,s and probabilities a=2^-r,b=2^-s. Three arbitrary core signs g0,g1,g2 share every data coordinate if desired. Let h=g1+B(g2-g1), f=g0+A(h-g0); query controls to resolution and retain terminals g0,g1,g2 with weights pi=(1-a,a(1-b),ab). No balance, density, disjoint-core or terminal FEI hypothesis is assumed for the signed condition.

This stage independently reviews an existing dependency rather than opening another broad candidate while earlier A029 claims await review. The lead's old unrestricted gain target was already refuted in stage3; its depth-two and quadratic scopes survive. We retire further gain searches and consume the paid-block dependency under the protocol dispatch order. This differs from the stale lead NEXT by using its already-broken target honestly; no claim of a new gain theorem is made.

# sources actually read, revisions and theorem locators

Read BOARD.md supervisor snapshot2026-10-14 02:43UTC, B06 STREAM_NOTES.md v2 2026-10-11 23:26Z, own STATUS.md, complete EXECUTION_PROTOCOL.json revision {protocol['revision']}. Read A023 LEARNED.md, current run REPORT.md, full PROOF.md and CLAIMS.json; source locator is PROOF sections Exact sector ownership, Boundary reserve, Full entropy. Read A024 LEARNED.md signed outer residual; A097 LEARNED.md current padded-bank/terminal ownership; own stage3 claim and checker/persistence fragments. These context reads supply direction, not mathematical premises. A025's old multi-bit face no-go is known via A023's source report; its original current proof was NOT independently reviewed this stage. No new literature, brain, web or remote premise used.

Current-source SHA256 receipts are SOURCE_RECEIPTS.json. The read BOARD snapshot is copied locally; source indices and other agents' folders remain read-only. Earlier campaign source reads from prior stages are not claimed as fresh rereads.

# complete derivation or exact first unsupported line

DERIVATION.md and REVIEW_A023.md are the complete analytic records. A023's whole-block erasure, entropy, genuine-minority/full allowance, coordinate owner and certified-child-rate clauses HOLDS after independent reconstruction. Earlier overlap/separator clauses, unconditional bent-edit/activation family and the entire bundled claim are explicitly excluded from acceptance. Direct character sums differ from the source's FWHT implementation; no source repair is supplied.

Put Iij=I(gi gj), I_B=2s b P(g1!=g2), I_A=2r a[(1-b)P(g0!=g1)+bP(g0!=g2)]. Actual removed influence is I_ctrl=I_A+a I_B. The two source reserves have exact data and future-control parts:

    R_data=2a(1-a)[(1-b)I01+b I02]+2ab(1-b)I12,
    R_controls=2a(1-a)I_B.

For every real price K, both complete physical children and their descendants are retained in the sufficient bound

    D_K(f)>=sum pi_j D_K(gj)+(K-11/2)I_ctrl-R_data-R_controls.

Its right side being nonnegative is sufficient; clipping a negative terminal deficit is invalid. The per-data-coordinate owner coefficients against original terminal capacities are2a,2(1-a+b),2(2-a-b). Thus certified terminal rates Cj give the concrete finite nested rate max(11/2+2(1-a),C0+2a,C1+2(1-a+b),C2+2(2-a-b)). This is an application of a reviewed source bound, not exact equality of entropy costs or universal FEI.

The symmetric terminal-pair functional R_star=2 sum_{{i<j}}pi_i pi_j Iij fits two terminal rate units, but exact expansion gives R_data-R_star=2a(1-a)b(1-b)I12. This exposes the inherited surcharge without dropping future controls. FIRST UNSUPPORTED LINE: replace R_data by R_star in the actual entropy payment, or charge the surcharge to already-spent terminal deficits. No claim that the symmetric functional pays entropy is made.

The all-depth grouped-event diagnostic keeps actual entropy and influence at every leaf: for f=1+A1...Ad(g-1), widths t_j, probabilities a_j, p=product a_j, e=1-Eg, split data reserve is2p I(g)sum(1-a_j); future-control reserve is2p e sum_j(1-a_j)sum_{{k>j}}t_k. Folding the SAME physical point event into one block uses only2p(1-p)I(g) and removes the exact redundancy of both parts. For d fair bits the split quantities are d p I(g) and p e d(d-1)/2. Full terminal accounts pH(g),pI(g) remain. This refines the existing nonreuse obstruction into an explicit refund when all failures are the same constant; it does not solve three-distinct-core ownership.

# executed validation with domain, arithmetic, commands and outputs

SPEC.json and VERIFY_SPEC.json were frozen before their respective jobs. No symmetry reduction, sampling, automatic dimension increase, GPU or background process. Primary memory estimate160MB, boundary checker15MB; no job expected to exceed300MB, so the memok gate was not applicable. One job at a time. Primary maxruntime180seconds; observed {checks['seconds']:.6f}seconds. Independent grouping max60seconds; observed {group['seconds']:.6f}seconds.

Commands: `python -X utf8 runs\\{RUN.name}\\code\\check.py --pilot`, then same command without --pilot; `python -X utf8 runs\\{RUN.name}\\code\\verify_grouping.py --pilot`, then without --pilot. Pilots completed under60seconds. The primary pilot was augmented to explicitly check genuine minority debt before the full run; both pilots passed, no assertion failure or narrowed domain. No tests rerun after the completed passing full jobs.

Primary PASS: {checks['pair_cases']} labeled shared-core pairs (all16^2 masks, widths1..3), {checks['triple_cases']} labeled nested triple cases (all16^3 masks, r,s1..2),255 width compositions, {checks['assertions']} assertions. Direct integer Walsh character sums, exact Fraction probabilities/influences, prime-log entropy forms and80-term rational atanh intervals with proved geometric tail certify every sign; exact-zero vectors are recognized. Actual minority m, complete terminals, erasure/JS, product edge costs and signed deficits checked. Maxdimension6. out/checks.json, out/pairs.json and out/chains.json were saved immediately.

Separate implementation PASS: {group['cases']} cases (all16 two-bit cores times255 ordered width compositions of totals1..8), {group['assertions']} assertions, maxdimension10. Independent undirected boundary enumeration/Fraction arithmetic verifies the FULL data and future-control reserve formula, actual total influence, original reach weights and refunds. It imports no primary checker or source implementation. out/grouping.json retains explicit fair-chain dictator witnesses; at d8, terminal I=1/256, split data=1/32, split controls=7/64, folded reserve=255/32768, exact refund=4353/32768. These are sufficient-ledger debits, never FEI counterexamples.

# proof dependencies and changed downstream conclusions

Only the independently accepted whole-block clause of A023@3 and the established B06-R2 leaf partition baseline are used. The original A023 statement hash is preserved in the local CLAIMS copy; its review record explicitly restricts acceptance. No shared registry or source is modified. We create no new broad candidate. The two-level owner/signed formulas and exact grouping refund are checked consequences in this run; their separate external review remains pending.

A023/A028/A027/A064 can now distinguish a data surcharge from a reserve on future queried controls. Resetting either account at the second block would be invalid. If all failed branches agree at a constant, folding gives the exact reserve refund on the unchanged leaf partition. For different terminal cores only the larger marked bank is currently justified. A025's prior face-pricing obstruction is not contradicted or relabeled as new; full FEI remains OPEN.

# one next mathematical action and independent reviewer

{nextaction} This targets the exact first uncompensated physical-child bill, rather than running another small-dimensional gain search. A023/A087 should check owner coefficients and the grouping proof; A094 should reconstruct the signed sufficient condition without clipping either child. Handoffs are saved artifacts, not sent messages or observed downstream adoption.

# actual persistence receipts or precise save blocker

Saved REPORT.md, CLAIMS.json, PROGRESS.json and byte-identical PACKET_DELTA.json, DERIVATION.md, REVIEW_A023.md, both frozen specs, direct reviewer/boundary checker/persistence code and all outputs. Exact protocol key checks, report headings, compatibility identity and every file<20MB are validated by code/persist.py. SOURCE_RECEIPTS.json and ARTIFACT_RECEIPTS.json contain SHA256 receipts. Rolling STATUS.md, WORKLOG.md and LEARNED.md updated inside A029 only. No local save blocker. Remote copies, external acceptance of the application and downstream use are unverified.

**Universal bridge:** This stage moves C019 stopping-tree payment and the C024 history interface by independently accepting a reusable source clause, retaining every actual child deficit, and locating the exact two-block data surcharge2a(1-a)b(1-b)I12 plus the separate future-control debit2a(1-a)I_B. On identical-constant-failure chains, grouping refunds BOTH redundancies with no repeated terminal slack; on three distinct shared cores the surcharge remains unpaid unless the displayed signed condition has a certified reserve. What remains is a noncircular terminal certificate and a universal way to fund that first surcharge without renewal. NEXT is the shortest route toward full FEI because it asks whether the existing paid interface composes on the first genuinely different-core history, instead of closing another isolated class or relabeling the same tree identity.
'''
(RUN/'REPORT.md').write_text(report,encoding='utf-8')
status='STATE: A029 stage4 saved: A023@3 whole-block scoped HOLDS; exact nested child/slack owner coefficients and full grouping refund;276? no,277567 exact assertions PASS; full FEI OPEN.\nNEXT: A023/A087/A094 review; fund exact three-core hierarchy surcharge and future-control debit from one unused signed terminal reserve; preserve original leaf weights.\n'
status=status.replace('276? no,277567','277567')
(AGENT/'STATUS.md').write_text(status,encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(f'\n{now} — Stage4 {RUN.name}: independently reconstructed A023@3 whole-block only, no repair; nested three-core deficits and owners retained. Exact data surcharge and future-control debit derived; identical-constant-failure grouping refunds both. Primary768 pairs/16384 triples248751 checks PASS92.51s; independent4080 grouping cases28816 checks PASS1.85s. Original gain target retired; no new broad candidate. Three-distinct-core universal surcharge payment OPEN.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('''
2026-10-14 stage4: A023@3 arbitrary-shared-data whole-point-block clause independently HOLDS; other bundled clauses excluded. Two nested blocks f=g0+A(g1+B(g2-g1)-g0), a,b, terminal weights(1-a,a(1-b),ab): Rdata=2a(1-a)[(1-b)I01+bI02]+2ab(1-b)I12; Rcontrols=2a(1-a)I_B. Actual signed sufficient D_K>=sum piD_K+(K-11/2)I_removed-Rdata-Rcontrols; negative children cannot be clipped. Coordinate terminal rate owner coefficients2a,2(1-a+b),2(2-a-b). Symmetric Rstar=2sum pi_i pi_j Iij<=2Iterminal, but Rdata-Rstar=2a(1-a)b(1-b)I12; Rstar paying actual entropy is UNPROVED. For a partitioned single point event with every failed branch the same constant, p=product a_j,e=1-Eg: split data reserve2pIg sum(1-a_j), split future-control reserve2pe sum(1-a_j)remaining_width_j; folded reserve2p(1-p)Ig. Exact refund covers both parts on the SAME leaf partition, keeps pH(g),pI(g). d fair bits give split dpIg and pe d(d-1)/2, hence resetting either bank is invalid. This is a sufficient-reserve diagnostic, not entropy growth or FEI failure. All276? count corrected:277567 exact assertions PASS. Full FEI open.
'''.replace('All276? count corrected:','All'))
sources=[PROTOCOL,TEAM/'BOARD.md',TEAM/'claude/B06/STREAM_NOTES.md',SRC/'REPORT.md',SRC/'PROOF.md',SRC/'CLAIMS.json',TEAM/'agents/A023/LEARNED.md',TEAM/'agents/A024/LEARNED.md',TEAM/'agents/A097/LEARNED.md',AGENT/'runs/20261013T235347Z-fleet05-A029-child-deficit-transport/CLAIMS.json']
dump(RUN/'SOURCE_RECEIPTS.json',{'saved_at':now,'scope':'Files actually read; current source hashes; earlier context excerpt reads scoped in report','sources':[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size} for p in sources]})
(RUN/'out/BOARD_snapshot.md').write_bytes((TEAM/'BOARD.md').read_bytes())
assert set(c)==set(protocol['required_per_run']['claim_fields'])
expected={s.split(' (')[0] for s in protocol['required_per_run']['progress_fields']}
assert set(progress)==expected
for h in protocol['required_per_run']['report_fields']:assert '# '+h in report
assert report.splitlines()[-1].startswith('**Universal bridge:**')
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
assert len((AGENT/'STATUS.md').read_text().splitlines())==2
files=[p for p in RUN.rglob('*') if p.is_file() and p.name!='ARTIFACT_RECEIPTS.json']
assert all(p.stat().st_size<20*1024*1024 for p in files)
dump(RUN/'ARTIFACT_RECEIPTS.json',{'saved_at':now,'protocol_fields_exact':True,'compatibility_byte_identical':True,'all_files_under20MB':True,'receipts':[{'path':str(p.relative_to(RUN)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in files]})
print(json.dumps({'status':'PASS','protocol_fields_exact':True,'run':str(RUN),'reviewed_source_hash':c['statement_sha256'],'total_assertions':checks['assertions']+group['assertions'],'rolling_current':True,'full_FEI':'OPEN'}))
