from pathlib import Path
import json
p=Path('LITERATURE.md');s=p.read_text(encoding='utf8')
s+='\n## Additional exact references from arXiv screening\n\n- Shayan Hundrieser, Marcel Klatt, Thomas Staudt, Axel Munk. *A Unifying Approach to Distributional Limits for Empirical Optimal Transport*. arXiv:2202.12790v1, 25 February 2022. https://arxiv.org/abs/2202.12790. Limit laws for the cost functional via dual empirical processes, not identification of nonunique primal plan selection.\n- Johan Segers. *Graphical and uniform consistency of estimated optimal transport plans*. arXiv:2208.02508v1, 4 August 2022. https://arxiv.org/abs/2208.02508. Abstract explicitly discusses squared Euclidean cost, so it cannot be substituted for the non-strict Euclidean distance model here.\n\nFull titles, authors, timestamps and abstracts from all three arXiv API searches are saved in arxiv_screening.json. Publication/submission dates can differ from dates printed inside downloaded PDFs; those differences are retained in the raw records. No exact solving theorem was found in the inspected material.\n'
p.write_text(s,encoding='utf8')
Path('STATUS.md').write_text('''STATE: DONE
NEXT: Derive a selection theorem for the horizontal conditional kernel from unrestricted empirical Euclidean assignments; leading local cost terms are degenerate.
VERDICT: PARTIAL
2026-10-12: Confirmed arXiv:2505.19104v2, revised 13 July 2026, Problem 4 on PDF page 30; source specifies no convergence mode. Checked source context and all requested literature services. No exact solution located; OpenAlex remained rate-limited, so its citing-works search could not be completed. Semantic Scholar citing-paper search succeeded.
2026-10-12: Read brain/topic/mistake recalls, supplied mathematical attempt, intake ledgers, and origin/master P0336 research records without changing repositories. Prior reductions were treated as leads and rechecked.
2026-10-12: Proved complete population characterization, a.s. subsequential vertical-support conclusion, and sharp-in-order expected rates for the ACTUAL empirical optimizer: with C=sqrt(10)+3 and L=log(27/16), 1/[3C(n+1)] <= E excess <= L/[6(n+1)], and 1/[3(n+1)] <= E vertical quadratic displacement <= CL/[6(n+1)].
2026-10-12: Proved height-rank surrogate converges a.s. to conditionally independent horizontals; exhibited a positive-probability two-point Euclidean counterexample to exact height sorting. Rechecked local quadratic/common-slope degeneracy and derived exact fourth-moment/remainder bounds for the rank competitor.
2026-10-12: Completed 36 independent numerical assignments through n=5000, plus exhaustive checks of 5912 small permutations. Small positive horizontal bias means product-limit evidence remains inconclusive. Each numerical job stayed below 1 GB and lasted seconds.
2026-10-12: Lean kernel checked three algebraic/finite theorems, exit 0; no sorry or native_decide. Probabilistic proofs remain written proofs. All claims and precise unresolved selection gap are recorded. DONE means this attempt is finished, not that Problem 4 is solved.
''',encoding='utf8')
rows=[json.loads(s) for s in Path('CLAIMS.jsonl').read_text(encoding='utf8').splitlines()]
assert len(rows)==8
assert Path('STATUS.md').read_bytes().startswith(b'STATE: DONE\n')
for file in ['ATTEMPT.md','LITERATURE.md','CLAIMS.jsonl']:
 assert Path(file).stat().st_size>0
lean=Path('P0336Checks.lean').read_text(encoding='utf8')
assert 'sorry' not in lean and 'native_decide' not in lean
assert Path('lean_check.txt').read_text(encoding='utf8').startswith('Exit code: 0')
print('Final artifact validation passed. STATE: DONE; VERDICT: PARTIAL; 8 claims.')
