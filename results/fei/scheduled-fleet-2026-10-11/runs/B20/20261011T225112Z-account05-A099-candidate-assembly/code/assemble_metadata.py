"""A099 v1: source receipts, dependency/schema validation and bounded TeX build.
No Boolean search and no upstream checker rerun. Writes only beneath A099.
"""
from pathlib import Path
import hashlib
import json
import re
import shutil
import subprocess
import time
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[3]
RUN = Path(__file__).resolve().parents[1]
BASE = Path(r'~\mop_fei100\reports\fei-2026-10-11')
SUP = Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents')
TEAM = Path(r'~\brain_workers\FEI100_20261011')
RID = RUN.name
OUT = RUN / 'out'
OUT.mkdir(exist_ok=True)

def read(p):
    return p.read_text(encoding='utf-8-sig', errors='replace')

def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def save(name, value):
    p = RUN / name
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

protocol = json.loads(read(BASE / 'EXECUTION_PROTOCOL.json'))
revision = protocol['revision']
assert ROOT.name == 'A099' and RUN.parent.parent == ROOT
start = time.monotonic()
inputs = []
def source(p, usage, locator):
    assert p.is_file(), str(p)
    inputs.append({'path': str(p), 'sha256': digest(p), 'bytes': p.stat().st_size,
                   'usage': usage, 'locators': locator})

for name in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json',
             'OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json',
             'FEI_100_agent_research_plan.tex','AGENT_ASSIGNMENTS.json']:
    source(BASE / name, 'protocol/background; no status label used as proof',
           'A099 contract; protocol field sets; B20 ownership; source pins')
for name in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']:
    source(SUP / name, 'background scope and live obligations', 'C005/C006/C018/C019/C020/C024')
for p in sorted((SUP / 'sources').glob('*.md')):
    source(p, 'proof source' if p.name in {'ERASURE_REDUCTION.md','BLOCK_RESTRICTION_IDENTITY_2026-09-18.md'}
           else 'context inventory; selected route-map sections inspected' if p.name == 'ROUTE_MAP_CURATED.md'
           else 'inventory only; not a mathematical premise',
           'ER Sections 1-6; BR Sections 1-5; RM Sections 11.13-11.16' if p.name in
           {'ERASURE_REDUCTION.md','BLOCK_RESTRICTION_IDENTITY_2026-09-18.md','ROUTE_MAP_CURATED.md'} else None)
for p in sorted((TEAM / 'context').glob('*')):
    if p.suffix in {'.txt', '.pdf'}:
        source(p, 'context only; paper-wide audit not performed; PDFs hashed, text sections inspected',
               '38pp threshold introduction/Sections 5 and 8; 29pp introduction; '
               '30pp percolation Theorems 3.1-3.2; 31pp introduction')
source(TEAM / 'BOARD.md', 'stage-start coordination', 'snapshot 2026-10-11 22:47 UTC')
source(TEAM / 'claude/B20/STREAM_NOTES.md', 'lead instructions followed', 'v1 2026-10-11 22:48Z; A099 target')
a097 = TEAM / 'agents/A097/runs/20261011T221240Z-account05-A097-cross-route-transfer'
for name in ['REPORT.md','CLAIMS.json','CROSS_ROUTE_SUBSTITUTION.tex','out/EXACT_RESULTS.json',
             'out/BLOCK_RESULTS.json']:
    source(a097 / name, 'complete reference transfer provenance; imported outputs not rerun',
           'REPORT Sections 1-5; compatible generator G and telescopes T/S; exact finite checks')
for p in sorted((BASE / 'runs').rglob('REPORT.md')):
    source(p, 'B05/B19 proof and review read; B09 inventory only, not imported' if 'B09' not in str(p)
           else 'inventory only; biased theorem not imported',
           'B05 Sections 2-7; B19 Sections 2-5' if 'B09' not in str(p) else None)
save('out/SOURCE_RECEIPTS.json', {'protocol_revision': revision, 'sources': inputs,
     'note': 'Hash receipts identify bytes. Inventory or hashing alone is not reading or acceptance.'})

nodes = [
 {'id':'C005','version':'supplement-2026-10-11/ER','kind':'PROVED_BASELINE_REPRODUCED','parents':[], 'tex_label':'lem:single'},
 {'id':'LSI','version':'A099-assembly-v1','kind':'STANDARD_LEMMA_REPRODUCED','parents':[], 'tex_label':'lem:lsi'},
 {'id':'C006','version':'supplement-2026-10-11/BR','kind':'PROVED_BASELINE_REPRODUCED','parents':['LSI'], 'tex_label':'lem:block'},
 {'id':'DOWNWARD','version':'supplement-2026-10-11/ER','kind':'PROVED_BASELINE_REPRODUCED','parents':[], 'tex_label':'lem:downward'},
 {'id':'C018','version':'supplement-2026-10-11/ER','kind':'PROVED_IMPLICATION_PAYMENT_OPEN','parents':['C005','DOWNWARD'], 'tex_label':'thm:erasure'},
 {'id':'C019','version':'A099-assembly-v1','kind':'PROVED_IMPLICATION_PAYMENT_OPEN','parents':['C006'], 'tex_label':'thm:tree'},
 {'id':'COMPLETE','version':'A097-v1','kind':'PROVED_INTERFACE_REPRODUCED','parents':[], 'tex_label':'lem:complete'},
 {'id':'A097-COMPATIBLE-LEAF-REFERENCE-TRANSFER','version':1,'kind':'AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW',
  'parents':['C006','COMPLETE'], 'tex_label':'thm:reference'},
 {'id':'B05-SPARSE-ACTIVATION-VARIANCE-REFUND-NOGO','version':1,
  'kind':'INDEPENDENTLY_REVIEWED_AT_STATED_SCOPE','parents':[], 'tex_label':'prop:b05'}
]
leaves = [
 {'id':'OPEN-C018-L','quantifiers':'exists finite K>=0; all n>=0; all real a satisfying complete signed Boolean convolution',
  'first_unproved_line':'L(f)<=K I(f)', 'tex_label':'conj:universal', 'effect':'FEI with K+3/ln(2)'},
 {'id':'OPEN-C019-TREE','quantifiers':'exists finite K,C_leaf and uniformly certified leaf class; for every Boolean f exists finite actual tree',
  'first_unproved_line':'sum_h pi_h B_h<=K I_removed with certified terminal entropies',
  'tex_label':'conj:tree','effect':'FEI with max(K+2/ln(2),C_leaf)'},
 {'id':'OPEN-REF-TRANSFER','quantifiers':'exists finite K,C_leaf; for every Boolean f exists actual tree and supported complete terminal references, interior lift G',
  'first_unproved_line':'sum_h pi_h(B_h-kappa_h)<=K I_removed AND CE(P_l,Q_l)<=C_leaf I(f_l)',
  'tex_label':'conj:reference','effect':'FEI with max(K+2/ln(2),C_leaf)'},
 {'id':'OPEN-C024-HISTORY','quantifiers':'exists finite K>=0; all n>=0 and Boolean f; explicitly defined Q_bias improper integral in nats',
  'first_unproved_line':'Q_bias(f)<=K I(f)', 'tex_label':None,
  'effect':'Historical source reports comparison to C_path; comparison not imported or independently reconstructed here'}
]
save('out/PROOF_DEPENDENCIES.json', {'nodes':nodes, 'open_leaves':leaves,
     'open_leaves_are_not_unconditional_premises':True, 'new_mathematics_claimed':False,
     'historical_C024_comparison_imported':False})
tex = read(RUN / 'CANDIDATE_MANUSCRIPT.tex')
labels = re.findall(r'\\label\{([^}]+)\}', tex)
refs = re.findall(r'\\(?:ref|eqref)\{([^}]+)\}', tex)
assert len(labels) == len(set(labels)), 'duplicate TeX label'
assert set(refs) <= set(labels), 'unresolved TeX references'
assert all(n['tex_label'] in labels for n in nodes)
assert tex.count('\\begin{conjecture}') == 4
assert 'Full FEI remains open' in tex
byid = {n['id']: n for n in nodes}
seen, active = set(), set()
def visit(key):
    assert key in byid and key not in active, 'missing or cyclic proof dependency'
    if key in seen:
        return
    active.add(key)
    for parent in byid[key]['parents']:
        visit(parent)
    active.remove(key)
    seen.add(key)
for key in byid:
    visit(key)
assert not set(x['id'] for x in leaves) & set(byid)
upstream = json.loads(read(a097/'CLAIMS.json'))
assert any(x['claim_id']=='A097-COMPATIBLE-LEAF-REFERENCE-TRANSFER' and x['version']==1 for x in upstream)
for claim in upstream:
    assert hashlib.sha256(claim['exact_statement'].encode()).hexdigest() == claim['statement_sha256']

save('CLAIMS.json', [])
progress = {
 'protocol_revision':revision,'run_id':RID,'stream':'B20','packet_id':'A099',
 'gap_id':'G-A099-ASSEMBLY-C018-C019','attempt_id':'A099-assembly-v1',
 'method':'Source-complete assembly, quantified open leaves, version-bound DAG, static/source validation and bounded PDF build',
 'mathematical_delta':'No new mathematics. Assembles C005/C006/C018/C019 and A097 G/T/S with complete proofs; pins B05 scope; keeps erasure and historical C024 payment explicitly open.',
 'deliverable_status':'COMPLETE_LOCAL_PENDING_SUPERVISOR_ADOPTION',
 'mathematical_status':'FULL_FEI_OPEN_CONDITIONAL_REDUCTION_CHAIN_ASSEMBLED',
 'claim_versions_used':[{ 'claim_id':n['id'],'version':n['version']} for n in nodes if n['id'] not in {'LSI','COMPLETE','DOWNWARD'}],
 'claims_created_or_changed':[],
 'source_artifacts':['CANDIDATE_MANUSCRIPT.tex','ASSEMBLY_STATUS.json','out/PROOF_DEPENDENCIES.json',
                     'out/SOURCE_RECEIPTS.json','out/VALIDATION.json','out/PERSISTENCE_RECEIPTS.json'],
 'next_consumers':['A090','A094','A093','A100','A097','A064','B20'],
 'next_action':'A090/A094 independently reconstruct the assembled chain; A097/A064 test prescribed complete leaf references on the B05 control-first tree and pay the erasure-minus-credit residual.',
 'stagnant_substantive_attempts':0,
 'blockers':['Universal C018/C019/reference payment unproved; two integrated independent reviews absent; supervisor copy/mirror not verified.'],
 'packet_ids':['A099']}
# The protocol lists a prose annotation for the compatibility key, while
# its compatibility section explicitly specifies the actual key packet_ids.
progress_fields = [x.split(' (', 1)[0] for x in protocol['required_per_run']['progress_fields']]
assert set(progress) == set(progress_fields)
save('PROGRESS.json', progress)
save('PACKET_DELTA.json', progress)

build = {'compiler':shutil.which('pdflatex'),'timeout_seconds_per_pass':60,'passes':[]}
if build['compiler']:
    for index in range(2):
        command = [build['compiler'],'--disable-installer','-interaction=nonstopmode','-halt-on-error',
                   '-output-directory=out','CANDIDATE_MANUSCRIPT.tex']
        try:
            result = subprocess.run(command, cwd=RUN, capture_output=True, timeout=60)
            (OUT / f'BUILD_PASS_{index+1}.txt').write_bytes(result.stdout + result.stderr)
            build['passes'].append({'command':command,'exit_code':result.returncode})
            if result.returncode:
                break
        except subprocess.TimeoutExpired as exc:
            (OUT / f'BUILD_PASS_{index+1}.txt').write_bytes((exc.stdout or b'')+(exc.stderr or b''))
            build['passes'].append({'command':command,'timeout':True})
            break
else:
    build['limitation'] = 'pdflatex unavailable; TeX static checks completed'
build['pdf_exists'] = (OUT / 'CANDIDATE_MANUSCRIPT.pdf').is_file()
validation = {'kind':'artifact validation, not mathematical certification',
 'boolean_searches_executed':0,'upstream_exact_checkers_rerun':False,
 'source_files_hashed':len(inputs),'dag_nodes':len(nodes),'dag_edges':sum(len(n['parents']) for n in nodes),
 'open_leaves':len(leaves),'label_count':len(labels),'tex_references_resolved':True,
 'dag_acyclic':True,'protocol_progress_exact_field_set':True,
 'protocol_key_annotation':'packet_ids (one primary ID, for compatibility) normalized to packet_ids, as required by protocol compatibility section',
 'claims_exact_field_set':'vacuously true; empty claims array; no new math',
 'A097_statement_hash_verified':True,'build':build,
 'elapsed_seconds':time.monotonic()-start}
save('out/VALIDATION.json', validation)
assembly = {'assembly_id':'A099-assembly-v1','run_id':RID,'full_fei_status':'OPEN',
 'deliverable_status':'COMPLETE_LOCAL','new_mathematical_claims':0,'nodes':nodes,'open_leaves':leaves,
 'independent_integrated_audits':[{'reviewer':'A090','verdict':'PENDING'}, {'reviewer':'A094','verdict':'PENDING'}],
 'acceptance_guard':'No open leaf may become a theorem by source status, finite tests, or artifact completion; both substantive independent chain audits required for a major candidate.',
 'B05_scope':'Refutes specified all-coordinate local Kd+A V+B M payment; does not refute selectable-coordinate, stopping-tree or FEI targets.',
 'A097_credit_scope':'Posterior credit bounded by terminal reference KL slack; must use compatible lift G with no unpriced resets.',
 'historical_C024':'Real multivalued trajectory process, not Boolean physical restrictions; external comparison not imported. Explicit Q_bias leaf supplied.',
 'source_manifest':'out/SOURCE_RECEIPTS.json','validation':'out/VALIDATION.json',
 'persistence':{'local':'saved','supervisor_copy':'NOT_VERIFIED','brain_mirror':'NOT_VERIFIED','public_release':'NONE'}}
save('ASSEMBLY_STATUS.json', assembly)

report = f'''# A099 candidate assembly, version 1

## exact target, quantifiers, hypotheses and units

Assemble the strongest source-complete uniform-cube reduction chain requested by B20: C005 -> C006 -> C018 -> C019 and A097's finite-tree reference transfer, with B05 scope retained. Every f is Boolean on an arbitrary finite uniform cube; entropy/divergence are in bits, ordinary influence is the mean Fourier set size. The explicit historical C024 Q_bias leaf uses natural units. This is assembly of existing arguments, no new mathematical claim, and not a full FEI proof.

## sources actually read, revisions and theorem locators

Execution protocol read in full, revision {revision}. Campaign README, CURRENT_STATUS, registries, stream actions, supplemental CAMPAIGN/CLAIMS/COUNTEREXAMPLES/SEED_LEMMAS/NATIVE_MAPPING and the A099 plan contract were inspected. PACKET_STATUS is an older adoption snapshot, not current mathematical evidence. BOARD snapshot 22:47 UTC and B20 STREAM_NOTES v1 22:48Z give the specific assembly direction, which is followed.

Original complete proofs used: ERASURE_REDUCTION Sections 1-6; BLOCK_RESTRICTION_IDENTITY Sections 1-5; B05 original REPORT Sections 2-7 at commit 80cc2e5027efa56d79c4ecdf7d4949759ef2068b; B19 review Sections 2-5 at commit 7955d427222392911dc6af2e4ee3aa8aab67ac8c; A097 run 20261011T221240Z-account05-A097-cross-route-transfer REPORT Sections 1-5 and version-1 claim. RM Sections 11.13-11.16 were read for historical C024 scope, but their external continuous-process proofs are not imported.

Context inspection: threshold 38pp introduction, Section 5 complete references and Section 8 selectors; threshold 29pp introduction; percolation 30pp Theorems 3.1-3.2 and 31pp introduction. These are selected-section inspections, not complete independent paper audits. Both paper versions and PDFs are hashed separately. Threshold/percolation theorems and B09's biased theorem are not proof premises. Other source files and B09 original run are inventory entries only where so labeled. out/SOURCE_RECEIPTS.json pins exact local bytes and distinguishes reading, inventory, proof use and reported validation.

## complete derivation or exact first unsupported line

CANDIDATE_MANUSCRIPT.tex is the single complete source. It includes singleton erasure/JS proof with sharp scalar normalization, elementary log-Sobolev proof including tensorization, actual block entropy and influence identities, aggregate downward-charge sandwich and C018 induction, finite-tree telescope with terminal entropy and exact reach probabilities, completion of nonempty reference laws, and the A097 supported subprobability G/T/S derivation. The B05 obstruction is proved in full from the Boolean sparse bent point-flip family and assigned only its correct local scope.

Four open leaves are explicit quantified conjectures: universal L(f)<=K I(f); actual stopping-tree sum pi B<=K I_removed with certified terminal class; reference-compatible sum pi(B-kappa)<=K I_removed with complete terminal CE costs; and the defined translated biased-law Q_bias improper integral <=K I in nats. The historical C_path comparison is source-reported context, not a proved premise here. No trajectory field is treated as a Boolean physical restriction.

The first universal unsupported line is L(f)<=K I(f) under all signed Boolean convolution identities, for one finite dimension-independent K. In the reference route it is sum pi(B-kappa)<=K I_removed together with uniformly certified terminal cross-entropies. The proof only closes their conditional consequences. Aggregate B and selectable coordinate erasure are kept distinct; B05's local L is renamed B_y. No source status or finite check closes an open leaf.

## executed validation with domain, arithmetic, commands and outputs

Command from A099: `python -X utf8 runs\\{RID}\\code\\assemble_metadata.py`. Domain is the fixed assembly artifacts, exact JSON field sets, directed dependency graph, TeX labels and source byte hashes. No Boolean search, numerical logarithmic sign claim, upstream checker replay or heavy job was performed. out/VALIDATION_SPEC.json was frozen before this artifact validation. SHA256 and exact string/graph/set checks supply artifact integrity, not mathematical truth. Validation output: {len(inputs)} source files hashed; {len(nodes)} acyclic proof nodes; four explicit open leaves; all TeX references resolved; A097 exact-statement hash verified; progress schema exact.

Compiler and bounded build results are recorded in out/VALIDATION.json and out/BUILD_PASS_*.txt; compiler runs disable package installation and have a 60-second per-pass timeout. The integrated proof remains unreviewed even if the PDF builds. A097's recorded 89,096 exact assertions and B19's recorded 16,404 exact assertions are upstream evidence, not fresh A099 test counts or independent acceptance of this assembly.

## proof dependencies and changed downstream conclusions

out/PROOF_DEPENDENCIES.json contains an acyclic version-bound DAG: C005 plus downward-charge lemma -> C018; log-Sobolev -> C006 -> C019; C006 and complete-reference/Gibbs interface -> A097 transfer. B05 is a separate obstruction, not a positive premise. Its sole accepted review imported is B19 at stated scope; the registry also records a recovery source check, which is not an A090/A094 integrated review. A097 version 1 remains author-proved pending independent review. CLAIMS.json is empty because no new mathematics or status mutation is requested by the lead.

No downstream claim version was changed. The usable handoff to A093/A100 is a reviewable candidate source with explicit theorem scope and open leaves; to A097/A064 it is the exact erasure-minus-credit residual with credit bounded by terminal KL slack. No adoption, registry mutation, mirror receipt or independent audit is asserted.

## one next mathematical action and independent reviewer

A090 and A094 should independently reconstruct the complete assembled chain, checking scalar constants, tensorization, zero true fibers with positive reference mass, subnormalization, actual physical reach weights, no influence reuse and the B05 quantifiers. The next mathematical action is for A097/A064 to test prescribed complete leaf references on the existing B05 control-first sparse-defect tree, then pay or falsify its sum pi(B-kappa) residual. This packet's assembly is complete locally; new erasure-payment research belongs with those existing consumers rather than another baseline rewrite.

## actual persistence receipts or precise save blocker

Saved locally: REPORT.md, CLAIMS.json, PROGRESS.json, identical PACKET_DELTA.json, CANDIDATE_MANUSCRIPT.tex, ASSEMBLY_STATUS.json, code/assemble_metadata.py, frozen artifact-validation spec and out source/DAG/build/validation receipts. out/PERSISTENCE_RECEIPTS.json lists exact sizes and SHA256 for all final run artifacts except itself. STATUS.md has exactly two lines; WORKLOG.md and LEARNED.md record the stage. Supervisor copy, GitHub/Brain mirror verification, independent acceptance and public release remain unverified. No write outside A099, git, mail, brain mutation, background job or worker creation was performed.

Universal bridge: This stage makes C018 erasure payment and C019 stopping-tree payment reviewable in one complete source, including A097's compatible C020 terminal-reference transfer and the historical C024 scope distinction. Mathematical progress is assembly and removal of ambiguity, not a new inequality or improved universal constant. The universal downward charge and the reference erasure-minus-credit payment still lack a dimension-independent proof; two independent integrated audits are also pending. The shortest NEXT is to audit this fixed chain while A097/A064 attack its one explicit residual on the already available B05 tree, because another isolated threshold or percolation class theorem would not close that universal payment.
'''
(RUN / 'REPORT.md').write_text(report, encoding='utf-8')
for field in protocol['required_per_run']['report_fields']:
    assert '## '+field in report
assert json.loads(read(RUN/'PROGRESS.json')) == json.loads(read(RUN/'PACKET_DELTA.json'))
assert all(p.stat().st_size < 20_000_000 for p in RUN.rglob('*') if p.is_file())
(ROOT/'STATUS.md').write_text('STATE: A099 source-complete reduction/reference assembly saved; full FEI OPEN; A090/A094 integrated audits and supervisor adoption pending.\nNEXT: A090/A094 audit the fixed chain; A097/A064 pay the prescribed-reference erasure residual on the B05 control-first tree.\n', encoding='utf-8')
with (ROOT/'WORKLOG.md').open('a', encoding='utf-8') as f:
    stamp = datetime.now(timezone.utc).isoformat()
    f.write(f'{stamp}: Saved assembly v1 with four explicit open leaves, {len(inputs)} source hashes, versioned DAG, and bounded TeX build (PDF exists={build["pdf_exists"]}). No new mathematical claim or Boolean search. Historical C024 Q_bias defined explicitly; external C_path comparison excluded from proof premises. Two independent chain reviews and supervisor mirror remain pending.\n')
receipts = [{'path':str(p.relative_to(RUN)), 'bytes':p.stat().st_size, 'sha256':digest(p)}
            for p in sorted(RUN.rglob('*')) if p.is_file() and p.name != 'PERSISTENCE_RECEIPTS.json']
save('out/PERSISTENCE_RECEIPTS.json', {'run_id':RID,'self_excluded':True,'files':receipts,
     'rolling_files':[{'path':str(p),'sha256':digest(p)} for p in
                      [ROOT/'STATUS.md',ROOT/'WORKLOG.md',ROOT/'LEARNED.md']],
     'external_copy':'NOT_VERIFIED'})
print(json.dumps(validation, indent=2))
