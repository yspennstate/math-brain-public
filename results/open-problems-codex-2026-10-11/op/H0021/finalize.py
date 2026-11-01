import pathlib,json
p=pathlib.Path('ATTEMPT.md');s=p.read_text(encoding='utf-8-sig');s+='''

### Executed verification results
- experiment.py finished its computations in 0.42 seconds. It enumerated all 1,024 labeled five-vertex graphs. Among them 633 contain a spanning path and 561 are universal for the two subcubic tree types; the difference is 72 (60 four-edge hosts and 12 five-edge hosts). The full edge-count arrays are in experiment_results.json.
- independent_check.py decoded all 5^3 Prüfer words by a separate leaf-removal algorithm, obtaining all 120 labeled maximum-degree-3 trees, then recovered the same universality counts. This checks completeness of the tree-family enumeration independently of NetworkX's nonisomorphic-tree generator.
- At p=0.23, exact weighted enumeration verifies both the isolation variance formula and the fixed-reservoir binomial mean/variance to error below 10^{-10}.
- Nine sparse random trials used c=1.5, k=2, and n=500, 2000, 8000. Six had minimum degree ≥2; all six passed the outside-neighbor and cardinality checks. Three lacked the minimum-degree premise and were skipped, not counted as successes. Initial reservoir sizes are roughly 2–2.5 times the limiting leading-order size at these finite n. This illustrates slow convergence; no finite-size sharpness conclusion is drawn.
- The auxiliary logarithmic-scale calculation is numerical evidence only: the lower-bound entropy/error ratio is not small at the first tested scales and is nonmonotone there. Its eventual convergence to zero follows from the proved analytic limit (log L)^2/L^δ→0, not from those finite values.
- Reservoir.lean was checked with `lake env lean ~/brain_workers/TRIO_1011/op/H0021/Reservoir.lean` from ~/lean_verify. Final exit code 0; printed axioms [propext, Classical.choice, Quot.sound], with no sorryAx. Only Mathlib.Algebra.Order.BigOperators.Group.Finset is imported. The first two runs failed (UTF-8 BOM and a missing order import); these were corrected before the successful check. The final proof uses standard finite-set and sum inequalities, no decision procedure and no native_decide. The probability theorem itself is not Lean formalized.

## 7. Final disposition
STATE: DONE, VERDICT: PARTIAL. The original problem is unresolved by this attempt. The full source statement was confirmed and no source-matching literature solution was found; two literature services remained inaccessible. The precise future research obligation is to construct and prove a uniform, vertex-disjoint spanning-completion method at coefficient 1+ε, already for subcubic trees. The results here identify and certify the adaptive reservoir scale but do not supply that method.
''';p.write_text(s,encoding='utf8')
p=pathlib.Path('CLAIMS.jsonl');a=[json.loads(x) for x in p.read_text(encoding='utf8').splitlines()]
for x in a:
 if 'minimum k-neighbor reservoir' in x['claim']:
  x['checks']=x['checks'].replace('Finite cardinality Lean verification pending.','Finite cardinality checked in Lean: exit 0, no sorryAx; lean_check.txt. Probability argument is not formalized.')
 if 'exactly 72' in x['claim']:x['checks']+=' Independently regenerated all 120 labeled subcubic trees via Prüfer codes and matched the host counts.'
p.write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in a),encoding='utf8')
p=pathlib.Path('LITERATURE.md');s=p.read_text(encoding='utf8');s+='\nGitHub returned total_count=0 for the recorded repository query. The unfiltered Crossref search and the exact/date-filtered query returned no exact matching theorem in their selected result windows. Literature coverage is limited as described above.\n';p.write_text(s,encoding='utf8')
pathlib.Path('STATUS.md').write_text('''STATE: DONE
NEXT: Prove a uniform disjoint spanning-completion theorem at p=(1+ε)log n/n, already for Δ=3; this step remains unresolved.
VERDICT: PARTIAL
2026-10-12: Source statement verified: arXiv:2608.06358v1, Conjecture 1.4, page 7. All requested search services attempted; OpenAlex and Semantic Scholar returned HTTP 429. No matching solution found in successful searches.
2026-10-12: Confirmed Δ=2 via a directly fetched Hamilton-cycle theorem; proved isolation lower bound and adaptive k-neighbor reservoir asymptotic size with fixed-reservoir failure on that scale. No novelty claim.
2026-10-12: Full proofs and hostile-referee gap audit saved in ATTEMPT.md. Exact n=5 enumeration independently checked through Prüfer codes; moments checked; six eligible random repair trials passed.
2026-10-12: Reservoir cardinality lemma passed Lean kernel checking (exit 0, no sorryAx). The probabilistic theorem is not formalized. Full conjecture remains unproved; attempt closed as partial.
''',encoding='utf8')
assert pathlib.Path('STATUS.md').read_bytes().startswith(b'STATE: DONE\n')
assert len(a)==7 and all(x['status'] in ['proved','counterexample','proved_special_case','numerical_evidence','conjecture'] for x in a)
assert 'exit_code=0' in pathlib.Path('lean_check.txt').read_text(encoding='utf8')
assert 'sorryAx' not in pathlib.Path('lean_check.txt').read_text(encoding='utf8')
print('Final record checks passed.');print(pathlib.Path('STATUS.md').read_text(encoding='utf8'));print(pathlib.Path('lean_check.txt').read_text(encoding='utf8'))
