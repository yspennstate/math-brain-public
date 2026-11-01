# R22 verification - overlap range, notation, citations, and Lean check

## Scope

Round R22 integrated five read-only agent reports and made a focused manuscript
pass on:

- the remaining II.B pair-correlation gap;
- notation conflicts against the older RMT/MP pruning manuscript;
- Balan--Wang and full-spark citations;
- one additional fixed-excess heterogeneous row-density lower side;
- a small Lean formal check for the sign-frame obstruction.

## Mathematical checks

1. `prop:small-D-negligible` is a lower/second-moment bookkeeping theorem only.
   It proves that for `s<h(gamma)/d_F`, the range `2<=D<=eps m` contributes
   negligibly because the hypergeometric overlap lower tail is exponentially
   rare and `q_D<=p_m`.  It does not close the bulk range.

2. `prob:pc` and `rem:pc-reduction` now ask only for the bulk estimate
   `E[(1-|varrho_ST|^2)^(-d_F/2); D>=eps m] <= 1+o(1)`.  This avoids the
   false stronger negative-moment statement over all `D>=3`, where small-D
   terms may be singular and must be handled by `q_D<=p_m` instead.

3. `rect:heterogeneous-row-density` follows the fixed-excess column-distance
   proof with row-wise density products.  It is lower-side only.  For `r=0`,
   the existing square row-wise budget remains sharper.

4. The supercritical phase-retrieval remark now distinguishes the Balan--Wang
   `omega` branch from the full lower-Lipschitz partition statistic.  No exact
   supercritical theorem for all stability conventions is claimed.

## Notation checks

- Density-growth rate is now `kappa`, not `rho`.
- Normal overlap remains `varrho`.
- Local ball radii use `tau`.
- Fixed rectangular excess uses `r`; `k` is reserved for the k-th singular
  value and two-sided k-by-k minors.
- The random-count binomial pool size is `n_m^{pool}`, not `L_m`.

## Lean check

Added `lean/SignCritical.lean`, which proves:

- determinant zero when the first two columns of a selected square integer
  matrix are equal;
- determinant zero when the first two columns are opposite.

This verifies the algebraic determinant step after the pigeonhole selection in
`prop:sign-critical`; it does not formalize the full finite-subset extraction.

Command run from `paper19/lean`:

```powershell
$pkgs = '~\phase_retrieval_omega\lean\omega_comb\.lake\packages'
$dirs = 'mathlib','batteries','aesop','Qq','proofwidgets','importGraph','LeanSearchClient','plausible' |
  ForEach-Object { Join-Path $pkgs "$_\.lake\build\lib\lean" }
$env:LEAN_PATH = ($dirs -join ';')
$lean = "$env:USERPROFILE\.elan\toolchains\leanprover--lean4---v4.29.1\bin\lean.exe"
& $lean .\SignCritical.lean
```

Result: exit code 0.  A previous `lake env lean` attempt timed out and left two
Lake processes; both were stopped, `.lake` was removed, and a final process
check showed no remaining Lean/Lake/Elan processes.
