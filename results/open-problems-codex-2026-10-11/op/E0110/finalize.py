from pathlib import Path
import json,xml.etree.ElementTree as E
with Path('LITERATURE.md').open('a',encoding='utf8') as f:
 f.write('''

## Relevant subsequent and surrounding references

- Sayan Banerjee and Amarjit Budhiraja, Parameter and dimension dependence of convergence rates to stationarity for Reflecting Brownian Motions, arXiv:1902.04501v2 (2019; subsequent publication in Annals of Applied Probability, 2020). The inspected abstract gives L1-Wasserstein rates for hard-reflected orthant RBM, including O((log d)^2) relaxation for the Blanchet–Chen class and O(d^6(log d)^2) for the Atlas model. These are not the soft GRBM or the requested TV bound.
- Sayan Banerjee and Brendan Brown, Dimension-free local convergence and perturbations for reflected Brownian motions, arXiv:2009.12937v3. The inspected abstract gives dimension-independent stretched-exponential local convergence and polynomial perturbation results for hard RBM. Local convergence does not settle joint-TV Conjecture 1.5.
- Jose Blanchet and Xinyun Chen, Rates of Convergence to Stationarity for Reflected Brownian Motion, Mathematics of Operations Research 45 (2020), 660–681, DOI 10.1287/moor.2019.1006; preprint arXiv:1601.04111. Hard-reflection coupling results, referenced by the source, not a solution for soft GRBM.
- Peter W. Glynn and Rob J. Wang, On the rate of convergence to equilibrium for reflected Brownian motion, Queueing Systems 89 (2018), 165–197, DOI 10.1007/s11134-018-9574-1. Earlier hard-reflection work; its existence does not supply a subsequent solution of the source conjecture.
- Milton Jara and Gregorio R. Moreno Flores, Stationary Directed Polymers and Energy Solutions of the Burgers Equation, arXiv:1908.06591v1 (16 August 2019). PDF fetched and inspected: intermediate-disorder convergence of stationary O'Connell–Yor increments to stochastic Burgers energy solutions. Its abstract explicitly says it avoids spectral-gap estimates. This is a scaling limit, not the requested finite-dimensional relaxation theorem.

The broader arXiv queries also returned polymer free-energy fluctuation/scaling papers, including arXiv:2307.01172, 2511.11207, 2505.05685, 2401.10130, 2008.07241, 1809.09869, 1204.1024 and 1312.2600. Their inspected abstracts concern integrability, large deviations, Airy/KPZ scaling, or boundary perturbations, and make no claim to solve the general GRBM relaxation conjecture. Query result XML files preserve exact metadata.

## Final bounded-search assessment (2026-10-11)

No inspected paper settles Conjecture 1.5. This is not a definitive assertion that the literature has no solution.
OpenAlex exact source metadata finally succeeded using /works/doi:10.1007/s11134-019-09610-5, identifying W2935248447 and reporting cited_by_count=1. Both subsequent searches filter=cites:W2935248447 returned HTTP 429, so the OpenAlex citation graph could not be inspected. Semantic Scholar's DOI citation endpoint succeeded and returned three unrelated citing works. All failures, retries and exact query URLs are recorded above. No built-in web search or image tool was used.
''')
status='''STATE: DONE
NEXT: Extend the weighted invariant-measure/Poincare method beyond Gamma=(R+R^T)/2 and U=-exp(-x), especially to Gamma=I; the full conjecture remains unresolved.
VERDICT: PARTIAL

2026-10-11: Retrieved arXiv:1806.03755v2 and verified Theorem 1.3 / Assumption 1.2 / Conjecture 1.5 exactly. Queried arXiv, OpenAlex (including citing-works attempts), Crossref, Semantic Scholar and GitHub; no solution identified in inspected literature. OpenAlex citing-works endpoints were rate-limited, so literature status is not definitive.
2026-10-11: Read brain recalls, intake records and origin/master E0110 prior attempt without modifying those stores. Prior frozen-rate / marginal-TV evidence does not prove the conjecture.
2026-10-11: Proved the requested TV rate for the product-form subclass U=-exp(-x), Gamma=(R+R^T)/2, and mu_i<=-m<0: exponent min(m/16,m^2/4)/d, sharpened to m/(4d) for m>=1. Full proof and exact remaining gap in ATTEMPT.md.
2026-10-11: Checked weighted covariance eigenvalues through d=1024 and Morse factorization numerically, refined discretization at a=6,20, and obtained five successful Lean algebraic checks (exit 0; no sorry/native_decide). Formal verification does not cover analytic/probabilistic steps.
2026-10-11: Finished this attempt with a proved special case and a precisely recorded gap; no full proof or counterexample claimed.
'''
Path('STATUS.md').write_text(status,encoding='utf8')
claims=[json.loads(s) for s in Path('CLAIMS.jsonl').read_text(encoding='utf8').splitlines()]
assert len(claims)==5
assert Path('STATUS.md').read_bytes().startswith(b'STATE: DONE\n')
assert 'exit=0' in Path('lean_check.txt').read_text(encoding='utf8')
assert 'sorry' not in Path('SpecialCase.lean').read_text(encoding='utf8')
assert 'native_decide' not in Path('SpecialCase.lean').read_text(encoding='utf8')
print('Final records verified:',[p.name for p in Path.cwd().iterdir() if p.name in ['STATUS.md','LITERATURE.md','ATTEMPT.md','CLAIMS.jsonl','SpecialCase.lean','lean_check.txt']])
