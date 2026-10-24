from pathlib import Path
import json,hashlib,datetime
RUN=Path(__file__).resolve().parent.parent;OWN=RUN.parent.parent;ROOT=OWN.parent.parent
BASE=Path(r'~\mop_fei100\reports\fei-2026-10-11');RID=RUN.name
def load(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
src=ROOT/'agents/A001/runs/20261014T011101Z-account05-A001-quantifier-audit'
claims=load(src/'CLAIMS.json');adopt=next(c for c in claims if c['claim_id']=='A096-TERMINAL-KL-REFUND-AUDIT')
statement=('For every finite uniform-cube Boolean sign f with masses p_S and influences e_i, let F_J replace each physical coordinate i in J by a disjoint pair parity u_i v_i. Then H(F_J)=H(f), I(F_J)=I(f)+sum_J e_i and M(F_J)=M(f)-sum_J M_i(f), where M_i=e_i[log2(1/e_i)-D(mu_i||r_i)] with complete normalized row laws mu_i(T)=p_(T+i)/e_i,r_i(T)=p_T+p_(T+i). Each duplicated row u_i or v_i has zero M and zero erasure. Marginalizing only its partner occupancy loses exactly M_i(f) of influence-weighted KL. In contrast retaining only that partner gives laws mu=(0,1),r=(1-e_i,e_i), preserves the complete KL log2(1/e_i) and loses zero refund. Independent common spectator factors can be discarded with zero loss in this binary quotient. All-pair deletion loss divided by total physical influence equals M(f)/I(f) if J is all coordinates. For every even d>=2 an actual witness G(u,v,y)=g(uv,y), g(s,y)=b(y)-1_{y=0}+s 1_{y=0}, b(y)=(-1)^(sum_j y_(2j-1)y_(2j)), has Inf_u=Inf_v=delta=2^-d, I(G)=d/2+(d+2)delta, H(G)/I(G)<=3, and each partner-deletion loss lies in [delta(d-1),delta d]. The reference partner and core are genuinely correlated. Thus no fixed local influence allowance using only the queried/erased pair pays this loss, even though the opposite binary quotient retains it exactly. No universal terminal-core payment or FEI disproof is asserted.')
new={'claim_id':'A096-SINGLE-SPECTATOR-REFUND-OWNERSHIP','version':1,'exact_statement':statement,
     'hypotheses':['Actual finite Boolean signs on the uniform physical cube; bits and ordinary flip influence','Disjoint two-bit parity substitutions, with no assertion of influence invariance under general linear changes','Complete reference probabilities retained, including derivative-free mass; irrelevant rows omitted','Bent witness even d>=2; y uses 0/1 labels of the uniform cube'],
     'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['A096'],
     'proof_source':{'path':str(RUN/'DERIVATION.md'),'locator':'Sections 2-4, equations (2)-(7) and binary repair','validation':str(RUN/'out/CHECK.json')},
     'proof_dependencies':[],'review_records':[],'status':'SCOPED_CONDITIONAL_REFERENCE_AUDIT_PROVED_PENDING_INDEPENDENT_REVIEW',
     'supersedes':[],'refutes':['For all actual Boolean rows, deleting a single physical spectator has KL refund loss <=K(Inf_query+Inf_spectator) for one finite absolute K'],
     'first_unproved_line':None,'next_consumers':['A001','A073','A090','A085','A099','A097','B20']}
save(RUN/'CLAIMS.json',[adopt,new])
sources=[ROOT/'BOARD.md',ROOT/'claude/B20/STREAM_NOTES.md',BASE/'EXECUTION_PROTOCOL.json',
         BASE/'CLAIM_REGISTRY.json',BASE/'OBSTRUCTION_REGISTRY.json',BASE/'PACKET_STATUS.json',
         src/'REPORT.md',src/'CLAIMS.json',
         ROOT/'agents/A073/runs/20261013T234148Z-account05-A073-certified-logarithms/REPORT.md',
         ROOT/'agents/A073/runs/20261013T234148Z-account05-A073-certified-logarithms/CLAIMS.json',
         ROOT/'agents/A090/runs/20261014T010003Z-account05-A090-independent-reconstruction/REPORT.md',
         ROOT/'agents/A090/runs/20261014T010003Z-account05-A090-independent-reconstruction/CLAIMS.json',
         ROOT/'agents/A078/LEARNED.md',OWN/'runs/20261013T220343Z-account05-A096-live-gap-ledger/STATUS.md']
# Rolling STATUS was read at entry, not a historical per-run file; preserve its current bytes before updating.
sources=[p for p in sources if p.exists()]+[OWN/'STATUS.md']
save(RUN/'out/SOURCE_MANIFEST.json',[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size} for p in sources])
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':RID,'stream':'B20','packet_id':'A096',
    'gap_id':'C018-HIGHER-ERASURE-SINGLE-BUDGET','attempt_id':'A096-STAGE4-CORRELATED-SPECTATOR',
    'method':'Consume within-tail/within-degree objections; exact signed Boolean parity-pair spectrum and conditional likelihood-ratio audit',
    'mathematical_delta':'Complete binary quotient preserves all refund on a genuinely correlated row; opposite one-bit deletion loses exact terminal M_i and cannot be paid by erased-pair influence. A001/A073 full-scope acceptance of prior audit adopted. Universal payment improvement zero.',
    'deliverable_status':'COMPLETE_LOCAL_ARTIFACTS','mathematical_status':'SCOPED_BINARY_REPAIR_AND_LOCAL_NOGO_PROVED; C018_OPEN; NEW_REVIEW_PENDING',
    'claim_versions_used':['A096-TERMINAL-KL-REFUND-AUDIT@1 (A073/A001 independent acceptance adopted)','A001-BOUNDED-DEGREE-REFUND-LOSS@1 (objection consumed, no independent acceptance)','A090-DEGREE-COARSENED-REFUND-OBSTRUCTION@1 (objection consumed, no independent acceptance)'],
    'claims_created_or_changed':['A096-SINGLE-SPECTATOR-REFUND-OWNERSHIP@1','A096-TERMINAL-KL-REFUND-AUDIT@1 acceptance adoption'],
    'source_artifacts':['DERIVATION.md','out/CHECK.json','out/ATTEMPT_1.json','out/SOURCE_LEDGER.json','out/SOURCE_MANIFEST.json'],
    'next_consumers':['A001','A073','A090','A085','A099','A097','B20'],
    'next_action':'On a nonzero-erasure shared-coordinate row, retain the informative likelihood-ratio statistic and either cancel its conditionally common core factor or debit the exact conditional remainder once to certified child slack; A001/A073 audit',
    'stagnant_substantive_attempts':0,'blockers':['Universal terminal-core payment remains unproved; new conditional audit needs independent review; canonical/mirror adoption unverified'],
    'packet_ids':['A096']}
save(RUN/'PROGRESS.json',progress);save(RUN/'PACKET_DELTA.json',progress)
ck=load(RUN/'out/CHECK.json');intake=load(RUN/'out/INTAKE_SUMMARY.json')
report=f'''# A096 stage 4: the informative spectator and its terminal owner

## exact target, quantifiers, hypotheses and units

Audit the nearest proposed payment after A001/A090's new compression objections: for an actual Boolean derivative row, can deleting one correlated physical spectator be paid by the queried/erased pair's influence? This local allowance is false. A positive alternative is proved on the same genuinely correlated row: retaining the informative partner bit preserves the full complete-reference KL with zero loss. Quantifiers cover every finite Boolean seed and partial disjoint two-bit parity duplication; the local witness covers every even d>=2. Entropy/KL are in bits and influences are ordinary physical flip influences. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

Read BOARD.md (supervisor snapshot 2026-10-14 01:30 UTC), own STATUS and B20 STREAM_NOTES v2 (still 2026-10-11 23:39Z); full execution-v2 protocol. The old T12 assignment is completed and independently accepted; this stage follows dispatch by consuming the new A001/A090 objections. No mathematical disagreement with the lead is asserted.

Critical saved originals: A001 stage4 REPORT/CLAIMS, especially bounded-degree full-support tensor obstruction and its full-scope acceptance of A096; A090 stage3 REPORT/CLAIMS, within-degree tribes KL loss; A073 stage3 REPORT, complete Q audit and support-conditioning mutation. Prior own terminal-refund derivation supplies context. Targeted A078/A052/A100 LEARNED reads distinguish existing bad-query/coherent collision ingredients: the new result concerns exact conditional-edge quotient loss and its opposite binary repair, not priority for a general bent/flip bad-query construction. No literature theorem or upstream executable is a proof premise. Byte provenance is in out/SOURCE_MANIFEST.json.

Intake read complete text from {intake['reports']} saved reports, with {intake['claim_records']} source claims, {intake['dependency_edges']} dependency records and all 100 packets; {intake['new_reports_since_stage3']} reports are new since the previous snapshot. The complete text bundle and source-bound proposed adoption delta are saved. Ingestion is not independent mathematical acceptance of every source. Shared indices are untouched.

## complete derivation or exact first unsupported line

DERIVATION.md gives the complete proof. Replace i in J by u_i v_i to obtain F_J. Direct character embedding proves H(F_J)=H(f), I(F_J)=I(f)+sum_J e_i and M(F_J)=M(f)-sum_J M_i(f). Each duplicated query has zero erasure and complete KL log2(1/e_i). Dropping just its partner leaves the exact original f row and loses M_i(f) of influence-weighted KL. Both members together lose 2M_i(f). This is an exact original-terminal bill and a single influence ledger, not a payment of that bill.

The positive conditional repair retains only the partner: mu=(0,1), r=(1-e_i,e_i). It keeps the derivative-free reference mass and exactly preserves complete KL log2(1/e_i); given partner=1 the discarded core laws agree. An independent common spectator factor cancels as well. Thus this quotient is spectator-compatible even though partner/core are correlated. It answers the requested first non-product row without assuming global independence. It is a zero-erasure row boundary case, not a result for arbitrary nonzero-erasure rows.

For the actual bent/one-flip selector g(s,y)=b(y)-1_0+s1_0, even d>=2 and delta=2^-d, Fourier pair masses are ((sigma sqrt(delta)-delta)^2,delta^2). The complete reference pair mass is at least delta/2, proving delta(d-1)<=M_s(g)<=delta d. Duplicating s into u v makes each full row M=B=0 but deleting its one partner loses exactly M_s(g). Hence the loss divided by either queried/erased influence is at least d-1; pooling both rows and both influences gives the same unbounded ratio. The witness has I=d/2+(d+2)delta and H<=d+1, so H/I<=3. This excludes a local exclusive-pair allowance, not FEI or a global core reserve.

For all-pair duplication, total deletion loss/I(F)=M(f)/I(f), so a universal aggregate payment of this shortcut retains the arbitrary seed obligation exactly. This is a diagnostic, not a renamed equivalent formulation claimed as progress. Its root erasure is zero; physical descendants carry the seed entropy. The exact first unsupported universal line remains sum_i e_i D(mu_i||r_i)>=sum_i e_i log2(1/e_i)-K I for one finite K and every Boolean seed. No nonzero-erasure conditional remainder or general child reserve is paid here.

## executed validation with domain, arithmetic, commands and outputs

The original FROZEN_SPEC declared 1,847 labeled cases: all n=1,2,3 truth tables and nonempty parity-substitution subsets, plus d=2,4,6 bent/flip witnesses. The command hit its frozen 60-second runtime guard. out/ATTEMPT_1.json preserves that failed attempt; partial counters were not saved, so no partial assertion or coverage count is claimed. It reported a runtime assertion, not a mathematical identity failure. Neither runtime nor dimension was increased.

TARGETED_SPEC was then saved before a smaller run: all n=1,2 truth tables and nonempty subsets (52 functions), plus the three bent/flip witnesses, 55 cases total; no symmetry reduction, maximum physical dimension eight. Integer Walsh transforms, direct physical flips, Fraction normalizers, exact prime-log coefficient identities and rational mass bounds. Memory estimate 100 MB, unmeasured; no job over 300 MB or memok trigger. Targeted v2 PASS: 2,365 assertions. After deriving the positive binary repair, SPEC_REVISION froze its additional checks on the same domain; the old PASS is preserved as CHECK_v2.json.

Final command: python -X utf8 runs/{RID}/code/check.py --targeted. PASS {ck['assertions']} exact assertions, {ck['cases']} cases, {ck['runtime_seconds']:.4f} seconds, out/CHECK.json. It verifies spectra, physical influences, H/M transport, full/coarsened row normalizers, exact deleted-partner KL loss, opposite binary reference, actual non-product conditionals and witness mass bounds. The analytic proof gives all seeds, subsets and even dimensions; finite checks are not extrapolated to those quantifiers. Intake command: python -X utf8 runs/{RID}/code/intake.py.

## proof dependencies and changed downstream conclusions

The new scoped audit is self-contained Boolean character expansion, direct pivotal counting, KL chain rule and elementary entropy/Jensen bounds; no unreviewed source payment theorem is used. Adopt the saved A073 and A001 independent acceptances of A096-TERMINAL-KL-REFUND-AUDIT@1 at full original scope, including constants and sublinear cutoff quantifiers. Their review does not pay K_M. A001's low-prefix/coarse-tail and A090's degree-only exclusions are consumed as specific objections, remaining pending their own independent review here.

The proposed ledger keeps existing A021 correction propagation, A098 T12 review and A090 tail acceptance source-bound, and adds the new exact loss/repair distinction. A generic single-bit marginalization allowance must be marked refuted at the precise local rate above. The original accepted full conditional reference is unchanged. No broad universal candidate is opened; this is a narrow mechanism audit under the pending-claim cap. There is no universal erasure constant improvement or FEI disproof.

## one next mathematical action and independent reviewer

On a nonzero-erasure shared-coordinate row, retain its informative likelihood-ratio statistic and cancel only conditionally common core factors; explicitly retain and price any conditional remainder once against certified child slack. Do not charge it to bit count or the queried/erased pair alone. A001 audits quantifiers/terminal ownership, A073 independently checks the complete normalized quotient, and A085 challenges the local witness and zero-erasure scope. A097/A099 consume the source-bound conditional interface; no message was sent to them.

## actual persistence receipts or precise save blocker

All four protocol files are saved in the assigned run with code/out, immediate DERIVATION.md, both frozen domains, SPEC_REVISION, failed-attempt receipt, two PASS outputs, complete report bundle, dependency/counterexample ledger and source manifest. STATUS has two lines, WORKLOG is appended and LEARNED updated. Final schema and SHA256 readback receipts are in out/SCHEMA_CHECK.json and out/RECEIPTS.json. Every file is below 20 MB; only A096 was written. Supervisor copying, canonical adoption, mirrors and independent review of the new claim remain unverified. No local persistence blocker exists.

## Universal bridge

This stage moves C018 by giving an exact zero-loss binary quotient for a genuinely correlated derivative row and proving that the opposite one-bit deletion loses the original terminal M_i, at a locally unbounded ratio between d-1 and d on an actual Boolean family with H/I<=3. It also consumes independent full-scope acceptance of the preceding terminal KL audit. The universal payment improvement is zero: arbitrary nonzero-erasure rows and their retained terminal-core divergence remain unpaid. NEXT targets a conditional likelihood-ratio partition with one certified terminal reserve, because the exact source-owned loss identifies what that reserve must pay and why smaller degree summaries or local spectator allowances cannot close full FEI; the zero-erasure example itself is not offered as another class theorem.
'''
(RUN/'REPORT.md').write_text(report,encoding='utf-8')
(OWN/'STATUS.md').write_text('STATE: A096 stage 4 proves exact binary KL repair for correlated parity-pair row; opposite one-bit deletion has unbounded local influence price despite H/I<=3; 55 cases/2,719 exact checks PASS; FEI OPEN.\nNEXT: A001/A073/A085 review; extend conditional likelihood-ratio retention to a nonzero-erasure shared row, debit exact remainder once to certified terminal slack; adopt source-bound ledger delta.\n',encoding='utf-8')
with (OWN/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(f'\n### {RID}; saved {stamp}\nConsumed A001 bounded-tail/A090 degree objections and A001/A073 full audit acceptances. Proved partial parity-duplication refund ownership; deleting one correlated partner loses M_i(seed), retaining only it has zero KL loss. Bent/flip witness gives local loss/Inf in [d-1,d] but H/I<=3. Large frozen pilot reached 60s guard; smaller declared 55-case checker passed 2365 assertions, then 2719 with the new positive binary checks, {ck["runtime_seconds"]:.4f}s. Intake: 301 reports, 553 claims, 579 dependency records, 100 packets. No universal constant paid.\n')
with (OWN/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\n## Stage 4 conditional spectator ownership\nFor partial physical parity duplication F_J: H unchanged, I increases by sum_J e_i, M loses sum_J M_i. Duplicated query rows have B=M=0 and D=log2(1/e_i). Deleting their one partner occupancy loses exactly M_i(seed); keeping ONLY that partner instead preserves complete KL exactly with mu=(0,1),r=(1-e_i,e_i). This retains derivative-free reference mass and cancels conditionally identical core laws, not only independent factors. For actual bent/flip selector g on even d+1 bits, duplicated selector witness has each influence delta=2^-d, I=d/2+(d+2)delta,H/I<=3, while partner-deletion loss/Inf lies in [d-1,d]. Local queried/erased-pair payment fails; global terminal bill persists. New positive quotient is a zero-erasure boundary, not arbitrary-row payment. A001/A073 independently accept prior A096 terminal KL audit at full scope. 55 actual cases/2719 exact checks PASS; larger pilot stopped at frozen 60s guard without saved partial counters.\n')
fields=load(BASE/'EXECUTION_PROTOCOL.json')['required_per_run']
assert set(progress)=={x.replace(' (one primary ID, for compatibility)','') for x in fields['progress_fields']}
for c in load(RUN/'CLAIMS.json'):assert set(c)==set(fields['claim_fields'])
assert all(s in report for s in fields['report_fields'])
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
assert len((OWN/'STATUS.md').read_text().splitlines())==2
assert all(p.stat().st_size<20*1024*1024 for p in RUN.rglob('*') if p.is_file())
save(RUN/'out/SCHEMA_CHECK.json',{'status':'PASS','progress_fields':'EXACT','claim_fields':'EXACT','report_fields':'PRESENT','packet_delta':'BYTE_IDENTICAL','status_lines':2,'files_under_20mb':True})
receipts=[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size} for p in sorted(RUN.rglob('*')) if p.is_file() and p.name!='RECEIPTS.json']
receipts +=[{'path':str(OWN/name),'sha256':sha(OWN/name),'bytes':(OWN/name).stat().st_size} for name in ['STATUS.md','WORKLOG.md','LEARNED.md']]
save(RUN/'out/RECEIPTS.json',receipts)
print(json.dumps({'schema':'PASS','receipted_files':len(receipts),'full_fei':'OPEN','report_bytes':(RUN/'REPORT.md').stat().st_size},indent=2))
