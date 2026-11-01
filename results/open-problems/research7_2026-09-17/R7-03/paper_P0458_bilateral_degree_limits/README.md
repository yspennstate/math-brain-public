# P0458 paper package — degree fluctuations in bilateral preference random graphs

Status: **mathematical source endpoint PROVED internally; package prepared; independent audits still required.**

Worker: `R7-03`  
Canonical target: `P0458`  
Source: Hossein Dabirian and Vijay Subramanian, *Connectivity of a family of bilateral preference random graphs*, Journal of Applied Probability 63(2) (2026), 552–579, DOI `10.1017/jpr.2025.10051`, §1.1, first of the “two additional questions.”

The source asks for the limiting distribution of

\[
\frac{D-\mathbb E D}{\sqrt{\operatorname{Var}D}}
\]

for the degree `D` of a fixed vertex of `LK(n,k)`, and remarks that even `Var(D)` is difficult because of the dependence structure.

## What this package proves

Let

\[
s_n^2=\frac{k(n-k)}{n},\qquad
v=\frac13+\frac{\sqrt3-2}{2\pi},\qquad
g(z)=\phi(z)+z\Phi(z).
\]

1. **Interior growing regime.** If `k→∞` and `n-k→∞`, then with `H=k-D`,

\[
\frac{H}{s_n}\Longrightarrow g(Z)
\]

with convergence of the first two moments. Hence

\[
\mathbb ED=k-\frac{s_n}{\sqrt\pi}+o(s_n),\qquad
\operatorname{Var}(D)=v s_n^2+o(s_n^2),
\]

and

\[
\frac{D-\mathbb ED}{\sqrt{\operatorname{Var}D}}
\Longrightarrow
L_\infty:=\frac{\pi^{-1/2}-g(Z)}{\sqrt v}.
\]

This includes, in particular, the source's natural regime `k→∞`, `k=o(n^{1/3})` used for its sharp mean-degree theorem.

2. **Fixed-complement boundary.** If `r=n-1-k≥1` is fixed, then `H=k-D` converges with its first two moments to a mixed-Poisson variable `H_r` satisfying

\[
A_r\sim\Gamma(r,1),\qquad
H_r\mid A_r=a\sim\operatorname{Poisson}(\Lambda_r(a)),
\]

where

\[
\Lambda_r(a)=e^{-a}\sum_{\ell=0}^{r-1}(r-\ell)\frac{a^\ell}{\ell!}.
\]

Thus the standardized degree tends to

\[
L_r=\frac{\mu_r-H_r}{\sqrt{\nu_r}},
\]

with explicit `mu_r=E H_r` and `nu_r=Var(H_r)>0`.

3. **Boundary-to-interior gluing.** As `r→∞`, `L_r=>L_∞`.

4. **No single law for arbitrary switching `k(n)`.** For example, the fixed-complement laws for `r=1` and `r=2` are distinct, so alternating those two complements produces two different subsequential limits.

5. **Fixed finite `k`.** This is reconciled with existing Erlang-weighted-tree prior art rather than claimed as new. Moharrami–Subramanian–Liu–Sundaresan identify the root-degree law in the local weak limit for fixed potential degree.

The package therefore gives a regime-complete source answer: a universal continuous non-Gaussian law throughout the entire interior growing regime, explicit discrete mixed-Poisson boundary laws at finite complement, and known fixed-`k` limits.

## Files

- `main.tex` — self-contained mathematical paper with all theorem proofs.
- `prior_art_2026-09-19.md` — dated source/current-version/literature comparison.
- `AUDIT_REQUEST.md` — exact independent-proof checklist. This file is only a request/checklist and is **not** an audit.

## Proof provenance

The paper consolidates and strengthens the two immutable full-proof artifacts:

- `research7_2026-09-17/R7-03/artifacts/2026-09-19/2026-09-19T070300Z__P0458_full_interior_growth_degree_law.md`;
- `research7_2026-09-17/R7-03/artifacts/2026-09-19/2026-09-19T073000Z__P0458_fixed_complement_mixed_poisson_and_regime_classification.md`.

The package adds an explicit source-regime corollary, an explicit CDF/density formula for the interior standardized law, and an independent beta–gamma derivation of the finite-complement mean.

## Closure discipline

This repository's closure protocol additionally requires:

- an actual `P26` independent full-proof PASS;
- one distinct OTHER-track independent full-proof PASS.

Neither is supplied or simulated here. Self-checks, readbacks, compilation, and coordinator reconciliation do not count as independent audits. Negative literature searches are not novelty certificates.
