from pathlib import Path
p=Path('ATTEMPT.md');s=p.read_text(encoding='utf8')
s=s.replace('Thus every proper weak limit satisfies E φ_i≥c log||i||_∞: apply bounded truncations min(φ_i,K), pass to weak limits, and let K→∞. Equivalently, domain monotonicity and the limit construction in Proposition 5 yield the same statement. This does not establish the existence of a proper limit.','Thus every proper weak limit satisfies E φ_i≥c log||i||_∞. To justify this without an incorrect exchange of means and weak limits, retain the full stochastic domination by the fixed ordinary wall field on D. For every K, E_{μ_N^+} min(φ_i,K)≥E_{wall,D} min(φ_i,K). Pass to weak limits at fixed K and then let K→∞; the right side tends to the box mean. This does not establish the existence of a proper limit.')
p.write_text(s,encoding='utf8')
with p.open('a',encoding='utf8') as f:f.write(r'''

## Hostile referee checklist

- **Incorrect domination direction:** resolved in Proposition 1; growing the domain increases the positive field. This invalidates the old fixed-small-box upper-bound argument.
- **Undefined conditioning at the pin:** avoided by keeping φ_0 fixed in the finite-volume energy, not conditioning on an event of zero probability.
- **Infinite-volume positivity event:** never conditioned upon directly. All constraints are finite-volume; tightness is required for the limiting construction.
- **Boundary signs:** Proposition 4 needs all neighbor heights ≥0. It is applied only to the wall field. No extension to unconstrained or signed boundary heights is asserted.
- **Curvature constants and β:** fixed positive inverse temperature and source edge weights are absorbed into c_±. The proof uses unit nearest-neighbor edges. If weights are used, the local denominator becomes c_+ times the sum of incident weights, and the numerator is the weighted sum times c_-.
- **Logarithm near the origin:** lower-bound statements are only for large distances. A logarithmic upper estimate is formulated with log(2+|i|).
- **Positivity boundary integration:** multiplying by φ_v makes the integration-by-parts boundary term zero at φ_v=0. Integration by parts without that factor would have a wall term and would be invalid here.
- **Weak-limit mean passage:** weak convergence alone does not preserve means. Proposition 2 instead preserves stochastic domination of bounded truncations; Proposition 5 uses uniform second moments to establish uniform integrability.
- **Using Brascamp–Lieb with a wall:** a convex C² soft-wall approximation is given explicitly. The variance bound centers at the actual mean, and thus cannot by itself bound that mean.
- **Borrowed lower-bound theorem:** external input B is precisely the ordinary full-box wall result as stated by the verified survey. A primary-source theorem-number verification of Deuschel–Giacomin was not obtained (publisher fetch forbidden). The finite-volume comparison and its implication are proved here; the literature dependency is explicit.
- **A maximum theorem is not a conditional theorem:** the later Ginzburg–Landau maximum papers concern unconstrained fields. Conditioning on simultaneous positivity is a rare event and destroys a naive application of their tail estimates.
- **Lean scope:** only finite algebra is submitted. No FKG, BL, box theorem, DLR construction or open-problem resolution is claimed formally verified.

## Computation (numerical evidence only)

numerics.py integrates a two-free-vertex grounded triangle 0--x--y--0 on the positive quadrant with V(t)=t²/2+ε(1−cos t). For ε=0.3, 0.7≤V''≤1.3. All integrals use product trapezoidal quadrature on [0,10]², at 401 and 801 points per axis, and no more than a few arrays of about 5 MB each. The upper endpoint cutoff and discretization are not interval-certified.

With zero boundary the Euler energy should equal n=2. At the finer grid it is 2.0000215365 (Gaussian) and 2.0000271962 (ε=0.3). The Gaussian mean benchmark is 0.7329037678543798; the finer-grid mean is 0.7328973451029526. For ε=0.3 and the boundary on the edge from y raised from 0 to 0.5 to 1, the finer-grid x means are 0.6592508487, 0.7017270366 and 0.7590288606. These checks support the sign and cancellation in the finite formulas. They test neither a growing two-dimensional box nor the missing uniform bound A. numerical_checks.json contains the complete results and model specification.
''')
with Path('LITERATURE.md').open('a',encoding='utf8') as f:f.write(r'''

## Later leads inspected, not exact resolutions

- David Belius and Wei Wu, *Maximum of the Ginzburg–Landau fields*, arXiv:1610.04195v2 (18 June 2019), PDF pp.1–2, especially Theorem 1.1. It proves that the maximum of the **unconstrained zero-boundary field** divided by log N tends to 2√g in L² under even uniformly convex V. The PDF was fetched and the hypotheses and theorem read. There is no origin pin and no simultaneous positivity conditioning. It is a useful multiscale lead, not a solution of F0073.
- Florian Schweiger, Wei Wu and Ofer Zeitouni, *Tightness of the maximum of Ginzburg–Landau fields*, arXiv:2403.11500v1 (18 March 2024), PDF pp.1–3, Theorem 1.1. The potential additionally has V'' Lipschitz. The result is tightness of the centered maximum of the **unconstrained zero-boundary field**. It supplies approximate random-walk and barrier technology but does not prove this pinned-positive statement. PDF inspected.
- Giambattista Giacomin, *On stochastic domination in the Brascamp–Lieb framework*, Mathematical Proceedings of the Cambridge Philosophical Society 134(3) (2003), 507–514. DOI 10.1017/S0305004102006552. Metadata verified; attempted primary PDF fetch returned 404. No theorem from it is used or claimed to solve F0073.
- Holley/FKG association and Brascamp–Lieb variance inequality are standard theorem inputs to ATTEMPT.md. The full proofs of the new comparisons, energy identity and one-site reduction are recorded there. Velenik also cites Brascamp–Lieb and Giacomin's framework in the source.

## Search limitations and conclusion

The first OpenAlex text search returned 30 works and the second 40; these are bounded relevance searches, not exhaustive. The works-citing-source query returned all 93 indexed citing works in one page; the full response is citing.json and a title/DOI digest is citing_summary.txt. These are metadata records, not 93 full-paper reviews. arXiv searches and Crossref responses are saved alongside their queries. Semantic Scholar returned HTTP 429 and GitHub repository search HTTP 403 (rate limit); these services were attempted but their contents were not searched successfully.

One preliminary wetting download used an unverified guessed arXiv ID math/0604175, which actually is Braverman–Yampolsky on Julia sets. It is off-topic and excluded from the evidence. The exact-title arXiv query later corrects that discovery error. The D–G publisher primary-source fetch returned HTTP 403; the box input is verified at the survey level, not by an inspected theorem in that original paper.

No inspected paper states and proves F0073 with the same objects, hypotheses and quantifiers. Therefore SOLVED_IN_LITERATURE is not warranted. The bounded search does not certify that the problem remains open throughout all literature. Mathematical work continues as PARTIAL.
''')
print('Referee and literature notes saved')
