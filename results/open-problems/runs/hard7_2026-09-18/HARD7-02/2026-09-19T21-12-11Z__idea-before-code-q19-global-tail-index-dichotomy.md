Model: GPT-5.6 Sol. Reasoning: UNVERIFIED; this run did **not** run on GPT-6 at verified maximum reasoning.

# HARD7-02 idea checkpoint before code — Question 1.9 global tail-index dichotomy

Status at checkpoint: **exploration / theorem candidate only; no code has been written in this run.** Active exclusive claim remains `operations/claims/CAMPBELL-OROURKE-2022-Q1.9.md`.

Frozen metric at entry: `T_corr=3`. Planned methods, as precommitted by the preceding run and different from its B1/B20/B27 triple: **B8 / B16 / B26**.

## Continuity recovered

The newest completed report is `runs/hard7_2026-09-18/HARD7-02/2026-09-19T20-13-38Z__q19-off-axis-mass-tail-exponent.md`. It proves, as a theorem candidate with full on-page proof but no independent audit, that every C2 angular probability law with positive off-axis mass

`rho_off(theta)=theta({(w1,w2): w1*w2 != 0})>0`

has exact radial power exponent `alpha`. Its proof supplies two stronger ingredients that were not yet extracted into one invariant:

1. every radial moment of order `p<alpha` is finite;
2. the logarithmically integrated radial tail

`V(r)=int_r^infinity F(t) dt/t`, `F(r)=mu({|z|>r})`,

satisfies `V(r) >= A r^(-alpha)` for all sufficiently large `r`, with some `A>0`.

Earlier HARD7-02 Question-1.8 work, in `2026-09-19T08-18-00Z__complete-axis-support-classification.md` and `2026-09-19T09-12-00Z__axis-cstar-logarithmic-mean.md`, proves that every C2 angular measure supported on the two coordinate axes is exactly a dilation of the Bordenave--Caputo--Chafai iid heavy-tailed circular law. The source itself states that the iid limiting ESD has an exponential tail, and earlier reports record that it has finite moments of every order.

Fresh primary-source readback this run confirms Campbell--O'Rourke Section 1.3 still asks exactly: `How does the tail behavior of mu_{alpha,theta_d} vary with respect to theta_d?` and explicitly contrasts the iid exponential tail with the Hermitian heavy tail. Bounded fresh 2026-09-19/20 web searches using the exact question wording, source title/authors, `theta_d`, `mu_{alpha,theta_d}`, tail and moment-index terms did not locate a later paper claiming a general resolution. This is bounded negative evidence, not a novelty certificate.

## New route before code

Define the **radial moment index**

`p_*(theta)=sup{p>0 : int |z|^p mu_{alpha,theta}(dz) < infinity}`.

The previous run's lower bound on `V` appears to determine the endpoint `p=alpha`, not merely the logarithmic tail exponent. Indeed, if the `alpha`-moment were finite then layer cake would give

`int_r^infinity F(t) dt/t <= r^(-alpha) int_r^infinity t^(alpha-1)F(t)dt = o(r^(-alpha))`,

contradicting `V(r)>=A r^(-alpha)`. Hence every positive-off-axis C2 law has infinite `alpha`-moment. Since all moments below `alpha` are finite, this would give the exact identity

`p_*(theta)=alpha` whenever `rho_off(theta)>0`.

On the complementary event `rho_off(theta)=0`, the angular measure is supported on the coordinate axes. C2 nondegeneracy forces positive mass on both axes. The earlier complete axis classification then gives a dilation of the iid law, hence

`p_*(theta)=infinity`.

Thus the whole C2 class may have a sharp two-phase classification:

`p_*(theta) = infinity` if `rho_off(theta)=0`, and `p_*(theta)=alpha` if `rho_off(theta)>0`.

This is stronger and cleaner than family-by-family tail exponents. It also shows a singular tail transition: arbitrarily small positive off-axis angular mass collapses the moment index from `infinity` to `alpha`.

## Planned B8 / B16 / B26 work

- **B8 DISCRETIZE:** replace the infinite-dimensional angular law, for this exact tail-index question only, by the Boolean support statistic `rho_off=0` versus `rho_off>0`; prove no third regime survives C2.
- **B16 SMALL CASES:** inspect the minimal atomic C2 support patterns symbolically: two-axis atoms lie in the exponential/all-moments regime; any admissible atomic support with an off-axis atom of positive mass lies in the `p_*=alpha` regime. This is a sanity check on the global partition, not finite-size spectral evidence.
- **B26 SPORADIC CASE:** hunt the two dangerous boundaries: arbitrarily unbalanced axis masses `p->0,1` (still all moments while C2 holds) and off-axis contamination `epsilon downarrow 0` (already `p_*=alpha` for every epsilon>0). If both survive exactly, the tail-index functional has a genuine support-boundary jump rather than a missing intermediate family.

Only after the proof is written will a tiny exact symbolic checker be added, and only if it checks a finite algebraic implication worth archiving. No simulation will be used as evidence.
