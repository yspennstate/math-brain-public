from pathlib import Path
import hashlib,json,datetime

ROOT=Path(__file__).resolve().parents[3]
RUN=Path(__file__).resolve().parents[1]
PROTOCOL=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
proto=json.loads(PROTOCOL.read_text(encoding='utf-8-sig'))
def sha(b):return hashlib.sha256(b).hexdigest()
def dump(name,obj): (RUN/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
run_id=RUN.name
common_hyp=['All input cubes uniform; Boolean sign functions; Fourier coefficients normalized; all entropy formulas in natural units unless converted explicitly.','Disjoint balanced composition required for the exact coherent/erasure identities; no restriction-closure assumption.']
claims=[]
statements=[
('A057-COHERENT-ERASURE-SPLIT',
 'For any disjoint balanced Boolean composition F=g(h_1,...,h_m), g=a+y_j b, q=Inf_j(g), alpha=hat h_j({i}), x=alpha^2: B_i(F)=q B_i(h_j)+L_j(x), D_i(F)=q D_i(h_j)+L_j(x)+J_j(x), where L_j=sum_T(a_T^2+x b_T^2) h_nat(x b_T^2/(a_T^2+x b_T^2)), J_j=E(a^2+x b^2)-(Eraw(a+alpha b)+Eraw(a-alpha b))/2. One has 0<=L_j<=x B_j(g)+qx ln(1/x), 0<=J_j<=2qx, so 0<=R<=x B_j(g)+qx ln(1/x)+2qx. Consequently B(F)<=sum_j q_j B(h_j)+sum_j W_1(h_j)B_j(g)+(2/e)I(F) in nats.',
 common_hyp),
('A057-NONREUSING-ALPHA-LOG-PAYMENT',
 'On any finite adaptive physical-coordinate restriction tree of Boolean root f, at any subset of nodes admitting disjoint balanced composition representations, sum_v w_v q_v alpha_v^2 ln(1/alpha_v^2)<=(2/e)sum_v w_v Inf_{i_v}(f_v)<=(2/e)I(f). Also sum_v w_v R_v<=sum_v w_v alpha_v^2 B_{j_v}(g_v)+(2+2/e)sum_v w_v Inf_{i_v}(f_v). In bits divide each entropy and its constants by ln(2).',
 common_hyp+['Each represented node is independently certified for its actual restricted Boolean function; w_v is its physical reach probability. Queried coordinates are removed on the branch. Other nodes may be omitted.'])]
for cid,statement,hyp in statements:
    c={'claim_id':cid,'version':1,'exact_statement':statement,'hypotheses':hyp,
       'statement_sha256':sha(json.dumps({'statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':')).encode()),
       'contributors':['A057'],'proof_source':{'run':run_id,'path':'COHERENT_REMAINDER_PAYMENT.tex'},
       'proof_dependencies':[{'source':'out/source_proof.md','git_blob':'37626caf9f1564342f8b6edfff54b3a3491fff35','role':'exact baseline coherent formula; its algebra is reconstructed in the new proof'},'Elementary entropy concavity and proved JS-Hellinger scalar bound; physical influence telescope'],
       'review_records':[],'status':'PROVED_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[],
       'first_unproved_line':None,'next_consumers':['A058','A059','A091','A090','A097','A026','A064']}
    assert set(c)==set(proto['required_per_run']['claim_fields'])
    claims.append(c)
dump('CLAIMS.json',claims)
progress={
 'protocol_revision':proto['revision'],'run_id':run_id,'stream':'B12','packet_id':'A057',
 'gap_id':'FEI-B12-A057-INITIAL','attempt_id':'A057-01-physical-singleton-budget',
 'method':'Exact coherent source import; allocation/JS separation; entropy concavity; Boolean derivative singleton domination; physical-tree influence conservation; independent integer-Walsh prime-log interval checker.',
 'mathematical_delta':'The retained q alpha^2 log(1/alpha^2) bank is summable by (2/(e ln2)) times consumed physical influence in bits. Full R is bounded by alpha^2 B_j(g) plus (2+2/e) times queried influence in nats. Exact erasure composition removes the separately paid JS term and yields a root aggregate erasure ledger.',
 'deliverable_status':'COMPLETE_SCOPED_PROOF_AND_PRECISE_GAP_HANDOFF',
 'mathematical_status':'LOGARITHMIC_COMPONENT_RESOLVED; FULL_REMAINDER_TRANSPORT_AND_FULL_FEI_OPEN',
 'claim_versions_used':[{'source_git_blob':'37626caf9f1564342f8b6edfff54b3a3491fff35','source_commit':'d6538f38b044b6206bc22764bd31859e334ed430','claim':'coherent balanced composition identity'}],
 'claims_created_or_changed':[{'claim_id':c['claim_id'],'version':1,'status':c['status']} for c in claims],
 'source_artifacts':['out/source_proof.md','out/source_readme.md','out/source_addendum54.md','COHERENT_REMAINDER_PAYMENT.tex','ALPHA_LOG_CONTROLS.md','code/check.py','out/validation.json','FROZEN_SPEC.json','FROZEN_SPEC_V2.json'],
 'next_consumers':['A058','A059','A091','A090','A097','A026','A064'],
 'next_action':'Use A056 recentered biased-child composition to formulate the actual descendant analogue of the alpha^2 B_j(g) transport term; test it on the existing sparse-bent split before seeking a tree potential.',
 'stagnant_substantive_attempts':0,
 'blockers':['No general influence payment for scaled outer erasure and inner-decrement residuals; terminal entropy remains; balanced representations are not restriction-closed.','Independent reviews by A091/A090 pending. B12 STREAM_NOTES.md absent at stage start.'],
 'packet_ids':['A057']}
expected_progress=[s.split(' (')[0] for s in proto['required_per_run']['progress_fields']]
assert set(progress)==set(expected_progress)
dump('PROGRESS.json',progress);dump('PACKET_DELTA.json',progress)
validation=json.loads((RUN/'out/validation.json').read_text())
assertions=sum(validation['counts'].values())
report=r'''# A057: coherent logarithm paid; scaled outer erasure remains

## exact target, quantifiers, hypotheses and units

Seek a nonreusing sum of the exact coherent-composition remainder across an actual physical restriction hierarchy. This stage proves two scoped all-dimensional statements: an exact erasure allocation identity with a full remainder upper bound, and a physical-tree payment for the retained logarithmic component. The full remainder-transport target remains open. Every main formula below is in nats; divide entropy quantities and constants by ln(2) for bits. Influence uses the ordinary uniform-cube convention.

For F=g(h_1,...,h_m) on disjoint blocks, all h_j balanced, write g=a+y_j b, q=Inf_j(g), alpha=hat h_j({i}), x=alpha^2, and Eraw(v)=sum v_T^2 ln(1/v_T^2). The complete imported remainder is

R=q x ln(1/x)+Eraw(a)+x Eraw(b)-[Eraw(a+alpha b)+Eraw(a-alpha b)]/2.

Both coherent terms and the logarithm remain explicit. No individual-child spectrum is replaced by its incoherent average.

## sources actually read, revisions and theorem locators

- EXECUTION_PROTOCOL.json, revision 2026-10-11-execution-v2, read in full; README, CURRENT_STATUS, CLAIM_REGISTRY, OBSTRUCTION_REGISTRY, PACKET_STATUS entry A057, STREAM_NEXT_ACTIONS B12 entry, and campaign plan A057 contract lines 870--874 and Brain54 bibliography entry. The B12 notes file was absent. BOARD.md was read at stage start; A056's disjoint-composition work was preserved as upstream.
- Supplemental CAMPAIGN, CLAIMS, COUNTEREXAMPLES, SEED_LEMMAS and NATIVE_MAPPING; relevant source records ISOSPECTRAL_SPLICING_CURATED sections 2--9 and LOG_ALLOCATION_CURATED sections 2--6. Existing campaign B05 and B19 reports were read for the exact local-refund obstruction and review. B09 report was read for bias-tax scope; none of its pending stronger claims is a premise here.
- Threshold 38-page text, Section 7 / Proposition 7.1 and Corollaries 7.2--7.4; the 29-page earlier text's corresponding Section 7. Percolation 30-page and other 31-page texts' introductions and entropy/influence conventions: background only, no percolation theorem used. These were focused relevant-section reads, not a claim of independent whole-manuscript audit.
- Main mathematical premise: math-open-problems commit d6538f38b044b6206bc22764bd31859e334ed430, coherent-balanced-composition-control/source/PROOF.md, Git blob 37626caf9f1564342f8b6edfff54b3a3491fff35, sections 1--8 read in full; preserved in out/source_proof.md. Reviewed README Git blob 37a3817fbd885b5c0f6b2ee2404c5a86eb123f26, preserved in out/source_readme.md.
- Brain Addendum 11.54, Git blob 4fa283ff7e3847d3b7b3c2ceead8274498de04c2, read in full and preserved in out/source_addendum54.md. Read-only brain recalls did not retrieve this formula; the connected GitHub read supplied the full pinned proof.

## complete derivation or exact first unsupported line

The complete proof is COHERENT_REMAINDER_PAYMENT.tex. Here is its mathematical ledger.

1. Put A_T=a_T^2, B_T=b_T^2, s_T=A_T+xB_T. The exact remainder is L_j(x)+J_j(x), where L_j(x)=sum s_T h_nat(x B_T/s_T) and J_j(x)=E(s)-[Eraw(a+alpha b)+Eraw(a-alpha b)]/2. Orthogonality gives identical total squared mass M=1-q+qx for both coherent child vectors. Thus J is a raw equal-mass JS divergence, not an entropy of an admitted Boolean leaf.
2. The actual erasure identity is B_i(F)=q B_i(h_j)+L_j(x). Residual block-j nonempty sectors contribute q times the inner erasure; the empty block-j sector has masses A_T,xB_T and contributes L. The corresponding JS identity is JS_i(F)=q JS_i(h_j)+J_j(x). These formulas retain the coherent phase dependence of physical child spectra.
3. Concavity of -u ln u gives E(A+xB)>=(1-x)E(A)+xE(A+B), hence L_j(x)<=x B_j(g)+qx ln(1/x). JS-Hellinger gives J_j(x)<=2 sum min(A_T,xB_T)<=2qx. Therefore R<=x B_j(g)+qx ln(1/x)+2qx. Every zero and endpoint case is covered in the proof.
4. Boolean physical half-differences give |alpha|<=Inf_i(h_j). Calculus yields alpha^2 ln(1/alpha^2)<=(2/e)|alpha|. Since Inf_i(F)=q Inf_i(h_j), the explicit logarithm costs at most (2/e) Inf_i(F). The constant in bits is 2/(e ln2), about 1.0615; the proof uses its exact symbolic value. This is a payment in actual influence, not an O(alpha^2) replacement.
5. Any finite actual physical restriction tree has I(f)=sum_internal w_v Inf_{i_v}(f_v)+E I(leaf). Thus the logarithmic bank over represented nodes costs at most (2/e) I(f), without reusing the same physical query. Full remainder sum is at most sum w_v alpha_v^2 B_{j_v}(g_v)+(2+2/e) consumed influence. Nodes need certified balanced representations; biased descendants are not assumed to retain them.
6. At a single root, sum over physical coordinates to get B(F)<=sum_j q_j B(h_j)+sum_j W_1(h_j) B_j(g)+(2/e)I(F). This is an exact interface to outer erasure transport, not a depth-independent recursive closure.

The first unsupported universal line is a source-valid physical hierarchy bound on
E H(leaf)+sum_v w_v[q_v D_{i_v}(h_{v,j_v})+alpha_v^2 B_{j_v}(g_v)]
by an absolute constant times the original influence, together with actual represented biased descendants. No such line is proved. At alpha=1, R=D_j(g), so a universal local full-remainder estimate would contain the known false all-coordinate restriction claim. The necessary AND alpha-log counterexample is retained in ALPHA_LOG_CONTROLS.md, including its benign selected-coordinate ratio.

## executed validation with domain, arithmetic, commands and outputs

Before search, FROZEN_SPEC.json froze helper, actual Boolean family, domain, count, arithmetic, memory and 60-second runtime. FROZEN_SPEC_V2.json froze the two added exact erasure/JS identities before the second execution. No dimension escalation, symmetry reduction, randomness, heavy job, GPU, or >300 MB job was used.

Command: python -X utf8 runs/20261011T220314Z-account05-A057-coherent-restriction-remainder/code/check.py

Domain: all 16 two-bit outers and all 70 balanced three-bit first inners, with a disjoint literal second inner, three selected first-block coordinates: 3360 composition splits. Six explicit parity-pair inners n=3,...,8. All 256 three-bit Boolean truth tables with the fixed complete physical restriction tree.

The independent implementation uses integer Walsh transforms, Fraction amplitudes, and exact rational coefficients of prime logarithms. Identity comparisons are coefficientwise exact; inequality comparisons use rational atanh-series log enclosures with 48 terms and an explicit geometric-tail bound. Signed coefficients select interval endpoints with the correct order. The general constants and all-dimensional statements rest on the analytic proofs; finite checks do not establish them.

Final result: PASS; ASSERTION_COUNT exact assertions/certificates, no failures. The final checker elapsed ELAPSED_SECONDS seconds. out/validation.json contains counts and six exact log-divergence scales. The finite tree log test uses the slightly weaker constant 1 nat, proved from 2/e<1, and does not pretend that its arbitrary biased nodes satisfy the source's balanced composition hypothesis. It tests the underlying derivative/telescope payment independently.

## proof dependencies and changed downstream conclusions

Only the pinned coherent source identity and elementary entropy, Hellinger, Boolean derivative, and physical influence conservation facts are used; their derivations are given in the proof. No full FEI premise, source-admission condition, pending B09 strong claim, real-wavefunction Booleanity claim, or overlapping-product entropy subadditivity is assumed.

A058/A059/A097 can replace an unpriced explicit logarithmic bank by its exact influence payment. They must retain scaled outer erasure and inner/terminal costs. A026/A064 can use the nonreuse statement on actual physical trees. The exact erasure allocation identity offers C018 an outer/inner interface with an influence-paid logarithm. Independent review of these new claims remains pending.

## one next mathematical action and independent reviewer

Use A056's recentered biased-child composition interface to express and test the scaled outer-erasure transport term at actual descendants, starting with the inherited sparse-bent split. This checks the exact remaining mechanism rather than re-enumerating balanced formulas. Reviewers A091 and A090 should independently reconstruct the empty block-j erasure sector, the signed JS-Hellinger bound, and the physical-tree influence telescope. Their reviews have not been run or inferred from the self-check.

## actual persistence receipts or precise save blocker

All requested run artifacts and rolling files are local under the authorized A057 folder. CLAIMS.json and PROGRESS.json were checked against exactly the protocol's field sets; PACKET_DELTA.json is the same content with packet_ids=[A057]. out/PERSISTENCE.json records byte lengths and SHA256 hashes after write/readback. Each file is below 20 MB. No shared indices, other agent folder, brain store, repository, mail, or trading files were modified. Supervisor mirroring and downstream adoption are pending, not claimed.

## Universal bridge

This stage moves C019 stopping-tree payment by resolving the explicit coherent q alpha^2 log(1/alpha^2) component with constant 2/(e ln2) in bits, and exposes a sharper C018 erasure transport interface. It does not pay the scaled outer-erasure bank, inner decrements, terminal entropy, or representation changes under biased restriction. NEXT is the recentered descendant ledger and sparse-bent test: it targets the residual universal tree cost after one real nonreusing component has been removed, instead of proving another isolated gate-class FEI bound.
'''
report=report.replace('ASSERTION_COUNT',str(assertions)).replace('ELAPSED_SECONDS',str(validation['elapsed_seconds']))
(RUN/'REPORT.md').write_text(report,encoding='utf-8')
for field in proto['required_per_run']['report_fields']:
    assert '## '+field in report,field
(ROOT/'STATUS.md').write_text('STATE: A057 scoped proofs complete locally: coherent logarithmic bank influence-paid; exact erasure split certified; independent review pending; full FEI OPEN.\nNEXT: Use A056 recentered biased-child ledger to transport scaled outer erasure on the sparse-bent physical tree; A091/A090 review the two new claims.\n',encoding='utf-8')
with (ROOT/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write('\n2026-10-12 — '+run_id+': Read protocol/board; stream notes absent. Brain recalls did not retrieve exact source; connected GitHub read recovered pinned full proof. Split R=L+JS; proved concavity-scaled outer erasure bound and exact B_i composition. Paid alpha-squared log via singleton derivative domination and actual physical-tree influence telescope. v1/v2 exact checks passed; final '+str(assertions)+' assertions. Balanced descendant closure and outer/inner/terminal transport remain open. Saved local proof, controls, schema-compliant claims/progress, and reviewer handoff.\n')
(ROOT/'LEARNED.md').write_text('''# Durable A057 facts

- Exact balanced/disjoint coherent source: R=q alpha^2 ln(1/alpha^2)+Eraw(a)+alpha^2 Eraw(b)-avg Eraw(a±alpha b), pinned at source Git blob 37626caf9f1564342f8b6edfff54b3a3491fff35.
- New exact erasure identity: B_i(F)=q B_i(h_j)+L_j(alpha^2), where L is packet entropy for masses a_T^2 and alpha^2 b_T^2. The JS contribution cancels from erasure; it remains in the full entropy decrement.
- Entropy concavity gives L_j(x)<=x B_j(g)+qx ln(1/x). JS-Hellinger gives J_j(x)<=2qx. Hence R<=x B_j(g)+qx ln(1/x)+2qx.
- Boolean physical half-difference gives |alpha|<=Inf_i(h). Therefore q alpha^2 ln(1/alpha^2)<=(2/e)Inf_i(F). In bits constant is 2/(e ln2). Actual restriction-tree influence conservation pays each physical query once; summing syntactic formula levels does not.
- The AND adjacent-pair parity family has alpha=-2^(2-n), inner queried influence 1, zero inner decrement, and R/(q alpha^2)>=2(n-2)ln2. This still refutes any O(q alpha^2) remainder bound; selected full decrement/influence tends to zero.
- Balanced children generally become biased. A per-node representation must be certified anew. Full remainder transport still owes scaled outer erasure, inner decrement, and terminal entropy. Alpha=1 leaves the arbitrary outer decrement unpaid.
- Integer Walsh / Fraction prime-log expressions compare entropy identities exactly; atanh-series intervals with a proved tail certify inequalities. v2 passed 3360 composition splits, six parity controls, and 256 exact physical trees. Finite checks supplement proofs; review by A091/A090 is pending.
''',encoding='utf-8')
files=[]
for path in sorted(RUN.rglob('*')):
    if path.is_file() and path.name!='PERSISTENCE.json':
        data=path.read_bytes();assert len(data)<20_000_000
        files.append({'path':str(path.relative_to(RUN)),'bytes':len(data),'sha256':sha(data)})
dump('out/PERSISTENCE.json',{'run_id':run_id,'local_readback':True,'files':files,'mirror_status':'PENDING_SUPERVISOR','independent_review':'PENDING'})
print(json.dumps({'run':str(RUN),'assertions':assertions,'claims':len(claims),'schema_fields':'PASS','files_hashed':len(files),'report_bytes':len(report.encode()),'rolling_root':str(ROOT)},indent=2))
