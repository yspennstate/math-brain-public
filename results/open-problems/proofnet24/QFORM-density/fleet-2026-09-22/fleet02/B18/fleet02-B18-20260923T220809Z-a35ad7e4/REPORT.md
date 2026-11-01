SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B18, 2026-09-23T22:08:09Z.
attacking: the exact-null-hub near-parallel private-bank collar; test whether the aligned endpoint and the partner transverse-cross estimate can be interpolated by a uniform conditional private-bank density bound, and if not identify the product-preserving coupled mechanism still required.

# fleet02/B18 — near-parallel private-bank conditional blowup

**Programme:** QFORM-DENSITY-3EIG-20260922  
**Status:** NEW SOURCE-VALID OBSTRUCTION TO A PROOF INTERFACE / TARGET-VALID STRESS FAMILY / PINNED THEOREM APPLIED / FULL QFORM OPEN  
**Continuity:** no new full-target continuity claim.  
**Execution:** WITHOUT_VERIFIED_BRAIN.

## 1. First unpaid implication

The latest designated partner fleet03/B18 theorem, source

`math-open-problems@f621e672e07c62d1565b9a0fddeb57626a97cb10`,

proves the following exact-null-hub branch. For

    Q = 2 (X0 + ell·X_L)(g·X_L) + d (beta·X_L)^2,

with original independent cap-one sources, beta·g=0, ||beta||=1, gamma=||g||>0, and a literal original-coordinate split L=J disjoint_union K with g_K=0, put

    b = ||beta_J||,
    rho = ||beta_K||,
    eta = ||P_{beta_K^perp} ell_K||.

If b rho eta>0, then

    ||p_Q||_infinity
    <= 3*2^(5/6) [ |d| gamma^2 b rho eta ]^(-1/3),                  (1.1)

and the density is continuous C_0. The preceding aligned endpoint theorem fleet03/B18 r34, source

`math-open-problems@12cb94062390a52deaf9a0c74b5d81aa41e5a128`,

proves, when ell_K is parallel to beta_K,

    ||p_Q||_infinity
    <= 2^(13/4) / [ rho sqrt(|d| gamma) ].                           (1.2)

Thus eta=0 is paid and every fixed eta>0 is paid, but (1.1) degenerates as eta->0. The tempting next step is to condition on the complementary original sources and seek an eta-uniform L-infinity bound for the private K-bank quadratic-linear pushforward. The theorem below shows that this step is false even for the cleanest possible genuine product source.

## 2. Exact product-source obstruction

### Theorem `QFORM-PRIVATE-TRANSVERSE-CONDITIONAL-BLOWUP-v1`

Let U1,U2 be independent Uniform[-1/2,1/2] random variables and define the orthogonal linear forms

    B = (U1+U2)/sqrt(2),
    V = (U1-U2)/sqrt(2).                                             (2.1)

For rho>0 and s!=0 put

    Z_{rho,s} = rho^2 B^2 + s V.                                    (2.2)

Then Z_{rho,s} has a density and

    p_{Z_{rho,s}}(0)
    = rho^(-2) [ sqrt(1 + 4 rho^2/(sqrt(2)|s|)) - 1 ].              (2.3)

Consequently, for every fixed rho>0,

    p_{Z_{rho,s}}(0)
    ~ 2^(3/4) rho^(-1) |s|^(-1/2)                                  (2.4)

as s->0. In particular no constant C(rho) can satisfy

    sup_{0<|s|<=1} ||p_{rho^2 B^2+sV}||_infinity <= C(rho).          (2.5)

This failure occurs although (B,V) is an orthogonal two-dimensional projection of a genuine product source whose original one-dimensional densities are exactly one on sets of measure one.

### Proof

The map

    (u1,u2) -> (b,v)=((u1+u2)/sqrt(2),(u1-u2)/sqrt(2))

is orthogonal, hence has Jacobian modulus one. The unit square [-1/2,1/2]^2 maps to the diamond

    D = { (b,v): |b|+|v| <= a },   a=1/sqrt(2),                     (2.6)

and therefore the joint density of (B,V) is exactly 1_D.

For s!=0, coarea in the v coordinate gives, for every regular z,

    p_{Z_{rho,s}}(z)
    = |s|^(-1) int_R
        1_D( b, (z-rho^2 b^2)/s ) db.                               (2.7)

At z=0 the condition in the integrand is

    |b| + rho^2 b^2/|s| <= a.                                      (2.8)

Writing x=|b|, the positive endpoint r is the positive root of

    x + rho^2 x^2/|s| = a,

namely

    r = |s|/(2 rho^2)
        [ sqrt(1+4a rho^2/|s|) - 1 ].                               (2.9)

Hence

    p_{Z_{rho,s}}(0)
    = 2r/|s|
    = rho^(-2)[sqrt(1+4a rho^2/|s|)-1],                             (2.10)

which is (2.3), since a=1/sqrt(2). Expanding the square root proves (2.4). QED.

The important point is stronger than merely saying that a generic bounded joint density is insufficient: the counterexample is itself an exact orthogonal image of two independent cap-one original coordinates. Thus a source-valid linear-projection theorem, even at an exact cap of one for this example, cannot by itself turn the private nonlinear pushforward into an eta-uniform conditional density cap.

## 3. Robustness under a moving square centre

The blowup is not an isolated artefact of the single centre zero. Let

    Z_{rho,s,q} = (rho B+q)^2 + sV.                                 (3.1)

At the target value q^2,

    p_{Z_{rho,s,q}}(q^2)
    = |s|^(-1) int
      1_D( b, -(rho^2b^2+2rho q b)/s ) db.                          (3.2)

If |q|<=sqrt(|s|)/4 and |s|<=2rho^2, then for every

    |b| <= sqrt(|s|)/(4rho),                                        (3.3)

we have

    |b| <= a/2,

and

    |rho^2b^2+2rho q b|/|s|
    <= 1/16+1/8 = 3/16 < a/2.                                      (3.4)

Thus the interval (3.3) lies in the diamond fibre and

    p_{Z_{rho,s,q}}(q^2)
    >= 1/(2rho sqrt(|s|)).                                          (3.5)

So the conditional cap blows up on a whole moving-centre window |q|=O(sqrt(|s|)), not only at q=0. This matters when the square centre is supplied by another original product bank: taking a supremum over the conditioned complementary variables necessarily pays this divergence.

## 4. A target-valid diffuse family in the partner geometry

The preceding two-variable calculation can be embedded into an exact owner-target family while simultaneously making every physical diagonal and every 2x2 principal determinant small.

Fix an even integer m. On m original J-coordinates choose the orthonormal coefficient vectors

    g_j = 1/sqrt(m),
    c_j = eps_j/sqrt(m),                                             (4.1)

where eps_j in {+1,-1} and sum_j eps_j=0. Put

    G = g·X_J,
    C = c·X_J.                                                       (4.2)

On two further original K-coordinates U1,U2 use B,V from (2.1). Let

    rho = 1/8,
    b0 = sqrt(1-rho^2) = sqrt(63)/8,
    beta = b0 c + rho B,                                             (4.3)

where c and B denote their coefficient vectors on disjoint source banks. For eta real define

    Q_{m,eta}
      = 2 X0 G + 2 eta G V + (b0 C + rho B)^2.                      (4.4)

All original variables X0, X_J, U1,U2 may be taken independent Uniform[-1/2,1/2], hence this is a literal cap-one product-source family.

The five deterministic coefficient directions

    e0, g, V, c, B

are mutually orthonormal. In this aggregate orthonormal basis the quadratic matrix splits as

    [[0,1,eta],
     [1,0,0],
     [eta,0,0]]

on span(g,e0,V), up to a permutation of basis coordinates, together with the rank-one projector onto b0 c+rho B. Therefore

    spec_nonzero(A_{m,eta})
      = { -sqrt(1+eta^2), 1, sqrt(1+eta^2) }.                       (4.5)

Thus every Q_{m,eta} is in the exact owner target: it has three eigenvalues of modulus at least one. No independence of G,C,B,V is asserted; only the original coordinates are independent.

This family is also physically diffuse. Its original-coordinate diagonals are

    A_00=0,
    A_jj=b0^2/m=63/(64m)             (j in J),
    A_U1,U1=A_U2,U2=rho^2/2=1/128.                                (4.6)

The 2x2 principal determinants are exactly zero for J-J, K-K and hub-K pairs; for a hub-J pair,

    det A[{0,j}] = -1/m.                                            (4.7)

For a J-K pair, since v_Uk=+/-1/sqrt(2),

    A_jk = (b0 rho eps_j +/- eta)/sqrt(2m),                         (4.8)

and hence

    det A[{j,k}]
      = -[eta^2 +/- 2 b0 rho eps_j eta]/(2m).                       (4.9)

For |eta|<=1,

    |det A[{j,k}]|
    <= [1+2b0rho]/(2m)
    < 1/m.                                                          (4.10)

Consequently, for m>=128 and |eta|<=1,

    max_i |A_ii| <= 1/128,
    max_{i<j} |det A[{i,j}]| <= 1/128.                              (4.11)

So the construction sits in the same small-diagonal/small-pair-minor geometry that motivates the null-hub compiler; it is not an artefact of a single conspicuously good physical pair.

## 5. The conditional obstruction occurs inside this exact target family

Condition on the original J variables. This fixes G and C while preserving independence of the private original K bank (U1,U2). The K-dependent part of (4.4) is

    (b0 C+rho B)^2 + 2 eta G V.                                    (5.1)

At any conditioned configuration with C=0 and G=g_*!=0, (5.1) is exactly Z_{rho,s} with

    s=2 eta g_*.                                                     (5.2)

Such configurations are genuinely in the interior of the source cube. For example, when m>=4, the choice x_J=g gives G=1 and C=0 and has every coordinate 1/sqrt(m) in (-1/2,1/2). Hence the uniform conditional-bank estimate would have to cover

    p(0 | G=1,C=0)
      = rho^(-2)
        [sqrt(1+4rho^2/(sqrt(2)*2|eta|))-1].                         (5.3)

With rho=1/8 this becomes

    p(0 | G=1,C=0)
      = 64 [ sqrt(1 + sqrt(2)/(64|eta|)) - 1 ]                     (5.4)

and therefore

    p(0 | G=1,C=0)
      ~ 2^(13/4)|eta|^(-1/2)
      = 9.5136569200... |eta|^(-1/2).                               (5.5)

By Section 3 the same order of divergence persists for a positive moving-centre window |b0 C|=O(sqrt(|eta G|)). Thus the obstacle is stable under the random centre supplied by the J bank.

## 6. Exact comparison with the designated partner endpoints

The family (4.4) is in the latest fleet03/B18 private-bank geometry with

    d=1,
    gamma=||g||=1,
    b=||beta_J||=b0=sqrt(63)/8,
    rho=1/8,
    eta_partner=|eta|.                                               (6.1)

For eta!=0, fleet03/B18 `QFORM-NULLHUB-PRIVATE-TRANSVERSE-CROSS-v1` gives

    ||p_{Q_{m,eta}}||_infinity
    <= 3*2^(5/6)(b0 rho |eta|)^(-1/3)
    = 10.7188818574... |eta|^(-1/3).                                (6.2)

At eta=0, the earlier aligned private-bank theorem gives

    ||p_{Q_{m,0}}||_infinity
    <= 2^(13/4)/rho
    = 76.1092553602... .                                             (6.3)

The two certified branches cross numerically at |eta| about

    0.00279341868557.                                                (6.4)

The new calculation explains why the most obvious bridge cannot remove this gap: after conditioning away the J/hub structure, the private K pushforward has a real peak of order |eta|^(-1/2), worse than the partner certificate's |eta|^(-1/3). Thus any uniform interpolation must exploit averaging/cancellation involving the complementary source before it is conditioned away.

This is an obstruction to a proof architecture, not to QFORM itself.

## 7. Required pinned result applied to a real target inequality

The pinned source `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `COUNTEREXAMPLE_SEARCH.md`, proves the ruled one-sheet theorem: for a rank-three form with signature (2+,1-) and all three nonzero eigenvalue moduli at least one,

    p_Q(t) <= pi sqrt(2)                                             (7.1)

for almost every t on the one-sheet sign side t>=0 (after orienting the sign accordingly).

Our physical spectrum (4.5) has exactly that signature for every eta. Applying the pinned theorem literally gives the actual target inequality

    boxed: p_{Q_{m,eta}}(t) <= pi sqrt(2)
           = 4.442882938158366...
           for a.e. t>=0, all m and eta.                             (7.2)

Therefore the conditional private-bank spike (5.5) does not translate into a one-sheet output spike. The complementary-source coupling genuinely regularizes after the conditioning that the false interpolation would have thrown away. This is direct evidence for the form the missing argument must take.

The pinned counterexample search reports no valid full-QFORM counterexample; that negative search outcome is not used as novelty evidence.

## 8. Primary-source literature boundary

The only general projection theorem relevant here is Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel J. Math. 216 (2016), 877--889, arXiv:1507.07949, Theorem 1.1.

Its literal hypotheses are: a product probability density

    f(x)=prod_i f_i(x_i),

with each f_i bounded, nonnegative and of L1 norm one. For a k-dimensional orthogonal subspace E it proves

    ||pi_E f||_infinity
    <= min{ (n/(n-k))^((n-k)/2), 2^(k/2) }
       prod_i ||f_i||_infinity^(gamma_i),                            (8.1)

for weights gamma_i in [0,1] summing to k. Hence in the owner cap-one class every k-dimensional orthogonal marginal has density at most 2^(k/2). No moment, compact-support, log-concavity, iid, smoothness, centering or symmetry assumption appears.

For the J directions g,c in (4.1), this yields the legitimate joint bound

    ||p_(G,C)||_infinity <= 2.                                      (8.2)

It does not assert that G and C are independent. More importantly, (2.3) shows that even replacing (8.2) by the stronger exact private-bank statement `p_(B,V)=1_D<=1` does not provide an eta-uniform bound after the nonlinear map `(B,V)->rho^2B^2+sV`. Thus there is no source-matching theorem available here that licenses the false conditional shortcut.

## 9. What is now ruled out and what remains

The new theorem rules out the following prospective implication:

> condition on all complementary original variables; use only a uniform density cap for the private two-dimensional linear projection; deduce an eta-uniform L-infinity bound for the private quadratic-linear pushforward; then average back.

It fails on an exact cap-one product source, quantitatively as |eta|^(-1/2).

The sharpened first unpaid implication is therefore `QFORM-NEARPARALLEL-HUB-COUPLED-INTERPOLATION-v1`:

retain the hub/product-source averaging jointly with

    2 G X0 + (b C+rho B)^2 + 2 eta G V                               (9.1)

through the eta->0 transition, and prove a uniform whole-line estimate without deleting the small nonzero eta term, without taking a supremum over the private-bank conditional density, and without declaring the projected variables independent. A plausible currency is a mixed fractional-potential or Fourier estimate in which the |eta|^(-1/2) conditional spike occupies only an O(sqrt(|eta G|)) centre window and is integrated against the genuine joint product projection of (G,C) before absolute values destroy that gain.

The full unrestricted QFORM conjecture and full-target continuity remain OPEN.

## 10. Numerical/algebraic checks

The aggregate matrix eigenvalues were checked numerically at eta=1, 0.1, 0.01 and 0.001 and agree with

    {-sqrt(1+eta^2),0,0,1,sqrt(1+eta^2)}

up to floating-point roundoff. The closed form (2.3) was checked against the explicit quadratic endpoint r in (2.9); for s=1,0.1,0.01,0.001 the two formulas agree to machine precision, and sqrt(|s|) p_{Z_{1,s}}(0) approaches 2^(3/4) as predicted. These checks support, but are not substitutes for, the exact algebraic proofs above.
