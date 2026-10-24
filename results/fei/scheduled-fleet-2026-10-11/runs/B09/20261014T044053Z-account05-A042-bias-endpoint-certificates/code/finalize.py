from pathlib import Path
import json,hashlib,datetime
root=Path(__file__).resolve().parents[1];agent=root.parents[1];team=agent.parents[1]
a44=team/'agents/A044/runs/20261014T025427Z-account05-A044-non-symmetric-gate-classes'
a43=team/'agents/A043/runs/20261014T022706Z-account05-A043-prime-gate-decomposition'
protocol=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
def save(name,obj): (root/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def digest(s,h):return hashlib.sha256(json.dumps({'statement':s,'hypotheses':h},sort_keys=True,separators=(',',':')).encode()).hexdigest()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
source=json.loads((a44/'CLAIMS.json').read_text(encoding='utf-8'))[0]
assert source['statement_sha256']=='7d78ab7cf325ab80263b94a66f6ac63f38d885de9a60e8fce6bebee46403a120'
assert digest(source['exact_statement'],source['hypotheses'])==source['statement_sha256']
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
review={'reviewer':'A042/account05','at_utc':now,'verdict':'HOLDS_FULL_STATED_NARROW_CLAIM','source_claim_id':source['claim_id'],'version':1,'statement_sha256':source['statement_sha256'],'accepted_scope':['all-bias three-event deficit-loss identity','fixed actual prime and positive-loss/root-slack obstruction','sharp coherent slice constant 4+1/ln2 and higher-degree bound','endpoint contraction and exclusions'],'excluded_scope':['A044 review of A043 two-term decomposition/census','any all-bias entropy upper bound for prime56067 or universal FEI'],'repair_supplied':False,'contributor_to_source_version':False,'method':'new direct centered-moment checker, direct physical influence, ten block-row tests; analytic physical cross-term and slice reconstruction in PROOF.md section4','evidence':['PROOF.md','code/check.py','out/CHECK.json']}
save('out/REVIEW_A044.json',review)
reviewed=dict(source);reviewed['review_records']=source['review_records']+[review];reviewed['status']='INDEPENDENTLY_RECONSTRUCTED_FULL_NARROW_SCOPE_LOCALLY; ORIGINAL_UNCHANGED'
statement=('For the Boolean prime mask56067, positive on {a=b=z=1}, {a=0,c=z=1} or {b=c=0}, '
 'write alpha=P(a=1),q=P(z=1),e=P(b=0),d=P(c=0), with alpha,q fixed interior and e,d independently tending to zero. '
 'Its exact combined normalized coefficients are (2) and its exact corrected natural entropy and deficit are (3)-(4) of PROOF.md. '
 'Writing Le=4alpha q(2-alpha-q),Ld=4(1-alpha)q(1+alpha-q), '
 'theta=Le e/(Le e+Ld d), delta=max(e,d), '
 'R(alpha,q)=ln4+2[(1-q)+q ln(1/q)+alpha ln(1/alpha)]/(2-alpha-q), '
 'one has Hplus/(I-Var)=[theta R(alpha,q)+(1-theta)R(1-alpha,q)]/ln2+O_alpha,q(delta ln(1/delta)), '
 'uniform over relative e,d rates and uniformly on compact interior alpha,q domains. '
 'Each fixed-interior R is strictly below 4+ln4; the supremum of all such face tangent ratios is 2+4/ln2 in bits. '
 'Thus the Cstar corrected inequality holds in a sufficiently small entire e,d collar for each fixed alpha,q, uniformly on compact interior parameter sets. '
 'The actual joint path (p_a,p_b,p_c,p_z)=(1-t^2,1-t^6,1-t^8,1-t) has '
 'I-Var=4t^7+O(t^8), E=(16+8ln2)t^7+O(t^8 ln(1/t)), and ratio tending to 2+4/ln2. '
 'At the contracted literal face E=I-Var=0; no endpoint quotient is assigned. '
 'No general four-bias upper bound or universal FEI theorem is asserted.')
hyp=['fixed actual Boolean mask56067 and independent Bernoulli physical inputs','spectral influence I and variance; E=(ln2)Hplus, corrected Hplus in bits','fixed alpha,q in (0,1) for the two-rate expansion; e,d>0 and max(e,d) tending to zero','compact-interior uniformity only; no substitution of boundary alpha,q into the fixed-parameter remainder','joint corner path established separately from exact coefficients, not by exchanging limits','h(0)=0 and deterministic endpoints contracted before normalization']
claim={'claim_id':'A042-COHERENT-PRIME-LITERAL-FACE-ENDPOINT','version':1,'exact_statement':statement,'hypotheses':hyp,'statement_sha256':digest(statement,hyp),'contributors':['A042/account05'],'proof_source':{'run_id':root.name,'paths':['PROOF.md','code/check.py','out/CHECK.json']},'proof_dependencies':['actual Boolean polynomial (1)','normalized product mixed differences and Parseval','elementary t ln(1/t)<=1-t and Taylor expansions with explicit zero-coefficient terms'],'review_records':[],'status':'SOURCE_COMPLETE_NARROW_ENDPOINT_REPAIR; INDEPENDENT_REVIEW_PENDING','supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['A043','A044','A041','A045','A090','A091','B09']}
save('CLAIMS.json',[claim,reviewed])
checks=json.loads((root/'out/CHECK.json').read_text())
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':root.name,'stream':'B09','packet_id':'A042','gap_id':'C025-G-BIASED-LTF-COHERENT-PRIME-FACE','attempt_id':'A042-stage5-independent-rate-literal-face','method':'consume new obstruction, independently review source, retain signed combined coefficients and derive symbolic two-rate endpoints','mathematical_delta':'A044 shared-guard obstruction/sharp slice independently HOLDS. Exact four-bias coefficient/deficit interface for prime56067; two-rate near-literal continuum with strict fixed-parameter tangent gap below Cstar and compact-uniform collars; actual joint endpoint path reaches Cstar.','deliverable_status':'COMPLETE_LOCAL','mathematical_status':'NARROW_ENDPOINT_THEOREM_PROVED; ALL_BIAS_PRIME_UPPER_BOUND_AND_FULL_FEI_OPEN','claim_versions_used':[{'claim_id':source['claim_id'],'version':1,'statement_sha256':source['statement_sha256'],'status':'INDEPENDENT_HOLDS_FULL_NARROW_SCOPE; fixture and rejected ledger consumed'}],'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1,'statement_sha256':claim['statement_sha256']},{'claim_id':source['claim_id'],'version':1,'change':'local independent review record only; original unchanged'}],'source_artifacts':['PROOF.md','out/FROZEN_SPEC.json','out/REVIEW_A044.json','code/check.py','out/CHECK.json'],'next_consumers':['A043','A044','A041','A045','A090','A091','B09','B20'],'next_action':'Use exact combined coefficients (2)-(4) to pay prime56067 away from the certified literal-face collars, with a signed quadratic reference and one complete terminal reserve; treat other joint endpoint regimes separately.','stagnant_substantive_attempts':0,'blockers':['No all-bias combined-spectrum entropy payment for prime56067.','No explicit collar radius uniform up to alpha,q boundary.'],'packet_ids':['A042']}
save('PROGRESS.json',progress);(root/'PACKET_DELTA.json').write_bytes((root/'PROGRESS.json').read_bytes())
report=f'''# A042 stage5: coherent prime literal-face endpoints

## exact target, quantifiers, hypotheses and units

Push the endpoint packet after mask33152 was closed at all biases by A043. Consume A044's obstruction on prime56067 before using any singleton reserve. Natural corrected entropy E=(ln2)Hplus; Hplus is in bits and D=I-Var uses spectral influence. Derive the literal-face limit p_b,p_c->1 at independent rates for every fixed interior p_a=alpha,p_z=q, then certify a joint corner path without exchanging limits. Full FEI remains OPEN.

Result: an exact combined-coefficient/deficit interface, the complete two-rate tangent interval and compact-interior uniform collars below Cstar=2+4/ln2. Every fixed face parameter gives a strict limiting gap; the envelope over face parameters is sharply Cstar. The actual path (1-t^2,1-t^6,1-t^8,1-t) realizes Cstar with D=4t^7+O(t^8). This is a local endpoint theorem, not the all-four-bias upper bound.

## sources actually read, revisions and theorem locators

Read BOARD.md snapshot2026-10-14 04:40UTC, specifically targeted B09 after the full board output truncated; B09 STREAM_NOTES.md v2 (2026-10-11 23:33); own STATUS.md; and full EXECUTION_PROTOCOL.json revision2026-10-11-execution-v2. Read A043 stage4 REPORT.md, PROOF.md and CLAIMS opening, run20261014T022706Z-account05-A043-prime-gate-decomposition. Its newly closed all-bias mask33152 result redirects the packet to the shared-guard fixture; no all-two-term theorem is a mathematical premise of the new local result.

Read A044 stage4 REPORT.md, PROOF.md and CLAIMS.json, run20261014T025427Z-account05-A044-non-symmetric-gate-classes, source {source['claim_id']}@1, hash {source['statement_sha256']}. The complete stated narrow obstruction/slice theorem is independently reconstructed in PROOF.md section4. The source's own review of A043 is excluded. No new paper theorem, external web premise, brain query, lead tax or AND baseline recomputation is used. Source bytes are pinned in out/SOURCE_RECEIPTS.json.

## complete derivation or exact first unsupported line

PROOF.md supplies all derivations. Reflect b,c into rare variables x,y and write the actual Boolean polynomial -1+2z+2xy-2z[ax+(1-a)y]. All twelve nonzero normalized coefficients are retained before squaring. This gives exact D=Le e(1-e)+Ld d(1-d)+(uw/4)(d-e)^2+4ed(1-e)(1-d) and full E as a ten-term h expression.

The linear entropy expansion has error O_alpha,q(delta^2 ln(1/delta)), uniformly over all relative e,d rates. Dividing by the positive linear deficit gives a convex mixture of the two explicit tangent ratios R(alpha,q),R(1-alpha,q), with error O_alpha,q(delta ln(1/delta)). The elementary log bound proves R<4+ln4. Positivity and continuity give a whole sufficiently small collar for each fixed parameter pair, uniformly over compact interior pairs. The exact formulas separately prove the joint corner path D=4t^7+O(t^8), E=(16+8ln2)t^7+O(t^8 ln(1/t)).

A044's positive raw loss L has unbounded L/D on its source slice, while the coherent E/D stays paid; its full narrow claim independently HOLDS. No repair was supplied to that version. First unsupported line: pay the complete combined spectrum at all independent biases, including interior points away from the collars and other joint alpha,q boundary regimes. The false positive-debit ledger is not reintroduced.

## executed validation with domain, arithmetic, commands and outputs

Frozen out/FROZEN_SPEC.json preceded execution. `python -X utf8 code/check.py`: {checks['assertions_passed']:,} exact assertions PASS in {checks['runtime_seconds']:.3f} seconds; 133 fixed laws (81 general,36 independent-rate face fixtures,8 source slice values,8 new joint-path values). Direct truth-table centered moments and physical derivatives check Parseval, influence, the entire normalized coefficient table and exact deficit formula. The three constituent truth tables independently verify the all-bias loss on the 81 general fixtures. Ten proper block row tests and essentiality certify prime56067. Exact outward natural-log intervals check K/Le against the simplified R, strict tangent inequalities, slice entropy identity/upper bound and high-degree cost. No floating-point sign test is used.

Logs use exact power-of-two reduction and24-term atanh sums with tail <=2z^49/[49(1-z^2)], z<=1/3. The finite grids verify algebra; continuum, all-relative-rate errors and the actual path limit come from the written proof. One pilot, no failed check or adaptive domain increase. Memory estimated60MB, peak not measured, so no >300MB job or memok trigger. No heavy job or background process.

## proof dependencies and changed downstream conclusions

The new theorem depends only on the actual Boolean polynomial, product Fourier algebra and elementary logarithms/Taylor bounds; its proof does not require accepting A043's all-bias two-term classification. A044's exact narrow source version receives an independent full-scope mathematical review with excluded meta-review content. Source version and hash are preserved in the local review record and copied claim; originals unchanged. A043 independently accepted A042 stage4 in its newly read source; that receipt is consumed as context, not counted as proof of this new version.

A043/A044/A041/A045 can now use an exact boundary target for a coherent quadratic reference. Independent guard rates introduce only a convex combination of two finite tangents for fixed interior remaining biases. The sharp corner lower limit Cstar is realized by an actual Boolean family, not an abstract profile. This is consistent with bounded FEI and supplies no upper theorem at arbitrary biases. No global optimum or universal payment is claimed.

## one next mathematical action and independent reviewer

NEXT: insert the exact combined coefficients and D expression into an all-bias signed quadratic payment for prime56067, using the established literal-face collars as boundary conditions and retaining one complete terminal reserve. Other joint endpoint regimes require separate analysis rather than substitution into a nonuniform fixed-parameter remainder. A043/A044 should consume (7)-(10); A090/A091 should independently check the two-rate remainder, strict tangent envelope and direct path asymptotics. New local theorem review remains pending.

## actual persistence receipts or precise save blocker

Saved the four protocol files, PROOF.md, frozen specification, exact checker/output, independent review and source receipts in this run. STATUS.md has two lines; WORKLOG.md and LEARNED.md append current results. out/VALIDATION.json checks schemas, canonical claim hashes, headings, progress-copy equality and artifact sizes; out/PERSISTENCE.json records local hashes and sizes. No save blocker. Registry adoption, supervisor copying, new independent review, brain ingestion and mirror verification are pending; no remote persistence is asserted.

**Universal bridge:** This stage moves the B09 lead's C025/G-BIASED-LTF prime payment toward a coherent whole-set reference by independently accepting the new shared-guard obstruction and deriving the exact independent-rate literal-face certificate for its first unresolved prime. It closes every approach with fixed interior alpha,q on that face and shows its sharp tangent envelope is Cstar, with an actual joint path attaining the envelope. General four-bias entropy payment and full FEI remain open. NEXT uses this exact cancellation-preserving interface and its certified collars to test the remaining signed quadratic cost, the shortest surviving extension of the successful two-term payment after positive shared-guard funding was rigorously ruled out.
'''
(root/'REPORT.md').write_text(report,encoding='utf-8')
state='STATE: A042 stage5 saved: A044 shared-guard narrow claim independently HOLDS; prime56067 exact coherent two-rate literal-face certificate and sharp Cstar joint path; 3,507 checks PASS; FEI OPEN.\nNEXT: A043/A044 consume exact coefficients and face collars; A090/A091 review tangents/path; pay full all-bias signed quadratic cost with one terminal reserve.\n'
(agent/'STATUS.md').write_text(state,encoding='utf-8')
if 'stage5 coherent-face' not in (agent/'WORKLOG.md').read_text(encoding='utf-8'):
 with (agent/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(f'\n{now} stage5 coherent-face: read new A043 closure of mask33152 and A044 loss obstruction; independently reviewed A044 full narrow claim. Derived exact prime56067 combined coefficients/D, two-independent-rate literal-face tangents, compact-interior collars and actual path reaching Cstar. 3507 exact assertions in {checks["runtime_seconds"]:.3f}s; full all-bias payment open.\n')
if 'Stage5 coherent-face:' not in (agent/'LEARNED.md').read_text(encoding='utf-8'):
 with (agent/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\nStage5 coherent-face: prime56067 in rare coordinates x=1-b,y=1-c is f=-1+2z+2xy-2z[ax+(1-a)y]. Le=4alpha q(2-alpha-q), Ld=4(1-alpha)q(1+alpha-q); exact D=Le e(1-e)+Ld d(1-d)+(uw/4)(d-e)^2+4ed(1-e)(1-d). Tangent R(alpha,q)=ln4+2[(1-q)+q ln(1/q)+alpha ln(1/alpha)]/(2-alpha-q)<4+ln4. Independent-rate ratio is weighted R(alpha,q),R(1-alpha,q), error O_alpha,q(delta ln(1/delta)), uniformly on compact interior parameters only. Actual path probabilities (1-t^2,1-t^6,1-t^8,1-t) gives D~4t^7, E~(16+8ln2)t^7, ratio Cstar. A044 source shared-guard loss/slice theorem independently HOLDS at full narrow scope; positive L cannot be funded by root slack. All-bias upper payment remains open.\n')
paths=[protocol,team/'BOARD.md',team/'claude/B09/STREAM_NOTES.md',a43/'REPORT.md',a43/'PROOF.md',a43/'CLAIMS.json',a44/'REPORT.md',a44/'PROOF.md',a44/'CLAIMS.json']
save('out/SOURCE_RECEIPTS.json',[{'path':str(p),'sha256':sha(p)} for p in paths])
pr=json.loads(protocol.read_text())['required_per_run']
for c in (claim,reviewed):
 assert set(c)==set(pr['claim_fields'])
 assert digest(c['exact_statement'],c['hypotheses'])==c['statement_sha256']
assert set(progress)=={s.split(' (')[0] for s in pr['progress_fields']}
assert (root/'PROGRESS.json').read_bytes()==(root/'PACKET_DELTA.json').read_bytes()
assert all('## '+h in report for h in pr['report_fields'])
assert len(state.splitlines())==2
assert checks['assertions_passed']==3507
assert all(p.stat().st_size<20*1024*1024 for p in root.rglob('*') if p.is_file())
save('out/VALIDATION.json',{'schema_fields':'PASS','statement_hashes':'PASS','progress_copies':'PASS','report_headings':'PASS','status_two_lines':'PASS','file_sizes':'PASS','assertions':checks['assertions_passed'],'full_fei':'OPEN'})
save('out/PERSISTENCE.json',[{'path':str(p.relative_to(root)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(root.rglob('*')) if p.is_file() and p.name!='PERSISTENCE.json'])
print(json.dumps({'local_save':'COMPLETE','schemas':'PASS','assertions':checks['assertions_passed'],'claim_hash':claim['statement_sha256']}))
