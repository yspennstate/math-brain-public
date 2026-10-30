import json,hashlib,datetime
from pathlib import Path
R=Path(__file__).resolve().parents[1]
A=R.parents[1]
run=R.name
# Retain the exact v1 helper text reconstructed from the explicitly versioned v2 edit.
current=(R/'code/check_signed.py').read_text(encoding='utf8')
v1=current.replace('Frozen v2: all Boolean tables n=0..3; n=4 characters and point defects.','Frozen v1: exact all Boolean tables n=0..4; no symmetry reduction.')
begin=v1.index('        if n<4:\n')
end=v1.index('            if time.monotonic()-start>58:',begin)
v1=v1[:begin]+'        for table in range(1<<N):\n'+v1[end:]
v1=v1.replace("'helper_version':'check_signed-v2','domain':'all Boolean tables n=0..3; n=4 signed characters and point defects'","'helper_version':'check_signed-v1','domain':'all Boolean tables n=0..4'")
(R/'code/check_signed_v1.py').write_text(v1,encoding='utf8')
def write(name,obj):
    (R/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
base=Path('~/mop_fei100/reports/fei-2026-10-11')
supp=Path('~/mop_fei100/research_pushes/2026-10-11-full-fei-100-agents')
context=Path('~/brain_workers/FEI100_20261011/context')
sources=[]
for folder,names in [(base,['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']),
                     (supp,['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md','sources/ERASURE_REDUCTION.md','sources/ERASURE_RIGIDITY.md','sources/ROUTE_MAP_CURATED.md']),
                     (context,['threshold_paper_38pp.txt','threshold_paper_29pp_earlier_version.txt','percolation_spectral_pivotal_entropy_30pp.txt','percolation_spectral_pivotal_entropy_31pp_other_version.txt'])]:
    for name in names:
        p=folder/name
        sources.append({'path':str(p),'sha256':sha(p),'scope':'Read relevant sections/excerpts; full protocol read. Hash pins local revision, not independent acceptance.'})
write('out/source_receipts.json',sources)
v=json.loads((R/'out/validation.json').read_text()) if (R/'out/validation.json').exists() else None
stmt1='For every finite uniform-cube Boolean sign f, let a_S=fhat(S), p_S=a_S^2, ell_S=log2(1/p_S) on positive atoms and a_S ell_S=0 otherwise, c_U=sum_S a_S a_(S xor U) ell_S, E_log=sum_(U nonempty)|U|c_U^2, and J_R=sum_(U nonempty)p_(R xor U)/|U|. Every occupied R obeys p_R[H(f)-ell_R]^2<=J_R E_log; also sum_(U nonempty)c_U^2=Var_p(ell). For a largest atom, H(f)<=ell_R+sqrt(J_R E_log/p_R).'
stmt2='There is no finite universal K with E_log(f)<=K I(f), nor any finite universal K with sqrt(J_R E_log(f)/p_R)<=K I(f) for the largest-atom anchor R of every Boolean f. The first is refuted by n-bit one-point defects with E_log/I~4n^2; the second by disjoint tensor powers of the three-bit point defect, whose anchor cost is exponentially large while influence is linear.'
claims=[]
for cid,stmt in [('A031-SIGNED-ENTROPY-ANCHOR',stmt1),('A031-ANCHOR-POSITIVE-PAYMENT-NOGO',stmt2)]:
    hyp=['Finite uniform cube','Genuine Boolean sign','Entropy in bits','Definitions and zero conventions in DERIVATION.md']
    payload=json.dumps({'statement':stmt,'hypotheses':hyp},sort_keys=True,separators=(',',':')).encode()
    claims.append(dict(claim_id=cid,version=1,exact_statement=stmt,hypotheses=hyp,
        statement_sha256=hashlib.sha256(payload).hexdigest(),contributors=['fleet05/A031'],
        proof_source={'path':str(R/'DERIVATION.md'),'sha256':sha(R/'DERIVATION.md')},
        proof_dependencies=[],review_records=[],status='AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW',
        supersedes=[],refutes=[] if cid.endswith('ANCHOR') else ['universal E_log<=K I','universal largest-atom positive anchor cost<=K I'],
        first_unproved_line=None,next_consumers=['A088','A094','A034','A035','B14','B20']))
write('CLAIMS.json',claims)
progress=dict(protocol_revision='2026-10-11-execution-v2',run_id=run,stream='B07',packet_id='A031',
    gap_id='G-BOOLEANITY',attempt_id='A031-signed-information-involution-1',
    method='Full signed convolution as orthogonal involution; information-weighted anchor cancellation; integer certificates and rational logarithms',
    mathematical_delta='Proved entropy-anchor inequality and information-variance identity; calibrated known point defects at asymptotic constant 4; refuted two naive positive payments with genuine Boolean families.',
    deliverable_status='COMPLETE_LOCAL_ARTIFACT' if v else 'SAVED_VALIDATION_PENDING',
    mathematical_status='AUXILIARY_PROOF_AND_HELPER_REFUTATION; FULL_FEI_OPEN; INDEPENDENT_REVIEW_PENDING',
    claim_versions_used=[],claims_created_or_changed=[{'claim_id':c['claim_id'],'version':1} for c in claims],
    source_artifacts=['DERIVATION.md','FROZEN_SPEC.json','FROZEN_SPEC_V2.json','code/check_signed.py','out/validation.json','out/pilot_v1_failure.txt','out/source_receipts.json'],
    next_consumers=['A088','A094','A034','A035','B14','B20'],
    next_action='Reconstruct the signed anchor equation blockwise with cross-block cancellation; seek a tensor-additive logarithmic remainder that also pays anchor surprisal.',
    stagnant_substantive_attempts=0,blockers=['B07 STREAM_NOTES.md absent at supplied path; no mathematical dependency blocked','No independent review yet','Supervisor mirror/copy not performed by A031'],packet_ids=['A031'])
write('PROGRESS.json',progress);write('PACKET_DELTA.json',progress)
protocol=json.loads((base/'EXECUTION_PROTOCOL.json').read_text(encoding='utf8'))
fields=protocol['required_per_run']
assert set(progress)==set(x.split(' ')[0] for x in fields['progress_fields'])
assert all(set(c)==set(fields['claim_fields']) for c in claims)
assert json.loads((R/'PACKET_DELTA.json').read_text())==json.loads((R/'PROGRESS.json').read_text())
validation=(f"Frozen v2 passed {v['total_cases']} actual Boolean truth tables and {v['exact_assertions']} integer assertions. Counts: {v['counts']}. Runtime {v['runtime_seconds']:.3f} seconds. Separate defects n=3..12 passed exact Fraction logarithm signs. See out/validation.json. Exhaustive integer weights are rational information proxies; the analytic isometry proves the actual logarithmic statement. No exhaustive four-bit success is claimed." if v else 'v2 validation pending; no finite success claimed yet.')
report=f'''# A031 signed entropy-anchor handoff

## exact target, quantifiers, hypotheses and units
For every Boolean sign f on every finite uniform cube, derive an explicitly entropy-weighted consequence of all signed XOR convolution identities. Entropy is in bits, influence is E|S|. The proved statement is (1)-(2) of DERIVATION.md. This is an auxiliary entropy bound with a cost, not full FEI. Full FEI remains OPEN. Point-defect calibration is a known class test, not a novelty claim.

## sources actually read, revisions and theorem locators
EXECUTION_PROTOCOL.json was read in full (revision 2026-10-11-execution-v2); the required campaign indices and board were inspected, including all five B07 packet entries. Plan sections Boolean phase/conditional entropy, normalized convolution, and A031/A033 acceptance tests were read. Sources and local hashes are in out/source_receipts.json. ERASURE_REDUCTION section 6 supplies the full-Booleanity equivalence; ERASURE_RIGIDITY section 1 and ROUTE_MAP sections 3-4 supply scope guards. CAMPAIGN, CLAIMS, COUNTEREXAMPLES, SEED_LEMMAS and NATIVE_MAPPING were read, with the counterexamples' precise scopes retained. Earlier B05, B09 and B19 reports were inspected; no unreviewed theorem from them is a proof premise. Threshold paper introductions, entropy units, Proposition 7.1 exact composition proof and selector locators, and percolation introductions, Proposition 7.3 six-cycle coercivity proof and Proposition 8.2 exterior-conditioning proof were inspected, along with both earlier-version introductions. Their geometric or composition theorems are not invoked. B07 STREAM_NOTES.md was absent. Earlier run files are source context, not asserted reproduced checks. Literature priority of the new auxiliary identity has not been researched.

## complete derivation or exact first unsupported line
DERIVATION.md contains the entire finite-sum proof. The decisive step is M^2=Id from ALL signed convolution equations, then Mc=b at anchor R. Signs remain until weighted Cauchy-Schwarz. The cutoff and information-variance identities expose the full-Booleanity consequence missing from finite prefixes, with an exact rational non-Boolean diagnostic. Point defects pay the new cost at asymptotic constant 4; E_log alone cannot be O(I). Boolean tensor powers disprove a universal positive largest-anchor payment. The first unsupported line is an influence-paid block/multiscale bound for the exact signed anchor remainder plus anchor surprisal; the unmodified positive cost is refuted and must not remain an open universal helper.

## executed validation with domain, arithmetic, commands and outputs
{validation}
Command: python -X utf8 runs/{run}/code/check_signed.py. Frozen v1 attempted n=0..4 but exited at its internal 58-second cap; failure preserved in out/pilot_v1_failure.txt. Frozen v2 is a deliberate narrower domain, not automatic escalation. Both specs existed before their respective runs. Memory estimate under 40 MB; no search requiring the 300 MB memok threshold was started. Proof is analytic in every finite dimension; finite checks do not supply a finite-to-infinite bridge.

## proof dependencies and changed downstream conclusions
No campaign claim version is used as a theorem premise. Only the explicit Fourier expansion of f^2=1 and elementary finite-dimensional linear algebra are needed. There are two source-complete author claims awaiting independent review; no independent acceptance is claimed. A034/A035/B14 may use the signed information equation conditionally after reconstruction. They must discard E_log<=K I and a universal single-anchor positive payment at unchanged hypotheses. Anchor surprisal and flat spectral entropy remain unpaid. No shared registry or other agent folder was modified.

## one next mathematical action and independent reviewer
Reconstruct the signed anchor equation blockwise, preserving cross-block cancellation, and replace the non-tensorizing positive anchor factor by a tensor-additive logarithmic remainder while retaining anchor surprisal. Independent reviewer: A088; second challenger A094. No message to either was sent; this is a source-bound handoff for supervisor ingestion.

## actual persistence receipts or precise save blocker
REPORT.md, CLAIMS.json, PROGRESS.json, PACKET_DELTA.json, DERIVATION.md, frozen specs, code, outputs and source hashes are saved locally under the prescribed run. The rolling STATUS.md, WORKLOG.md and LEARNED.md are current. out/artifact_receipts.json lists exact local hashes. No supervisor copy, GitHub save, brain write, downstream adoption or public release is inferred. The only save blocker is none for local artifacts; external mirroring awaits the supervisor.
'''
(R/'REPORT.md').write_text(report,encoding='utf8')
(A/'STATUS.md').write_text('STATE: A031 local artifact complete: signed entropy-anchor inequality and Boolean payment obstructions proved; '+('342 cases checked; ' if v else 'validation pending; ')+'independent review pending; full FEI OPEN.\nNEXT: A088/A094 reconstruct the proof; replace the refuted single-anchor positive cost with a blockwise signed remainder retaining anchor surprisal.\n',encoding='utf8')
with (A/'WORKLOG.md').open('a',encoding='utf8') as f:
    f.write(datetime.datetime.now(datetime.timezone.utc).isoformat()+': '+validation+' Two local author claims and complete derivation saved; no independent acceptance or mirror claimed.\n')
receipts=[{'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in R.rglob('*') if p.is_file() and p.name!='artifact_receipts.json']
write('out/artifact_receipts.json',receipts)
print(json.dumps({'saved':len(receipts),'validation_present':v is not None,'run':str(R)},indent=2))
