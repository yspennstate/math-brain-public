# Current-state addendum — splice with the already-completed same-hour B20 compiler

This addendum supersedes only the proof-graph ordering in `REPORT.md`; all mathematics proved there remains valid. The same-hour canonical B20 run `20260923T150220Z-account02-B20-QFORM-auto11` had already completed before this invocation and is newer than the previously consumed local state. Its canonical report is `yspennstate/math-open-problems@f4e997fa4f98146cfe958ca34a1c397b413d5184`. It proves source-coordinate rank-one-tube self-replication at the fixed energy floor

`E_infty = 1919/4160`,

and forces every unpaid pure rank-one chain to reach a finite curvature-flip packet. The theorem below applies the new tail-volume argument from this invocation uniformly to **every descendant** of that chain.

## 1. Uniform Frobenius collar on every unpaid rank-one descendant

Let an unpaid descendant have literal physical cross block `W`, energy `E=||W||_F^2>=E_infty`, satisfy strong-top-four, and satisfy `s2(W)<1/64`. Write

`W=s1 u v^T+R`,  `||R||_op=s2(W)<1/64`,  `T=||R||_F^2`.

The same-hour compiler gives, for the squared singular values,

`s1^2 > (63/64)E - 3/4096`.

At the fixed floor this yields the exact bound

`boxed: s1^2 > (63/64)(1919/4160)-3/4096 =60351/133120.}`              (1.1)

Assume `T>=1/64`. Since every tail square is `<1/4096`, the bounded-coordinate fourth-volume lemma proved in `REPORT.md` gives

`e4(s2^2,s3^2,...)`
` >=(1/64)(63/4096)(62/4096)(61/4096)/24.`                              (1.2)

Therefore

`e5(W^T W)`
` >=s1^2 e4(s2^2,s3^2,...)`
` > (60351/133120)(1/64)(63/4096)(62/4096)(61/4096)/24`
` =2396598561/2341871806232657920`
` =1.0233688089252761e-9.`                                               (1.3)

Apply the pinned unrestricted physical D5 receiver to this **actual original-coordinate cross block**. It gives

`||p_Q||_infinity`
` <5 sqrt(2e) (2396598561/2341871806232657920)^(-1/10)`
` =92.3908633722... <92.391.`                                            (1.4)

Hence every still-unpaid descendant obeys

`boxed: ||R||_F^2<1/64, equivalently ||R||_F<1/8.}`                     (1.5)

This is `QFORM-N3-SELFREPLICATING-RANK1-FROBENIUS-COLLAR-v1`. It upgrades the current chain from an operator-norm rank-one tube to a dimension-free Frobenius rank-one tube without deleting the residual random term.

## 2. Sharpened curvature-flip packet

The same-hour compiler forces a finite original-coordinate partition

`[n]=P disjoint_union Q disjoint_union R0`

with

`||A[P union Q,P union Q]||_op>63/64`,                                  (2.1)

`||A[Q union R0,Q union R0]||_op>63/64`,                                (2.2)

`||A[P,Q]||_F^2>961/4096`,                                               (2.3)

`||A[P,R0]||_op^2>60351/266240`,                                         (2.4)

and current cross block

`W=A[P,Q union R0]`

still in the unpaid strong-top-four, `s2(W)<1/64` chamber.

Apply (1.5) and write `W=s1 u(v_Q,v_R)^T+Rtail`. From (2.3),

`s1||v_Q|| >= ||A[P,Q]||_F-||Rtail_Q||_F`
` >31/64-1/8 =23/64.`                                                    (2.5)

From (2.4) and `||Rtail_R||_op<1/64`,

`s1||v_R||`
` > sqrt(60351/266240)-1/64`
` =0.4604831140855... .`                                                 (2.6)

Thus the **same deterministic top rank-one factor** simultaneously carries two fixed literal physical arms. No independence of `u^T X_P`, `v_Q^T X_Q`, or `v_R^T X_R` is asserted.

The transverse-curvature lemma proved in this invocation also applies to the current cut. Put `B=A[P,P]`, `C=A[Q union R0,Q union R0]`, `beta=u^TBu`, and `gamma=v^TCv`. The rank-at-most-two matrix

`H=[[beta uu^T,s1uv^T],[s1vu^T,gamma vv^T]]`

satisfies, by `s3(A)>=1` and `||Rtail||_op<1/64`,

`boxed: max(||B-beta uu^T||_op, ||C-gamma vv^T||_op)>63/64.}`            (2.7)

Equivalently the third large spectral direction cannot be absorbed into the aligned rank-one two-bank geometry: after subtracting the longitudinal scalar curvature on the top cross singular vectors, a same-bank transverse operator of fixed size remains. As shown in `REPORT.md`, this further implies a transverse star or compression `>63/128` and a literal internal physical cross cut with Frobenius-square `>3721/65536` on one side.

## 3. Updated first unpaid implication

The global first unpaid edge must retain the unresolved E2 branches from the same-hour compiler. It is now sharpened to

`QFORM-N3-E2-OR-THIN-CURVATURE-FLIP-PAYMENT-v1`:

> Under the original independent cap-one product-source hypotheses, `A in N3(1/64)` and `s3(A)>=1`, prove a universal essential-density bound or source-preservingly route to an existing paid receiver for every remaining state consisting either of the current E2 half-Riesz / double-star / nested-anchor / rank-two-core branches, or of a curvature-flip packet `P,Q,R0` satisfying (2.1)-(2.4), with current cross block `W=A[P,Q union R0]` strong-top-four and `s2(W)<1/64`, together with the new quantitative collar `||W-s1uv^T||_F<1/8`, two-arm bounds (2.5)-(2.6), and transverse same-bank curvature (2.7). Arbitrary same-bank quadratic blocks, all nonzero tails, outside couplings and extra spectrum must be retained.

The next useful mechanism should combine the two top-rank-one arms with the transverse same-bank operator **before reciprocal inversion**. A small-coefficient perturbation argument remains invalid.

Full QFORM remains OPEN. No target counterexample is claimed. Global continuity remains OPEN separately.
