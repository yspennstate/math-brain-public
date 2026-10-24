SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B01, 2026-09-22T21:05:23Z.
attacking: the zero/near-isotropic physical-pivot branch via an exact singular-pair row gate plus dependence-safe square smoothing.

# QFORM account02/B01 r27 — singular physical pair plus transverse row

Status: `ESSENTIAL_STEP_APPLIED / CANDIDATE_REFUTED / FULL_TARGET_OPEN / WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and source state

Target: for arbitrary dimension, independent real coordinates with probability densities bounded by one, and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove a universal finite essential bound for the density of `Q=X^T A X`, or give a target-valid counterexample. No moment, support, log-concavity, Gaussianity, diagonal-basis, or post-rotation independence assumption is used below.

Fresh controls were read from `yspennstate/math-research-brain`; startup main was `42bec6f16eedcf68865159f35a82ebc92e54ddaa`, and the pre-write refresh was `76e129ce7679d60145bcb175da42011e59b5c700`. OWNER CONTROL remained revision `2026-09-22.15`, QFORM-only, with no pause for account02/B01. I consumed the current corrections: law-uniform pointwise Fresnel decay is false; arbitrary-joint rank-three coarea is false; positive moments of full conditional projection heights are not dimension-free; worst scalar-remainder conditioning `sup_b` is false; absolute Fourier `L^1` is not the correct universal interface; fixed good physical minors are not forced.

The immediately preceding B01 result (`math-open-problems@b3f18a11f29e878b69278f6487fe50b4e3380d99`) supplied a leakage-safe bank-overlap identity but left a three-bank synthesis debt. This run changes mechanism inside the same target: it attacks the owner-highlighted zero/near-isotropic physical-pivot branch and uses the fresh designated partner account03/B01 result.

## 2. Source-pinned partner inputs actually applied

### 2.1 Exact-zero row all-`L^p` theorem

From account03/B01 r18, canonical source

`yspennstate/math-open-problems@7acff3e983f6e6a3ede04ecbaf8405a3ce4ee8e2`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B01/account03-B01-20260922T202731Z-r18/REPORT.md`:

If `X` is independent of `(U,R)`, `f_X<=1`, and `p_U<=M`, then for

`T=2 X U+R`

and every `1<p<infinity`,

`||p_T||_p <= p M^(1-1/p)`.                                      (2.1)

For a physical zero-diagonal row whose off-diagonal coefficient vector has Euclidean norm `sigma`, the same source uses the product-projection bound

`M <= sqrt(2)/sigma`.                                            (2.2)

No dependence restriction between `U` and `R` is imposed.

### 2.2 Dependence-safe square smoother

From account03/B01 r12, canonical source

`yspennstate/math-open-problems@a80bb254a3a1e2883cbfabdf03b53919d6621990`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B01/20260922T142626Z-account03-B01-qform-r12/REPORT.md`:

If `R` has density `h in L^p`, `p>2`, and the conditional law of `V|R=r` has density at most one, then

`||p_(R+dV^2)||_infinity <= K_p |d|^(-1/2) ||h||_p^(p/[2(p-1)])`, (2.3)

where at `p=3`

`K_3=2 sqrt(pi)/3^(1/4)`.                                       (2.4)

This theorem explicitly permits dependence between `R` and `V`; the only requirement is the conditional cap.

### 2.3 Signed Fejer interface

I also read the underlying completed account04/B01 theorem

`yspennstate/math-open-problems@a3693ed6d50e8e4143b2f33bf997c5de2cb52d79`,
`proofnet24/QFORM-density/fleet-2026-09-22/account04/B01/20260922T141507Z-b01-qform-fejer-r1/REPORT.md`.

For any law `mu`, a uniform bound on its signed Fejer averages `D_T mu(y)` is equivalent to a bounded density, and for a bounded density

`||p_mu||_infinity = sup_(T,y) D_T mu(y)`.                     (2.5)

Thus every density bound proved below is simultaneously an averaged-frequency replacement and does not invoke absolute Fourier integrability.

## 3. New theorem: exact singular physical pair with transverse Schur row

### Theorem 3.1 — `QFORM-SINGULAR-PAIR-TRANSVERSE-SMOOTHER-v1`

Let `A` be any real symmetric `n x n` matrix and let `X_1,...,X_n` be independent with probability densities bounded by one. Fix distinct physical coordinates `i,k`. Put

`a=A_ii`, `b=A_ik`, `d=A_kk`,

assume

`d != 0`,                                                      (3.1)
`a d-b^2=0`.                                                   (3.2)

Let `J={1,...,n}\{i,k}` and define the transverse Schur-row coefficient vector

`c_j=A_ij-(b/d) A_kj`, `j in J`,                              (3.3)

with

`sigma=(sum_(j in J) c_j^2)^(1/2)`.                           (3.4)

If `sigma>0`, then the full ambient quadratic form `Q=X^T A X`, with every residual coefficient and coupling retained, has an essentially bounded density satisfying

`boxed: ||p_Q||_infinity
 <= 2^(5/4) sqrt(3 pi) (|d| sigma)^(-1/2)
 < 7.302 (|d| sigma)^(-1/2).`                                 (3.5)

No matrix-rank assumption is made. In particular, arbitrary additional large or small eigenvalues and arbitrary quadratic couplings within the remaining coordinates are allowed. Continuity is not claimed.

### Proof

Rename `X=X_i`, `V=X_k`, and `Z=(X_j)_(j in J)`. Write

`u(Z)=sum_(j in J) A_ij Z_j`,
`w(Z)=sum_(j in J) A_kj Z_j`,
`R(Z)=Z^T A_(J,J) Z`.                                         (3.6)

Then exactly

`Q=aX^2+dV^2+2bXV+2Xu(Z)+2Vw(Z)+R(Z)`.                       (3.7)

Complete the square only in the original physical coordinate `V`:

`Q=d [V+(bX+w)/d]^2
  +(a-b^2/d)X^2
  +2X[u-(b/d)w]
  +R-w^2/d`.                                                  (3.8)

The singular-pair identity (3.2) cancels the scalar `X^2` coefficient exactly. Define

`U=u-(b/d)w=sum_(j in J)c_j Z_j`,                              (3.9)
`R'=R-w^2/d`,                                                  (3.10)
`S=2 X U+R'`,                                                  (3.11)
`V'=V+(bX+w)/d`.                                               (3.12)

Hence

`Q=S+d(V')^2`.                                                 (3.13)

Because `X` is an original coordinate and `U,R'` are functions only of `Z`, `X` is independent of `(U,R')`. By (2.2), since `sigma>0`,

`||p_U||_infinity <= M:=sqrt(2)/sigma`.                       (3.14)

Apply account03/B01 r18 at `p=3`:

`||p_S||_3 <= 3 M^(2/3)`.                                     (3.15)

It remains to verify the only nontrivial hypothesis needed for the dependence-safe square theorem. Let `G=sigma(X,Z)`. The original `V` is independent of `G` and has density `f_V<=1`; both `S` and the shift

`H=(bX+w(Z))/d`                                                (3.16)

are `G`-measurable. Given `S=s`, the regular conditional law of `H` is some probability kernel `nu_s`. Therefore the conditional density of `V'=V+H` is the mixture

`g_s(v)=int f_V(v-h) nu_s(dh) <=1`.                           (3.17)

Thus account03/B01 r12 applies to (3.13). Using (2.4) and (3.15),

`||p_Q||_infinity
 <= [2 sqrt(pi)/3^(1/4)] |d|^(-1/2)
    [3 M^(2/3)]^(3/4)
 = 2 sqrt(3 pi) M^(1/2)|d|^(-1/2).`                          (3.18)

Substitution of (3.14) gives

`2 sqrt(3 pi) (sqrt(2)/(sigma |d|))^(1/2)
 =2^(5/4) sqrt(3 pi)(sigma |d|)^(-1/2)`,                      (3.19)

which is (3.5). QED.

### Signed-frequency corollary

By (2.5), the same constant controls the exact signed Fejer quantity:

`sup_(T>0,y) D_T law(Q)(y)
 <=2^(5/4)sqrt(3pi)(|d|sigma)^(-1/2)`.                         (3.20)

Thus the result is an averaged/distributional replacement at a point where the false law-uniform pointwise Fresnel estimate is unavailable.

## 4. Why this fills a genuine local analytic gap

For a physical symmetric `2x2` pair `B=[[a,b],[b,d]]` with `d!=0`, the determinant trichotomy is now:

* `det B>0`: `B` is definite, and the completed account04/B01 physical-plane theorem gives a bounded density with cost `pi/sqrt(det B)`.
* `det B<0`: `B` is invertible indefinite, and the completed full-matrix pair-log theorem gives a bounded density with its quantitative `(D,kappa,s_3(A))` cost.
* `det B=0`: neither reciprocal determinant theorem applies. Theorem 3.1 supplies a finite bound whenever the Schur-transverse row `c` is nonzero.

The new theorem therefore pays the exact singular boundary rather than hiding it inside an inverse determinant. It also retains all outside couplings: the Schur correction `R-w^2/d` is allowed to depend arbitrarily on the same coordinates that generate `U`.

## 5. Near-singular continuation by the same `L^3` row mechanism is false

A tempting continuation would be: after (3.8), if the Schur scalar

`delta=a-b^2/d`                                                (5.1)

is merely small rather than exactly zero, perhaps the row variable

`S_delta=delta X^2+2XU+R`                                     (5.2)

still has a uniform `L^p` density for some `p>2`, allowing the same dependence-safe square smoother. This is false under the row hypotheses alone for every `delta!=0`.

Take independent `X,U ~ Uniform[-1/2,1/2]` and set

`R=U^2/delta`.                                                 (5.3)

Then

`S_delta=delta (X+U/delta)^2`.                                (5.4)

The random variable `Y=X+U/delta` has a continuous density with

`p_Y(0)=min(1,|delta|)>0`.                                    (5.5)

Consequently the square pushforward has the usual inverse-square-root singularity:

`p_(S_delta)(s) ~ p_Y(0)/sqrt(|delta| |s|)`                    (5.6)

on the appropriate one-sided neighborhood of zero. Hence

`p_(S_delta) notin L^2`, and in particular no `L^p`, `p>2`, estimate can follow from the nonzero-pivot row assumptions alone. This is a falsifier of that intermediate continuation, not a QFORM counterexample. The full target may and often does spend other spectral directions to remove the singularity.

This explains the discontinuity between the exact singular branch (3.5) and the current near-singular debt: at `delta=0`, the bilinear row has all finite `L^p`; for every nonzero `delta`, arbitrary residual dependence can recreate a square singularity. A successful near-singular theorem must use additional product/spectral currency rather than perturb Theorem 3.1 through `delta=0`.

## 6. Consequence for the full proof programme

The full conjecture remains OPEN. The new theorem does not prove that the three-large-eigenvalue hypothesis forces a physical singular pair with `|d| sigma` bounded below. Known high-cardinality bank examples prevent replacing the global problem by one uniformly good fixed pair/minor.

The first unpaid implication is now sharpened to

`QFORM-NEAR-SINGULAR-PAIR-AGGREGATION-v1`:

> In the global heavy/diffuse reduction, when every usable physical pair has very small determinant but not exactly zero, aggregate several Schur-transverse row resources (or use ridge/grouped coordinates) before paying any reciprocal determinant, so the third spectral direction is spent before the nonzero-pivot square singularity of Section 5 forms.

This is the precise bridge between the full-matrix pair theorem (`det B<0` with reciprocal determinant cost), Theorem 3.1 (`det B=0` with transverse-row cost), and the ridge/diffuse high-cardinality branches. A fixed-pair continuity argument is ruled out by Section 5.

## 7. Phase-aligned counterexample preserved

For completeness, none of the above revives the refuted pointwise oscillatory estimate. For any prescribed `s!=0` and small `eta>0`, choose a measurable set of measure one inside

`{x: dist(s x^2,2pi Z)<=eta}`

and use its indicator as a density. Then `Re E exp(i s X^2)>=cos eta`. The new result uses the partner's distributional `L^3` row estimate and the signed Fejer equivalence; it makes no law-uniform pointwise decay claim.

## 8. Exact regression

`CHECK.py` checks the Schur identity (3.8) on exact rational test points and the constant simplification in (3.18)-(3.19). Its captured output is in `CHECK_OUTPUT.txt` and ends with the numerical constants

`K3=2.6935473741771965`,
`combined=6.13996024767893`,
`physical_constant=7.301684412373654`.

The computation is regression evidence only; the proof above is symbolic.

## 9. Status

`ESSENTIAL_STEP_APPLIED`: proved a new arbitrary-rank, arbitrary-residual density/Fejer theorem at the exact singular physical-pair boundary by directly composing two completed account03/B01 results.

`CANDIDATE_REFUTED`: the same `L^p`, `p>2`, row mechanism cannot be continued to any nonzero Schur scalar without spending additional hypotheses.

`FULL_TARGET_OPEN`: no claim is made that the bare three-large-eigenvalue condition forces the new certificate, and no full end-to-end proof or two independent reviews exist.
