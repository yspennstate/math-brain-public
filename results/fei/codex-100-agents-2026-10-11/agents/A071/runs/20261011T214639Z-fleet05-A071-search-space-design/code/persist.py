import hashlib,json
from datetime import datetime,timezone
from pathlib import Path

root=Path(__file__).resolve().parents[1];agent=root.parents[1]
def write(name,data):
    (root/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
spec=json.loads((root/'FROZEN_SPEC.json').read_text());s=json.loads((root/'out/search.json').read_text());z=json.loads((root/'out/zero_certificates.json').read_text());pilot=json.loads((root/'out/pilot.json').read_text())
assert s['cases']==20736 and not s['violations'] and z['exact_zero_certificates']==len(s['unresolved'])==600 and not z['remaining']
write('SEARCH_DOMAIN.json',spec)
(root/'SEARCH_BUDGET.md').write_text(f'''Frozen before execution: FROZEN_SPEC.json; equality follow-up frozen in ZERO_RESOLUTION_SPEC.json.
One Python process, serial loops, no worker pool, no GPU, no automatic dimension increase. Each computational job has a 55-second elapsed-time cap checked after bounded batches. Expected peak RAM <=100 MB for grid, <=30 MB for equality resolution; no >300 MB job was started. RAM was estimated, not measured. CPU is a single serial execution lane, with no promise of exclusive hardware.
Pilot: 768 cases in {pilot['runtime_seconds']:.6f} s (<60 s).
Full grid: 20736 cases in {s['runtime_seconds']:.6f} s.
Equality resolution: 600 cases in {z['runtime_seconds']:.6f} s.
Command startup/tool latency is distinct from the computational runtimes recorded by perf_counter. The timeout can overrun by one bias-vector batch; measured full job remained below 55 seconds. No heavy job or memok gate was needed for this bounded low-memory search.
''',encoding='utf-8')
statement='For every Boolean sign f on {0,1}^3, every product-bias vector p in {1/8,1/4,1/2,3/4,7/8}^3, and every nonempty proper physical block A, J_A <= M_A + Delta_A(p), with M_A=H(S_A|S_B), J_A=H(S_B)-E_Z H(mu_Z), Delta_A=sum_i_in_A[h2(p_i)+log2(max(p_i,1-p_i))], and mu_Z the inherited biased squared Fourier law of the actual restriction. Entropy is in bits.'
hyp=['Actual Boolean truth table, not arbitrary real amplitudes','Independent physical coordinates at the specified finite bias grid','Inherited normalized product Fourier basis','Zero spectral masses contribute zero entropy']
claim={'claim_id':'A071-B09-THREEBIT-GRID-CERTIFICATE','version':1,'exact_statement':statement,'hypotheses':hyp,'statement_sha256':hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':')).encode()).hexdigest(),'contributors':['fleet05/A071'],'proof_source':['REPORT.md','code/search.py','code/resolve_zeros.py','out/search.json','out/zero_certificates.json'],'proof_dependencies':[],'review_records':[],'status':'EXACT_FINITE_CERTIFICATE_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['A072','A073','A074','A085','A092','B09','B20']}
write('CLAIMS.json',[claim])
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':root.name,'stream':'B15','packet_id':'A071','gap_id':'G-BIASED-TAX','attempt_id':'A071-G-BIASED-TAX-001','method':'Exhaustive bounded actual-Boolean truth tables; rational weighted spectra; rigorous atanh intervals; exact prime-log equality resolution','mathematical_delta':'Frozen complete finite family and certified 20736 representatives of 192000 raw cases; 20136 interval passes plus 600 exact cancellations; no violation. Does not close the universal B09 lemma or full FEI.','deliverable_status':'COMPLETE_LOCAL_SAVED','mathematical_status':'FINITE_GRID_CERTIFIED_UNREVIEWED; FULL_FEI_OPEN','claim_versions_used':['B09-BIASED-BLOCK-UNCERTAINTY@1 (target only, not proof dependency)','B09-TAXFREE-AND-COUNTEREXAMPLE-REPAIRED@1 (calibration only)'],'claims_created_or_changed':['A071-B09-THREEBIT-GRID-CERTIFICATE@1'],'source_artifacts':['REPORT.md','SEARCH_DOMAIN.json','SEARCH_BUDGET.md','FROZEN_SPEC.json','ZERO_RESOLUTION_SPEC.json','code/search.py','code/resolve_zeros.py','out/pilot.json','out/search.json','out/zero_certificates.json'],'next_consumers':['A010','A032','A047','A072','A073','A074','A085','A092','B09','B20'],'next_action':'A085/A092 independently reconstruct grid coverage and log certificate; A074 reproduce the minimum-positive case using centered tensor transforms. B09 may use the family to test an explicitly versioned sharper singleton tax; do not raise n automatically.','stagnant_substantive_attempts':0,'blockers':['B15 lead STREAM_NOTES.md absent at stage start; no direction inferred','Independent review and supervisor copy/mirror not yet observed'],'packet_ids':['A071']}
write('PROGRESS.json',progress);write('PACKET_DELTA.json',progress)
report=r'''# A071 / B15: bounded search-space design and exact biased-block grid certificate

## exact target, quantifiers, hypotheses and units

Target: B09-BIASED-BLOCK-UNCERTAINTY@1 in CLAIM_REGISTRY.json. For any actual Boolean sign under independent interior biases and a physical block A with complement B, the live helper asserts 0 <= J_A <= M_A+Delta_A. Here M_A=H(S_A|S_B), J_A=H(S_B)-E_Z H(mu_Z), and Delta_A=sum_i_in_A[h2(p_i)+log2(max(p_i,1-p_i))]. All entropy is in bits. Z is a physical input assignment, not a spectral conditioning event. We test its upper inequality; J>=0 follows from the exact mixture identity and entropy concavity.

Family: all three-bit truth tables, all six nonempty proper physical blocks, and p_i in {1/8,1/4,1/2,3/4,7/8}. Assignments x=0..7 use little-endian bits. Output complement lets f(000)=+1; seven code bits specify the remaining signs, giving 128 tables. Input flips paired with p_i -> 1-p_i preserve every squared coefficient (a sign changes on the flipped basis coordinate) and biject the physical children with unchanged branch weights. Delta also stays fixed. Therefore use ordered p_i in {1/8,1/4,1/2}: 27 bias vectors. This covers the entire raw 256*125*6=192000 grid with 128*27*6=20736 representatives. It is a covering reduction, not a claim that all representatives lie in distinct orbits. No coordinate permutations or multiplication by an input character are quotiented: biased character multiplication does not preserve squared spectra generally.

Dummy coordinates embed all n<=2 proper-block cases. Empty blocks have J=M=Delta=0; full blocks have J=0 and M>=0, Delta>=0. For p<=1/2, delta=p log2((1-p)/p)>=0, and reflection handles p>=1/2. No claim covers off-grid parameters or n>=4. A finite helper falsifier would be sufficient to refute its universal statement, but this search found none.

## sources actually read, revisions and theorem locators

EXECUTION_PROTOCOL.json read in full: revision 2026-10-11-execution-v2. Read campaign README, CURRENT_STATUS, CLAIM_REGISTRY, OBSTRUCTION_REGISTRY, PACKET_STATUS B15 records, STREAM_NEXT_ACTIONS B15, and plan A071-A075 contracts (LaTeX lines 958 onward). Read BOARD.md at stage start: 2026-10-11 21:45 UTC snapshot, no earlier B15 result. B15 STREAM_NOTES.md was absent. Earlier run reports B05/B09/B19 were consulted; B09 sections 2-4 supply the precise target definitions, section 5(4) is flagged in the registry as unsupported tax-necessity reasoning. This stage does not use that reasoning.

Supplement CAMPAIGN, CLAIMS (C005-C007, C022-C025, retired C027-C034), COUNTEREXAMPLES, SEED_LEMMAS, NATIVE_MAPPING and source notes were consulted. BLOCK_RESTRICTION_IDENTITY sections 1-3 were read for physical versus spectral experiment distinctions. ONE_BIT_ENDPOINT and ROUTE_MAP were consulted for the two-address scope; the existential constant there is unsuitable for a single finite falsifier without choosing an additional fixed constant. Hence the named current B09 helper was preferred.

Local context papers were consulted in their text versions: threshold_paper_38pp introduction/Theorems A-D, Fourier preliminaries, product-bias normalization and Section 6.4; threshold_paper_29pp_earlier_version composition/restriction locators; percolation_spectral_pivotal_entropy_30pp introduction, normalized product characters and Theorems 1.1-1.6; 31pp earlier version introduction. Their class results are context, not proof dependencies of this exact certificate. No claim of complete independent reconstruction of these manuscripts or of the Maassen-Uffink theorem is made. Local hashes are persisted in out/source_receipts.json.

## complete derivation or exact first unsupported line

Let m_i=8p_i, w(x)=product_i[m_i if x_i=1 else 8-m_i], and V_S=sum_x f(x)w(x) product_i_in_S(8x_i-m_i). In the orthonormal centered basis phi_i=(x_i-p_i)/sqrt(p_i(1-p_i)), the exact squared coefficient is

    mu(S) = V_S^2 / [8^(2n) product_i_in_S m_i(8-m_i)].

This follows by writing each expectation with its physical probability numerator and cancelling the 8 powers in the variance normalization. All masses are rational, nonnegative and sum to one (checked for every parent and child). Each restricted table is constructed by the actual fixed physical assignment. The code checks q(T)=sum_R mu(R union T)=sum_z P(Z=z)mu_z(T) in Fraction arithmetic for every tested case. Thus the defect is exactly

    D = M+Delta-J = H(mu)-2H(q)+E_Z H(mu_Z)+Delta.

For rational t in [1,2], use y=(t-1)/(t+1), so 0<=y<=1/3. The natural logarithm has positive expansion 2 sum_j>=0 y^(2j+1)/(2j+1). After N=32 terms its remainder is between 0 and 2 y^(2N+1)/[(2N+1)(1-y^2)]. Each retained term is floored at scale 2^80; adding N plus the ceiling of the scaled tail is a rigorous upper enclosure. Range reduction p=2^k t and the separately enclosed ln 2 gives a natural-log interval; multiplication by negative k reverses endpoint order. The base-two division takes extrema of all four rational corner quotients, then floors/ceilings at scale 2^60. Powers of two are evaluated exactly. Multiplying by the negative entropy coefficient -p swaps endpoints. Linear interval arithmetic then encloses D with no floating sign decision.

The initial intervals certified 20136 cases nonnegative, including 504 exact zeros. The other 600 intervals contained zero. A separate frozen follow-up expands each D as a rational linear combination of logarithms of rational masses, factors numerator and denominator integers into primes, and sums each prime's exact coefficient. Every coefficient is zero in all 600 cases, proving D=0 without numerical precision refinement. The follow-up also matches each such parent spectrum using a second algorithm: recursively transform physical value pairs (u,v) to ((1-p)u+pv,v-u), then square the centered-basis coefficients and multiply by product variances. This is a second implementation by the same contributor, not independent review.

Consequently every representative satisfies D>=0; the proved invariances extend this finite certificate to the raw grid. There is no unsupported line within the stated finite claim, subject to independent implementation review. The first unsupported extrapolation would be: grid verification implies the same bound for all real biases and dimensions. We do not make it.

## executed validation with domain, arithmetic, commands and outputs

All commands were run from the A071 workspace, with Python UTF-8 and no randomness:

    python -X utf8 runs/20261011T214639Z-fleet05-A071-search-space-design/code/search.py --pilot
    python -X utf8 runs/20261011T214639Z-fleet05-A071-search-space-design/code/search.py
    python -X utf8 runs/20261011T214639Z-fleet05-A071-search-space-design/code/resolve_zeros.py

Saved outputs: out/pilot.json (768/768 certified), out/search.json (20736 cases, 20136 initial certifications, 600 interval-unresolved, zero certified violations), out/zero_certificates.json (600/600 exact prime-log cancellations and alternate spectra matches, no remaining cases). Original unresolved records are retained. The known AND calibration is embedded with a dummy third bit at p=(1/8,1/4,1/2); the exact spectrum is (225,7,3,21)/256 followed by four zeros. This is a calibration, not a new claim about the retired tax-free helper.

The minimum positive lower-bound case is code 4, p=(1/8,1/8,1/2), A={coordinate 2} (block mask 4). Its sign table is +1 except x=3, i.e. (x0,x1,x2)=(1,1,0). The saved lower bound is (12119843879252555703/4096)/2^60 > 0.00256647677032632 bits. Final exact zero count is 1104 and strictly positive count is 19632.

Computational runtimes: PILOT_TIME seconds pilot, SEARCH_TIME seconds full grid, ZERO_TIME seconds equality resolution. Single serial process; RAM estimate <=100 MB, not measured. Resource and batch-timeout qualifications are in SEARCH_BUDGET.md. No heavy computation, automatic dimension escalation or >300 MB job occurred.

## proof dependencies and changed downstream conclusions

The finite proof depends on the explicit Boolean tables, elementary normalized product transform, exact arithmetic and the displayed log remainder. It does not assume the universal B09 theorem. One finite claim created: A071-B09-THREEBIT-GRID-CERTIFICATE@1, pending independent review. Universal B09 status and full FEI stay open in this run; no refutation propagation is needed. The finite completeness domain and alternate transform interface are ready for A072/A073/A074; B09 can test a separately versioned sharper tax on this family.

## one next mathematical action and independent reviewer

A085/A092 should independently reconstruct the symmetry coverage and logarithm error proof, with A074 reproducing the minimum-positive case via a centered tensor transform. The next mathematical target is an explicitly versioned sharper singleton tax on the same frozen grid, as suggested by B09's section 8; no automatic n increase or finite-to-all-bias inference. The broader gap G-BIASED-TAX remains unpaid.

## actual persistence receipts or precise save blocker

All run files, code, frozen specs and outputs saved locally inside A071 only. REPORT.md, CLAIMS.json, PROGRESS.json and identical PACKET_DELTA.json follow the protocol fields. SEARCH_DOMAIN.json and SEARCH_BUDGET.md fulfill the A071 plan contract. STATUS.md, WORKLOG.md and LEARNED.md updated. out/source_receipts.json pins local source bytes; out/manifest.json records saved artifact hashes and sizes. Independent review, supervisor GitHub copy and mirror verification are pending; none is claimed. No shared indices or other agent folders were modified.
'''
report=report.replace('PILOT_TIME',f"{pilot['runtime_seconds']:.6f}").replace('SEARCH_TIME',f"{s['runtime_seconds']:.6f}").replace('ZERO_TIME',f"{z['runtime_seconds']:.6f}")
(root/'REPORT.md').write_text(report,encoding='utf-8')
sources=[]
reportdir=Path('~/mop_fei100/reports/fei-2026-10-11');supp=Path('~/mop_fei100/research_pushes/2026-10-11-full-fei-100-agents');ctx=Path('~/brain_workers/FEI100_20261011/context')
paths=[reportdir/n for n in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]+[supp/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]+[supp/'sources'/n for n in ['BLOCK_RESTRICTION_IDENTITY_2026-09-18.md','ONE_BIT_ENDPOINT.md','ROUTE_MAP_CURATED.md']]+list(ctx.glob('*.txt'))+[Path('~/brain_workers/FEI100_20261011/BOARD.md')]
paths+=list((reportdir/'runs').rglob('REPORT.md'))
for p in paths:
    b=p.read_bytes();sources.append({'path':str(p),'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)})
write('out/source_receipts.json',sources)
(agent/'STATUS.md').write_text('STATE: A071 B15 packet complete locally: frozen search family; all 20736 biased-block cases certified, no violation; finite claim unreviewed; full FEI OPEN; B15 lead notes absent.\nNEXT: A085/A092 audit coverage/log bounds; A074 reproduce minimum-positive witness; B09 version a sharper singleton tax on this grid.\n',encoding='utf-8')
with (agent/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(f"\n{datetime.now(timezone.utc).isoformat()}: Pilot 768 cases in {pilot['runtime_seconds']:.6f}s; full grid 20736 in {s['runtime_seconds']:.6f}s. Certified 20136 by rational intervals; all 600 remaining exact zeros resolved by prime-log cancellation in {z['runtime_seconds']:.6f}s, with second centered-transform parent spectra matches. Saved finite certificate and symmetry/resource handoff. Independent review and supervisor mirror pending; FEI open.\n")
(agent/'LEARNED.md').write_text('''# Durable facts from A071 stage 1

- B09-BIASED-BLOCK-UNCERTAINTY@1 can be attacked with exact rational squared spectra at rational biases even though individual normalized coefficients contain square roots. Weighted integer centered moments cancel those square roots on squaring.
- All three-bit Boolean tables on p_i in {1/8,1/4,1/2,3/4,7/8}, all proper physical blocks, satisfy the B09 tax inequality in this local exact certificate, pending independent review. Raw cases 192000; covering representatives 20736. Output complement and paired input/bias flips suffice; parity multiplication is unsafe at nonuniform biases.
- Initial separate entropy intervals left 600 equality cases unresolved. Exact rational prime-log coefficient cancellation resolved every case without increasing precision. Including initial zeros, final equality count is 1104.
- Dividing negative logarithm intervals by an ln2 interval must account for all four corners. Atanh range reduction permits short exact interval evaluation. Floating approximations in output are display only.
- The finite grid does not prove all-bias or all-dimensional inequalities; it supplies a complete bounded falsification domain and an exact finite certificate. B15 lead notes were absent at stage start.
''',encoding='utf-8')
manifest=[]
for p in sorted(root.rglob('*')):
    if p.is_file() and p.name!='manifest.json' and '__pycache__' not in str(p):
        b=p.read_bytes();assert len(b)<20_000_000
        manifest.append({'path':str(p.relative_to(root)),'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)})
write('out/manifest.json',manifest)
print(json.dumps({'saved_files':len(manifest),'certified_cases':20736,'final_exact_zero':1104,'full_fei':'OPEN'},indent=2))
