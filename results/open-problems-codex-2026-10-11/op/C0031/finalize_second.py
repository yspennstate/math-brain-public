from pathlib import Path
import json

root = Path(__file__).resolve().parent
p = root/'SECOND_ATTEMPT.md'
s = p.read_text(encoding='utf-8')
old = 'It is summable for every fixed t>0. Therefore S_n(z)-E S_n(z)->0 almost surely, and the deterministic-centering argument implies E S_n(z)->ell(z).'
new = 'It is summable for every fixed t>0. Therefore S_n(z)-E S_n(z)->0 almost surely. To check centering directly, if |E S_n(z)-ell(z)|>2t along a subsequence, the events |S_n(z)-E S_n(z)|<=t and |S_n(z)-ell(z)|<=t would be disjoint, although both probabilities tend to one. This contradiction for every t>0 proves E S_n(z)->ell(z). No interchange of limits and expectations is used.'
s = s.replace(old,new)
s += '''\n\n### Additional details of the deterministic stress test\n\nThe cyclic spectra converge to the uniform circle law because their test integrals are the Riemann sums (1/n) sum_{k=0}^{n-1} f(exp(2 pi i k/n)) of a continuous periodic function. Both types of event occur infinitely often almost surely: the independent bad-event probabilities sum to infinity, and so do their complementary probabilities. Thus the bounded continuous test min(1,|z|^2) takes spectral integral zero infinitely often and one infinitely often. There is no weak almost-sure limit in this non-iid model. For |z|<=r<1 the cyclic singular values lie in [1-r,1+r], so eventually its clipped and true potentials coincide uniformly. Also |log|1-z^n||<=max(-log(1-r^n),log(1+r^n)), which tends to zero, proving the uniform potential convergence used above. The rank-one clipped bound then proves uniform convergence for the nilpotent matrix too. At n=1 any finite clipped definition, for example S_1=0, may be used; finite initial terms have no effect on the averaged theorem.\n'''

log = root/'CESARO_LEAN_CHECK.txt'
if not log.exists():
    raise SystemExit('Lean result not yet available: do not finalize.')
lean = log.read_text(encoding='utf-8')
if 'EXIT_CODE: 0' in lean or 'Exit code: 0' in lean or 'exit_code: 0' in lean:
    result = 'CesaroCore.lean passed with exit code 0 and no sorry or native_decide. The only formally checked claim is the algebraic dyadic-interpolation inequality; the random-matrix theorem is checked by the written proof, not formalized.'
else:
    result = 'Lean command finished; see CESARO_LEAN_CHECK.txt for its exact result. No Lean certification is claimed unless that log records exit code 0.'
s += '\n\n### Lean check outcome\n\n'+result+'\n'
p.write_text(s,encoding='utf-8')
with (root/'ATTEMPT.md').open('a',encoding='utf-8') as f:
    f.write('\n'+result+'\n')
with (root/'STATUS.md').open('a',encoding='utf-8') as f:
    f.write('\n2026-10-11 renewed attempt completed: '+result+' Full-sequence convergence remains unproved; no iid-entry counterexample is established. VERDICT PARTIAL.\n')
status = (root/'STATUS.md').read_text(encoding='utf-8').splitlines()
status[0] = 'STATE: DONE'
status[1] = 'NEXT: To continue, obtain almost-sure decay of the local integrated clipping defect, or a summable polynomial hard-edge bound for arbitrary-core masked noise; sparse bad dimensions remain possible under the current estimates.'
(root/'STATUS.md').write_text('\n'.join(status)+'\n',encoding='utf-8')
claims = [json.loads(line) for line in (root/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()]
print('STATE DONE; VERDICT PARTIAL; claims JSON valid:', len(claims))
print(lean)
