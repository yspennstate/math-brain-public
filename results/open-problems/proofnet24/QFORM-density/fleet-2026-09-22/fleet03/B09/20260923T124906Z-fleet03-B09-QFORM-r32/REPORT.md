SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B09, 2026-09-23T12:49:06Z.
attacking: compile diffuse singleton third-volume mass in a rank-two hub/star into one genuine original-coordinate cross cut before reciprocal minor payment.

# fleet03/B09 r32 — aggregate singleton volume compiler for a rank-two physical hub/star

## Status

This run proves two supporting results.

1. `QFORM-FRACTIONAL-SUBVOLUME-BL-v1`: the q=1 fractional three-volume Fourier/BL theorem remains valid when its determinant probability measure is supported on ANY chosen nonempty family of actual 3x3 physical minors, provided that chosen family's normalized row marginals are at most 1/2.

2. `QFORM-RANK2-HUBSTAR-AGGREGATE-COMPILER-v1`: in a physical rank-two hub/star with arbitrary within-leaf quadratic curvature, an order-one aggregate of singleton third exterior volumes can be compiled into one literal original-coordinate cross cut. If the physical two-dimensional hub frame has maximum row leverage at most 1/2, this yields a continuous-density and linear-interval estimate

    ||p_Q||_infinity
      <= 3 e (512/27)^(1/6) (sum_k Gamma_k^2)^(-1/6)
      < 13.317 (sum_k Gamma_k^2)^(-1/6).

No moment, bounded-support, log-concavity, connected-support, Gaussian, diagonal-basis, or post-rotation independence assumption is used. Same-bank quadratic curvature is retained exactly inside the characteristic-function amplitudes. The theorem pays the aggregate third-volume quantity identified in r31 without choosing one universally good physical minor.

The unrestricted QFORM conjecture remains OPEN. This theorem still needs either a universal lower bound on the relevant aggregate resource in its structural branch or a routing argument for high physical hub leverage. Full-target continuity remains OPEN; continuity is proved in this theorem's stated branch.

Execution status: `WITHOUT_VERIFIED_BRAIN`.

## 1. Current controls, corrections, and sources actually used


Corrections retained include: no law-uniform pointwise quadratic-phase decay; no independence after spectral rotation; naive spectral-fiber suprema can lose dimension; an arbitrary-joint rank-three coarea estimate is false; a universally good single physical cross minor is false; and max-singleton third-volume stability is false. None of those corrections refutes the original QFORM conjecture.

The proof uses the following completed inputs at their exact scopes.

- fleet03/B09 r31, `QFORM-RANK2-NOAUGMENT-AGGREGATE-STABILITY-v1`, `yspennstate/math-open-problems@e8b97d9dcd8dd85cacc8fc73c2be4e86fde4b27a`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B09/20260923T114612Z-fleet03-B09-QFORM-r31/REPORT.md`. It identifies the singleton third-volume quantities Gamma_k and proves that their squared aggregate is the correct dimension-free defect from the exact rank-two no-augmentation model.

- fleet03/B09 r30, grouped rank-r cross smoothing, `yspennstate/math-open-problems@0257b7a08990f303da16797bcbad0d3e6a1e6538`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B09/20260923T104947Z-fleet03-B09-QFORM-r30/REPORT.md`. At rank three it gives

      ||p_Q||_infinity <= 3e Gamma^(-1/3)

  for an actual original-coordinate cross cut with third singular product Gamma, retaining arbitrary same-side curvature and giving a continuous density.

- newest volume-stability/Fourier theorem, `yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`, path `proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`. For an actual cross matrix M, if the normalized three-volume row marginals alpha_i are <=q/2, 1<=q<3/2, then

      ||p_Q||_infinity
       <= 3e / ((3-2q)sqrt(q)) * e_3(M^T M)^(-1/6).

  Its proof is by decoupling in original coordinates, determinant-weighted Brascamp--Lieb, sharp Hausdorff--Young, and Fourier inversion.

- designated partner fleet04/B09, `QFORM-PHYSICAL-CROSS-DETERMINANT-SMOOTHING-v1`, `yspennstate/math-open-problems@c0d3f34e557a374f41b2639994c43af4f950b682`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B09/20260923T101659Z-fleet04-B09-dense-self-cross-fourier-r1/REPORT.md`. For a literal physical 3x3 cross block K,

      ||p_Q||_infinity <= 3 |det K|^(-1/3),

  with arbitrary dense same-side self-couplings and continuous density. Section 7 applies this partner theorem to a target-valid matrix at an actual inequality.

## 2. Setup: physical rank-two hubs and singleton third volume

Let H and I be disjoint sets of ORIGINAL coordinates. Condition, if necessary, on every coordinate outside H union I; all generated affine terms may depend arbitrarily on the conditioned values. Suppose the physical cross block has rank two and write its thin factorization as

    A[H,I] = P C^T,          P^T P = I_2,

where P is |H| by 2 and C is |I| by 2. Let

    D=A[I,I]

be the completely arbitrary symmetric within-leaf block.

For k in I let

    M_k = A[H union {k}, I\{k}]
        = [ P C_{-k}^T ; D[k,I\{k}] ].

Define

    Gamma_k^2 = e_3(M_k^T M_k).

Because the top block has rank two, Gamma_k is exactly the product of the three nonzero singular values when rank M_k=3 and zero when rank M_k<=2. An orthogonal algebraic change of basis on the ROW INDEX SPACE H shows that

    Gamma_k^2
      = sum_{J subset I\{k}, |J|=3}
          det([ C_J^T ; D[k,J] ])^2.                    (2.1)

This is only a singular-value/Cauchy--Binet identity; the random variables are never rotated.

Put

    G_* = sum_{k in I} Gamma_k^2.                        (2.2)

The r31 stability theorem shows why G_* is the right aggregate resource: max_k Gamma_k can vanish with dimension while G_* stays order one.

## 3. Compiler lemma: aggregate singleton volume becomes one literal cross cut

For S subset I let T=I\S and form the genuine original-coordinate cross cut

    M_S=A[H union S,T]
       = [ P C_T^T ; D[S,T] ].                          (3.1)

For k in S define

    w_k(S)
      = sum_{J subset T, |J|=3}
          det([ C_J^T ; D[k,J] ])^2,

    W(S)=sum_{k in S} w_k(S).                           (3.2)

### Lemma 3.1 (Bernoulli aggregate compiler)

There exists S subset I such that

    W(S) >= (27/256) G_*.                               (3.3)

Moreover W(S) is a subvolume of the actual physical three-volume of M_S.

### Proof

Choose each k in I independently into S with probability p. For fixed k and a fixed three-set J subset I\{k}, the determinant term in (2.1) contributes to W(S) exactly when k is in S and all three indices of J are in T. That event has probability

    p(1-p)^3.

Therefore, by linearity of expectation and (2.1),

    E W(S)=p(1-p)^3 G_*.                                (3.4)

The scalar factor is maximized at p=1/4 and equals

    c := (1/4)(3/4)^3 = 27/256.                         (3.5)

Hence some S satisfies W(S)>=cG_*.

To see physical provenance, let p_a^T denote physical row a of P. For a<b in H, k in S, and J subset T with |J|=3,

 det M_S[{a,b,k},J]
   = det([p_a^T;p_b^T])
     det([C_J^T;D[k,J]]).                               (3.6)

Since P^T P=I_2, Cauchy--Binet gives

    sum_{a<b} det(P[{a,b},:])^2=1.                     (3.7)

Summing (3.6)^2 over a<b,k,J therefore gives exactly W(S). Thus W(S) is the mass of a literal family of physical 3x3 minors of M_S and in particular

    e_3(M_S^T M_S) >= W(S) >= cG_*.

QED.

This step has no leverage hypothesis. It is the aggregate-before-reciprocal-minor conversion that the max-singleton counterexample requires.

## 4. New analytic lemma: determinant-weighted BL may use a selected minor family

The newest volume theorem normalizes all squared 3x3 minors of M. Its q=1 proof in fact needs only a nonempty selected family.

### Theorem 4.1 (`QFORM-FRACTIONAL-SUBVOLUME-BL-v1`)

Let M be any actual original-coordinate cross matrix. Let Omega be any nonempty collection of pairs (R,C) of physical row triples and physical column triples for which det M[R,C] may be nonzero. Put

    Z_Omega = sum_{(R,C) in Omega} det M[R,C]^2 >0.      (4.1)

Normalize the weights

    pi_(R,C)=det M[R,C]^2/Z_Omega.

Let alpha_i be the probability that physical row i belongs to R and beta_j the probability that physical column j belongs to C. If

    max_i alpha_i <= 1/2,                               (4.2)

then for the full quadratic-plus-affine form, retaining arbitrary same-bank measurable phases and arbitrary conditioned outside variables,

    boxed:
    ||p_Q||_infinity <= 3e Z_Omega^(-1/6).              (4.3)

The characteristic function is L^1, so the density has a continuous representative vanishing at infinity. Consequently every interval L satisfies

    P(Q in L) <= 3e Z_Omega^(-1/6) |L|.                (4.4)

### Proof

Only the determinant lower bound in the existing q=1 proof needs checking. Give the row maps the exponents alpha_i and the coordinate maps the exponents 1-beta_j. In the Gaussian BL calculation, with positive row parameters d_i and active column parameters e_j,

 det(D_J+M^T D_I M)
   >= sum_{all 3x3 minors}
        det M[R,C]^2 prod_{i in R}d_i prod_{j notin C}e_j
   >= sum_{(R,C) in Omega}
        det M[R,C]^2 prod_{i in R}d_i prod_{j notin C}e_j.     (4.5)

Weighted AM--GM with the probabilities pi_(R,C) gives

    (4.5)
    >= Z_Omega prod_i d_i^(alpha_i)
                    prod_j e_j^(1-beta_j).              (4.6)

Endpoint columns with beta_j=1 are handled exactly as in the source proof: every positive-weight selected minor contains that column, so the corresponding zero Gaussian parameter does not appear in any selected determinant product.

All remaining analytic steps in the q=1 source proof depend only on

    sum_i alpha_i=sum_j beta_j=3,
    0<=alpha_i,beta_j<=1,
    alpha_i<=1/2,

not on completeness of the minor family. The sharp Hausdorff--Young factors and the two entropy products give the same characteristic-function envelope and Fourier inversion constant 3e. Replacing the source Z by Z_Omega proves (4.3)--(4.4). QED.

This is useful precisely because a structured subfamily can have admissible row marginals even when the full three-volume measure has concentrated marginals.

## 5. Main theorem: arbitrary leaf curvature paid by aggregate singleton volume

Assume from now on that the two-dimensional physical hub frame is diffuse:

    max_{h in H} (P P^T)_{hh} <= 1/2.                  (5.1)

No leverage condition is imposed on the leaf rows C.

### Theorem 5.1 (`QFORM-RANK2-HUBSTAR-AGGREGATE-COMPILER-v1`)

Under (5.1), if G_*>0, then for every admissible cap-one product law,

    boxed:
    ||p_Q||_infinity
      <= 3e (512/27)^(1/6) G_*^(-1/6)
      < 13.317 G_*^(-1/6).                              (5.2)

The density is continuous, and for every interval L,

    P(Q in L) < 13.317 G_*^(-1/6) |L|.                 (5.3)

All within-H curvature A[H,H], the full arbitrary D=A[I,I], all outside quadratic coefficients/couplings, and every conditioning-generated affine term are allowed.

### Proof

Set c=27/256.

#### Case A: one singleton carries a fixed fraction of G_*

Suppose for some k

    Gamma_k^2 >= (c/2)G_* = (27/512)G_*.               (5.4)

The actual source-coordinate cross cut M_k has rank three. Apply the completed fleet03/B09 r30 rank-three grouped-cross theorem to this literal cut:

    ||p_Q||_infinity
      <= 3e Gamma_k^(-1/3)
      = 3e (Gamma_k^2)^(-1/6)
      <= 3e(512/27)^(1/6)G_*^(-1/6).                   (5.5)

This branch has continuous density.

#### Case B: singleton volume is diffuse

Assume instead

    Gamma_k^2 < (c/2)G_* for every k.                  (5.6)

Choose S maximizing W(S). Lemma 3.1 gives

    W(S)>=cG_*.                                         (5.7)

For this S construct a selected family Omega_S of actual physical minors of M_S as follows: row triples are {a,b,k} with a<b in H and k in S, while column triples are J subset T, |J|=3. By (3.6)--(3.7),

    Z_(Omega_S)=W(S).                                   (5.8)

We compute its normalized physical row marginals.

For a moved leaf k in S, factorization (3.6) and (3.7) give

    alpha_k = w_k(S)/W(S)
             <= Gamma_k^2/W(S)
             < [(c/2)G_*]/[cG_*]
             =1/2.                                     (5.9)

For a physical hub row h, summing squared 2x2 minors of P containing h gives

    sum_{b != h} det(P[{h,b},:])^2
       = ||p_h||_2^2
       = (PP^T)_{hh}.                                  (5.10)

Since the remaining k,J mass factors independently and normalizes to W(S),

    alpha_h=(PP^T)_{hh}<=1/2                           (5.11)

by (5.1). Therefore every selected-family row marginal obeys the gate of Theorem 4.1. Apply that theorem:

    ||p_Q||_infinity
      <=3e W(S)^(-1/6)
      <=3e(256/27)^(1/6)G_*^(-1/6)
      =11.863926209... G_*^(-1/6).                     (5.12)

Again the density is continuous and the same constant multiplies interval length.

The Case A constant is larger:

    3e(512/27)^(1/6)=13.316806914....                  (5.13)

Combining (5.5) and (5.12) proves (5.2)--(5.3). QED.

### Why this avoids the forbidden losses

There is no square-root small-ball decoupling. The argument aggregates squared physical three-volumes first, chooses a disjoint original-coordinate bank partition, and pays the resulting determinant mass by an L^1 characteristic-function estimate. Arbitrary self-curvature remains inside the same-side complex amplitudes throughout. Reciprocal determinants appear only after aggregation.

## 6. Relationship with r31 aggregate stability

R31 proved, under its leaf no-coloop gate q_leaf=max c_k^T(C^TC)^(-1)c_k<1,

    (sum Gamma_k^2)^(1/2) / Delta
      <= dist_F(D, C Sym_2 C^T + diagonal)
      <= sqrt(2)/(sqrt(1-q_leaf))
           (sum Gamma_k^2)^(1/2)/Delta.                 (6.1)

The present theorem gives an analytic payment when that aggregate defect is not zero, provided the hub frame itself satisfies (5.1). Combining (6.1) and (5.2), a lower bound

    dist_F(D,C Sym_2 C^T+diagonal) >= eta

alone is not enough for a density estimate, because (6.1) supplies the wrong direction for a lower bound on G_* unless additional Delta/q_leaf control is known. This is recorded explicitly to avoid silently converting a small matrix residual into a small random quadratic error on unbounded inputs.

What the present theorem DOES accomplish is to remove the earlier need for one large Gamma_k: diffuse aggregate transverse curvature can now be paid directly through one literal selected cross cut.

## 7. Designated partner theorem applied to an actual target-valid inequality

Take four physical hub coordinates and four leaf coordinates. Let

    P = [[1/sqrt(2),0],
         [1/sqrt(2),0],
         [0,1/sqrt(2)],
         [0,1/sqrt(2)]],

    C = [[1,0],
         [0,1],
         [0,0],
         [0,0]],

and let D have only D_34=D_43=1 among the leaf entries. Define

    A = [[0_4, P C^T],
         [C P^T, D]].                                   (7.1)

The attached deterministic checker gives the exact nonzero spectrum

    {-1,-1,-1,1,1,1}.                                  (7.2)

Hence (7.1) satisfies the target spectral hypothesis. Its singleton volumes are

    (Gamma_1^2,Gamma_2^2,Gamma_3^2,Gamma_4^2)
      =(0,0,1,1),                                      (7.3)

so G_*=2. More concretely, use physical hub rows 1 and 3, moved leaf row 3, and leaf columns 1,2,4. The corresponding literal physical 3x3 cross block K has

    |det K|=1/2.                                        (7.4)

Now apply the designated fleet04/B09 completed theorem at the actual inequality:

    ||p_Q||_infinity
       <= 3 |det K|^(-1/3)
       = 3*2^(1/3)
       = 3.779763149684619... .                         (7.5)

This is a continuous-density, O(|L|) estimate for every admissible cap-one product input law, with all other same-side curvature allowed by the partner theorem. It is not merely a citation to the partner result.

The regression also illustrates the two complementary mechanisms: a concrete strong physical minor may give the sharper bound (7.5), whereas Theorem 5.1 remains useful when all individual minors are diffuse but their determinant mass is large in aggregate.

## 8. Deterministic checks

`CHECK.py` and `CHECK_OUTPUT.txt` in this run directory verify:

- the Bernoulli expectation identity E W=(27/256)G_* on 25 seeded random matrices;
- existence of a cut attaining at least the expectation;
- the physical factorization (3.6) after summing over physical hub pairs, to relative numerical error below 1.3e-15;
- the target-valid regression spectrum (7.2);
- the singleton weights (7.3);
- the physical partner determinant 1/2;
- the constants

      3e(256/27)^(1/6)=11.86392620905637,
      3e(512/27)^(1/6)=13.316806913608668,
      3*2^(1/3)=3.7797631496846193.

The finite checks support arithmetic and matrix identities only; the proof above supplies the analytic argument.

## 9. Remaining exact implication

The present branch is paid when the physical rank-two hub frame satisfies

    max_h (PP^T)_{hh} <=1/2

and the aggregate singleton volume G_* is quantitatively nonzero. The first exact B09 debt is now

`QFORM-RANK2-HUBSTAR-HIGH-HUBLEVERAGE-OR-SCALE-ROUTING-v1`:

> Starting from the bare three-large-eigenvalue hypothesis in the surviving rank-two hub/star geometry, either force a universal-scale aggregate G_* in a diffuse hub frame, or use a physical hub coordinate with leverage >1/2 to route the form into an already-paid physical-pivot / finite-core / rank-three cross endpoint, preserving arbitrary within-bank curvature and original-coordinate product provenance.

A high-leverage row must not simply be deleted, and a small operator/Frobenius residual cannot be treated as a uniformly small random quadratic perturbation because admissible product inputs may have unbounded support.

The full QFORM conjecture remains OPEN. Full-target continuous density remains OPEN. Theorem 5.1 proves continuity only in its stated branch.
