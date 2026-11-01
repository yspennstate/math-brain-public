# fleet01/B08 r12 — threshold reduction review and two-anchor Schur currency

Run: `20260924T135201Z-fleet01-B08-fixedmult-r12`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Baseline manuscript: `7c0d6e60946b19423e6400a12d34b473cf0591e2`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

This report has three purposes:

1. state the strongest multiplicity reduction I can rigorously support after this audit;
2. independently reconstruct the nine-direction proof under the repaired Schur count rather than importing its headline;
3. add one exact structural identity for the remaining eight-direction collar.

It does **not** claim the unrestricted three-eigenvalue conjecture, and it does not claim global continuity.

## 1. Strongest threshold supported in this run: nine

The current repository contains the fleet03/B04 candidate theorem at

`8ff490c177d0cd7d6f33130f1431785e312a9d10`,

and independent end-to-end reconstructions by fleet01/B16 and fleet03/B08. I independently reconstructed the same threshold in this B08 run, but with the fixed-threshold repair of the baseline Schur lemma inserted explicitly.

### Theorem — fixed multiplicity nine, repaired-chain form

Let `X_1,...,X_n` be independent real random variables with densities bounded by `K`. Let `A=A^T` be arbitrary, and let `b,c` be arbitrary. If

` s_9(A)>=s>0`,

then `Q=X^TAX+b^TX+c` has an essentially bounded density. Retaining the current sharp constant ledger gives

` ||p_Q||_infinity < 2582 K^2/s.`

The no-pivot branch has a `C_0` density. Global continuity is not asserted.

### Proof, normalized case `K=s=1`

Keep the manuscript parameters

`eta=1/100`, `kappa=1/80^2`.

#### 1.1 No physical pivot

The repaired baseline spectral-to-volume proposition is unchanged. At order `k=3` its multiplicity requirement is exactly

`4k-3=9`.

Therefore `s_9(A)>=1` and absence of an `eta`-pivot imply

`V_3(A)>=kappa^3`.

A fair original-coordinate cut captures each ordered disjoint three-minor with probability `4^-3`, so there is a literal physical crossing block `M` with

`E_3(M)=e_3(MM^T)>=4^-3 kappa^3`.

The completed marginal-free third-compound crossing theorem applies to the **full** quadratic form, retaining arbitrary same-bank quadratic and affine terms. In its sharp completed form,

`||p_Q||_infinity <=6^(4/3) E_3(M)^(-1/6)`.

Since `(4^-3 kappa^3)^(-1/6)=160`, this branch is `<1745` and has a continuous `C_0` representative. The self-contained B04 compiler gives a slightly larger but still `<2400` constant; either version closes the branch.

#### 1.2 Scalar pivot

Suppose an original coordinate `h` has `|A_hh|>=eta`. Completing the square only in that original coordinate gives the measure profile

`p_Q(z)<=|A_hh|^-1/2 E|z-R|^-1/2`,

where the quadratic matrix of `R` is the principal Schur complement. By the **repaired** Schur spectral-count lemma,

`N_R(1)>=N_A(1)-1>=8`.

If the Schur complement itself has an `eta`-pivot, the sharpened pivot half-potential calculation below gives

`sup_a E|R-a|^-1/2 <258.2`.

If the Schur complement has no `eta`-pivot, then in particular `s_5(R)>=1`. The baseline volume theorem at order two gives `V_2(R)>=kappa^2`, and a fair physical cut yields

`Z_2>=4^-2 kappa^2`.

The completed row-marginal-free two-volume collision theorem gives

`sup_a E|R-a|^-1/2 <= C_2 Z_2^-1/8`,

with the sharp completed coefficient

`C_2=8*2^(3/8)=10.3747164372...`.

Here `Z_2^-1/8<=sqrt(160)`, so this is `<132`, again below `258.2`.

Thus the outer scalar profile costs at most `eta^-1/2=10`, giving `<2582`.

#### 1.3 Definite two-coordinate pivot

If a physical principal two-by-two pivot is definite with determinant modulus at least `eta`, the direct two-dimensional density calculation gives

`||p_Q||_infinity <=pi/sqrt(eta)=10pi<32`.

No Schur density theorem is needed.

#### 1.4 Indefinite two-coordinate pivot

If the physical pair is indefinite with determinant modulus at least `eta`, its principal Schur complement retains at least seven unit spectral directions by the repaired count. In particular it retains one unit operator-norm direction. The baseline hyperbolic-pair plus logarithmic-potential argument therefore applies unchanged and gives `<251` in the normalized problem.

These four branches are exhaustive.

### Exact constant ledger for the scalar-pivot branch

The current sharpened pivot proof uses the exact singular-convolution envelope

`J(d)<=pi+4 log 2+2 log_+(1/|d|)`

and the certified quarter-power coefficient

`2^(5/8) pi^(-1/4) e^(3/8) Gamma(3/8)<174933/40000`.

With the rational certificates

`log 2<1733/2500`,

`log(174933/40000)<73777/50000`,

and `pi<22/7`, the logarithmic potential obeys

`L_log<4+4*(73777/50000)`.

Hence the truncated half potential at a scalar pivot is bounded by

`10*(22/7+4*(1733/2500)+2*(4+4*(73777/50000)))`

`=1125249/4375=257.1997714...`.

Adding the outside tail costs at most one:

`H_full<1129624/4375=258.1997714...`.

Multiplication by the outer scalar-pivot factor `10` gives

`2259248/875=2581.997714...<2582`.

All other normalized branches are smaller.

### Scaling

Put `Y=KX` and

`Q_tilde=Y^T(A/s)Y+(K/s)b^T Y+(K^2/s)c=(K^2/s)Q`.

The coordinates of `Y` have density cap one and `s_9(A/s)>=1`; scalar density scaling therefore gives

`||p_Q||_infinity<2582 K^2/s`.

No Gaussianity, support, moment, log-concavity, sign, diagonal-basis or post-rotation-independence hypothesis entered.

## 2. Review state of the nine-direction result

Mathematically, the nine-direction argument has now been reconstructed end to end by multiple distinct slots, including fleet01/B16, fleet03/B08, and this fleet01/B08 run. However, the baseline manuscript blob they inherit still contains the singular-Schur limiting paragraph identified as a repairable GAP in this run and independently by fleet01/B18.

Accordingly I do **not** label the current canonical source independently validated. The safe release path is:

1. patch `lem:schur` with the fixed-threshold proof from the audit report;
2. place the nine-direction theorem in a canonical source blob;
3. have two genuinely separate reviewers pin and approve that exact patched blob.

Until then, `s_9` is the strongest rigorously supported mathematical reduction, but release/validation status should remain distinct from the theorem-level argument.

## 3. Why the interpolation bookkeeping itself cannot lower nine

The B08 exact normal form from the audit shows that `rank R<=3r` and `rank R[L,L]<=r` are simultaneously sharp. For order-three volume, the terminal bad seed has `r=2`. Under only eight large eigenvalues, global rank subtraction can force only two large diagonal residual coordinates, while restricted rank two can accommodate a nonsingular two-by-two block. Thus the diagonal-dominance contradiction that proves the nine threshold does not fire at eight.

This is not evidence that eight is false; it proves only that a rank-count retuning is insufficient.

## 4. Existing eight-direction collar and a new B08 exact identity

The current fleet03/B04 eight-direction structural theorem says that in the no-pivot `s_8>=1` chamber, either the order-three disjoint volume is already target-scale and the density is paid, or one reaches a quantitative two-anchor collar. For a good order-two seed `S,T`, `|S|=|T|=2`, there are two anchor coordinates `H={h_1,h_2}` in the residual set with the completion

`A=D+R+E`,

`R[L,L]=P[L,L]`,

`P=A[:,T] A[S,T]^-1 A[S,:]`,

and

`|D_h|>=1-epsilon_*`,  `||E||<=epsilon_*`,

where

`epsilon_*=3 sqrt(2)/80=0.0530330085...`.

The same collar also gives the two-sided determinant currency in the blocks from `S` to `H` and from `H` to `T`.

The following exact identity is useful for the still-unpaid pair-pivot chamber.

### Lemma — two-anchor Schur blow-up identity

Put

`M=A[S,T]`,

`B=A[S,H]`,

`C=A[H,T]`,

`K=A[H,H]`,

and

`P_H=C M^-1 B=P[H,H]`.

Then

`K-P_H=(D+E)[H,H]`.

Because `D` is diagonal, `diag E=0`, both selected diagonal entries satisfy `|D_h|>=1-epsilon_*`, and every entry of `E[H,H]` has modulus at most `epsilon_*`,

`|det(K-P_H)|`

`>= (1-epsilon_*)^2-epsilon_*^2`

`=1-2 epsilon_*`

`=:gamma_*`

`=1-3 sqrt(2)/40`

`=0.8939339828...`.

Now assume `det K !=0` and let `S_K` be the principal Schur complement after pivoting the physical pair `H`. Its `S x T` block is

`S_K[S,T]=M-B K^-1 C`.

Sylvester's determinant identity gives the **exact** formula

`det(S_K[S,T])`

`=det M * det(I-M^-1 B K^-1 C)`

`=det M * det(I-K^-1 C M^-1 B)`

`=det M * det(K-P_H)/det K`.

Therefore

`|det(S_K[S,T])| >= gamma_* |det M|/|det K|`.            (4.1)

No approximation is present in (4.1).

### Consequence — critical two-volume half-potential currency

Choose any physical cut of the residual coordinates placing `S` on one side and `T` on the other. The crossing block of the Schur quadratic has a two-by-two minor `S_K[S,T]`, hence its two-volume satisfies

`Z_2 >= |det(S_K[S,T])|^2`.

Applying the completed row-marginal-free critical two-volume theorem gives, for the Schur remainder `R_K`,

`sup_a E|R_K-a|^-1/2`

`<= C_2 Z_2^-1/8`

`<= C_2 gamma_*^-1/4 |det K|^1/4 |det M|^-1/4`,

where `C_2=8*2^(3/8)`. Numerically,

`C_2 gamma_*^-1/4 <10.670`.                                  (4.2)

Thus the dangerous small physical pair determinant produces an **equal and opposite quarter-power gain** in the Schur remainder's half-potential. This is genuine new currency: the collar is not merely saying that some wings are large; after pivoting the two physical anchors, it forces a target residual two-volume that grows like `|det K|^-2` at the determinant level.

## 5. Why this does not yet prove multiplicity eight

Equation (4.2) isolates the missing analytic implication very sharply. To close the pair-pivot branch uniformly as `det K ->0`, one needs a dependency-safe physical-pair receiver that can spend the `|det K|^(1/4)` half-potential gain without reintroducing a worse factor.

The manuscript's present indefinite-pair envelope contains a coarse `|det K|^-1/2` constant term. Combining that bound naively with (4.2) still loses a negative quarter-power. The definite-pair `L^infinity` bound has the same issue. At `det K=0`, the Schur identity itself must be replaced by a rank-one/zero-pair argument.

So the exact next target is a **two-anchor pair/critical-E2 fusion theorem** which retains the dependence between the translated physical pair and its Schur remainder; one may not simply convolve conditional suprema or assume independence after completing the pair.

I therefore do **not** claim `s_8` in this run. The current rigorous threshold is nine, and multiplicity eight remains open at the explicit collar/fusion step above.

## 6. Status

- baseline exact source: `GAP (repairable)` because of the singular Schur paragraph;
- baseline theorem with repair inserted: `PASS` in this B08 review;
- strongest mathematically supported multiplicity reduction: `9`, with essential density `<2582 K^2/s`;
- multiplicity `8`: `OPEN`, reduced further here by (4.1)–(4.2);
- global continuity: `OPEN` outside the Fourier-integrable branches;
- unrestricted three-eigenvalue conjecture: `OPEN`.
