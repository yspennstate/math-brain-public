SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B02, 2026-09-23T20:22:54Z.
attacking: integrated Fourier estimate — squeeze the strong-cut survivor to an arbitrarily thin relative rank-two tube, then expose the exact third-curvature alternatives that remain without deleting the small cross tail.

# fleet01/B02 r36 — parametric tail squeeze and third-curvature routing

Programme: `QFORM-DENSITY-3EIG-20260922`.
Status: **ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN / GLOBAL_FOURIER_CRITERION_OPEN_NOT_REFUTED**.
Continuity: proved on the paid Fourier branches below because the full characteristic function is in `L1(R)`; unrestricted continuity remains open.
Execution/memory status: `WITHOUT_VERIFIED_BRAIN`.

## 1. Fresh scope and exact sources


The full target remains: independent real original coordinates with scalar densities at most one and arbitrary real symmetric `A` with `s_3(A)>=1`; prove one universal essential density bound for `Q=X^TAX`, or a valid counterexample. No moment, support, Gaussian, log-concave, iid, sign or diagonal-basis assumption is added.

The strong original-coordinate cut is the completed fleet04/B20 theorem

`yspennstate/math-open-problems@c6f29397b3d45a7cf7ab67633a5451767b478912`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B20/20260923T142031Z-fleet04-B20-QFORM-r10/REPORT.md`.

In the live `N3(1/64)` chamber it gives an ORIGINAL-coordinate partition and physical cross block `M` satisfying

`E:=||M||_F^2 > E0:=11907/16384`,                                  (1.1)

and, for every chosen `0<delta<1`, either its D5 Fourier branch pays, or

`S4:=x1+x2+x3+x4 > (1-delta)E`,                                   (1.2)

where `x1>=x2>=...>=0` are the squared singular values of this same physical block. The D5 paid branch has

`||p_Q||_infinity
 < 5 sqrt(2e) 120^(1/10) delta^(-2/5) E0^(-1/2)`,                  (1.3)

with genuine Fourier `L1`.

The designated partner actually applied below is the completed fleet02/B02 marginal-free physical-E3 theorem

`yspennstate/math-open-problems@3fccd9b82b456e198758e5839be364b4b0ec5024`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B02/20260923T170839Z-fleet02-B02-qform-auto11/REPORT.md`.

For every literal original-coordinate physical cross block `B` with `Z=E3(B)>0`, it proves

`||p_Q||_infinity <=10.345084 Z^(-1/6)`,                           (1.4)

`integral_R |phi_Q(t)|dt <=2*pi*10.345084 Z^(-1/6)`,               (1.5)

with a continuous `C_0` density. Arbitrary same-bank quadratic terms, outside couplings, affine terms, signs and extra spectrum are retained.

For one secondary structural splice I use the completed fleet01/B07 near-rank-two Pluecker theorem

`yspennstate/math-open-problems@4a0d5ffbeb2cd078b6f33a4b3a678ae3dd94763f`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B07/fleet01-B07-20260923T170819Z-r29/REPORT.md`,

which says that if the complete physical E2 determinant law of a cross block lies within TV `1/64` of the product Pluecker law of its best rank-two truncation, then either one literal physical `2x2` minor carries at least `15/64` of `E2`, or the full ambient form has half-Riesz potential

`H_(1/2)(Q):=sup_t E|Q-t|^(-1/2)
 <=39.379 E2^(-35/253) E^(27/1012)`.                               (1.6)

That theorem is used only at its stated scope; half-Riesz by itself is not called a density bound.

## 2. Parametric D5/E3 squeeze

Put

`T2:=sum_(r>=3) x_r`.                                               (2.1)

The preceding r35 proof used `delta=1/64`. The same argument is actually parametric.

### Theorem 2.1 — `QFORM-D5UNPAID-PARAMETRIC-E3-SQUEEZE-v1`

Let `0<delta<=1/8`. Suppose a real matrix satisfies

`S4>(1-delta)E`,                                                     (2.2)

`T2>=delta E`.                                                       (2.3)

Then

`boxed: E3(M) > ((1-delta)delta^2/2) E^3.`                         (2.4)

#### Proof

Normalize by `E` and put

`a=x2/E`, `b=T2/E`; hence `x1/E=1-a-b`.                            (2.5)

**Case 1: `a>=delta`.** Keeping only the `x1*x2*x_r`, `r>=3`, terms gives

`E3/E^3 >= a b(1-a-b)`.                                           (2.6)

Since `x1>=x2`, `b<=1-2a`. On the rectangle-with-sloping-edge

`a>=delta`, `b>=delta`, `b<=1-2a`,

the concavity in `b` reduces the minimum to `b=delta` or `b=1-2a`; the remaining one-variable minima are at the endpoints. Hence

`a b(1-a-b)
 >= min{delta^2(1-2delta), delta(1-delta)^2/4}`.                  (2.7)

For `delta<=1/8`, the first displayed quantity is already larger than

`(1-delta)delta^2/2`.                                              (2.8)

**Case 2: `a<delta`.** Let `R4=sum_(r>=5)x_r`. From (2.2),

`R4<delta E`.                                                       (2.9)

Since `x3,x4<=x2=aE`,

`b<2a+delta`, so with `c=a+b` we have

`delta<=b<=c<4delta<=1/2`.                                        (2.10)

For `z=(x3,x4,...)`, every coordinate is at most `x2`, so

`e2(z)
 =[(T2)^2-sum z_j^2]/2
 >=[(T2)^2-x2*T2]/2`.                                              (2.11)

Thus for the full tail `y=(x2,x3,...)`,

`e2(y)=x2*T2+e2(z)
 >=(E^2/2)b(a+b)=(E^2/2)bc`.                                      (2.12)

Keeping only E3 terms containing `x1`,

`E3/E^3 >= (1/2)(1-c)bc`.                                        (2.13)

Because `c<=1/2`, `c(1-c)` is increasing, while `b,c>=delta`; therefore

`E3/E^3
 >(1/2)delta^2(1-delta)`.                                        (2.14)

This proves (2.4). No singular tail is deleted from the random form. QED.

### Corollary 2.2 — a tunably thin strong-cut survivor

Combine fleet04/B20 (1.2)-(1.3), Theorem 2.1, and the designated fleet02/B02 theorem (1.4)-(1.5). For every fixed `0<delta<=1/8`, every live strong-cut state is in one of three branches:

1. D5 already gives (1.3);
2. `T2>=delta E`, in which case

`Z:=E3(M) > Z_delta
 :=((1-delta)delta^2/2) E0^3`,                                   (2.15)

and therefore

`||p_Q||_infinity <10.345084 Z_delta^(-1/6)`,                    (2.16)

`integral |phi_Q| <2*pi*10.345084 Z_delta^(-1/6)`;                (2.17)

3. the sole cross-volume survivor obeys

`boxed: T2<delta E.`                                               (2.18)

This is the required new equation-level application of the completed `fleet02/B02` result.

A useful concrete choice is

`delta=2^(-19)=1/524288`.                                         (2.19)

Then the two paid density constants are, respectively,

`C_D5<4282.399`,                                                     (2.20)

`C_E3<1098.343`,                                                     (2.21)

and the E3 branch has

`integral |phi_Q|<6901.092`.                                      (2.22)

Hence, at the cost of a still universal finite constant, the unresolved strong-cut cross tail can be squeezed from the previous `T2<E/64` to

`boxed: T2<E/524288.`                                              (2.23)

The point is structural, not numerical optimization: for every fixed positive `delta`, the remaining tube can be made that thin; the constants deteriorate as `delta->0`, so this alone does not finish the conjecture.

## 3. The target's third singular direction cannot disappear into a rank-one crossing

The next deterministic lemma identifies exactly where the missing third curvature must go when the cross block is close to rank one.

### Theorem 3.1 — `QFORM-RANKONE-CROSS-SUBTRACTION-v1`

Let an arbitrary real symmetric matrix be written in any ORIGINAL-coordinate block partition as

`A=[[B,M],[M^T,C]]`,                                               (3.1)

and assume `s3(A)>=1`. Let `sigma1>=sigma2>=...` be the singular values of `M`. Then

`boxed: max{||B||op,||C||op} >= 1-sigma2.`                        (3.2)

In particular, if `sigma2<1/2`, then one of the two physical-bank self blocks has operator norm strictly larger than `1/2`.

#### Proof

Let `M1=sigma1 u1 v1^T` be a best rank-one approximation and define the symmetric matrix

`H=[[0,M1],[M1^T,0]]`.                                             (3.3)

Its rank is at most two. By the singular-value min-max / Eckart--Young characterization,

`||A-H||op >= s3(A)>=1`.                                          (3.4)

But

`A-H = diag(B,C)
      + [[0,M-M1],[(M-M1)^T,0]]`.                                (3.5)

The second summand has operator norm exactly `sigma2`, while

`||diag(B,C)||op=max{||B||op,||C||op}`.                            (3.6)

The triangle inequality applied to (3.4)-(3.6) proves (3.2). QED.

This is purely deterministic coefficient geometry. The vectors `u1,v1` are never treated as independent random coordinates.

## 4. Physicalize the third curvature in the actual N3 chamber

The fleet04/B20 strong-cut theorem is used in the `N3(1/64)` chamber, where

`max_i |A_ii|<1/64`.                                               (4.1)

Suppose the surviving strong-cut block from (2.23) additionally has

`x2=sigma2^2<1/4`.                                                  (4.2)

By Theorem 3.1, one bank self block, call it `K`, has

`||K||op>1/2`.                                                       (4.3)

Write `D=diag(K)` and `H=K-D`. From (4.1),

`||D||op<1/64`, hence

`||H||op>31/64`,                                                    (4.4)

so

`||H||F^2>(31/64)^2`.                                               (4.5)

Randomly color the physical coordinates of this bank into two parts `S,T`. Because `H` is symmetric with zero diagonal,

`E_color ||H[S,T]||F^2 = (1/4)||H||F^2`.                           (4.6)

Consequently there is a deterministic ORIGINAL-coordinate internal cut with

`boxed:
 ||A[S,T]||F^2 > (1/4)(31/64)^2
              =961/16384
              =0.05865478515625.`                                  (4.7)

Thus the genuine near-rank-one face of the tiny outer cross tube cannot be featureless: it carries a second, target-scale physical crossing inside one original bank. This is a three-bank product geometry, not a rotated-coordinate claim.

## 5. If the second cross singular scale survives, the E2 currency is macroscopic

On the same tiny-tail survivor (2.23), if instead

`sigma2>=1/2`,                                                      (5.1)

then `x2>=1/4`. Also

`x1 >= (E-T2)/2 > (1-delta)E/2`,                                  (5.2)

and therefore

`boxed:
 E2(M)>=x1x2 > ((1-delta)/8)E
                > ((1-delta)/8)E0.`                               (5.3)

At `delta=2^-19`,

`E2(M)>0.0908430274`,                                              (5.4)

or equivalently

`sigma1 sigma2>0.3014017707`.                                      (5.5)

This does **not** by itself prove bounded density: a rank-two crossing with arbitrary two-bank self curvature is the critical logarithmic endpoint. The fleet has explicit rank-two saddle examples, so I do not promote (5.3) to a false density theorem.

However the tiny-tail assumption allows a further rigorous split using the existing Pluecker compiler.

### 5.1 Relative second-scale subbranch `x2>=E/64`

Put `c=1/64`. Then

`P:=x1x2 >= c(1-delta-c)E^2`.                                     (5.6)

For `Omega=E2(M)`, the exterior-square tail satisfies

`Omega-P <= E*T2 < delta E^2`.                                    (5.7)

Hence

`rho:=(Omega-P)/Omega
 < delta/[c(1-delta-c)]`.                                         (5.8)

At `delta=2^-19`,

`rho<0.00012400818`,

and the fleet01/B07 TV estimate gives

`TV(W,W0)<=sqrt(rho)+rho/2<0.011198<1/64`.                         (5.9)

Therefore its completed r29 theorem applies. We get either

`det M[R,C]^2 >=(15/64)Omega`,                                    (5.10)

for one literal physical `2x2` minor, or

`H_(1/2)(Q)<=39.379 Omega^(-35/253)E^(27/1012)`.                   (5.11)

Using `E>E0` and (5.6), these become the absolute quantitative alternatives

`boxed: |det M[R,C]|>0.04363`,                                    (5.12)

or

`boxed: H_(1/2)(Q)<75.99.`                                        (5.13)

Neither is mislabeled as a full density result. The live cross-minor correction forbids using (5.12) alone as an inverse-pivot theorem, while (5.13) is a fractional potential awaiting a dependence-safe third-curvature transducer.

### 5.2 Absolute second-scale but relative-near-rank-one subbranch

Assume

`1/4<=x2<E/64`.                                                     (5.14)

Then automatically `E>16`. Let

`tau=1/4096`.                                                       (5.15)

If

`T2>=tau/E`,                                                        (5.16)

then `x1>(1-c-delta)E`, so

`E3(M)>=x1 x2 T2
       >(1-c-delta)tau/4
       >6.00813e-5`.                                                (5.17)

Applying the designated fleet02/B02 theorem at this **actual inequality** gives

`boxed: ||p_Q||infinity<52.273`,                                  (5.18)

`boxed: integral |phi_Q|<328.441`,                                (5.19)

and a continuous `C_0` density.

If instead `T2<tau/E`, then

`rho< E*T2/(x1x2)
    < tau / [(1-c-delta)E/4]
    < tau/[4(1-c-delta)]
    <6.201e-5`,                                                     (5.20)

because `E>16`. Thus again `TV(W,W0)<1/64` and the B07 theorem applies. Moreover

`Omega>=x1x2>4(1-c-delta)>3.93749`.                                (5.21)

So its alternatives sharpen here to

`boxed: |det M[R,C]|>0.96065`,                                    (5.22)

or

`boxed: H_(1/2)(Q)<35.08.`                                        (5.23)

Again these are routing currencies, not an illicit one-minor density conclusion.

## 6. Compact proof-graph consequence

After the paid diagonal / pivot branches and the fleet04/B20 strong-cut reduction, choose once and for all `delta=2^-19`. The remaining strong-cut state is now confined as follows.

**Fourier-paid states.** Either D5 pays with density constant `<4282.399`; or `T2>=delta E` pays by designated fleet02/B02 with density constant `<1098.343`; or, in the relative-near-rank-one but absolute-second-scale chamber, (5.16) pays with density constant `<52.273`.

**Unpaid structural states.** Every remaining state has `T2<delta E` and is one of:

1. `sigma2<1/2`: by (4.7), one of the two original outer banks contains an internal physical crossing of Frobenius energy `>961/16384`;
2. `sigma2>=1/2`: by (5.4), the outer physical crossing has `E2>0.090843`, and after the further splits above either a macroscopic literal `2x2` minor is present or the full ambient law has a universal half-Riesz bound (`<75.99`, or `<35.08` in the relative-near-rank-one absolute-second-scale subbranch).

Thus the old vague `T2<E/64` obstruction has been sharpened into a **three-bank/internal-crossing or E2-plus-half-Riesz/macro-minor** obstruction at fixed target scale. The small nonzero tail is retained everywhere; it is never dropped from the random quadratic phase.

The first unpaid B02 interface is now

`QFORM-THREEBANK-INTERNALCROSS-OR-E2-HALFRIESZ-TO-L1-v1`:

> convert either (i) an outer near-rank-one crossing plus the internal physical bank crossing (4.7), or (ii) the target-scale E2 crossing together with the source-proven half-Riesz/macro-minor alternatives, into a dependence-safe third-curvature receiver with a universal density bound. Existing one-sided-zero and overlap-square theorems pay substantial exact subcases, but the arbitrary nonzero leakage on both product banks still cannot be deleted or treated by a conditional density supremum.

No target-valid counterexample to the global criterion

`integral_R |E exp(it X^T A X)|dt <= C`

was found. It remains `OPEN_NOT_REFUTED`. Full bounded density and full continuity remain OPEN.

## 7. Correction ledger and scope checks

This proof does not use law-uniform pointwise quadratic phase decay, independence after a spectral rotation, arbitrary-joint coarea, a worst-fiber density supremum, conditional projection caps as independence, or a one-good-minor reciprocal shortcut. The B07 half-Riesz conclusion is kept distinct from an `L-infinity` density conclusion. The singular vectors are used only in deterministic inequalities. All physical cuts act on original coordinates.

The exact-rank-three/four crossing Fourier results remain compatible but do not authorize dropping the nonzero tail in (2.23). Likewise the fresh two-bank curved-tube/hub theorem is compatible supporting mathematics, but its specific normal form is not silently inferred here.
