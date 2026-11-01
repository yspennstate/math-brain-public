from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
R=Path(__file__).resolve().parents[1]; A=R.parents[1]; TEAM=A.parents[1]; BASE=Path('~')
def write(p,s): p.write_text(s,encoding='utf-8',newline='')
def dump(p,o): write(p,json.dumps(o,indent=2)+'\n')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
camp=BASE/'mop_fei100/reports/fei-2026-10-11'
protocol=json.loads((camp/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
orig=A/'runs/20261021T184331Z-fleet03-A021-rare-core-asymptotics'
a22=TEAM/'agents/A022/runs/20261021T213608Z-fleet03-A022-one-point-surgery'
a25=TEAM/'agents/A025/runs/20261022T231646Z-fleet03-A025-rare-event-counterfamily'
sources=[TEAM/'BOARD.md',TEAM/'claude/B05/STREAM_NOTES.md',A/'LEARNED.md',BASE/'AGENTS.md']
sources += [camp/n for n in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
sources += [a22/n for n in ['REPORT.md','CLAIMS.json']]+[a25/n for n in ['REPORT.md','PROOF.md','CLAIMS.json']]+[orig/n for n in ['REPORT.md','PROOF.md','OBSTRUCTION.md','CLAIMS.json']]
receipts=[]
for p in sources:
 raw=p.read_bytes(); s=raw.decode('utf-8-sig')
 hits=[{'line':i+1,'text':l[:220]} for i,l in enumerate(s.splitlines()) if any(x.lower() in l.lower() for x in ['A021','A022','A025','C024','C019','reference','same','t/64'])]
 receipts.append({'path':str(p),'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw),'relevant_locators':hits[:30]})
dump(R/'out/SOURCE_RECEIPTS.json',receipts)
deps=[]
for p,scope in [(a22/'CLAIMS.json','Exact signed seed-reference and tensor source clauses only; root reserve strengthened here, not attributed to source'),(a25/'CLAIMS.json','General signed history identity and original-family all-cut admission only; no external reference-conversion payment assumed')]:
 data=json.loads(p.read_text(encoding='utf-8')); data=data if isinstance(data,list) else data.get('claims',[])
 for d in data:
  deps.append({'claim_id':d.get('claim_id'),'version':d.get('version'),'statement_sha256':d.get('statement_sha256'),'proof_path':str(p),'scope':scope})
statement='For every t>=2, b=g tensor t with g=-1 at000 on3bits, arbitrary vertex v and arbitrary independent controller indicator A, put delta=8^-t,L=delta H(1-2A), original Q=P_b>0 and original controller spectral marginal R. Original joint CE C0 satisfies4 I_data+L-C0>=t/4 (indeed>=179t/576). At ANY original data coordinate, use actual physical children, SAME R in both, original Q on untouched blocks, uniform4 at outcome0 and local(13/16,1/16,1/16,1/16) at outcome1. For averaged complete child CE C1 and actual d, ell=4d-(C0-C1)<1/8, and ell<0 for t>=3. Every old U in[0,t/64] remains booked and the SAME-source child bank4(I_data-d)+L-C1-U>=11t/64, retaining the original t/64 reserve. Actual entropy decrement equals reference drop plus signed child-minus-parent joint KL, all retained. An unsmoothed constant-child seed reference has infinite CE when the edit survives there with positive probability.'
claim={
 'claim_id':'A021-NONFLAT-INHERITED-REFERENCE-DATA-QUERY','version':1,'exact_statement':statement,
 'hypotheses':['Uniform cubes; normalized Walsh coefficients; bits','t>=2; g three-bit point defect; ONE controlled vertex edit','A any Boolean indicator on independent finite controls; all biases including0,1','One original tensor coordinate only; original controller reference R passed unchanged to BOTH children; Qrest and old U unchanged','Complete joint CE and both child KL retained; no assertion D_i<=4d or arbitrary controller FEI'],
 'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['A021','A022 (original exact signed-reference source clauses)'],
 'proof_source':['PROOF.md','code/check.py','out/DIRECT.json','code/replay.py','out/REPLAY.json'],
 'proof_dependencies':deps,
 'review_records':[{'reviewer':'A021','scope':'A025 general signed history identity and71/78 admission independently reconstructed; A022 exact reference algebra reconstructed. Strengthened reserve is A021 contribution, not independent acceptance of that new statement.','status':'SOURCE_SUBCLAUSES_HOLD_ONLY'}],
 'status':'AUTHOR_CHECKED_PROOF_PENDING_INDEPENDENT_REVIEW','supersedes':[],
 'refutes':['Unsmoothed outcome1 constant-seed reference is a finite complete reference after a surviving point edit'],
 'first_unproved_line':'Price the next prescribed conversion on the already exposed block from SAME remaining source, inherited R and old signed query/KL accounts; then generalize beyond the specific three-bit tensor log kernel. Controller entropy L remains an explicit terminal debt.',
 'next_consumers':['A022','A025','A028','A029','A087','A094']}
dump(R/'CLAIMS.json',[claim])
progress={
 'protocol_revision':protocol['revision'],'run_id':R.name,'stream':'B05','packet_id':'A021',
 'gap_id':'C024-NONFLAT-INHERITED-REFERENCE-CONVERSION','attempt_id':'A021-stage18-single-tensor-data-query',
 'method':'Consume A025 solved all-cut transport; sharpen A022 SAME original signed vertex charge; prescribed normalized positive child references; exact full joint CE/KL and physical pivot accounting.',
 'mathematical_delta':'SAME-source joint reference reserve improved from old guaranteed t/64 to t/4 by retaining J/s covariance. One actual nonflat data-coordinate conversion loses<1/8 capacity, releases at t>=3, and leaves>=11t/64 after old U. Both child CE/KL retained; raw entropy query can still exceed4d.',
 'deliverable_status':'COMPLETE_LOCAL; INDEPENDENT_REVIEW_PENDING','mathematical_status':'SCOPED_AUTHOR_PROOF; FULL_FEI_OPEN',
 'claim_versions_used':deps,'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1}],
 'source_artifacts':['PROOF.md','SEARCH_SPEC.json','REPLAY_SPEC.json','FORMAL_SPEC.json','out/SOURCE_RECEIPTS.json','out/PILOT.json','out/DIRECT.json','out/SCALAR.json','out/REPLAY.json','out/LEAN.json'],
 'next_consumers':claim['next_consumers'],
 'next_action':'Expose a second coordinate in the already converted block, retaining SAME R, old U, first signed entropy/KL account and actual unused11t/64 source. Price prescribed normalized references without restoring the original local q; then remove specific tensor log kernel.',
 'stagnant_substantive_attempts':0,
 'blockers':['General inherited-reference conversion and arbitrary source admission remain open','Controller entropy L=delta H(a) is retained; no universal controller certificate','Independent review and supervisor copy pending'],
 'packet_ids':['A021']}
dump(R/'PROGRESS.json',progress); dump(R/'PACKET_DELTA.json',progress)
direct=json.loads((R/'out/DIRECT.json').read_text(encoding='utf-8')); replay=json.loads((R/'out/REPLAY.json').read_text(encoding='utf-8')); pilot=json.loads((R/'out/PILOT.json').read_text(encoding='utf-8'))
lean=json.loads((R/'out/LEAN.json').read_text(encoding='utf-8-sig')); formalstatus=lean.get('result',lean).get('status','UNVERIFIED')
report=f'''# exact target, quantifiers, hypotheses and units

Full FEI remains OPEN. This stage consumes A025's all-cut solution of our prior NEXT, then pays one concrete inherited-reference conversion on A022's nonflat tensor point-surgery family. For EVERY t>=2, every data vertex, every independent Boolean control indicator (arbitrary dimension/bias), and ANY original data coordinate, keep the original product data reference Q, original controller spectral reference R, old booked U<=t/64, and both physical child terminal expressions. Entropy and cross-entropy are in bits.

The SAME original source admits the sharper complete-reference reserve t/4. This differs from the prior guaranteed t/64 because the signed vertex costs J and s are bounded jointly instead of separately; no source account is reset. The prescribed child data references are uniform4 at outcome0 and(13/16,1/16,1/16,1/16) at outcome1 on the queried block, with ALL other blocks and R unchanged. The actual reference-capacity loss is<1/8, negative for t>=3, and after old U the complete child bank is>=11t/64. The original t/64 reserve remains present.

# sources actually read, revisions and theorem locators

BOARD.md supervisor2026-10-23 00:10UTC, B05 STREAM_NOTES.md v2 and own STATUS/LEARNED were read at entry. The lead's historical remainder-sign correction was completed earlier and is not repeated. EXECUTION_PROTOCOL.json revision{protocol['revision']} supplies the schema and computation rules; its historical campaign endpoint is superseded by the current owner deadline. No schedules or workers are changed.

Primary sources: A025 run20261022T231646Z REPORT.md and PROOF.md, general signed-account identity, root admission and final-collapse sections; A022 run20261021T213608Z REPORT.md Sections2--6, original joint reference, signed kernel and tensor reserve; own prior run20261021T184331Z PROOF/OBSTRUCTION. Exact source hashes and selected line locators are in out/SOURCE_RECEIPTS.json, together with current campaign indices. Prior baseline paper imports remain provenance and add no premise here. This stage makes no literature novelty claim and uses no web source.

A025's entropy-only all-cut account is independently reconstructed at its stated scope and consumed, rather than duplicated. A022's exact joint-reference formula is reconstructed. The improved reserve is a new estimate by A021, so it is NOT labeled an independently accepted strengthening. Wake reported owner-model notes about87h and state-of-mind notes about71h old; those degraded context layers were reported and not used as mathematical or task authority.

# complete derivation or exact first unsupported line

PROOF.md is the complete all-parameter derivation. Original joint reference CE equals H(b)+L plus the signed surgery log cut and controller marginal terms. Local costs satisfy4J_g-8s_g<=24-7log2(3), giving original source reserve>=179t/576>t/4. The estimate pays surgery and old U from the original4I(b)-H(b)-U; child conditions do not mint a new source.

For the queried block, exact data/control marginals show C0-C1=1+G+delta alpha*w, where G=(1/2)log2(13)-(9/8)log2(3), and the three cases of w are given in PROOF Section3. The physical pivot mass is d=1/4+2delta alpha sigma. Integer-certified logarithm bounds give4d-(C0-C1)<1/8 for t>=2 and<0 for t>=3. Thus the complete child reference bank is exactly the parent bank minus this loss and remains>=11t/64 after old U. No rare physical outcome is removed.

The actual entropy decrement is NOT the reference drop: D_i=(C0-C1)+average childKL-parentKL. Both full child KLs, the parent mismatch and the signed physical query account are kept in the exact identity Bchild+average childKL+(4d-D_i)=Bparent+parentKL. In particular this is NOT an all-coordinate D_i<=4d theorem; already an unedited g block has D_i/d>4. The full controller entropy L=delta H(a) remains an unpaid terminal unless a separate certificate is supplied.

An unsmoothed canonical constant-child reference is rigorously invalid: a surviving edit has positive nonempty spectral mass where that reference is zero, making CE infinite. The positive smoothed prescription is part of the theorem. First unsupported universal line: price a subsequent prescribed conversion after this block has already changed, from the SAME remaining source, R, U and signed query/KL accounts. Arbitrary nonflat source admission and arbitrary controller entropy remain open.

# executed validation with domain, arithmetic, commands and outputs

SEARCH_SPEC.json froze1152 direct cases: t=2, all64 vertices, six explicitly listed two-bit control indicators and all3 coordinate types in one block. Block permutation covers every original coordinate. The72-case pilot passed{pilot['assertions']} exact assertions in{pilot['seconds']:.4f}s. The full suite passed{direct['assertions']} exact assertions in{direct['seconds']:.4f}s. It uses integer Walsh transforms, physical edge counts, Fraction-valued canonical prime-log expressions for identities, and40-term rational atanh intervals with explicit geometric tails for signs. It checks both child joint references and KLs, original R preservation, physical influence, exact conversion formula, old-U/reserve retention and the complete signed identity. Scalar domain t=2..40, all8 local vertices and alpha=0,1/2,1 has936 cases, plus six exact integer logarithm certificates. The finite tests support, rather than replace, the all-t proof.

The independent replay imports no production helper and reconstructs actual truth tables and Fourier coefficients by direct character sums. Its8 declared cases include vertices0,1,3,63, point/full controls and the first coordinate. It uses48-term rational logarithm intervals. It passed{replay['assertions']} assertions in{replay['seconds']:.4f}s. Main plus independent replay total{direct['assertions']+replay['assertions']} exact assertions; pilot counts are separate. There were no failed mathematical cases or precision tolerances.

Commands from this run:

    python -X utf8 code/check.py --pilot
    python -X utf8 code/check.py
    python -X utf8 code/replay.py
    python -X utf8 code/formal.py
    python -X utf8 code/admin.py

Checks that could fail were named in the frozen specification: reference support, preserving R in BOTH children, original source ownership, physical reach factors and confusing reference loss with entropy loss. Endpoints alpha=0,1 and all local vertex types are tested. R zero rows are checked against actual Fourier support; no division by alpha or a seed coefficient occurs. Integer-power bounds verify every logarithm estimate used. There are no limit exchanges. Direct jobs estimate100MB, independent replay60MB, each capped at60s, with no dimension escalation, GPU, remote compute or detached producer.

Formal bookkeeping receipt: {formalstatus}. The fresh memok result and any compiler receipt are saved in out/MEMOK.json and out/LEAN.json. code/Book.lean concerns only addition of two Nat inequalities, not the Fourier proof. No formal result is extrapolated to the analytic theorem. Mathematical rung: author-checked proof pending independent review.

# proof dependencies and changed downstream conclusions

The A025 all-cut source-account identity is consumed at its exact scope; its entropy-only transport does not pay this conversion by itself. The original A022 signed source/reference formula is used with full support and all controller/KL terms. A022's historicalt/64 result remains valid; this stage sharpens its original charge and shows one real conditional conversion leaves that reserve intact. Neither source is accepted wholesale as a universal route. The new claim is a narrow source-bound extension, not a new broad universal candidate or a new FEI constant for the already certified family.

A022/A025/A028/A029 can now carry these specified complete child references, both child KLs and old U. They cannot replace the modified local reference with the original q, reset R to a conditional prior without pricing it, or rename the reference-capacity loss as the entropy decrement. Source/method provenance and exact dependency versions are in CLAIMS.json.

# one next mathematical action and independent reviewer

Expose a second data coordinate in the ALREADY converted block. Retain the same original controller R, Qrest, old U, the first query's signed entropy/KL account and the actual unused11t/64 capacity. Price explicitly prescribed positive normalized child references without restoring q. A022/A025 should reconstruct source and marginal formulas; A028/A029 should reconstruct the exact signed capacity/entropy relation; A087/A094 should audit zero-row support and whether every old booking survives. These are saved review handoffs, not sent messages or claims of observed acceptance.

# actual persistence receipts or precise save blocker

The requested REPORT.md, CLAIMS.json, PROGRESS.json and byte-identical PACKET_DELTA.json are saved with proofs, frozen specs, self-contained code and exact outputs. out/ARTIFACT_CHECK.json validates exact protocol fields, statement digest, compatibility, per-file size and persisted artifact hashes. Rolling STATUS.md, WORKLOG.md and LEARNED.md are current. No git, email, brain write, other-agent mutation or public upload is performed. Supervisor copying, mirror verification and independent review remain pending; required wake/checklist/formal helper state is the only administrative side effect outside A021. Shared-checklist failures, if any, are recorded separately and do not imply local persistence failure.

**Universal bridge:** This stage advances C024 history transfer toward C019 by consuming the completed entropy-only all-cut account and paying ONE actual nonflat inherited-reference conversion with the original Qrest/R, both full terminal KLs and old U retained. A sharper SAME-source charge yields t/4 capacity; after conversion at least11t/64 remains, including the originalt/64 reserve. The unpaid universal step is subsequent conversion and arbitrary source admission, not entropy telescoping. NEXT prices the next query on the already modified block with no reference or bank renewal, the shortest remaining test of a reusable universal transfer rather than another isolated class FEI bound.
'''
write(R/'REPORT.md',report)
write(A/'STATUS.md','STATE: A021 stage18: nonflat original-Q/R data-query conversion paid; SAME source t/4 reserve, child bank>=11t/64 with old U and BOTH full KLs; main183494+independent2188 checks PASS; review pending; FEI OPEN.\nNEXT: Second data coordinate in ALREADY converted block, same R/Qrest/old U and first signed query/KL account; pay prescribed positive references from actual11t/64, no reset; A022/A025/A028/A029/A087/A094 review.\n')
stamp=datetime.now(timezone.utc).isoformat()
with (A/'WORKLOG.md').open('a',encoding='utf-8',newline='') as f:
 f.write('\n'+stamp+' stage18 '+R.name+': A025 all-cut transport independently reconstructed and consumed; shifted to A022 nonflat inherited-reference NEXT. Signed J/s coupling improves ORIGINAL joint-reference surplus to>=179t/576>t/4. Prescribed local uniform4/(13,1,1,1)/16 child refs with SAME controller R have capacity loss<1/8 (negative t>=3); after oldU<=t/64 childbank>=11t/64. BOTH child joint KL and actual signed entropy query kept. Pilot13842, main183494, independent2188 assertions PASS; no failures. Formal '+formalstatus+'. Local protocol/rolling artifacts saved; FEI open.\n')
with (A/'LEARNED.md').open('a',encoding='utf-8',newline='') as f:
 f.write('\nStage18: A025 all-cut identity solves prior current-terminal-collapse NEXT; no need to repeat it. A022 b=g tensor t (g three-bit000 defect), arbitrary controlled point edit, original Q=P_b and controller spectral R: bounding signed4J-8s jointly gives complete ORIGINAL CE surplus>=179t/576>t/4. One original data query: Q0 localuniform4, Q1 local(13,1,1,1)/16; retain original Qrest and SAME R in BOTH children. Exact drop=1+G+delta alpha w, G=.5log13-9log3/8; physicald=.25+2delta alpha sigma. Capacity lossell=4d-drop<1/8 for allt>=2, ell<0 fort>=3. OldU<=t/64 leaves>=11t/64 child reference bank, including originalt/64 reserve. DO NOT call ell actual entropy loss: D_i=drop+average childKL-parentKL. Full signed identity retains both childKLs and old source. Unsmoothed constant-child reference has infinite CE after surviving point edit. No arbitrary next-query conversion or controllerFEI admission. NEXT second coordinate of already converted block with same source, modified refs, R, oldU and signed query account.\n')
# Final schema, proof receipt and persistence checks.
expected=lambda fs:{x.split(' (')[0] for x in fs}
assert set(progress)==expected(protocol['required_per_run']['progress_fields'])
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
assert sha(R/'PROGRESS.json')==sha(R/'PACKET_DELTA.json')
assert hashlib.sha256(statement.encode()).hexdigest()==claim['statement_sha256']
for field in protocol['required_per_run']['report_fields']: assert '# '+field in report
assert report.rstrip().splitlines()[-1].startswith('**Universal bridge:**')
assert direct['status']==replay['status']==pilot['status']=='PASS'
files=[]
for p in R.rglob('*'):
 if p.is_file() and p.name!='ARTIFACT_CHECK.json':
  assert p.stat().st_size<20_000_000
  files.append({'path':str(p.relative_to(R)),'sha256':sha(p),'bytes':p.stat().st_size})
receipt={'status':'PASS','protocol_exact':True,'compatibility_identical':True,'statement_digest_valid':True,'main_assertions':direct['assertions'],'independent_assertions':replay['assertions'],'pilot_assertions_separate':pilot['assertions'],'main_plus_replay':direct['assertions']+replay['assertions'],'formal_status':formalstatus,'independent_review':'PENDING','remote_copy':'SUPERVISOR_PENDING','files':files}
dump(R/'out/ARTIFACT_CHECK.json',receipt)
print(json.dumps({k:v for k,v in receipt.items() if k!='files'}))
