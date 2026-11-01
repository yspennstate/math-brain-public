from pathlib import Path
p=Path('SECOND_ATTEMPT.md')
p.write_text('''# G0006 — second serious attempt (2026-10-11)

The previous remaining gap is an upper bound on infected spatial connectivity at a rate strictly above lambda_c. No such bound follows from marginal density or stationary pairs.

Two approaches not pursued in the first attempt:

A. Finite-volume stationary laws with permanently infected exterior, and block annulus crossing events. Dominate the infinite-volume law locally by these finite-state laws, color enlarged blocks using a fixed number of colors, and derive a computable renormalization certificate from a finite stationary crossing probability. Unlike the earlier singleton exit criterion, the independence penalty is fixed as the block size grows. Pursue this first: it preserves actual spatial connectivity and permits a concrete finite-state calculation.

B. A cluster-weight stationarity identity. Replace the one-site observable by the reciprocal finite occupied-cluster size, or a truncated cluster generating function. A birth can merge finite components or attach them to an infinite one, while a death can split a component. A mass-transport rewrite might control the density of infinite components directly and avoid averaging infinite vertices together with isolated sites. The obstacle to check is that truncation errors and pivotal split/merge terms depend on multi-point connectivity, not only density. This is a distinct dynamic reduction, not a product comparison.

Chosen approach: A. It gives a finite and explicitly testable certificate and does not presuppose near-critical mixing. No success is claimed yet.
''',encoding='utf8')
