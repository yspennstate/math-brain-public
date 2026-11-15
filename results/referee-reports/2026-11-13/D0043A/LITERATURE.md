# Literature search and exact locators

Search date: 13 November 2026. Primary sources were consulted throughout. Secondary search snippets were used only to discover primary papers, notably Baslingker; conclusions below are based on the primary texts. PDFs were converted in memory and discarded; only text is retained. The source manifest records URLs, byte hashes of the unretained PDF streams, text hashes and page counts. Page numbers below count PDF pages, not guessed journal pagination. Several arXiv PDFs have a regenerated date on their title page; the URL and hash identify the text actually inspected.

## Decisive result

Jnaneshwar Baslingker, *Stochastic domination in beta ensembles*, [arXiv:2304.09236v2](https://arxiv.org/abs/2304.09236v2), 22 December 2024 (first submitted 18 April 2023), **Theorem 4, PDF p. 7**: the KRV conjecture fails for β=2, k=1. The definition and precise connection to the conjectured operator are on pp.6–7; the proof is Section3, pp.10–12. Equation(22), p.12, gives the Gaussian variational lower-tail exponent (4k+3)/(4k+2). Equation(16), p.11, records the incompatible critical-unitary right-tail bound at k=1.

Published as *Journal of Mathematical Physics* **66**, 053303 (2025), [DOI10.1063/5.0254593](https://doi.org/10.1063/5.0254593). The [publisher page](https://pubs.aip.org/aip/jmp/article/66/5/053303/3346682/Stochastic-domination-in-beta-ensembles) explicitly confirms the negative result and is dated12May2025. Its readable abstract/reference page is saved as `baslingker_published_web.txt`. The journal PDF returned403, so the theorem number and exact pages cited here refer explicitly to arXiv v2. We do not claim to have checked the journal's internal pagination or theorem renumbering.

This is a negative literature resolution, so REPORT.md begins COUNTEREXAMPLE. The user's early-stop instruction for a theorem *proving* the conjecture for k≥1 is not triggered. There is no claim of a new refutation.

## Other primary sources checked

| Source | Exact location checked | Scope and implication |
|---|---|---|
| Virág, [1804.06953](https://arxiv.org/abs/1804.06953) | Conjecture5, p.14; Theorems5.1 p.6 and8.1 in Section8 | Exact requested statement; half-line Airy limit and context of polynomial-potential tridiagonal matrices. |
| Krishnapur–Rider–Virág, [1306.4832](https://arxiv.org/abs/1306.4832), CPAM69(2016),145–199 | Theorem1 p.3; entry density eq.(8) p.8; local minimizers eqs.(10)–(14) p.9; Assumptions1–2 and Theorem9 pp.13–15; Proposition41 eq.(68) p.49; Section13 pp.55–57, Conjecture45 p.57 | Proves uniformly convex regular potentials, not critical k≥1. Conjecture45 is the arXiv numbering; Baslingker refers to the published numbering Conjecture13.1. |
| Ramírez–Rider–Virág, [math/0607331](https://arxiv.org/abs/math/0607331) | Theorem5.1 p.21; Assumptions1–2 pp.20–21 | General tridiagonal convergence criterion. The saved preprint uses this numbering; do not substitute a theorem number from a different printing. |
| Bloemendal–Virág, [1011.1877](https://arxiv.org/abs/1011.1877) | Theorem2.10, p.19; Remark2.11 same page | Boundary-condition extension used by KRV; spikes concern regular Airy limits. [1109.3704](https://arxiv.org/abs/1109.3704) abstract also checked: matrix-valued spiked regular-edge limits, not the critical-density operator. |
| Claeys–Vanlessen, [math-ph/0607043](https://arxiv.org/abs/math-ph/0607043) | Example1.2 p.5; Theorem1.7 pp.6–7; Lax pair eqs.(1.15)–(1.21) p.4; Theorem1.11 p.8 | Rigorous β=2, k=1 critical kernel convergence, locally uniform including the diagonal. Theorem1.11 concerns deterministic orthogonal-polynomial recurrence coefficients, not random KRV coefficient convergence. |
| Claeys–Its–Krasovsky, [0901.2473](https://arxiv.org/abs/0901.2473) | Example1.2 p.2; discussion of eqs.(1.13)–(1.15) p.3; RH eqs.(1.19)–(1.21) p.4; right-tail eqs.(1.23)–(1.24) p.5; Theorem1.5 p.6; Theorem1.12 p.9 | Critical kernels/Fredholm determinants and hierarchy formulas. The p.3 paragraph expressly says their goal is not to prove general kernel or largest-eigenvalue convergence. Theorem1.5 is a left-tail asymptotic theorem, not an operator-convergence theorem and not the positive-tail bound used here. |
| Claeys–Kuijlaars, [math-ph/0501074](https://arxiv.org/abs/math-ph/0501074) | Theorem2.1 p.6, introduction | Quadratic *interior* zero, PainlevéII double scaling. Not a5/2 right edge. |
| Bleher–Its, [math-ph/0201003](https://arxiv.org/abs/math-ph/0201003) | Introduction; Theorem1.2 p.16 | Symmetric critical quartic/interior double scaling and orthogonal-polynomial asymptotics, not the proposed random edge operator. |
| Dumaz–Labbé, [2212.04862](https://arxiv.org/abs/2212.04862) | Theorem1 p.2 | Whole-line white-noise Anderson localization. Does not prove the critical β-ensemble limit. Their large-temperature Airy and localization-crossover work was also searched by title/abstract. |
| Dumaz–Li–Valkó, [2003.02779](https://arxiv.org/abs/2003.02779) | Theorem3 p.4 | Operator-level hard-to-soft Bessel→ordinary Airy transition, not k≥1. |
| Li–Valkó–Xu, [2607.08536](https://arxiv.org/abs/2607.08536) | Theorem1 p.2; introduction and operator-convergence discussion | 2026 lower Laguerre edge transition to ordinary Airy for diverging parameters, not a higher-order vanishing edge. |
| Gorin–Kleptsyn, [2009.02006](https://arxiv.org/abs/2009.02006) | Theorem1.1 p.4 and introduction | β→∞ multilevel Gaussian/Airy objects, not finite-β critical-density universality. |
| Lambert–Paquette, [2009.05003](https://arxiv.org/abs/2009.05003) | Theorem1.5 p.5 and introduction | Gaussian regular-edge characteristic polynomials and stochastic Airy function. |
| Edelman–Sutton, [math-ph/0607038](https://arxiv.org/abs/math-ph/0607038) | Abstract and Airy/Bessel operator sections | Classical finite-difference stochastic operators; no critical polynomial-potential limit theorem. |
| Forrester–Rahman–Shen, [2611.10990](https://arxiv.org/abs/2611.10990) | Abstract | November2026 hard-edge review/results. Hard-edge gap/correction results do not establish the proposed k≥1 soft edge. Earlier Forrester edge/Coulomb-gas work was searched by name and subject; no positive resolution was found. |
| Cafasso–da Silva Pinheiro, [2504.20721](https://arxiv.org/abs/2504.20721) | Theorem1.5 p.4 and Theorem1.10 p.6 | Critical5/2 unitary determinantal statistics governed by KdV. “Operator” here includes integral/RH structures, not convergence to the displayed Gaussian Schrödinger operator. |
| Dai–Long–Xu–Yao–Zhang, [2501.12679](https://arxiv.org/abs/2501.12679) | Theorem1.1 p.6 | Multiplicative constant in higher-order Fredholm large-gap asymptotics; no KRV stochastic-operator limit. |
| Claeys–Olver, [1111.3527](https://arxiv.org/abs/1111.3527) | Abstract and numerical RH/Fredholm method | A method for numerical higher-order TW distributions; no certified implementation/data was available in this workspace. We do not replace this law by ordinary TW₂. |

## Search record and limits

Queries included the exact source title and arXiv identifier; “exotic edge operators”; “Universality of the stochastic Airy operator”; “higher order stochastic Airy operator”; “critical edge beta stochastic operator2024 2025 2026”; “higher order edge beta ensembles”; “beta ensemble critical point operator”; “stochastic operator higher order Tracy-Widom”; every author group named in the task; and follow-ups through the cited references and recent author publication pages.

The decisive follow-up was “stochastic higher order Tracy-Widom operator conjecture”, which surfaced Baslingker's title. The initial search by “Conjecture5” or “Conjecture45” missed the published numbering13.1. Searching the operator description rather than only the conjecture label found the negative result.

The search is not a proof that no additional literature exists. It *is* enough to establish that this problem, as stated with the displayed operator, already has a printed counterexample at k=1,β=2. No higher-k or β≠2 classification is asserted.
