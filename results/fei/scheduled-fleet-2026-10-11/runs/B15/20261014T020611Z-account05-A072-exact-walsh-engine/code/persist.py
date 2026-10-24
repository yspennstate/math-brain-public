import json,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];AGENT=ROOT.parents[1]
def write(name,obj):
    (ROOT/name).write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
statement='For every nonconstant uniform Boolean g with 0<p=P(g=-1)<=1/16, iteration of J=-h(x xor1) on six disjoint copies, stopped at the first minority probability above1/16, terminates at G with 1/16<P(G=-1)<1/4, E(G)>=E(g)-(3/16)log2(192e)>E(g)-111/64 and H(G)/I(G)<=H(g)/I(g)+45/22. E=min over relevant physical coordinates of H(S_i|S_-i)/Inf_i. Every step retains H(F)=Q H(g)+C, I(F)=Q I(g), C=H_p(J)-Q h2(4p(1-p)).'
hyp=['h is negative exactly on {0,1,2,4,8,16,32,6,17,40} in little-endian six-bit indexing.','All six copies at each step have disjoint physical inputs; entropy units are bits.']
cid='A072-ONEFLIP-RARE-ESCAPE-PRICE'
claim=dict(claim_id=cid,version=1,exact_statement=statement,hypotheses=hyp,statement_sha256=hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':')).encode()).hexdigest(),contributors=['A072'],proof_source='PROOF.md',proof_dependencies=[],review_records=[],status='AUTHOR_PROVED_INDEPENDENT_REVIEW_PENDING',supersedes=[],refutes=[],first_unproved_line=None,next_consumers=['A071','A075','A089','A074','A092','B15'])
write('CLAIMS.json',[claim])
nextaction='A075/A089 derive an absolute admission or physical-exposure bound for moderate-bias terminal cores; A074/A092 independently reconstruct the summable one-flip loss and complete signed entropy ledger. Prevent repeated excursions from reusing a constant payment.'
progress=dict(protocol_revision='2026-10-11-execution-v2',run_id=ROOT.name,stream='B15',packet_id='A072',gap_id='G-R-SELECT',attempt_id='A072-COMPOSITION-4',method='Consume A071 one-flip escape; self-contained dimension-independent summable price proof with exact Walsh and pivotal checks',mathematical_delta='Any rare actual Boolean core escapes to minority bias (1/16,1/4) with E loss <111/64 and H/I upper increment <=45/22. The entire initial H/I and signed terminal C survive. No absolute bound and no physical-tree payment are inferred.',deliverable_status='COMPLETE_LOCAL_SAVED_REVIEW_PENDING',mathematical_status='BOUNDED_ESCAPE_PRICE_PROVED_BY_AUTHOR_FULL_FEI_OPEN',claim_versions_used=[],claims_created_or_changed=[cid+'@1'],source_artifacts=['SPEC.json','PROOF.md','code/verify.py','out/validation.json','out/REVIEW.json','out/source_receipts.json','out/manifest.json'],next_consumers=['A071','A075','A089','A074','A092','B15','B20'],next_action=nextaction,stagnant_substantive_attempts=0,blockers=['Absolute terminal-core admission/physical-exposure payment is open.','Independent review and supervisor mirror adoption are not verified.'],packet_ids=['A072'])
write('PROGRESS.json',progress);write('PACKET_DELTA.json',progress)
write('out/REVIEW.json',{'source':'A071/runs/20261014T013355Z-account05-A071-search-space-design/PROOF.md','scope':'One flipped block escapes common-sign rare region: polynomial and all-dimensional bias-escape clause only','verdict':'HOLDS_SCOPED','independence':'Enumerated J truth table directly, reconstructed its negative weight counts and exact biased polynomial; all-dimensional 3p<sigma<4p inequalities reproduced in PROOF.md. Did not reuse ten-orbit search implementation.','not_reviewed':['10-orbit completeness','g3 high-E and all64 sign upper certificates'],'new_price_claim_review':'PENDING; A072 is contributor and cannot independently accept own extension.'})
REPORT='''# exact target, quantifiers, hypotheses and units

For EVERY actual nonconstant uniform Boolean core with minority probability 0<p<=1/16, bound the price of A071's one-flipped-block escape, independently of dimension. Entropy is in bits; E(g)=min_i B_i/Inf_i over relevant coordinates. The gate and disjoint-copy convention are specified in PROOF.md. Result: finite escape to minority bias (1/16,1/4), E loss at most (3/16)log2(192e)<111/64, and H/I upper increment at most45/22. Author proof complete; independent review pending; full FEI OPEN.

# sources actually read, revisions and theorem locators

EXECUTION_PROTOCOL.json revision2026-10-11-execution-v2; BOARD.md snapshot2026-10-14 02:02 UTC; B15 STREAM_NOTES.md v2; own stage3 status, helper and report. New dependencies consumed: A071 run20261014T013355Z PROOF.md (one flipped block and exact composition identities), A080 run20261014T005622Z REPORT.md (actual rare high-E core and common-sign obstruction), A084 run20261014T000747Z REPORT.md (moderate continuum), A089 run20261014T000812Z REPORT.md (slope criterion), and A075 run20261014T005346Z REPORT.md (rare localization and retained entropy ledger). Exact accessible source hashes are recorded separately. These guide the target; the new proof reconstructs its own complete chain and has no unreviewed theorem dependency.

# complete derivation or exact first unsupported line

PROOF.md proves the stated universal-over-cores escape theorem. Key bounds are R_j>=-q_j Phi(m^2,beta_i^2), |beta_i|<=min(Inf_i,2p), and sigma(p)>3p. The erasure loss is a summable O(p log(1/p)) quantity. Spectral entropy subadditivity and the proved scalar inequality h2(vq)<=q h2(v)+v h2(q) give C<=120p^2 log2(e/(5p)); Q>=11/4 and I>=2p log2(1/p) make its normalized cost summable. The exact identity H(F)/I(F)=H(g)/I(g)+C/(Q I(g)) retains every signed terminal correction and the starting core entropy.

First unsupported universal line: an absolute admission/exposure bound for the moderate-bias terminal core, with a finite global budget if later operations create additional excursions. No complete physical restriction-tree ledger or absolute bound on H/I or E follows from this stage. Explicitly, sup E over0<p<=1/16 is at most sup E over1/16<p<1/4 plus (3/16)log2(192e). A uniform moderate-bias bound therefore controls the rare sector after just one escape.

# executed validation with domain, arithmetic, commands and outputs

SPEC.json was frozen before computation. Commands: `python -X utf8 code/verify.py --pilot` and `python -X utf8 code/verify.py`, run from this run directory (the actual invocation used their workspace-relative paths). Pilot passed in0.315 seconds; full run passed in1.731 seconds. Frozen estimated memory100MB, so the >300MB memok condition was not triggered; peak memory was not instrumented. No dimension escalation or heavy search.

The exact six-bit J gate passes integer Walsh Parseval, sign-valued inverse, direct character sums and independent edges. Five rational biases1/16 through1/256 pass rational biased Parseval/inverse and pivotal-vs-spectral influences, all30 block reserve checks, polynomial equality and terminal upper bounds. Four actual12-bit compositions from two-bit core masks1,14,6,10 pass all16384 signed Fourier coefficient identities, inverse signs, Parseval and48 physical coordinate edge counts. Large tables use FWHT and its inverse, without the quadratic direct character-sum check. Every structural check precedes entropy comparisons. Logs use the earlier independently derived48-term rational atanh enclosure, not floats. Per-case exact outputs and the final summary are in out/. The finite checks validate implementation; the all-dimensional conclusion is the analytic proof.

# proof dependencies and changed downstream conclusions

No proof dependencies beyond the elementary facts reconstructed in PROOF.md. Scoped independent review accepts A071's polynomial/bias-escape clause only; it does not certify A071's ten-orbit or g3 numerical clauses. A080's common-sign obstruction survives. A084's moderate common-sign theorem is not extended or re-reviewed here. This stage prices escape from A080's rare sector instead of excluding rare high-E cores. Composition levels are never substituted for physical restriction queries, and all starting entropy survives.

# one next mathematical action and independent reviewer

A075/A089 should close the moderate-bias terminal admission/exposure bound with a global payment preventing repeated excursions from accumulating an unbounded bill. A074/A092 should reconstruct the Phi loss bound, scalar thinning inequality, edge-isoperimetric normalization and signed terminal telescope independently. This is a continuation of the same admission gap, not another finite census.

# actual persistence receipts or precise save blocker

All four protocol files, frozen spec, proof, code, exact outputs, scoped review and hashes are saved locally in this run. Rolling STATUS.md, WORKLOG.md and LEARNED.md are current. out/manifest.json records byte lengths and SHA256, excluding itself. Each file is below20MB. PROGRESS.json and PACKET_DELTA.json have identical content. Independent review, remote mirroring and downstream adoption remain unverified; no writes outside A072 were made.

## Universal bridge

This stage moves the B15 erasure-selection admission bridge underlying C018: every rare core, in arbitrary dimension, can be transported back to moderate minority bias with E loss <111/64 and complete signed H/I upper bill <=45/22. It does not prove the total-erasure C018 inequality or C019 physical stopping-tree payment. The remaining obstruction is an absolute terminal admission/exposure bound and ownership of repeated excursion costs. That single global payment is the shortest route forward because the construction now transports arbitrary cores, while another bounded-dimension class computation cannot close the remaining universal line.
'''
(ROOT/'REPORT.md').write_text(REPORT,encoding='utf-8')
(AGENT/'STATUS.md').write_text('STATE: A072 stage4 saved: all-dimensional one-flip rare escape proved with E loss<111/64 and retained H/I upper price<=45/22; exact checks PASS; review pending; FEI OPEN.\nNEXT: A075/A089 bound moderate-bias terminal admission and own repeated-excursion costs; A074/A092 independently reconstruct PROOF.md and signed C ledger.\n',encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:
    if ROOT.name not in (AGENT/'WORKLOG.md').read_text(encoding='utf-8'): f.write('\n2026-10-14 stage4: Consumed A071 mixed-sign escape and A080 rare obstruction. Reconstructed J polynomial and proved dimension-independent bounded escape prices (<111/64 E loss, <=45/22 H/I upper increment). Five biases,30 reserves,4 actual12-bit compositions,16384 signed coefficients and48 edge counts PASS. Starting H/I and signed C retained. Independent review pending; universal terminal admission/exposure budget remains open. Run '+ROOT.name+'.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:
    if '2026-10-14: For rare' not in (AGENT/'LEARNED.md').read_text(encoding='utf-8'): f.write('\n2026-10-14: For rare minority p<=1/16, J=-h(x xor1) satisfies3p<sigma(p)<4p. Repeating until exit gives E loss <=(3/16)log2(192e)<111/64 and H/I upper increment <=45/22, for arbitrary actual cores (author proof, review pending). R_j>=-q_j Phi(m^2,beta^2), |beta|<=min(Inf,2p) supplies summable erasure loss. The scalar thinning inequality h2(vq)<=q h2(v)+v h2(q) plus dominant pivotal union bounds supplies C<=120p^2 log2(e/(5p)). Keep H(F)=QH(g)+C; no physical restriction-tree ownership or absolute FEI bound follows.\n')
sources=[Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'),AGENT.parents[1]/'BOARD.md',AGENT.parents[1]/'claude/B15/STREAM_NOTES.md',ROOT.parent/'20261013T222130Z-account05-A072-exact-walsh-engine/code/check.py']
for agent,run in [('A071','20261014T013355Z-account05-A071-search-space-design'),('A080','20261014T005622Z-account05-A080-universal-counterexample-standard'),('A084','20261014T000747Z-account05-A084-continuum-parameters'),('A089','20261014T000812Z-account05-A089-repair-specialist'),('A075','20261014T005346Z-account05-A075-search-to-theorem-bridge')]:
    sources.append(AGENT.parent/agent/'runs'/run/'REPORT.md')
write('out/source_receipts.json',[{'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sources if p.exists()])
manifest=[]
for p in sorted(ROOT.rglob('*')):
    if p.is_file() and p.name!='manifest.json':
        data=p.read_bytes();assert len(data)<20_000_000
        manifest.append({'path':str(p.relative_to(ROOT)),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
write('out/manifest.json',manifest)
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
print(json.dumps({'saved_files':len(manifest)+1,'claim':cid+'@1','status':'local complete; independent review pending'}))
