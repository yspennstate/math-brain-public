# An orientation-free rank-two fractional estimate and its rank-three Schur consequence

Programme: QFORM-DENSITY-3EIG-20260922. Interactive mathematical record: 20260922T161801Z-rank-two-fusion.

**Status:** complete analytic arguments for the stated supporting theorems are supplied below; independent end-to-end review is pending. The unrestricted three-large-eigenvalue bounded-density conjecture is not proved here. No literature-wide novelty claim is made.

## 1. Target and exact contribution

The full target is a universal finite C such that, for independent real X_i with probability densities bounded by one and every real symmetric A having at least three eigenvalues of absolute value at least one,

    P(X^T A X in [t,t+h]) <= C h

for every real t and h>0. No moment, centering, identical-law, smoothness, support, or sign assumptions are available.

The main result in this report is an orientation-free rank-two estimate, including arbitrary original-coordinate affine terms. Let U be n-by-2 with U^T U=I_2, let Lambda be an invertible real symmetric 2-by-2 matrix, and let b be any vector in R^n. Then

    sup_t E |(U^T X)^T Lambda(U^T X) + b^T X - t|^(-1/2)
        <= 128 |det Lambda|^(-1/4).                         (1.1)

There is NO leverage assumption on U and no requirement that b belong to range(U). Both signatures of Lambda are included. This is a fractional-potential estimate, not an L-infinity density estimate for a rank-two form: an indefinite rank-two form can still have an unbounded density.

A sharper constant 16 sqrt(30) applies when the affine term lies in range(U), including b=0. More importantly, the arbitrary-b formulation permits conditioning outside an original-coordinate block without adding an unjustified assumption on the induced linear term.

The rank-three consequence is the following. Suppose an original-coordinate principal block has rank exactly three and representation A_{I,I}=V M V^T, where V^T V=I_3 and M is invertible symmetric. If its row i has squared norm c_i and a=A_ii is nonzero, then the FULL ambient quadratic form has an essentially bounded density with

    ||p_Q||_infinity <= 128 [c_i |a| |det M|]^(-1/4).         (1.2)

All outside coefficients and cross couplings are arbitrary. For a full matrix A of rank exactly three with all three eigenvalues of magnitude at least one, (1.2) implies

    ||p_Q||_infinity <= 128 / sqrt(|A_ii|)                   (1.3)

for each nonzero diagonal entry A_ii. The estimate (1.2), rather than an unproved statement about independent spectral coordinates, is the precise extension proved here.

The new synthesis eliminates the previously unpaid small-Rayleigh strip INSIDE the rank-two Schur remainder. It does not eliminate the remaining small or zero OUTER scalar pivot, and does not provide an arbitrary-higher-rank Schur estimate. These limitations are detailed in Section 9.

## 2. Sources and conventions

Fourier transforms are defined by

    hat f(xi) = integral exp(-i xi x) f(x) dx.

The following classical inputs are used with their stated hypotheses:

1. Sharp Hausdorff--Young: for complex f, 1<=p<=2, and q=p/(p-1),

       ||hat f||_q <= (2pi)^(1/q) p^(1/(2p)) q^(-1/(2q)) ||f||_p.

   W. Beckner, *Inequalities in Fourier analysis*, Annals of Mathematics 102 (1975), 159--182, DOI 10.2307/1970980. Publisher record: https://annals.math.princeton.edu/1975/102-1/p11 .

2. Geometric rank-one Brascamp--Lieb: if v_j are unit vectors in R^r and c_j>0 satisfy sum c_j v_j v_j^T=I_r, then

       integral prod_j H_j(v_j dot x)^(c_j) dx
           <= prod_j (integral H_j)^(c_j)

   for nonnegative integrable H_j. The normalized formulation is Theorem 3.3 in G. Livshyts, G. Paouris and P. Pivovarov, *On sharp bounds for marginal densities of product measures*, https://arxiv.org/pdf/1507.07949 .

3. Rogozin--Ball scalar projection bound: if sum a_i^2=1, then sum a_i X_i has density at most sqrt(2). See Theorem 1.2 and its attribution to Rogozin and Ball in M. Rudelson and R. Vershynin, *Small Ball Probabilities for Linear Images of High-Dimensional Distributions*, https://arxiv.org/pdf/1402.4492 .

The source of the elementary logarithmic kernel used below is the completed account03/B16 report:

    yspennstate/math-open-problems@1defc84f1bfd79994a103a6d683c887d9dead1e7
    proofnet24/QFORM-density/fleet-2026-09-22/account03/B16/
    B16-20260922T135620Z-r11/REPORT.md
    blob d64c5e5cfc01bf3783cdcdeac2f03dd766bbda3d.

That source proves a physical two-variable fractional estimate by taking a supremum over translated first-coordinate densities. This report retains that supremum when the shift is correlated with a projected residual and, for arbitrary affine terms, supplies a rank-one affine small-ball lemma to replace a scalar-density argument. The kernel is credited to the source, not claimed as newly derived here.

The diffuse Fourier calculation extends the previously supplied separable-phase argument at

    yspennstate/math-open-problems@773b7fb6f0e6a8142066f0bac08d228dfc164fdb
    proofnet24/QFORM-density/interactive/
    20260922T120815Z-separable-perturbations/REPORT.md.

The rank-three residual obstruction being addressed is explicitly identified in account01/B10's handoff and supplement at

    yspennstate/math-open-problems@2152b0b8c7ddc76247b46d74dd1888d93920b0dd
    proofnet24/QFORM-density/fleet-2026-09-22/account01/B10/
    20260922T135338Z-account01-B10-QFORM-r13/SUPPLEMENT.md.

The classical sources and worker reports are dependencies; none is a certificate of a full solution or of independent review of this report.

## 3. A Fourier bound for diffuse projections with linear phases

### Lemma 3.1

Let V be n-by-r with V^T V=I_r and rows v_i^T satisfying c_i=|v_i|^2<=1/2. Let L be any invertible symmetric r-by-r matrix and b any vector in R^n. For

    F=(V^T X)^T L(V^T X)+b^T X,

the characteristic function obeys

    |phi_F(t)| <= min(1, e^(r/2) pi^(r/2)
                         |det L|^(-1/2) |t|^(-r/2)).        (3.1)

This lemma will be used for r=1 and r=2. Neither case asserts integrability of phi_F on the entire time axis.

### Proof

For fixed t, define h_{i,t}(x)=f_i(x) exp(it b_i x). Since 0<=f_i<=1 and integral f_i=1, all the norms ||h_{i,t}||_p are at most one for p>=1. Push the complex product measure with density prod h_{i,t} through x -> V^T x. It has a complex density g_t with ||g_t||_1<=1, by orthogonal disintegration and the triangle inequality. Its Fourier transform is

    hat g_t(xi)=prod_i hat h_{i,t}(v_i dot xi).

Zero rows contribute constant factors of modulus at most one and may be omitted from the upper bounds. For c_i>0 put w_i=v_i/sqrt(c_i). Then sum c_i w_i w_i^T=I_r and sum c_i=r. Brascamp--Lieb gives

    ||hat g_t||_1 <= prod_i c_i^(-c_i/2) ||hat h_{i,t}||_(1/c_i).

Since c_i<=1/2, the exponent 1/c_i lies in the Hausdorff--Young range [2,infinity). With p_i=1/(1-c_i), sharp Hausdorff--Young gives

    ||hat h_{i,t}||_(1/c_i)
      <= (2pi)^c_i (1-c_i)^(-(1-c_i)/2) c_i^(c_i/2).

The powers of c_i cancel. The elementary inequality -(1-c)log(1-c)<=c implies

    ||hat g_t||_1 <= (2pi)^r exp(r/2).                       (3.2)

Fourier inversion is justified because g_t and hat g_t are integrable. Insert exp(-epsilon|y|^2) in the physical-space integral for phi_F(t). Fubini is then justified by the Gaussian factor and (3.2). Diagonalizing L in this Gaussian calculation, each factor of the Fourier-transformed quadratic phase has modulus at most pi^(1/2)|t lambda_j|^(-1/2); its remaining exponential has modulus at most one. Consequently the regularized integral has modulus at most

    (2pi)^(-r) ||hat g_t||_1 pi^(r/2)|t|^(-r/2)|det L|^(-1/2).

As epsilon decreases to zero, dominated convergence against |g_t| removes the cutoff. Combine this with |phi_F(t)|<=1 to obtain (3.1). No transformed coordinates are declared independent. QED.

## 4. Rank-one curvature survives arbitrary affine terms

### Lemma 4.1

For |u|=1, lambda!=0, arbitrary b in R^n and d in R, put

    R=lambda(u dot X)^2+b dot X+d.

Uniformly in w in R and rho>0,

    P(|R-w|<rho) <= min(1,10 sqrt(rho/|lambda|)).             (4.1)

### Proof

If some u_i^2>=1/2, condition on every coordinate except X_i. The remaining polynomial in X_i has quadratic coefficient lambda u_i^2. The inverse image of an interval of length 2rho under a quadratic with coefficient a!=0 has total length at most 2sqrt(2rho/|a|): translate to the vertex, rescale, and use sqrt(v+2rho)-sqrt(v)<=sqrt(2rho). Since f_i<=1,

    P(|R-w|<rho | X_{-i}) <=4 sqrt(rho/|lambda|).

If every u_i^2<=1/2, Lemma 3.1 for r=1 gives

    |phi_R(t)| <= sqrt(e pi)|lambda t|^(-1/2), t!=0.

For any v>0, 1_{|z|<rho}<=exp(v)exp(-v z^2/rho^2). Gaussian Fourier inversion and the last envelope therefore give

    P(|R-w|<rho)
     <= exp(v) rho/(2sqrt(pi v))
          integral exp(-rho^2 t^2/(4v)) |phi_R(t)| dt
     <= exp(v) sqrt(e) Gamma(1/4)/(sqrt(2) v^(1/4))
          sqrt(rho/|lambda|).

Set v=1/4. The constant becomes e^(3/4)Gamma(1/4)<10. For example Gamma(1/4)<=4+e^(-1) follows by splitting its defining integral at one, and e^(3/4)(4+e^(-1))<10. This proves (4.1) in both cases. Constants and linear terms introduce only phases already retained in the argument. QED.

## 5. The translated quadratic kernel

Define the even function

    Psi(a)=1+log(1/|a|), 0<|a|<=1;
    Psi(a)=|a|^(-1/4), |a|>=1;
    Psi(0)=+infinity.

### Lemma 5.1 (source kernel)

For a!=0,

    sup_{0<=f<=1, integral f=1}
       integral f(x)|a-x^2|^(-1/2) dx <=8 Psi(a).             (5.1)

For a probability density bounded by K, the corresponding bound is

    integral f(x)|a-x^2|^(-1/2) dx <=8K Psi(K^2 a).           (5.2)

### Proof

Let m_a(s) be the Lebesgue measure of {x: |a-x^2|^(-1/2)>s}. Layer cake bounds the left side of (5.1) by integral_0^infinity min(1,m_a(s)) ds.

For a>0 and epsilon=s^(-2), if epsilon>=a then m_a(s)=2sqrt(a+epsilon)<=2sqrt(2)/s. If epsilon<a, then

    m_a(s)=2[sqrt(a+epsilon)-sqrt(a-epsilon)]
          <=4/(sqrt(a)s^2).

For a<0, m_a(s)<=2/s and m_a(s)=0 once s>=|a|^(-1/2).

When 0<a<=1, splitting at 1 and a^(-1/2) gives at most 5+sqrt(2)log(1/a), bounded by 8Psi(a). When -1<=a<0 it gives at most 1+log(1/|a|). For a>=1, split at 2a^(-1/4), which is at least a^(-1/2); the bound is at most 4a^(-1/4). For a<=-1, the kernel itself is at most |a|^(-1/2)<=|a|^(-1/4). These estimates prove (5.1). Rescaling x by K proves (5.2). QED.

### Lemma 5.2 (averaging the kernel from a small-ball estimate)

Suppose W is a real random variable and, for some L>0,

    P(|W|<rho)<=L sqrt(rho) for every rho>0.

Then

    E Psi(W)<=4sqrt(L).                                    (5.3)

### Proof

The hypothesis excludes an atom at zero. For 0<s<1, Psi(W)>s implies |W|<s^(-4), so its probability is at most Ls^(-2). For s>=1, the probability is at most L exp((1-s)/2). Since

    sup_{s>=1} s^2 exp((1-s)/2)=16e^(-3/2)<4,

both ranges are bounded by min(1,4L/s^2). Integrating this bound over s>0 gives 4sqrt(L). QED.

## 6. Main theorem: arbitrary orientation and arbitrary affine perturbations

### Theorem 6.1 — QFORM-RANK2-AFFINE-HALF-RIESZ-v1

Let U^T U=I_2 and Lambda be an invertible symmetric 2-by-2 matrix. Write D=|det Lambda|. For any independent cap-one input laws and ANY b in R^n,

    sup_w E |(U^T X)^T Lambda(U^T X)+b^T X-w|^(-1/2)
         <=128 D^(-1/4).                                  (6.1)

### Proof: diffuse case

If all row leverages are at most 1/2, Lemma 3.1 gives

    |phi_R(t)|<=min(1,K/|t|),  K=e pi D^(-1/2).

The following elementary Gaussian representation justifies the fractional-potential estimate without distributional Fourier manipulations:

    |z|^(-1/2)=Gamma(1/4)^(-1)
                   integral_0^infinity v^(-3/4)exp(-v z^2)dv.

Apply the scalar Gaussian Fourier formula to E exp(-v(R-w)^2), take the absolute value in its Fourier integral, and then use Tonelli. Integrating in v gives exactly

    E|R-w|^(-1/2)
      <=(2pi)^(-1/2) integral_R |t|^(-1/2)|phi_R(t)|dt.

The right side is finite. Splitting at |t|=K gives integral |t|^(-1/2)min(1,K/|t|)dt=8sqrt(K). Therefore

    E|R-w|^(-1/2)<=4sqrt(2e)D^(-1/4)<128D^(-1/4).            (6.2)

### Proof: a heavy physical coordinate

Otherwise choose an original coordinate i whose row leverage is h>1/2. An orthogonal change of basis in the TWO-DIMENSIONAL SPECTRAL SPACE makes its row (sqrt(h),0). This does not rotate the independent input coordinates. In the new spectral basis write

    Y_1=sqrt(h)X_i+T,   Y_2=Z,
    Lambda=[[beta,gamma],[gamma,delta]].

Both T and Z depend only on X_{-i}; X_i is independent of the pair (T,Z). T and Z need not be independent. The coefficient vector of Z, regarded as a linear form in X_{-i}, has Euclidean norm one. Thus Z has density at most sqrt(2) by the scalar projection theorem.

Put k=h^(-1/2) and d=b_i/sqrt(h). Let L_0=b_{-i}^T X_{-i}-dT. The full polynomial is exactly

    R=beta Y_1^2+2gamma Y_1 Z+delta Z^2+dY_1+L_0.            (6.3)

Conditional on all X_{-i}, the density of Y_1 is bounded by k, and its arbitrary translation is allowed in (5.2).

If beta!=0, completing the square in Y_1 yields

    R=beta(Y_1+(gamma/beta)Z+d/(2beta))^2+R_0,

    R_0=(det Lambda/beta)Z^2-(gamma d/beta)Z
                      -d^2/(4beta)+L_0.                   (6.4)

Crucially, R_0 is a rank-one quadratic form in the ORIGINAL remaining independent variables, plus a deterministic linear form and a constant. Its linear term may involve T and may lie outside the span of Z. Lemma 4.1 was proved precisely with those terms allowed.

By (5.2), for fixed X_{-i},

    E[|R-w|^(-1/2) | X_{-i}]
        <=8k |beta|^(-1/2) Psi(W),
    W=k^2(w-R_0)/beta.                                    (6.5)

The magnitude of the rank-one quadratic coefficient of W, on the normalized linear form Z, is

    lambda_0=k^2 D/beta^2.

Lemma 4.1 gives P(|W|<rho)<=10sqrt(rho/lambda_0). Applying Lemma 5.2 and then simplifying all powers,

    E|R-w|^(-1/2)
      <=32sqrt(10) k |beta|^(-1/2) lambda_0^(-1/4)
       =32sqrt(10) sqrt(k) D^(-1/4)
      <=32sqrt(10) 2^(1/4)D^(-1/4)
       <128D^(-1/4).                                     (6.6)

There is no reciprocal beta left. This calculation is uniform over every nonzero beta, however close to zero, with either sign of det Lambda.

If beta=0, then gamma!=0 and D=gamma^2. For fixed X_{-i}, (6.3) is affine in X_i with coefficient sqrt(h)(2gamma Z+d). For any cap-one probability density f,

    integral f(x)|x-a|^(-1/2)dx<=2sqrt(2),                  (6.7)

by layer cake, filling nearest a first. Hence

    E[|R-w|^(-1/2) | X_{-i}]
      <=2h^(-1/4)|gamma|^(-1/2)|Z+d/(2gamma)|^(-1/2).

For a probability density bounded by H, rescaling (6.7) gives 2sqrt(2H). Use H=sqrt(2) for Z. After averaging, the result is at most

    4*2^(3/4) h^(-1/4) D^(-1/4)<=8D^(-1/4).

The exceptional value 2gamma Z+d=0 has probability zero. The diffuse, nonzero-beta, and zero-beta cases exhaust all possibilities. This proves (6.1). QED.

### Corollary 6.2: a small-ball bound, but not bounded rank-two density

Markov's inequality applied to |R-w|^(-1/2) gives

    P(|R-w|<=rho)<=128D^(-1/4)sqrt(rho).

The half-potential estimate (6.1) is stronger information than this displayed consequence at its critical exponent. Neither statement implies a bounded density for an indefinite rank-two form. For example X_1^2-X_2^2 can have a logarithmic singularity.

## 7. Refined homogeneous constant and conditional-shear formulation

For completeness, the direct source-kernel route gives a sharper constant when there are no arbitrary extra affine directions.

Suppose Z has density at most H, and the conditional density of S given Z is at most K. For any invertible symmetric L=[[beta,gamma],[gamma,delta]],

    sup_w E| (S,Z)L(S,Z)^T-w |^(-1/2)
       <=16sqrt(15) sqrt(KH)|det L|^(-1/4).                 (7.1)

Deterministic affine terms in S and Z are also allowed, because a deterministic translation removes them and preserves the two caps. No independence of S and Z is claimed or required here.

To prove (7.1) for beta!=0, complete the square as before and use (5.2). The remaining deterministic kernel is Psi(a+epsilon delta_0 z^2), epsilon in {-1,1}, delta_0=K^2|det L|/beta^2. The uniform sublevel estimate

    |{z: |z^2+a|<rho}|<=4sqrt(rho)

implies

    ||Psi(a+epsilon delta_0 z^2)||_(L^{2,infinity}(dz))
         <=sqrt(15)delta_0^(-1/4).

Indeed for levels below one the squared weak norm is at most four, and for levels above one its bound is 64e^(-3/2)<15. The sign epsilon is harmless since Psi is even. For a cap-H probability density g and any nonnegative weak-L2 function v, layer cake gives integral gv<=2sqrt(H)||v||_(2,infinity). Substitution cancels beta exactly and proves (7.1). For beta=0 the affine calculation gives the smaller constant 4sqrt(2)sqrt(KH)|det L|^(-1/4).

In the heavy branch of Theorem 6.1 with b=0, the conditional density of Y_1 given Z remains at most h^(-1/2): mix over T using the genuine independence of X_i from (T,Z). The marginal density of Z is at most sqrt(2). Thus (7.1) gives

    16sqrt(15)(2/h)^(1/4)D^(-1/4)
       <=16sqrt(30)D^(-1/4).

Together with (6.2), this proves the refined constant 16sqrt(30) for b=0. An affine term in range(U) is removed by completing the square in spectral space and then translating the ORIGINAL independent inputs by a deterministic vector Uv. This preserves the refined constant for that scope.

The conditional-shear lemma is a half-potential assertion only. It must NOT be used to replace genuine independence in a three-variable bounded-density assertion; the archive contains a counterexample to that stronger inference.

## 8. Rank-three Schur consequence with arbitrary outside couplings

### Theorem 8.1 — QFORM-RANK3-ALL-RESIDUAL-ORIENTATIONS-v1

Let I be a set of original coordinates for which the principal block has rank exactly three:

    A_{I,I}=V M V^T,  V^T V=I_3,  det M!=0.

Choose i in I with a=A_ii!=0 and let c_i be the squared norm of row i of V. Then the full ambient form, with every outside block and cross coupling unrestricted, has an essentially bounded density satisfying

    ||p_Q||_infinity<=128[c_i|a||det M|]^(-1/4).              (8.1)

### Proof

Condition first on all original coordinates outside I. Their only effect is a deterministic affine term in X_I. Independence and the cap-one densities inside I are unchanged. We prove the same bound uniformly in every such affine term.

Order i first and write the conditional quadratic block as [[a,b^T],[b,C]]. If the induced linear coefficients are ell_i and ell_rest, completing the square in X_i gives

    Q=a(X_i+b^T X_rest/a+ell_i/(2a))^2+R(X_rest),

where R has quadratic matrix S=C-bb^T/a and an arbitrary original-coordinate affine term. Conditioning on X_rest, the shifted scalar has density at most one. The square change of variables therefore yields the density majorant

    p_Q(t)<=|a|^(-1/2) E|t-R|^(-1/2).                      (8.2)

It remains to represent S with an orthonormal rank-two frame and compute its determinant coefficient exactly.

Let v be the transpose of row i of V, so |v|^2=c_i. Let V_- be V with that row removed. Let T be a 3-by-2 orthonormal basis of v-perpendicular. Since V_-^T V_-=I_3-vv^T,

    W=V_- T  satisfies W^T W=I_2.

The symmetric matrix

    H=M-Mvv^T M/a

has kernel span(v), so H=TNT^T with N=T^T H T. Direct substitution gives

    S=W N W^T.                                            (8.3)

To calculate det N, use a spectral-space orthogonal basis with v=sqrt(c_i)e_1. Write M=[[alpha,q^T],[q,G]]. Then a=c_i alpha and

    N=G-qq^T/alpha,
    det N=det M/alpha=c_i det M/a.                         (8.4)

In particular N is invertible. Apply Theorem 6.1 to R using (8.3), including its arbitrary original-coordinate affine term. Equations (8.2)--(8.4) give

    p_Q(t)<=128 |a|^(-1/2)(c_i|det M|/|a|)^(-1/4),

which is (8.1). The conditional scalar change of variables supplies absolute continuity, and the displayed majorant bounds its density almost everywhere. The estimate is independent of the outside values, so averaging completes the proof. QED.

### Corollary 8.2: a uniformly nonzero physical diagonal entry

For a full matrix A of rank exactly three with all three nonzero eigenvalues of magnitude at least one, D=|det M|>=||M||. Also |a|<=c_i||M||. Therefore

    c_i|a|D >= |a|^2 D/||M|| >= |a|^2.

Theorem 8.1 gives ||p_Q||_infinity<=128/sqrt(|a|). Thus any fixed positive lower bound on one diagonal entry's magnitude gives a dimension-independent density bound, without any additional residual orientation, leverage, or Rayleigh-quotient assumption.

The theorem proves essential boundedness. It does not claim that its density majorant has a continuous representative.

## 9. What this closes, and what is still missing

The account01/B10 supplement cited in Section 2 left an indefinite rank-two residual branch with 0<|beta|<sqrt(Delta)/5, in addition to a separate outer-pivot problem. Equation (6.6) cancels beta uniformly, including arbitrary induced original-coordinate linear terms; the exact beta=0 case is separately proved. There is therefore no residual small-Rayleigh restriction in Theorem 8.1. This is an actual completed implication in the rank-three Schur route, not just a renamed obstruction.

The unrestricted conjecture still requires work in at least the following directions:

* All usable OUTER physical diagonal pivots can be tiny or zero. Equation (8.1) can deteriorate there. An indefinite matrix may have zero diagonal and rank three, so this is not an empty case. For example [[0,1,1],[1,0,1],[1,1,0]] has eigenvalues 2,-1,-1 and no nonzero scalar diagonal pivot. Existing finite-coordinate or paired-pivot arguments control that example, but not an exhaustive dimension-free aggregate reduction.
* An arbitrary admissible higher-rank matrix need not have an original principal block of rank exactly three with the required quantitative resources. Deleting spectral summands changes dependencies and is not legitimate independent convolution. Higher-rank Schur remainders are not covered by Theorem 6.1 merely because they have two large eigenvalues.
* A cross-rank-three-or-good-small-minor dichotomy is already refuted by the singleton-plus-two-banks family in the correction inbox. Any final structural reduction must retain grouped-coordinate possibilities and preserve product provenance.

No full-target universal constant, completion date, or literature-wide novelty conclusion follows from this report.

## 10. Verification, delivery and independent review

The analytic proof is Sections 3--8. The executable checks.py/check_results.json verify finite scalar and matrix identities and Fourier-envelope integrations. These checks are supporting diagnostics, NOT a universal proof or an independent review. An additional affine_checks.py verifies the Gaussian small-ball constant and the rank-one reduction of the affine residual.

Requested existing-worker reviews: account03/B16 checks the use of its translated kernel with conditional shifts, the rank-one affine lemma, and all signs; account01/B10 checks the exact Schur frame/determinant identity, arbitrary induced affine terms, and whether the previous residual strip is indeed eliminated in the stated scope. Passing reviews must be actual source-bound records, not generated on their behalf. Other workers should apply the precise result to their next missing implication rather than reproduce all reviews.

All work is within the authorized private mathematical programme. No new task, restart, schedule change, notification, public release, paid call, or native learned-memory-ingestion claim is involved.
