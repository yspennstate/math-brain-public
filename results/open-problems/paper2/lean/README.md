# Lean formalization - paper2 (`udc_whp`)

Machine-checked proofs of the elementary arithmetic core of Proposition
`prop:affine-transfer` in `../udc_whp.tex`.

## File

- `UdcAffineTransferArithmetic.lean`:
  - `preimage_width_mem_grid`: if `lam <= a <= Lam`, then the image-width
    interval `[Lam * ell, lam * beta / k)` pulls back by `t -> t / a` into
    `[ell, beta / k)`;
  - `preimage_width_mem_allwidth`: the same interval calculation for
    `[Lam * ell, lam * beta)`;
  - `affine_grid_transfer_arithmetic`: a pullback identity
    `muA t = mu (t / a)` transfers the source grid-form inequality to the
    image inequality;
  - `affine_allwidth_transfer_arithmetic`: the corresponding all-width
    transfer;
  - `grid_step_interpolation`: monotonicity interpolates a grid inequality to
    intermediate widths, paying the multiplier loss `k -> k^2`.

The Lean file intentionally leaves slab geometry, singular values, and
empirical pushforward equality as hypotheses. It verifies the real-arithmetic
and order manipulations that determine the constants in the paper statement.

No file uses `sorry` or `admit`.

## Toolchain Status

This folder matches the local setup used by `../../paper12/lean`:

- Lean / Lake toolchain `leanprover/lean4:v4.29.1`
- mathlib reused from
  `~\phase_retrieval_omega\lean\omega_comb\.lake\packages\mathlib`

## How To Check

From this directory in PowerShell:

```powershell
$pkgs = "~\phase_retrieval_omega\lean\omega_comb\.lake\packages"
$dirs = "mathlib","batteries","aesop","Qq","proofwidgets","importGraph","LeanSearchClient","plausible" |
        ForEach-Object { Join-Path $pkgs "$_\.lake\build\lib\lean" }
$env:LEAN_PATH = ($dirs -join ";")
$lean = "$env:USERPROFILE\.elan\toolchains\leanprover--lean4---v4.29.1\bin\lean.exe"
& $lean .\UdcAffineTransferArithmetic.lean
```

A `0` exit code with no output means the proof checks clean.
