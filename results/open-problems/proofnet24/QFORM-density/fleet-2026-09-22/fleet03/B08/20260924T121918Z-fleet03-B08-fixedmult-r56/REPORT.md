# fleet03/B08 r56 — fixed-multiplicity audit plus `s_16` terminal saturation

Current owner objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924` (later than the historical diffuse-only B08 assignment).  
Run: `20260924T121918Z-fleet03-B08-fixedmult-r56`.

Canonical detailed artifacts for this run:

- full second textual audit: `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/audits/fleet03/B08/20260924T121918Z-fleet03-B08-fixedmult-r56/AUDIT.md`;
- full new theorem/proof: `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/fleet03/B08/20260924T121918Z-fleet03-B08-fixedmult-r56/TERMINAL_S16_SATURATION.md`;
- exact arithmetic checker and executed output in the same improvement folder.

## Mathematical result

The 17-eigenvalue manuscript, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, was reread end to end and passes this review. The full three-eigenvalue conjecture remains open.

The new theorem `QFORM-S16-TERMINAL-R4-SATURATION-v1` treats the exact chamber where the current proof architecture fails if `s_17>=1` is weakened to `s_16>=1`. Put `eta=1/100`, `kappa=1/80^2`. If `A=A^T` has no eta-pivot, `s_16(A)>=1`, and `V_5(A)<kappa^5`, then all bad volume ratios of orders `r<=3` are impossible, so necessarily `V_4>=kappa^4` and `V_5/V_4<kappa`. A sampled `r=4` seed gives

`A=D+R+E`, `||E||_F<=1/16`, `rank R<=12`, `R[L,L]=P[L,L]`, `rank P[L,L]<=4`.

The terminal chamber then obeys the quantitative identities/inequalities

\[
s_5(D)\le\frac{291}{350},\qquad
s_{12}(R)\ge\frac{297}{2800}.
\]

There are four heavy physical coordinates `H subset L` on which

\[
s_4(P_{H,H})\ge\frac{109}{700},
\qquad
|\det P_{H,H}|\ge\left(\frac{109}{700}\right)^4.
\]

Writing `B=A[S,T]`, the exact interpolation identity

\[
P_{H,H}=A_{H,T}B^{-1}A_{S,H}
\]

gives the physical determinant chain

\[
|\det A_{H,T}|\,|\det A_{S,H}|
\ge
\left(\frac{109}{700}\right)^4 |\det A_{S,T}|.
\]

Moreover `rank P[L,L]=4`, so for `L_0=L\setminus H`,

\[
P_{L_0,L_0}=P_{L_0,H}P_{H,H}^{-1}P_{H,L_0}.
\]

Finally, for the manuscript decomposition

\[
R=P+\Pi_T(R-P)+(I-\Pi_T)(R-P)\Pi_S,
\]

each of the three rank-at-most-four terms is quantitatively indispensable:

\[
\min\{s_4(P),s_4(\Pi_T(R-P)),s_4((I-\Pi_T)(R-P)\Pi_S)\}
\ge\frac{297}{2800}.
\]

Thus the terminal `r=4` obstacle is a genuinely saturated 12-direction low-rank configuration, not merely slack in the manuscript's rank count.

## Actual analytic payment and remaining scalar loss

Applying the completed single-cross-bank Plancherel theorem to the larger of the two physical four-by-four banks `A[H,T]`, `A[S,H]` yields

\[
\|p_Q\|_\infty
<8.357\,|\det A_{S,T}|^{-1/8}.
\]

This is a real bound on the full quadratic form with all other curvature retained, but it does not close `17 -> 16` because the sampled seed determinant can be arbitrarily small even when aggregate `V_4` is bounded below.

The designated fleet04/B08 theorem `QFORM-PHYSICAL-DELETION-CHILD-WINDOW-v1` was also applied at an actual fixed-multiplicity inequality. Since deleting one original coordinate is a rank-at-most-two change,

\[
s_5(A)\ge1\implies s_3(C_i)\ge1
\]

for every deletion child. Hence, if any child spectral projection onto `|lambda|>=1/64` has maximum physical leverage at most `1/32`,

\[
\|p_Q\|_\infty<64,
\qquad p_Q\in C_0.
\]

After scaling this is `<64 K^2/s`. Therefore every unpaid `s_16` terminal survivor must have a localized `1/64` high spectral window in every deletion child.

## Exact next implication

To prove a universal 16-eigenvalue theorem from this route, consume simultaneously:

1. the saturated `r=4` identities above;
2. the determinant-chain seed loss without dividing by a tiny sampled determinant; and
3. the forced localized child-window witness for every deletion.

No 16-eigenvalue theorem is claimed yet. The unrestricted three-eigenvalue target and full continuity remain open. Status: `WITHOUT_VERIFIED_BRAIN`.
