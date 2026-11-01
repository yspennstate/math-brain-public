# P0309 referee result: sharp absolute-relative-energy boundary

Date: 2026-10-10. Target status: unresolved; current openness UNKNOWN. This extends w534's finite-support simple-cubic instability from the range of finite raw energy, s>3, to the larger range s>2 where only relative energy is absolutely defined. It does not identify a crystalline Gibbs phase.

## Statement

Let v_s(r)=|r|^{-s} on R^3, s>0. For a finitely supported scalar field p:Z^3 -> R and sufficiently small a, define the **unordered relative pair energy**

    R_{s,p}(a)= (1/2) sum_{x != y in Z^3}
       [v_s(x-y+a(p_x-p_y)e_1)-v_s(x-y)].                 (1)

1. For every finite p and every s>2, (1) is absolutely convergent near a=0 and is twice differentiable there. Its first derivative at zero is zero. The threshold s>2 is sharp for this absolute-convergence assertion: for p_0=1 and p_x=0 otherwise, the sum of absolute pair differences diverges for every fixed nonzero |a|<1/4 whenever 0<s<=2.

2. For every s>2 there is a finite p such that R''_{s,p}(0)<0, hence arbitrarily small finite-support displacements lower the relative energy of Z^3. Thus force balance of Z^3 does not imply nonnegative displacement Hessian even for 2<s<=3, where the raw per-particle Riesz sum diverges. This is a relative-energy statement only.

## Proof of convergence and its sharp threshold

Only pairs touching supp(p) contribute. For |a| max|p_x-p_y| <=1/4 and |r|>=1, the mean-value theorem gives

    |v_s(r+a q e_1)-v_s(r)| <= C_s |a q| |r|^{-s-1}.      (2)

For a finite support, the number of far pairs in a shell of radius n is O(n^2), so (2) is summable exactly when s>2. The first derivative is dominated by the same series. The second derivative is dominated by C_s |r|^{-s-2}, summable for s>1. The near pairs are finite and remain separated. This proves absolute convergence and twice differentiability for s>2. Pairwise symmetry r <-> -r cancels the force at every lattice site, proving R'_{s,p}(0)=0.

For sharpness take p_0=1, all other p_x=0. Fix 0<|a|<1/4. In each dyadic annulus R<=|y|<2R choose the lattice box R<=y_1<=5R/4 and |y_2|,|y_3|<=R/8. It has at least cR^3 lattice points for large dyadic integer R, and y_1/|y|>=c'>0. The one-dimensional mean-value theorem along e_1 gives on this box

    ||y-a e_1|^{-s}-|y|^{-s}| >= c_s |a| R^{-s-1}.

Hence the sum of absolute differences on each such box is at least c_s'|a| R^{2-s}. The boxes at dyadic R are disjoint. Their contributions do not sum to a finite value when 0<s<=2 (constant per scale at s=2). This concerns absolute convergence; symmetric or neutralized regularizations are separate objects.

## Proof of negative finite-support curvature

Use w534's alternating-plane field. For Q_L={-L,...,L}^3 set p_x=1 if x in Q_L and x_3 is odd, and p_x=0 otherwise. Put h_s(r)=partial_1^2 |r|^{-s}. Differentiating the absolutely convergent relative energy gives

    K_L:=R''_{s,p}(0)
       = (1/2) sum_{r != 0} h_s(r) sum_x (p_{x+r}-p_x)^2.     (3)

Since |h_s(r)|<=C_s |r|^{-s-2}, the outer sum is absolutely convergent for s>1. For fixed r, the inner sum divided by |Q_L| tends to 1 if r_3 is odd and 0 otherwise. It is at most 2, because (u-v)^2<=u+v for binary u,v and the supports of p_x and p_{x+r} each have at most |Q_L| elements. Dominated convergence yields

    lim_{L->infinity} K_L/|Q_L| = (1/2) sum_{r_3 odd} h_s(r).  (4)

To determine the sign, define the absolutely convergent **relative** alternating-plane energy for s>2,

    Delta_s(a)=(1/2) sum_{r_3 odd} [|r+a e_1|^{-s}-|r|^{-s}]. (5)

The same mean-value bound gives absolute convergence of (5) for s>2, and the second derivative is the right side of (4). By the gamma integral and Fubini (the integrated absolute value of each Gaussian difference equals Gamma(s/2) times the absolute potential difference),

    Delta_s(a)= [2 Gamma(s/2)]^{-1} int_0^infinity
       t^{s/2-1} Theta(t,0) O(t) [Theta(t,a)-Theta(t,0)] dt, (6)

where Theta(t,a)=sum_m exp(-t(m+a)^2) and O(t)=sum_{n odd}exp(-t n^2). The Gaussian Fourier series is

    Theta(t,a)-Theta(t,0)=2 sqrt(pi/t) sum_{k>=1}
       exp(-pi^2 k^2/t)[cos(2 pi k a)-1].                (7)

All weights in (6) are positive. Differentiating (7) twice at a=0 makes the integral strictly negative: the k=1 term alone has negative curvature. Differentiation is justified by exponential decay exp(-pi^2/t) at t down to zero and by O(t)<=C exp(-t) at t up to infinity, with only polynomial factors from the Gaussian derivatives. Therefore Delta_s''(0)<0. Equations (4)-(5) imply K_L<0 for all sufficiently large finite L. Since R'_{s,p}(0)=0, Taylor's theorem gives R_{s,p}(a)<0 for all sufficiently small nonzero a.

The factor 1/2 in (3)-(6) counts unordered pairs once. The field has finite support for each L. The extension is a counterexample to the auxiliary force-balance-to-stability bridge; it neither selects BCC/FCC nor controls Gibbs free energy, defects or thermodynamic limits.

## Primary-source scope and gap

The campaign intake wording is in `brain_bundle_C006p02.json`, key `op-p0309`; Lewin's primary review, arXiv:2202.09240v2, Section VI, defines a finite-temperature solid as a periodic probability law and gives numerical phase diagrams for d=3. The exact s>3 Gibbs problem requires a symmetry-breaking DLR law at finite beta, not an exactly periodic point configuration. For s=1 it additionally requires a specified neutralizing background. The hardest original gap is a uniform nonlinear free-energy/order estimate for a stable candidate that survives defects and the infinite-volume limit. No formal checker or numerical proof is claimed here.

Independent referee requested: w539. Until that audit, this worker's extension is `proved special case` by its author, not `independently checked proof`.
