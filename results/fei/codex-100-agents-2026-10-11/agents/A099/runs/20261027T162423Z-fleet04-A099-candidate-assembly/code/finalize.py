from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,re
R=Path(__file__).resolve().parents[1];A=R.parents[1]
OLD=A/'runs/20261026T233346Z-fleet04-A099-candidate-assembly'
def load(p):return json.loads((R/p).read_text(encoding='utf-8'))
def put(p,x):(R/p).write_text(x if isinstance(x,str) else json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(x):return hashlib.sha256(x).hexdigest()
now=datetime.now(timezone.utc).isoformat();main=load('out/VALIDATION.json');pilot=load('out/PILOT.json')
claims=load('out/BASELINE_CLAIMS.json');dag=load('out/BASELINE_DAG.json')
new=[]
sources=[('20261027T062634Z-fleet04-A012-sparse-activation-accounting',0,'thm:v12-bill',['C005']),('20261027T092641Z-fleet04-A097-cross-route-transfer',0,'lem:v12-update',['A012-UNIVERSAL-PROJECTION-PROFILE-HISTORY']),('20261027T092641Z-fleet04-A097-cross-route-transfer',1,'prop:v12-moment',[]),('20261027T124307Z-fleet04-A093-literature-and-priority',0,'prop:v12-forward',[])]
priorreviews=json.loads((R/'out/sources/20261027T125558Z-fleet04-A098-resource-reallocation-CLAIMS.json').read_text(encoding='utf-8'))
for run,idx,label,deps in sources:
 c=json.loads((R/'out/sources'/(run+'-CLAIMS.json')).read_text(encoding='utf-8'))[idx]
 candidates={'raw':sha(c['exact_statement'].encode())}
 for key in ['statement','exact_statement']:
  for ascii in [False,True]:candidates[key+str(ascii)]=sha(json.dumps({key:c['exact_statement'],'hypotheses':c['hypotheses']},sort_keys=True,separators=(',',':'),ensure_ascii=ascii).encode())
 matched=[k for k,v in candidates.items() if v==c['statement_sha256']];assert matched,(c['claim_id'],candidates)
 for reviewed in priorreviews:
  if reviewed['claim_id']==c['claim_id']:
   assert reviewed['statement_sha256']==c['statement_sha256']
   for record in reviewed['review_records']:
    if str(record.get('reviewer','')).startswith('A098'):c['review_records'].append(record)
 c['review_records'].append(dict(reviewer='A099',timestamp=now,status='SCOPED_ANALYTIC_RECONSTRUCTION_HOLDS_UNCHANGED',source_statement_sha256=c['statement_sha256'],hash_conventions=matched,proof='STAGE12_ADDITIONS.tex; code/check.py; out/VALIDATION.json',limits='Different direct-Walsh and Fraction implementation; no author checker executed. Analytic all-dimensional statements plus exact bounded tests. Neither integrated-chain audit supplied; no Lean certification inferred.'))
 c['status']='SCOPED_SOURCE_RECONSTRUCTION_HOLDS_FULL_FEI_OPEN';claims.append(c);new.append(c)
 dag['nodes'].append(dict(claim_id=c['claim_id'],version=c['version'],proof_dependencies=deps,tex_label=label,statement_sha256=c['statement_sha256']))
put('CLAIMS.json',claims);put('out/PROOF_DEPENDENCIES.json',dag)
base=(R/'out/BASELINE_v11.tex').read_text(encoding='utf-8')
base=re.sub(r'\\date\{[^\n]*\}',lambda m:r'\date{27 October 2026; assembly version 12}',base,count=1)
addition=(R/'STAGE12_ADDITIONS.tex').read_text(encoding='utf-8');assert base.count(r'\end{document}')==1
text=base.replace(r'\end{document}',addition+'\n'+r'\end{document}');put('CANDIDATE_MANUSCRIPT.tex',text)
formal=(R/'out/LEAN.log').read_text(encoding='utf-16') if (R/'out/LEAN.log').read_bytes().startswith(b'\xff\xfe') else (R/'out/LEAN.log').read_text(encoding='utf-8-sig')
put('out/FORMAL_STATUS.json',dict(output=formal,scope='Optional rational ledger rearrangement only; not a certification of the entropy/Boolean theorems',rung='NO_FULL_FORMAL_CERTIFICATION',admission='memok OK physical10.9GB commit21.7GB'))
report='''# A099 v12: complete query bills and reference-policy handoffs

## exact target, quantifiers, hypotheses and units

Assemble the strongest supported source into one standalone manuscript for C005--C006--C018--C019/C024. This stage integrates the complete projection-history ledger, affine-moment calibration, the high-moment query-loss obstruction, and the exact forward cost of switching to normalized true-kernel inheritance. All physical cubes are finite and uniform, Boolean outputs plus/minus one, entropy/CE/KL bits, influence physical. Old bookings, actual reaches, both full children, reference-only mass, full normalizers and fee orientation are retained. Full FEI remains OPEN; both independent integrated-chain audits remain pending.

## sources actually read, revisions and theorem locators

Fresh BOARD and own STATUS; B20 STREAM_NOTES v2 (2026-10-11); complete execution protocol revision2026-10-11-execution-v2. Previous campaign plan/registries/supplement and paper baselines are retained from v11 rather than advertised as a fresh full-source audit. The latest A094 run20261027T162148Z had no claim or proof file at intake and supplies no premise.

Original sources read and byte-pinned in out/SOURCE_RECEIPTS.json and out/sources: A012 run20261027T062634Z DERIVATION1--7, A097 run20261027T092641Z PROOF1--5, A093 run20261027T124307Z DERIVATION1--5; A011 run20261027T025625Z DERIVATION1--4; A094 run20261026T232939Z REPORT; A100 run20261027T023227Z REVIEW; A098 run20261027T125558Z REVIEW and exact claim records. A098 scoped reviews are imported only where exact statement hashes match. No board summary is an independent acceptance. A single read-only math-brain search supplied generic route cautions but no new mathematical premise; unrelated recall hits are not dependencies.

## complete derivation or exact first unsupported line

Complete proofs are in STAGE12_ADDITIONS.tex, inserted literally into standalone CANDIDATE_MANUSCRIPT.tex. For projection inheritance BOTH children use pi_i Q. The exact local true-divergence change is J_i-L_i, where L_i is the FULL projection contraction and J_i the true child JS. The direct scalar proof gives J_i<=2Inf_i/ln2, including coefficient signs and endpoints. The complete transaction bill is exactly U+CEroot+sum reached J+sum reached G, where G=D(R||Q)+D(P||R)-D(P||Q). Thus permitted partition calibrations have G<=0, and affine information projections containing P have G=0. The support proof handles boundary minimizers; the full forward fee is paid once by the CE decrease. Finite adaptivity telescopes at true reaches, not reference outcome probabilities. The bound more precisely uses retired influence Iroot-E Ileaf; this is the original proof's influence telescope, not a changed universal constant.

The high-moment AND2 tensor family matches the vacuum and every marginal of order<=n-2 at a rate-four ORIGINAL complete reference, while every first query i<=n-1 loses L_i between n-1/4 and n. Matching these moments causes zero affine-calibration release and cannot justify a local O(Inf_i) price. These are alternative first queries; their invoices cannot be summed as repeated losses on one path. The first such projection consumes the original mismatch. H/I=2, so FEI is not refuted.

The actual AND3 source CE=3=4I has a projection-to-true-kernel handoff with excess 3log2(5)/32 averaged over BOTH children. The nonconstant child starts matched and pays a strictly positive symmetric KL. This forward finite-fee guard is separate from A012's reverse-infinite AND2 support guard. Neither invalidates the scoped history theorem. A required handoff must pay its actual G from the SAME diminished original owner. The ledger depends on the policy, not merely its name.

A011 v5's terminal-to-transaction identification is withdrawn at its original scope: Braw=Hroot+mean Dterminal+Qloss, rather than Hroot+mean Dterminal. Its v6 inherited/vacuum policy is a distinct repair. Neither v5 numerical reserves nor v6 root constants are accepted anew here; the false identification is not a premise of this source. Valid earlier inherited-CE identities remain scoped to their stated costs.

A012's arbitrary-reference activation extraction is also reconstructed, so its bundled source claim is not accepted only at an unlabelled fragment. For balanced g and fresh point controls, CE_F>=A_r+p CE_g for the actual reference extracted from ANY complete Q_F. Disjoint balanced tensor amplification converts a universal initial supplier on these activations to full FEI with the same K; no finite numerical extrapolation occurs.

FIRST UNSUPPORTED UNIVERSAL LINE: construct a useful influence-priced ORIGINAL complete reference for every Boolean core, or pay a necessary compatible conversion/stopping obligation from actual unused original capacity after all old charges and both full terminal liabilities. Choosing Q=P starts at CE=H and does not establish CE<=K I. No new absolute FEI constant or divergent Boolean H/I family is proved.

## executed validation with domain, arithmetic, commands and outputs

Frozen out/FROZEN_SPEC.json precedes the pilot and main searches and pins checker/helper bytes. Commands from A099: python -B -X utf8 runs/20261027T162423Z-fleet04-A099-candidate-assembly/code/init.py; code/check.py --pilot; code/check.py; code/finalize.py; code/seal.py. Pilot and main results are separate below. Full code and outputs are local; no author checker was imported or executed. Direct literal Walsh summation and direct physical edge counts independently reconstruct spectra and influence. Arithmetic is Fraction, prime-log linear cancellation and proved outward rational atanh bounds. Scalar J ln2<=2Inf uses outward rational upper bounds; all sign verdicts are rigorous on the tested domain.

MAIN_RESULTS

The 44 small outcome-dependent stopping trees include old charged fees via the exact identity, projection losses and complete leaves. The three inverse-tilt affine fixtures have different true and minimizing laws with equal vacuum/degree moments; an extreme feasible boundary pins a constant law. Partition-update endpoints0,1 and interior1/2 include reference-only cells. The AND3 guard covers all16 translations/output signs x3 queries x2 children, without a symmetry quotient. High-moment n4,6,8,10 fixtures verify full rational spectra, exact moments through n-2, positive full support, and every relevant first projection. Analytic parity cancellation and the exact formula prove all even n>=4, not finite extrapolation. All22 labelled cores n<=2 with m1,2 and r1,2 give88 literal activated sources and arbitrary correlated reference tests. The allocation policy is not inferred from these bounded tests.

Estimated checker memory140MB; each frozen pilot/main cap55s, no automatic escalation, GPU, detached research job or unrelated workload change. Optional Lean admission passed memok with physical10.9GB and commit21.7GB free. Its exact output is saved in out/LEAN.log and out/FORMAL_STATUS.json. The target is only a rational ledger rearrangement; even a pass would not certify KL, scalar entropy, affine support or Boolean claims. No full Lean theorem or PDF build is claimed.

## proof dependencies and changed downstream conclusions

The33 v11 claim records remain; four unchanged source statements give37 records and57 DAG nodes. Actual proof dependencies are acyclic and resolved. A012's profile identity and affine support argument are rederived in the additions; no unreviewed v8 class theorem is silently imported. A098's existing scoped review records are preserved for the two A097 statements and A093 guard; A099 adds a separate direct implementation/reconstruction. These are scoped reviews, not either full-chain acceptance. All four previous universal conjectures remain explicit and unchanged.

Downstream consumers must retain the query contraction under the selected policy and charge forward handoffs through G. Moment matching is compatible with an order-n invoice and cannot renew original mismatch. The complete history theorem isolates stability from initial source pricing. Universal numerical improvement: zero. This is a synthesis of universally quantified conditional accounting and exact route obstructions, not another isolated finite FEI class claim.

## one next mathematical action and independent reviewer

A050/A011/A097 must construct a productive arbitrary-core ORIGINAL O(I) source or specify a necessary stricter interface with actual reached G paid from SAME unused original B-C-U. A012/A096 should use the explicit projection convention; A085/A094 should independently challenge the full chain, especially query-KL ownership, handoff direction and both full terminal liabilities. These are saved handoffs, not messages sent or claimed adoptions. Further admitted-history examples cannot replace this source theorem.

## actual persistence receipts or precise save blocker

REPORT, CLAIMS, PROGRESS and byte-identical PACKET_DELTA have protocol fields. Source copies/hashes, frozen spec, portable checker/helper, pilot/main outputs, complete additions, standalone source, dependency graph, formal status and readback receipts are saved inside this A099 run. Rolling STATUS has exactly two lines; dated WORKLOG and LEARNED record the mathematical delta. Every artifact is below20MB. Local persistence is checked; supervisor copying, remote mirrors, downstream use and public release remain UNVERIFIED. No git, mail, brain writes, other-agent edits, trading access or external mutation occurs. Brain self-care is degraded/unverified: stale owner-model, state and dream notes affect personal-context continuity, not the directly checked mathematical premises.

## Universal bridge

C024 history transfer and C019 stopping-tree payment advance through a complete universally quantified projection/affine full-fee ledger, while C020 source compatibility gains the exact positive forward-handoff invoice and high-order moment guard. The numerical universal FEI improvement is zero. C018 and full FEI stay OPEN: original arbitrary-core O(I) source pricing or a necessary compatible conversion paid from actual unused original capacity remains unproved. NEXT attacks that supplier/interface obligation because history stability is now explicitly paid and no optional reset, moment match or omitted query contraction can close the initial-source gap.
'''
report=report.replace('MAIN_RESULTS',f"Pilot PASS: {pilot['exact_assertions']:,} exact assertions in{pilot['seconds']:.4f}s on{pilot['tables']} Boolean tables. Main PASS: {main['exact_assertions']:,} exact assertions in{main['seconds']:.4f}s on{main['tables']} tables n0..3;{main['queries']} local physical-query checks including trees/guards;{main['updates']} profile updates;{main['trees']} adaptive small trees;{main['affine_fixtures']} inverse-tilt affine fixtures;{main['moment_fixtures']} moment-family fixtures;{main['handoff_queries']} AND3 handoff queries;{main['activation_fixtures']} literal activation fixtures. Pilot/main counts are never pooled.")
put('REPORT.md',report)
progress=json.loads((OLD/'PROGRESS.json').read_text(encoding='utf-8'))
progress.update(run_id=R.name,attempt_id='A099-assembly-v12',method='Independent exact-source integration of full projection-query/affine-fee ledger, high-moment obstruction and forward policy-handoff cost',mathematical_delta='Four exact source claims reconstructed; complete bill=U+CEroot+sumJ+sumG. Projection contractions retained; affine/full profile fees paid once; high moment matching does not price queries; true-kernel handoff on AND3 costs3log2(5)/32 extra. Universal initial source remains open.',deliverable_status='COMPLETE_LOCAL_SOURCE_ASSEMBLY_AND_SCOPED_REVIEWS',mathematical_status='SCOPED_ANALYTIC_PROOFS_EXACT_FINITE_CHECKS_FULL_FEI_OPEN',claims_created_or_changed=[c['claim_id']+'@1' for c in new],source_artifacts=['CANDIDATE_MANUSCRIPT.tex','STAGE12_ADDITIONS.tex','CLAIMS.json','out/SOURCE_RECEIPTS.json','out/FROZEN_SPEC.json','out/VALIDATION.json','out/FORMAL_STATUS.json','out/FINAL_RECEIPTS.json'],next_consumers=['A011','A012','A050','A085','A093','A094','A096','A097','A098','B20'],next_action='Construct useful ORIGINAL arbitrary-core O(I) source or pay REQUIRED forward interface G from SAME diminished owner, with full query KL, old U and both terminals. A085/A094 reconstruct integrated chain.',stagnant_substantive_attempts=0,blockers=['Arbitrary-core initial source or necessary paid interface still unproved','Two independent integrated-chain audits pending','No full formalization or PDF build; scalar formal status recorded separately','Supervisor mirrors/adoption unverified'])
progress['claim_versions_used'] += [dict(claim_id=c['claim_id'],version=c['version']) for c in new]
put('PROGRESS.json',progress);put('PACKET_DELTA.json',progress)
(A/'STATUS.md').write_text(f"STATE: A099 v12 saved: full projection/affine bill plus moment/handoff guards reconstructed;{main['exact_assertions']} exact main checks PASS;37 claims/57 DAG nodes;full FEI OPEN.\nNEXT: A050/A011/A097 construct ORIGINAL arbitrary-core O(I) source or pay REQUIRED forward G from SAME unused owner;query KL/old U/BOTH terminals retained;A085/A094 integrated audits pending.\n",encoding='utf-8')
for name,line in [('WORKLOG.md',f"A099 v12: integrated four unchanged claims; {main['exact_assertions']} exact main checks in{main['seconds']:.4f}s; policy-specific full query fees, paid affine updates, moment invoice and forward handoff3log2(5)/32. Initial arbitrary-core supplier and full-chain audits OPEN."),('LEARNED.md','Projection full bill equals U+CEroot+sum reached JS+sum reached G, G=D(new||old)+D(P||new)-D(P||old). Affine information projections containing P have G=0; partial-profile mixtures have G<=0. A switch to normalized true-kernel inheritance need not: AND3 uniform root rate4 has mean G=3log2(5)/32>0. Matching ALL marginals through n-2 at rate4 does not bound query contraction by coordinate influence; n-1 alternative first queries lose nearly n KL on AND2 tensors, consuming the SAME original mismatch once. Initial reference CE=O(I) remains the FEI-level unpaid step.')]:
 with (A/name).open('a',encoding='utf-8') as f:f.write('\n'+now+': '+line+'\n')
print(json.dumps(dict(saved=True,claims=len(claims),nodes=len(dag['nodes']),main_assertions=main['exact_assertions'],full_FEI='OPEN')))
