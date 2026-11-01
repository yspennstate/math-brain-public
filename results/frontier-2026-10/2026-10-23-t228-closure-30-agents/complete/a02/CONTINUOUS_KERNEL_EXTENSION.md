# A02: A quantitative raw-input extension of T336 to continuous kernels

Date: 2026-10-23. Status: author proof candidate; not independently audited or formally verified. The construction extends the existing finite-rank result to all continuous PSD kernels, including an explicit RBF specialization. It does not prove the literal arbitrary-bounded-kernel statement, does not claim new approximation theory, and does not contain a training guarantee. A05 is developing the separate ERM bridge.

## 1. Source and scope

The exact registry row is `T336_REGISTRY.json`. Its title is “Transformers as amortized Bayesian inference: approximation and generalization.” The current repaired dossier asks for a fixed GP prior, bounded kernel on a compact domain, positive observation noise, bounded context labels, uniform forward KL for the noisy predictive, transformer size, and an ERM bound for the prior-averaged objective. Its only numbered target is finite rank. That target was reported closed in the 2026-10-21 moves entry by C002/C005. Infinite rank and the ERM clause are larger-statement obligations.

This note adds **continuity of the kernel**. The existing C003 exhibits a rank-one discontinuous kernel for which every continuous Gaussian predictor has a fixed positive uniform forward-KL error, showing that boundedness alone is insufficient for a theorem covering all kernels. This does not assert that continuity is necessary for every individual kernel or parameter regime. Therefore the statement below is not a full solution of an interpretation permitting every bounded discontinuous kernel.

Architecture throughout: bidirectional residual attention

    h_i -> h_i + (1/N) sum_heads sum_j ReLU(<Q h_i,K h_j>) V h_j,

followed, when needed, by a tokenwise residual MLP

    h_i -> h_i + W2 ReLU(W1 h_i).

The token count is fixed at N=n+1 by zero-role padding. These are Definitions 1–3 of Bai et al., arXiv:2306.04637, with arbitrary real weights. There is no softmax, layer normalization, causal mask, or free nonlinear kernel/feature oracle. A constant coordinate implements affine biases. The network outputs two coordinates interpreted as a Gaussian mean and positive variance. A prior scale is absorbed into the kernel.

The exact C002 proof and C004 encoder were read locally. Sections 5–6 below restate enough of their algebra to specify the composition. No independent claim that the historical result is new is made.

## 2. Main theorem and completely specified size

Let X be a nonempty compact subset of R^d, d>=1. Let k be a continuous, real, symmetric PSD kernel on X, with

    0 <= k(x,x) <= R^2.

The kernel can have infinite rank. Fix n>=0, B>=0, observation-noise variance s>0, and eps>0. The prior is GP(0,k), every observation adds independent N(0,s) noise, and the target is a new noisy observation. The approximation statement is deterministic and uniform over every context of length t<=n, labels |y_i|<=B, and query x in X. The input consists only of raw coordinates, labels, two role flags, and fixed constants.

If R=0 then k=0 by PSD Cauchy–Schwarz, and the exact output (0,s) is constant. Assume R>0 below.

Define the canonical modulus using ambient L1 distance:

    Omega(r) = sup{sqrt(k(x,x)+k(y,y)-2k(x,y)):
                   x,y in X, ||x-y||_1 <= r}.

It is finite, nondecreasing, and tends to zero as r decreases to zero. Set

    S=R+1,
    H0=1+n S^2/s,
    Cm=n B H0/s,
    Cv=H0^2,
    theta=min(1, sqrt(s eps)/(2(1+Cm)),
                 s sqrt(eps)/(2Cv), s/(4Cv)),
    eta=theta/[2(2R+1)].

Thus 0<eta<=1. Choose a fixed r0>0 with

    Omega(r0)^2 <= theta/2,

and a finite r0-net G0 contained in X. Let p=|G0|>=1. These choices depend only on the fixed prior and desired accuracy, never on the presented context.

For the feature encoder put

    e=eta/sqrt(p),
    choose r1>0 such that Omega(r1)<=e/2,
    Acone=(2R+e)/r1,
    h=e/(2Acone).

Choose a fixed finite h-net G1 in X and let J=|G1|>=1. A specified upper modulus and covering-number bound make all these quantities quantitative. Continuity guarantees existence but is not an algorithm for computing an arbitrary kernel's modulus from black-box queries.

For the solver set

    eps0=min(eps/4,1/16),
    kappa=1+max(1,n) S^2/s,
    M=n S^2 B/s,
    delta=min(1/2, s/(2S^2), sqrt(s eps0)/(1+M),
              s sqrt(eps0)/S^2),
    T=ceil(sqrt(kappa) log(2/delta)/2).

There exists a transformer of the specified architecture with

    token width D=7p+6+d+Jd+pJ,
    tokenwise MLP hidden width <= H=2Jd+pJ+4p+1,
    depth L=T+5+ceil(log_2 J),
    at most five attention heads per layer,
    at most L(15D^2+2DH)+2D dense real parameters,

whose output (mhat,vhat) satisfies

    vhat>=s,
    |m-mhat|<=sqrt(s eps),
    |v-vhat|<=min(s/2,s sqrt(eps)),
    KL(N(m,v) || N(mhat,vhat))<=eps.

Here (m,v) are the exact posterior noisy-predictive parameters under the original infinite-rank kernel k. All inequalities are uniform over the stated contexts and queries. The weights use only finitely many fixed kernel values on G0 union G1, a finite matrix factorization, net coordinates, and the displayed scalar constants. No context-dependent inverse is hidden in preprocessing.

The dense count includes zeros and is deliberately loose. It excludes only fixed affine placement of raw inputs and constants into registers. It is a size theorem over arbitrary real weights; it gives no bit complexity, bound on offline kernel-evaluation/factorization time, or SGD convergence.

## 3. Finite-rank reduction with a uniform residual bound

Construct the canonical Hilbert space from finite combinations of symbols Phi(x), with inner product <Phi(x),Phi(y)>=k(x,y), quotienting zero-norm vectors and completing. PSD implies Cauchy–Schwarz, so

    ||Phi(x)||<=R,
    ||Phi(x)-Phi(y)||^2=k(x,x)+k(y,y)-2k(x,y).

The latter and continuity of k show Phi is continuous. Compactness then gives uniform continuity. Equivalently, if Omega(r) did not tend to zero, there would be x_j,y_j with ||x_j-y_j||_1->0 and feature distance bounded away from zero. A convergent subsequence in compact X would give a contradiction to continuity of the displayed kernel expression.

Let V0=span{Phi(a):a in G0} and let P0 be orthogonal projection onto V0. This is a finite-dimensional closed subspace, of dimension <=p. Define

    k0(x,y)=<P0 Phi(x),P0 Phi(y)>,
    r(x,y)=<(I-P0)Phi(x),(I-P0)Phi(y)>.

Both k0 and r are PSD and k=k0+r, because the cross terms vanish. If a in G0 is within r0 of x, then Phi(a) belongs to V0 and the best-approximation property gives

    ||(I-P0)Phi(x)|| <= ||Phi(x)-Phi(a)|| <= Omega(r0).

Consequently

    0<=r(x,x)<=Omega(r0)^2<=theta/2,
    |r(x,y)|<=sqrt(r(x,x)r(y,y))<=theta/2.

Choose orthonormal coordinates on V0, padded to p coordinates, for z(x)=P0 Phi(x). Then

    k0(x,y)=z(x)^T z(y), ||z(x)||<=R,
    ||z(x)-z(y)|| <= ||Phi(x)-Phi(y)||.

In particular the modulus of z is at most Omega. This proof makes no Mercer eigenfunction assumptions, requires no reference design measure, and works for arbitrary compact Euclidean domains.

The necessary fixed feature samples are explicitly finite-data quantities. Write K00=(k(a,b)) on G0 and diagonalize its positive part as U Lambda U^T. Coordinates of P0 Phi(x) can be taken as

    z(x) = Lambda^(-1/2) U^T (k(a,x))_{a in G0},

with zeros appended. A vector in the nullspace of K00 represents a zero-norm combination of Phi(a), hence is orthogonal to every Phi(x); thus the cross-kernel vector is in range(K00). The coordinate formula and its inner products follow. Only z(b) at b in G1 are used as encoder weights, computed from K00 and K01. The formula is not evaluated on runtime inputs.

## 4. Raw feature encoding and total kernel error

For each coordinate j<=p define the finite cone envelope

    ztilde_j(x)=min_{a in G1}[z_j(a)+Acone ||x-a||_1].

For a with ||x-a||_1<=r1, the first term is at least z_j(x)-e/2. For a farther than r1, use |z_j(a)|,|z_j(x)|<=R to obtain

    z_j(a)+Acone||x-a||_1 > z_j(x)-2R+Acone r1
                                      =z_j(x)+e.

Every candidate is therefore at least z_j(x)-e/2. For the upper bound, choose a within h. Since h=e r1/[2(2R+e)]<=r1/2,

    ztilde_j(x)<=z_j(x)+Omega(r1)+Acone h<=z_j(x)+e.

It follows that

    sup_x ||ztilde(x)-z(x)||<=sqrt(p)e=eta,
    ||ztilde(x)||<=R+eta<=S.

Define the finite-feature PSD kernel ktilde(x,y)=ztilde(x)^T ztilde(y). For any x,y,

    |k0(x,y)-ktilde(x,y)|
      <= ||z(x)-ztilde(x)|| ||z(y)||
         + ||ztilde(x)|| ||z(y)-ztilde(y)||
      <= (2R+eta)eta <= (2R+1)eta = theta/2.

Together with Section 3 this gives

    sup_{x,y}|k(x,y)-ktilde(x,y)|<=theta,
    k(x,x),ktilde(x,x)<=S^2.

It is important that ktilde is PSD by its feature representation; merely approximating arbitrary kernel entries would not guarantee the predictive variance floor.

## 5. A uniform kernel-to-predictive perturbation lemma

This lemma is useful independently of the network. Suppose k and ktilde are any real PSD kernels with diagonal at most S^2 and sup entrywise difference <=a. For a context of t<=n points, let K,Ktilde be their Gram matrices, b,btilde their vectors of query covariances, c,ctilde their query diagonal values, and

    A=K+sI, Atilde=Ktilde+sI.

Both inverse norms are <=1/s. Entrywise bounds and PSD Cauchy–Schwarz give

    ||A-Atilde||op<=t a,
    ||b-btilde||<=sqrt(t)a,
    ||b||,||btilde||<=sqrt(t)S^2,
    ||y||<=sqrt(t)B,
    ||A^(-1)-Atilde^(-1)||op<=t a/s^2.

For t=0 the corresponding empty vectors contribute zero. The means and noisy variances are

    m=b^T A^(-1)y,  v=s+c-b^T A^(-1)b,
    mt=btilde^T Atilde^(-1)y,
    vt=s+ctilde-btilde^T Atilde^(-1)btilde.

The block matrix with entries (A,b;b^T,c) is PSD: it is the original joint kernel Gram matrix plus a PSD sI block on the context. Its Schur complement is nonnegative, so v>=s. The same proves vt>=s. Also v<=s+S^2 and vt<=s+S^2.

Adding and subtracting btilde^T A^(-1)y gives

    |m-mt| <= (t B/s)(1+tS^2/s) a <= Cm a.

For the variance, first change the two query factors holding A^(-1) fixed, then change the inverse. This gives

    |v-vt| <= [1+2tS^2/s+t^2 S^4/s^2] a
            <= Cv a.

Here Cm,Cv are exactly those in Section 2. This comparison does not assume the kernel residual has a sign and hence covers the encoder perturbation too. All quantities are deterministic and there is no design-distribution assumption.

Apply the lemma with a=theta to obtain

    |m-mt|<=sqrt(s eps)/2,
    |v-vt|<=min(s/4,s sqrt(eps)/2).

The 1+Cm denominator in theta handles B=0 and n=0 without division by zero.

## 6. Exact implementation and Chebyshev error

The encoder uses the same exact residual-MLP identities as C004. Its registers comprise the seven p-dimensional solver registers described below, four solver scalars, raw coordinates (d), two role flags, absolute values (Jd), and cone values (pJ). This is D=7p+6+d+Jd+pJ.

1. One MLP layer computes every |x_r-a_r| as ReLU(x_r-a_r)+ReLU(a_r-x_r), using 2Jd hidden units.
2. One layer writes all pJ cone candidates from the nonnegative absolute registers and the constant register.
3. A balanced tournament uses u-ReLU(u-v)=min(u,v) in the first slot of each pair. It takes ceil(log_2 J) residual-MLP layers, with disjoint output slots at each level. An unpaired entry passes through. The identity works for signed values.
4. One layer routes each feature according to binary context/query flags using, for |f|<=S,

       g(f,r)=ReLU(f+S(r-1))-ReLU(-f+S(r-1)).

   This equals f for r=1 and zero for r=0. It takes 4p hidden units. Padding uses any fixed anchor point of X and both flags zero.

Thus E=3+ceil(log_2 J) encoder layers suffice, with the claimed H. All their attention value matrices are zero. This computes ztilde exactly, not approximately as an algebraic expression.

For completeness, the finite-feature solver uses registers

    (z_c,z_q,qbar,w,u,w_old,u_old ; y,one,mout,vout).

Initially the encoder supplies z_c for context tokens and z_q for the single query, with zero feature roles on padding. The other working registers vanish; one=1, vout=s. A one-head layer with Q=K=one and V writing N z_q broadcasts q=ztilde(x) into qbar at every token.

Set

    Af=sI+sum_i ztilde_i ztilde_i^T,
    f=sum_i ztilde_i y_i.

The exact finite-feature mean and noisy variance are

    mt=q^T Af^(-1) f,
    vt=s+s q^T Af^(-1) q.

The spectrum of Af lies in [s,s+max(1,n)S^2]. With c=(Lspec+s)/2, dspec=(Lspec-s)/2, alpha=c/dspec>1, and Chebyshev polynomials C_j, use

    eta_0=1/c, beta_0=0,
    eta_j=2 C_j(alpha)/(dspec C_{j+1}(alpha)),
    beta_j=C_{j-1}(alpha)/C_{j+1}(alpha), j>=1,

in the two simultaneous recurrences

    w_next=w+beta_j(w-w_old)+eta_j(f-Af w),
    u_next=u+beta_j(u-u_old)+eta_j(q-Af u).

Start all iterates at zero. Five attention heads realize one update exactly: two signed-ReLU heads implement sum_i z_i(y_i-z_i^T w), two implement -sum_i z_i z_i^T u, and one constant-score averaging head supplies ridge, momentum, q, and previous-iterate updates. All iterate registers remain identical at every token. Detailed Q/K/V coordinate lists are in the pinned C002, Section 4. This is an exact use of ReLU(a)-ReLU(-a)=a; no multiplication is hidden outside attention.

The residual polynomial after T steps is

    r_T(lambda)=C_T((c-lambda)/dspec)/C_T(alpha).

For lambda in the spectral interval,

    |r_T(lambda)| <= 2 ((sqrt(kappa)-1)/(sqrt(kappa)+1))^T
                  <= 2 exp(-2T/sqrt(kappa)) <= delta.

The recurrence follows by substitution and the Chebyshev three-term identity. Denominators are positive because C_j(alpha)=(zeta^j+zeta^(-j))/2 for zeta=alpha+sqrt(alpha^2-1)>1. The middle estimate follows from log((1+x)/(1-x))>=2x for 0<x<1.

A four-head signed-ReLU readout produces q^T w and s+s q^T u. Since u=g_T(Af)q with g_T(lambda)=(1-r_T(lambda))/lambda>0 when delta<=1/2, its variance output is >=s. The approximation errors satisfy

    |mt-mhat|<=M delta<=sqrt(s eps0)<=sqrt(s eps)/2,
    |vt-vhat|<=S^2 delta<=s sqrt(eps0)
                                <=min(s/4,s sqrt(eps)/2).

The solver contributes T+2 layers and at most five heads, giving the claimed total depth and parameter count.

Combining scalar errors from Sections 5 and 6 proves the displayed mean/variance error bounds. For any Gaussian target and model with variances >=s and |v-vhat|<=s/2, write h=(v-vhat)/vhat. Then |h|<=1/2 and

    KL=(h-log(1+h))/2+(m-mhat)^2/(2vhat)
      <=(v-vhat)^2/(2s^2)+(m-mhat)^2/(2s)<=eps.

The elementary bound h-log(1+h)<=h^2 on [-1/2,1/2] follows by integration of h/(1+h). This proves the theorem without using a triangle inequality for KL.

## 7. Explicit RBF corollary without a Mercer tail assumption

Let X=[0,1]^d and

    k(x,y)=R^2 exp(-||x-y||_2^2/(2 ell^2)), ell>0, R>0.

Let c=(1/2,...,1/2), u=(x-c)/ell, and U=d/(4ell^2). The exact feature expansion is

    Phi_alpha(x)=R exp(-||u||^2/2) u^alpha/sqrt(alpha!),
    k(x,y)=sum_{alpha in N^d} Phi_alpha(x)Phi_alpha(y).

Absolute convergence follows from the exponential series, or from the squared-norm identity and Cauchy–Schwarz. For an integer r>=1 retain multi-indices |alpha|<=r-1. This has

    p=binom(d+r-1,d)

features. The residual kernel is PSD. Its diagonal is

    R^2 exp(-||u||^2) sum_{j=r}^infty ||u||^(2j)/j!
      <= R^2 U^r/r!.

To see the inequality directly, (r+h)!>=r! h!, so the sum is at most (||u||^(2r)/r!) exp(||u||^2), which cancels the prefactor. Also r!>=(r/euler)^r by integrating log over [1,r]. Therefore the explicit choice

    r=max(1,ceil(max(euler^2 U, log(2R^2/theta))))

gives U^r/r!<=(euler U/r)^r<=exp(-r) and residual diagonal <=theta/2. Its off-diagonal absolute value has the same bound by PSD Cauchy–Schwarz. This truncation has p polynomial in log(1/theta) for fixed d,ell,R.

The full canonical feature distance satisfies

    ||Phi(x)-Phi(y)||^2
      =2R^2[1-exp(-||x-y||_2^2/(2ell^2))]
      <=(R^2/ell^2)||x-y||_2^2.

Coordinate truncation is an orthogonal projection, so the retained z obeys ||z||<=R and each coordinate is K-Lipschitz in L1 with K=R/ell. Use the simpler Lipschitz cone envelope of C004 on the regular grid with

    m=max(1,ceil(K d sqrt(p)/eta)),
    G1={0,1/m,...,1}^d, J=(m+1)^d.

For every coordinate, the envelope min_a[z_j(a)+K||x-a||_1] lies between z_j(x) and z_j(x)+Kd/m; hence the Euclidean feature error is <=eta. Sections 4–6 apply unchanged. The same formulas for D,H,L,T and parameter count now depend only on d,ell,R,n,B,s,eps and elementary arithmetic, with no unspecified modulus, net, or kernel eigenfunctions.

This is a particularly direct completion of the dossier's stated RBF truncation obstruction. The Gaussian feature expansion, its truncation, finite-net approximation, and Chebyshev method are classical ingredients. The present contribution is their explicit assembly into the exact T336 architecture and deterministic uniform noisy-predictive KL budget; publication-level novelty remains unestablished.

## 8. Optional bounded-output interface for ERM

The exact target has

    s<=v<=s+R^2,
    |m|<=B sqrt(n R^2/s).

The mean bound follows from k_query^T A^(-1)k_query<=R^2 and y^T A^(-1)y<=nB^2/s by Cauchy–Schwarz in the A^(-1) inner product. Let M_B=B sqrt(n R^2/s), with M_B=0 when n=0 or B=0.

Clipping the network mean to [-M_B,M_B] and its variance to [s,s+R^2] preserves the scalar error bounds, because each target coordinate lies in the interval onto which that coordinate is projected. Thus the same KL proof remains valid. A clip to [a,b] has the residual ReLU form t+ReLU(a-t)-ReLU(t-b); the constant register supplies the offsets. The two clips require one additional tokenwise MLP layer and four hidden ReLU units. Since the displayed H is already at least four, width need not increase. The depth/parameter count increases by one layer.

This does not claim that variance clipping always decreases total Gaussian KL: with a nonzero mean error, the optimal variance is v+(m-mhat)^2. The preserved scalar error bounds are the reason the stated KL guarantee survives.

An input-label clip at B, if used to handle genuine unbounded GP training labels, is also a finite tokenwise ReLU operation and costs one additional MLP layer. The deterministic uniform theorem applies on the event that all original context labels are within B. Controlling the complement and finite-sample ERM requires a separate probabilistic argument.

## 9. What has and has not been obtained

- The all-continuous-kernel approximation clause has an explicit existence/size proof, including raw encoding. An explicit RBF formula avoids an unspecified Mercer truncation rate.
- The proof permits infinite rank, arbitrary compact X, all contexts of length <=n, and repeated observations. Positive s handles singular Gram matrices.
- It is a real-weight construction and an ERM comparator, not a statement that gradient descent learns the weights.
- C003 still blocks the literal bounded-discontinuous-kernel uniform raw-input claim. This hypothesis repair cannot be suppressed when reporting scope.
- A full T336 settlement would additionally require the prior-averaged training/sample-complexity result, careful interpretation of the registry's prior/design assumptions, independent audits, and a novelty comparison. The present note alone is not such a settlement.
