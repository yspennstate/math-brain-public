SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B02, 2026-09-23T00:46:23Z.
attacking: integrated Fourier estimate — close the clustered high-volume-row collar by an exact exterior-factor identity and fleet02/B02's gate-free D5 Fourier compiler.

# fleet01/B02 QFORM r18 — clustered-pair exterior compiler

**Status:** `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN / WITHOUT_VERIFIED_BRAIN`.

The full target remains: independent real coordinates with densities bounded by one, arbitrary real symmetric A, and at least three eigenvalues of modulus at least one. No moment, support, log-concavity, Gaussian, post-rotation independence, or pointwise scalar oscillatory-decay assumption is used below. The theorem proved here is a supporting conditional Fourier theorem, not the unrestricted result.

## 1. Conditional end-to-end statement first

Let `M=A[I,J]` be any ORIGINAL-coordinate physical cross block and put

`Z3=e_3(M^T M)>0`.

Use the natural order-three row-volume law

`P(S)=det(M_S M_S^T)/Z3`,  `|S|=3`.

Suppose a row `i` lies in a random volume triple with probability `alpha_i>=3/4`, and under conditioning on `i in S` some second row `j` has conditional inclusion probability at least `1/2`. Let `r_i,r_j` be these two physical rows, let

`Delta^2=det Gram(r_i,r_j)`,

let `P_perp` be the orthogonal projection in coefficient space onto the orthogonal complement of `span(r_i,r_j)`, and let `N` be the matrix whose rows are `P_perp r_l`, `l notin {i,j}`. Write

`L=||N||_F^2`.

Then the exact identities below imply

`Delta^2 L >= (3/8) Z3`.                                           (1.1)

If in addition

`sr(N)>=5/2`,                                                       (1.2)

then

`Z5=e_5(M^T M) >= (3/250) Z3 L^2`.                               (1.3)

Apply the completed fleet02/B02 gate-free D5 theorem

`||p_Q||_infinity <= (5e/sqrt(2)) Z5^(-1/10)`                    (1.4)

for the SAME physical cross block M. Therefore

`boxed(
 ||p_Q||_infinity
 <= (5e/sqrt(2)) (250/3)^(1/10) Z3^(-1/10) L^(-1/5)
 < 14.957 Z3^(-1/10)L^(-1/5).
)`                                                                  (1.5)

The D5 characteristic-function envelope is integrable, so this branch has a **continuous density** (indeed vanishing at infinity), not merely an essentially bounded representative.

Hence for every threshold `tau>0`, the unresolved clustered-heavy case has the rigorous trichotomy:

1. if `L>=tau` and `sr(N)>=5/2`, (1.5) closes the branch by direct unweighted Fourier;
2. if `L<tau`, then the same exact identity forces the physical two-row area
   `Delta^2 >= 3 Z3/(8 tau)`;
3. otherwise `sr(N)<5/2`, i.e. the transverse packet is quantitatively low-effective-rank.

This converts the current multirow co-heaviness obstruction into either a paid D5 Fourier branch, a genuinely strong physical rank-two pair, or a low-effective-rank transverse packet. No fixed tiny minor is selected and no random-variable rotation is made.

## 2. Exact exterior-factor identity

Let a real matrix M have row vectors `r_s`. Fix a linearly independent row set `H` of size d. Put

`G_H=Gram((r_h)_(h in H))`, `Delta_H^2=det G_H`,

and let `P_H` denote orthogonal projection in the COLUMN/COEFFICIENT Euclidean space onto `span{r_h:h in H}^perp`. Let `N_H` be the matrix with rows `P_H r_l`, for `l notin H`.

For every integer `k>=d`,

`boxed(
 sum_(S superset H, |S|=k) det(M_S M_S^T)
 = Delta_H^2 e_(k-d)(N_H^T N_H).
)`                                                                  (2.1)

Proof. For `S=H union T`, the block Gram matrix of the rows in S has upper-left block `G_H`. Its Schur complement is exactly the Gram matrix of the projected rows `(P_H r_l)_(l in T)`. Therefore

`det(M_S M_S^T)=Delta_H^2 det((N_H)_T (N_H)_T^T)`.

Sum over all `|T|=k-d` and use Cauchy--Binet,

`sum_|T|=m det((N_H)_T(N_H)_T^T)=e_m(N_H^T N_H)`.

This proves (2.1). The projection is used only to evaluate Gram determinants; it is NOT a change of random coordinates and creates no independence assertion.

## 3. The clustered pair identity

Take `H={i,j}`, d=2. Let

`gamma=P(i,j in S)`

under the natural order-three volume law. Formula (2.1) at k=3 gives

`gamma Z3 = Delta^2 e_1(N^T N)=Delta^2 ||N||_F^2=Delta^2 L`.       (3.1)

Now

`gamma=P(i in S)P(j in S | i in S)=alpha_i a_j`.

Thus `alpha_i>=3/4` and `a_j>=1/2` imply

`gamma>=3/8`,

which proves (1.1).

This exact identity is the key new structural step. It says the clustered Pluecker/volume mass cannot disappear into many tiny local triples: it is exactly the product of one physical two-row area and the TOTAL transverse squared energy after that pair.

## 4. From clustered pair mass to fifth exterior volume

Formula (2.1) at k=5 gives the exact contribution of all five-row minors containing the pair:

`sum_(S superset {i,j}, |S|=5) det(M_S M_S^T)
 =Delta^2 e_3(N^T N).`                                            (4.1)

Since every term in the full Cauchy--Binet sum for `Z5=e_5(M^T M)` is nonnegative,

`Z5 >= Delta^2 e_3(N^T N)`.                                      (4.2)

Let the squared singular values of N be `x_l`, with `sum x_l=L`. The capped-simplex lemma proved in fleet01/B02 r16 states that if

`sr(N)=L/max x_l >= 2+delta`,  `0<delta<=1`,

then

`e_3(N^T N) >= [delta/(2+delta)^3] L^3`.                          (4.3)

At `delta=1/2` this is

`e_3(N^T N) >= (4/125)L^3`.                                      (4.4)

Combining (4.2), (4.4), and (3.1),

`Z5 >= (4/125) Delta^2 L^3
     = (4/125)(Delta^2L)L^2
     = (4/125) gamma Z3 L^2
     >= (3/250) Z3 L^2`,                                         (4.5)

which is (1.3).

A useful interpretation is that an order-three volume law with two clustered rows reaches the gate-free order-five Fourier theorem precisely when the transverse packet supplies three exterior directions. Order four would be the q=2 endpoint `|t|^-1`; order five moves strictly into L1. Thus the appearance of `e_3(N^T N)` is not cosmetic: it is the exact exterior resource needed to cross the unweighted Fourier threshold after two rows have become coloops.

## 5. Completed partner result applied to an actual inequality

The completed partner result used here is fleet02/B02 r16:

`yspennstate/math-open-problems@49c80441f24d6c697350119fac09426077b7e313`
`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B02/20260922T231047Z-fleet02-B02-qform-r16-6c4f9a1e/REPORT.md`.

Its D5 branch states, for any physical cross block M and arbitrary same-bank curvature/outside couplings,

`||p_Q||_infinity <= (5e/sqrt(2)) Z5^(-1/10)`,                    (5.1)

with an integrable characteristic-function envelope and no row-marginal gate. Insert (4.5) into (5.1) to obtain (1.5). Numerically

`(5e/sqrt(2))(250/3)^(1/10)=14.9565478177...`.

This is an equation-level application of the named partner theorem, not a parallel restatement.

## 6. Relation to the newest mixed-order result

Fleet01/B01's newest mixed-order theorem closes a heavy 3-volume row whenever its conditional co-marginals can be rebalanced below 1/2. Its first unpaid case is exactly clustered conditional co-heaviness. The present identity starts at that obstruction rather than repeating the rebalancing proof.

If natural D' has already failed because `alpha_i>=3/4` and some conditional partner has `a_j>=1/2`, then (3.1) gives the stronger constant `gamma>=3/8`. In the more general assumptions `alpha_i>=1/2`, `a_j>=1/2`, the same proof gives `gamma>=1/4` and the slightly weaker bound

`Z5 >= Z3 L^2/125`,

hence

`||p_Q||_infinity <15.576 Z3^(-1/10)L^(-1/5)`

whenever `sr(N)>=5/2`.

## 7. What remains unpaid

The full target is not closed. The new first missing implication is now sharply localized inside the clustered-volume branch:

`QFORM-CLUSTERED-PAIR-LOWTRANSVERSE-CLOSURE-v1`:

Given a useful order-three physical volume currency Z3 and a clustered pair with (3.1), handle the alternatives

- `L` small, where the physical pair area is forced large by `Delta^2 >= gamma Z3/L`, or
- `sr(N)<5/2`, where the transverse coefficient packet is near effective rank at most two,

by an already-proved pair/rank-two, ridge, one-sided-square, grouped-bank, or product-preserving Schur mechanism, without rotating the random variables and without dividing by a vanishing local scalar/minor.

This is strictly narrower than the preceding unstructured high-volume-coloop collar. It also identifies why a determinant-compound-only proof stalls: a true two-row coloop plus a transverse packet of effective rank at most two sits at or below the order-four/q=2 Fourier endpoint.

No exact-target counterexample to the global stronger criterion `integral |E exp(itQ)| dt <= C` was obtained. That global L1 criterion remains OPEN. The theorem above proves continuity only on its stated D5-paid branch.

## 8. Regression check

A direct random-matrix check (used only as algebraic regression, not proof) verified to floating precision both identities

`C3(i,j)=Delta^2 ||N||_F^2`

and

`C5(i,j)=Delta^2 e_3(N^T N)`

for random rectangular matrices. The proof itself is the Schur-complement/Cauchy--Binet argument in Section 2.

**Classification:** `ESSENTIAL_STEP_APPLIED`.
