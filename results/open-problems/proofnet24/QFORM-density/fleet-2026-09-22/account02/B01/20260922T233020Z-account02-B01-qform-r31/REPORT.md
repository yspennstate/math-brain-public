SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B01, 2026-09-22T23:30:20Z.
attacking: the natural-volume heavy-row barrier by entropy-reweighting the 3-minor distribution past the h=3/4 threshold, then comparing the resulting averaged-frequency bound with the account03/B01 endpoint-pair smoother on the same target family.

# QFORM B01 r31: entropy-rebalanced 3-volume and a heavy-row stress family

## Status

**ESSENTIAL_STEP_APPLIED / NEW AVERAGED-FREQUENCY COROLLARY / FULL QFORM OPEN.**

This note preserves the phase-aligned-density refutation of every law-uniform pointwise quadratic-phase decay estimate. Nothing below reintroduces such a pointwise bound. The mechanism is the source-valid *integrated* characteristic-function theorem obtained after Weyl differencing, Brascamp--Lieb, and volume sampling.

The full target remains: for every dimension, independent real coordinates with densities bounded by one, and every real symmetric matrix with at least three eigenvalues of modulus at least one, prove a universal essential density bound for X^T A X or give a valid counterexample. No moments, support regularity, log-concavity, Gaussianity, spectral-coordinate independence, or small-tail assumption is used here.

## Source premises actually used

1. `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md` on the current math-open-problems source contains the proved volume-sampling Fourier theorem. For a physical cross block M=A_{IJ}, put

   Z = e_3(M^T M) = sum_{|S|=|T|=3} det(M_{ST})^2.

   The report proves the natural-volume theorem, its arbitrary-weight/KL version, and the Jensen extension D'. In particular, for **any** probability weight w on nonzero 3x3 minors whose I-side row marginals are at most 1/2, the same proof gives

   D(Q) := ||p_Q||_infinity <= 6 sqrt(e) K(w)^(-1/6),

   where

   K(w) = exp( E_w log det(M_{ST})^2 + H(w) )
        = Z exp(-KL(w || w_0)),

   and w_0(S,T)=det(M_{ST})^2/Z is the natural volume distribution. This retains arbitrary self-blocks, all outside couplings after conditioning, and arbitrary affine terms. The same report proves D' for the natural weight when max row marginal h<3/4.

2. The completed assigned-partner result `account03/B01` r20 proves: if an invertible indefinite physical endpoint pair P has D=|det P| and kappa=sigma_min(P), and its exact Schur remainder has any nonzero original-coordinate cross block C with F=||C||_F, then

   D(Q) < 11.021 D^(-2/5) kappa^(-1/10) F^(-1/10).

The pointwise Fresnel counterexample remains a required correction throughout.

## 1. Entropy-rebalanced heavy-row theorem

Let M=A_{IJ} have Z=e_3(M^T M)>0. Let w_0 be its natural 3-volume distribution. Fix a row i and put

  alpha = P_{w_0}(i in S),    0<alpha<1.

For k != i define the two conditional row occupancies

  a_k = P_{w_0}(k in S | i in S),
  b_k = P_{w_0}(k in S | i notin S).

### Theorem 1 (one-heavy-row entropy rebalance)

Assume alpha>1/2 and

  a_k + b_k <= 1       for every k != i.                 (1.1)

Then the full quadratic form satisfies

  **D(Q) <= 6 sqrt(e) Z^(-1/6) [4 alpha(1-alpha)]^(-1/12).**    (1.2)

This is an averaged-frequency statement; it is uniform over all admissible input densities and over the self-blocks A_{II}, A_{JJ}, the conditioned outside variables, and induced affine terms.

### Proof

Let E={i in S}. Define a new weight on the same nonzero minors by

  w = (1/2) w_0(. | E) + (1/2) w_0(. | E^c).             (1.3)

Its marginal at row i is exactly 1/2. For k!=i its row marginal is

  P_w(k in S) = (a_k+b_k)/2 <= 1/2                       (1.4)

by (1.1). Therefore w is admissible in the arbitrary-weight/KL version of the proved Fourier theorem.

Because w differs from w_0 only by changing the Bernoulli mass of E from alpha to 1/2,

  KL(w||w_0)
   = (1/2) log[(1/2)/alpha] + (1/2) log[(1/2)/(1-alpha)]
   = -(1/2) log[4 alpha(1-alpha)].                        (1.5)

Thus

  K(w)=Z exp(-KL)=Z sqrt(4 alpha(1-alpha)).               (1.6)

Substitution into D(Q)<=6 sqrt(e) K(w)^(-1/6) gives (1.2). QED.

The theorem crosses the h=3/4 barrier of the *natural* D' weight whenever (1.1) holds. Its price is only the twelfth root of the Bernoulli imbalance. In particular it does not confuse failure of a chosen volume weight with failure of the Fourier route itself.

## 2. A structural identity carried by a heavy natural-volume row

The same natural measure gives a useful exact/one-sided pair of identities. Write r for row i of M and N for M with row i deleted. Then

  **e_3(N^T N) = (1-alpha) Z,**                           (2.1)

and

  **e_2(N^T N) >= alpha Z / ||r||_2^2.**                 (2.2)

Indeed, (2.1) is Cauchy--Binet: the left side is precisely the sum of squared 3-minors that avoid i. For (2.2), the total weight of 3-minors containing i is alpha Z, and

  alpha Z
   = sum_{j<k} || r wedge n_j wedge n_k ||_2^2
   <= ||r||_2^2 sum_{j<k} || n_j wedge n_k ||_2^2
   = ||r||_2^2 e_2(N^T N).                               (2.3)

So a volume-heavy row cannot erase all lower-order transverse currency in the remaining rows. This does not by itself close QFORM, because converting that two-volume into a third product-preserving smoother without paying a tiny physical determinant remains structural work.

## 3. Exact target stress family beyond the natural D' threshold

For 0<alpha<1 define a 6x3 matrix U_alpha by rows

  u_1 = (sqrt(alpha),0,0),

and, for k=0,...,4,

  u_{k+2} = ( sqrt((1-alpha)/5),
              sqrt(2/5) cos(2 pi k/5),
              sqrt(2/5) sin(2 pi k/5) ).                 (3.1)

The pentagon identities sum cos=sum sin=sum sin cos=0 and sum cos^2=sum sin^2=5/2 give

  U_alpha^T U_alpha = I_3.                               (3.2)

Now form the symmetric 9x9 bipartite matrix

  A_alpha = [ 0       U_alpha
              U_alpha^T   0 ].                           (3.3)

Its nonzero eigenvalues are exactly +1,+1,+1,-1,-1,-1, so this is an exact full-target family for *arbitrary* independent cap-one input laws.

Take the physical cross block M=U_alpha. Then Z=e_3(U^T U)=1. Since M has exact rank three, the natural volume row marginals are the row leverages. Thus

  alpha_1=alpha,
  alpha_2=...=alpha_6=(3-alpha)/5.                       (3.4)

For alpha>=3/4 the new report's natural-weight D' hypothesis fails because h>=3/4.

Nevertheless, conditional on row 1 being selected, cyclic symmetry among rows 2,...,6 and the fixed cardinality |S|=3 imply

  a_k=2/5  (k>=2),                                       (3.5)

while conditional on row 1 not being selected,

  b_k=3/5  (k>=2).                                       (3.6)

Hence a_k+b_k=1 exactly, and Theorem 1 applies for every alpha>1/2:

  D(Q_alpha) <= 6 sqrt(e) [4 alpha(1-alpha)]^(-1/12).    (3.7)

At alpha=0.9 this is

  D(Q_0.9) <= 10.771428004.                              (3.8)

This explicitly applies the newest averaged-frequency/KL tool in a regime where the displayed natural D' threshold is violated.

## 4. Assigned partner applied on the *same* family

Use the physical pair consisting of left coordinate 1 and right coordinate 1. Its principal block is

  P = [0          sqrt(alpha)
       sqrt(alpha) 0],                                   (4.1)

so

  D=|det P|=alpha,     kappa=sqrt(alpha).                (4.2)

Row 1 of U_alpha has no coupling to right coordinates 2,3. Therefore exact Schur completion of this pair makes no correction to the remaining left-(right 2,3) cross block. That residual 5x2 block is U_alpha[2:6,{2,3}] and

  F^2 = ||C||_F^2 = 5*(2/5)=2.                          (4.3)

The completed account03/B01 r20 theorem therefore gives

  D(Q_alpha)
   < 11.021 alpha^(-2/5) (sqrt(alpha))^(-1/10) (sqrt(2))^(-1/10)
   = 11.021 alpha^(-9/20) 2^(-1/20).                    (4.4)

At alpha=0.9 this is <11.162472. More importantly, it stays uniformly bounded as alpha approaches one, exactly where (3.7) pays its entropy endpoint loss.

Combining the two source routes gives a uniform certificate for the entire family. For alpha<=1/2, the natural D' weight has h=(3-alpha)/5<=3/5, hence

  D(Q_alpha) <= 10 sqrt(5e/6) < 15.051.                 (4.5)

For alpha>=1/2, (4.4) is decreasing in alpha and is at most its alpha=1/2 value <14.543. Consequently

  **sup_{0<alpha<1} D(Q_alpha) < 15.051**                (4.6)

for every choice of independent cap-one input laws. This family contains arbitrarily severe natural 3-volume concentration on one row, so (4.6) is a useful stress-test closure rather than a numerical observation.

## 5. Preserved counterexample to pointwise quadratic-phase decay

For every s>0 and sufficiently small delta>0, the phase-aligned set

  {x : dist(s x^2, 2 pi Z) <= delta}

has infinite Lebesgue measure. A finite union of its components of total measure one gives an admissible density f<=1 with

  Re int exp(i s x^2) f(x) dx >= cos(delta).

Thus no law-uniform pointwise decay C |s|^{-gamma}, gamma>0, can hold. Theorems 1--4 do not contradict this: all decay is obtained only after coupling coordinates, Weyl differencing and integrating frequency via the Brascamp--Lieb volume currency.

## 6. First unpaid implication

The new first unpaid structural implication is

**QFORM-CLUSTERED-HEAVY-VOLUME-REBALANCE-v1.**

Given an arbitrary full-target matrix whose useful 3-volume measure is concentrated on several *conditionally co-heavy* physical rows so that the one-row condition a_k+b_k<=1 fails for every heavy row, prove a dimension-free routing to at least one of:

1. a multirow entropy-reweighted 3-minor distribution with all I-side marginals <=1/2 and bounded KL cost;
2. an indefinite endpoint pair plus any nonzero Schur cross Frobenius mass, to which account03/B01 r20 applies;
3. the source D_5 / ridge / mixed-hub certificates; or
4. an exactly cross-free remainder exposing a third curvature direction product-preservingly.

Identity (2.2) says a single heavy row already leaves quantitative 2-volume in its complement; the remaining problem is to spend that currency jointly with the third direction before reciprocal local-minor losses occur.

Full QFORM is therefore **OPEN**. This report is not a full-proof candidate and does not have the two end-to-end reviews required for one.
