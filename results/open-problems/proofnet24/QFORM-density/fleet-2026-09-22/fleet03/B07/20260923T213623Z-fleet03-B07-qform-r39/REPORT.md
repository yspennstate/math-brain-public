SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B07, 2026-09-23T21:36:23Z.
attacking: source-audit the moving-E2-plane obstruction, then change mechanism after the preceding three interface-transfer runs: spend the global disjoint third-compound mass directly through a random physical bipartition and the new marginal-free Z3 crossing receiver.

# fleet03/B07 r39 — direct analytic payment of the overlap-zero third compound

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: coordinate minor selection / GEOMETRY  
Run: `20260923T213623Z-fleet03-B07-qform-r39`  
Fresh control at publication: `yspennstate/math-research-brain@7d2ad323cb8b2f1d1ac362f1c58dafb8f5f0fad1`  
Execution: `WITHOUT_VERIFIED_BRAIN`, `full_brain_connected=false`.  
Status: **NEW ANALYTIC CLOSURE OF THE O0/DISJOINT-THIRD-COMPOUND BRANCH / FULL QFORM OPEN / FULL CONTINUITY OPEN**.

The unrestricted conjecture is not proved or disproved here. No Gaussian, log-concave, moment, compact-support, connected-support, iid, post-rotation independence, pointwise van-der-Corput, arbitrary-joint coarea, fiber-supremum, or deletion of a small nonzero coefficient is used. All partitions below are literal original-coordinate partitions.

## 1. Duplicate-source audit and mechanism change

The planned incoming debt from r38 was `QFORM-MOVING-E2-PLANE-SYNCHRONIZATION-v1`. Before extending that mechanism, I source-searched the repository. This found my own earlier theorem

`yspennstate/math-open-problems@07ce749022db2bb11f390431409b013fe30457cc`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B07/20260923T000734Z-fleet03-B07-qform-r20/REPORT.md`,

which already proves the exact overlap decomposition

`E_q(A)=sum_{|I|=|J|=3, |I intersect J|=q} det A[I,J]^2`, `q=0,1,2,3`,

and finite-bank random-color selectors for all four overlap types. I therefore do **not** re-claim that coloring theorem. In accordance with the owner instruction to change mechanism after three closely related substantive runs, this run instead closes the entire `q=0` branch analytically using a receiver that did not exist when r20 was written.

The analytic dependency is fleet02/B03's completed theorem `QFORM-Z3-CROSSING-MARGINAL-FREE-v1`, available at the fresh master snapshot

`yspennstate/math-open-problems@df4894c85a1e34f832685aaf85ac05bbecc24b7e`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B03/20260923T184716Z-fleet02-B03-QFORM-auto11/REPORT.md`.

For every genuine original-coordinate cut `L sqcup R=[n]`, writing `K=A[L,R]` and

`Z3=e_3(KK^T)=sum_{I subset L,J subset R, |I|=|J|=3} det A[I,J]^2`,

that theorem gives, for `Z3>0`,

`||p_Q||_infinity <= C3 Z3^(-1/6)`,

`C3=3*2^(4/3)*e^(1/3)=10.5501688311648...`,

with a **continuous** density. Arbitrary same-side quadratic blocks, arbitrary affine terms, and all additional spectrum are retained.

## 2. Total third-compound currency

For a real symmetric `A`, Cauchy--Binet gives

`M3tot := ||wedge^3 A||_F^2
       = sum_{|I|=|J|=3} det A[I,J]^2
       = e_3(A^2)
       = sum_{a<b<c} lambda_a^2 lambda_b^2 lambda_c^2`,              (2.1)

where `lambda_a` are the eigenvalues of `A`. Under the owner hypothesis, at least three satisfy `|lambda|>=1`, hence

`M3tot >= 1`.                                                        (2.2)

Let

`E0(A):=sum_{|I|=|J|=3, I intersect J=emptyset} det A[I,J]^2`.       (2.3)

This is exactly the overlap-zero part of r20's ledger.

## 3. Main theorem — `QFORM-O0-DIRECT-Z3-PAYMENT-v1`

### Theorem

For every real symmetric `A` and independent original coordinates with marginal densities at most one, if `E0(A)>0`, the full quadratic form `Q=X^T A X` has a continuous density satisfying

`boxed: ||p_Q||_infinity <= 2 C3 E0(A)^(-1/6).`                      (3.1)

Equivalently every interval `J` obeys

`P{Q in J} <= 2 C3 E0(A)^(-1/6) |J|`.                               (3.2)

In particular, under `s_3(A)>=1`, if

`E0(A)>=1/4`,                                                        (3.3)

then

`boxed: ||p_Q||_infinity
        <= C3*2^(4/3)
        =3*2^(8/3)*e^(1/3)
        =26.5847595806586... .`                                      (3.4)

Thus every still-unpaid target instance may be restricted, without loss, to

`E0(A)<1/4`,                                                         (3.5)

and hence by (2.2)

`E1(A)+E2(A)+E3(A)>3/4`.                                             (3.6)

Combining (3.6) with the already-proved r20 coloring theorem, at least one of the still-overlapping packets obeys the same macroscopic threshold as before:

- one-shared packet `P1>1/3125`, or
- two-shared packet `P2>1/512`, or
- principal-triple packet `P3>1/18`.

The disjoint overlap class no longer belongs to the structural debt.

### Proof

Color every original coordinate independently `L` or `R`, each with probability `1/2`, and put

`K=A[L,R]`.

By Cauchy--Binet,

`Z3(L,R)=e_3(KK^T)
 =sum_{I subset L,J subset R, |I|=|J|=3} det A[I,J]^2`.              (3.7)

Fix an ordered pair `(I,J)` of disjoint triples. The event `I subset L` and `J subset R` has probability exactly `2^(-6)=1/64`. Therefore Tonelli gives the exact expectation identity

`E_color Z3(L,R)=E0(A)/64`.                                         (3.8)

Hence some literal physical bipartition satisfies

`Z3(L,R)>=E0(A)/64`.                                                 (3.9)

Apply `QFORM-Z3-CROSSING-MARGINAL-FREE-v1` to that actual crossing. It applies to the **full** quadratic form with the untouched blocks `A[L,L]` and `A[R,R]`, so there is no Schur-random-vector substitution and no post-rotation independence claim. Equations (3.9) and the receiver give

`||p_Q||_infinity
 <= C3 (E0/64)^(-1/6)
 =2 C3 E0^(-1/6)`,                                                   (3.10)

because `64^(1/6)=2`. The source theorem supplies continuity. If `E0>=1/4`, then `E0^(-1/6)<=4^(1/6)=2^(1/3)`, giving (3.4). QED.

## 4. High-small-ball-ratio contrapositive

The interval form (3.2) is useful even before one assumes existence of a density. If some interval `J` has slab ratio

`rho=P{Q in J}/|J|`,                                                 (4.1)

then every `E0>0` instance obeys

`rho <= 2 C3 E0^(-1/6)`.                                            (4.2)

Therefore a high-ratio survivor must satisfy

`boxed: E0(A) <= (2 C3/rho)^6.`                                     (4.3)

So an attempted counterexample sequence with `rho -> infinity` must drive the entire disjoint third-compound energy to zero at least as `rho^(-6)`, while total third-compound energy stays at least one. Its volume is forced quantitatively into the one-shared, two-shared, or principal overlap geometries. This is a target-level restriction, not a one-minor selection.

## 5. Actual designated-partner inequality

The completed designated partner fleet04/B07 result is source-pinned at

`yspennstate/math-open-problems@842652e93680813d356fde0f15f12ab70b59c3c3`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B07/20260923T091740Z-fleet04-B07-actual-core-diffuse-banks-r1/REPORT.md`.

In its strict-N3 chamber it applies the original-coordinate coefficient cap at

`h=(2sqrt(2)-1)/1572864=1.1624826588606455e-6`,

and with `tau0=h^2/128` obtains the physical off-diagonal bound

`|A_ij|<=h/8`.                                                       (5.1)

Apply (5.1) to the **actual new O0 branch**. Every entry of a disjoint `3x3` minor `A[I,J]` is off diagonal because `I intersect J=emptyset`. Hence every row of that minor has Euclidean norm at most `sqrt(3)h/8`, and Hadamard gives

`|det A[I,J]|^2 <= (sqrt(3)h/8)^6
                  =27 h^6/262144`.                                  (5.2)

Consequently, if the macroscopic O0 branch `E0>=1/4` occurs, the number `N0` of nonzero literal ordered disjoint physical `3x3` minors satisfies

`boxed: N0 >= ceil(65536/(27 h^6))
             =983551868769506981504265073786003390464.`              (5.3)

Since the total number of ordered disjoint triple pairs is

`binom(n,3) binom(n-3,3)`,                                          (5.4)

the same branch in the strict-N3 chamber forces

`boxed: n>=5730381.`                                                 (5.5)

This is a genuine equation-level use of the designated partner result. It is not needed to prove the density estimate (3.4); rather, it shows that any strict-N3 realization of the newly paid O0 branch is necessarily **extremely diffuse** in physical coordinates. No Monte Carlo or one-lucky-minor inference is involved.

The newer designated partner theorem

`yspennstate/math-open-problems@dab16464e87c939cc0cf3fd01d070045290192fa`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B07/20260923T161510Z-fleet04-B07-coordinate-core-r2/REPORT.md`

was also scope-checked. Its diagonal-plus-rank core payment is not invoked here because the O0 crossing branch does not supply the required collection of large physical diagonal pivots.

## 6. Relation to the r38 moving-plane chamber

The r38 theorem remains valid. Its unpaid moving-plane synchronization chamber is no longer the only lens through which to attack the same target: the present global theorem first removes every instance with `E0>=1/4`, regardless of what its row-deleted E2-heavy planes do. Therefore any continuation of r38 may assume simultaneously

`E0<1/4`,

`E1+E2+E3>3/4`,

and the r38 moving-plane conditions if that branch is still being followed.

This is precisely the requested mechanism change after the r36--r38 interface-transfer sequence.

## 7. What remains

The next coordinate-minor debt is

`QFORM-OVERLAP123-ANALYTIC-COMPILER-v1`:

starting from (3.6) and the already-proved r20 packets, consume at least one of

1. the one-shared packet `P1>1/3125`, retaining exact-zero and genuine nonzero scalar-pivot pieces without selecting one pivot;
2. the two-shared packet `P2>1/512`, retaining singular and invertible physical-pair pieces and the exact pair-Schur first-compound weight;
3. the principal-triple packet `P3>1/18`, without inferring one uniformly conditioned principal triple.

The newest fleet02/B03 one-hub/two-volume receiver is a natural analytic candidate for parts of item 1, but no implication from the r20 bordered determinants to its projected `S^2 Z2` currency is asserted here without proof.

Full QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**. Full-target continuity remains **OPEN**. Continuity is proved on the entire `E0>0` branch by (3.1), but forms with `E0=0` include target-valid rank-three bank examples and still require the overlap receivers.

## 8. Exact regression checks

`CHECKS.py` performs exact integer arithmetic on random symmetric integer matrices of size six. It verifies:

- `sum_q E_q(A)=e_3(A^2)` using the Newton trace formula;
- the exact Bernoulli-bipartition identity `64 sum_color Z3 = 2^n E0`;
- the older r20 one-shared and two-shared coloring expectation identities, to ensure the downstream thresholds quoted after removing O0 are unchanged;
- the numerical constants in (3.4), (5.3), and the exact minimal dimension in (5.5).

Twelve independent integer regression instances pass exactly. These computations are regression evidence only; the proof of (3.1) is the exact Cauchy--Binet expectation plus the completed analytic receiver.
