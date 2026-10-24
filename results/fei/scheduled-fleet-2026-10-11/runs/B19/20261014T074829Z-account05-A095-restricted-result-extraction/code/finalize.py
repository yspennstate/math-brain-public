from pathlib import Path
import hashlib,json,datetime

RUN=Path(__file__).resolve().parents[1];OWN=RUN.parents[1];ROOT=OWN.parents[1]
OLD=OWN/'runs/20261014T034647Z-account05-A095-restricted-result-extraction'
A094=ROOT/'agents/A094/runs/20261014T061347Z-account05-A094-proof-chain-challenger'
A097=ROOT/'agents/A097/runs/20261014T050248Z-account05-A097-cross-route-transfer'
A086=ROOT/'agents/A086/runs/20261014T042208Z-account05-A086-joint-code-referee'
PROTO=Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def dump(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def plain(s):return hashlib.sha256(s.encode()).hexdigest()
protocol=read(PROTO)
records=[read(RUN/'out'/('EXACT_'+s+'.json')) for s in ['small','critical-one','critical-two']]
assert all(r['status']=='PASS' and r['elapsed_seconds']<55 for r in records)
keys=['histories','exact_assertions','transports','admitted_histories','both_nonconstant_first_children','nonunit_child_normalizers']
results={'status':'PASS',**{k:sum(r[k] for r in records) for k in keys},'elapsed_python_seconds':sum(r['elapsed_seconds'] for r in records),'jobs':[r['mode'] for r in records],'serialization_failure_credited':False}
assert results['histories']==1570 and results['exact_assertions']==143810
dump(RUN/'out/EXACT_RESULTS.json',results)
sourcepaths=[PROTO,ROOT/'BOARD.md',ROOT/'claude/B19/STREAM_NOTES.md',OWN/'STATUS.md',OWN/'LEARNED.md',OLD/'DERIVATION.md',OLD/'CLAIMS.json',OLD/'REPORT.md',A094/'AUDIT.md',A094/'CLAIMS.json',A097/'DERIVATION.md',A086/'RECONSTRUCTION.md']
dump(RUN/'out/SOURCE_MANIFEST.json',[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sourcepaths])
(RUN/'BOARD_SNAPSHOT.md').write_bytes((ROOT/'BOARD.md').read_bytes())
old=read(OLD/'CLAIMS.json')[0]
statement=old['exact_statement']+' Further SAME-reference finite-history application: retain the support-completed Q_M of version4 and let any finite deterministic adaptive tree query only unrevealed original core coordinates, leaving selector,padding and an independent prescribed terminal untouched. At each node inherit actual posterior-weighted child references from marginal r(T)=Q(T)+Q(T+i): raw Q_b=2r P_b/(P_0+P_1), explicit normalized zero-true-row posteriors, actual Z_b normalizers, and Q_b/Z_b. The exact nonnegative release is Gamma_T=sum reach[Delta+L-avg log2 Z], with E CE_leaf=CE_M-Gamma_T and D_M-E D_leaf=sum reach[L-avg log2 Z]. If Pi_g is the actual original-core queried influence, t_a the queried count on the edited-vertex path, j_a its originally pivotal queried edges and j_rem=j-j_a, then Pi_M=Pi_g+delta(t_a-2j_a) and E I_Mleaf=I(g)-Pi_g+delta[n+1-t_a-2j_rem]. One source bank S_K=KI(g)-c therefore suffices for terminal-average payment under S_K-KPi_g+Gamma_T >=delta[(5/4)2^k c+(4-K)n+K(t_a+2j_rem-1)+3], with no child-bank renewal. For supplied c<=K0 I(g),K0>=0,K>=4,K>K0,nonconstant g,beta=Pi_g/I(g), the sufficient condition2^-m[(5/4)K0+kK+(3-K)/2]<=K-K0-Kbeta proves E CE(inherited leaf)<=K E I(actual leaf). Thus supplied4I cores with beta<=1/6 and2^m>=6k+7/2 have complete inherited terminal average paid at6 for every such adaptive tree; individual child ratios need not be bounded. An arbitrary independent terminal reference retains c_q and D_q unchanged throughout product-compatible transport. The actual unequal-spectrum h3*h2 core has I=7/4 and a weak edge-destroying first query Pi_g=1/4 with two nonconstant children, paid at m6; a second query on its zero branch gives Pi_g=1/2 and is paid at m7 by the SAME source bank. Histories beyond the explicit cumulative-spend/padding condition and universal original-core admission remain unpaid.'
claim={
 'claim_id':'A095-RANK-KL-EQUIVALENCE','version':5,'exact_statement':statement,
 'hypotheses':old['hypotheses']+['New history theorem: finite deterministic queries of original core coordinates only, no selector/padding/terminal queries, and no repeated physical coordinate along a path','One fixed incoming reference; each descendant uses actual normalized posterior transport with every zero-row reference mass retained','Terminal-average payment requires stated cumulative original-core influence-spend/padding condition; no individual child FEI-reference admission is assumed'],
 'statement_sha256':plain(statement),'contributors':old['contributors']+['A095 finite adaptive point-path/source-bank theorem; generic one-query normalized reference transport credited to A094 stage5'],
 'proof_source':{'retained_v4':str(OLD/'DERIVATION.md'),'earlier_sources':old['proof_source'],'new_history_theorem':str(RUN/'DERIVATION.md'),'validation':str(RUN/'out/EXACT_RESULTS.json')},
 'proof_dependencies':[{'claim_id':'A095-RANK-KL-EQUIVALENCE','version':4,'scope':'Support-completed point-selector root reference, exact physical edit budget and arbitrary terminal product; older statements retained','status':'Author-proved with review pending; this stage further directly validates its root reference in every history case'},{'claim_id':'A094-INCOMING-PAID-FLOOR-DESCENDANT-SHOCK-AND-OWNER','version':1,'scope':'Only generic one-query posterior/normalizer CE-KL identity and independent-terminal product transport','status':'Independently reconstructed at stated clauses here; no blanket new audit of its shock family or34/3 owner'},'Finite reference-cost and influence telescoping; exact edited-point path enumeration; Boolean Fourier/influence granularity'],
 'review_records':old['review_records'],'status':'AUTHOR_PROVED_NEW_HISTORY_PENDING_INDEPENDENT_REVIEW; LEGACY_SCOPED_REVIEWS_PRESERVED',
 'supersedes':[{'claim_id':'A095-RANK-KL-EQUIVALENCE','version':4,'scope':'Existing C020 candidate retained; quantitatively paid adaptive SAME-reference C024 continuation added'}],
 'refutes':old['refutes'],'first_unproved_line':None,'next_consumers':['A094','A097','A011','A039','A086','A099','B19','B20']}
sourceclaims=read(A094/'CLAIMS.json')
review=next(c for c in sourceclaims if c['claim_id']=='A094-INCOMING-PAID-FLOOR-DESCENDANT-SHOCK-AND-OWNER')
recipes={'plain':plain(review['exact_statement']),'canonical_statement_hypotheses':plain(json.dumps({'statement':review['exact_statement'],'hypotheses':review['hypotheses']},sort_keys=True,separators=(',',':'),ensure_ascii=False))}
assert review['statement_sha256'] in recipes.values()
review['review_records'].append({'reviewer':'A095','verdict':'HOLDS_AT_GENERIC_ONE_QUERY_AND_TERMINAL_PRODUCT_CLAUSES','scope':'CE/KL posterior transport including actual child Z normalizers, nonnegative disintegration release and arbitrary terminal product; original all-n shock/owner family not newly blanket reviewed','proof':str(RUN/'DERIVATION.md'),'locator':'Section2','validation':str(RUN/'out/EXACT_RESULTS.json'),'source_claims_sha256':sha(A094/'CLAIMS.json'),'substantive_repair_supplied':False,'contributor_conflict':False})
review['status']='PARTIALLY_INDEPENDENTLY_RECONSTRUCTED_AT_EXPLICIT_TRANSPORT_SCOPE'
for c in [claim,review]:assert set(c)==set(protocol['required_per_run']['claim_fields'])
dump(RUN/'CLAIMS.json',[claim,review])
next_action='At a concrete short-padding or higher-influence-spend core history beyond admission(E), pay the excess cumulative KPi_g using measured SAME-reference Gamma_T and signed old-sector conditional KL, retaining actual child normalizers and one original source bank.'
progress={
 'protocol_revision':protocol['revision'],'run_id':RUN.name,'stream':'B19','packet_id':'A095',
 'gap_id':'C020-SHARED-COLLISION-NONREUSED-CORE-RESERVE','attempt_id':'A095-stage5-adaptive-incoming-bank-transport',
 'method':'Consume source-bound A094 incoming-descendant obstruction and one-query normalizer identity; prove cumulative physical point-path debit and quantify inherited terminal-average payment from one original bank through arbitrary finite core-only adaptive histories',
 'mathematical_delta':'Same incoming complete point-selector reference survives finite adaptive weak-core history under explicit Pi_g/padding admission; supplied4I core gives6I terminal-average payment for beta<=1/6 and2^m>=6k+7/2, preserving all terminal KL and normalizers. Unequal-spectrum two-nonconstant-child weak first and second exposures exactly certified; no universal FEI constant changes.',
 'deliverable_status':'COMPLETE_LOCALLY_SAVED','mathematical_status':'RESTRICTED_ALL_PARAMETER_HISTORY_AUTHOR_PROVED_PENDING_REVIEW; SCOPED_A094_IDENTITY_HOLDS; FULL_FEI_OPEN',
 'claim_versions_used':[{'claim_id':'A095-RANK-KL-EQUIVALENCE','version':4},{'claim_id':'A094-INCOMING-PAID-FLOOR-DESCENDANT-SHOCK-AND-OWNER','version':1}],
 'claims_created_or_changed':[{'claim_id':'A095-RANK-KL-EQUIVALENCE','version':5},{'claim_id':review['claim_id'],'version':1,'change':'scoped transport independent-review record'}],
 'source_artifacts':[str(RUN/'DERIVATION.md'),str(RUN/'out/EXACT_RESULTS.json'),str(RUN/'out/EXACT_critical-one.json'),str(RUN/'out/EXACT_critical-two.json'),str(RUN/'out/SOURCE_MANIFEST.json')],
 'next_consumers':claim['next_consumers'],'next_action':next_action,'stagnant_substantive_attempts':0,
 'blockers':['New adaptive-history theorem awaits independent review','Histories exceeding explicit cumulative-spend/padding admission need actual measured refund payment','No universally influence-paid arbitrary core reference or mixed selector/data history admission'], 'packet_ids':['A095']}
assert set(progress)=={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
dump(RUN/'PROGRESS.json',progress);dump(RUN/'PACKET_DELTA.json',progress)

pilot=read(RUN/'out/PILOT.json')
report=f'''# A095 restricted-result extraction, stage5

## exact target, quantifiers, hypotheses and units

For any Boolean core with supplied normalized finite-cost positive-support reference, retain the support-completed point-selector reference through a finite adaptive history querying original core data only. Pay actual cumulative query influence and the full surviving terminal reference costs from ONE original source bank. Selector,padding and independent arbitrary terminal coordinates remain unqueried. All information quantities bits; influence physical uniform influence. Prove a complete explicit admission, not universal tree/core existence or uniform individual child ratios. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

Read supervisor BOARD 2026-10-14 07:47 UTC, including middle streams separately, B19 STREAM_NOTES v2 still2026-10-11 23:35 UTC, own STATUS/LEARNED and full execution protocol v2. The new prompt arrived while stage4 persistence was unfinished: checkpointed its complete proof and reduced validation first, with55,486 exact assertions and both incomplete compute attempts excluded. Its four protocol files and rolling receipts are now saved; previous immutable stages remain unchanged. Read A097 stage5 DERIVATION Sections1-5, A086 stage5 RECONSTRUCTION Sections1-5, A094 stage5 AUDIT Sections1-6 and exact CLAIMS. Their negative-cell root floor is already reviewed and is not re-enumerated here. A094's generic one-query identity and actual inherited-descendant shock identify the history gap; only the one-query/product-transport clauses receive new scoped independent acceptance. B19's original block reference was already closed, so resume this productive C020 dependency, with no disagreement with lead. Prior campaign/paper intake is retained, not claimed as newly read. Source hashes and exact paths are in out/SOURCE_MANIFEST.json; BOARD_SNAPSHOT is a closing snapshot, not evidence that the mutable board stayed unchanged.

## complete derivation or exact first unsupported line

DERIVATION.md proves the finite all-parameter history theorem. The incoming-reference posterior transport has actual normalizers Z_0+Z_1=2 and nonnegative CE release Delta+L-avg log2 Z; no fresh descendant floor is assumed. Its finite-tree cumulative release Gamma_T keeps every conditional KL and normalizer. The point edit affects queried influence only along one physical vertex path: Pi_M=Pi_g+delta(t_a-2j_a), including erased original edges. Therefore surviving physical influence is I(g)-Pi_g+delta[n+1-t_a-2j_rem]. The SAME source bank obeys the explicit lower bound(D), with KPi_g spent cumulatively and Gamma_T measured under the incoming model.

If c<=K0 I(g),K>=4,K>K0,beta=Pi_g/I(g), the sufficient terminal-average admission is2^-m[(5/4)K0+kK+(3-K)/2]<=K-K0-Kbeta. Under supplied4I, beta<=1/6 and2^m>=6k+7/2 suffice for inherited mean terminal CE<=6 times mean physical terminal influence through EVERY such finite adaptive tree. This goes beyond a paid root to a retained-model history, but asserts no per-leaf bound. Independent arbitrary terminal c_q,D_q stay additive and do not fund the core bank. No bank is renewed at a descendant.

The explicit unequal-spectrum h3*h2 source has I=7/4 and destroys original point edges. Its first query has original influence1/4 and two nonconstant children; m6 admits it. A second query on its zero branch has cumulative original influence1/2; m7 admits it using the SAME bank. The exact physical debits and complete inherited terminal costs are certified. Generic reference telescoping is a known identity credited to A094; the new contribution is the quantified adaptive point-path/source-bank admission and these weak unequal exposures. No source theorem is refuted or repaired.

The first unsupported universal line is paying histories beyond this explicit Pi_g/padding condition using the measured refund and signed inherited old-sector debt, or admitting arbitrary original core references at an absolute influence price. A paid root alone does not certify its descendants, and no fresh model reset or child slack can be inserted for free.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC preceded all jobs. Final completed coverage: {results['exact_assertions']} exact assertions, {results['histories']} actual histories, {results['transports']} reference transports; {results['admitted_histories']} sufficient-payment histories, {results['both_nonconstant_first_children']} first exposures with two nonconstant original children, {results['nonunit_child_normalizers']} explicitly retained nonunit child normalizers. Small domain: all4 one-bit and16 two-bit Boolean cores plus three-bit labels1,3,15,23,85,105,127,255, every136 specified core vertex, m1/4,two uniform/increasing full-core references. One-query, fixed two-query and branch-stopped adaptive policies give1568 histories; k1 uses one policy only. No exhaustive3-bit or symmetry count is claimed. Two critical histories expand the actual h3*h2 core at m6/m7, with product-spectrum reference, one or two weak physical core queries. Largest actual parent has13 bits. Arbitrary terminal tensor clauses have direct all-parameter product proofs, not an expanded terminal census.

Commands from A095 were `python -X utf8 runs\\{RUN.name}\\code\\check.py pilot`, then `small`, `critical-one`, `critical-two`, sequentially. Pilot {pilot['exact_assertions']} assertions PASS in {pilot['elapsed_seconds']:.6f}s. Completed small {records[0]['elapsed_seconds']:.6f}s, critical one {records[1]['elapsed_seconds']:.6f}s, critical two {records[2]['elapsed_seconds']:.6f}s, all below55-second in-helper guard. The first critical-two attempt hit Python's4300-digit integer-string limit while serializing a computed exact interval; it has no credited result. Original checker and out/SERIALIZATION_FAILURE preserve that attempt. FROZEN_SERIALIZATION_AMENDMENT changes only saving: outward integer rounding to2^-80; no precision, integer-limit, family or dimension increase. Only that case was rerun. Prior passing cases were not repeated unnecessarily.

Arithmetic uses integer Walsh and independent actual edge counts, Fraction reference/posterior/normalizer and atom-likelihood identities, exact cumulative physical influence equations, and rational24-term range-reduced atanh bounds with tail2y^49/[49(1-y^2)]. Binary logs are exact. No factoring huge transport ratios or accepting floating signs. Recorded times are Python observations, not billing or resources. Estimated memory120MB, not measured; no expected>300MB job, GPU, parallel heavy work, window or background process.

## proof dependencies and changed downstream conclusions

Version5 continues the existing A095 C020 candidate; its earlier statements and scoped independent-review receipts remain intact. No third broad pending candidate is opened. The new proof depends on v4's complete inherited root construction and on the source-bound A094 one-query identity, reconstructed independently here. Earlier rank/equivalence clauses are not blanket accepted through these scopes; v4's new root application still awaits external review. A094's original all-n shock and34/3 strong-pivot owner are consumed as gap context, not newly accepted by this partial review. Imported statement hashes retain their actual convention; new v5 hashes plain UTF8 exact_statement.

Downstream mathematical change: weak adaptive core exposure with two nonconstant children now has a full incoming-model terminal-average payment under a quantified original influence-spend condition, retaining conditional KL and real child normalizers. The complete terminal q is never used to subsidize that bank. This is a finite history class theorem, not universal tree selection or a new FEI counterfamily. Universal constant improvement is zero.

## one next mathematical action and independent reviewer

{next_action} A097/A039 supplies or challenges the next weak-core physical query; A094/A086 independently reconstructs point-path debit and the source-bank admission; A011/A099 consumes only explicit cumulative-budget scope. This replaces a fresh-root floor by carried likelihood/normalizers and exposes the actual first unpaid request.

## actual persistence receipts or precise save blocker

Saved this exact run's four protocol files, DERIVATION, frozen specs, original/repaired checker, completed outputs, critical outward rational certificates, source manifest, board snapshot and receipts. code/finalize.py validates exact claim/progress fields, statement hashes, identical packet delta, report headings, two-line STATUS and20MB limits; out/PERSISTENCE_RECEIPTS.json records local file hashes. Stage4 is checkpointed separately and was not falsely reported as completed before its final audit. WORKLOG/LEARNED updated with actual stage5 results. No shared index, other-agent folder, brain, git/mail or remote mirror changed; no adoption, independent acceptance of new theorem or public release claimed.

## Universal bridge

This stage advances C020's complete-reference payment through C024 history transfer: one fixed support-completed code and its original source bank now pay a finite adaptive weak-core history at terminal-average rate6 when a supplied4I core satisfies beta<=1/6 and2^m>=6k+7/2; exact cumulative destroyed-edge debits, conditional KL and child normalizers remain. It closes the weak unequal h3*h2 first and second exposure without renewing the bank. The universal FEI constant improvement is zero: histories beyond the explicit admission and arbitrary original-core reference payment remain open. NEXT pays that precise excess cumulative request with the measured SAME-model refund and retained signed core debt, making it a direct route to the missing universal reserve rather than another fresh-root class theorem.
'''
for h in protocol['required_per_run']['report_fields']:assert '## '+h in report
(RUN/'REPORT.md').write_text(report,encoding='utf-8')
(OWN/'STATUS.md').write_text('STATE: A095 stage5 saved: adaptive SAME-reference point-edit history paid from one source bank under explicit cumulative Pi_g/padding admission; weak unequal two-child first/second exposure certified;143,810 exact assertions PASS; independent review pending; FEI OPEN.\nNEXT: A094/A086 review point-path bank; pay beyond-admission weak history using measured incoming Gamma and signed old-sector KL, retaining child normalizers and one original owner (C020/C024).\n',encoding='utf-8')
with (OWN/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write('\n2026-10-14 stage5 ('+RUN.name+'): First checkpointed prior stage4 reduced exact domain and completed A094 audit,55,486 assertions. Consumed current A094 incoming paid-root descendant shock and reconstructed its one-query normalizer/product identity. Proved arbitrary finite core-only adaptive point-path influence debit and SAME-reference cumulative source-bank admission; supplied4I core gives mean6I terminal cost for beta<=1/6 and2^m>=6k+7/2. Unequal h3*h2 weak first and adaptive second exposures both certified.143,810 completed exact assertions/1570 histories; only critical-two serialization failed and was repaired by outward rounding, no precision increase. New theorem review pending, no universal bridge closes.\n')
with (OWN/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\n2026-10-14 stage5: Through any finite adaptive core-only tree on a point-selector, Pi_M=Pi_g+delta(t_a-2j_a) and mean remaining I=Ig-Pi_g+delta[n+1-t_a-2(j-j_a)]. A094 posterior transport retains actual Z_0+Z_1=2 and release Delta+L-mean logZ>=0, so mean terminal CE=Croot-Gamma with full conditional KL retained. One original bank pays terminal average if2^-m[(5/4)K0+kK+(3-K)/2]<=K-K0-K(Pi_g/Ig),given raw c<=K0Ig,K>=4,K>K0. With K0=4,K6, beta<=1/6 needs2^m>=6k+7/2. No individual-leaf ratio or renewal follows. h3*h2 has unequal magnitudes3/8,1/8,Ig7/4; first original query1/4 paid m6,two-query Pi_g1/2 paid m7 using SAME owner and destroyed-edge correction. Independent terminal cost/deficit remains additive. Histories beyond admission need measured Gamma and signed incoming log profile, not a new floor.\n')
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
assert len((OWN/'STATUS.md').read_text().splitlines())==2
receipts=[]
for p in sorted(RUN.rglob('*')):
    if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json':
        assert p.stat().st_size<20_000_000
        receipts.append({'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)})
for p in [OWN/'STATUS.md',OWN/'WORKLOG.md',OWN/'LEARNED.md']:receipts.append({'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)})
dump(RUN/'out/PERSISTENCE_RECEIPTS.json',{'scope':'LOCAL_ONLY','generated_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'schema_checks':'PASS','progress_bytes_identical':True,'files':receipts})
print(json.dumps({'status':'PASS','claim_version':5,'files_receipted':len(receipts),'exact_assertions':results['exact_assertions']}))
