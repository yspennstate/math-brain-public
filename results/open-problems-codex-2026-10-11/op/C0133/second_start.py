from pathlib import Path
p=Path('SECOND_ATTEMPT.md');p.write_text('''# C0133 second serious attempt — 2026-10-12

Target gap: for arbitrary IID elliptic cookie stacks in d>=2, prove that the consumed projected drift D_n is o(n) on paths returning infinitely often to some finite ball, or construct a genuine IID/EL counterexample.

## Two approaches not used in the first attempt

A. Discovery-order sampling and outstanding drift reservoirs. Reveal an entire stack only on the site's first arrival. IID suggests that stacks listed in discovery order can be sampled from an IID sequence even though the visited labels are adaptive. With an integrable absolute stack budget B(x), try to prove sum over discovered sites B(x) = E[B] times range + o(n). For signed total drift delta(x), decompose D_n into total drift on discovered stacks minus the unconsumed remainder. This may sharpen the remaining gap to outstanding cookie mass. The obstacle is that eventual consumption at each fixed recurrent site need not imply sublinear outstanding mass at moving frontiers.

B. Exchangeability within a stack and de Finetti's theorem. If each site's infinite sequence of cookie probability vectors is exchangeable in visit index, represent it as conditionally IID given a directing random measure. Average that measure to a single nearest-neighbor transition vector q_x. Conditional on the directing measures, the walk may have exactly the law of an IID elliptic Markovian random environment. Then Zerner's 2002 non-ballistic LLN on the non-transient event might answer C0133 in this genuinely larger special case. The representation, independence across sites, strict ellipticity of q_x, event transfer, and exact statement of Zerner's theorem must all be checked.

Selected approach: B. It directly removes memory for a testable class of infinitely many signed cookies. A will be checked as a supplementary reduction if time permits. Neither assumption is claimed for arbitrary IID stacks in the original problem.

Brain query on the gap: math_recall.py "excited random walk recurrent sublinear range bounded cookie stacks drift budget". It returned the earlier unproved exponential-excursion attempt and neighbouring recurrence questions; these are hints only. No new valid theorem closes the gap from that query.
''',encoding='utf8');print('two approaches saved')
import json
for x in json.loads(Path('crossref.json').read_text())['message']['items']:
 if x['DOI'].lower()=='10.1214/ecp.v7-1060':print(json.dumps({k:x.get(k) for k in ['title','DOI','link','URL']},indent=2))
