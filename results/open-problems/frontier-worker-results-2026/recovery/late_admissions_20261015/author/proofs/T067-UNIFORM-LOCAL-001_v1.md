# T067-UNIFORM-LOCAL-001 v1: explicit q3 critical local radii at every degree

Status: proof (unaudited), conditional on T067-CUBIC-FUSION-001 v1 and the F2,C inequalities of T067-TERNARY-MOMENTS-001 v1. No priority assertion. No global canonical entry assertion.

Let d>=3 be an integer, lambda=1/sqrt(d), and let mu be a uniform-mean, fully coordinate-permutation-invariant posterior-law fixed point of the regular d-child, uniform-root, three-state ferromagnetic Potts BP map. Put

    M=E|3(p-u)|^2, U=E|3(p-u)|^4,
    T=E sum_i[3(p_i-u_i)]^3, u=(1/3,1/3,1/3), x=M/9.

We prove the following two exclusion statements, including their endpoints:

    for every integer d>=3: x<=3/100 implies mu=delta_u;
    for every integer d>=100: x<=1/10 implies mu=delta_u.  (UL)

All degree dependence is covered by two exact bivariate polynomial certificates; there is no unverified final degree cutoff or extrapolation from a list of degrees.

## 1. Child prefixes and global fixed-point moment bounds

Write mu_j for the root-posterior law after the first j child experiments, and M_j,U_j,T_j for its moments, with mu_0=delta_u and mu_d=mu. Each individual child message has moments

    m=M/d, V=U/d^2, t=lambda*T/d.

The positive critical edge has lambda<=1/sqrt(3)<eta=2887/5000. Every effective child posterior coordinate is at least (1-eta)/3. The generic fourth/cubic fusion inequalities F2,C therefore apply at every merge, including the first pair:

    U_(j+1)<=U_j+U/d^2+(5/d)M_j*M,
    |T_(j+1)-T_j-lambda*T/d|<=(5/(3d))M_j*M.              (1)

Discarding observations is a degradation. Conditional Jensen and the fixed-point equality give M_j<=M for j<=d. The cubic-fusion sign lemma applies since d*lambda^3=lambda<1: T>=0, and repeated fusion gives T_j>=0 for every prefix. These facts require no assumption on the sign of a general symmetric input law.

Induct on a target prefix k=2,...,d. Before treating k, assume

    M_j<=j*M/d for 1<=j<k.                                (2)

The j=1 equality starts the induction. Combining (2) with M_j<=M for j>=k gives

    sum_(j=1)^(d-1) M_j
       <=M*[k(k-1)/(2d)+d-k].                             (3)

Telescoping (1) to the fixed point yields

    (1-1/d)U <=(5M/d) sum_(j=1)^(d-1) M_j,
    (1-lambda)T <=(5M/(3d)) sum_(j=1)^(d-1) M_j.

Define

    Z=k(k-1)/2+d(d-k),
    Cu=5Z/[d(d-1)], Ct=Cu*(1+lambda)/3.

Using (1-lambda)(1+lambda)=(d-1)/d, we obtain

    U<=Cu*M^2, 0<=T<=Ct*M^2.                              (4)

For every j<k, telescope (1) using only the earlier prefix bounds (2). This gives

    U_j<=u_j*M^2, T_j<=t_j*M^2,
    u_j=[j*Cu+(5/2)j(j-1)]/d^2,
    t_j=j*lambda*Ct/d+(5/6)j(j-1)/d^2.                   (5)

This is an ordered induction. The bound on M_k is not used in (3)--(5) before being proved.

## 2. Exact variance identity and a polynomial error bound

For two independent symmetric base posterior deviations a,b, let their second, fourth and cubic moments be m,V,T_a and n,W,T_b. Put c=a.b, S=3+c, v=a+b+a*b-(c/3)1 and N=|v|^2. The exact Bayesian fusion identity, proved by the tensor contractions in T067-TERNARY-LOCAL-001 v1, is

    M_fuse=m+n-mn/6-(n*T_a+m*T_b)/3+R,
    R=E[N*c^2/(3S)]>=0,
    E[N*c^2]=(nV+mW)/2+3T_a*T_b
                         +(V*T_b+T_a*W)/2+VW/12.          (6)

These equations use independent marginal base laws; the Bayesian pair weight S/3 has already been accounted for. In this application both cubic moments are nonnegative, so the displayed cubic term in M_fuse is nonpositive and can be discarded in an upper bound. All terms used to upper-bound E[N*c^2] are nonnegative.

For the first two individual child messages, S>=3(1-lambda^2)=3(d-1)/d. To see this, write their effective posteriors as u+lambda*(p-u),u+lambda*(r-u), and use p.r>=0. For a later prefix merged with one child message, S=9 sum_i p_i r_i>=3(1-lambda), because every right coordinate is at least (1-lambda)/3.

Set

    Kpre=d/[9(d-1)], K=1/[9(1-lambda)],
    ve=Cu/d^2, te=lambda*Ct/d,
    g_j=j(j-1)/(12d^2),
    A2=Kpre*Cu/d^3,
    B2=Kpre*[3Ct^2/d^3+lambda*Cu*Ct/d^3+Cu^2/(12d^4)].

Substituting (4) into (6) for the first pair gives

    M_2<=2M/d-g_2*M^2+A2*M^3+B2*M^4.                    (7)

For 2<=j<k define recursively

    A_(j+1)=A_j+g_j/(6d)
                    +K*[u_j/(2d)+j*Cu/(2d^3)],
    B_(j+1)=B_j+K*[3t_j*te+(u_j*te+t_j*ve)/2+u_j*ve/12]. (8)

Then the same identity implies

    M_k<=kM/d-g_k*M^2+A_k*M^3+B_k*M^4.                  (9)

Here is the induction in detail. In (6) use left moments M_j,U_j,T_j and right moments M/d,U/d^2,lambda*T/d. Drop its nonpositive cubic term. From (2),(4),(5) and the later-merge denominator bound, the remainder is at most

    K*[u_j/(2d)+j*Cu/(2d^3)]*M^3
      +K*[3t_j*te+(u_j*te+t_j*ve)/2+u_j*ve/12]*M^4.

The leading variance terms are (1-M/(6d))*M_j+M/d. Since M<=6 and d>=3 this multiplier is positive, so insert the inductive version of (9). Multiplication increases A by g_j/(6d). It adds only the nonpositive terms -A_j*M^4/(6d),-B_j*M^5/(6d), which may be dropped because all A_j,B_j are nonnegative. The new quadratic coefficient is g_j+j/(6d^2)=g_(j+1). This proves (8),(9) without assuming the desired linear bound at k.

## 3. Closed forms for all k,d

For k>=2 put

    S1=k(k-1)/2-1=sum_(j=2)^(k-1) j,
    S2=k(k-1)(k-2)/3=sum_(j=2)^(k-1) j(j-1),
    sum_u=[Cu*S1+(5/2)S2]/d^2,
    sum_t=lambda*Ct*S1/d+(5/6)S2/d^2.

Summing (8) gives exactly

    A_k=A2+S2/(72d^3)+K*[Cu*S1+(5/4)S2]/d^3,
    B_k=B2+K*[(3te+ve/2)*sum_t+(te/2+ve/12)*sum_u].      (10)

The sums vanish at k=2. For integer 2<=k<=d all constants are nonnegative. If, for a positive Mstar<=6 and a number delta>0,

    (1-delta)*g_k-Mstar*A_k-Mstar^2*B_k >=0              (11)

holds at every target k, then for every 0<M<=Mstar, (9) gives

    M_k<=kM/d-delta*g_k*M^2<kM/d.                        (12)

Thus it proves the next inductive bound. At k=d, M_d=M makes (12) impossible. Hence no nonzero fixed point can have M<=Mstar.

## 4. Two certificates covering the unbounded degree range

For the purpose of certifying (11), write a real variable l=lambda, substitute

    d=1/l^2, k=2+r(d-2), 0<=r<=1,
    l=L*z, 0<=z<=1.

Every integer pair d>=3,2<=k<=d is included in the first rectangle below, because 1/sqrt(3)<2887/5000. Every such pair with d>=100 is included in the second rectangle. Values at l=0 are used only for the continuous polynomial certificate; actual degrees have l>0.

Let G=(1-delta)g_k-Mstar*A_k-Mstar^2*B_k, using (10). Exact rational simplification gives a polynomial P(z,r)=D(l)*G, with strictly positive denominator-clearing factor D(l) for 0<l<=L<1. The parameters are:

| Certificate | Mstar | xstar=Mstar/9 | L | delta | D(l) |
| --- | --- | --- | --- | --- | --- |
| all_d3 | 27/100 | 3/100 | 2887/5000 | 1/100 | 12800(1-l)^3(1+l)^3 |
| large_d100 | 9/10 | 1/10 | 1/10 | 1/20 | 1920(1-l)^3(1+l)^3 |

For each row the stored raw integer polynomial H differs from P only by the positive rational factor recorded in its metadata. Each has degrees (17,6) in (z,r). Converting both coordinates to the tensor-product Bernstein basis on [0,1]^2 gives 126 possible coefficients: 120 strictly positive and 6 zero, with none negative. The nonnegative Bernstein basis therefore proves (11) throughout each closed rectangle, including every actual k,d in the asserted ranges. The positive retained fractions delta give strictness in (12) even at a zero of P.

The builder checks/uniform_local_certificate.py uses exact rational/symbolic algebra and integer Bernstein conversion. Reproduce with

    python -X utf8 checks/uniform_local_certificate.py --M 27/100 --lambda-max 2887/5000 --margin 1/100 --name all_d3
    python -X utf8 checks/uniform_local_certificate.py --M 9/10 --lambda-max 1/10 --margin 1/20 --name large_d100

The checks/uniform_local_<name>_raw,bern1,bern2,report.json files give every coefficient, scaling factor, parameters and source hash. There are no floating-point bounds, infinite truncations, sampled degrees or asymptotic error terms in this step. Each tensor has fewer than 130 entries and the memory estimate is below 10MB.

The separate checks/uniform_local_fast_independent_check.py imports no builders or computer-algebra libraries. It first cancels inverse powers of l explicitly: w=l^2, K0=k*w=r+2(1-r)w, D0=1-w, H1=K0(K0-w)-2w^2 and H2=K0(K0-w)(K0-2w). Then Cu=N/D0 and Ct=J/D0, where N=(5/2)[K0(K0-w)+2(1-K0)] and J=(1+l)N/3. Substituting these into the prefix sums reconstructs D0^3*A_k and D0^3*B_k as exact rational bivariate polynomials, without any negative power or rational-function simplifier. It checks coefficientwise equality of the restored raw polynomial with D(l)*G. It also independently verifies every coefficient in both Bernstein transformations by exact rational dot products and checks every final sign. Its two fast_independent.json reports record hashes and PASS. Additional exact checks compare this independently reconstructed polynomial to the unsummed prefix recurrence at integer square degrees. The builder itself compares (10) to direct rational prefix recurrences at 23 integer (d,k) pairs with d=4,9,16,25,49. Those finite comparisons are checks of the encoding; the polynomial identity and full rectangles establish the unbounded parameter assertion. The optional generic-CAS checker is not a dependency of this certificate.

Apply (11),(12) in order for k=2 through d. A positive M<=27/100 contradicts the fixed-point equality for every d>=3; a positive M<=9/10 contradicts it for every d>=100. Since M=0 implies p=u almost surely, this proves (UL), conditional on the stated fusion lemmas.

## Scope

This is a critical fixed-point exclusion result only. It does not by itself put the canonical posterior sequence into either local radius. The existing independently checked binary proof has its own radius. The submitted ternary and degree-four proofs have separate exact entry certificates and do not depend on this new version. Closing q=3 at every regular degree still needs a rigorous global-entry argument or enough separately certified cases together with an explicit large-degree bridge. q=4 and arbitrary Galton-Watson offspring require further arguments.

NEXT: Obtain external audits of the cubic and uniform-local lemmas; use the explicit high-degree radius in a separate canonical-entry argument, and test whether lower-degree finite certificates can use coarser grids with the larger local radius.
