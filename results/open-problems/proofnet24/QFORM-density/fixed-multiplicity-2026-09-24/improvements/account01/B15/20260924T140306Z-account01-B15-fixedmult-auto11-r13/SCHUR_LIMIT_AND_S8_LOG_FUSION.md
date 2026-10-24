# account01/B15 r13 improvement — exact Schur-limit audit and half-potential/log fusion at the s8 frontier

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Pinned baseline commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Pinned manuscript blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Pinned SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`  
Status: **PROVED SUPPORTING RESULTS; multiplicity eight remains open.**

This note records two independent B15 conclusions. First, the pinned manuscript's singular Schur-complement paragraph is already rigorous; the later proposed fixed-threshold amendment is optional exposition, not a needed mathematical repair. Second, at the current multiplicity-eight two-anchor frontier, a full negative-half-potential bound for the Schur critical value completely cancels the small pair determinant from the logarithmic singularity of the hyperbolic-pair envelope. The only pair-determinant singularity left by that route is the nonlogarithmic tail term.

## 1. The moving-threshold Schur limit is valid as written

The baseline Lemma `lem:schur` states that for

`A=[[B,C],[C^T,D]]`, `det B !=0`, `S=D-C^T B^-1 C`,

one has

`N_S(t) >= N_A(t)-k`,  `k=dim B`.

The invertible case is already proved in the manuscript by applying principal-compression min-max to `A^-1` and `-A^-1`.

For singular `A`, choose `epsilon_m->0` so `A_m=A+epsilon_m I` is invertible and `|epsilon_m|<t`; for all sufficiently large `m`, `B+epsilon_m I` remains invertible. Let `S_m` be the corresponding Schur complement. Then

`S_m -> S` in operator norm,

and the elementary reverse triangle inequality for each eigenvalue of the scalar shift gives

`N_(A_m)(t-|epsilon_m|) >= N_A(t)`.

Apply the already-proved invertible Schur count at the positive threshold `t-|epsilon_m|`:

`N_(S_m)(t-|epsilon_m|) >= N_A(t)-k`.

Let

`q=N_A(t)-k`.

If `q<=0`, the result is empty. If `q>=1`, the preceding count is exactly

`s_q(S_m) >= t-|epsilon_m|`,

where `s_q` is the `q`-th largest eigenvalue modulus (equivalently singular value for a symmetric matrix). Weyl continuity gives

`s_q(S_m)->s_q(S)`.

Therefore

`s_q(S) >= lim_m (t-|epsilon_m|)=t`,

so `N_S(t)>=q`.

This is precisely the limiting inference compressed into manuscript lines 205–207. A moving threshold causes no loss because the inequality controls an **ordered modulus from below** and the threshold converges to `t`. Thus the literal pinned source is not mathematically dependent on the later fixed-`delta` rewrite.

## 2. General potential-to-logarithm transfer

### Lemma `QFORM-POTENTIAL-TO-LOG-v1`

Let `R` be any real random variable and let `0<beta<infinity`. Suppose

`H_beta := sup_a E |R-a|^(-beta) < infinity`.

Then for every `A>0`,

`boxed: sup_z E log_+( A/|R-z| ) <= (H_beta/beta) A^beta.`

For the B15 half-potential exponent `beta=1/2`,

`boxed: sup_z E log_+( A/|R-z| ) <= 2 H_(1/2) sqrt(A).`

### Proof

For `x>0`, layer cake gives

`log_+(A/x)=int_0^infinity 1_{x<A e^{-u}} du`.

Therefore, by Tonelli,

`E log_+(A/|R-z|)
 =int_0^infinity P{|R-z|<A e^{-u}} du.`

Markov applied to `|R-z|^{-beta}` gives

`P{|R-z|<r} <= H_beta r^beta`.

Substituting `r=Ae^{-u}` and integrating gives

`H_beta A^beta int_0^infinity e^{-beta u}du
 = (H_beta/beta)A^beta`.

No density or continuity of `R` is required.

## 3. Application to the indefinite-pair / Schur-collar interface

Take a literal original-coordinate indefinite principal pair `K` with

`det K=-D`, `D>0`.

After completing the square in that pair, let `R_K` denote its critical-value Schur remainder. The audited baseline hyperbolic-pair lemma gives, after averaging over the complement,

`p_Q(z)
 <= D^(-1/2) [ 6 + E log_+(16 sqrt(D)/|z-R_K|) ].`       (3.1)

Assume a full half-potential estimate

`H := sup_a E|R_K-a|^(-1/2) < infinity`.

Apply the lemma above with `A=16 sqrt(D)`. Since

`sqrt(16 sqrt(D))=4 D^(1/4)`,

we get

`E log_+(16 sqrt(D)/|z-R_K|)
 <= 8 H D^(1/4)`.

Substitution into (3.1) yields the dependency-safe fusion inequality

`boxed:
 p_Q(z) <= 6 D^(-1/2) + 8 H D^(-1/4)
}`                                                        (3.2)

for almost every `z`.

This estimate spends the half-potential **before** separating the logarithm into an additive `log_+(16 sqrt D)` plus a generic log potential. It is therefore the correct form for the small-determinant collar.

## 4. Exact cancellation using the current two-anchor Schur currency

The current account01/B08 two-anchor identity gives the following local currency in the unresolved `s_8` collar. Write

`M=A[S,T]`, `K=A[H,H]`, `D=|det K|`,

and

`gamma_* = 1-3 sqrt(2)/40 = 0.8939339828...`.

For `D>0`, the Schur complement after pivoting `H` has a literal order-two crossing satisfying

`|det S_K[S,T]| >= gamma_* |det M|/D`.

The completed order-two receiver consequently gives

`H = sup_a E|R_K-a|^(-1/2)
 <= C_2 gamma_*^(-1/4) D^(1/4) |det M|^(-1/4),`           (4.1)

where the conservative fully proved coefficient is

`C_2=8 sqrt(e) 2^(-1/8)=12.095072570796...`.

Insert (4.1) into the second term of (3.2):

`8 H D^(-1/4)
 <= 8 C_2 gamma_*^(-1/4) |det M|^(-1/4).`

Numerically,

`8 C_2 gamma_*^(-1/4) = 99.5112321381...`.

Hence

`boxed:
 p_Q(z)
 <= 6 D^(-1/2)
    +99.512 |det M|^(-1/4).
}`                                                        (4.2)

The important structural conclusion is not the numerical constant. It is that **the entire moving-critical-value logarithmic singularity has lost all negative power of the small physical pair determinant `D`.** The quarter-power gain supplied by the Schur order-two packet cancels it exactly.

Therefore the logarithmic critical singularity is *not* the remaining `s_8` obstruction for this local collar. What survives is the nonlogarithmic `6 D^(-1/2)` term in the current hyperbolic envelope, together with the separate aggregate/local issue that `|det M|` need not itself have a dimension-free lower bound.

## 5. Relation to the exact-zero anchor theorem and the real endpoint debt

A separate completed exact-zero theorem proves that when `K=0` exactly and the two-anchor outside cross map has row rank two, one can obtain a finite density cap directly from the affine receiver; thus the true law does not intrinsically have to blow up as `D->0` in every collar configuration.

Equation (4.2) shows where the present **method** is discontinuous at `D=0`: completion of an invertible indefinite pair leaves the coarse nonlogarithmic term `6D^(-1/2)`, while the logarithmic part is already neutralized by Schur currency. Any successful eight-direction overlap receiver should therefore target one of the following equivalent debts before local reciprocal payment:

1. replace the constant `6` in the pair envelope by a scale-sensitive term that can be integrated against the Schur packet;
2. interpolate directly between the exact-zero affine two-anchor receiver and the nonzero-curvature pair without completing the pair first; or
3. spend the aggregate `Xi_2/Omega_1` collar in a grouped product-Fourier receiver before selecting a possibly tiny local seed determinant.

The recent explicit six-coordinate collar with `K=0` and nontrivial two-sided wings confirms that extracting a conventional principal-pair pivot cannot solve this endpoint.

## 6. Threshold conclusion

This note does **not** prove multiplicity eight. The strongest complete theorem supported by the current repository remains multiplicity nine (with all original assumptions retained and multiple independent full reviews). The unrestricted three-eigenvalue conjecture remains open.

What is new here is a sharper analytic localization of the eight-direction obstruction:

- order-two Schur currency already pays the entire logarithmic critical-value singularity;
- the unresolved pair endpoint is the determinant-singular **nonlogarithmic tail/central term**, plus aggregate-to-local provenance;
- the baseline singular-Schur paragraph itself is sound and needs no mathematical repair.