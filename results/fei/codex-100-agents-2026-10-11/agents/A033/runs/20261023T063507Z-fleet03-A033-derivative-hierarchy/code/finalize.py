from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
ROOT=Path(__file__).resolve().parents[1];AGENT=ROOT.parents[1];BASE=AGENT.parents[1]
def rd(p):return Path(p).read_text(encoding='utf-8-sig')
def wr(p,s):Path(p).write_text(s,encoding='utf-8',newline='')
def dump(p,v):wr(p,json.dumps(v,indent=2)+'\n')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
v=json.loads(rd(ROOT/'out/validation.json'));assert v['status']=='PASS'
assert v['physical_face_states']==6968 and v['internal_query_transitions']==5832
assert v['helper_sha256']==sha(ROOT/'code/check.py')
now=datetime.now(timezone.utc).isoformat();cid='A033-FEI-HARD-ZERO-REFUND-WINDOW'
st='For every Boolean g on n>=1 uniform independent inputs and every fixed L>=2, let h_L(x)=g(product of the L physical bits in block j : j=1..n). Its full squared Fourier spectrum is exactly ghat^2 on unions of whole blocks; H(h_L)=H(g), I(h_L)=L I(g), so uniform FEI on this class for any fixed L is full-FEI-equivalent up to factor L. At every physical restriction with at least one bit remaining in each block the full spectrum and any supplied finite calibrated core reference R, R(empty)=(Eg)^2, are pushed forward by the remaining-block injection; all reference-only atoms and full arbitrary-core CE survive. At every query whose block has at least two remaining bits, the spectral fiber contains at most one actual/reference image atom: BOTH child squared laws equal the marginalized parent law, physical query entropy decrement, conditional erasure, JS and conditional occupancy KL are zero. For ANY complementary disjoint controller A,B and BOTH actual tag children A+sigma B h_L with current coherent signed-vacuum reference, the FULL controller-vacuum-plus-tail calibration refund is also zero; the physical query influence is beta Inf_j(g). Every adaptive tree of depth D<L has this property at all internal queries, retaining the whole arbitrary core spectrum at every leaf. These are actual full-Boolean functions satisfying the complete convolution/derivative hierarchy, not fixed-prefix controls. This is a local-refund/bounded-lookahead obstruction, not an FEI disproof or a refutation of a genuinely unused ancestor bank.'
claim={'claim_id':cid,'version':1,'exact_statement':st,'hypotheses':['Uniform independent disjoint physical blocks; fixed L for each family','Every stated zero-refund query leaves at least one unqueried bit in its block','Supplied complete source reference R is finite on the actual core spectrum and vacuum-calibrated; its price is not assumed universally cheap','Full terminal spectra, reference-only atoms and BOTH children remain; bits throughout'],'statement_sha256':hashlib.sha256(st.encode()).hexdigest(),'contributors':['A033'],'proof_source':{'path':str(ROOT/'PROOF.md'),'sha256':sha(ROOT/'PROOF.md'),'validation':['out/validation.json'],'formal_verification':'NOT_LAUNCHED_MEMORY_GATE'},'proof_dependencies':[],'review_records':[],'status':'AUTHOR_PROOF_WITH_EXACT_CERTIFICATES_INDEPENDENT_REVIEW_PENDING','supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['A032','A079','A088','A094','A096','A097','B07','B20']}
dump(ROOT/'CLAIMS.json',[claim])
nxt='Quantify which prescribed zero-refund profile changes can be paid by ORIGINAL local influence; then price necessary conversions across an actual block-completion/selection frontier from SAME unused ancestor account. A096/A097/A032/A079/A088/A094 review; no new fixed-bank reset cycles.'
p={'protocol_revision':'2026-10-11-execution-v2','run_id':ROOT.name,'stream':'B07','packet_id':'A033','gap_id':'G-BOOLEANITY','attempt_id':'A033-FEI-HARD-ZERO-REFUND-WINDOW-1','method':'Arbitrary-core physical product-block lift; exact full Fourier/reference injection on ALL allowed faces; Boolean zero-refund window obstruction','mathematical_delta':'Parity-only zero-refund guard extends to a FULL-FEI-HARD arbitrary Boolean core family. For every finite physical lookahead there are fully Boolean lifts with zero erasure/JS/occupancy/coarse signed-vacuum refund throughout, yet all core entropy and CE remain. No universal source price gained.','deliverable_status':'COMPLETE_LOCAL','mathematical_status':'AUTHOR_PROOF_EXACT_CERTIFICATES; FULL_FEI_OPEN; INDEPENDENT_REVIEW_PENDING','claim_versions_used':[],'claims_created_or_changed':[{'claim_id':cid,'version':1}],'source_artifacts':['PROOF.md','FROZEN_SPEC.json','code/check.py','out/pilot.json','out/validation.json','out/formal_status.json'],'next_consumers':claim['next_consumers'],'next_action':nxt,'stagnant_substantive_attempts':0,'blockers':['Universal initially influence-priced source/necessary global reset payment remains open','Original cyclic atom-cap construction/checker absent locally; inherited summary only','Formal compiler not launched: memok exit1, physical2.0GB<4GB and commit6.0GB<8GB','New claim independent review and supervisor publication unverified'],'packet_ids':['A033']}
dump(ROOT/'PROGRESS.json',p);wr(ROOT/'PACKET_DELTA.json',rd(ROOT/'PROGRESS.json'))
report=f'''# exact target, quantifiers, hypotheses and units

Find the actual scope of A096's zero-singleton refund obstruction, beyond
parity, without assuming a cheap initial source. For EVERY Boolean core g
and EVERY fixed block width L, (1)--(7) in PROOF.md preserve the complete
core spectrum and arbitrary finite calibrated reference through every
allowed adaptive physical prefix. Every query leaving a bit in its block
has ZERO full current refund, including the controller-vacuum profile.
Entropy/CE/KL are bits; influences are original physical influences.
Full FEI remains OPEN. Quantitative local-price consequences in section5
are developed and independently certified in the next requested stage.

# sources actually read, revisions and theorem locators

Entry BOARD2026-10-23 06:27UTC, B07 STREAM_NOTES v2 and own STATUS were
read; protocol v2 was consulted against its unchanged schema. A032
run20261023T054918Z PROOF through third-reset derivation and A096
run20261023T053800Z DERIVATION sections1--4 plus exact first claim were
read. A032 independently HOLDS A033's preceding post-tag identity;
A096 phase-funded rule correctly makes no change at d=0. No new source
lemma is assumed: the lift proof is self-contained. Prior campaign/paper
intake remains background. The current23October14:49UTC endpoint governs.
Old fixed-order G_(K,w), dyadic, atom-cap-prefix and small-defect no-go
directions are inherited from A033 prior NO_GO_IMPORT.md, not retried;
the distinct cyclic atom-cap original source/checker is still missing.

# complete derivation or exact first unsupported line

Every core monomial lifts to the union of its physical blocks. Before
block completion, restrictions merely shorten blocks and change Fourier
signs by known exposed products. The map of frequencies is injective.
Every admissible query fiber has at most one image atom for BOTH actual
and inherited reference laws, including reference-only atoms. Its two
actual child squared spectra equal the common marginal; conditional
erasure, JS and occupancy KL vanish exactly. Signed wrapper vacuum
coefficients and tail masses are unchanged, so even the FULL A033 coarse
KL is0. No scalar-only relaxation is used. All terminal H(g) and CE(g,R)
remain. Arbitrary adaptive trees follow by the per-face identity, not
an invalid multiplication of conditional inequalities.

For fixed L, H(h_L)=H(g), I(h_L)=L I(g). Therefore this obstruction class
is full-FEI-hard up to constant L and cannot be discarded as a solved
special case. For any proposed finite depth D choose L>D. These functions
are Boolean pointwise and obey ALL signed convolution and restriction
identities; a more complete finite Booleanity prefix does not remove them.
The first unsupported universal repair remains payment of NECESSARY
profile changes across a block-completion/selection tree from UNUSED
original influence, retaining the full arbitrary core and all old debits.

# executed validation with domain, arithmetic, commands and outputs

Frozen spec precedes the search. Pilot:164 faces,72 internal queries,
4149 exact checks PASS in0.276644s. Completed final:6968 actual physical
faces,5832 internal queries, {v['exact_assertions']} exact assertions PASS
in{v['runtime_seconds']:.6f}s. This covers ALL cores through3 bits at width2,
ALL16 two-bit cores at width3 through depth2, and four explicitly frozen
boundary cores at width4 through depth3. Both outcomes, true/nonflat
references, reference-only atoms and both tag signs are checked. Integer
FWHT verifies the full signed spectrum; direct physical edges independently
verify influences. Exact rational fiber/injection certificates prove H/CE
identities without floating logarithms. The universal statement follows
from the proof, not finite extrapolation. Command: python -B -X utf8
runs/{ROOT.name}/code/check.py. After a new owner stage message the first
launch's interaction handle was unavailable and no completed output was
present; the same frozen command was completed subsequently. No success
or extra counts are assigned to that unreceipted launch.

Fresh memok exited1: physical2.0GB below4GB and commit6.0GB below8GB.
No compiler or >300MB job was launched; exact Python estimate65MB.
Formal status NOT_LAUNCHED_MEMORY_GATE. No GPU/detached worker/git/mail/
brain write/other-agent mutation or stop of existing work occurred.

# proof dependencies and changed downstream conclusions

New theorem is self-contained. A096's parity guard was a correct boundary;
this stage expands it to arbitrary cores and arbitrary finite physical
lookahead. A096's phase-funded theorem and A032's paid reset chain are NOT
refuted. No universal ancestor-bank payment, full FEI or new Booleanity-
specific admission inequality is obtained. External review/adoption and
supervisor copying are unverified.

# one next mathematical action and independent reviewer

{nxt}
This is a saved source-bound handoff, not a sent message.

# actual persistence receipts or precise save blocker

Four protocol files, proof/spec/helper and complete outputs are here.
out/PERSISTENCE_RECEIPT.json checks field keys, hashes, actual completed
counts, size limit and identical progress/delta. Rolling notes are current.
All research writes are within A033; supervisor publication unverified.
Brain self-care degraded/unverified: stale owner/state notes affect only
personal-context freshness and were not authorization or mathematical facts.

# Universal bridge

This stage sharpens the C024/C019 obstruction from a single parity example
to EVERY arbitrary-core full-FEI-hard product-block family: a bounded
physical query window earns exactly zero complete refund while retaining
the ENTIRE unpaid core entropy and reference. Universal price gained:0.
What remains is a selection/ancestor-payment theorem at actual block
completion, not a hidden positive local refund. NEXT quantifies the local
influence-price repair on actual Boolean low-influence cores, then targets
that precise universal global payment rather than another fixed prefix
or another isolated paid-reset class.
'''
wr(ROOT/'REPORT.md',report)
dump(ROOT/'out/formal_status.json',{'status':'NOT_LAUNCHED_MEMORY_GATE','exit_code':1,'physical_free_GB':2.0,'commit_free_GB':6.0,'compiler_started':False})
wr(AGENT/'STATUS.md','STATE: Full-FEI-hard arbitrary-core product-block family has EXACT zero erasure/JS/occupancy/FULL signed-vacuum refund through every precompletion query;262673 exact checks PASS;FEI OPEN.\nNEXT: Quantify fixed-strength reset/current-influence obstruction on majority cores; then pay necessary block-completion conversion from SAME unused ancestor influence, full terminals/old debits retained;A096/A097/A032/A079/A088/A094 review.\n')
for name in ('WORKLOG.md','LEARNED.md'):
 text=rd(AGENT/name)
 if ROOT.name not in text:wr(AGENT/name,text+f'\n{now} - {ROOT.name}: Arbitrary Boolean g lifted by disjoint L-bit products has H unchanged,I multiplied by L. Every physical query before block completion has zero erasure,JS,occupancy KL and FULL signed-vacuum coarse refund, for arbitrary finite nonflat calibrated core R; CE/core entropy and reference-only atoms persist exactly. Thus bounded-lookahead refund supply fails on a full-FEI-hard Boolean family, not just parity. Final6968 faces/5832 query transitions/262673 exact assertions PASS. Universal initial source/necessary ancestor conversion still open. NEXT: quantify local-rate failure, then actual completion/selection account.\n')
fields=set('protocol_revision run_id stream packet_id gap_id attempt_id method mathematical_delta deliverable_status mathematical_status claim_versions_used claims_created_or_changed source_artifacts next_consumers next_action stagnant_substantive_attempts blockers packet_ids'.split());assert set(p)==fields
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
files=[x for x in ROOT.rglob('*') if x.is_file() and x.name!='PERSISTENCE_RECEIPT.json'];assert all(x.stat().st_size<20*1024*1024 for x in files)
dump(ROOT/'out/PERSISTENCE_RECEIPT.json',{'status':'PASS','at':now,'file_count':len(files),'exact_protocol_keys':True,'progress_delta_identical':True,'statement_sha256':claim['statement_sha256'],'files':[{'path':str(x.relative_to(ROOT)),'bytes':x.stat().st_size,'sha256':sha(x)} for x in files]})
print(json.dumps({'status':'PASS','run':ROOT.name,'faces':6968,'checks':v['exact_assertions'],'full_fei':'OPEN'}))
