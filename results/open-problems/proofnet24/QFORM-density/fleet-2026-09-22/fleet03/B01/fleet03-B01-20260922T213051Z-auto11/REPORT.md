SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B01, 2026-09-22T21:30:51Z.
attacking: translation-uniform mixed-frequency Riesz/Fejer synthesis for three spectral directions without coordinatewise absolute-value losses.

# fleet03/B01 auto11 — logarithmic-pair + fractional-Riesz compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: `Oscillatory replacement` / FOURIER  
Run: `fleet03-B01-20260922T213051Z-auto11`  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **PROVED SUPPORTING THEOREM / NEW TARGET-LEVEL SUBBRANCH / FULL QFORM OPEN**.

The full owner target remains open: for arbitrary dimension, independent original coordinates with probability densities bounded by one, and every real symmetric matrix with at least three eigenvalues of modulus at least one, prove a universal essential bound for the density of `X^T A X`, or give a genuine target counterexample. Continuity is a separate requested conclusion and is not proved by the new branch below.

## 1. Source-valid inputs and correction boundary

This run uses three completed source-pinned inputs.

1. **Physical indefinite-pair logarithmic envelope.**  
   `yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`,  
   `proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.  
   For two independent cap-one physical coordinates with an invertible indefinite `2 x 2` quadratic block `B`, put
   `D=|det B|` and `kappa=sigma_min(B)`. After completing the pair, for every gradient cutoff `r>0` the conditional pair density around its critical value obeys
   
   `p_pair(u) <= 2 sqrt(2)/r + D^(-1/2) log_+(2 r^2/(kappa |u|)).`       (1.1)
   
   The coordinate shifts may depend arbitrarily on the remaining original coordinates.

2. **Aggregate exterior-mass fractional Riesz theorem from the preceding B01 run.**  
   `yspennstate/math-open-problems@7df1461e33f7ea4e6026a650391822a16e56e987`,  
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B01/fleet03-B01-20260922T205456Z-r19/REPORT.md`.  
   For any quadratic-plus-affine residual `R` in independent cap-one original coordinates and any physical cross block `C`, write `E_k=e_k(CC^T)`. For
   `0<alpha<min(1,k/4)`,
   
   `H_alpha(R):=sup_s E|R-s|^(-alpha)
      <= C_(alpha,k) E_k^(-alpha/(2k)),`                         (1.2)
   
   where
   
   `C_(alpha,k)=((pi e/2)^alpha /(2k Gamma(alpha) cos(pi alpha/2)))
                  *Beta(alpha/(2k),1/8-alpha/(2k)).`             (1.3)
   
   This keeps arbitrary residual self blocks, affine terms, signs, outside couplings and extra spectrum. It uses the valid regularized-determinant bound, not law-uniform scalar pointwise Fresnel decay.

3. **Designated partner fleet04/B01 signed-Fejer theorem.**  
   `yspennstate/math-open-problems@a3693ed6d50e8e4143b2f33bf997c5de2cb52d79`,  
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B01/20260922T141507Z-b01-qform-fejer-r1/REPORT.md`.  
   For any probability law `mu`, its triangular signed Fejer averages `D_T mu(y)` satisfy
   
   `mu has density p with ||p||_infinity<=M`
   iff `D_T mu(y)<=M` for every `T>0,y`, and when finite
   `||p||_infinity=sup_(T,y) D_T mu(y)`.                         (1.4)

The source corrections are preserved. In particular, bounded one-dimensional input densities do **not** imply any law-uniform positive pointwise power decay for `E exp(i t X^2)`: phase-aligned fragmented supports remain a valid counterexample. Nothing below uses that false statement, post-rotation independence, unrestricted fiber suprema, or absolute Fourier integrability as a universal target.

## 2. A general logarithm-to-fractional-Riesz compiler

The pair-log theorem previously averaged its logarithm using a `sqrt(rho)` small-ball estimate. The key observation here is that a logarithmic singularity needs far less: **any positive fractional Riesz control** suffices.

### Lemma 2.1 — `QFORM-LOG-FRACTIONAL-RIESZ-COMPILER-v1`

Let `R` be any real random variable and suppose for some `0<alpha<1`

`H_alpha:=sup_t E|R-t|^(-alpha)<infinity`.                         (2.1)

Let a conditional two-coordinate indefinite pair have the envelope (1.1), with parameters `D,kappa>0`, and let its critical value after pair completion be exactly `R`. Then the resulting scalar law has an essentially bounded density and

`||p_Q||_infinity
 <= K_alpha D^(-1/[2(2alpha+1)])
             kappa^(-alpha/(2alpha+1))
             H_alpha^(1/(2alpha+1)),`                              (2.2)

where

`K_alpha=(2alpha+1)(2alpha)^(-2alpha/(2alpha+1))
          (2sqrt(2))^(2alpha/(2alpha+1))
          [2^alpha/(alpha e)]^(1/(2alpha+1)).`                     (2.3)

No independence between the completed-pair shift and `R` is required; only the two selected original input coordinates must remain independent of the residual original-coordinate vector, exactly as in the pair-log source.

#### Proof

For `0<x<L` and every `alpha>0`,

`log(L/x) <= (L/x)^alpha /(alpha e)`.                              (2.4)

Indeed, with `y=x/L`, the maximum of `y^alpha log(1/y)` on `(0,1]` is `1/(alpha e)`, attained at `y=e^(-1/alpha)`.

Condition on the residual original coordinates and apply (1.1). Averaging the conditional densities gives, for every output point `t` and every cutoff `r>0`,

`p_Q(t)
 <= 2sqrt(2)/r
    +D^(-1/2) E log_+(2r^2/(kappa |t-R|)).`                       (2.5)

Apply (2.4) with `L=2r^2/kappa`, then (2.1):

`p_Q(t)
 <= A/r + C r^(2alpha),`                                         (2.6)

where

`A=2sqrt(2),`
`C=D^(-1/2) H_alpha 2^alpha/(alpha e kappa^alpha).`               (2.7)

The minimum of `A/r+C r^(2alpha)` occurs at

`r_*=[A/(2alpha C)]^(1/(2alpha+1)).`                              (2.8)

At this point `A/r_*=2alpha C r_*^(2alpha)`, hence the minimum equals

`(2alpha+1)(2alpha)^(-2alpha/(2alpha+1))
 A^(2alpha/(2alpha+1)) C^(1/(2alpha+1)).`                         (2.9)

Substitution of (2.7) yields (2.2)-(2.3). Absolute continuity follows from the conditional pair-density formula and Tonelli. QED.

### Why this is a genuine mechanism change

The endpoint `alpha=1/2` is **not** required. Any `alpha>0` pays the logarithm. Therefore a two-cross aggregate that is too weak to supply the critical half-Riesz potential can nevertheless close a density bound once a physical indefinite pair has already reduced the remaining singularity to a logarithm. This is precisely different from the preceding B01 scalar-square route, where the square kernel itself requires the critical `alpha=1/2` potential.

## 3. Unconditional two-cross aggregate closes an indefinite pair

Take `alpha=1/4` and `k=2` in the aggregate Riesz theorem (1.2). No leverage assumption is needed because the preceding B01 theorem used the unconditional `q=2` regularized determinant estimate. We obtain

`H_(1/4)(R)
 <= C_R E_2(C)^(-1/16),`                                         (3.1)

where

`C_R=((pi e/2)^(1/4)/(4 Gamma(1/4) cos(pi/8)))
      *Beta(1/16,1/16)
    =3.4130191088555859... .`                                    (3.2)

### Theorem 3.1 — `QFORM-INDEFINITE-PAIR-PLUS-E2-SCHUR-v1`

Let `Q=X^T A X+b^T X+d` with independent original coordinates of densities at most one. Choose two ORIGINAL coordinates whose principal block `B` is invertible indefinite, and write

`D=|det B|`, `kappa=sigma_min(B)`.                                (3.3)

Complete this pair exactly. Let `S` be the resulting Schur-complement quadratic matrix on the remaining original coordinates, so

`Q=((X_i,X_j)+m(Z))^T B ((X_i,X_j)+m(Z)) + R(Z)`,                 (3.4)

where `R` is the quadratic-plus-affine Schur remainder and `Z` consists of the remaining independent original coordinates.

Suppose some disjoint residual original-coordinate sets `I,J` have Schur cross block

`C=S[I,J]`                                                        (3.5)

with

`E_2(C)=e_2(CC^T)>0.`                                             (3.6)

Then `Q` has an essentially bounded density satisfying

`boxed:
 ||p_Q||_infinity
 <= C_* D^(-1/3) kappa^(-1/6) E_2(C)^(-1/24),`                    (3.7)

where

`C_* =3*2^(4/3)*e^(-2/3)*C_R^(2/3)
     =8.798137416949853... <8.799.`                               (3.8)

No sign, moment, compact-support, log-concavity, connected-support, diagonal-basis, exact-rank, or small-additional-spectrum assumption is made on the Schur remainder. Extra singular values of `C` and arbitrary residual self curvature are retained.

#### Proof

Apply Lemma 2.1 at `alpha=1/4`. In this case (2.6) is

`p_Q(t) <= A/r+B sqrt(r),`                                        (3.9)

with

`A=2sqrt(2),`
`B=(4*2^(1/4)/e) D^(-1/2) kappa^(-1/4) H_(1/4)(R).`              (3.10)

The exact minimum is

`3(A B^2/4)^(1/3)
 =3*2^(4/3)e^(-2/3)
   D^(-1/3) kappa^(-1/6) H_(1/4)(R)^(2/3).`                       (3.11)

Insert (3.1). Since `(E_2^(-1/16))^(2/3)=E_2^(-1/24)`, (3.7)-(3.8) follow. QED.

### Exterior-mass form

By Cauchy-Binet,

`E_2(C)=sum_(|P|=|Q|=2) det(C[P,Q])^2.`                          (3.12)

Thus Theorem 3.1 spends the **whole squared two-minor bank before taking a reciprocal**. It does not select a single tiny `2 x 2` residual cross minor. This is exactly the aggregation feature required by the live low-local-minor corrections.

## 4. What the new theorem pays relative to the current frontier

The previous B01 run showed that unconditional `E_2` control by itself reaches the critical half-Riesz endpoint only logarithmically: the `alpha=1/2,k=2,q=2` beta integral diverges. A scalar-square transducer therefore needs `E_3` (or another endpoint improvement).

Theorem 3.1 shows that this obstruction is **transducer-dependent**, not a dead end for `E_2`: once another part of the form has been reduced to the source-valid indefinite-pair logarithm, the strictly subcritical `alpha=1/4` Riesz potential is enough. In particular, any structural branch producing

* a quantitative physical indefinite pair `(D,kappa)`, and
* a Schur residual cross bank with aggregate `E_2(C)>=eta>0`

is paid without requiring residual `E_3`, without a leverage hypothesis, and without selecting a good individual residual minor.

For example, if `D>=d0`, `kappa>=k0`, and `E_2(C)>=eta0`, then

`||p_Q||_infinity
 <8.799 d0^(-1/3) k0^(-1/6) eta0^(-1/24).`                       (4.1)

The exponent `1/24` on the aggregate two-minor bank is deliberately mild. This makes the compiler useful when second-compound mass is diffuse over many physical minors.

This theorem does **not** prove that the bare three-large-eigenvalue hypothesis forces such a pair-plus-bank certificate. It therefore does not close QFORM. It also does not subsume the many-small-pair/heavy-star residual where every physical indefinite pair may be tiny; that remains an aggregation problem.

## 5. Designated partner applied to the new inequality

Apply fleet04/B01's exact signed-Fejer equivalence (1.4) to Theorem 3.1. On the pair-plus-`E_2` branch,

`boxed:
 sup_(T>0,y) D_T law(Q)(y)
 <=8.799 D^(-1/3) kappa^(-1/6) E_2(C)^(-1/24).`                  (5.1)

This is an actual averaged-frequency inequality, not merely a citation. It controls exactly the quantity equivalent to the target essential density norm while making no pointwise claim about `phi_Q(t)`.

The phase-aligned fragmented-support counterexample remains untouched: it refutes law-uniform pointwise scalar quadratic decay, whereas (5.1) is obtained from a physical-space logarithmic pair envelope plus an integrated fractional Riesz bound for the complete Schur remainder.

## 6. Continuity and first unpaid implication

The proof above establishes **absolute continuity plus an essential `L^infinity` bound**. It does not prove that the density has a continuous representative. Signed-Fejer boundedness alone also does not imply continuity. Continuity therefore remains OPEN on this branch.

The first unpaid implication for this B01 mechanism is now sharper:

`QFORM-AGGREGATE-PAIR-OR-LOG-COMPILER-ROUTING-v1`:

> In the still-unpaid many-small-pair / heavy-star or near-rank-two structural states, either aggregate the physical pair resource before reciprocal payment, or produce one quantitative indefinite physical pair whose exact Schur remainder retains a dimension-free second exterior cross mass. Theorem 3.1 then closes the analytic side without requiring the critical `E_3` half-Riesz currency.

A direct next analytic target is a **many-pair averaged logarithmic envelope** in which the physical-pair logarithms are summed with determinant/exterior weights before any `D^(-1/2)` or `kappa^(-alpha)` reciprocal cost is incurred. That would address the heavy-star branch where selecting one pair is known to lose dimension.

Full QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**.
