"""Persist this A043 continuation and validate the protocol schema. No external writes."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,runpy
R=Path(__file__).resolve().parents[1];A=R.parents[1];O=R/'out'
P=Path(r'math-open-problems/reports\fei-2026-10-11')
B=Path(r'math-open-problems/research_pushes\2026-10-11-full-fei-100-agents')
C=Path(r'context')
OLD=A/'runs/20261014T052009Z-account05-A043-prime-gate-decomposition'
def read(p):return p.read_text(encoding='utf-8')
def write(p,s):p.write_text(s,encoding='utf-8')
def dump(p,x):write(p,json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
runpy.run_path(str(R/'code/check_corner.py'),run_name='__main__')
checks=json.loads(read(O/'checks.json'));corner=json.loads(read(O/'corner_checks.json'))
assert checks['status']==corner['status']=='PASS'
assert checks['helper_sha256']==digest(R/'code/check_reserve.py')
assert corner['helper_sha256']==digest(R/'code/check_corner.py')
protocol=json.loads(read(P/'EXECUTION_PROTOCOL.json'))
oldprogress=json.loads(read(OLD/'PROGRESS.json'))
rawclaims=json.loads(read(OLD/'CLAIMS.json'))
if isinstance(rawclaims,dict):rawclaims=rawclaims.get('claims',[rawclaims])
used=[{k:c[k] for k in ('claim_id','version','statement_sha256') if k in c} for c in rawclaims]
sources=[P/x for x in ('EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex')]
sources += [B/x for x in ('CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md')]
sources += sorted((B/'sources').glob('*.md'))+sorted(C.glob('*.txt'))
sources += [OLD/'PROOF.md',OLD/'REPORT.md',OLD/'CLAIMS.json',OLD/'PROGRESS.json',A/'LEARNED.md',A/'STATUS.md',A/'WORKLOG.md',A.parents[1]/'BOARD.md',A.parents[1]/'claude/B09/STREAM_NOTES.md']
receipts=[]
for p in sources:
 if not p.exists():receipts.append({'path':str(p),'missing':True});continue
 data=p.read_bytes()
 try:text=data.decode('utf-8');encoding='utf-8'
 except UnicodeDecodeError:text=data.decode('cp1252');encoding='cp1252'
 hits=[line for line in text.splitlines() if any(q in line.lower() for q in ('a043','prime','singleton','composition','entropy'))]
 receipts.append({'path':str(p),'sha256':hashlib.sha256(data).hexdigest(),'encoding':encoding,'bytes':len(data),'inspection':'complete text decoded; relevant excerpts inspected; no theorem inferred from a digest','excerpt':hits[:2]})
dump(O/'source_receipts.json',receipts)
now=datetime.now(timezone.utc).isoformat()
statement=('For every Boolean sign f in every finite dimension and every interior independent product law, in natural units let Delta=I-Var, R=sum_{|A|>=3}(|A|-2)P(A), S=4Delta-2R-E_single. With v_i=4p_i(1-p_i), t_i=|E D_i|, d_i=E D_i^2 and S_m=sum_i v_i[2(d_i-t_i)+t_i(1-t_i)sum_{k=1}^m 2(1-t_i)^k/(k(k+1))], every integer m>=0 satisfies 0<=S_m<=S_{m+1}<=S and S-S_m<=2(2Delta-R)/(m+1)<=4Delta/(m+1). The last coefficient is sharp, approached by AND2 at equal biases tending to zero. For actual reflected prime56067 at (alpha,e,d,q)=(t,t^2,t^4,t), fixed m and t->0, (S_m-4T)/T->-4/(m+1), whereas (S+2T-G)/T->6. Thus every fixed-order sufficient assertion S_m>=4T is false; actual G<=S+2T and full FEI remain unresolved.')
claim={'claim_id':'A043-RETAINED-SLACK-POLYNOMIAL-HIERARCHY','version':1,'exact_statement':statement,
 'hypotheses':['Boolean values {-1,1}; finite n; independent input coordinates; interior biases, with deterministic coordinates contracted for endpoint statements','Natural entropy units; actual biased orthonormal squared spectrum; nonempty corrected entropy','m is a fixed nonnegative integer before any corner limit; t in (0,1/2) for the prime56067 path'],
 'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),'contributors':['A043'],
 'proof_source':['PROOF.md','code/check_reserve.py','out/checks.json','code/check_corner.py','out/corner_checks.json'],
 'proof_dependencies':[{'source':str(OLD/'PROOF.md'),'sha256':digest(OLD/'PROOF.md'),'scope':'prime56067 polynomial and G ledger; Fourier variance identity reconstructed in current proof'}],
 'review_records':[],'status':'PROVED_AUTHOR_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[],
 'first_unproved_line':'No unproved line in the stated hierarchy or fixed-order obstruction. The target G<=S+2T on every prime56067 law and all-arity actual cofactor packet payment remain OPEN. Lean SETUP_UNVERIFIED: compute admission held; no compiler was started.',
 'next_consumers':['A042','A044','A091','B20']}
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
dump(R/'CLAIMS.json',[claim])
progress={'protocol_revision':protocol['revision'],'run_id':R.name,'stream':'B09','packet_id':'A043',
 'gap_id':oldprogress['gap_id'],'attempt_id':R.name+'-retained-slack-hierarchy',
 'method':'Repair actual singleton reserve by a positive logarithm series, exact rational truncations, sharp Boolean lower path, and a signed prime cofactor corner obstruction.',
 'mathematical_delta':'Dimension-independent sharp approximation error 4Delta/(m+1), with refined error 2(2Delta-R)/(m+1); second term repairs old witness; every fixed-order S_m>=4T shortcut refuted on an actual prime56067 interior path. No new universal FEI constant.',
 'deliverable_status':'COMPLETE_LOCAL_PENDING_INDEPENDENT_REVIEW','mathematical_status':'AUTHOR_PROOF_FOR_STATED_LEMMA_AND_ROUTE_OBSTRUCTION; FULL_FEI_OPEN',
 'claim_versions_used':used,'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1}],
 'source_artifacts':['PROOF.md','out/frozen_spec.json','out/checks.json','out/corner_frozen_spec.json','out/corner_checks.json','out/source_receipts.json'],
 'next_consumers':claim['next_consumers'],
 'next_action':'Price actual G against S_m+2T plus the exact omitted tail, retaining original packet ownership; do not replace G by 6T and seek S_m>=4T for fixed m. A042/A091 independently reconstruct the hierarchy and corner limit.',
 'stagnant_substantive_attempts':0,
 'blockers':['Independent review pending; no acceptance claimed.','Lean check returned SETUP_UNVERIFIED because compute admission was held; no compiler process started.','Universal bounded-congestion ownership for actual cofactor profiles remains unpaid.'],
 'packet_ids':['A043']}
fields={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
assert set(progress)==fields
dump(R/'PROGRESS.json',progress);write(R/'PACKET_DELTA.json',read(R/'PROGRESS.json'))
gaps=checks['old_witness']['S_m_minus4T']
report=f'''# exact target, quantifiers, hypotheses and units

Repair the actual singleton reserve in B09's all-product-bias prime route. For every finite-dimensional Boolean sign under every interior independent product law and every integer m>=0, the polynomial lower reserve S_m increases to S with error at most 2(2Delta-R)/(m+1)<=4Delta/(m+1), in natural entropy units. The last coefficient is sharp on actual AND2 gates. Every fixed-m sufficient strengthening S_m>=4T fails on an interior path of the actual prime56067. Full FEI remains OPEN; no new all-arity FEI constant is claimed.

# sources actually read, revisions and theorem locators

EXECUTION_PROTOCOL.json revision {protocol['revision']} was read in full. BOARD.md snapshot 2026-10-22 21:06 UTC, B09 STREAM_NOTES.md v2 (2026-10-11 23:33), own rolling files and the documented stage-five PROOF.md/REPORT.md were consumed. The later named 20261021T142724Z directory has no REPORT.md; its existence is not treated as a mathematical result. Campaign indices, supplemental source notes and all four paper text versions were decoded and inspected with source hashes and excerpts in out/source_receipts.json. Threshold Proposition7.1 is the composition locator; the new hierarchy does not depend on an unverified extension of it. Legacy campaign dates in the static indices do not override the current task's 23 October deadline. A read-only two-wording math recall returned no source for this hierarchy; its Booleanity warning is respected. Wake flagged stale personal-context notes, which were not used.

# complete derivation or exact first unsupported line

PROOF.md gives the complete author derivation. The exact identity sum_i v_i Var(D_i)=2Delta-R transfers a scalar tail bound to the original spectral deficit, with no added reserve. Expand phi(t)=2t(1-t)-t^2 ln(1/t^2) as t(1-t)sum_{{k>=1}}2(1-t)^k/[k(k+1)]. Truncation at m leaves a nonnegative tail bounded by 2t(1-t)/(m+1). Booleanity gives d_i>=|c_i| and therefore the claimed error. Rare AND2 proves coefficient optimality. Zero singleton coefficients, unit coefficients, Delta=0, m=0 and deterministic-coordinate contraction are treated explicitly.

At the old rational witness, S_1-4T={gaps['1']}<0, whereas S_2-4T={gaps['2']}>0. This repairs that witness only. A different path (alpha,e,d,q)=(t,t^2,t^4,t) has T=4t^4(1-t)^2(1-t^6) and (S_m-4T)/T -> -4/(m+1) for each fixed m. Thus raising a fixed truncation order cannot prove that stronger sufficient assertion globally. The actual sharp residual divided by T tends to 6, so this path refutes neither actual sharp payment nor FEI.

First unpaid sharp line: G<=S+2T over all four interior biases. First unpaid universal line: assign arbitrary actual cofactor-profile costs to nonreused higher-degree packets and terminal entropy with bounded congestion. The approximation theorem pays no such cost.

# executed validation with domain, arithmetic, commands and outputs

Frozen specifications precede each search in out/frozen_spec.json and out/corner_frozen_spec.json. Command: python -X utf8 code/check_reserve.py. It completed {checks['boolean_cases']} Boolean fixtures and {checks['scalar_cases']} scalar fixtures with {checks['assertions']} exact assertions in {checks['runtime_seconds']:.6f} seconds. Domain: all functions n<=2 on the three-point bias grid; all ternary functions at fair law; five ternary prime representatives on that grid; 625 four-bias prime56067 grid points; the old rational witness; five rare-AND paths. These are declared fixtures with some overlap, not a count of distinct functions. Arithmetic is Fraction moments/direct physical derivatives and 24-term outward rational atanh log intervals after range reduction. All hierarchy checks pass. The 625 moderate prime fixtures have zero S_1>=4T failures; the thin old witness is outside that grid, so those facts agree.

Command: python -X utf8 code/check_corner.py. At t=1/1024 it independently verifies the actual truth table, all ten proper-block primality tests, direct derivative means and their displayed formulas, and negative S_m-4T for m=0,1,2,4,8,16,32. Output: {corner['assertions']} exact assertions, {corner['runtime_seconds']:.6f} seconds. This one-point certificate supplements the analytic all-fixed-m limit; it does not replace that limit. Helpers' SHA256 values are pinned in their outputs and checked again during finalization.

Checks that could fail were the factor of two in derivative normalization, endpoint logarithms, a zero Delta denominator, sign-cell absolute values, a non-Boolean witness, an invalid prime mask, and an exchange of m with the corner limit. Direct derivative/Fourier reconstruction, scalar endpoints, exact mask/block checks and the stated quantifier order address them. Booleanity is necessary: the real-valued one-bit f(x)=x-1/2 on {{0,1}} has Delta=0 but negative S. The requested Lean finite-tail coefficient check returned SETUP_UNVERIFIED: compute admission held (hung window or under5500MB free); no compiler process started. No Lean-checked claim is made and no repeated compiler attempt was launched.

Memory estimates were60MB and30MB, both below300MB; no memok admission was needed. No heavy job, dimension escalation, detached process or process termination was used. The current compute snapshot showed high CPU/commit pressure and7.6GB free disk; work remained lightweight. The initial source-receipt write preceded creation of out/ and failed; finalization reread the sources and saved the receipt successfully. Mathematical check outputs were unaffected.

# proof dependencies and changed downstream conclusions

The hierarchy and sharp approximation error are reconstructed from Boolean derivative variance and a positive scalar series. The stage-five actual prime polynomial/G ledger is source-bound by hash; the new corner independently checks its truth table and primality. Existing nonsharp prime56067 and disjoint-composition theorems remain unchanged. The unregistered fixed-order sufficient shortcut is false for every m, but G<=S+2T is not refuted. Rung: author proof plus exact certificates, pending independent review. There are no independent acceptance records for this version.

# one next mathematical action and independent reviewer

Pay actual G against S_m+2T with the exact omitted tail, retaining the original cofactor packet owners. Do not continue seeking S_m>=4T for a fixed order: (6) closes that mechanism. A042 or A091 should reconstruct the series/error identity and the all-fixed-m corner separately; A044 can check the direct cofactor representation. These are proposed consumers, not messages sent or reviews received.

# actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json, byte-identical PACKET_DELTA.json, PROOF.md, code/ and out/ are saved in the requested A043 run. STATUS.md has two lines; WORKLOG.md and LEARNED.md are appended. out/schema_validation.json checks exact protocol field sets, statement/helper hashes and compatibility; out/persistence_receipts.json records local file hashes. Completed locally at {now}; the directory timestamp is the requested stage label, not a claim about execution start. No local persistence blocker. Supervisor copy, GitHub save, mirror verification, brain ingestion and independent acceptance are not claimed. No git or shared-tree mutation was performed.

**Universal bridge:** This stage moves B09's all-arity product-biased prime endpoint by replacing an uncontrolled loss of singleton slack with a dimension-independent, sharp error4Delta/(m+1), and by closing the entire fixed-order S_m>=4T shortcut with an actual irreducible-gate path. The missing theorem is still an all-arity payment of actual higher-degree cofactor costs from the same spectral deficit and terminal reserve. Pricing G itself with the exact tail is the shortest surviving next step: it retains the cancellation that makes the failed corner's actual residual positive, whereas another fixed-order sufficient charge is now rigorously ruled out.
'''
write(R/'REPORT.md',report)
write(A/'STATUS.md','STATE: Stage17 complete locally: sharp universal reserve approximation 4Delta/(m+1); every fixed-order Sm>=4T shortcut false on actual prime56067; exact checks PASS; review pending; full FEI OPEN.\nNEXT: Pay actual G against Sm+2T plus exact omitted tail with original packet ownership; A042/A091 review hierarchy and fixed-m corner; no further fixed-order Sm>=4T search.\n')
with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(f'\n{now} — Continued documented stage5. Proved sharp dimension-independent singleton-reserve hierarchy, repaired old witness at m=2, and refuted every fixed-order Sm>=4T via interior prime56067 path. Main checks {checks["assertions"]} PASS, corner {corner["assertions"]} PASS. Lean admission held; no compiler started. Source receipt write retried after out creation. All results local; review/full FEI open.\n')
with (A/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\n2026-10-23 stage17: For all Boolean signs and product laws, Sm=sum vi[2(di-ti)+ti(1-ti)sum(k<=m)2(1-ti)^k/(k(k+1))] increases to S with sharp error <=2(2Delta-R)/(m+1)<=4Delta/(m+1). AND2 p->0 attains the last normalized error. S1 is the old polynomial bound; S2 repairs its old rational witness, but no fixed m gives Sm>=4T globally. Actual prime56067 path (alpha,e,d,q)=(t,t^2,t^4,t) has T=4t^4(1-t)^2(1-t^6), (Sm-4T)/T -> -4/(m+1), while actual (S+2T-G)/T ->6. Retain G and exact tail; avoid the now-closed stronger fixed-order charge. Author proof pending independent review; Lean admission held; full FEI OPEN.\n')
assert read(R/'PACKET_DELTA.json')==read(R/'PROGRESS.json')
assert len(read(A/'STATUS.md').splitlines())==2
assert hashlib.sha256(claim['exact_statement'].encode('utf-8')).hexdigest()==claim['statement_sha256']
for name in protocol['required_per_run']['report_fields']:assert '# '+name in report
dump(O/'schema_validation.json',{'status':'PASS','claim_fields_exact':True,'progress_fields_exact':True,'packet_delta_byte_identical':True,'statement_sha256_checked':True,'helper_hashes_checked':True,'status_lines':2,'completed_at':now})
artifacts=[p for p in R.rglob('*') if p.is_file() and p.name!='persistence_receipts.json']
assert all(p.stat().st_size<20*1024*1024 for p in artifacts)
dump(O/'persistence_receipts.json',[{'path':str(p.relative_to(R)),'sha256':digest(p),'bytes':p.stat().st_size} for p in sorted(artifacts)])
print(json.dumps({'artifact_status':'COMPLETE_LOCAL','mathematics':'author proof; independent review pending; full FEI OPEN','main_assertions':checks['assertions'],'corner_assertions':corner['assertions'],'schema':'PASS','saved_files':len(artifacts)+1,'run':str(R)}))
