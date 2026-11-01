SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B01, 2026-09-23T13:30:48Z.
attacking: an indefinite physical pair followed by an arbitrary-sign exact-rank-two Schur principal bank; replace the pair logarithm by a translation-uniform half-Riesz receiver, then transfer the resulting density bound to signed Fejer averages.

# fleet03/B01 — indefinite pair + arbitrary rank-two Schur bank

Run: `fleet03-B01-20260923T133048Z-auto11`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Oscillatory replacement  
Status: **NEW SUPPORTING TARGET-LEVEL THEOREM / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Continuity: **not proved in the full scope below**; essential boundedness and absolute continuity are proved.

## 1. Source boundary and first missing implication

The full target remains open. Inputs are independent original-coordinate real random variables with probability densities bounded by one; the matrix is an arbitrary real symmetric matrix with at least three eigenvalues of modulus at least one. No moment, support, Gaussian, log-concavity, connected-support, identical-law, or post-rotation-independence hypothesis is added.


* law-uniform pointwise quadratic Fresnel decay is false for arbitrary cap-one densities;
* an arbitrary spectral rotation does not preserve independence;
* the arbitrary-joint rank-three coarea statement and positive conditional-density-moment gate are false;
* one uniformly good fixed physical minor or rank-two cross packet is not forced by the three-large-eigenvalue hypothesis.

The first analytic implication attempted in this run is the following. After completing an invertible **indefinite physical pair**, suppose one can expose a disjoint original-coordinate bank whose **Schur principal block itself has exact rank two**. Existing results paid (i) semidefinite rank-two Schur banks only with a range-compatible affine term, and (ii) rank-two **cross** bicore blocks between two banks. The goal here is to pay an arbitrary-sign rank-two Schur principal bank with an arbitrary affine term, including its kernel component.

The exact dependencies used are:

1. `QFORM-PHYSICAL-PAIR-LOG-ENVELOPE-v1`, source  
   `yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`,  
   `proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.  
   For an invertible indefinite original-coordinate pair matrix `B`, with
   `D=|det B|` and `kappa=sigma_min(B)`, its translated conditional density satisfies for every `r>0`

   `p_pair(t) <= 2sqrt(2)/r + D^(-1/2) log_+(2r^2/(kappa |t-t0|))`.  (1.1)

   If the exact remainder obeys `sup_t P(|R-t|<rho)<=H sqrt(rho)`, the same source gives

   `||p_Q||_infinity <=4 sqrt(2H) (D kappa)^(-1/4)`.                 (1.2)

   Pair translations may depend arbitrarily on the remainder variables.

2. `QFORM-RANK2-AFFINE-HALF-RIESZ-v1`, source  
   `yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`,  
   `proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.  
   If `U^T U=I_2`, `Lambda` is invertible symmetric, and `b` is arbitrary, then for independent cap-one original coordinates

   `sup_s E |(U^T X)^T Lambda(U^T X)+b^T X-s|^(-1/2)
        <=128 |det Lambda|^(-1/4)`.                               (1.3)

3. Designated partner fleet04/B01, newest completed overlap-two receiver:  
   `yspennstate/math-open-problems@27ae9c5fbf53787fac1d61d7f480e0283be8c1c5`,  
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B01/20260923T121347Z-fleet04-B01-overlap2-explicit-r1/REPORT.md`.  
   For an invertible indefinite physical pair `S`, it proves

   `||p_Q||_infinity <=22.385 (D kappa)^(-1/6) W_2(S)^(-1/12)`.     (1.4)

4. Designated partner fleet04/B01 signed-Fejer identity, source  
   `yspennstate/math-open-problems@88003dc06af684cc4bc178a7dfe8e7cbebb0f987`,  
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B01/20260922T234537Z-fleet04-B01-grouped-square-fejer-r2/REPORT.md`. It proves for every probability law `mu`

   `||p_mu||_infinity = sup_(T>0,y in R) D_T mu(y)`,                (1.5)

   with both sides `+infinity` if no bounded density exists, where `D_T` is the signed triangular Fejer average.

No literature-wide novelty claim is made.

## 2. Preserve the phase-aligned obstruction

For every prescribed frequency `s>0` and every small `delta>0`, the set

`E_(s,delta)={x: dist(s x^2,2pi Z)<=delta}`

has infinite Lebesgue measure. Choose a finite measurable union inside it of total measure one and let `f=1_E`. Then `f` is an admissible probability density with `0<=f<=1`, while

`Re int exp(i s x^2) f(x) dx >= cos(delta)`.                         (2.1)

Thus no law-uniform estimate `|E exp(i s X^2)|<=C|s|^(-alpha)` with any `alpha>0` can hold over the target class. Nothing below uses such an estimate. The replacement is a distributional/fractional one after retaining original-coordinate product structure.

## 3. A determinant-free pointwise pair envelope

The pair-log envelope (1.1) immediately has a useful pointwise optimization that is uniform in the pair determinant.

### Lemma 3.1 — `QFORM-INDEFINITE-PAIR-HALFRIESZ-KERNEL-v1`

For an invertible indefinite physical pair `B`, let `kappa=sigma_min(B)`. Uniformly over all translations and affine terms, its density satisfies, for almost every `t!=t0`,

`boxed: p_pair(t) <=4 kappa^(-1/2)|t-t0|^(-1/2).`                   (3.1)

#### Proof

In (1.1) choose

`r^2=kappa |t-t0|/2`.                                                 (3.2)

Then the logarithmic argument is exactly one, so the logarithmic term vanishes, while

`2sqrt(2)/r =4 kappa^(-1/2)|t-t0|^(-1/2)`.                          (3.3)

The value at the single critical point may be infinite. This is harmless in every subsequent half-Riesz average. QED.

This is not a pointwise characteristic-function estimate. It is a pointwise **output-density kernel** for a two-coordinate physical pair.

## 4. Main theorem: arbitrary-sign rank-two Schur principal bank

Let `P={p,q}` be two ORIGINAL coordinates and write the physical principal pair as

`B=A[P,P]`.

Assume `B` is invertible and indefinite. Put

`D=|det B|`, `kappa=sigma_min(B)>0`.                                (4.1)

Let `C=P^c` and form the exact Schur complement

`S=A[C,C]-A[C,P]B^(-1)A[P,C]`.                                    (4.2)

Choose any original-coordinate bank `V subset C`; write `Z=C\V`. Assume only that the symmetric principal block

`S0=S[V,V]`                                                         (4.3)

has exact rank two. Let its two nonzero eigenvalues be `mu_1,mu_2` and define the aggregate rank-two curvature

`Pi_2=|mu_1 mu_2|=pdet_abs(S0)>0`.                                 (4.4)

No sign restriction is imposed: `S0` may be definite, semidefinite of either sign, or indefinite (rank two means the two listed eigenvalues are nonzero; in ambient dimension greater than two it has a kernel). No restriction is imposed on the affine component along that kernel.

### Theorem 4.1 — `QFORM-INDEFINITE-PAIR-RANK2-SCHUR-HALFRIESZ-v1`

Under (4.1)--(4.4), for arbitrary independent cap-one input laws and arbitrary remaining blocks/couplings,

`boxed:
 ||p_(X^T A X)||_infinity
 <=512 kappa^(-1/2) Pi_2^(-1/4).
`                                                                       (4.5)

A second, complementary estimate is

`boxed:
 ||p_(X^T A X)||_infinity
 <=64 (D kappa)^(-1/4) Pi_2^(-1/8).
`                                                                       (4.6)

Therefore

`boxed:
 ||p_(X^T A X)||_infinity
 <=min{512 kappa^(-1/2)Pi_2^(-1/4),
        64(Dkappa)^(-1/4)Pi_2^(-1/8)}.
`                                                                       (4.7)

The law is absolutely continuous. Continuity of a representative is **not proved** at this full level of roughness and dependence.

### Proof

Complete the physical pair exactly, without rotating any random input coordinates. With `Y=X_C`,

`Q=(X_P+m(Y))^T B (X_P+m(Y))+R(Y)`,                                  (4.8)

where `m(Y)=B^(-1)A[P,C]Y` (plus the analogous deterministic shift if affine terms are present) and

`R(Y)=Y^T S Y+ell^T Y+c`.                                            (4.9)

The pair inputs remain independent cap-one variables conditional on all of `Y`; the translation `m(Y)` may depend arbitrarily on the same variables that produce `R`.

Now condition only on `Z=z`. The exact remainder is a quadratic polynomial in the untouched original-coordinate bank `V`:

`R_z(V)=V^T S0 V+q(z)^T V+d(z)`,                                   (4.10)

where `q(z)=2S[V,Z]z+ell_V` and `d(z)` contains all remaining terms. Diagonalize **the deterministic rank-two matrix only**:

`S0=U Lambda U^T`, `U^T U=I_2`, `Lambda=diag(mu_1,mu_2)`.             (4.11)

No independence of `U^T X_V` is asserted. The orientation-free theorem (1.3) is specifically designed for this situation and allows the arbitrary physical affine vector `q(z)`. Therefore, uniformly in `z` and `s`,

`E_V |R_z(V)-s|^(-1/2)
 <=128 |mu_1mu_2|^(-1/4)
 =128 Pi_2^(-1/4).`                                                  (4.12)

Averaging over `Z` gives

`H_(1/2)(R):=sup_s E|R-s|^(-1/2) <=128 Pi_2^(-1/4).`                 (4.13)

Apply Lemma 3.1 conditionally to (4.8), with the critical output translated by `R(Y)`, and average:

`p_Q(t)
 <=4 kappa^(-1/2) E|t-R|^(-1/2)
 <=512 kappa^(-1/2) Pi_2^(-1/4).`                                   (4.14)

This proves (4.5) and absolute continuity.

For the complementary bound, Markov against the half-Riesz kernel gives for every `rho>0`

`P(|R-s|<rho)
 <=sqrt(rho) E|R-s|^(-1/2)
 <=128 Pi_2^(-1/4) sqrt(rho).`                                     (4.15)

Thus the pair-log small-ball compiler (1.2) applies with

`H=128 Pi_2^(-1/4)`.                                                (4.16)

Consequently

`||p_Q||_infinity
 <=4 sqrt(2*128 Pi_2^(-1/4))(Dkappa)^(-1/4)
 =64 (Dkappa)^(-1/4) Pi_2^(-1/8),`                                 (4.17)

which is (4.6). QED.

### Scope gain relative to existing receivers

This theorem is deliberately not renamed as a full solution. Its exact gain is local but useful:

* the earlier rank-two semidefinite Schur-bank receiver required `S0` semidefinite and required every conditioning-induced affine vector to lie in `Range(S0)`; (4.7) allows **either signature** and an **arbitrary affine vector**, including a kernel component;
* the existing pair-plus-rank-two-cross theorem assumes a rank-two cross block between two disjoint residual banks; (4.7) instead assumes a rank-two **principal quadratic block on one bank**;
* no individual physical coefficient of `S0` is inverted. The aggregate pseudo-determinant `Pi_2` is paid after the full bank is retained.

## 5. Exact signed-Fejer consequence

Apply the designated fleet04/B01 identity (1.5) to (4.7). For the same scope,

`boxed:
 sup_(T>0,y in R) D_T law(Q)(y)
 <=min{512 kappa^(-1/2)Pi_2^(-1/4),
        64(Dkappa)^(-1/4)Pi_2^(-1/8)}.
`                                                                       (5.1)

This is the assigned averaged-frequency replacement. It is phase-sensitive and does **not** imply `int |phi_Q(t)|dt<infinity`; it also does not assert any law-uniform pointwise Fresnel decay.

Equivalently every interval `J` satisfies

`P(Q in J)
 <=min{512 kappa^(-1/2)Pi_2^(-1/4),
        64(Dkappa)^(-1/4)Pi_2^(-1/8)} |J|.`                          (5.2)

## 6. Actual designated-partner application

Use the newest completed fleet04/B01 overlap-two theorem on the concrete full-target family

`A_c=diag(1,-1) direct_sum [[0,c],[c,0]], |c|>=1.`                   (6.1)

Its spectrum is `{1,-1,c,-c}`, so it has four eigenvalues of modulus at least one. Take the physical base pair `P={1,2}`. Then

`D=kappa=1`,                                                        (6.2)

while its Schur complement is exactly

`S0=[[0,c],[c,0]]`,                                                 (6.3)

whose rank-two pseudo-determinant is

`Pi_2=c^2`.                                                         (6.4)

The new theorem gives

`||p||_infinity <=min{512 |c|^(-1/2),64 |c|^(-1/4)}.`               (6.5)

For the same pair, fleet04/B01 computes

`W_2(P)=2c^2`                                                        (6.6)

and therefore proves

`||p||_infinity <=22.385 (2c^2)^(-1/12).`                           (6.7)

Combining the actual inequalities gives

`boxed:
 ||p_(X^T A_c X)||_infinity
 <=min{22.385(2c^2)^(-1/12),
        64|c|^(-1/4),
        512|c|^(-1/2)}.
`                                                                       (6.8)

At `|c|=1`, the partner branch is `21.1286264...`; for sufficiently large `|c|`, the new `|c|^(-1/2)` branch is stronger. This is an equation-level use of the designated partner, not a status citation.

Applying the signed-Fejer identity once more yields exactly the same right side in (6.8) for

`sup_(T>0,y) D_T law(X^T A_c X)(y)`.                                (6.9)

## 7. Strict no-pivot stress family paid uniformly

The theorem is not confined to a localized physical rank-two block. Fix `0<epsilon<=1/2`, set

`sigma=epsilon^(-3)`,                                                (7.1)

and choose three disjoint diffuse original-coordinate banks `I,J,W`, each of size `m`. Let `a,b,w` be the normalized all-ones vectors on those banks. On two additional original coordinates `P={p,q}`, take

`B_epsilon=[[0,epsilon],[epsilon,0]].`                               (7.2)

On `I union J`, take the exact rank-two Schur block

`S_(sigma,m)=sigma a a^T - sigma b b^T`,                            (7.3)

and on `W` add the rank-one positive block `w w^T`. Define the full matrix by the direct sum

`A_(epsilon,m)=B_epsilon direct_sum S_(sigma,m) direct_sum w w^T`.   (7.4)

The nonzero spectrum is exactly

`{epsilon,-epsilon,sigma,-sigma,1}`.                                (7.5)

Thus the owner target is satisfied: `sigma,-sigma,1` have modulus at least one. For the physical pair (7.2),

`D=epsilon^2`, `kappa=epsilon`, `Pi_2=sigma^2=epsilon^(-6)`.         (7.6)

The two bounds in (4.7) become

`512 epsilon^(-1/2) epsilon^(3/2)=512 epsilon`,                      (7.7)

and

`64 (epsilon^3)^(-1/4) epsilon^(3/4)=64`.                           (7.8)

Hence for every admissible cap-one product law,

`boxed: ||p_Q||_infinity <=min{512 epsilon,64}.`                    (7.9)

This family can simultaneously defeat every fixed physical pivot threshold. Indeed its largest diagonal magnitude outside the zero pair is `sigma/m`, and its nonzero physical `2x2` principal determinants are bounded by a constant multiple of `max{epsilon^2,sigma^2/m^2}`. Given any fixed `tau>0`, choose `epsilon` so that `epsilon^2<tau`, then choose `m` so large that `sigma/m<tau` and `sigma^2/m^2<tau`. Thus all physical scalar pivots and pair determinants can be made arbitrarily small while (7.9) remains dimension-free.

This is a control family, not a structural proof that every strict-N3 target exposes such a rank-two Schur bank.

## 8. A dependent-shift grouped-square control

For a second concrete control, let five independent cap-one variables be `X,Y,Z_1,Z_2,Z_3` and define

`Q=2(X+Z_1)(Y+Z_2)+Z_1^2+Z_2^2+Z_3^2.`                         (8.1)

The pair translation depends on the **same** square-producing variables, so a naive independent-convolution argument between pair and remainder is unavailable. Nevertheless the pair-log theorem explicitly allows this dependence. The fleet04/B01 grouped-square theorem gives the exact remainder density cap

`M=2pi`                                                           (8.2)

from any two of the three same-sign unit squares. Feeding that actual cap into the completed bounded-remainder pair-log optimization gives

`||p_Q||_infinity <=3+log(16pi)=6.917318608...`.                   (8.3)

The coefficient matrix of (8.1) has characteristic polynomial

`(lambda-1)(lambda^2-3lambda+1)(lambda^2+lambda-1)`,                (8.4)

hence spectrum

`{1,(3+-sqrt5)/2,(-1+-sqrt5)/2}`.                                  (8.5)

Exactly three eigenvalues have modulus at least one, so (8.3) is another genuine full-target control. This partner application keeps the dependence generated by pair completion rather than pretending the translated pair is independent of the square bank.

## 9. What remains

The full QFORM conjecture is still open. The first unpaid implication after this run is structural:

`QFORM-INDEFINITE-PAIR-RANK2-SCHUR-OR-EXISTING-EXIT-v1`:

> From the remaining strict-N3 / low-cross-rank states under the bare three-large-eigenvalue hypothesis, prove a product-preserving alternative that either exposes an invertible indefinite physical pair together with an exact rank-two Schur principal bank for which the combined currency in (4.7) is target-scale, or routes the same state into an already-paid definite-pair, rank-two/rank-three cross, grouped-square, ridge, hub, null-coloop, exterior-star, or diffuse-volume exit.

One must not demand a uniformly good fixed physical pair or minor: the live correction inbox contains source-valid families refuting that intermediate claim. The theorem here instead removes two analytic restrictions once the rank-two Schur bank is present: its sign and its conditioning-induced kernel-affine component.

Continuity remains separate. The proof above supplies conditional pair densities, an essentially bounded mixture, and absolute continuity, but no common translation modulus for arbitrary rough conditional laws. Therefore **only essential boundedness is claimed** in Theorem 4.1.

## 10. Deterministic checks

The accompanying `CHECKS.txt` records:

* `4*sqrt(2*128)=64`;
* the stress-family cancellation in (7.7)--(7.8);
* the exact characteristic polynomial in (8.4);
* `3+log(16pi)=6.917318608...`;
* the partner constant `22.385*2^(-1/12)=21.128626489...` at `|c|=1`.

These finite checks diagnose constants and algebra only; they are not substitutes for the proof above.

Full target: **OPEN**.  
Unrestricted continuity: **OPEN**.  
Branch result: **essential boundedness + absolute continuity proved**.  
Brain execution: **WITHOUT_VERIFIED_BRAIN**.
