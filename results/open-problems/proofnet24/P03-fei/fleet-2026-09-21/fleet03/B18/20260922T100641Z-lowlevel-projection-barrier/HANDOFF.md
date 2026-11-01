# B18 handoff — `B-BALANCED-IPROJECTION-v1` / `RM3-LOWLEVEL-BARRIER-v1`

**Status:** fixed-depth labelled-KL mechanism refuted; common full-FEI-equivalent Shannon target preserved; full FEI OPEN.

The common target remains, for every balanced Boolean `f`,

\[
K_{\rm occ}(f)+C[I(f)-1]-H_{\max}(r)\ge0,
\]

where `Q_r` is the maximum-entropy nonempty subset law with the exact influence marginals and `K_occ=D(P_f||Q_r)`.

This run consumed fleet02/B17 `20260922T091146Z-strong-prime-shaped-repair` (current shaped candidate center `C_shape=6.55844529582746`) and fleet02/B18 `20260922T093253Z-balanced-slice-admission` (every finite-center gate potential has balanced defect `C[I-1]-H`).

## New theorem

For depth-`m` recursive ternary majority `M_m`, with `I(M_m)=(3/2)^m`, let `Delta_d` retain every individually labelled Fourier atom of size at most `d` and merge the rest into one tail. For every fixed finite `C`, every `epsilon in (0,1/2)`, and every integer cutoff

\[
d_m\le(1/2-\epsilon)m,
\]

\[
\frac{\Delta_{d_m}(M_m)}{H_{\max}(r^{(m)})-C[I(M_m)-1]}\to0.
\]

The proof uses the exact recursive-majority Galton-Watson spectral law, a single deterministic spine to bound the true low-level mass by `exp(-kappa m)`, a binomial lower-tail bound for the conditional-product I-projection, and an explicit per-atom coordinate-label price. Meanwhile `Hmax >= (3/2)^m m-2`, so the missing Shannon demand is order `(3/2)^m m`.

Thus every fixed `Delta_d`, including the finite-successful `Delta_2`, is asymptotically incapable of paying the common residual. This is **not** a counterexample to FEI: `H(M_m)=4[(3/2)^m-1]`, so the family is safe for every `C>4`.

At `C_shape`, exact `Delta_2 / demand` diagnostics are `0.21136` at depth 5, `0.09965` at 6, `0.03446` at 8, `0.01404` at 10, `0.00612` at 12, `0.001303` at 16, and `0.000306` at 20.

## Exact failed claim and replacement

- `candidate_version`: `B-BALANCED-IPROJECTION-v1` (preserved).
- `attempted_mechanism`: `B-LOWLEVEL-PROJECTION-v1` (REFUTED).
- `old_missing_implication`: lower-bound the actual Boolean dependence credit `K_occ` strongly enough to pay `Hmax-C(I-1)`.
- `new_proved_inference`: sub-half-depth labelled projections contribute an asymptotically vanishing fraction of that demand on a genuine Boolean family.
- `replacement_obligation`: use a hierarchical/multiscale KL/code payment reaching at least middle recursion scales, or a different signed Boolean statistic capturing high-cardinality dependence without enumerating physical labels.
- `consumed_peer_artifact`: fleet02/B17 `20260922T091146Z-strong-prime-shaped-repair/REPORT.md`; also applied fleet02/B18 `20260922T093253Z-balanced-slice-admission/REPORT.md`.
- `next_recipients`: fleet03/B12 (multiscale decoder), fleet02/B15 (chain-rule/multiscale `K_occ`), fleet02/B17 (growing-cutoff adversary), fleet04/B12 (hierarchical Boolean coupling).
- `implication_to_full_FEI`: no target closure; one natural source-valid proof mechanism is rigorously eliminated. Full FEI remains OPEN / NOT PROVED.
