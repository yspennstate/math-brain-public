from pathlib import Path
import json, hashlib, re
from datetime import datetime,timezone
R=Path(__file__).resolve().parents[1];A=R.parents[1]
def load(p):return json.loads((R/p).read_text(encoding='utf-8'))
def put(p,x): (R/p).write_text(x if isinstance(x,str) else json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(b):return hashlib.sha256(b).hexdigest()
now=datetime.now(timezone.utc).isoformat()
sources=R/'out/sources'
claims=load('out/BASELINE_CLAIMS.json');dag=load('out/BASELINE_DAG.json')
new=[]
for run,name,idx,label in [('20261023T140303Z-fleet03-A096-live-gap-ledger','A096',1,'lem:v11-ghost'),('20261023T143952Z-fleet03-A097-cross-route-transfer','A097',0,'lem:v11-floor')]:
 c=json.loads((sources/(run+'-CLAIMS.json')).read_text(encoding='utf-8'))[idx]
 statement=c['exact_statement'];hyps=c['hypotheses']
 candidates={'raw_statement':sha(statement.encode()),'statement_hypotheses':sha(json.dumps({'statement':statement,'hypotheses':hyps},sort_keys=True,separators=(',',':')).encode()),'exact_statement_hypotheses_unicode':sha(json.dumps({'exact_statement':statement,'hypotheses':hyps},sort_keys=True,separators=(',',':'),ensure_ascii=False).encode())}
 matched=[k for k,v in candidates.items() if v==c['statement_sha256']]
 assert matched,(c['claim_id'],candidates)
 c['review_records'].append(dict(reviewer='A099',timestamp=now,status='SCOPED_ANALYTIC_RECONSTRUCTION_AND_EXACT_CHECKS_HOLD',source_statement_sha256=c['statement_sha256'],hash_convention=matched,proof='STAGE11_ADDITIONS.tex; code/check.py; out/VALIDATION.json',limits='Statement unchanged. A097 proof derivative and inherited CE text use A093 corrections; not an independent acceptance of a new repaired version. Neither integrated-chain audit is supplied.'))
 c['status']='SCOPED_RECONSTRUCTION_HOLDS_FULL_FEI_OPEN'
 claims.append(c);new.append(c)
 dag['nodes'].append(dict(claim_id=c['claim_id'],version=c['version'],proof_dependencies=[],tex_label=label,statement_sha256=c['statement_sha256']))
put('CLAIMS.json',claims);put('out/PROOF_DEPENDENCIES.json',dag)
base=(R/'out/BASELINE_v10.tex').read_text(encoding='utf-8')
base=re.sub(r'\\date\{[^\n]*\}',lambda m:r'\date{27 October 2026; assembly version 11}',base,count=1)
addition=(R/'STAGE11_ADDITIONS.tex').read_text(encoding='utf-8')
assert base.count(r'\end{document}')==1
text=base.replace(r'\end{document}',addition+'\n'+r'\end{document}')
put('CANDIDATE_MANUSCRIPT.tex',text)
fields=load('out/READ_RECEIPTS.json')
validation=load('out/VALIDATION.json');pilot=load('out/PILOT.json')
report='''# A099 v11: signed admission and complete inherited references

## exact target, quantifiers, hypotheses and units

Assemble the strongest source-complete C005--C006--C018--C019/C024 argument while retaining every universal open leaf. This stage integrates two unchanged scoped source statements: sharp signed admission from arbitrary current references and ghost-complete inherited witness transport. All physical cubes are finite and uniform, Boolean values are plus/minus one, entropy/CE/KL are in bits, and influence is ordinary physical influence. Both full outcomes, true reaches, reference-only mass, old bills and original capacities remain explicit. Full FEI is OPEN. Two independent complete-chain audits remain pending.

## sources actually read, revisions and theorem locators

Execution protocol 2026-10-11-execution-v2; current BOARD, B20 STREAM_NOTES v2, own v10 report/status and standalone source. The archived registry snapshot is 2026-10-11, whereas the live board supplies newer navigation. README, CURRENT_STATUS, claim/obstruction/packet registries, stream actions, campaign plan, supplemental CAMPAIGN/CLAIMS/COUNTEREXAMPLES/SEED_LEMMAS/NATIVE_MAPPING and sources were freshly loaded and pinned in out/READ_RECEIPTS.json. Four paper text versions were loaded; threshold Proposition7.1 and Proposition8.6 locate the unchanged composition baseline. Percolation text explicitly excludes arbitrary Boolean FEI and continuum singularity claims; no stronger literature premise is imported. Loading/hashing baseline sources is provenance, not a new independent audit of all their mathematics.

New original proofs actually reconstructed: A096 run20261023T140303Z DERIVATION2--5 and its ghost claim; A097 run20261023T143952Z PROOF and its signed-floor claim; A093 run20261026T202338Z DERIVATION supplies two literal proof-text errata; A098 run20261026T203914Z REVIEW is corroborating navigation. Copies and byte hashes are saved under out/sources and out/READ_RECEIPTS.json. Math-brain card claim_222dcbc67cb0e75c4bdea3e4e3981211a615008a4e57bce5337d4d0b9b000aca confirms that suitable-coordinate payment is explicitly unproved; it is not used as a proof premise.

## complete derivation or exact first unsupported line

STAGE11_ADDITIONS.tex gives complete local proofs, literally included in standalone CANDIDATE_MANUSCRIPT.tex. The exact signed floor cost follows by atomwise cancellation and strict convexity. The derivative is t(z-a)/(z(t-z)ln2), with t>0: the source proof omits t, but its minimizer and exact theorem statement remain unchanged. The signed reached cost fits the SAME original account exactly iff sum rho*beta*Delta<=B-C-U. Negative prices release previous mismatch once. Positivity is not implied merely by crossing a required floor.

Ghost-complete mixtures use one stochastic kernel on BOTH true and reference laws, including explicit stochastic choices on true-zero rows. Each child has r_t>=b/2>0 and the same original labelled witnesses with updated weights. The divergence chain is A=D_erase+D_out+average A_child. Therefore B_i+average CE_child-CE_parent=-JS-D_erase-D_out. The log(1/b) envelope loses exactly D_out. Actual fair child reaches must not be replaced by reference outcome probabilities. Induction supplies all finite adaptive stopping trees, including constant and irrelevant queries and full complementary terminals. The finite checker samples bounded trees; it does not exhaust all adaptive policies or prove the all-dimensional quantifier by enumeration.

The source's separate common-marginal policy has B_i+average CE_child-CE_parent=-D_erase. A097's CE-only equality to -D_occ omits B_i. The corrected identity is the one integrated here, preserving its weaker nonincrease conclusion. It must not be conflated with A096's outcome-adapted inheritance, which additionally releases JS+D_out. The actual AND2 control has CE change=-1, B_i=1, D_erase=0 and refutes the literal uncorrected equality. This is an editorial/accounting correction to a proof paragraph, not a refutation of the signed-floor theorem or FEI.

FIRST UNSUPPORTED UNIVERSAL LINE: construct a useful complete ORIGINAL source with capacity at most K*I(core), K independent of dimension, for every Boolean core, or pay a necessary compatible stopping/admission obligation from actual UNUSED original capacity after all prior charges. Ghosts alone do not force a reset in the expanded interface. Choosing Q=P leaves initial CE=H and does not price the source. This stage supplies no new universal constant and no divergent Boolean H/I family.

## executed validation with domain, arithmetic, commands and outputs

Commands from A099: python -B -X utf8 runs/20261026T233346Z-fleet04-A099-candidate-assembly/code/init.py; code/check.py --pilot; code/check.py; code/finalize.py. FROZEN_SPEC precedes searches; its case-count description was corrected after the pilot before main, without changing family or domain. Main checker/helper hashes are pinned before main execution. Pilot: 4,090 exact assertions,22 tables,144 local checks including tree queries,44 adaptive trees,197 floor profiles,0.2474s PASS. Main: 41,320 exact assertions,278 labelled tables n=0..3,1,680 local checks including tree queries,44 adaptive trees,1,026 floor profiles,480 ghost-row observations,1.9335s PASS. Pilot and main counts are separate, never pooled.

No symmetry quotient is used. Integer Walsh transforms and Fraction probabilities reconstruct both physical restrictions. Exact prime-log linear identities and outward rational atanh bounds check KL/CE equalities and nonnegative releases. The bounded floor grid uses denominators8,12 and vacuum0,1/4, with true-zero reference atoms in both cells. An analytic convexity proof supplies continuum optimality. Checks cover zero vacuum, duplicates, ghost rows, deterministic/fair ghost splits, constants, matched/mismatched signed endpoints, and the AND2 missing-erasure negative control. A supplied original finite-CE law always has b>0 by finite support; an influence price or dimension-free witness count does not follow.

The research checker estimated110MB and finished in under2s; no heavy search, dimension escalation, GPU, detached worker or unrelated process change. Fresh memok admitted an optional Lean check (physical free7.6GB, commit free22.1GB); its outcome is separately recorded in out/FORMAL_STATUS.json. The analytic theorems and exact bounded certificates are not represented as fully Lean-checked. No PDF build or new literature search is claimed.

## proof dependencies and changed downstream conclusions

The31 inherited claim records are retained; two unchanged source statements give33 records and53 dependency nodes. Source statement-hash conventions are checked rather than rewritten. New review records are limited to scoped reconstruction and cite the existing A093 proof corrections. They do not constitute either required whole-chain audit or independent acceptance of an amended proof version. The DAG remains acyclic, all dependency targets resolve, and the complete prior source remains included. Existing four universal conjectures remain explicit.

C024/C020 transport can now carry ANY supplied complete finite reference using a possibly exponential initial witness list. This removes a source-zero exclusion and an alleged automatic conversion liability; it does not pay the initial reference or a genuinely required fresh class. The signed admission interface is now correct for arbitrary incoming mismatch and uses the SAME diminished original budget. Downstream consumers must use either the common-marginal or outcome-adapted identity with its proper erasure term, never mix their refunds or book a release twice.

## one next mathematical action and independent reviewer

A050/A011/A097: provide a noncircular influence-priced ORIGINAL arbitrary-core source, or specify one actually useful REQUIRED stricter compatible class and pay its exact reached signed price from the old unused original account. A085/A094: challenge the integrated source, including which inheritance policy each use invokes, all terminal/old-charge retention, and source necessity. No messages have been sent and no review acceptance is inferred from this routing.

## actual persistence receipts or precise save blocker

REPORT, CLAIMS, PROGRESS and byte-identical PACKET_DELTA are saved locally with protocol fields. Standalone manuscript, complete additions, portable exact helper/checker, frozen search, source copies/hashes, main/pilot results, dependency graph, formal status and structural readback are in this run. All artifacts are below20MB. Rolling STATUS is exactly two lines; dated WORKLOG and LEARNED entries are appended. Local persistence is checked, while supervisor copying, remote mirrors, downstream adoption and public release remain UNVERIFIED. Brain wake warns of stale owner-model/state/dream; those notes are not mathematical premises. No brain writes, git, mail, external mutation, other-agent edit or trading access occurs.

## Universal bridge

C024 history transfer and C020 complete-reference accounting inside C019 advance by ghost-complete heredity for every supplied finite reference and by a sharp SIGNED arbitrary-incoming-reference admission price at the SAME original account. The universal numerical improvement is zero. C018 erasure payment and full FEI remain OPEN because initial arbitrary-core O(I) pricing or a useful necessary paid stopping obligation is still unsupported. NEXT targets that initial supplier or a genuinely required stricter class because optional resets and repeated admitted-history examples cannot close this universal line.
'''
put('REPORT.md',report)
old=json.loads((A/'runs/20261023T131709Z-fleet03-A099-candidate-assembly/PROGRESS.json').read_text(encoding='utf-8'))
old.update(run_id=R.name,attempt_id='A099-assembly-v11',method='Exact-source reconstruction of signed admission and ghost-complete reference heredity; source-level correction propagation',mathematical_delta='Two unchanged scoped claims integrated. Distinguishes common-marginal from outcome-adapted inheritance; correct derivative factor t and retain erasure in query CE. Arbitrary supplied ghost reference transports without forced conversion, but initial O(I) supplier remains open.',deliverable_status='COMPLETE_LOCAL_SCOPED_SOURCE_ASSEMBLY',mathematical_status='SCOPED_ANALYTIC_RECONSTRUCTION_EXACT_FINITE_CERTIFICATES_FULL_FEI_OPEN',claims_created_or_changed=[c['claim_id']+'@1' for c in new],source_artifacts=['CANDIDATE_MANUSCRIPT.tex','STAGE11_ADDITIONS.tex','CLAIMS.json','out/READ_RECEIPTS.json','out/PROOF_DEPENDENCIES.json','out/VALIDATION.json'],next_consumers=['A050','A011','A085','A094','A096','A097','A098','B20'],next_action='Supply an influence-priced ORIGINAL arbitrary-core source or price an actually required stricter class from SAME unused original account; A085/A094 audit full chain.',stagnant_substantive_attempts=0,blockers=['Initial arbitrary-core influence-priced supplier unproved','Two independent integrated-chain audits pending','No PDF build; formal check scope recorded separately','Remote mirrors/adoption unverified'])
old['claim_versions_used'] += [dict(claim_id=c['claim_id'],version=c['version']) for c in new]
put('PROGRESS.json',old);put('PACKET_DELTA.json',old)
(A/'STATUS.md').write_text('STATE: A099 v11 saved: signed-floor and ghost-complete source claims reconstructed;41,320 exact checks PASS;33 claims/53 DAG nodes;two proof-text errata propagated;full FEI OPEN.\nNEXT: A050/A011/A097 supply ORIGINAL arbitrary-core O(I) source or pay REQUIRED compatible admission from SAME unused original margin;A085/A094 integrated-chain audits pending.\n',encoding='utf-8')
for name,line in [('WORKLOG.md','A099 v11: integrated two exact-source scoped claims, separated common-marginal/outcome-adapted inheritance, propagated missing-t and missing-erasure errata. Main41,320 exact checks;33 claims/53 nodes. Universal source price and two full-chain reviews OPEN.'),('LEARNED.md','Any supplied complete finite-CE Q has a positive P component plus at most2^n point witnesses; ghost-complete same-kernel transport preserves original provenance through ANY finite adaptive tree. It pays erasure plus terminal CE from original CE but not its O(I) initial price. Signed floor derivative has factor t; common-marginal inheritance releases D_erase after erasure, while outcome-adapted inheritance additionally releases JS+D_out. Their budgets cannot be mixed. Signed floor crossings may refund prepaid mismatch.')]:
 with (A/name).open('a',encoding='utf-8') as f:f.write('\n'+now+': '+line+'\n')
ids={x['claim_id'] for x in dag['nodes']};assert len(ids)==len(dag['nodes'])
edges={x['claim_id']:x['proof_dependencies'] for x in dag['nodes']};done=set();active=set()
def visit(i):
 assert i in ids
 if i in done:return
 assert i not in active
 active.add(i)
 for j in edges[i]:visit(j)
 active.remove(i);done.add(i)
for i in ids:visit(i)
labels=re.findall(r'\\label\{([^}]+)\}',text);refs=re.findall(r'\\(?:ref|eqref)\{([^}]+)\}',text)
assert len(labels)==len(set(labels));assert not set(refs)-set(labels)
assert text.count(r'\begin{conjecture}')==base.count(r'\begin{conjecture}')
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
proto=json.loads(Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
claimfields=set(proto['required_per_run']['claim_fields']);assert all(set(c)==claimfields for c in claims)
progressfields={x.split(' (')[0] for x in proto['required_per_run']['progress_fields']};assert set(old)==progressfields
for h in proto['required_per_run']['report_fields']:assert h in report
put('out/STRUCTURAL_CHECK.json',dict(status='PASS',claim_records=len(claims),dag_nodes=len(ids),resolved_DAG=True,labels=len(labels),universal_conjectures=text.count(r'\begin{conjecture}'),exact_schema=True,main_assertions=validation['exact_assertions'],pilot_assertions=pilot['exact_assertions'],timestamp=now))
print(json.dumps(load('out/STRUCTURAL_CHECK.json')))
