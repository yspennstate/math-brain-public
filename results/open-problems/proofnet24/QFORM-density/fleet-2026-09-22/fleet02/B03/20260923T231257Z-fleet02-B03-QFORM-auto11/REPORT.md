SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B03, 2026-09-23T23:12:57Z.
attacking: the singular conjugate-difference-curvature corner — exhibit a target-valid family where every physical 2D determinant receiver degenerates, then promote to a genuine 3-coordinate localized receiver and recover a uniform whole-copy fractional-time bound.

# fleet02/B03 — double-singular conjugate corner paid by 3-coordinate promotion

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Classification:** `NEW SUPPORTING THEOREM / SOURCE-VALID OBSTRUCTION / PINNED RESULT APPLIED / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The unrestricted QFORM conjecture remains OPEN. The result below is deliberately narrower: it closes a concrete singular/near-singular corner singled out by the newest fleet03/B03 theorem and proves that a purely 2-dimensional determinant dichotomy cannot be the exhaustive bridge. It preserves the dependence of conjugate sum/difference variables throughout.

## 1. First unpaid implication attacked

The newest designated partner report is

`yspennstate/math-open-problems@545738ea4ac5730dc20e6ed5f50315dfcf3322f1`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B03/20260923T215603Z-fleet03-B03-QFORM-r41/REPORT.md`.

Its `QFORM-CONJUGATE-DIFFERENCE-CURVATURE-HALFRIESZ-v1` theorem considers the genuinely dependent conjugate pair

`U=X-X'`, `V=X+X'`

but expands the sum back in the genuinely independent original banks `(X,X')`. With symmetric `P_-,P_+`, it sets

`H=P_-+P_+`, `K=P_+-P_-`,

and proves that when `K` is invertible,

`sup_s E|R_-(U)+R_+(V)-s|^{-1/2} <= 4sqrt(2)|det K|^{-1/4}`,

with the corresponding whole-copy weighted-time bound. Its explicit remaining endpoint is `det K -> 0`, especially where no quantitatively invertible same-bank 2D quadratic matrix is available either.

The first question here is therefore not to repeat the invertible theorem, but to test whether that mixed singular corner can force a new pathology or whether a product-preserving promotion pays it.

## 2. A one-parameter double-singular family

Fix `lambda>=1` and `|delta|<=lambda/2`. Let

`S=[[0,1],[1,0]]`,
`P_- = lambda S`,
`P_+ = (lambda+delta) I_2`.

Let `X=(X_1,X_2)` and `Y=(Y_1,Y_2)` have four mutually independent scalar coordinates, each with density at most one. To match the conjugate interpretation one may take `Y` to be an independent copy of `X`; the density estimate below does not need equality of the laws. Put

`U=X-Y`, `V=X+Y`.

The pair `(U,V)` is dependent. Define

`Q_delta = U^T P_- U + V^T P_+ V`.

Write `a=lambda+delta`. Exact expansion in the original product coordinates gives

`Q_delta = X^T H X + Y^T H Y + 2 X^T K Y`,

where

`H=[[a,lambda],[lambda,a]]`,
`K=[[a,-lambda],[-lambda,a]]`.

Thus the physical `4 x 4` matrix is

`A_delta = [[H,K],[K,H]]`.

No probabilistic independence of `U,V` is used or asserted.

## 3. All physical 2D determinant receivers degenerate together

Both conjugate matrices have the same determinant:

`det H = det K = a^2-lambda^2 = delta(2lambda+delta)`.                 (3.1)

At `delta=0`, both are singular. More strongly, direct enumeration of the actual physical coordinates gives:

- every physical `2 x 2` principal determinant is either `0` or `delta(2lambda+delta)`;
- for the three physical partitions into two 2-coordinate banks, the cross-block determinants are
  `delta(2lambda+delta)`, `0`, and `-delta(2lambda+delta)`.

Hence at the exact singular point **every** physical 2D determinant certificate is zero. As `delta -> 0`, the best possible physical 2D determinant is only order `lambda |delta|`.

Applying the newest fleet03/B03 theorem where it is legal gives the actual comparison

`sup_s E|Q_delta-s|^{-1/2}
 <= 4sqrt(2)|delta(2lambda+delta)|^{-1/4}`                            (3.2)

for `delta != 0`. The right side diverges as `delta ->0`, and the theorem is silent at `delta=0`. This is not a failure of that theorem; it is an exact source-valid witness for the endpoint it leaves open.

The same family also rules out repairing (3.2) merely by switching from the difference-curvature determinant to another fixed physical two-bank determinant: all such determinants vanish together at `delta=0`.

## 4. Yet the family is strongly inside the owner target

The block Hadamard transform gives the deterministic algebraic decomposition

`H+K=2P_+=2a I_2`,
`H-K=2P_-=2lambda S`.

Therefore

`spec(A_delta)={2a,2a,2lambda,-2lambda}`.                            (4.1)

This is only a matrix spectral calculation; the product probability law is never rotated. Since `|delta|<=lambda/2` and `lambda>=1`, all four eigenvalues have modulus at least one. Thus this is a genuine owner-target family, not a lower-rank toy outside the conjecture.

## 5. Three-coordinate promotion is uniformly nondegenerate

Every physical `3 x 3` principal block has the same characteristic polynomial

`(2a-t)(t^2-a t-2lambda^2)`.                                        (5.1)

Hence its eigenvalues are

`2a`,
`(a+sqrt(a^2+8lambda^2))/2`,
`(a-sqrt(a^2+8lambda^2))/2`.                                        (5.2)

The negative root has magnitude

`m(a)=4lambda^2/(sqrt(a^2+8lambda^2)+a)`.                            (5.3)

For `a in [lambda/2,3lambda/2]`, this is minimized at `a=3lambda/2`, so

`m(a) >= c0 lambda`,
`c0 = 8/(sqrt(41)+3) = 0.8507810593...`.                             (5.4)

The other two eigenvalues have still larger modulus. Thus every physical triple satisfies

`min |eig(A_delta[T,T])| >= c0 lambda`.                              (5.5)

This is exactly where the required pinned source gives a completed receiver.

## 6. Required pinned result applied to an actual inequality

The required package

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

was read at `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. Its `COUNTEREXAMPLE_SEARCH.md` Theorem A states, with arbitrary affine terms allowed, that a physical principal `3 x 3` block whose three eigenvalues have modulus at least `c` gives

`||p_Q||_infty <= 6sqrt(pi)/c`.                                      (6.1)

Applying (6.1) to (5.5) yields the actual uniform bound

`boxed:
 ||p_{Q_delta}||_infty
 <= [3(3+sqrt(41))/4] sqrt(pi) lambda^{-1}
 = 12.4999528239... lambda^{-1}.`                                   (6.2)

Consequently every interval `I` obeys the requested linear one-copy small-ball estimate

`boxed:
 P(Q_delta in I)
 <= [3(3+sqrt(41))/4] sqrt(pi) lambda^{-1} |I|.`                     (6.3)

At the exact double-singular point `delta=0`, every physical triple has spectrum

`{-lambda,2lambda,2lambda}`,

so the sharper pinned bound is

`boxed: ||p_{Q_0}||_infty <= 6sqrt(pi)/lambda.`                      (6.4)

This is a nonperturbative payment of the exact singular point. No moment, support, log-concavity, diagonal-basis assumption, or post-rotation independence has entered.

## 7. Fractional potential and the assigned whole-copy time integral

The localized density bound can be converted back into the B03 fractional-time quantity without splitting any conjugate pair.

For any scalar random variable `Z` with density cap `M`, layer cake gives, uniformly in `s`,

`E|Z-s|^{-1/2}
 = int_0^infty P(|Z-s|<u^{-2}) du
 <= int_0^infty min(1,2M u^{-2}) du
 = 2sqrt(2M).`                                                       (7.1)

With `M` from (6.2),

`boxed:
 sup_s E|Q_delta-s|^{-1/2}
 <= pi^(1/4) sqrt(18+6sqrt(41)) lambda^{-1/2}
 = 9.99998112954... lambda^{-1/2}.`                                 (7.2)

Thus, on this near-singular family, the apparent `|det K|^{-1/4}` blow-up in (3.2) is not a blow-up of the actual fractional potential; a physical 3-coordinate promotion removes it uniformly.

Now let `Q_delta'` be an independent copy of the **whole scalar variable** `Q_delta`. Since

`p_{Q_delta-Q_delta'} = p_{Q_delta} * \widetilde p_{Q_delta}`,        (7.3)

`||p_{Q_delta-Q_delta'}||_infty <= ||p_{Q_delta}||_infty=M`. Hence (7.1) applies to the whole difference. Using only the exact whole-copy identity

`|phi_{Q_delta}(t)|^2
 = E exp(it(Q_delta-Q_delta'))`                                       (7.4)

and the positive-regularized Riesz identity

`int_R |t|^{-1/2} e^{itx} dt = sqrt(2pi)|x|^{-1/2}`,                 (7.5)

we obtain

`boxed:
 int_R |t|^{-1/2}|phi_{Q_delta}(t)|^2 dt
 <= 2 pi^(3/4) sqrt(9+3sqrt(41)) lambda^{-1/2}
 = 25.0662354451... lambda^{-1/2}.`                                 (7.6)

No coordinate sum and its conjugate difference are separated or declared independent. The dependence of `(U,V)` is preserved; only `Q_delta'` is an independent copy of the entire scalar output.

There is also a linear collision small-ball bound

`boxed:
 P(|Q_delta-Q_delta'|<=r)
 <= [3(3+sqrt(41))/2]sqrt(pi) lambda^{-1} r
 = 24.9999056478... lambda^{-1} r.`                                 (7.7)

At `delta=0`, (6.4) improves (7.6) to

`boxed:
 int_R |t|^{-1/2}|phi_{Q_0}(t)|^2 dt
 <= 4sqrt(6) pi^(3/4) lambda^{-1/2}
 = 23.1205425476... lambda^{-1/2}.`                                 (7.8)

## 8. What this changes in the proof graph

This family proves a precise obstruction and a precise repair.

The obstruction is:

> `invertible difference curvature OR another invertible physical 2D determinant`

cannot be an exhaustive reduction of the r41 singular endpoint. At `delta=0`, both `H` and `K` are singular, every physical `2 x 2` principal determinant is zero, and every physical `2+2` cross determinant is zero, even though the matrix has four eigenvalues of modulus at least one.

The repair on this family is to **promote by one physical coordinate before paying reciprocal determinant cost**. Every physical triple is then uniformly conditioned, and the pinned localized theorem supplies a universal density bound. This is compatible with the older correction that there is no universally well-conditioned physical triple in the full target: the present statement is only a receiver for this mixed singular family, not a universal extraction theorem.

## 9. First remaining B03 implication

The singular/near-singular difference-curvature gap is therefore narrower than in r41. One needs a structural alternative for a general owner-target matrix in the mixed endpoint where all candidate 2D determinants are small:

1. expose a quantitatively nondegenerate physical `3 x 3` principal block and use the localized theorem above; **or**
2. if every physical triple is also bad, aggregate original coordinates into a grouped-hub / low-rank-carrier / projected-volume receiver already proved elsewhere.

The second alternative is essential because existing exact families show that the three-large-eigenvalue hypothesis does not force one uniformly good physical triple or one rank-three physical cross cut. Thus the next unpaid statement is not a missing Fourier exponent; it is a product-preserving **3-coordinate-or-aggregate structural bridge** through the double-singular collar.

Continuity is not claimed from the density-to-half-Riesz argument here. The full unrestricted QFORM conjecture remains OPEN.

## 10. Sources and scope

- Required pinned mathematical package: `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, especially `COUNTEREXAMPLE_SEARCH.md` Theorem A, with `RESULTS.md` and `FOURIER_ROUTE_REPORT.md` also read.
- Designated partner theorem actually used for the endpoint comparison: `yspennstate/math-open-problems@545738ea4ac5730dc20e6ed5f50315dfcf3322f1`, fleet03/B03 r41.
- Current continuation also confirms that the unrestricted theorem is still OPEN and warns against independence after rotation and small-random-error interpretations of small matrices.

All spectral diagonalizations above are deterministic matrix identities only. All probability estimates stay in genuine original independent coordinates.
