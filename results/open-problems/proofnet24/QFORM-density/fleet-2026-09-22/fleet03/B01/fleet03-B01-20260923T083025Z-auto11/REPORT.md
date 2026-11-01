SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B01, 2026-09-23T08:30:25Z.
attacking: exact-rank-two physical cross smoothing when the two-dimensional cross-kernel has definite curvature; combine a planar shell L2-time estimate with rank-two gradient Plancherel and then transfer to signed Fejer.

# fleet03/B01 — rank-two cross plus definite two-dimensional kernel

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `fleet03-B01-20260923T083025Z-auto11`  
Classification: `PROVED SUPPORTING TARGET-LEVEL ANALYTIC THEOREM / FULL QFORM OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Continuity: the new branch has a continuous `C_0(R)` density.

## 1. Scope and correction boundary

The full owner target remains open: for arbitrary independent real coordinates with probability densities bounded by one and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove a universal density cap or give a target-valid counterexample. No moment, support, Gaussian, log-concavity, connected-support, identical-law, or post-rotation independence hypothesis is added.

The live pointwise correction is preserved. For any prescribed frequency `s>0` and small `delta>0`, the set

`{x: dist(s x^2,2 pi Z)<=delta}`

has infinite Lebesgue measure (the admissible intervals around `sqrt(2 pi k/s)` have lengths comparable to `delta/sqrt(k)` and their sum diverges). Hence one may choose a finite union of such intervals of total length one and use its indicator as a cap-one probability density. Then

`Re E exp(i s X^2) >= cos(delta)`.

Thus there is no law-uniform pointwise `C |s|^{-1/2}` estimate. The theorem below uses an integrated `L^2(dt)` shell estimate in two transverse dimensions, not scalar pointwise stationary phase.

Fresh source inputs actually used are:

1. The current Claude volume-stability theorem, `yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`, `proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`. Its equation (10) pays admissible rank-at-least-three original-coordinate cross packets, with arbitrary self phases retained. Section 8 explicitly leaves low-cross-rank/hub packets as the next obligation.
2. The two-dimensional product-marginal theorem in the current proof map: if `M` is a rank-two real `2 x m` matrix and `Y` has independent cap-one coordinates, then
   `||p_(MY)||_infinity <= 2/sqrt(det(MM^T))`.
3. Designated partner fleet04/B01, canonical `yspennstate/math-open-problems@a3693ed6d50e8e4143b2f33bf997c5de2cb52d79`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B01/20260922T141507Z-b01-qform-fejer-r1/REPORT.md`, proving the exact signed-Fejer identity
   `||p_mu||_infinity = sup_(T>0,y) D_T mu(y)`
   with `+infinity` on both sides when no bounded density exists.

The current result attacks precisely the rank-two side left outside the volume-stability exit.

## 2. Setup and invariant currency

Choose four ORIGINAL coordinates `I` and a disjoint ORIGINAL-coordinate bank `J`; put all remaining coordinates in `W`. After conditioning on `X_W=w`, write the exact form as

`Q_w = X_I^T B X_I + 2 X_I^T K X_J + l_w^T X_I + G_w(X_J)`,       (2.1)

where `B=A[I,I]` is symmetric `4 x 4`, `K=A[I,J]`, `l_w` is arbitrary, and `G_w` is an arbitrary measurable real function (for the quadratic-form application it contains every `J-J`, `J-W`, and conditioned constant term).

Assume

`rank K=2`.                                                        (2.2)

Let `V` be any `4 x 2` orthonormal basis of `ker(K^T)`. Put

`Delta = sigma_1(K) sigma_2(K) > 0`,                              (2.3)
`H = V^T B V`,                                                     (2.4)
`d_2 = |det H|`.                                                   (2.5)

The new hypothesis is that `H` is definite, positive or negative. Thus `d_2>0`.

The quantity `Delta^2 d_2` is basis-independent. If `R` is any orthonormal basis of `range(K^T)` and

`C_6 = [[B, K R],[(K R)^T,0_2]]`,                                (2.6)

then

`|det C_6| = Delta^2 d_2`.                                        (2.7)

Indeed rotate the four-dimensional center so that its first two coordinates span `range(K)` and its last two span `ker(K^T)`. Then `K R` becomes `[[S],[0]]` with invertible `2 x 2` matrix `S` and `|det S|=Delta`. In the order `(u,source,z)`, the upper `4 x 4` block is `[[B_uu,S],[S^T,0]]`; its inverse has zero `u-u` block and its determinant has absolute value `det(S)^2`. Therefore the Schur complement of the `z` block is exactly `H`, proving (2.7). This is algebra only; no probabilistic independence after the rotation is asserted.

## 3. A mass-sensitive planar shell L2 lemma

### Lemma 3.1

Let `0<=rho<=1` be integrable on `R^2`, with mass `m<=1`. Let `H` be a definite real symmetric `2 x 2` matrix. For arbitrary `b in R^2,c in R`, set

`F(t)=int rho(z) exp(it(z^T H z+b^T z+c)) dz`.

Then

`boxed: int_R |F(t)|^2 dt <= 2 pi^2 |det H|^(-1/2) m.`             (3.1)

**Proof.** Complete the square. If necessary reflect the output so that `H` is positive definite. Under `y=H^(1/2)(z-z_0)`, Lebesgue measure changes by `det(H)^(-1/2)`. The pushforward of Lebesgue measure by `|y|^2` has density exactly `pi` on the positive half-line, because an annulus with squared-radius width `ds` has area `pi ds`. Since `rho<=1`, the pushforward density `g` of the subprobability measure `rho(z)dz` therefore satisfies

`0<=g<=pi/sqrt(|det H|)`,   `int g=m`.                             (3.2)

Hence

`int g^2 <= (pi/sqrt(|det H|)) m`.                                (3.3)

With Fourier convention `F(t)=int e^{its}g(s)ds`, Plancherel gives `int|F|^2=2pi int g^2`, proving (3.1). QED.

This is the replacement for scalar pointwise decay used in this run. It is translation-uniform and depends only on a genuine two-dimensional definite shell.

## 4. Main theorem

### Theorem 4.1 — `QFORM-RANK2-CROSS-DEFINITE-KERNEL-L2-v1`

Under (2.1)-(2.5), with `H` definite, the full ambient quadratic form has a continuous density in `C_0(R)` and

`boxed:
 ||p_Q||_infinity
 <= 3 (pi/2)^(1/3) Delta^(-1/3) d_2^(-1/6)
 < 3.488 Delta^(-1/3)d_2^(-1/6).`                                (4.1)

Equivalently, by (2.7),

`boxed: ||p_Q||_infinity <= 3(pi/2)^(1/3) |det C_6|^(-1/6).`       (4.2)

All same-side curvature on BOTH active banks is retained: `B` is arbitrary subject only to definiteness of its restriction to the cross-kernel, and `G_w` is arbitrary. All outside spectrum and couplings are retained through conditioning.

**Proof.** Fix `w`. Choose `O in O(4)` whose first two columns span `range(K)` and last two columns are `V`. Write

`(u,z)=O^T X_I`,  `u,z in R^2`.                                   (4.3)

The four original center coordinates are independent with densities at most one, so their joint density is at most one. Orthogonal change of variables preserves this pointwise cap: the joint density `rho(u,z)` in (4.3) obeys

`0<=rho<=1`, `int rho=1`.                                         (4.4)

No independence of `u,z` is claimed.

In these coordinates

`O^T K = [[M],[0]]`,                                               (4.5)

where `M` is rank two and

`sqrt(det(MM^T))=Delta`.                                          (4.6)

For fixed `t`, integrate first in `z` and write the resulting function of `u` as `h_(t,w)(u)`. For each fixed `u`, the quadratic coefficient in `z` is exactly `H`; all `u-z` and conditioned terms contribute only a linear term and a constant in `z`. Put

`m(u)=int rho(u,z)dz`.                                             (4.7)

Lemma 3.1 therefore gives

`int_R |h_(t,w)(u)|^2 dt <= 2 pi^2 d_2^(-1/2) m(u)`.              (4.8)

Let

`A_w(t)=||h_(t,w)||_(L^2(du))`.                                   (4.9)

Tonelli and `int m(u)du=1` imply

`||A_w||_2 <= sqrt(2) pi d_2^(-1/4)`.                             (4.10)

Now use the untouched original-product `J` bank. Put `L=2M X_J`. The product-projection theorem and two-dimensional scaling give

`||p_L||_infinity <= 1/(2 Delta)`.                                (4.11)

The arbitrary phase `exp(itG_w(X_J))` can be disintegrated over `L`; its resulting complex density `eta_(t,w)(l)` satisfies `|eta_(t,w)(l)|<=p_L(l)`. Hence

`||eta_(t,w)||_2 <= (2Delta)^(-1/2)`.                             (4.12)

The cross phase is `exp(it u.l)`. Cauchy-Schwarz in `l` and two-dimensional Plancherel give, for `t!=0`,

`|phi_w(t)|
 <= (2Delta)^(-1/2)
    [int |hat h_(t,w)(t l)|^2 dl]^(1/2)
 = sqrt(2) pi Delta^(-1/2)|t|^(-1) A_w(t).`                      (4.13)

Average over `W` and put `A(t)=E_W A_w(t)`. Minkowski and (4.10) give

`||A||_2 <= sqrt(2) pi d_2^(-1/4)`.                              (4.14)

Together with `|phi_Q(t)|<=1`, for every `T>0`,

`int_R |phi_Q(t)|dt
 <= 2T + sqrt(2)pi Delta^(-1/2)
          int_(|t|>T) |t|^(-1)A(t)dt
 <= 2T + 2sqrt(2) pi^2 Delta^(-1/2)d_2^(-1/4) T^(-1/2).`         (4.15)

Set

`B_0=2sqrt(2) pi^2 Delta^(-1/2)d_2^(-1/4)`.                      (4.16)

The exact minimizer of `2T+B_0T^(-1/2)` is

`T=(B_0/4)^(2/3)`,                                                (4.17)

and the minimum is `6(B_0/4)^(2/3)`. Thus `phi_Q in L^1`; Fourier inversion supplies a continuous `C_0` density and

`||p_Q||_infinity
 <= (3/pi)(B_0/4)^(2/3)
 = 3(pi/2)^(1/3) Delta^(-1/3)d_2^(-1/6).`                       (4.18)

This proves (4.1). QED.

### Scaling check

Under `A -> lambda A`, `Delta -> lambda^2 Delta` and `d_2 -> lambda^2 d_2`; the right side scales as `|lambda|^(-2/3)|lambda|^(-1/3)=|lambda|^(-1)`, exactly the required density scaling.

## 5. Exact signed-Fejer consequence from the designated partner

Fleet04/B01 proves

`||p_mu||_infinity = sup_(T>0,y) D_T mu(y)`,                      (5.1)

where

`D_T mu(y)=(1/(2pi)) int_(-T)^T (1-|t|/T)
              Re(e^(-ity) muhat(t))dt`.                           (5.2)

Applying (5.1) to Theorem 4.1 at the actual new inequality gives

`boxed:
 sup_(T>0,y) D_T law(Q)(y)
 <=3(pi/2)^(1/3) Delta^(-1/3)d_2^(-1/6).`                        (5.3)

Therefore every interval `I_0` also satisfies directly

`P(Q in I_0) <=3(pi/2)^(1/3) Delta^(-1/3)d_2^(-1/6)|I_0|`.       (5.4)

Equation (5.3) is the requested averaged-frequency replacement. It retains signed time cancellation as the exact density interface; the proof of its cap does not invoke a law-uniform pointwise quadratic-phase envelope.

## 6. A genuinely overlapping target-valid control family

Let `H_4/2` be a normalized `4 x 4` Hadamard matrix. Split its columns as orthonormal `U,V in R^(4 x 2)`. Take two further original coordinates `Y in R^2` and define

`Q = X_I^T (V V^T) X_I + 2 X_I^T U Y`.                            (6.1)

Here `K=U`, `Delta=1`, `ker(K^T)=range(V)`, and the kernel restriction is `H=I_2`, so `d_2=1`. The theorem gives, for every cap-one product input law,

`boxed: ||p_Q||_infinity <=3(pi/2)^(1/3)<3.488`,                  (6.2)

and `p_Q in C_0`.

In the orthogonal center basis `(U,V)`, the matrix spectrum is exactly

`{-1,-1,1,1,1,1}`.                                                (6.3)

Thus this is a genuine target-valid family. Importantly, each column of `V` uses all four original center coordinates, so the two smoothing squares overlap the same source coordinates that generate the rank-two cross term. The designated partner's disjoint grouped-square theorem does not directly apply to this overlap; Theorem 4.1 does.

As an equation-level check against the newest source, the current finite-dimensional spectral theorem would pay the six-dimensional control (6.1) by the much coarser universal bound `2sqrt(6 pi * 6)=12sqrt(pi)`. The new estimate (6.2) is dimension-free in the size of the `J` and conditioned `W` banks and specifically exploits the rank-two/definite-kernel geometry. More generally, the newest volume-stability theorem pays admissible rank-at-least-three cross packets, while Theorem 4.1 pays this exact-rank-two definite-kernel packet. These are compatible exits rather than competing uses of a false single-minor dichotomy.

## 7. What remains

The theorem does **not** close the unrestricted N3/no-pivot problem. It requires an exposed four-original-coordinate versus original-bank packet whose physical cross block has exact rank two and whose two-dimensional cross-kernel curvature is definite with quantitative currency `Delta^2 d_2`.

The first unpaid implication after this run is therefore narrower:

`QFORM-RANK2-KERNEL-SIGNATURE-ROUTING-v1` — in the remaining low-cross-rank/hub N3 states, either expose a rank-two four-row packet with dimension-free lower bound on `Delta^2 d_2` and definite kernel restriction, route to an already-paid volume/grouped/hub/null/pair-log branch, or control the **indefinite or nearly singular two-dimensional cross-kernel** without reverting to arbitrary-joint coarea or scalar pointwise stationary phase.

The definite assumption is mathematically real for this `L^2` mechanism: an arbitrary cap-one planar density can concentrate along an increasingly long thin hyperbolic shell, so the corresponding indefinite quadratic pushforward need not have a uniform `L^2` density bound. That obstruction does not disprove QFORM because the full product provenance and the remaining spectral direction are not represented by an arbitrary planar density.

Full QFORM remains OPEN. No global continuity conclusion is claimed beyond the new branch.
