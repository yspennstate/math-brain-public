"""Record the analytic tensor extension; no additional search or precision refinement."""
import hashlib
import json
from pathlib import Path

run = Path(__file__).resolve().parents[1]
agent = run.parents[1]

def read(path):
    return path.read_text(encoding='utf-8')

def write(path, value):
    path.write_text(value, encoding='utf-8')

def dump(path, value):
    write(path, json.dumps(value, indent=2, ensure_ascii=False) + '\n')

assert 8**4 == 4096 < 4802 == 2*7**4
certificate = {
    'comparison': '8^4 < 2*7^4', 'left': 4096, 'right': 4802,
    'integer_margin': 706, 'conclusion': 'log2(8/7)<1/4',
    'precision_refinement': 'NONE; integer sign determined',
    'family': 'All finite disjoint products of Boolean factors on at most three coordinates',
    'input_certificate': 'MAIN_CHECK.json: all256 three-bit tables satisfy S4(g)>=1-|E g|',
    'identities': ['S4(product g_j)=sum S4(g_j)', '|E product g_j|=product |E g_j|',
                   'sum(1-a_j)>=1-product a_j for 0<=a_j<=1',
                   'Var(h)<=2(1-|E h|)', 'D(p_h||r_h^(1/8))<=Var(h)log2(8/7)<=S4(h)/2'],
    'scope': 'New initial WHOLE-core supplier; no free conversion from a product reference; hereditary under physical restrictions'
}
dump(run/'out/TENSOR_SUPPLIER_BRIDGE.json', certificate)

extension = '''## 6a. Unbounded-dimensional disjoint tensor application

Let h be any finite product of Boolean factors g_j on disjoint blocks, each block using at most three coordinates. The exhaustive certificate in section6 gives S4(g_j)>=1-|E g_j| for every factor and every restriction of every factor. Fourier entropy and total influence add under disjoint Boolean products, while means multiply. Put a_j=|E g_j| in[0,1]. Induction from (1-a)+(1-b)>=(1-ab) gives

    S4(h)=sum_j S4(g_j)>=sum_j(1-a_j)>=1-product_j a_j=1-|E h|.

Every physical restriction stays in this same family, so this is a hereditary entropy eligibility certificate, with no bound on the total number of variables or factors.

Supply the NEW initial WHOLE-essential-core reference q=r_h^(1/8). This is not a free conversion from any pre-existing tensor reference. The exact integer comparison8^4=4096<4802=2*7^4, margin706, proves log2(8/7)<1/4. Since Var(h)=(1-|E h|)(1+|E h|)<=2(1-|E h|), equation(1) gives

    D(p_h||q)<=Var(h)log2(8/7)<= (1-|E h|)/2<=S4(h)/2,
    CE(p_h,q)=H(h)+D(p_h||q)<=4I(h)-S4(h)/2<=4I(h).

Constants and characters retain their exact laws. Thus BOTH supplier and hereditary frontier hypotheses of the eight-generation theorem are closed for this unbounded-dimensional family. Use the single ORIGINAL Var(h) gross budget of section4, not a sum of factor variances. The same >=3/4 remaining reserve applies after the old quarter for all allowed histories with at most eight reset generations. This extension is a proof from the finite factor certificates and exact product identities, not extrapolation from enumerated trajectories. It neither supplies a certificate for arbitrary Boolean cores nor proves unlimited nonpoint refreshes.

'''
proof_path = run/'PROOF.md'
proof = read(proof_path)
assert '## 6a.' not in proof
proof = proof.replace('## 7. Exact computational domain and precision', extension+'## 7. Exact computational domain and precision')
write(proof_path, proof)

claim_path = run/'CLAIMS.json'
claims = json.loads(read(claim_path))
claim = claims[0]
claim['exact_statement'] += ' Analytic tensor corollary: both hypotheses are closed unconditionally for every finite disjoint product of at-most-three-variable Boolean factors, with the NEW initial WHOLE-core1/8 reference. Additivity gives S4(h)>=1-|E h|; 8^4<2*7^4 certifies D(p_h||q)<=S4(h)/2. All restrictions remain in the family, so this application has unbounded total dimension.'
claim['statement_sha256'] = hashlib.sha256(claim['exact_statement'].encode('utf-8')).hexdigest()
claim['hypotheses'].append('Unconditional tensor corollary uses disjoint factors of at most3variables and the specified NEW whole-core1/8 initial supplier; arbitrary core remains conditional')
claim['proof_source'].append('out\\TENSOR_SUPPLIER_BRIDGE.json')
claim['status'] = 'CONDITIONAL_GENERAL_THEOREM_UNBOUNDED_TENSOR_APPLICATION_CLOSED_REVIEW_PENDING'
dump(claim_path, claims)

progress_path = run/'PROGRESS.json'
progress = json.loads(read(progress_path))
progress['mathematical_delta'] += ' Analytically closed BOTH initial whole-core1/8 supplier and hereditary entropy eligibility for arbitrary finite disjoint tensors of at-most3bit factors, hence unbounded total dimension: S4(h)>=1-|E h| and D<=S4(h)/2; exact initial-supplier logarithm integer margin706. No additional search.'
progress['mathematical_status'] = 'CONDITIONAL_GENERAL_THEOREM_UNBOUNDED_TENSOR_APPLICATION_CLOSED_REVIEW_PENDING_FULL_FEI_OPEN'
dump(progress_path, progress)
dump(run/'PACKET_DELTA.json', progress)

report_path = run/'REPORT.md'
report = read(report_path)
heading = 'Universal bridge'
index = report.rfind(heading)
assert index >= 0
# Preserve the report's heading syntax and replace its final paragraph.
line_start = report.rfind('\n', 0, index)+1
report = report[:line_start] + '''Tensor extension: For every finite disjoint product of Boolean factors on at most three variables, the verified factor bound implies the hereditary certificate S4(h)>=1-|E h|. The NEW whole-core1/8 initial reference costs at most S4(h)/2, using the exact integer margin706 in 8^4<2*7^4. Therefore the eight-generation payment theorem applies unconditionally to this unbounded-dimensional family. See PROOF.md section6a and out/TENSOR_SUPPLIER_BRIDGE.json. All8190 computational checks remain unchanged; this extension uses only product identities and a checked integer sign. Independent review remains pending.

Universal bridge: This stage advances C019 stopping-tree payment and C024 history transfer by paying up to EIGHT genuinely positive whole-core refresh generations from the SAME original source account, with margin at least1+2t^2 before the old quarter and at least3/4 after it. The arbitrary-core theorem is conditional; both supplier and hereditary terminal obligations are now closed for arbitrary disjoint tensors of at-most-three-variable Boolean factors, including nonpoint factors and unbounded total dimension. Arbitrary Boolean suppliers and terminal entropy eligibility remain unsupported. NEXT is independent reconstruction of the original-variance antichain factor and a genuinely positive ninth refresh priced against the actual remaining account, preserving all eight debits and both sign trees. This directly tests the universal history-payment obstruction rather than launching another isolated finite-class search.
'''
write(report_path, report)
write(agent/'STATUS.md', 'STATE: A073 stage22 saved: EIGHT whole-core positive refresh generations paid SAME4; unbounded disjoint tensors of <=3bit factors closed; 8190 checks PASS; FEI OPEN, review pending.\nNEXT: Independent review of original-variance factor1/4 and positive-witness ledger; price positive ninth refresh from actual remaining original account, all debits/both signs/old quarter retained; arbitrary supplier open.\n')
with (agent/'WORKLOG.md').open('a', encoding='utf-8') as stream:
    stream.write('\n2026-10-23 stage22 tensor amendment: Extended the eight-generation application to arbitrary disjoint products of <=3bit factors analytically. Certified factor S4>=1-|mean| tensorizes and is hereditary; NEW whole-core1/8 supplier D<=S4/2 follows from integer4096<4802 (margin706). No larger search or further logarithm refinement. Full FEI and independent review remain open.\n')
with (agent/'LEARNED.md').open('a', encoding='utf-8') as stream:
    stream.write('\n2026-10-23: If each disjoint Boolean factor and its restrictions satisfy S4(g)>=1-|Eg|, their product satisfies the same hereditary bound, since surplus adds and absolute means multiply. A NEW whole-core1/8 spike then costs D<=Var(h)log2(8/7)<=S4(h)/2, certified by8^4<2*7^4 (margin706). This closes the supplied interface for arbitrary finite tensors of <=3bit factors, but not arbitrary Boolean cores or free conversions from existing tensor references.\n')

# Preserve protocol keys exactly; independently check delta equality and statement digest.
assert json.loads(read(progress_path)) == json.loads(read(run/'PACKET_DELTA.json'))
assert len(read(agent/'STATUS.md').splitlines()) == 2
assert claim['statement_sha256'] == hashlib.sha256(claim['exact_statement'].encode('utf-8')).hexdigest()
protocol = json.loads(read(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')))
assert set(claim) == set(protocol['required_per_run']['claim_fields'])
assert set(progress) == {k.split(' (')[0] for k in protocol['required_per_run']['progress_fields']}
manifest = {str(p.relative_to(run)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(run.rglob('*')) if p.is_file() and p.name != 'MANIFEST.json'}
assert all(p.stat().st_size < 20*1024*1024 for p in run.rglob('*') if p.is_file())
dump(run/'out/MANIFEST.json', manifest)
assert all(hashlib.sha256((run/p).read_bytes()).hexdigest() == digest for p, digest in manifest.items())
print(json.dumps({'tensor_extension': 'SAVED', 'dimension': 'unbounded disjoint <=3bit factors', 'integer_margin': 706, 'FEI': 'OPEN', 'review': 'PENDING'}))
