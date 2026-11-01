# One collision of quadratic affine rows

Entropy is in bits. All physical cubes carry independent uniform coordinates. For a real function u, write E(u)=sum_i ||D_i u||_2^2 and mu(u)=||u||_2^2. When mu>0 let P_u(T)=uhat(T)^2/mu. This E is the usual influence when u is Boolean. No independence of spectral coordinates is assumed.

## Statement

Let F(X,Y) be Boolean and write F=sum_J chi_J(X) u_J(Y). Assume that each nonzero u_J is a sum of at most two signed quadratic phases on disjoint affine physical cells of Y. A phase is (-1)^q, with q of degree at most two over F2 in affine coordinates on its cell. The cells belonging to ALL rows partition Y. Then

H(S_Y|S_X)<=24 I_Y(F), and H(F)<=24 I_Y(F)<=24 I(F).

The X-degree can be any integer d>=1 (require |J|<=d if desired); neither constant depends on d or either dimension. The condition is stable under every physical Y coordinate restriction. It contains every single X-coordinate restriction of the previously accepted distinct-label quadratic affine partition class. It does not claim stability through unrestricted further X collisions.

Any admitted fresh-Y Boolean tensor factor has F2 phase degree at most three. Thus the condition excludes arbitrary tensor factors; a quartic monomial phase is an explicit exclusion. Some admitted cubic phases have genuinely nonproduct squared Fourier laws.

## 1. Quadratic component interface

For v=1_A(-1)^q on an affine cell of mass alpha=2^-k, the normalized spectrum is uniform on an affine coset, by the signed quadratic polar-kernel identity of A034's accepted quadratic-row theorem (also reconstructed as follows). Squaring a Fourier coefficient and grouping pairs by their difference w in the direction V leaves the character average of the polar form q(z+w)+q(z)+q(w)+q(0). It vanishes unless w belongs to the polar kernel. On that kernel the residual phase is linear, so the last character sum is either zero or the full kernel size. The surviving frequencies form an affine coset. If its dimension is s, H(P_v)=s. Every varying spectral coordinate is fair, hence sum_i P_v(i in T)>=s/2. Consequently

alpha H(P_v)<=2 E(v).

Also alpha k<=2 E(v): every coordinate direction outside V contributes alpha/2, and their number is at least codim V=k. These statements include rank-zero phases and singleton cells.

## 2. A generic coherent entropy inequality

Let a,b have disjoint physical supports, squared norms alpha,beta>0, mu=alpha+beta, lambda=alpha/mu, and u=a+b. Define Q=lambda P_a+(1-lambda)P_b. Orthogonality gives mu=||u||^2 and Cauchy gives P_u<=2Q pointwise. A zero of Q is a zero of P_u. Nonnegativity of KL and nonnegativity of log(1/Q) give

H(P_u)<=sum_T P_u(T) log2(1/Q(T))<=2 H(Q)
<=2[lambda H(P_a)+(1-lambda)H(P_b)+h2(lambda)].

This step is generic; it is NOT presented as a Booleanity consequence. Multiplication by mu retains the full normalized row entropy.

## 3. Geometric protection against energy cancellation

Let A=a0+V, B=b0+W be disjoint affine cells, with masses alpha,beta, and signed quadratic components a,b. Write E0=E(a)+E(b). For each physical coordinate i,

E_i(u)=E_i(a)+E_i(b)-<a,tau_i b>.

If A intersects B+e_i, then e_i belongs to neither V nor W (otherwise it would force A intersect B). Thus E_i(a)+E_i(b)=(alpha+beta)/2. Their intersection has mass gamma=2^(dim(V intersect W)-n), independent of the crossing direction, and |<a,tau_i b>|<=gamma.

If alpha != beta, the dyadic masses differ by a factor at least two, so gamma<=min(alpha,beta)<=(alpha+beta)/3. Thus E_i(u)>=E0_i/3 on crossing directions; on other directions E_i(u)=E0_i. If alpha=beta and V!=W, then dim(V intersect W)<=dim(V)-1, so gamma<=alpha/2=(alpha+beta)/4 and the stronger E_i(u)>=E0_i/2 holds. Therefore, EXCEPT when V=W and alpha=beta,

E(u)>=E0/3.

No lower bound on the individual quadratic polar ranks is used. The exceptional parallel case is handled separately, not passed through a false cancellation estimate. In particular two complementary halfcubes with the same sign can cancel all energy.

## 4. Complete row bill, nonparallel or unequal cells

Put k_A=log2(1/alpha), k_B=log2(1/beta), and L=mu log2(1/mu)>=0. Exact entropy grouping gives mu h2(lambda)=alpha k_A+beta k_B-L. Sections 1 and 2 imply

mu H(P_u)<=4E0+2mu h2(lambda).

Hence the COMPLETE joint row bill obeys

L+mu H(P_u)<=4E0+2(alpha k_A+beta k_B)-L
<=8E0-L<=8E0<=24E(u).

Both conditional and address entropy are included; no reserve is reset and no terminal is discarded. For equal masses and distinct directions the same proof gives rate16. A single cell gives rate4 by section1.

## 5. Parallel equal cells: affine cubic gluing

If V=W, the union A union B is the affine cell C=a0+span(V,b0-a0), of mass mu=2alpha. On C choose affine coordinate t distinguishing the two cells and coordinates z on V. The two signs have quadratic polynomials q0(z),q1(z). Their union sign is

q(t,z)=q0(z)+t(q0(z)+q1(z)),

of degree at most three. This also absorbs a minus sign on either component.

For ANY affine-cell cubic sign u on C, let U be its direction, k=codim U, and b the number of physical coordinate directions outside U. Each such coordinate has P_u(i in T)=1/2. Every other coordinate is tangent to U. Its derivative sign is a degree-at-most-two F2 polynomial. If the corresponding spectral inclusion p_i is nonzero, the elementary Reed-Muller minimum-weight induction gives p_i>=1/4: a nonzero degree-r polynomial has weight at least2^-r, by induction on the last essential variable (the two sections differ by a nonzero polynomial of degree at most r-1). Constant-one derivatives give p_i=1 and are covered as well.

Binary entropy satisfies h2(p)/p decreasing for p>0, since its derivative is log2(1-p)/p^2<0 for p<1. Thus h2(p_i)<=4h2(1/4)p_i<=4p_i for tangent directions. Subadditivity and k<=b now give

log2(1/mu)+H(P_u)<=k+b+sum_tangent h2(p_i)
<=2b+4sum_tangent p_i=4E(u)/mu.

No division by zero is made: mu>0; coordinates with p_i=0 contribute zero, and p_i=1 is treated by continuity or directly. This is a scoped use of A033's bounded phase-degree mechanism, not a claim that it pays arbitrary terminal phases.

## 6. Global ledger and stability

The physical cell partition gives |u_J|=1 on its row support and zero outside it. Thus w_J=mu(u_J), sum_J w_J=1, and Parseval gives I_Y(F)=sum_J E(u_J). The exact chain rule is

H(F)=sum_J [w_J log2(1/w_J)+w_J H(P_uJ)].

Apply the corresponding row estimate to each term. This proves the claimed full rate24, including H(S_Y|S_X); it is not merely an X marginal bound. Restricting a Y coordinate intersects each affine cell with a coordinate hyperplane and restricts its quadratic polynomial, so preserves the condition after empty cells are removed.

In the original distinct-label class, restricting one X bit groups labels J and J symmetric-difference{i}. Each resulting row is the signed sum of at most two old rows, with disjoint physical cells; row supports still partition Y. This proves the one-collision assertion on actual Boolean restrictions, at the same constant24 and with their actual physical influence. Further collisions may create four cells and are not covered here.

## 7. Tensor and vacuous-embedding guards

Suppose an admitted nonzero F equals G(X,Y) h(Z) for a fresh Boolean cube Z. Fix an X-frequency J and a physical y for which its G row is nonzero. The row value must have magnitude1 there, since admitted nonzero rows take values+-1. Restricting y leaves h(Z), up to sign, as at most two quadratic affine cells covering ALL of Z. If both cells are nonempty, their dyadic masses sum to1, forcing both to have mass1/2, and disjoint affine hyperplanes are parallel. Section5 shows h has F2 degree<=3. With one cell it has degree<=2. Conversely the quartic phase (-1)^(z1z2z3z4) has degree4 by uniqueness of the F2 multilinear representation and is excluded. This does not forbid every tensor, only arbitrary seeds as required.

The three-bit point defect is a cubic phase and is admitted: splitting on one physical bit gives a constant phase and a quadratic phase on complementary halfcubes. Its full H/I=16/3-(3/2)log2(3)<4. Its normalized spectrum has one squared mass9/16 and seven masses1/16, so is nonproduct. Thus the old constant-two conditional bound is not silently preserved, and vacuous one-coordinate embeddings are not used to infer a universal theorem. The normalized non-Boolean psi_N has H=log2 N and E=1; it violates24 at N>2^24. The proof uses affine-cell unit magnitudes, F2 phase degree, dyadic mass separation and exact physical translation geometry, which that generic vector lacks.

## Exact remaining line

No dimension-independent analogue is proved when a row contains an unbounded number of colliding cells. The coherent entropy inequality loses a factor equal to the number of components, and the geometric energy comparison can fail through simultaneous cancellations. The next unpaid step is one further physical X collision with the same inherited row components and full terminal spectra, paying its additional cross terms without renewing the constant or reserve. This statement gives an all-dimensional terminal after one collision; it is not a reusable local erasure charge or full FEI proof.
