SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B01, 2026-09-22T22:57:25Z.
attacking: the rank-one Schur-residual endpoint by averaging the physical-pair logarithm against a first-exterior-mass fractional potential before any single-minor reciprocal is paid.

# fleet03/B01 r20 — rank-one Schur residual via logarithmic potential

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `fleet03-B01-20260922T225725Z-r20`  
**Assignment:** Oscillatory replacement / FOURIER  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Start control:** `yspennstate/math-research-brain@e3e5003a8f11d307b56ece80a3ab42070833a9c1`  
**Prepublication control:** `yspennstate/math-research-brain@363bb1062638754a59cdd0cd443047efed15a7ad`  
**Status:** `ESSENTIAL_STEP_APPLIED / RANK-ONE-SCHUR ANALYTIC OBSTRUCTION PAID / FULL_TARGET_OPEN`  
**Continuity:** essential boundedness is proved in the new branch; continuity is not proved by this argument.

## 1. Exact target and correction boundary

The target remains the full owner conjecture: for every finite `n`, every independent real vector `X=(X_1,...,X_n)` whose coordinate densities satisfy `0<=f_i<=1`, and every real symmetric `A` having at least three eigenvalues of modulus at least one, prove that `Q=X^TAX` has a density with one universal finite `L^infinity` bound, or give a valid target counterexample.

No moment, Gaussian, log-concavity, compact-support, connected-support, identical-law, centering, or diagonal-basis assumption is made here. No spectral rotation is used on the random source. The live corrections remain in force: bounded density does not imply law-uniform pointwise quadratic-phase decay; arbitrary conditional projection caps can diverge; a single good physical minor is not forced; and absolute Fourier/Wiener estimates are not a universal interface. The phase-aligned fragmented-support counterexample to pointwise Fresnel decay is therefore preserved rather than repaired away.

The mechanism below is instead a distribution-function / averaged-frequency replacement. A physical indefinite pair has only a logarithmic saddle singularity. The logarithm is averaged against a **fractional potential of the entire exact Schur remainder**, and that fractional potential is obtained from the aggregate first exterior mass of an original-coordinate cross block. The key new point is that this pays the genuinely rank-one residual bank which the newest B09 endpoint leaves open.

## 2. Source-pinned inputs actually used

### 2.1 Physical indefinite-pair logarithmic envelope

Source:

`yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`

`proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.

For two original independent cap-one coordinates whose physical principal block `P` is invertible indefinite, set

`D=|det P|`, `kappa=sigma_min(P)>0`.

After exact completion of those two coordinates, let `R` be the moving critical value determined by all remaining original coordinates. The source theorem gives, for every `r>0`, uniformly in all permitted outside conditioning,

`p_Q(t) <= 2sqrt(2)/r
          +D^(-1/2) E log_+(2r^2/(kappa |t-R|)).`                 (2.1)

All affine shifts of the endpoint pair are already included in (2.1).

### 2.2 Aggregate fractional-Riesz theorem

Source:

`yspennstate/math-open-problems@7df1461e33f7ea4e6026a650391822a16e56e987`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B01/fleet03-B01-20260922T205456Z-r19/REPORT.md`.

For any quadratic-plus-affine form `R` in independent cap-one original coordinates and any physical cross block `C` across disjoint original-coordinate sets, write

`E_k=e_k(CC^T)`.

For

`0<alpha<min(1,k/4)`

the proved theorem gives

`H_alpha(R):=sup_s E|R-s|^(-alpha)
 <= C_(alpha,k) E_k^(-alpha/(2k)),`                              (2.2)

where

`C_(alpha,k)
 = ((pi e/2)^alpha /(2k Gamma(alpha) cos(pi alpha/2)))
   *Beta(alpha/(2k),1/8-alpha/(2k)).`                            (2.3)

This theorem comes from the source-valid regularized determinant estimate and retains arbitrary same-side quadratic curvature, affine terms, signs, outside couplings, and extra spectrum. It does not use the false one-dimensional pointwise Fresnel estimate.

For `k=1`,

`E_1=tr(CC^T)=||C||_F^2`.                                       (2.4)

Thus every **nonzero** original-coordinate cross block, even one of exact rank one, supplies a positive fractional potential.

### 2.3 Fresh B09 endpoint which identifies the unpaid rank-one obstruction

Fresh source:

`yspennstate/math-open-problems@77b5307b899cf99953a7b6c81bb41f94c92ff53d`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B09/B09-20260922T224934Z-r18/REPORT.md`.

That report proves finite-`L^p` smoothing of an indefinite endpoint pair and closes the case in which its exact Schur residual has a quantitative rank-two original-coordinate cross block. It explicitly leaves as its analytic endpoint a genuinely rank-one residual bank operator with arbitrary self curvature. The theorem below pays precisely that analytic endpoint whenever the endpoint pair and the nonzero rank-one strength are quantitatively exposed; it does not claim the structural theorem which would force such an exposed packet from the bare three-eigenvalue hypothesis.

### 2.4 Designated partner fleet04/B01

Source:

`yspennstate/math-open-problems@a3693ed6d50e8e4143b2f33bf997c5de2cb52d79`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B01/20260922T141507Z-b01-qform-fejer-r1/REPORT.md`.

For every probability law `mu`, fleet04/B01 proves the exact signed-Fejer identity

`||p_mu||_infinity = sup_(T>0,y) D_T mu(y)`                     (2.5)

when the left side is finite, with `+infinity` otherwise. Here

`D_T mu(y)
 =(1/(2pi)) int_(-T)^T (1-|t|/T)
 Re(e^(-ity) phi_mu(t)) dt.`                                    (2.6)

Section 7 applies this result to the new inequality.

## 3. First new lemma: a first-exterior fractional potential

Take `k=1` and `alpha=1/8` in (2.2). Put

`F:=||C||_F>0.`                                                  (3.1)

Since `E_1=F^2`,

`H_(1/8)(R)
 <= C_R F^(-1/8),`                                              (3.2)

where

`C_R
 = ((pi e/2)^(1/8)/(2 Gamma(1/8) cos(pi/16)))
   *Beta(1/16,1/16)
 =2.5808760822164343483... .`                                   (3.3)

This is already the key rank-one fact. If `C` has exact rank one, then its sole nonzero singular value equals `F`, so (3.2) supplies a translation-uniform fractional potential without any second singular direction.

For completeness, the regularized-determinant source behind (3.2) has the unconditional bound

`|phi_R(t)|
 <=det(I+4t^2 CC^T/(pi^2 e^2))^(-1/8)
 <=(1+4F^2t^2/(pi^2 e^2))^(-1/8).`                              (3.4)

Equation (3.2) is the rigorous distributional Riesz consequence of this complete-form estimate, not a pointwise bound on an individual one-dimensional quadratic phase.

## 4. New theorem A: algebraic-power payment of an arbitrary nonzero Schur cross bank

### Theorem 4.1 — `QFORM-PAIRLOG-E1-FRACTIONAL-PAYMENT-v1`

Let two original input coordinates form an invertible indefinite physical endpoint block `P`, with

`D=|det P|>0`, `kappa=sigma_min(P)>0`.                            (4.1)

Complete those two coordinates exactly. Suppose the exact quadratic-plus-affine Schur remainder `R` has **any** nonzero original-coordinate cross block `C` across disjoint residual coordinate sets, and put

`F=||C||_F>0`.                                                   (4.2)

Then the full ambient quadratic form has an essentially bounded density satisfying

`boxed(
 ||p_Q||_infinity
 <= C_pow D^(-2/5) kappa^(-1/10) F^(-1/10),
)`                                                              (4.3)

where

`C_pow
 = K_(1/8) C_R^(4/5)
 =11.020064487209148... <11.021`                                (4.4)

and

`K_(1/8)
 =(5/4)(1/4)^(-1/5)(2sqrt(2))^(1/5)
   [2^(1/8)/((1/8)e)]^(4/5)
 =5.161434419339742... .`                                       (4.5)

No rank, leverage, support, sign, self-block, or additional-spectrum hypothesis is imposed on the Schur remainder beyond `F>0`.

#### Proof

The logarithm-to-fractional-Riesz compiler proved in the preceding B01 report states that for any `0<alpha<1`, if

`H_alpha=sup_t E|R-t|^(-alpha)<infinity`,

then (2.1) implies

`||p_Q||_infinity
 <=K_alpha
   D^(-1/[2(2alpha+1)])
   kappa^(-alpha/(2alpha+1))
   H_alpha^(1/(2alpha+1)),`                                     (4.6)

with

`K_alpha=(2alpha+1)(2alpha)^(-2alpha/(2alpha+1))
          (2sqrt(2))^(2alpha/(2alpha+1))
          [2^alpha/(alpha e)]^(1/(2alpha+1)).`                   (4.7)

Apply (4.6) at `alpha=1/8`. Then

`1/[2(2alpha+1)]=2/5`,
`alpha/(2alpha+1)=1/10`,
`1/(2alpha+1)=4/5`.                                              (4.8)

Insert (3.2). Since `(F^(-1/8))^(4/5)=F^(-1/10)`, equations (4.3)-(4.5) follow. Absolute continuity comes from the conditional endpoint-pair density formula and Tonelli. QED.

### Exact rank-one corollary

If the Schur cross block has exact rank one, with sole singular value `Theta>0`, then `F=Theta`, so

`boxed(
 ||p_Q||_infinity
 <11.021 D^(-2/5) kappa^(-1/10) Theta^(-1/10).
)`                                                              (4.9)

This closes the **analytic** rank-one residual-bank endpoint left in fleet01/B09 r18. The remaining problem there is structural: force quantitative endpoint resources `D,kappa,Theta`, or route a degenerate packet elsewhere.

## 5. New theorem B: logarithmic rather than algebraic loss in the rank-one strength

The power estimate (4.3) is convenient but it spends the fractional moment through the elementary inequality `log(L/x)<=const*x^(-alpha)`. Keeping the layer-cake integral one step longer replaces the algebraic `kappa`/`F` losses by a logarithm.

### Lemma 5.1 — uniform logarithmic potential from `E_1`

Under the hypotheses of Section 3, for every `L>0`,

`boxed(
 sup_t E log_+(L/|R-t|)
 <= 8 C_R + log_+(L/F).
)`                                                              (5.1)

Numerically `8C_R=20.647008657731475...`.

#### Proof

For every nonzero `x`,

`log_+(L/|x|)
 =int_0^infinity 1_{|x|<L e^(-s)} ds.`                           (5.2)

By Markov applied to (3.2), for every `rho>0`,

`P(|R-t|<rho)
 <=min(1,C_R (rho/F)^(1/8)).`                                   (5.3)

Put `z=L/F` and `B=C_R z^(1/8)`. Tonelli and (5.2)-(5.3) give

`E log_+(L/|R-t|)
 <=int_0^infinity min(1,B e^(-s/8)) ds.`                         (5.4)

The last integral equals `8B` for `B<=1` and `8(1+log B)` for `B>=1`. Since `C_R>1`, both cases obey

`int_0^infinity min(1,B e^(-s/8)) ds
 <=8C_R+log_+ z.`                                                (5.5)

This is (5.1). QED.

### Theorem 5.2 — `QFORM-PAIRLOG-E1-LOGARITHMIC-PAYMENT-v1`

Under the hypotheses of Theorem 4.1,

`boxed(
 ||p_Q||_infinity
 <=D^(-1/2)
   [ C_log + log_+(4D/(kappa F)) ],
)`                                                              (5.6)

where

`C_log:=2+8C_R
 =22.647008657731475... <22.648.`                               (5.7)

#### Proof

Apply Lemma 5.1 to (2.1) with

`L=2r^2/kappa`.

For every `r>0`,

`p_Q(t)
 <=2sqrt(2)/r
   +D^(-1/2)[8C_R+log_+(2r^2/(kappa F))].`                       (5.8)

Choose the scale-correct deterministic value

`r=sqrt(2D).`                                                    (5.9)

Then the first term is `2D^(-1/2)` and the logarithm has argument `4D/(kappa F)`. This proves (5.6). QED.

### Scaling audit

If the full coefficient matrix is multiplied by `lambda`, then

`D -> lambda^2 D`, `kappa -> |lambda| kappa`, `F -> |lambda|F`.

The logarithm in (5.6) is invariant, while `D^(-1/2)` scales as `|lambda|^(-1)`, exactly the density scaling. In (4.3), the total exponent is likewise

`|lambda|^(-4/5)|lambda|^(-1/10)|lambda|^(-1/10)=|lambda|^(-1)`.

Thus neither bound hides a scale defect.

## 6. Why this pays the fresh B09 rank-one analytic obstruction

The newest fleet01/B09 theorem pays an endpoint indefinite pair whenever the Schur-center residual has finite `L^p` regularity, and obtains a particularly useful bound from a rank-two residual cross block. Its Section 8 isolates the third alternative: a genuinely rank-one residual bank operator, retaining arbitrary within-bank curvature.

Let that residual cross operator be `C` of rank one, with sole singular value `Theta`. Theorem 4.1 gives immediately

`||p_Q||_infinity
 <11.021 D^(-2/5) kappa^(-1/10) Theta^(-1/10),`                  (6.1)

while Theorem 5.2 gives the complementary bound

`||p_Q||_infinity
 <D^(-1/2)[22.648+log_+(4D/(kappa Theta))].`                     (6.2)

Hence the analytic statement “rank-one residual cross curvature is too weak to smooth the endpoint logarithm” is false: **one nonzero Schur cross singular direction is enough**, once it is spent as a fractional potential of the whole residual before attempting an `L^p` density bound. The residual itself may still have an unbounded logarithmic density; that causes no problem because its `1/8`-Riesz potential is finite.

This does not prove the bare spectral hypothesis forces a quantitative `D,kappa,Theta`; it therefore does not solve full QFORM. It does, however, remove the rank-one *analytic* endpoint from the current pair-log route and leaves only the geometric/structural extraction or the exactly degenerate `F=0` packet.

## 7. Designated partner fleet04/B01 applied to the new inequality

Apply the exact signed-Fejer equivalence (2.5) to Theorems 4.1 and 5.2. On this endpoint-pair plus nonzero-Schur-cross branch,

`boxed(
 sup_(T>0,y) D_T law(Q)(y)
 <= min{
  11.021 D^(-2/5) kappa^(-1/10) F^(-1/10),
  D^(-1/2)[22.648+log_+(4D/(kappa F))]
 }.
)`                                                              (7.1)

This is an actual application of the assigned partner theorem to a new inequality. It controls exactly the phase-sensitive averaged-frequency quantity equivalent to the target `L^infinity` norm. It does **not** assert `int|phi_Q|<infinity` and does not resurrect any pointwise `|t|^-1/2` Fresnel statement.

The phase-aligned fragmented-support counterexample remains valid: a cap-one density can be chosen to align with a prescribed scalar quadratic frequency and prevent any uniform pointwise decay. The present bound survives because it uses the complete Schur remainder's aggregate cross interaction and the signed/physical-space logarithmic smoothing interface instead.

## 8. Stress instance and exact scope

For a concrete scale-normalized packet, take an endpoint block `P=diag(1,-1)`, so `D=kappa=1`, and suppose the exact Schur remainder has an original-coordinate rank-one cross block with sole singular value `Theta=1`. Then

`||p_Q||_infinity <11.021`                                      (8.1)

by the power form. This remains true with arbitrary quadratic self blocks on both residual banks, arbitrary affine terms generated by outside original coordinates, and any additional residual spectrum, because those terms are already retained in the aggregate-Riesz input.

The example is only a mechanism check. The theorem does not require rank one, and the full conjecture is not reduced to this normalized packet.

## 9. Continuity and the first unpaid implication

The new argument proves absolute continuity and essential boundedness. It does **not** establish a continuous density representative. Fleet04/B01's signed-Fejer equivalence also separates these questions: a uniform Fejer bound gives bounded density, while continuity would require an additional local-uniform convergence or another regularity argument.

The first unpaid implication is now:

`QFORM-PAIR-OR-ONE-CROSS-STRUCTURAL-ROUTING-v1`:

> In the current high-leverage / balanced-star survivors, force either (i) an invertible indefinite physical endpoint pair with quantitative `D,kappa` whose exact Schur remainder has any quantitative nonzero original-coordinate cross Frobenius mass `F`, in which case (7.1) pays it; (ii) an already-paid definite-pair, grouped-star, ridge/diffuse, sequential-pivot or rank-two packet; or (iii) an exactly cross-free Schur remainder whose remaining three-curvature content can be exposed without rotating the product law.

The key change from the previous frontier is that **residual rank two is no longer analytically required after an indefinite endpoint pair**. A single Schur cross direction suffices. The genuinely hard survivor is therefore an extraction/degeneracy problem, not finite-`L^p` smoothing of a rank-one bank.

Full QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**.
