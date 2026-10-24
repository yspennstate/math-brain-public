# account02/B09 independent audit — spectral rank perturbation / diagonal dominance

Run: `20260924T114444Z-account02-B09-QFORM-auto11`

Current objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.
Pinned manuscript source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`.
Pinned source SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.
Pinned git blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

## Verdict

**B09 lens: PASS.** I did not find a mathematical defect in the spectral-rank-perturbation / diagonal-dominance chain that turns the sampled interpolation into Proposition `prop:volume`. The proof correctly uses singular values for the nonsymmetric auxiliaries, uses the global rank `<=3r` only to force large diagonal entries, and then uses the restricted rank `<=r` on the seed complement for the contradiction.

**Threshold-improvement status: NO 16-eigenvalue improvement from the present rank-count argument alone.** The terminal bad-ratio case for order five is `r=4`. With only `s_16(A)>=1`, the displayed perturbation argument forces only four large entries of `D`, while `rank R[L,L]<=4` is compatible with an invertible `4 x 4` block. The existing diagonal-dominance contradiction needs five large diagonal entries. A reduction from 17 to 16 therefore needs an additional structural ingredient in the terminal `r=4` case; merely replacing one displayed index by 16 is invalid.

I also give below an explicit no-pivot, large-spectrum family showing that the algebraic rank constants `rank R<=3r` and `rank R[L,L]<=r` cannot be naively lowered from support considerations: they can be simultaneously attained.

## Source-package check

Status: **GAP (reproducibility/package only; no mathematical downstream impact on the pinned manuscript proof).** At pinned source commit `7c0d6e...`, the manuscript directory contains only `manuscript.tex`. On current `master` during this audit, `README.md` and `AUDIT.md` are present in addition to `manuscript.tex`, but `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json` are still absent, even though current `README.md` names them as canonical/reproducible files. I therefore could not independently run or inspect the claimed finite checker in this run. The complete proof text itself is present in `manuscript.tex`, and this packaging gap does not alter the mathematical argument audited below.

## Detailed audit

### `lem:rank` / `eq:rank-perturb` — source lines 162–181 — PASS

The approximation formula `s_j(T)=inf_{rank B<j}||T-B||` is the correct singular-value distance characterization for arbitrary real matrices. The Lipschitz estimate follows in both directions by the triangle inequality. If `rank R<=q`, adding `R` to a rank-`<j` approximant to `D` gives a rank-`<j+q` approximant to `D+R`, hence `s_{j+q}(D+R)<=s_j(D)`. No symmetry is needed, exactly as used later for `A-E=D+R`.

### `lem:completion` — source lines approximately 559–584 — PASS for the B09 rank/support statements

For an invertible disjoint seed `B=A[S,T]`, `P=A[:,T]B^{-1}A[S,:]` has rank at most `r`, agrees with `A` on rows `S`, and agrees with `A` on columns `T`. With `E[L,L]=off(A[L,L]-P[L,L])`, `D_ii=A_ii-P_ii` on `L`, and `D=0` on `S union T`, the residual `R=A-D-E` obeys `R[L,L]=P[L,L]`, hence `rank R[L,L]<=r`.

For `R-P`, rows `S` vanish, columns `T` vanish, and the whole `L x L` block vanishes. Every remaining entry is supported either in rows `T` or columns `S`. Splitting those two supports gives rank at most `r+r`; adding `rank P<=r` yields `rank R<=3r`. No symmetry of `P,R,E` is used. The condition `D=0` on the seed is exact and is essential later: every large diagonal entry forced in `D` lies in `L`.

### `prop:volume` — source lines approximately 585–621 — PASS

Assume a bad ratio `V_{r+1}<kappa V_r` with `1<=r<=4`. From `kappa=1/80^2`, `epsilon=||E||_F<=(r+1)/80<=1/16`. Let `m=4k-3`. Since `s_m(A)>=1` and `||E||<=epsilon`, singular-value Lipschitz continuity gives `s_m(D+R)=s_m(A-E)>=1-epsilon`. Using `rank R<=3r` gives `s_{m-3r}(D)>=s_m(D+R)>=1-epsilon`.

Because `r<=k-1`, `m=4k-3>=4r+1`, so `m-3r>=r+1`. Since `D` is diagonal, at least `r+1` of its entries have modulus at least `1-epsilon`; since `D=0` on `S union T`, all lie in `L`. Choose `H subset L`, `|H|=r+1`, among them.

On `H`, zero diagonal of `E` and the no-pivot bound give

`|R_ii| >= 1 - 1/16 - 1/100 = 371/400`.

For `i!=j`,

`|R_ij| <= |A_ij|+|E_ij| < 1/7+1/16 = 23/112`.

Since `r<=4`, each row has at most four off-diagonal entries, so

`sum_{j!=i}|R_ij| < 4*(23/112)=23/28`.

The exact strict slack is

`371/400 - 23/28 = 297/2800 > 0`.

Therefore `R[H,H]` is strictly row diagonally dominant and invertible, hence rank `r+1`, contradicting `rank R[H,H]<=rank R[L,L]<=r`.

The `r=0` branch is also sound: `V_1=||off A||_F^2<kappa`, while no pivot gives `||diag A||<eta`; hence `||A||<1/100+1/80<1`, contradicting any singular value at least one.

### `lem:cut` and `cor:no-pivot` — source lines approximately 623–651 — PASS for the spectral-to-analytic handoff

Each ordered disjoint `(S,T)` with `|S|=|T|=k` survives a fair coordinate cut with probability `2^{-2k}=4^{-k}`, so the expectation identity is exact. Combining `V_k>=kappa^k` with the cut gives `Z_k^{-1/(2k)}<=2kappa^{-1/2}=160`. Substitution into the manuscript's previously proved volume envelopes gives the stated `k=3` half-potential and `k=5` density constants. This B09 report does not independently certify the Fourier determinant theorem itself; see scope below.

## Counterexample stress test: the rank constants are simultaneously sharp as algebraic support bounds

Status: **OBSTRUCTION to a naive rank-constant improvement; not a counterexample to the 17-eigenvalue theorem and not a proof that 17 is optimal.**

Let

`C = 3 * [[0,1,1],[1,0,1],[1,1,1]]`.

Its eigenvalues are exactly `-3`, `3(1+sqrt(2))`, and `3(1-sqrt(2))`, so all have modulus greater than one. For any integer `m>=512`, replace each base coordinate by a disjoint bank of `m` physical coordinates and let `u_1,u_2,u_3` be the normalized flat bank vectors. Put `A_m=U C U^T`, `U=[u_1 u_2 u_3]`.

Then `A_m` has the same three nonzero eigenvalues as `C`. Every physical diagonal has modulus at most `3/m<1/100`; every principal `2 x 2` determinant has modulus at most `9/m^2<1/100`. Thus `A_m` has no `eta`-pivot.

Choose a one-coordinate seed `S={s}` in bank 1 and `T={t}` in bank 2. Then `B=A_st=3/m`. For any physical coordinate `ell` in bank 3,

`P_{ell,ell}=A_{ell,t} B^{-1} A_{s,ell}=(3/m)(m/3)(3/m)=3/m=A_{ell,ell}`.

In the associated completion, the `3 x 3` submatrix of `R` on `(s,t,ell)` is exactly `C/m`, hence invertible. Therefore `rank R>=3`; the support lemma gives `rank R<=3`, so `rank R=3`. Also `R[L,L]=P[L,L]` has rank one: it is at most one by construction, and the displayed nonzero diagonal entry makes it nonzero.

Taking a direct sum of `r` disjoint copies and choosing one such seed coordinate pair per copy gives an invertible `r x r` seed with

`rank R=3r`, and `rank R[L,L]=r`,

while the full physical matrix still has no `eta`-pivot and has `3r` eigenvalues of modulus greater than one. This does **not** assert that the chosen seed is the volume-sampled minimizer, so it does not show `prop:volume` is threshold-sharp. It does show that lowering 17 cannot be justified by simply changing `3r` to `2r` or the restricted `r` to `r-1` from support considerations alone.

## Why the present proof stops at 17 rather than 16

For the density branch `k=5`, the telescoping bad ratio can occur at `r=4`. The current proof with `s_17>=1` gives `17-12=5` large entries of `D`, producing a `5 x 5` diagonally dominant block of `R[L,L]` against its rank bound four. With only `s_16>=1`, the same argument gives `16-12=4` large entries. A `4 x 4` invertible block is compatible with `rank R[L,L]<=4`, so there is no contradiction. A rigorous 16-eigenvalue improvement needs new information specifically in this terminal `r=4` chamber, or must replace the order-five route analytically.

## End-to-end scope in this run

The full 790-line `manuscript.tex` was read from the pinned git blob. The B09-sensitive chain above was independently reconstructed and checked, and the main theorem's uses of the no-pivot consequences were checked for index consistency. I am **not** marking the remaining analytic sections independently validated in this run: the heat-flow proof of geometric Brascamp--Lieb, product-projection constants, regularized determinant proof, hyperbolic envelope, Riesz/half-potential normalization, and rough-law/Tonelli details remain `UNCHECKED` by this particular B09 review. This is therefore a scoped independent PASS, not an end-to-end review certificate.

## First unpaid implication

`QFORM-FIXEDMULT-R4-TERMINAL-SATURATION-v1`: in the no-pivot order-five bad-ratio chamber with `r=4`, determine whether the four large diagonal directions forced by `s_16>=1`, together with the exact sampling/interpolation identities, force additional crossing volume or another analytic receiver. A proof here would lower the current candidate threshold to 16; a source-valid counterexample would show that a different route is required.
