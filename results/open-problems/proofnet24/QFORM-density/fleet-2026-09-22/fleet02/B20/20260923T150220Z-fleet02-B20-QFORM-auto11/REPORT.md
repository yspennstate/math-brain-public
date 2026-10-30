SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B20, 2026-09-23T15:02:20Z.
attacking: the newest fleet03/B20 absolute-rank-one nested three-bank survivor; prove a source-coordinate non-degenerate recursion and force its first curvature flip.

# fleet02/B20 — rank-one cross-tube self-replication and curvature-flip compressor

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T150220Z-fleet02-B20-QFORM-auto11`  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **ESSENTIAL_STEP_APPLIED / FULL QFORM OPEN / GLOBAL CONTINUITY OPEN**.

## 1. Scope and source pins

The target remains unrestricted: for every dimension, independent ORIGINAL real random variables with probability densities bounded by one, and every real symmetric `A` with at least three eigenvalues of absolute value at least one, prove one universal finite essential-supremum bound for the density of `X^T A X`, or give a valid target counterexample. No moment, compact-support, connected-support, Gaussian, log-concavity, iid, diagonal-basis, finite-rank, or post-rotation-independence hypothesis is added. Continuity is a separate conclusion.


The newest completed designated partner actually consumed is fleet03/B20 r33:

`yspennstate/math-open-problems@82fb3ecce909f03acbbe69b2e9d0def93f85194b`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B20/20260923T144528Z-fleet03-B20-QFORM-r33/REPORT.md`.

Its current N3 compiler uses an ORIGINAL-coordinate partition `S sqcup T=[n]`, `M=A[S,T]`, and after its already-paid fifth-volume / grouped-rank-three exits leaves an absolute-rank-one nested packet with

`E:=||M||_F^2 > E_*:=1241405/2097152`,                              (1.1)

`S_4(M) > (63/64)E`,                                                  (1.2)

`s_2(M)<1/64`.                                                        (1.3)

The same report also gives, on any absolute-rank-two descendant with `s_2>=1/64`, the determinant-law E2 cascade: high weighted disjointness yields a half-Riesz bound; low disjointness yields a paid physical pair or an anchored cofactor/double-star/large-core packet.

The required pinned interactive source was read both at the requested base commit `e5f71d79eff325201dd0274053d20268ce65b837` and in the latest compatible state of the same directory. In particular `FOURIER_ROUTE_REPORT.md` proves the unrestricted physical fifth-volume receiver

`||p_Q||_infinity <= 5 sqrt(2e) e_5(M^T M)^(-1/10)`                  (1.4)

for any literal ORIGINAL-coordinate cross block `M`, with arbitrary same-bank quadratic terms and outside couplings retained. This theorem is applied quantitatively in Section 4.

I also use the newer compatible fleet03/B06 r38 aggregate cofactor theorem

`yspennstate/math-open-problems@e83d0cc194d791acf31d6c86245204887cfd8171`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B06/20260923T144727Z-fleet03-B06-qform-r38/REPORT.md`,

only at its stated physical-coordinate scope in Section 5.

## 2. Rank-one tube forces a large same-bank block

Write `tau=1/64`. Let

`M_1=s_1 u v^T`

be the top singular component of `M`, and `R=M-M_1`. From (1.3),

`||R||_op=s_2(M)<tau`.                                                (2.1)

Form the symmetric rank-at-most-two matrix

`H=[[0,M_1],[M_1^T,0]]`

in the physical cut `S sqcup T`. Since the third singular value of the full symmetric `A` is at least one, the Eckart--Young operator-norm distance to matrices of rank at most two is at least one. Therefore

`1 <= s_3(A) <= ||A-H||_op
              <= max(||A[S,S]||_op,||A[T,T]||_op)+||R||_op`.

Using (2.1),

`boxed: max(||A[S,S]||_op,||A[T,T]||_op)>63/64.}`                    (2.2)

No random input is rotated here. The rank-one truncation is used only as deterministic coefficient geometry; the residual `R` remains in the actual quadratic form.

## 3. A large same-bank block reproduces the cross tube with a fixed energy floor

Let `C` be a physical side attaining (2.2), and let `R_0=C^c` be the old opposite bank. Since the N3 chamber has

`|A_ii|<1/64` for every physical coordinate,                               (3.1)

the zero-diagonal part

`H_C=A[C,C]-diag(A[C,C])`

satisfies

`||H_C||_op>63/64-1/64=31/32`,

hence

`||H_C||_F^2>961/1024`.                                               (3.2)

Randomly two-colour the ORIGINAL coordinates of `C` into `P sqcup Q`. Every off-diagonal physical edge is separated with probability `1/2`, and because `H_C` is symmetric with zero diagonal,

`E_color ||A[P,Q]||_F^2 = (1/4)||H_C||_F^2 >961/4096`.

Choose one realizing partition, so

`boxed: ||A[P,Q]||_F^2>961/4096.}`                                    (3.3)

Relabel the two colours so that `P` carries at least one half of the squared mass of the relevant top singular vector (`u` if `C=S`, `v` if `C=T`). From (1.2)-(1.3), writing `x_j=s_j(M)^2`,

`x_1 > (63/64)E-(x_2+x_3+x_4)
     > (63/64)E-3/4096.                                               (3.4)

The literal arm from `P` to the old opposite bank therefore satisfies

`||A[P,R_0]||_op^2 > (1/2)[(63/64)E-3/4096].`                         (3.5)

Now take the new ORIGINAL-coordinate cut

`P sqcup P^c = P sqcup (Q sqcup R_0)`

and its cross block

`M':=A[P,P^c]=[A[P,Q],A[P,R_0]]`.

The two column banks are disjoint, so (3.3)-(3.5) give the exact affine lower recursion

`boxed:
 E':=||M'||_F^2
 > 961/4096 + (1/2)[(63/64)E-3/4096]
 = 1919/8192 + (63/128)E
 =:F(E).}`                                                            (3.6)

The fixed point of `F` is

`boxed: E_infty = 1919/4160 =0.461298076923... .}`                    (3.7)

Consequently, if `E>=E_infty`, every still-unpaid absolute-rank-one reproduction again has

`E'>E_infty`.                                                         (3.8)

For the designated partner's actual input (1.1), the first reproduced cut has

`boxed:
 E'>141090307/268435456
   =0.525602351874... .}`                                             (3.9)

This is `QFORM-N3-RANK1-TUBE-SELF-REPLICATION-v1`. It is dimension-free and source-preserving: all cuts are made on original physical coordinates, and no small nonzero quadratic tail is removed.

## 4. The fixed floor can be spent uniformly at every reproduction

The point of (3.7) is that the already-completed physical receivers can be rerun at every descendant with constants that do not deteriorate with the number of reproductions.

### 4.1 Pinned fifth-volume payment

The current cross-cut compiler gives the deterministic fifth-volume lower bound

`e_5(M^T M) >= (1/64)^4 E^5/120`                                    (4.1)

whenever the top four squared singular values carry at most `(63/64)E`. At the fixed floor `E>=E_infty`, combine (4.1) with the pinned interactive D5 theorem (1.4):

`||p_Q||_infinity
 <=5sqrt(2e)[(1/64)^4 E_infty^5/120]^(-1/10)
 <146.229.`                                                          (4.2)

Thus every descendant that fails strong-top-four is fully paid, with a continuous `C_0` density at the source theorem's scope.

### 4.2 Third singular direction payment

If strong-top-four holds and `s_3(M)>=1/64`, then

`s_1^2>(63/256)E`, `s_2^2,s_3^2>=1/4096`,

so at `E>=E_infty`

`Delta_3:=s_1s_2s_3
 >sqrt((63/256)E_infty)/4096
 =8.22585720425...e-5.`                                               (4.3)

The completed grouped physical cross-rank-three receiver gives

`boxed: ||p_Q||_infinity<187.509.}`                                  (4.4)

### 4.3 Genuine second direction: uniform E2 currency

Suppose strong-top-four holds, `s_3<1/64`, but `s_2>=1/64`. Then exactly as in the designated partner's E2 gate,

`Z_2=e_2(M^TM)
 > (1/4096)[(63/64)E-1/2048-1/4096]`.

At `E>=E_infty`,

`boxed:
 Z_2 > z_infty:=60351/545259520
      =0.000110683074364... .}`                                      (4.5)

Applying the completed determinant-law receiver at weighted-disjointness threshold `1/256` gives either

`sup_t E|Q-t|^(-1/2)<41.184`,                                        (4.6)

or a physical-pair density payment `<546.895`, or a physical anchor with cofactor matrix

`C=bD-c r^T`

satisfying

`L:=||C||_F > gamma_infty
 :=sqrt((127/512)z_infty)
 =0.00523971284627... .`                                             (4.7)

In the non-pair branch `|b|<1/32`; the triangle inequality then gives either

`boxed: ||c||_2||r||_2>gamma_infty/2
       =0.00261985642313...}`                                        (4.8)

or

`boxed: ||D||_F>16gamma_infty
       =0.0838354055404... .}`                                       (4.9)

The half-Riesz estimate (4.6) is deliberately not promoted to a density bound.

## 5. New sharpening of the low-disjointness large-core branch

This section consumes fleet03/B06 r38 at an exact expression. Work in the low-disjointness cofactor state (4.7), assume `|b|<1/32`, and suppose the double-star alternative does not occur in its stronger actual form `||c||||r||>L/2`. Then

`||D||_F>16L`.                                                        (5.1)

In particular `b` cannot be zero: if `b=0`, then `C=-cr^T` and `||c||||r||=L`.

Apply r38's parametric cofactor theorem with the *state-dependent deterministic parameter*

`theta:=L^2`.                                                         (5.2)

If

`e_2(C^TC)>=b^2 L^4`,                                                 (5.3)

then the anchored three-volume satisfies `e_3(M^TM)>=L^4`. If one orientation of its canonical physical three-minor law has every row marginal at most `2/3`, the completed D-prime receiver gives

`||p_Q||_infinity
 <=9sqrt(3e)L^(-2/3)
 <9sqrt(3e)gamma_infty^(-2/3)
 <851.946.`                                                          (5.4)

If (5.3) holds but the diffuse marginal gate fails on both orientations, there is instead a physical row and physical column each contained in more than `2/3` of the canonical third-volume law: a nested double-anchor certificate.

If (5.3) fails, r38 gives

`dist_F(C,rank<=1)^2 <2L^2b^2 <L^2/512`,                             (5.5)

and

`dist_F(D,rank<=2)^2 <2L^2 < ||D||_F^2/128`,                         (5.6)

where (5.1) was used in the final inequality. Equivalently,

`boxed: s_1(C)^2/||C||_F^2>511/512,}`                                (5.7)

`boxed: [s_1(D)^2+s_2(D)^2]/||D||_F^2>127/128.}`                     (5.8)

Thus the low-disjointness large-core survivor is no longer an amorphous Frobenius-large block: it is either paid by `<851.946`, carries nested `>2/3` physical third-volume anchors, or consists of a `>99.80%`-energy rank-one cofactor feeding a `>99.21%`-energy rank-two residual physical core. No reciprocal individual minor is selected.

## 6. Infinite nesting is impossible without a curvature flip

It remains to understand descendants that avoid Sections 4.1-4.3 and so continue as strong-top-four absolute-rank-one tubes with energy `>E_infty`.

At each such step, Section 2 supplies a side `C` with `||A[C,C]||_op>63/64`; Section 3 splits it into nonempty physical banks `P sqcup Q` satisfying (3.3), and the next active cut is `P sqcup P^c`.

Call the next step a **same-side continuation** if its large same-bank block is again `A[P,P]`. Because (3.3) is positive, `Q` is nonempty, hence a same-side continuation strictly decreases the cardinality of the active bank. A singleton can never support another same-side continuation, since by N3

`||A[{i},{i}]||=|A_ii|<1/64<63/64`.

Therefore an unpaid pure-rank-one chain cannot continue on the same side forever. At some finite step it has a **curvature flip**: for the parent decomposition

`[n]=P sqcup Q sqcup R`,                                              (6.1)

where `C=P sqcup Q` was the parent active bank and `R=C^c`, one has simultaneously

`boxed: ||A[P sqcup Q,P sqcup Q]||_op>63/64,}`                       (6.2)

`boxed: ||A[Q sqcup R,Q sqcup R]||_op>63/64,}`                       (6.3)

`boxed: ||A[P,Q]||_F^2>961/4096,}`                                   (6.4)

and from (3.5), using the fixed floor,

`boxed:
 ||A[P,R]||_op^2
 > (1/2)[(63/64)E_infty-3/4096]
 =60351/266240
 =0.226678936298... ,}`                                              (6.5)

so

`||A[P,R]||_op>0.476108114085... .`                                  (6.6)

The current cross block `A[P,Q sqcup R]` still has energy `>E_infty`; if it were not strong-top-four, or had `s_3>=1/64`, or had `s_2>=1/64`, it would already have exited through Sections 4.1-4.3. Thus every still-unpaid curvature-flip packet also satisfies

`S_4(A[P,Q sqcup R])>(63/64)||A[P,Q sqcup R]||_F^2`,

`s_2(A[P,Q sqcup R])<1/64`.                                         (6.7)

This is `QFORM-N3-RANK1-TUBE-CURVATURE-FLIP-v1`. The number of preceding same-side steps is irrelevant: no analytic constant is spent during the deterministic descent, and the energy floor is invariant by (3.8).

## 7. Strongest current conditional closure graph

Inside the newest designated-partner N3 branch, every state is now routed into one of the following:

1. fifth-volume payment `<146.229` at the invariant energy floor;
2. grouped physical rank-three payment `<187.509`;
3. an E2 packet with half-Riesz `<41.184`, or physical-pair payment `<546.895`, or double-star / anchored-cofactor structure;
4. on the low-disjointness large-core subbranch, D-prime payment `<851.946`, nested `>2/3` third-volume anchors, or the quantitative cofactor/rank-two residual tube (5.7)-(5.8);
5. a finite curvature-flip three-bank packet (6.1)-(6.7).

The first unpaid implication after this run is therefore

`QFORM-N3-E2-OR-CURVATURE-FLIP-PAYMENT-v1`:

Under the full original independent cap-one product hypotheses and `N3(1/64)`, prove a universal linear small-ball / essential-density payment for the remaining E2 half-Riesz/double-star/nested-anchor/recursive-rank-two packets, or for the curvature-flip packet (6.1)-(6.7), while retaining arbitrary same-bank quadratic curvature, every extra spectral direction, and every small nonzero coefficient; alternatively route each quantitatively into an already completed physical pair, grouped-square/hub, ridge, or volume receiver.

The curvature-flip packet is strictly stronger than the previous indefinitely nested rank-one label: it contains two overlapping principal blocks of operator norm `>63/64`, a fixed internal physical cross energy, and a fixed strong arm, all in literal source coordinates.

## 8. Correction audit and status

No step uses uniform pointwise scalar stationary phase, an arbitrary-joint coarea bound, a worst-fiber density supremum, post-rotation independence, a moment assumption, a compact-support assumption, or deletion of a small random quadratic tail. The only rotations are deterministic singular-vector calculations on the coefficient matrix; every probabilistic bank is a set of original independent coordinates.

No target counterexample was found. Full QFORM remains **OPEN**. Global continuity remains **OPEN**; continuity is asserted only on branches whose cited Fourier receiver proves a continuous representative. This report is a conditional compiler advance, not a full candidate and therefore does not claim the two independent end-to-end reviews required for a complete proof.
