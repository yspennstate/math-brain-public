# QFORM B02 — disjoint-compound Fourier compiler and the exact coloop/rank-one-compression endpoint

Status: PROVED SUPPORTING RESULTS; FULL TARGET OPEN.

Target throughout: independent real original coordinates with densities at most one, arbitrary real symmetric A with at least three eigenvalues of modulus at least one, no moments/support/log-concavity assumptions and no independence after spectral rotation. Continuity is asserted only on branches where an L1 characteristic-function bound is proved.

Source control read for this run: yspennstate/math-research-brain@b6aebb50868cb7b2edcd402e5d3d83a5b03ccd2a, owner revision 2026-09-22.15. Newest required source package used here: yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837, `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/{RESULTS.md,FOURIER_ROUTE_REPORT.md,COUNTEREXAMPLE_SEARCH.md}`. The reviewed sharp-Hausdorff--Young refinement used below is the preceding account02/B02 result `QFORM-SHARP-HY-VOLUME-JENSEN-v1`, math-open-problems@49c80441f24d6c697350119fac09426077b7e313. The designated partner result actually used below is account03/B02 `QFORM-EXACT-RANK3-CROSSBLOCK-FOURIER-v1`, canonical math-open-problems@484c89f85cda352b2c4318364a6206ebc4154950.

## 1. First unpaid implication attacked

The previous B02 run left the high-volume-coloop / effective-rank-at-most-four collar after D', D5 and the sharp-HY improvement. This report makes that collar precise in a coordinate-invariant exterior-energy language and closes one exact coloop endpoint. It does not claim an exhaustive reduction from the bare three-eigenvalue hypothesis.

For an n by n matrix A and k>=1 define the *disjoint k-compound energy*

    D_k^dis(A) := sum det(A[S,T])^2,

where the sum is over ordered k-subsets S,T of [n] with S intersection T empty. For a physical cut I,J (disjoint original-coordinate banks), write

    Z_k(I,J) := e_k(A[I,J]^T A[I,J])
              = sum_{S subset I,T subset J, |S|=|T|=k} det(A[S,T])^2.

These are deterministic quantities of the actual matrix A; no spectral rotation is performed on the inputs.

## 2. Random-cut exterior compiler

**Lemma 2.1 (random-cut identity).** For every k,

    E_cut Z_k(I,J) = 2^(-2k) D_k^dis(A),

where each coordinate is independently sent to I or J with probability 1/2. Consequently some physical cut obeys

    Z_k(I,J) >= 2^(-2k) D_k^dis(A).                                  (2.1)

**Proof.** Fix an ordered disjoint pair (S,T). Its squared minor appears in Z_k(I,J) exactly when every member of S is colored I and every member of T is colored J, an event of probability 2^(-2k). Sum and use linearity of expectation. QED.

This simple identity is useful because D_k^dis measures exactly the exterior mass that can be made product-preserving across an original-coordinate cut; overlapping minors are deliberately not counted.

### 2.2 D5 becomes a global disjoint-fifth-volume certificate

The sharp-HY D5 estimate proved in the previous B02 run says that every physical cut satisfies

    ||p_Q||_infinity <= (5e/sqrt(2)) Z_5(I,J)^(-1/10)                (2.2)

whenever Z_5(I,J)>0, with no volume-marginal gate. Combining (2.1) with k=5 gives the new global certificate

    boxed(||p_Q||_infinity <= 5 sqrt(2) e [D_5^dis(A)]^(-1/10)).    (2.3)

Numerically 5 sqrt(2)e = 19.2211551408. This branch has phi_Q in L1, hence a continuous density vanishing at infinity. In particular, any unresolved sequence for a universal L1 Fourier bound must have D_5^dis(A) tending to zero after the target normalization, or else (2.3) closes it uniformly.

### 2.3 Exact-rank-three disjoint compiler: actual use of account03/B02

Assume D_4^dis(A)=0 but D_3^dis(A)>0. Apply Lemma 2.1 with k=3 and choose a cut with

    Z_3(I,J) >= 2^(-6) D_3^dis(A)>0.                                (2.4)

Because D_4^dis(A)=0, every physical cross block has rank at most three: a rank-four cross block would contain a nonzero disjoint 4 by 4 minor. The block in (2.4) therefore has exact rank three. The completed designated-partner theorem account03/B02 gives, with Gamma the product of the three nonzero singular values,

    ||p_Q||_infinity <= 6 Gamma^(-1/3)
                       = 6 Z_3(I,J)^(-1/6).

Using (2.4),

    boxed(||p_Q||_infinity <= 12 [D_3^dis(A)]^(-1/6)).              (2.5)

This is a genuine partner-to-new-inequality application. Arbitrary same-bank quadratic terms, outside couplings and affine terms are retained because the partner theorem has exactly that scope. The branch is continuous by the partner's L1 Fourier proof.

Thus the exterior collar is already closed at its exact-rank-three endpoint whenever the disjoint third-compound energy is quantitatively nonzero.

## 3. The rank-four collar and why only a physical coloop can defeat D4

The sharp-HY volume theorem works for every integer k>2q. Applied at k=4, let h be the largest row marginal of squared 4 by 4 volume sampling in a physical cross block M. If h<=1/2 choose q=1; if 1/2<h<1 choose q=2h. Then

    ||p_Q||_infinity <= 2e Z_4(M)^(-1/8),                           (3.1)

for h<=1/2, and

    ||p_Q||_infinity <= e/[sqrt(2h)(1-h)] Z_4(M)^(-1/8),            (3.2)

for 1/2<h<1. The same statement may be applied to M^T, so one is free to constrain the better side.

For an exact-rank-four M, the 4-volume row marginals are exactly the diagonal leverages of the projection onto range(M), because every nonzero 4-volume uses all four singular directions. Therefore the only exact endpoint at which the k=4 integrated estimate itself ceases to be integrable is a physical row of leverage one (or, after transposition, a physical column of leverage one). This is the precise `coloop` endpoint; near one the constant in (3.2) records the quantitative collar rather than hiding it.

Combining a high-energy cut satisfying Z_4>=2^(-8)D_4^dis(A) with (3.1) gives, when h<=1/2,

    ||p_Q||_infinity <= 4e [D_4^dis(A)]^(-1/8) < 10.874 [D_4^dis(A)]^(-1/8),

and for 1/2<h<1 gives

    ||p_Q||_infinity <= 2e/[sqrt(2h)(1-h)] [D_4^dis(A)]^(-1/8).     (3.3)

No claim is made that Lemma 2.1 alone forces the high-energy cut to have h bounded away from one.

## 4. A sharper D' obstruction: opposite-side star concentration

For a fixed physical cut with Z_3>0, let (S,T) be sampled with probability proportional to det(M[S,T])^2. Let

    alpha_i=P(i in S),   beta_j=P(j in T).

The sharp-HY D' compiler closes the cut whenever either orientation has maximum marginal below 3/4: if h=max_i alpha_i<3/4, use M; if max_j beta_j<3/4, use M^T. Therefore failure of D' in both orientations forces coordinates i in I and j in J with alpha_i,beta_j>=3/4. For such a pair,

    P(i in S and j in T) >= alpha_i+beta_j-1 >= 1/2,

so

    boxed(sum_{S contains i,T contains j} det(M[S,T])^2 >= Z_3/2). (4.1)

This is an exact deterministic narrowing of the high-volume collar: at least half of all third exterior mass is simultaneously pinned to one physical row and one physical column. It is stronger than merely saying that one side has a heavy row. It does not, by itself, imply that the single entry M_ij is large; cross-cycle cancellation can make that inference false, consistently with the live correction inbox.

Equation (4.1) is the next object a product-preserving hub/pair argument must spend. It is also why the remaining collar is genuinely different from the already-paid diffuse D' branch.

## 5. Exact spectral-coloop endpoint with rank-one compression

The newest source's mixed-Fresnel theorem pays one important endpoint of (4.1) without any reciprocal coordinate minor.

**Theorem 5.1 (physical spectral coloop + rank-one compression).** Let

    A = U Lambda U^T,
    U^T U = I_3,
    min_k |lambda_k| >= 1,

so A has exact rank three. Suppose an original coordinate i has spectral leverage one: if u is the i-th row of U, then ||u||=1. Choose an orthonormal basis [u,V] of R^3 and write

    Lambda' = [ d   b^T ]
              [ b    M  ],                                      (5.1)

where M is 2 by 2. Assume rank(M)=1. Let R=U_{-i}V, so R^T R=I_2. If

    max_{ell != i} ||r_ell||^2 <= 1/2,                           (5.2)

then for every independent cap-one product input and arbitrary affine term,

    |phi_Q(t)| <= ((4pi)^(3/2)/2) |det Lambda|^(-1/2) |t|^(-3/2),

and hence

    boxed(||p_Q||_infinity <= 12/2^(2/3) |det Lambda|^(-1/3)
                               <= 7.559526300).                   (5.3)

The output density is continuous and vanishes at infinity.

**Proof.** Since ||u||=1 and U has orthonormal columns,

    U_{-i}^T U_{-i}=I_3-u u^T,

so after identifying u^perp with R^2, R^T R=I_2. Write the rank-one compression as M=mu s s^T with |s|=1, and choose n perpendicular to s. Write b=gamma s+beta n. Invertibility of Lambda' forces beta!=0. Moreover direct expansion of (5.1) gives

    det Lambda' = -mu beta^2.                                   (5.4)

On the residual original coordinates L=[n]\{i},

    A_LL = mu (Rs)(Rs)^T,
    A_Li = Rb.

Apply Theorem MF of the required e5f source package with one physical hub H={i} and one residual Fresnel square r=1. Its leaf feature at coordinate ell is

    w_ell=((Rb)_ell,(Rs)_ell).

The Gram matrix of these features is

    Gamma = [ ||b||^2   gamma ]
            [ gamma        1  ],

because R^T R=I_2, and det Gamma=beta^2. Since the two columns Rb and Rs are obtained from R by an invertible 2 by 2 change of basis, their normalized row leverage is invariant:

    w_ell^T Gamma^(-1) w_ell = ||r_ell||^2.

Thus (5.2) is exactly the mixed-Fresnel leverage gate. The source theorem yields

    |phi_Q(t)| <= (4pi)^(3/2) 2^(-1) |t|^(-3/2)
                  |mu|^(-1/2) |beta|^(-1).

Use (5.4) to identify the last two factors as |det Lambda|^(-1/2). Finally

    integral_R min(1,K|t|^(-3/2)) dt = 6 K^(2/3),

and Fourier inversion contributes 1/(2pi), giving exactly 12*2^(-2/3)|det Lambda|^(-1/3). QED.

This theorem is useful specifically because a leverage-one spectral row makes every rank-three Pluecker basis contain that physical coordinate, so disjoint third-compound energy can vanish even though the target has three large eigenvalues. The mixed-hub proof pays that exact failure mode when the two-dimensional residual frame is diffuse and its spectral compression has rank one.

## 6. What is still unpaid

After the results above, an unresolved integrated-Fourier sequence must evade all of the following simultaneously:

1. quantitatively nontrivial disjoint fifth-compound energy, by (2.3);
2. the exact-rank-three disjoint endpoint D_4^dis=0 with quantitative D_3^dis, by (2.5);
3. a rank-four physical cut with 4-volume leverage bounded away from one, by (3.1)-(3.3);
4. either orientation of D' with third-volume marginal below 3/4; if both fail, (4.1) forces at least half of Z_3 into one opposite-side row/column star pair;
5. the exact spectral-coloop / rank-one-compression / diffuse-residual endpoint, by Theorem 5.1.

The first unpaid implication is therefore narrower than at the start of the run: spend the joint row-column star mass (4.1) in the near-coloop rank-four collar, and in the exact spectral-coloop case handle the rank-two compression or a localized residual row, without the false two-sided Gabor-line L2 restriction and without a random-variable shear that destroys product provenance. The N3 no-pivot reduction remains open.

No target-valid counterexample to the global unweighted integral |phi_Q(t)| dt criterion was obtained here. The stronger Fourier criterion therefore remains open, not refuted.
