# HARD10-03 — 2026-09-16T07-22-52Z checkpoint addendum

This file is append-only. It does not overwrite the mathematical checkpoint.

## 1. Main report delivery receipt

Main report:

`proofnet24/HARD10-03/runs/2026-09-16/2026-09-16T07-22-52Z__report.md`

Create commit:

`75dfe37aa0cea05bdefad9211356bf9c73c7ccf5`

Exact-commit readback blob:

`e4fc739060cb52979e6bab837f0065183d036c55`

The file was fetched using the exact create-commit ref above. Therefore the main report delivery status is **VERIFIED**.

No transient write retry was needed. No approval/security denial occurred. Approval requirement: **NOT EXPOSED**.

## 2. Green-kernel derivation clarification

Equation (3.2) of the main report,

\[
g(x)\le C(1+|x|_\infty)^{-1},
\]

is standard and correct. To remove any possible ambiguity in the report's compressed continuous-time Gaussian derivation, here is a fully discrete Poissonization proof for the exact rate convention.

A single interchange label jumps at total rate `6` and chooses each of its six neighbors with probability `1/6`. If `S_n` is discrete-time nearest-neighbor SRW and `q_n(x)=P(S_n=x)`, then

\[
p_t(0,x)
=e^{-6t}\sum_{n\ge0}\frac{(6t)^n}{n!}q_n(x).
\]

Tonelli and

\[
\int_0^\infty e^{-6t}\frac{(6t)^n}{n!}\,dt=\frac16
\]

give the exact identity

\[
\boxed{
g(x)=\frac16\sum_{n\ge0}q_n(x).}
\]

The standard discrete-time Gaussian heat-kernel estimate

\[
q_n(x)\le C n^{-3/2}\exp(-c|x|_2^2/n)
\]

(on the allowed parity class; zero probabilities only improve the bound), summed over `n`, yields

\[
\sum_{n\ge1}n^{-3/2}e^{-c|x|^2/n}
\le \frac C{1+|x|},
\]

by splitting at `n=|x|^2` or by the substitution `u=|x|^2/n`. This proves (3.2) without relying on a short-time continuous-time Gaussian form outside its natural regime.

No statement or exponent in NEW-L65--68 changes.

## 3. Post-write self-review

The following points were checked after exact readback of the main report:

1. **Positive-definite pointwise bound:** `G_beta(x)<=G_beta(0)` follows from the `2 x 2` principal minor of the positive-definite kernel and the already proved symmetry/nonnegativity of `G_beta`.
2. **NEW-L65 exponent:** choosing `R^3=beta^(1/4)/(1+log beta)` balances `c_beta R^2` against `beta^(-1/4)/R`, giving `beta^(-1/3)(1+log beta)^(1/3)`.
3. **Capacity direction:** with the explicit variational definition, `1/Cap_g(A)` is the infimum energy and is at most the uniform-measure energy; the Markov step therefore has the stated direction.
4. **Packing lemma:** a maximal `R`-separated family gives an `R`-ball cover; each assigned cell has diameter at most `2R`, and Cauchy--Schwarz gives `D_{2R}>=1/m`.
5. **Superdiffusive packing exponent:** at `R=(1/4)beta^(3/4-epsilon)`, NEW-L64 gives `E D_{2R}=O(beta^-epsilon)` for `0<epsilon<1/4`; Markov at the square-root threshold yields packing `Omega(beta^(epsilon/2))` with failure `O(beta^(-epsilon/2))`.
6. **Random-grid inverse participation:** same cube implies pair displacement `<r` pathwise. The independent random shift is retained explicitly; no fixed-grid point-shift invariance is asserted.
7. **Scope:** all NEW-L65--68 conclusions are necessary conditions under the hypothesis `p_infty(beta)=0`; none is presented as a proof of the Tóth conjecture.

The principal remaining gap is still anticipativity: the many remote blocks/representatives forced by NEW-L67/68 are selected from the final cycle. The existing conditional random-cut theorem cannot be applied until a no-peeking exploration extracts comparable block geometry before revealing the relevant clocks.

No Gmail/email, Google Drive, public posting, repository settings/workflows/permissions changes, force-push, third-party contact, or paid compute was used.