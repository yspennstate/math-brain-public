# P0282 idea before production validation — affine typical-shape cutoff

Date: 2026-09-19 UTC

Continue the admitted P0282 target. Do not reopen intake or change the frozen metric.

The previous typical-shape theorem used a homogeneous first-row cutoff `mu_1 < ceil(9s/25)`, giving the source-valid window `k/n >= 355/576`. The new route is to keep the asymptotically smaller slope `3/10` while adding a finite-rank buffer:

`r_s := ceil(3s/10 + 2)`, and call a parent good when `mu_1 < r_s`.

For a good parent every addable content satisfies `C < 3s/10 + 2`, so the exact Kerov moment identity used in the predecessor gives

`G_mu(K) <= 1/K + s/[K^2 (K - 3s/10 - 2)]`.

The additive `+2` is intended only to suppress the low-rank Plancherel tail near the retained fixed-defect frontier `j=67`; asymptotically the deterministic boundary is governed by slope `3/10`, not `9/25`.

Candidate rational boundary to validate exactly:

`K >= (3933/2500) j + 1`, equivalently `2500 n >= 6433 j`, hence `k/n >= 3933/6433 ~ 0.6113788279`.

Validation obligations before claiming the theorem:

1. exact Plancherel tail counts for `s=66,...,110` via the already reviewed Gessel/Toeplitz machinery, checking the `R^2`-tilted bad mass is `< 1/(700j)` at the candidate boundary;
2. for `s>=111`, a source-independent union bound with `r_s=ceil(3s/10+2)` plus a 10-step residue-class induction, again implying bad tilted mass `<1/(700j)`;
3. exact rational algebra proving the deterministic good-parent factor is `>1+1/(675j)` for every `j>=67` (prefer a shifted positive-coefficient polynomial in `j-67`);
4. combine the two factors: `(1+1/(675j))(1-1/(700j))>1`;
5. separately advance the frozen metric from row 106 to row 107 with a new exact Gessel/CRT seam certificate.

If any of these fail, record the obstruction rather than weakening the metric or silently changing the source.