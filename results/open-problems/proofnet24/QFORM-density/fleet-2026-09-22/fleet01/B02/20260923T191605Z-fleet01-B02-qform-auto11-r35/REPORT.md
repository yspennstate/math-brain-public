SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B02, 2026-09-23T19:16:05Z.
attacking: the strong-cut low-cross-rank collar — prove that D5 failure plus any nontrivial tail automatically creates target-scale physical third exterior volume, thereby removing the near-rank-one survivor and paying it by the designated fleet02/B02 integrated-Fourier theorem.

# fleet01/B02 r35 — D5-unpaid strong cut: only the near-rank-two tube survives

Programme: `QFORM-DENSITY-3EIG-20260922`.
Status: **ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN / GLOBAL_FOURIER_CRITERION_OPEN_NOT_REFUTED**.
Continuity: proved on the branch below because the full characteristic function is in `L1(R)`; unrestricted continuity remains open.
Execution/memory status: `WITHOUT_VERIFIED_BRAIN`.

## 1. Fresh source state and exact inputs


The strong-cut source is fleet04/B20,

`yspennstate/math-open-problems@c6f29397b3d45a7cf7ab67633a5451767b478912`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B20/20260923T142031Z-fleet04-B20-QFORM-r10/REPORT.md`.

In the fleet's `N3(1/64)` chamber it gives an ORIGINAL-coordinate partition `J sqcup K=[n]` and the literal physical cross block

`M=A[J,K]`

with

`E:=||M||_F^2 > E0:=11907/16384`.                                   (1.1)

Write the squared singular values of this same physical block as

`x1>=x2>=x3>=...>=0`,

and define

`T2:=sum_(r>=3) x_r`,

`S4:=x1+x2+x3+x4`.                                                    (1.2)

The fleet04/B20/fleet04-B02 D5 split says that either the D5 Fourier receiver already pays the law, or the same matrix satisfies

`S4 > (63/64) E`.                                                      (1.3)

The **designated partner actually applied** in this run is the latest completed fleet02/B02 theorem,

`yspennstate/math-open-problems@3fccd9b82b456e198758e5839be364b4b0ec5024`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B02/20260923T170839Z-fleet02-B02-qform-auto11/REPORT.md`.

It proves, for every ORIGINAL-coordinate physical cross block `B` with

`Z=E3(B)=e3(B^T B)>0`,

`||p_Q||_infinity <= 10.345084 Z^(-1/6)`,                            (1.4)

`integral_R |phi_Q(t)| dt <= 2*pi*10.345084 Z^(-1/6)`,              (1.5)

with a continuous representative vanishing at infinity. This is marginal-free and retains arbitrary same-bank quadratic terms, affine terms, outside couplings, signs, and extra spectrum.

The purpose of this run is to strengthen the structural input fed into (1.4)-(1.5).

## 2. Main new deterministic lemma

Set

`delta:=1/64`.                                                        (2.1)

### Lemma `QFORM-D5UNPAID-NONSMALLTAIL-FORCES-E3-v1`

Let `M` be any real matrix with squared singular values `x1>=x2>=...`, Frobenius energy `E=sum_r x_r`, and `T2,S4` as in (1.2). Assume

`S4>(1-delta)E`,                                                      (2.2)

`T2>=delta E`.                                                        (2.3)

Then

`boxed: E3(M) > ((1-delta) delta^2/2) E^3.`                          (2.4)

For `delta=1/64`,

`boxed: E3(M) > (63/524288) E^3.`                                   (2.5)

Thus a D5-unpaid strong-cut state with `T2>=E/64` can never be genuinely third-volume-poor, even when `x2<E/64`.

### Proof

Normalize by `E` and put

`a:=x2/E`, `b:=T2/E`.                                                 (2.6)

Then

`x1/E=1-a-b`.                                                         (2.7)

We split only according to whether the formerly separate near-rank-one threshold holds.

#### Case I: `a>=delta`

Here also `b>=delta`. Because `x1>=x2`,

`1-a-b>=a`, so `b<=1-2a`.                                            (2.8)

The terms of `e3(x)` containing `x1*x2` and one tail singular value give

`E3(M)>=x1*x2*T2
       =E^3 a b(1-a-b)`.                                             (2.9)

For fixed `a`, the function `b -> b(1-a-b)` is concave on `[delta,1-2a]`, hence its minimum occurs at an endpoint. At `b=delta`, the function of `a` is `delta*a*(1-a-delta)`, again concave on `a in [delta,(1-delta)/2]`, so its minimum is at an endpoint. At `b=1-2a`, the value is `a^2(1-2a)`, whose minimum over the same interval is likewise at an endpoint. The two endpoint values are

`delta^2(1-2delta)`

and

`delta(1-delta)^2/4`.                                                 (2.10)

For `delta=1/64` the first is smaller, hence

`E3(M)>=delta^2(1-2delta)E^3
       =(31/131072)E^3`,                                              (2.11)

which is stronger than (2.5).

#### Case II: `a<delta`

Now the D5-unpaid concentration (2.2) becomes decisive. Let

`R4:=sum_(r>=5)x_r=E-S4`.                                             (2.12)

Then `R4<delta E`. Since `x3,x4<=x2=aE`,

`b=T2/E=(x3+x4+R4)/E < 2a+delta`.                                   (2.13)

Consequently, with `c:=a+b`,

`delta<=b<=c<4delta=1/16<1/2`.                                      (2.14)

Let `z=(x3,x4,...)`; its sum is `T2=bE`, and every coordinate satisfies `z_j<=x2=aE`. Therefore

`sum_j z_j^2 <= x2 T2`,                                              (2.15)

and hence

`e2(z)=((T2)^2-sum_j z_j^2)/2
      >=((T2)^2-x2*T2)/2`.                                          (2.16)

For the full tail `y=(x2,x3,...)`,

`e2(y)=x2*T2+e2(z)
      >=((T2)^2+x2*T2)/2
      =(E^2/2)b(a+b)
      =(E^2/2)bc`.                                                    (2.17)

All elementary-symmetric terms are nonnegative, so retaining only the terms containing `x1` gives

`E3(M)>=x1 e2(y)
       >= (E^3/2)(1-c)bc`.                                           (2.18)

Since `b>=delta`, `c>=delta`, and `c<1/2`, the function `c(1-c)` is increasing throughout the relevant interval. Therefore

`E3(M)
 > (E^3/2) delta * delta(1-delta)
 = ((1-delta)delta^2/2)E^3`,                                        (2.19)

which proves (2.4). For `delta=1/64`, (2.19) is exactly (2.5). QED.

### Why this is not a forbidden perturbation argument

No small singular tail is deleted from the random quadratic form. The tail is used positively in the elementary-symmetric identity (2.17)-(2.18), and the Fourier theorem is then applied to the **entire original physical cross block**. No singular-vector coordinate is treated as an independent random variable.

## 3. Equation-level application of fleet02/B02

Return to the strong-cut block (1.1). On every D5-unpaid state satisfying

`T2>=E/64`,                                                          (3.1)

the lemma gives

`Z:=E3(M) > (63/524288) E^3`.                                       (3.2)

Using `E>E0=11907/16384`,

`Z > Z0
   :=(63/524288)(11907/16384)^3
   =4.6123034756722584e-5`.                                         (3.3)

Now insert this **actual new inequality** into the designated fleet02/B02 theorem (1.4)-(1.5). It yields

`boxed: ||p_Q||_infinity < 54.627884`,                              (3.4)

and the genuine unweighted integrated-Fourier estimate

`boxed: integral_R |phi_Q(t)| dt < 343.237116`.                     (3.5)

Thus this branch has a continuous `C_0` density.

The numerical arithmetic is only evaluation of the exact expressions

`10.345084 Z0^(-1/6)`

and

`2*pi*10.345084 Z0^(-1/6)`;

the mathematical implication is the exact inequality (3.2).

## 4. Proof-graph consequence: the near-rank-one tube disappears

Before this run, after the D5 / marginal-free-E3 exits the strong-cut proof graph retained two low-rank tubes:

`x2<E/64`  (near rank one),

or

`T2<E/64`  (near rank two).                                         (4.1)

The new lemma shows that the first alternative is not independently live. Indeed, even if `x2<E/64`, whenever `T2>=E/64` the D5-unpaid condition forces (3.2), and fleet02/B02 pays it by (3.4)-(3.5).

Therefore the strong-cut chamber now has the strictly simpler exhaustive form:

1. D5 already pays; or
2. `T2>=E/64`, in which case (3.4)-(3.5) pay by physical `E3`; or
3. the sole low-cross-volume survivor is

`boxed: T2<E/64.`                                                    (4.2)

In particular, the former `x2<E/64` branch survives only as a subcase of (4.2), not as a separate obstruction.

This also improves the previous strong-cut `E3` threshold on the non-low-rank chamber: the old direct product floor was

`E3(M) > (63/1048576)E^3`,

whereas (3.2) doubles that coefficient to

`63/524288`

without requiring `x2>=E/64`.

## 5. Relation to the global third-compound decomposition

A newer compatible fleet03/B02 theorem, source

`yspennstate/math-open-problems@c2a842f9cd113aa20d792ca1692a358fdc1be356`,

shows globally that the disjoint third-compound stratum can be converted by random original-coordinate coloring into a target-scale physical `E3` cut. That result leaves overlap strata `V1,V2,V3`. The present lemma is complementary rather than duplicative: it works inside the established `N3(1/64)` strong-cut chamber and shows that once D5 has forced top-four concentration, **any** tail of size `E/64` already creates enough third exterior mass, independent of whether the second singular value itself crosses `E/64`.

## 6. Stronger global Fourier criterion and remaining obstruction

I found no source-valid counterexample to a universal target-wide bound

`integral_R |E exp(it X^T A X)| dt <= C`.

Accordingly the stronger Fourier criterion remains `OPEN_NOT_REFUTED`.

The first unpaid B02 implication is now

`QFORM-STRONGCUT-NEARRANK2-OVERLAPPING-BANK-INTEGRATED-OR-DENSITY-v2`:

on the literal strong-cut block with

`E>11907/16384`, `T2<E/64`,

retain the small but nonzero cross tail exactly and combine the dominant rank-two crossing with the third curvature forced elsewhere by the full `s3(A)>=1` hypothesis. The r34 independent-square theorem pays this if the third curvature lives on a genuinely independent physical bank; the hard case is overlap with the rough product bank. The small cross tail cannot be deleted on unbounded inputs, and a general rotation cannot be used to manufacture independence.

The full QFORM density conjecture and full continuity remain **OPEN**.

## 7. Source / correction ledger

Consumed mathematical sources:

- strong physical cut: `math-open-problems@c6f29397b3d45a7cf7ab67633a5451767b478912`;
- D5 / optimized strong-cut continuation: `math-open-problems@674f13a108a33176aafffe8f9b6d44ec3a89f03a`;
- designated fleet02/B02 marginal-free E3 theorem: `math-open-problems@3fccd9b82b456e198758e5839be364b4b0ec5024`;
- compatible global disjoint-compound theorem: `math-open-problems@c2a842f9cd113aa20d792ca1692a358fdc1be356`.

Live correction boundaries honored include `QFORM-CROSSMINOR-ALONE-FALSE`, `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE`, `QFORM-UV-CONDITIONAL-CAP-FALSE`, `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1`, the arbitrary-joint coarea correction, the fiber-sup dimension-loss correction, and the law-uniform scalar pointwise-decay correction.

No schedule, task identity, notification, email, permission, model/API, public-release, or installation state was changed.
