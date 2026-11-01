SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B02, 2026-09-23T02:20:40Z.
attacking: integrated Fourier estimate — convert global third compound mass into a physical random-cut cross-volume, then isolate the heavy-row/heavy-column collar without selecting a tiny local minor.

# fleet01/B02 r20 — random-cut compound Fourier theorem and nested heavy-volume fallback

## Status

`ESSENTIAL_STEP_APPLIED / SUPPORTING_ANALYTIC_THEOREM / FULL_QFORM_OPEN / GLOBAL_L1_OPEN_NOT_REFUTED / WITHOUT_VERIFIED_BRAIN`.

This report proves an exact global-to-physical compound identity and applies the completed fleet02/B02 three-volume Fourier theorem to obtain a genuine unweighted `L^1_t` characteristic-function estimate on a new coordinate-free spectral branch. If the volume-sampling gate fails in both orientations, the same calculation forces two dimension-free aggregate two-volume packets after deleting heavy physical coordinates, and in a diffuse nested subbranch gives a quantitative `L_t^(5/3)` estimate. It does **not** close the overlap-dominated third-compound regime or the nested double-heavy endpoint, so the unrestricted conjecture remains open.

Continuity: the direct `L^1_t` branch below gives a continuous density vanishing at infinity. The nested `L^(5/3)` fallback alone does not imply a bounded or continuous density.

No Gaussian, log-concavity, moment, compact-support, connected-support, identical-law, or post-rotation independence assumption is used. All cuts, compounds, singular values, and Schur identities below are deterministic algebra on the coefficient matrix; the random variables remain in their original independent coordinates.

## 1. Sources and live corrections actually used

Fresh `math-research-brain/main` was read at run start and again before publication. The owner control remains revision `2026-09-22.15`, QFORM is the sole research target, and there is no later pause/stop. The current state still marks the full conjecture and full continuity conclusion open.

The designated completed partner result actually applied is:

- repository `yspennstate/math-open-problems`;
- commit `ffcfabe542e6005c8d62d231eb5566f5d569498a`;
- path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B02/20260923T010832Z-fleet02-B02-QFORM-auto11/REPORT.md`.

The partner re-audits the sharp fractional three-volume theorem: if `M=A[I,J]`, `Z=e_3(M^T M)>0`, `1<=q<3/2`, and every natural row third-volume marginal obeys `alpha_i<=q/2`, then the full quadratic-plus-affine form has a continuous density and

`||p_Q||_infinity <= [3e/((3-2q)sqrt(q))] Z^(-1/6).`          (1.1)

The proof supplies the stronger characteristic-function envelope itself, so

`int_R |phi_Q(t)| dt
 <= [6 pi e/((3-2q)sqrt(q))] Z^(-1/6).`                       (1.2)

Arbitrary within-bank quadratic terms are retained. Interchanging `I,J` applies the same theorem to `M^T`, so only the chosen row side is subject to the marginal gate.

The preceding B02 result used below is my r19 report:

- commit `2c64efc8863bc0d519090613ba29fb113c3b7ddc`;
- path `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B02/20260923T014852Z-fleet01-B02-qform-r19/REPORT.md`.

For a physical cross block `N` with `Z_2=e_2(N^T N)>0`, if its natural two-volume row marginals satisfy `max alpha_i<=q/2` and `1<=q<r<2`, then

`int |phi(t)|^r dt
 <= [2 pi r/(r-q)] [B_beta prod_i H_q(alpha_i)]^(1/2) Z_2^(-1/4)`

and, coarsely,

`int |phi(t)|^r dt
 <= [2 pi r/(r-q)] e q^(-1/2) Z_2^(-1/4).`                    (1.3)

This estimate is uniform under conditioning on outside original coordinates, because only affine/same-bank terms change.

Corrections retained include: law-uniform pointwise quadratic van-der-Corput decay is false; post-rotation coordinates are not independent; one fixed good minor is not forced; a bounded projection density does not by itself control an indefinite quadratic trace; arbitrary-joint coarea and positive conditional-height moment gates are false; coefficient-small terms may not be discarded under unrestricted fragmented supports; and an absolute spectral Wiener majorant can diverge even when the target density is bounded. Nothing below invokes those invalid interfaces.

## 2. Global third compound and the disjoint part

Let `s_1>=s_2>=...>=0` be the singular values of the real symmetric matrix `A`. Define the total third compound mass

`C_3(A) := sum_{|S|=|T|=3} det(A[S,T])^2.`                     (2.1)

Cauchy--Binet gives the exact identity

`C_3(A)=e_3(A^T A)=e_3(A^2)=e_3(s_1^2,s_2^2,...).`             (2.2)

Under the target spectral hypothesis,

`C_3(A) >= s_1^2 s_2^2 s_3^2 >= 1.`                            (2.3)

Define the **disjoint third-compound mass**

`D_3(A) := sum_{|S|=|T|=3, S cap T=empty} det(A[S,T])^2.`       (2.4)

This is the portion of the global third compound that can be placed into a genuine original-coordinate cross block without reusing a coordinate on both sides. The ratio

`eta(A):=D_3(A)/C_3(A) in [0,1]`                               (2.5)

is purely deterministic. It can be zero (for example for a diagonal matrix), so it is not itself a full-target lower bound.

## 3. Exact random-cut identity

### Theorem 3.1 — `QFORM-RANDOM-CUT-COMPOUND-IDENTITY-v1`

Choose a random bipartition `[n]=I disjoint_union J` by independently putting each coordinate in `I` or `J` with probability `1/2`, and set

`M=A[I,J]`, `Z_3(I,J)=e_3(M^T M)`.

Then

`boxed( E_cut Z_3(I,J) = D_3(A)/64. )`                         (3.1)

Consequently there exists a deterministic physical cut satisfying

`boxed( Z_3(I,J) >= D_3(A)/64. )`                              (3.2)

#### Proof

For each fixed cut, Cauchy--Binet gives

`Z_3(I,J)
 = sum_{S subset I, T subset J, |S|=|T|=3} det(A[S,T])^2.`      (3.3)

A fixed ordered pair of triples `(S,T)` can occur in (3.3) only when `S cap T=empty`. If disjoint, the six distinct coordinates must receive six prescribed independent cut signs, so

`P(S subset I, T subset J)=2^(-6)=1/64.`                       (3.4)

Taking expectation termwise proves (3.1), and the maximum of nonnegative values is at least their mean. QED.

This is an aggregate-before-inversion identity. It does not assert a fixed good `3x3` minor and therefore does not conflict with the fleet's fixed-minor counterexamples.

## 4. Apply the fleet02/B02 sharp three-volume Fourier theorem

Assume for the moment that

`D_3(A) >= eta C_3(A)`                                         (4.1)

for some `eta>0`. Choose a cut from Theorem 3.1. Then

`Z_3 >= eta C_3(A)/64
     >= eta s_1^2 s_2^2 s_3^2/64.`                            (4.2)

Let `alpha_i` be the natural row third-volume marginals of `M`, and `beta_j` the natural column marginals. Put

`h_R=max_i alpha_i`, `h_C=max_j beta_j`.                       (4.3)

Because the partner theorem can be applied to `M` or to `M^T`, if

`min(h_R,h_C) <= 2/3`                                          (4.4)

we orient the cut so the lighter side is the row side and take `q=4/3` in (1.1)-(1.2). This gives

`int |phi_Q(t)| dt <= 9 pi sqrt(3) e Z_3^(-1/6)`               (4.5)

and therefore, using (4.2),

`boxed(
 int |phi_Q(t)| dt
 <= 18 pi sqrt(3) e eta^(-1/6)
 < 266.243 eta^(-1/6).
)`                                                              (4.6)

Fourier inversion yields the continuous-density bound

`boxed(
 ||p_Q||_infinity
 <= 9 sqrt(3) e eta^(-1/6)
 < 42.374 eta^(-1/6).
)`                                                              (4.7)

The factor `C_3(A)^(-1/6)` was bounded by one using only the target's three-large-singular-value hypothesis. More sharply, (4.7) carries the factor `(s_1s_2s_3)^(-1/3)`.

If the oriented row marginal is at most `1/2`, we may instead take `q=1`, obtaining the cleaner certificates

`int |phi_Q| <= 12 pi e eta^(-1/6)` and
`||p_Q||_infinity <= 6e eta^(-1/6) <16.310 eta^(-1/6).`         (4.8)

### What has been achieved

A **dimension-free positive fraction of global disjoint third compound, together with one diffuse orientation of the induced physical volume law, is now a true target-compatible unweighted Fourier certificate.** No coordinate minor is individually inverted. This directly applies the completed fleet02/B02 theorem to a matrix quantity controlled from the full spectrum via (2.2)-(3.2).

## 5. If the three-volume gate fails: a universal two-volume packet appears

The same selected cut gives a useful fallback without any reciprocal local minor.

For a row `r_i` of `M`, let `h_i=alpha_i`, and let `N_i=M[-i,:]`. The exact row-star mass is

`h_i Z_3 = sum_{S: |S|=3, i in S} || wedge_{k in S} r_k ||^2.` (5.1)

For each pair of other rows,

`||r_i wedge r_j wedge r_k||^2
 <= ||r_i||^2 ||r_j wedge r_k||^2.`                             (5.2)

Summing gives

`boxed(
 h_i Z_3 <= ||r_i||^2 e_2(N_i^T N_i).
)`                                                              (5.3)

This is the `k=3` version of the same exterior row-deletion mechanism used by the partner at order four.

If the direct row gate fails, choose `i` with `h_i>2/3`. Since

`||r_i|| <= ||M||_op <= ||A||_op=s_1`,                         (5.4)

(4.2)-(5.3) imply

`e_2(N_i^T N_i)
 > (2/3) [eta s_1^2 s_2^2 s_3^2/64]/s_1^2
 = eta s_2^2 s_3^2/96
 >= eta/96.`                                                    (5.5)

Thus failure of the three-volume row gate does **not** merely say "one row is heavy": it forces a row-deleted physical two-volume packet of dimension-free size.

Applying the same argument to `M^T`, if the column gate also fails there is a column `j` such that

`e_2(M[:,-j] M[:,-j]^T) >= eta/96.`                            (5.6)

Therefore the only failure of the direct `L^1` branch under (4.1) is a **double-heavy collar with two separate aggregate two-volume currencies**.

## 6. Apply the previous B02 two-volume Fourier compiler to the fallback

This section supplies an actual Fourier inequality, rather than leaving (5.5) as a matrix observation.

Condition on the heavy original coordinate `X_i`. The remaining quadratic form keeps the physical cross block

`N_i=A[I\{i},J]`;                                               (6.1)

conditioning only changes affine and same-bank terms. Hence r19 applies uniformly in the conditioned value.

Suppose the natural two-volume row marginals of `N_i` satisfy

`max gamma_k <= 2/3.`                                          (6.2)

Take `q=4/3`, `r=5/3` in (1.3). Since

`r/(r-q)=5`, `q^(-1/2)=sqrt(3)/2`,                             (6.3)

for every conditioned value `x` we obtain

`int |phi_{Q|X_i=x}(t)|^(5/3) dt
 <= 5 pi e sqrt(3) e_2(N_i^T N_i)^(-1/4).`                    (6.4)

By Minkowski,

`||phi_Q||_(5/3)
 <= E ||phi_{Q|X_i}||_(5/3)`,                                  (6.5)

so (5.5) yields the unconditional nested Fourier estimate

`boxed(
 int |phi_Q(t)|^(5/3) dt
 <= 5 pi e sqrt(3) (96/eta)^(1/4).
)`                                                              (6.6)

If the two-volume marginals are at most `1/2`, taking `q=1,r=3/2` instead gives

`boxed(
 int |phi_Q(t)|^(3/2) dt
 <= 6 pi e (96/eta)^(1/4).
)`                                                              (6.7)

These are genuine global characteristic-function estimates for the original `Q`, obtained after conditioning only on an original coordinate and averaging back. They do not by themselves imply `L^1_t`; they are the exact intermediate currency available in the heavy-three-volume branch.

The same argument is available from the heavy column after conditioning on `X_j` and transposing the cross block.

## 7. Double-heavy row/column: exact joint-star Schur identity

There is one further exact structural identity worth recording because it makes the remaining collar sharply algebraic.

Assume `h_R>2/3` and `h_C>2/3`, and choose a heavy row `i` and heavy column `j`. Under the natural squared-three-minor law `(S,T)`, the union bound gives

`P(i in S and j in T) >= h_R+h_C-1 > 1/3.`                    (7.1)

Let `a=M_ij`. If `a!=0`, define the rectangular one-pivot Schur complement

`B=M[-i,-j]-M[-i,j] a^(-1) M[i,-j].`                          (7.2)

For every two-row set `U` avoiding `i` and two-column set `V` avoiding `j`, the determinant identity for a `1x1` pivot gives, up to an irrelevant sign,

`det M[{i} union U,{j} union V] = a det B[U,V].`              (7.3)

After squaring and summing,

`boxed(
 P(i in S,j in T) Z_3 = a^2 e_2(B^T B).
)`                                                              (7.4)

Using (4.2), (7.1), and `|a|<=s_1` therefore gives

`boxed(
 e_2(B^T B)
 > eta C_3(A)/(192 s_1^2)
 >= eta s_2^2 s_3^2/192
 >= eta/192.
)`                                                              (7.5)

This does **not** by itself prove a density bound, because completing a rectangular bilinear pivot must still preserve the original-product provenance while same-bank curvature is present. Equation (7.5) is recorded as a deterministic resource, not as an illicit post-rotation or conditional-independence step. If `a=0`, (7.3) is unavailable and the joint-star mass must be paid by a different zero-pivot/mixed-hub mechanism.

## 8. Compact end-to-end conditional implication

The new argument can be summarized without hidden assumptions.

Assume `D_3(A)>=eta C_3(A)` for a specified `eta>0`. Then there exists an original-coordinate cut with `Z_3>=eta C_3/64`. On that cut:

1. if either row or column natural third-volume marginal maximum is `<=2/3`, the completed fleet02/B02 theorem proves

   `int|phi_Q| <=18 pi sqrt(3)e eta^(-1/6)`

   and hence a continuous density bounded by `9sqrt(3)e eta^(-1/6)`;

2. otherwise there are a heavy row and heavy column; deleting either one leaves an aggregate physical `e_2` packet at least `eta/96`;

3. if one of those row/column-deleted `e_2` packets has a corresponding natural two-volume marginal maximum `<=2/3`, the full characteristic function obeys the quantitative `L^(5/3)` estimate (6.6);

4. if both nested two-volume laws are again concentrated, the problem has been reduced to a nested hub/coloop collar. In the nonzero heavy-row/heavy-column cross-pivot subcase, the exact rectangular Schur packet (7.5) is additionally available.

Thus the spectral-to-physical loss has been reduced to two explicit mechanisms rather than an unspecified "find a good minor":

- **overlap-dominated global compound mass** `eta=D_3/C_3 ->0`; or
- **nested heavy-volume/coloop structure** after a disjoint third-volume packet is found.

Both are precisely grouped-coordinate/localized phenomena, complementary to the diffuse volume-Fourier branch.

## 9. What is still open

The target-wide statement

`int_R |E exp(it X^T A X)| dt <= C`                             (9.1)

remains `OPEN_NOT_REFUTED`. This run gives (9.1) with a quantitative constant when a fixed positive fraction `eta` of the global third compound is disjoint and one induced orientation is volume-diffuse; it does not prove a universal positive lower bound on `eta`, which is impossible (diagonal matrices have `eta=0`), nor does it yet replace the overlap-dominated mass by the already-known grouped-square mechanisms in one exhaustive theorem.

No target-valid counterexample to (9.1) was found. The known phase-aligned supports refute only pointwise decay, not this integrated criterion.

The full bounded-density conjecture therefore remains open. Essential boundedness is proved only on the stated direct branch; the nested `L^r` statements are supporting Fourier estimates. Continuity is proved only where unweighted `L^1_t` is obtained.

## 10. First unpaid implication

`QFORM-COMPOUND-OVERLAP-OR-NESTED-COLOOP-CLOSURE-v1`.

Use the exact partition

`C_3(A)=sum_{r=0}^3 C_3^{(r)}(A)`,

where `C_3^{(r)}` sums squared `3x3` minors with `|S cap T|=r`. The present run pays a dimension-free fraction of the `r=0` mass unless it generates a nested heavy-volume collar. The next step is to route a dimension-free fraction of the `r=1,2,3` overlap mass into existing original-coordinate square/pair/grouped-bank smoothers, while routing the nested `e_2` coloop collar into the existing mixed-hub or independent-linear-square mechanisms. Crucially, this must be done **before** any reciprocal local-minor payment and without deleting small coefficients.

## 11. Sanity checks

The algebraic identities were independently checked on random symmetric finite matrices by brute-force enumeration of all `3x3` minors and all cuts:

- `sum_{S,T} det(A[S,T])^2 = e_3(A^2)` to floating precision;
- `average_cut e_3(A[I,J]^T A[I,J]) = D_3(A)/64` to floating precision;
- the row-star deletion inequality (5.3) on every row of sampled cuts.

These finite checks are not proofs; Sections 2-7 give the proofs.

## 12. Scope checklist

- arbitrary independent cap-one input laws: yes;
- arbitrary dimension: yes in the stated structural branches;
- arbitrary signs / indefinite A: yes;
- arbitrary additional small or large eigenvalues: yes;
- no moment/support/log-concavity hypotheses: yes;
- no independence after rotation: yes;
- no fixed-good-minor assumption: yes;
- designated fleet02/B02 completed theorem applied to an actual inequality: yes, equations (4.5)-(4.7);
- global unweighted `L^1_t` theorem: not proved;
- target-valid counterexample to global `L^1_t`: not found;
- full bounded-density conjecture: open;
- full continuity conclusion: open;
- native brain ingestion: not verified; repository retrieval only.
