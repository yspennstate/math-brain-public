"""A099 assembly v2: source pins, exact certificate intake, metadata, PDF.
Writes only to this run and A099 rolling files. No upstream checker replay.
"""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime, timezone
import hashlib
import json
import re
import shutil
import subprocess

RUN = Path(__file__).resolve().parents[1]
ROOT = RUN.parent.parent
TEAM = ROOT.parent.parent
BASE = Path(r'~\mop_fei100\reports\fei-2026-10-11')
SUP = Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents')
OLD = ROOT/'runs/20261011T225112Z-fleet05-A099-candidate-assembly'
RID = RUN.name
OUT = RUN/'out'
assert ROOT.name == 'A099'
def text(p): return p.read_text(encoding='utf-8-sig')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def save(name,data):
    p = RUN/name
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

protocol = json.loads(text(BASE/'EXECUTION_PROTOCOL.json'))
sources = []
def pin(path,usage,locator):
    assert path.is_file(),str(path)
    sources.append({'path':str(path),'sha256':sha(path),'bytes':path.stat().st_size,
                    'usage':usage,'locator':locator})
    return str(path)

b20 = TEAM/'claude/B20/runs/20261011T225100Z-claude-B20-erasure-activation-transfer'
b06 = TEAM/'claude/B06/runs/20261011T223800Z-claude-B06-block-tree-reductions'
a096 = TEAM/'agents/A096/runs/20261011T234252Z-fleet05-A096-live-gap-ledger'
a098 = TEAM/'agents/A098/runs/20261012T024601Z-fleet05-A098-resource-reallocation'
a097old = TEAM/'agents/A097/runs/20261011T221240Z-fleet05-A097-cross-route-transfer'
a097 = TEAM/'agents/A097/runs/20261012T005449Z-fleet05-A097-cross-route-transfer'
a005 = TEAM/'agents/A005/runs/20261011T225209Z-fleet05-A005-noncircular-endpoint-referee'
a002 = TEAM/'agents/A002/runs/20261011T234442Z-fleet05-A002-hardness-preserving-transformations'
for name in ['EXECUTION_PROTOCOL.json','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json']:
    pin(BASE/name,'protocol or prior immutable navigation snapshot','revision 2026-10-11-execution-v2')
for name in ['BOARD.md','claude/B20/STREAM_NOTES.md','claude/B20/SYNTHESIS.md','claude/B06/STREAM_NOTES.md']:
    p = TEAM/name
    pin(p,'stage intake and coordination','BOARD 2026-10-12 04:39 UTC; B20 v2; B06 v2')
    if name=='BOARD.md':
        (OUT/'BOARD_SNAPSHOT.md').write_text(text(p),encoding='utf-8')
for path,loc in [(b20,'REPORT Sections 1-4'),(b06,'R1/R2 records; upstream REPORT absent'),
                 (a096,'REPORT equations (1)-(7)'),(a098,'independent layer review'),
                 (a097old,'G/T/S complete compatible reference derivation'),
                 (a097,'complete prescribed-reference B05 application'),
                 (a005,'REPORT Sections 3-5: coordinate-witness scope'),
                 (a002,'aggregate activation/tensor ledger')]:
    for name in ['REPORT.md','CLAIMS.json']:
        p=path/name
        if p.is_file(): pin(p,'source proof or claim version',loc)
for path in [a096/'DERIVATION.md',a098/'out/REVIEW_RECORD.json',a098/'out/LEVEL12_REVIEW_CHECK.json',
             a097/'DERIVATION.md',a097/'out/RESULTS.json',a097/'code/check_bent.py',
             a097old/'out/EXACT_RESULTS.json',a097old/'out/BLOCK_RESULTS.json',
             b20/'out/ACTIVATION_RESULTS.json',OLD/'CANDIDATE_MANUSCRIPT.tex',OLD/'ASSEMBLY_STATUS.json']:
    pin(path,'original source consumed; prior outputs not rerun',None)
for path in [b20/'code/write_meta.py',b06/'code/make_claims.py']:
    pin(path,'source hash convention inspected','SHA256 of canonical JSON statement plus hypotheses')
for name in ['ERASURE_REDUCTION.md','BLOCK_RESTRICTION_IDENTITY_2026-09-18.md','ROUTE_MAP_CURATED.md']:
    pin(SUP/'sources'/name,'retained stage-1 proof/context pin','ER/BR complete proofs; RM 11.13-11.16 external interface only')
save('out/SOURCE_RECEIPTS.json',{'sources':sources,'note':'Source hashes prove bytes, not mathematical acceptance. Dynamic board snapshot retained.'})

def claims(path):
    obj=json.loads(text(path/'CLAIMS.json'))
    return obj if isinstance(obj,list) else obj['claims']
all_sources = {x['claim_id']:x for path in [b20,b06,a096,a097old,a097] for x in claims(path)}
hash_conventions=[]
for c in all_sources.values():
    raw=hashlib.sha256(c['exact_statement'].encode()).hexdigest()
    canonical=hashlib.sha256(json.dumps({'statement':c['exact_statement'],'hypotheses':c['hypotheses']},
                                       sort_keys=True,separators=(',',':')).encode()).hexdigest()
    assert c['statement_sha256'] in {raw,canonical},c['claim_id']
    hash_conventions.append({'claim_id':c['claim_id'],
                             'convention':'statement-plus-hypotheses canonical JSON' if c['statement_sha256']==canonical else 'raw exact_statement'})
save('out/HASH_CONVENTIONS.json',hash_conventions)

statement = ('For every finite-valued s:N->[0,infinity) with s(N)=o(N), let K_E(s) be the '
             'supremum B(F)/I(F) over all finite N-bit Boolean signs satisfying '
             '0<I(F)<=2^(-s(N)), with B=sum_i H(S_i|S_-i) in bits and ordinary influence. '
             'Then K_E(s)=K_E in the extended reals. For any nonconstant seed f, '
             'h_m=z*f^(tensor m) is balanced, B(h_m)=mB(f), I(h_m)=mI(f)+1; its '
             'point activation obeys B(F_m)>=2^(-k_m)*mB(f) and '
             'I(F_m)=2^(-k_m)*(mI(f)+1+k_m), with k_m=o(m) chosen for the s-class. '
             'Consequently C_FEI<=K_E(s)+2/ln2 by C018. This is aggregate-erasure '
             'transport and does not preserve a selected coordinate witness. '
             'Finiteness of K_E(s) remains open.')
dependencies = [{'claim_id':cid,'version':1,'statement_sha256':all_sources[cid]['statement_sha256'],
                 'usage':'source identity reproduced with fresh balancing; no independent acceptance inferred'}
                for cid in ['B20-ERASURE-TENSOR-ADDITIVE','B20-ACTIVATION-ERASURE-FORMULA']]
dependencies.append({'claim_id':'C018','version':'supplement-2026-10-11',
                     'source':str(SUP/'sources/ERASURE_REDUCTION.md'),
                     'source_sha256':sha(SUP/'sources/ERASURE_REDUCTION.md'),
                     'usage':'proved constant comparison only for the C_FEI corollary; equality of erasure suprema does not need this reduction'})
new_claim = {'claim_id':'B20-ERASURE-LOW-INFLUENCE-COMPLETE','version':2,
 'exact_statement':statement,
 'hypotheses':['Uniform finite Boolean signs; all dimensions; entropy in bits',
               'Finite-valued s:N->[0,infinity) with s(N)=o(N)',
               'Aggregate B, not selectable-coordinate min ratio',
               'Suprema and equality interpreted in extended reals'],
 'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),
 'contributors':['claude-B20 (version-1 activation/tensor proof)','A099 (fresh-balancing refinement)'],
 'proof_source':{'run_id':RID,'files':['REFINEMENT_PROOF.md','CANDIDATE_MANUSCRIPT.tex',
                                      'code/check_balanced_transfer.py','out/EXACT_TRANSFER.json'],
                 'locator':'Theorem thm:low; no unproved universal payment premise'},
 'proof_dependencies':dependencies,
 'review_records':[{'reviewer':'A090','verdict':'PENDING'}, {'reviewer':'A094','verdict':'PENDING'}],
 'status':'AUTHOR_PROVED_SCOPED_REFINEMENT_PENDING_INDEPENDENT_REVIEW',
 'supersedes':[{'claim_id':'B20-ERASURE-LOW-INFLUENCE-COMPLETE','version':1,
                'scope':'strengthens valid additive estimate; preserves original source unchanged'}],
 'refutes':[],'first_unproved_line':None,'next_consumers':['B20','A096','A097','A100','A090','A094','A005']}
new_claim['statement_sha256']=hashlib.sha256(json.dumps(
    {'statement':statement,'hypotheses':new_claim['hypotheses']},sort_keys=True,separators=(',',':')).encode()).hexdigest()
assert set(new_claim)==set(protocol['required_per_run']['claim_fields'])
save('CLAIMS.json',[new_claim])

results=json.loads(text(a097/'out/RESULTS.json'))
certificate=[]
for row in results['results']:
    if row['reference']!='uniform': continue
    assert F(row['erasure_over_removed']['upper'])<3
    certificate.append({key:row[key] for key in ['k','reference','I_removed','I_terminal',
                       'erasure_over_removed','posterior_credit_over_removed','residual_over_removed']})
assert F(certificate[0]['erasure_over_removed']['upper'])<F(253,100)
assert F(certificate[1]['erasure_over_removed']['upper'])<F(235,100)
save('out/B05_CERTIFICATE_INTAKE.json',{'source':str(a097/'out/RESULTS.json'),
     'source_sha256':sha(a097/'out/RESULTS.json'), 'records':certificate,
     'status':'Consumed source-certified rational-log enclosures; fraction endpoint ordering rechecked, source log evaluator not rerun',
     'all_even_k_proof':'CANDIDATE_MANUSCRIPT.tex prop:b05ref plus two certified base cases'})
review=json.loads(text(a098/'out/REVIEW_RECORD.json'))
assert review['source_recorded_statement_sha256']==all_sources['A096-UNIVERSAL-LEVEL12-ERASURE']['statement_sha256']
assert review['verdict']=='ACCEPT_AT_STATED_SCOPE'
save('out/CONSUMED_REVIEWS.json',{'A096_layer_review':review,
 'scope':'H2/T12 only. This is not a second audit of the integrated assembly.',
 'A097_application':'author proof, independent review pending',
 'B20_refinement_v2':'both independent refinement reviews pending'})

nodes = [
 ('C005','supplement-2026-10-11',[],'lem:single'),
 ('LSI','retained-assembly-lemma',[],'lem:lsi'),
 ('C006','supplement-2026-10-11',['LSI'],'lem:block'),
 ('DOWNWARD','supplement-2026-10-11',[],'lem:downward'),
 ('C018','supplement-2026-10-11',['C005','DOWNWARD'],'thm:erasure'),
 ('B06-LEAD-R1-BLOCK-TO-SINGLETON',1,['C005','C006'],'lem:r1'),
 ('C019','assembled-conditional-theorem',['C006'],'thm:tree'),
 ('B06-LEAD-R2-LEAF-PARTITION-INVARIANCE',1,['C019'],'lem:r2'),
 ('B20-ROOT-BIAS-ERASURE-PAID',1,[],'lem:root'),
 ('A096-UNIVERSAL-LEVEL12-ERASURE',1,[],'thm:level12'),
 ('B20-ERASURE-TENSOR-ADDITIVE',1,[],None),
 ('B20-ACTIVATION-ERASURE-FORMULA',1,[],None),
 ('B20-ERASURE-LOW-INFLUENCE-COMPLETE',2,['B20-ERASURE-TENSOR-ADDITIVE','B20-ACTIVATION-ERASURE-FORMULA','C018'],'thm:low'),
 ('COMPLETE','A097-v1',[],'lem:complete'),
 ('A097-COMPATIBLE-LEAF-REFERENCE-TRANSFER',1,['C006','COMPLETE'],'thm:reference'),
 ('B05-CERTIFIED-BASE-CASES','A097-results-sha256',[],None),
 ('A097-B05-COMPATIBLE-REFERENCE-CERTIFICATE',1,['A097-COMPATIBLE-LEAF-REFERENCE-TRANSFER','B20-ACTIVATION-ERASURE-FORMULA','B05-CERTIFIED-BASE-CASES'],'prop:b05ref'),
 ('B05-SPARSE-ACTIVATION-VARIANCE-REFUND-NOGO',1,[],'prop:b05')]
dag=[{'claim_id':cid,'version':version,'proof_dependencies':deps,'tex_label':label,
      'statement_sha256':new_claim['statement_sha256'] if cid==new_claim['claim_id'] else all_sources.get(cid,{}).get('statement_sha256')}
     for cid,version,deps,label in nodes]
leafs=[
 {'id':'OPEN-C018-HIGHER','quantifiers':'exists finite K; all Boolean f in every finite dimension',
  'first_unproved_line':'R_ge2(f)<=K I(f)', 'conditional_constant':'K+c_root+16700/2187+2/ln2'},
 {'id':'OPEN-C019-TREE','quantifiers':'exists finite K,C_leaf and certified leaf class; each Boolean f has actual finite stopping tree',
  'first_unproved_line':'sum pi B_h<=K I_removed plus all terminal entropies paid'},
 {'id':'OPEN-REF-TRANSFER','quantifiers':'exists finite K,C_leaf; each Boolean f has physical tree and complete compatible terminal references',
  'first_unproved_line':'sum pi(B_h-kappa_h)<=K I_removed plus CE(P_l,Q_l)<=C_leaf I(f_l)'},
 {'id':'OPEN-C024-HISTORY','quantifiers':'exists finite K; all Boolean f; explicit translated biased-spectrum Q_bias integral in nats',
  'first_unproved_line':'Q_bias(f)<=K I(f); historical external comparison not imported'}]
save('out/PROOF_DEPENDENCIES.json',{'nodes':dag,'open_leaves':leafs,'conditional_FEI_only':True,
     'scope_guard':'Variant-equivalence map describes finiteness and does not identify all optimal constants.'})
visited=set(); stack=set(); byid={x['claim_id']:x for x in dag}
def visit(k):
    assert k in byid and k not in stack
    if k in visited:return
    stack.add(k)
    for d in byid[k]['proof_dependencies']:visit(d)
    stack.remove(k);visited.add(k)
for k in byid:visit(k)
manuscript=text(RUN/'CANDIDATE_MANUSCRIPT.tex')
labels=re.findall(r'\\label\{([^}]+)\}',manuscript)
refs=re.findall(r'\\(?:ref|eqref)\{([^}]+)\}',manuscript)
assert len(labels)==len(set(labels)) and set(refs)<=set(labels)
assert manuscript.count('\\begin{conjecture}')==4
assert all(n['tex_label'] in labels for n in dag if n['tex_label'])
assert '\\input' not in manuscript and '\\include{' not in manuscript

exact=json.loads(text(OUT/'EXACT_TRANSFER.json'))
assert exact['cases']==80 and exact['failures']==0
progress={'protocol_revision':protocol['revision'],'run_id':RID,'stream':'B20','packet_id':'A099',
 'gap_id':'G-A099-ASSEMBLY-C018-C019','attempt_id':'A099-assembly-v2',
 'method':'Source-complete revised assembly; reviewed universal layer intake; fresh-balancing refinement and exact symbolic spectrum certificates',
 'mathematical_delta':'Aggregate low-influence erasure optimum is unchanged: K_E(s)=K_E, removing the prior root-price loss. Assembled reviewed T12 and B06 R1/R2 plus closed prescribed-reference B05 calibration; universal remaining bill R_ge2 is explicit.',
 'deliverable_status':'COMPLETE_LOCAL_PENDING_REVIEW_AND_SUPERVISOR_ADOPTION',
 'mathematical_status':'SCOPED_REFINEMENT_PROVED_FULL_FEI_OPEN',
 'claim_versions_used':[{'claim_id':x['claim_id'],'version':x['version']} for x in dag],
 'claims_created_or_changed':[{'claim_id':new_claim['claim_id'],'version':2}],
 'source_artifacts':['CANDIDATE_MANUSCRIPT.tex','REFINEMENT_PROOF.md','ASSEMBLY_STATUS.json',
                     'CLAIM_EQUIVALENCE_MAP.json','out/EXACT_TRANSFER.json','out/SOURCE_RECEIPTS.json',
                     'out/PROOF_DEPENDENCIES.json','out/B05_CERTIFICATE_INTAKE.json'],
 'next_consumers':['B20','A090','A094','A096','A097','A100','A005','A064'],
 'next_action':'A090/A094 reconstruct fresh-balancing refinement and the expanded integrated chain; A096 develops one normalized all-degree reference for R_ge2, while A097/A064 pursue overlapping-control ownership with terminal cost retained.',
 'stagnant_substantive_attempts':0,
 'blockers':['R_ge2 universal influence bound unpaid','No two independent complete-chain/refinement audits','Supervisor copying and mirror verification unobserved'],
 'packet_ids':['A099']}
assert set(progress)=={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
save('PROGRESS.json',progress);save('PACKET_DELTA.json',progress)
save('ASSEMBLY_STATUS.json',{'assembly_version':2,'full_fei_status':'OPEN','run_id':RID,
     'new_or_refined_claims':[{'claim_id':new_claim['claim_id'],'version':2,'independent_audits':'PENDING'}],
     'integrated_independent_audits':[{'reviewer':'A090','verdict':'PENDING'},{'reviewer':'A094','verdict':'PENDING'}],
     'consumed_review':'A098 accepts A096 universal level12 version 1 only',
     'frontier':'R_ge2(f)<=K I(f); no cross-level reuse of total influence allowed',
     'closed_prior_handoff':'A097 B05 prescribed-reference calibration, author proof and exact certificate, not universal payment',
     'canonical_equivalence_map':'CLAIM_EQUIVALENCE_MAP.json','source_dag':'out/PROOF_DEPENDENCIES.json',
     'prior_run_preserved':str(OLD),'no_other_agent_or_shared_index_writes':True,
     'scope_checks':['Aggregate versus selected coordinate distinguished','A005 witness no-go retained',
                     'B05 local obstruction unchanged','Continuous C024 trajectory distinct from physical trees',
                     'B06 leaf-partition invariance does not assert invariant individual KL credit'],
     'public_release':'NONE','mirror_verification':'NOT_OBSERVED'})

build={'compiler':shutil.which('pdflatex'),'timeout_seconds_per_pass':60,'passes':[]}
if build['compiler']:
    for i in range(2):
        cmd=[build['compiler'],'--disable-installer','-interaction=nonstopmode','-halt-on-error',
             '-output-directory=out','CANDIDATE_MANUSCRIPT.tex']
        try:
            r=subprocess.run(cmd,cwd=RUN,capture_output=True,timeout=60)
            (OUT/f'BUILD_PASS_{i+1}.txt').write_bytes(r.stdout+r.stderr)
            build['passes'].append({'command':cmd,'exit_code':r.returncode})
            if r.returncode:break
        except subprocess.TimeoutExpired as exc:
            (OUT/f'BUILD_PASS_{i+1}.txt').write_bytes((exc.stdout or b'')+(exc.stderr or b''))
            build['passes'].append({'timeout':True});break
build['pdf_exists']=(OUT/'CANDIDATE_MANUSCRIPT.pdf').is_file()
save('out/VALIDATION.json',{'exact_transfer':{k:v for k,v in exact.items() if k!='cases_checked'},
     'source_files_hashed':len(sources),'claim_statement_hashes_verified':len(all_sources)+1,
     'dag_nodes':len(dag),'dag_acyclic':True,'open_leaves':4,'tex_refs_resolved':True,
     'single_source_no_inputs':True,'progress_exact_fields':True,'claim_exact_fields':True,
     'B05_source_certified_interval_endpoint_comparisons':'PASS','A098_review_bound_to_original_statement_hash':True,
     'build':build,'scope':'Exact identities and artifact checks; full FEI and independent audits remain open'})

report=f'''# A099 assembly v2: reviewed layers and loss-free low-influence transport

## exact target, quantifiers, hypotheses and units

Follow B20 v2: assemble C005/C006/C018/C019, B06 R1/R2, low-total-influence completeness and the A097 compatible-reference telescope in one source, with one canonical ID per duplicated theorem and explicit conjectural leaves. Consume the new reviewed A096 layer and the now-complete A097 B05 calibration. Uniform finite-dimensional Boolean signs, ordinary physical influence and bit entropies throughout; historical Q_bias alone is in nats.

The scoped refinement is K_E(s)=K_E for every finite-valued nonnegative s(N)=o(N), where K_E(s) is the supremum aggregate B/I over 0<I<=2^(-s(N)). This strengthens the existing B20 low-influence claim under the same ID, proposed version 2. It is not a new broad universal-payment candidate or a proof of FEI.

## sources actually read, revisions and theorem locators

Read own STATUS, supervisor BOARD 2026-10-12 04:39 UTC, B20 STREAM_NOTES v2 and SYNTHESIS in full; protocol {protocol['revision']} reread. Prior canonical/source background and paper proofs were retained from stage 1 rather than reaudited without cause.

Original new proof inputs read: Claude B20 run 20261011T225100Z REPORT Sections 1-4 and CLAIMS; Claude B06 run 20261011T223800Z R1/R2 CLAIMS records (REPORT absent at upstream save, so no phantom report acceptance); A096 run 20261011T234252Z REPORT equations (1)-(7), DERIVATION and claim; A098 run 20261012T024601Z independent layer proof and exact review record; A097 run 20261012T005449Z REPORT/DERIVATION, original exact interval outputs and logarithm helper; A097 stage-1 G/T/S proof retained. A002 stage-2 aggregate activation ledger and A005 stage-1 Sections 3-5 were read to distinguish aggregate transport from same-K selected-witness transport. The latter obstruction remains valid.

out/SOURCE_RECEIPTS.json binds {len(sources)} source files to SHA256; the board snapshot is preserved. A098's ACCEPT_AT_STATED_SCOPE is bound to A096 statement hash 5083b93ed95b2ec27859e733a86e242b7b652ab71dbc48563c8653cdeb7b7bd8. It does not accept higher-level summability or this integrated assembly. A guessed A002 timestamp was absent; the discovered actual run 20261011T234442Z supplied the proof input. No access error became a mathematical premise.

## complete derivation or exact first unsupported line

CANDIDATE_MANUSCRIPT.tex is the single expanded source: all stage-1 proved reductions are retained, and complete proofs of B06 R1/R2, root payment, reviewed universal T12, the low-influence refinement, and A097's scoped B05 certificate are inserted. No external TeX input is required. REFINEMENT_PROOF.md saves the new derivation separately for immediate review.

For arbitrary nonconstant f, h_m=z*f^(tensor m) has mean zero, B(h_m)=mB(f), I(h_m)=mI(f)+1. A point activation at k controls has exact I=2^(-k)[mI(f)+1+k] and B_data=2^(-k)mB(f) plus two explicitly nonnegative root-packet sums. Thus B(F)>=2^(-k)mB(f). With sbar(N)=max_(M<=N)s(M) and k_m=ceil(sbar(2mn)+log2(3mn))+1, the constructed N_m=mn+1+k_m cube meets I<=2^(-sbar(N_m)) for large m and k_m/m->0. Dividing an assumed low-influence bound by m*2^(-k_m) proves B(f)<=K_E(sbar)I(f), hence K_E(s)=K_E in the extended reals. This removes the prior additive root price 2/(sqrt(e)ln2), and the C018 corollary is C_FEI<=K_E(s)+2/ln2. Neither finiteness nor a chosen-coordinate witness is assumed or established.

The original version-1 additive theorem remains true; version 2 strengthens it. A005's counterexample concerns a cheap CONTROL witness, which does not invalidate a lower bound on the entire aggregate B. Fresh balancing can create deterministic spectral membership on z, whose B_z is zero; its one influence unit is retained until the limit. Tensor and activation must not be confused with unconditional coordinate-witness transfer.

The revised universal conjecture is R_ge2(f)<=K I(f), with all n and all exact signed Boolean convolution identities quantified. Root and singleton-to-pair layers are paid at c_root=2/(sqrt(e)ln2) and c12=16700/2187; full FEI would follow with K+c_root+c12+2/ln2. The other open leaves are actual stopping-tree payment with terminal entropy, compatible-reference erasure-minus-credit with terminal CE, and explicit Q_bias history integral in nats. No uniform summability of repeated fixed-level bounds is supplied.

The old B05 NEXT is completed by consuming A097's exact k=2,4,6,8 reference residuals and all-even-k B_tree<=3I_removed proof. The certificate is specific to its control-first tree and prescribed complete leaf references. Its posterior credit is bounded by O(2^(-k)/k) of removed influence. It leaves arbitrary-core/overlapping-control compatibility open. B06 R2 invariance is carefully limited to total entropy drop, removed influence and their deficit combination, rather than every isolated credit component.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json preceded both commands:

    python -X utf8 runs/{RID}/code/check_balanced_transfer.py --pilot
    python -X utf8 runs/{RID}/code/check_balanced_transfer.py

Pilot: all labelled one-bit seeds, m=1,2, k=1,2, 16 cases, 433 exact assertions PASS. Full unchanged frozen domain: all 20 labelled seeds on one and two bits, m=1,2, k=1,2, 80 cases, {exact['exact_assertions']} exact assertions PASS, helper runtime {exact['runtime_seconds']:.6f} seconds. Largest actual cube is 7 bits; estimated memory 30 MB, so no job above the memok threshold ran. Integer FWHT spectra are compared against physical edge counts and exact activation coefficients; entropy identities cancel as rational coefficients of prime logarithms. No floating-point entropy sign, automatic dimension growth, GPU or background job is used. Analytic proof, not finite extrapolation, supplies arbitrary n, m and s=o(N).

The B05 base-case certificate intake copies exact source interval endpoints and checks their rational ordering (<253/100 and <235/100). Its source atanh intervals are consumed, not rerun as an alleged independent audit. A096/A098 finite censuses are not repeated. Canonical statement hashes, A098 scope binding, proof-DAG acyclicity, four quantified leaves, TeX references and protocol field sets are checked by code/finalize.py. The compatibility key packet_ids uses the protocol's explicitly stated key, stripping the field-list prose annotation.

PDF build is bounded to two 60-second passes with package installation disabled; exact commands/results are in out/VALIDATION.json and BUILD_PASS files. Compile and schema success do not establish mathematical acceptance. No Lean certification is claimed.

## proof dependencies and changed downstream conclusions

CLAIM_EQUIVALENCE_MAP.json consolidates finite-selection/block/KL/tree finiteness reformulations under C018 and retains scope distinctions and potentially different optimal constants. Scalar JS and block-selector identities use C005/C006 rather than duplicate new IDs. B06 R1/R2, B20 root/activation/tensor, A096 T12 and A097 transfer/application each retain their original IDs. Only B20-ERASURE-LOW-INFLUENCE-COMPLETE is proposed at version 2, with A099 as refinement contributor; the prior version and all source trees remain unchanged.

out/PROOF_DEPENDENCIES.json contains {len(dag)} acyclic source-version nodes and four open leaves. No open leaf is admitted as an unconditional FEI premise. The low-influence refinement uses the tensor and balanced specialization of activation, not the paid root lemma; C018 is used only for its FEI corollary. A096's all-dimensional layer has one consumed independent A098 review; neither the low-influence refinement nor the expanded chain has either required integrated A090/A094 audit.

Downstream change proposed: B20/A096 may use the exact equality of aggregate erasure suprema instead of a +1.7501 loss; A099/A100 replace the old unevaluated B05 calibration NEXT with A097's scoped completed certificate; the universal open line is updated from all nonempty lower sets to lower sets of size >=2. Shared registries and consumer reports are not modified; no supervisor adoption or mirror is asserted.

## one next mathematical action and independent reviewer

A090/A094 should reconstruct version-2 fresh-balancing transport and the full revised chain, with explicit scrutiny of N_m dimension accounting, all nonnegative remainders, extended-real suprema, scope of A098's review, and the A097 finite base-case certificate dependency. The shortest mathematical continuation is A096's one normalized all-degree sparse-derivative reference for R_ge2, retaining its total normalizer and one influence budget; A097/A064's separate overlapping-control ownership work is the next nonadditive reference-transfer test. Do not reopen bounded-ratio B05 calibration or duplicate T12 and half-tax proofs.

## actual persistence receipts or precise save blocker

Saved locally in the exact assigned stage directory: four protocol files, single CANDIDATE_MANUSCRIPT.tex and PDF, ASSEMBLY_STATUS.json, REFINEMENT_PROOF.md, CLAIM_EQUIVALENCE_MAP.json, frozen spec, independent identity-check code, outputs, source hashes, DAG, consumed review and B05 certificates. out/PERSISTENCE_RECEIPTS.json records final sizes/SHA256, excluding itself. STATUS is two lines, WORKLOG appended with actual UTC date, LEARNED preserves scope and refinement. The previous immutable A099 run is untouched. No writes outside A099, git, brain mutation, mail, shared-index edits or background job. Two integrated audits, supervisor copying and mirror verification are unobserved.

Universal bridge: This stage moves C018 by strengthening low-total-influence completeness from an additive root-price loss to the exact aggregate equality K_E(s)=K_E, while assembling the independently reviewed universal T12 payment so the explicit remaining erasure starts at |S|>=2. It closes the prior C019/C024 finite-reference B05 calibration handoff through A097's scoped certificate and incorporates B06's same-node and leaf-partition scope controls. No finite universal FEI constant is obtained: R_ge2, arbitrary-core/overlapping-history reference payment, historical Q_bias and both independent chain/refinement audits remain open. NEXT targets a single normalized higher-level bill using actual sparse Boolean derivatives, because repeating fixed-layer payments or more isolated known-class calibrations would reuse influence or leave the universal bridge unchanged.
'''
(RUN/'REPORT.md').write_text(report,encoding='utf-8')
for name in protocol['required_per_run']['report_fields']:assert '## '+name in report
assert json.loads(text(RUN/'PROGRESS.json'))==json.loads(text(RUN/'PACKET_DELTA.json'))
assert all(p.stat().st_size<20_000_000 for p in RUN.rglob('*') if p.is_file())
(ROOT/'STATUS.md').write_text('STATE: A099 v2 saved: loss-free aggregate low-influence completeness proved; reviewed T12 and scoped B05 certificate assembled; full FEI OPEN, chain/refinement audits pending.\nNEXT: A090/A094 reconstruct v2; A096 pay R_ge2 with one normalized derivative reference; A097/A064 extend compatible references to overlapping controls.\n',encoding='utf-8')
stamp=datetime.now(timezone.utc).isoformat()
with (ROOT/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write(f'{stamp}: Stage {RID}: consumed B06 R1/R2, A096 universal layer with A098 scoped review, A097 B05 reference certificate. Fresh balancing strengthens B20 low-influence aggregate constant to exact equality; 80 frozen cases/{exact["exact_assertions"]} exact assertions passed. Version2 proposed under existing B20 ID, no shared writes, review pending.\n')
with (ROOT/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('\nFresh balancing z*f^(tensor m) removes the activation root loss exactly: mean is zero, aggregate B=mB(f), influence=mI(f)+1, and B_data(point activation)>=delta*mB(f). Economical controls then prove K_E(s)=K_E for any finite-valued nonnegative s=o(N), in extended reals. This does not transfer a selected coordinate witness and does not prove either supremum finite.\n\nA096 universal T12<=16700/2187 I is independently accepted by A098 at that layer only. Remaining C018 bill is R_ge2 over lower spectral sets of size at least two; fixed-layer reuse of I is not a summed payment.\n\nB06 leaf-partition invariance applies to full entropy drop and influence removal, not necessarily isolated erasure or reference-posterior credit. A097 B05 prescribed-reference control-first calibration is now closed at author/certificate scope; no need to recalculate it as a FEI test.\n')
receipt=[{'path':str(p.relative_to(RUN)),'bytes':p.stat().st_size,'sha256':sha(p)}
         for p in sorted(RUN.rglob('*')) if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json']
save('out/PERSISTENCE_RECEIPTS.json',{'run_id':RID,'self_excluded':True,'files':receipt,
     'rolling_files':[{'path':str(p),'sha256':sha(p)} for p in [ROOT/'STATUS.md',ROOT/'WORKLOG.md',ROOT/'LEARNED.md']],
     'external_mirror':'NOT_VERIFIED'})
print(json.dumps({'refined_claim':new_claim['claim_id'],'version':2,'exact_cases':exact['cases'],
      'assertions':exact['exact_assertions'],'sources':len(sources),'DAG_nodes':len(dag),'open_leaves':4,
      'build':build,'full_FEI':'OPEN'},indent=2))
