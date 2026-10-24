Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# R7-06 admission — C0032 / explicit heavy-tailed circular-law density

Date checked: 2026-09-18 UTC  
Native slot: `6aabe827777c8191a43330b4a87d481d`  
Own root: `research7_2026-09-17/R7-06/`  
Captured pre-admission master: `33fed5494c0b3f3ad71731631b2bed9933e6ed23`

## Canonical identity and shard gate

Canonical candidate: `C0032`.  The case-sensitive shard check is

`sum(ord(c) for c in "C0032") % 7 = 5`,

so C0032 is eligible for R7-06's shard.  At the captured master there is no `operations/claims/C0032.md`; repository search found only intake/ranking/history records, not a live canonical claim.

## Outside source and exact target

Primary source posing the unresolved identification:

- Charles Bordenave and Djalil Chafaï, **Around the circular law**, Probability Surveys 9 (2012), 1–89, arXiv:1109.3343v4, last revised 2012-03-13, https://arxiv.org/abs/1109.3343 .
- Heavy-tailed section, paragraph describing the limiting eigenvalue law `mu_alpha`: the current source says that `mu_alpha` is isotropic, has density `d mu_alpha(z)=g_alpha(|z|) dx dy`, and **is not known explicitly**; only `g_alpha(0)` is explicit and a large-radius asymptotic is given.  This is the source-level endpoint carried by canonical intake C0032.
- The campaign intake locator says `Section 6.6, p. 39`; the current arXiv v4 HTML places the actual “not known explicitly” statement in the heavy-tailed discussion preceding the later technical `6.6` convergence subsection.  I preserve the canonical ID but use the current-source statement, not the stale page/section metadata, as the scope authority.

Underlying theorem/implicit characterization:

- Charles Bordenave, Pietro Caputo and Djalil Chafaï, **Spectrum of non-Hermitian heavy tailed random matrices**, Communications in Mathematical Physics 307 (2011), 513–560, arXiv:1006.1713v5, https://arxiv.org/abs/1006.1713 .
- For i.i.d. entries in the domain of attraction of an `alpha`-stable law, `0<alpha<2`, this paper constructs the universal limiting law `mu_alpha`, proves isotropy/continuity, gives `g_alpha(0)` explicitly and the stretched-exponential tail, and gives an implicit scalar PWIT/stable-variable formula for the density.

### Full source closure criterion used by this worker

Produce, for every `0<alpha<2` and every radius `rho>=0`, an explicit identification of `g_alpha(rho)` that removes the still-implicit scalar fixed-point unknown from the Bordenave–Caputo–Chafaï representation (for example, a closed standard-special-function formula or an equivalent explicit transform/integral with no self-consistent unknown), together with a proof that it equals the density of their `mu_alpha`.  A finite Taylor jet, special alpha, numerical inversion, or merely rewriting the existing fixed-point equation is PARTIAL, not closure.

## Exact hypotheses/quantifiers

The canonical object is the universal `mu_alpha` from the heavy-tailed i.i.d. non-Hermitian ensemble for each `alpha in (0,2)` under the source hypotheses ensuring convergence.  The density is radial: `d mu_alpha(z)=g_alpha(|z|) dx dy`.  The target quantifies over **all** `alpha in (0,2)` and **all** radii, not merely `alpha=1`, the origin, or asymptotic radii.

## Recovered prior attempt and correction

The campaign record `C0032-A001` in `probability_1000_intake_claude_20260907/batch_C001.py` attempted to derive the density from the PWIT recursion and recorded the obstruction that the recursion “does not reduce to a scalar equation away from z=0.”  That obstruction is not valid against the cited original paper: Bordenave–Caputo–Chafaï already reduce the `t=0` problem at every radius to a scalar equation for a deterministic function `y_*(r)` driven by two independent positive `beta=alpha/2` stable variables, and their density formula is expressed using that scalar `y_*` and its derivative.  This run will therefore not repeat the old matrix-valued dead end.

No competing active claim or separate alias owner for C0032 was found in the bounded repository search.  This is a new R7-06 target, not a revival of handed-off I0114/I0006/G0008 or known G0001.

## Dated literature/current-version check

Checked 2026-09-18:

1. `arXiv:1109.3343v4` is still the current Bordenave–Chafaï survey version and still states that `mu_alpha` is not known explicitly.
2. `arXiv:1006.1713v5` is still the current expanded Bordenave–Caputo–Chafaï source and supplies the scalar implicit characterization, origin value, and tail, not an all-radius closed form.
3. Bounded searches for 2024–2026 work on the BCC heavy-tailed circular-law density did not locate a source-matching explicit all-radius formula.  Modern papers on heavy-tailed elliptic matrices generalize the PWIT method, while work on Brown measures/free-stable or fractional-free-convolution laws concerns different limiting objects; it is not treated as a resolution of this BCC law.

These search misses are **negative evidence only** and do not certify novelty or openness.  Source/current-version evidence is what justifies admission.

## Classification, milestone, frozen metric

Classification: **HARD OUTSIDE**.  It is a long-standing explicit-identification problem, but unlike a grand conjecture it has a concrete movable analytic quantity through the scalar stable recursion.

First milestone: compute a genuinely new exact local coefficient of the radial density at the origin, uniformly for every `alpha in (0,2)`, and use it to expose a systematic jet recursion if possible.

Frozen metric for this target:

`M_jet = largest m >= 0 such that the radial expansion g_alpha(rho)=sum_{k=0}^m c_{alpha,k} rho^(2k)+o(rho^(2m)) has coefficients c_{alpha,0},...,c_{alpha,m} in explicit Gamma-function/standard-constant form for every alpha in (0,2), with proof from the BCC scalar equation.`

Evidenced baseline: **`M_jet = 0`**.  The source gives `c_{alpha,0}=g_alpha(0)` explicitly, while no nonconstant coefficient is supplied there.  The metric is not the source closure flag: any finite `M_jet` remains PARTIAL.

Initial ordinary-run methods after claim: **B2 / B14 / B16**.  B2 attacks the prior obstruction by testing its negation against the actual scalar source equation; B14 exploits radial/isotropic symmetry to use `r=|z|^2`; B16 computes the exact first local coefficient and the special case `alpha=1` as a consistency certificate.
