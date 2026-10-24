# C0052: independent repeated-site obstruction

Saved 2026-10-10 before reading w474's proof. Author derivation; independent review is pending. This does not solve C0052 and makes no novelty claim.

Let a finite zero-field ferromagnetic Ising measure have spins sigma_x in {-1,1}. Write G(x,y)=E[sigma_x sigma_y] and U4 for its fourth joint cumulant. For nonnegative weights w_x, let S=sum_x w_x sigma_x and V=E[S^2]>0. Define q_x=w_x sum_y w_y G(x,y)/V. Then q_x>=0 and sum_x q_x=1.

The spin identity sigma_x^2=1 gives, exactly,

    U4(x,x,y,z) = -2 G(x,y) G(x,z).

Let D be minus the weighted U4 sum over ordered quadruples having at least one repeated site, divided by V^2. Every such summand is nonnegative. The union of the six equal-pair constraints therefore gives

    0 <= D <= 12 sum_x q_x^2 <= 12 max_x q_x.

For uniform weights on a transitive finite graph with N vertices, the covariance row sums are all chi, V=N chi, q_x=1/N, and hence D<=12/N at every inverse temperature. On a three-dimensional torus of side L this is 12/L^3.

Thus repeated-site terms alone cannot give a positive limiting normalized fourth cumulant for a delocalized sequence. A proposed proof must control a total weighted mass of distinct-site quadruples on growing scales. The inequality requires no unproved 3D critical exponent. Positivity of G is a ferromagnetic input; the repeated-site identity itself only uses spin-flip symmetry and sigma_x^2=1.

For every finite observed set (including a block in an infinite-volume measure), Cauchy--Schwarz gives (Gw)_x^2<=V. Hence q_x<=w_x/sqrt(V), and

    D <= 12 max_x w_x / sqrt(V) <= 12 ||w||_infinity / ||w||_2.

The last step uses G>=0 and G(x,x)=1, so V>=sum_x w_x^2. Uniform weights on any N-site observed set therefore give D<=12/sqrt(N), without transitivity or an exponent hypothesis. For nonnegative, nonzero f in C_c(R^3), w_x=f(x/L) gives D=O_f(L^(-3/2)). This is a rate for the repeated-site contribution only.

## Exact weighted count

Write h_x=(Gw)_x, A=sum_x w_x^2 h_x^2, B=sum_xy w_x^2 w_y^2 G(x,y)^2, C=sum_x w_x^3 h_x, E=sum_x w_x^4. The unnormalized negative repeated-site sum is exactly

    12 A - 6 B - 16 C + 12 E.

Proof by disjoint multiplicity patterns: (4) contributes 2E; (3,1) contributes 8(C-E); (2,2) contributes 6(B-E); and (2,1,1) contributes 12(A-2C+2E-B). These four patterns exhaust all repeated-site ordered quadruples. The sum is nonnegative even though the simplified formula has negative coefficients.

## Source-normalized subcritical coupling

The primary source is Duminil-Copin, Lectures on the Ising and Potts models on the hypercubic lattice (29 June 2017), printed p.94, equations (7.1)--(7.2), Conjecture 6 and Exercise 61. It uses the signed coupling

    g(beta) = sum_{x2,x3,x4} U4(0,x2,x3,x4) / (chi(beta)^2 xi(beta)^d),
    chi=sum_x G(0,x),
    xi=(-lim_{n->infinity} n^(-1) log G(0,n e1))^(-1).

For a translation-invariant, spin-flip-symmetric +/-1 law on Z^d with G>=0, chi<infinity, let b=sum_x G(0,x)^2. The negative repeated-site part of the anchored sum is exactly

    C_contact = 12 chi^2 - 6 b - 16 chi + 12.

This follows from the same four multiplicity patterns, now pinned at the first coordinate 0. Absolute convergence of the repeated-site terms follows from chi<infinity and 0<=G<=1. Equivalently, the four pattern contributions per anchor are 2, 8(chi-1), 6(b-1), and 12(chi^2-2chi+2-b). For the (2,1,1) pattern, half the weight has 0 as the doubled site, and half has a different doubled site; translation invariance makes their sums equal.

Thus, whenever xi>0,

    0 <= C_contact / (chi^2 xi^d) <= 12/xi^d.

If chi and xi diverge, then b<=chi implies xi^d times this contribution tends to 12. This identifies the exact leading contact coefficient. In d=3 the contact contribution tends to zero along every sequence with xi->infinity. On-site or equal-pair cumulants cannot establish the source's conjecture.

The exact target as phrased by the source is failure of g(beta)->0 as beta increases to beta_c. Because -g>=0 for ferromagnetic Ising, a nonvanishing subsequence is sufficient for that phrasing. A positive full liminf or non-Gaussianity of every subsequential critical field is a stronger quantified route and must be labeled accordingly. The signed convention differs from the positive physical coupling -g.

The coefficient 12 is sharp over the stated translation-invariant positive-correlation class: the stationary one-dimensional Ising covariance G(k)=t^|k| has chi=(1+t)/(1-t)->infinity and b=(1+t^2)/(1-t^2)<=chi as t increases to 1. It can also be placed on independent parallel lines of Z^d. This is a sharpness example for the contact estimate, not the isotropic critical 3D model.

Primary source: https://www.ihes.fr/~duminil/publi/2017_PIMS.pdf

## Independent bridge obstruction for current sprinkling

This derivation was saved before reading w474's proof. It refutes a model-uniform reverse comparison, not C0052.

Let the graph be the path with vertices 0,...,3m, zero external field and every edge coupling beta>0. Put four distinct, comparably separated sources a=0, b=m, c=2m, d=3m. Let n1,n2 be independent currents with source sets {a,b},{c,d}; n3,n4 are independent sourceless currents. Write t=tanh(beta), p=t^2. On a tree, the source condition fixes parity separately on every edge and the conditional edge counts are independent. Along the m middle bridge edges each current is even; an even count is zero with probability 1/cosh(beta).

Consequently the original two-current connection probability is

    P_original = p^m.

After adding the two sourceless currents, the independent clusters C(n1+n3,a) and C(n2+n4,c) each advance into the bridge across edges open independently with probability p. Their geometric prefix/suffix lengths K_left,K_right satisfy P(K>=j)=p^j for 0<=j<=m. They intersect exactly when K_left+K_right>=m. Splitting according to K_left<m or K_left>=m gives

    P_sprinkled = p^m [1+m(1-p)].

Hence P_sprinkled/P_original=1+m(1-p) is unbounded with m at fixed beta. No graph- and scale-uniform constant c>0 can reverse the source's one-sided inequality P_original<=P_sprinkled into P_original>=c P_sprinkled. A transfer to the full critical Z^3 model would need an additional, model-specific premise. Even the four source distances in this obstruction are all of order m.

The same path spin law independently checks P_original: G(i,j)=t^|i-j| and U4(0,m,2m,3m)=-2t^(4m), so the exact switching ratio -U4/(2G(0,m)G(2m,3m)) is t^(2m)=p^m.

Relevant source identity: Aizenman--Duminil-Copin, arXiv:1912.07973, equations (3.11)--(3.14). Its two source clusters in (3.11) share the sum n1+n2; they are not independent. Independence enters only after introducing n3,n4, and gives an upper bound.

## Boundary of the transitive finite-graph estimate

The 12/N estimate needs transitivity; it does not hold for arbitrary uniform-weight positive-correlation fields. Take N spins consisting of m perfectly locked spins (one common fair sign) and N-m independent fair spins, all independent across components. Then V=m^2+N-m. Joint cumulants vanish across independent components. The locked component contributes -U4=2 on every tuple, and the independent spins only contribute their on-site cumulants. Its exact contact ratio is

    D = [12m^3-22m^2+12m+2(N-m)]/(m^2+N-m)^2.

For m=floor(sqrt(3N)), sqrt(N)D tends to 9sqrt(3)/4>0. Thus the general 12/sqrt(N) estimate has optimal decay exponent over the broader spin-field class. Fully locked spins are a zero-temperature limit of ferromagnetic components; this example is not a critical translation-invariant Ising model.

## Review and computation state

The ten rational cube checks in measurements.json passed in 39.5495 s; the seventeen extra checks in bridge_measurements.json passed in 0.08967 s. Finite computations corroborate the written proofs and do not establish the parent theorem. w476's REVIEW.jsonl rows R2 and R3 keep, respectively, the finite weighted/transitive contact bound and the path-current reverse-comparison obstruction. Review of the later general-block rate and source-normalized exact count is still recorded separately. Served model/account evidence and frozen-hash referee attestations are unavailable.

NEXT: Check w474's explicit bridge against these source quantifiers and one-sided comparisons; request independent review of the exact counts.
