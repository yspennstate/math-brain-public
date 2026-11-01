from pathlib import Path
import datetime
import hashlib
import json
import pymupdf

root = Path(__file__).resolve().parent
result = json.loads((root / 'lean_result.json').read_text(encoding='utf8'))
assert result['state'] in {'PASSED', 'TIMEOUT'}, 'Do not finalize a running or failed check'
assert result['source_unchanged']
source = root / 'FiniteChecks.lean'
assert hashlib.sha256(source.read_bytes()).hexdigest() == result['source_sha256']
assert source.read_bytes().isascii()
text = source.read_text(encoding='utf8')
assert 'sorry' not in text and 'native_decide' not in text
passed = result['state'] == 'PASSED'
if passed:
    assert result['exit_code'] == 0

doc = pymupdf.open(root / 'source.pdf')
(root / 'verified_source_p22.txt').write_text(doc[21].get_text(), encoding='utf8')
assert 'the average height above a site at distance L' in doc[21].get_text()

attempt = root / 'ATTEMPT.md'
s = attempt.read_text(encoding='utf8')
assert '?' not in s
s = s.replace('## Components developed below', '## Completed components')
s = s.replace('The retained verification invocation is queued through the supplied shared-slot lake wrapper, which gives actual Lean execution a 3600-second timeout.', 'The original queued tool session was unavailable on continuation and no successful completion record was found. A fresh ASCII-source verification was therefore submitted through the shared-slot lake wrapper with a 3600-second total timeout.')
s = s.replace('only finite algebra is submitted.', 'only the three finite algebra lemmas are checked.' if passed else 'only finite algebra was submitted; the fresh check timed out and is not called checked.')
verification = ('Lean completed successfully with exit code 0. The exact source hash and run metadata are in lean_result.json; output is in lean_stdout.txt and lean_check.txt. The three checked lemmas are edge_euler_cancellation, grounded_path_resistance, and gaussian_edge_monge. They verify algebra over arbitrary real inputs, the resistance inequality on a two-edge grounded path, and the Gaussian edge Monge inequality. The general convex FKG argument, energy integration, variance inequality, limiting argument, and the open problem itself are not formalized.' if passed else 'The fresh shared-slot invocation reached its 3600-second timeout. Output and metadata are retained; no successful formal verification is claimed. The finite algebra remains proved analytically, and the mathematical verdict is unchanged.')
s += '\n\n## Final referee audit and closure (2026-10-12)\n\n'
s += 'The continuation repaired an actual serialization error: PowerShell had replaced mathematical characters by question marks in the Lean file, header, edge-check paragraph, and diagnostic example. Pre-repair bytes are preserved locally. The repaired formulas were read against their derivations; no inequality direction or domain condition was changed. The Lean source now uses ASCII Real and <= syntax.\n\n'
s += verification + '\n\n'
s += 'Rechecked Proposition 1 edge-by-edge: convexity gives the ordered-pair energy inequality, FKG supplies association, and differentiating in a boundary height has the positive covariance sign stated. Domain enlargement thus gives a lower comparison, not an upper bound. Rechecked Proposition 2 directly against source PDF p.22 (text saved in verified_source_p22.txt): the full-box uniformly convex result is explicitly asserted there. Its use here is an external theorem dependency, not a proof reproduced from the primary Deuschel-Giacomin paper. The lower bound passes to any proper weak limit by comparison of bounded truncations, rather than by an unjustified passage of first moments.\n\n'
s += 'Rechecked the orthant Euler identity: the phi_v factor cancels the boundary term at zero. Rechecked the local derivative bound for all s,b>=0, the likelihood-ratio covariance formula, and the positive truncated-Gaussian integral. Rechecked the soft-wall approximation: its convex penalty leaves the grounded Hessian lower bound intact, and full-space Gaussian domination passes first and second moments to the orthant. The variance is centered and alone gives no mean bound. The path argument transfers a bound at one neighbor to all fixed sites; product tightness, monotone uniqueness and second-moment uniform integrability then give a proper Gibbs limit. Conversely, unbounded monotone means plus bounded variance force escape at that neighbor. The deterministic diagnostic violates the Gibbs specification and is explicitly not a counterexample to F0073.\n\n'
s += 'Final verdict: PARTIAL. No exact printed resolution was found in the recorded bounded search, and no full proof or counterexample is claimed. The remaining gap is estimate A (uniform neighboring mean bound) and a spatial upper bound C(V) log(2+|i|), uniform in the outer box size. The finite-volume lower comparison and the one-site existence reduction do not fill that gap. This closes the present attempt.\n'
attempt.write_text(s, encoding='utf8')

claims_path = root / 'CLAIMS.jsonl'
claims = [json.loads(line) for line in claims_path.read_text(encoding='utf8').splitlines()]
for c in claims:
    if c['claim'].startswith('Finite-volume E phi_i'):
        c['checks'] = ('Grounded Laplacian Cauchy-Schwarz proof re-refereed; the two-edge grounded path inequality was Lean kernel checked with exit 0. The general probabilistic resistance bound is proved analytically, not formally.' if passed else 'Grounded Laplacian Cauchy-Schwarz proof re-refereed. Fresh finite-algebra Lean invocation timed out; no successful formal check claimed.')
    if c['claim'].startswith('Nonnegative boundary heights'):
        c['checks'] += ' Continuation: convex edge integral and interpolation covariance signs rechecked.'
    if c['claim'].startswith('The positive pinned box exhaustion'):
        c['checks'] += ' Continuation: tightness versus mean bound, coordinate uniform integrability and Gibbs-kernel continuity rechecked.'
if passed:
    claims.append({'problem_id':'F0073',
        'claim':'The real algebra lemmas edge_euler_cancellation, grounded_path_resistance and gaussian_edge_monge are accepted by Lean 4 with targeted Mathlib imports.',
        'status':'proved', 'proof_location':'FiniteChecks.lean; lean_result.json; lean_check.txt',
        'remaining_gap':'Only these algebraic lemmas are formalized. No probabilistic theorem or solution of F0073 is claimed checked in Lean.',
        'checks':'Exit code 0; source SHA256 '+result['source_sha256']+'; unchanged source; no sorry or native_decide.'})
with claims_path.open('w',encoding='utf8') as out:
    for c in claims:
        assert c['problem_id'] == 'F0073'
        assert c['status'] in {'proved','counterexample','proved_special_case','numerical_evidence','conjecture'}
        assert set(c) == {'problem_id','claim','status','proof_location','remaining_gap','checks'}
        out.write(json.dumps(c,ensure_ascii=False)+'\n')

with (root / 'LITERATURE.md').open('a',encoding='utf8') as out:
    out.write('\n2026-10-12 final audit: re-read downloaded Velenik source PDF p.22 (printed 133), which explicitly states the full-box two-dimensional convex-interaction entropic-repulsion result and logarithmic average height. Exact extraction saved in verified_source_p22.txt. This confirms the dependency of our lower comparison; it is not a new literature resolution. No further web search was run during closure.\n')

status = 'STATE: DONE\nNEXT: To advance F0073, prove sup_N E_(mu_N^+) phi_(1,0) < infinity and then a logarithmic spatial upper bound uniform in N.\nVERDICT: PARTIAL\n\n'
status += '2026-10-12: Source hypotheses and bounded literature search recorded. No exact resolution found; rate limits and primary-source access limits are documented.\n'
status += '2026-10-12: Proved finite-volume comparisons and energy/resistance bounds, a local mean inequality, and the equivalence of proper exhaustion convergence with a uniform mean bound at one neighbor. Logarithmic lower bound uses the verified existing full-box theorem. Corrected the earlier intake upper-bound limiting error.\n'
status += '2026-10-12: Continuation repaired encoding substitutions, saved pre-repair records, and re-refereed every recorded argument. '+('Three finite algebra lemmas passed Lean; result and unchanged source hash saved.' if passed else 'Fresh hour-timeout Lean invocation timed out; no formal success claimed.')+'\n'
status += '2026-10-12: Attempt closed with PARTIAL verdict. Infinite-volume existence for general V and the uniform logarithmic upper bound are not proved here. Exact remaining gap is in ATTEMPT.md.\n'
(root / 'STATUS.md').write_text(status,encoding='utf8')
audit = {'state':'DONE','verdict':'PARTIAL','claims':len(claims),'lean_state':result['state'],
         'checked_source_sha256':result['source_sha256'],
         'finalized_local':datetime.datetime.now().isoformat(timespec='seconds'),
         'remaining_gap':'Uniform one-neighbor mean bound and volume-uniform logarithmic spatial upper bound.'}
(root / 'final_audit.json').write_text(json.dumps(audit,indent=2),encoding='utf8')
print(json.dumps(audit,indent=2),flush=True)
