# The parent-alternative cap: conditional reduction and an interior envelope

The manuscript is OpenAI, *Pure-Point Spectrum for the Two-Dimensional Anderson Model at Every Positive Disorder*, September 23, 2026. This note concerns the finite hierarchy, not the infinite-volume localization conclusion.

The structural inputs are the geometry and sampling rules in [resonant.tex](https://raw.githubusercontent.com/openai/math/main/preprints/Pure-Point-Spectrum-for-the-Two-Dimensional-Anderson-Model-at-Every-Positive-Disorder-September-23-2026/build/sections/resonant.tex) and [hierarchy.tex](https://raw.githubusercontent.com/openai/math/main/preprints/Pure-Point-Spectrum-for-the-Two-Dimensional-Anderson-Model-at-Every-Positive-Disorder-September-23-2026/build/sections/hierarchy.tex). The boundary normalization is in [transmission.tex](https://raw.githubusercontent.com/openai/math/main/preprints/Pure-Point-Spectrum-for-the-Two-Dimensional-Anderson-Model-at-Every-Positive-Disorder-September-23-2026/build/sections/transmission.tex), trans:normalization. These are mutable main-branch sources opened November 15, 2026.

## 1. Statement and the remaining assumption

Fix the torus, the offset, an interior energy, the disorder width, and a permitted artificial-probe mask. Write
\[
 b_l=3^l,\quad L_l=(b_l-1)/2-b,\quad q_l=p_l=e^{-b_l^6}.
\]
For deterministic site data f and a parent tile D, set
\[
 h_D=\sup_{x,y\in D}|f(x)-f(y)|,\qquad
 B_l(f)=q_lp_l\,\mathbb E_{\rm off}\sum_{U:\,\operatorname{level}(U)=l}h_{D(U)}^2.
\]
Let Z_l(theta) be the expected oriented scattering energy from retained thinnable level-l roots to sources outside their immediate parents. The cell strengths are squared coupling coefficients; the artificial scale satisfies 0<=tau<=1 and the manuscript's stricter scale condition when the lower transmission bound is used.

**Conditional proposition.** Assume the branch transmission lower bound trans:lower: for the open parent root, each fixed passive exterior and each permitted set of corner boxes,
\[
 \mathbb E_{\rm branch}|S_{j,a_D}|^2
 \ge c e^{-C(\log L)^2}\,\mathbb E_{B,\rm branch}\rho,
 \qquad L=L_{l+1}.                                      \tag{1}
\]
Then the finite conditioning and sampling rules imply
\[
 Z_l(\theta)\le \theta K_l\mathbb E\mathcal Q_{\rm current}(f)
                    +C\theta B_l(f),\qquad 0\le\theta\le1. \tag{2}
\]
One can use
\[
 \log K_l\le 2b_{l+1}^6+C b_{l+1}^2                       \tag{3}
\]
for sufficiently large levels. Constants depend on the fixed cell parameters, not on the outer torus, the exterior matrix, or theta.

Below, (1) is an assumption throughout. The interior envelope and the side-law comparison needed to deduce (2) are derived explicitly. In particular, neither the lower transmission estimate nor its weighted good-boundary and jitter inputs are certified here.

## 2. Recheck of the preceding hidden-root result

Fix selectors, the necessary corner labels, all non-open-root true values z, and the accepted/rejected statuses. Integrate the numerical acceptance uniforms. For an accepted tile U, its likelihood has the factorization
\[
 \mathcal L_U(z,y)=\ell_U(z)(2h)k_U(y;z),\qquad
 \int k_U(y;z)\,dy=1.
\]
Here k_U is the prescribed root kernel. The original root density is 1/(2h). Thus acceptance contributes the joint density p_l ell_U(z) k_U(y;z). Disjoint eligible tiles give a product of these factors; rejected tiles contain no still-hidden root. Normalizing in all hidden values gives precisely the product of their k_U kernels.

Equivalently, for bounded tests b_U, integrating each uniform gives
\[
 \mathbb E\left[\prod_U b_U(v_{a_U})\,1_{\{\text{specified accepted tiles}\}}
                   \mid z,\text{labels,selectors}\right]
 =\prod_U p_{l(U)}\ell_U(z)\int b_U(y)k_U(y;z)\,dy,
\]
with any factors from disjoint rejected tiles canceling on normalization. This directly checks the same conditional law without treating acceptance status as information-free.

The references exclude their own roots, and eligible tiles are disjoint. The start response is therefore measurable without all these roots simultaneously. Independent thinning marks and revealing any already closed roots preserve each remaining kernel. A sign fixed from that start response stays measurable at every later closure. Numerical acceptance uniforms and recomputed signs are excluded. This confirms the preceding round's local result under the specified geometry.

## 3. A one-coordinate integral bound

Let a be a nonnegative continuously differentiable function satisfying
\[
 |a'(x)|^2\le A a(x),\qquad 0\le a(x)\le1.
\]
The functions 0 and 1 also qualify. Fix alpha real, beta>0, and tau>=0. Put
\[
 \gamma(x)=\beta+\tau a(x),\quad
 z(x)=x-\alpha-i\gamma(x),\quad
 m(x)=\operatorname{Im}\frac1{z(x)}
       =\frac{\gamma(x)}{(x-\alpha)^2+\gamma(x)^2}.
\]
Take the continuous argument phi=arg z in (-pi,0). Direct differentiation yields
\[
 \phi'(x)=m(x)-\frac{(x-\alpha)\gamma'(x)}{|z(x)|^2}.
\]
Young's inequality gives
\[
 \frac{|(x-\alpha)\gamma'|}{|z|^2}
 \le\frac12m+\frac{(\gamma')^2}{2\gamma}
                      \frac{(x-\alpha)^2}{|z|^2}
 \le\frac12m+\frac12A\tau.
\]
The last step uses (gamma')^2/gamma <= A tau; for tau=0 it holds directly. Hence
\[
 \phi'\ge\tfrac12m-\tfrac12 A\tau.
\]
On any interval I, the total endpoint change of phi is at most pi, regardless of its intermediate variation. Integrating proves
\[
 \int_I m(x)\,dx\le2\pi+A\tau |I|.                       \tag{4}
\]
The sign can also be checked through the logarithmic derivative: Im(z'/z)=(gamma-(x-alpha)gamma')/|z|^2. The numerical factor in the Young bound follows independently by expanding
\[
 (\sqrt\gamma-|x-\alpha|\,|\gamma'|/\sqrt\gamma)^2\ge0.
\]
If a is constant, direct integration gives a difference of arctangents, at most pi. Thus (4) is consistent with the exact constant-absorption case, including a narrow resonance at arbitrary alpha. No numerical quadrature near that resonance is needed.

For a finite complex-symmetric dissipative matrix whose true diagonal coordinates are independent uniforms on [-h,h], add -i epsilon I, epsilon>0. Conditional on every coordinate except v_i, its diagonal inverse entry is of the form 1/z(v_i). Indeed, Schur elimination of the other coordinates gives a passive scalar self-energy independent of v_i; its imaginary part contributes to beta>=epsilon. Formula (4), divided by 2h, gives
\[
 \mathbb E\operatorname{Im}G_{ii}\le \pi/h+A\tau=:C_h
\]
for every interior coordinate i. Summing n such coordinates and using Fatou as epsilon decreases to zero gives
\[
 \mathbb E\operatorname{tr}\operatorname{Im}G_{VV}\le C_h n. \tag{5}
\]
This bound is independent of the dimension and norm of the fixed passive exterior. All other coordinates can first be conditioned on; Tonelli applies to the nonnegative imaginary parts. The profile hypothesis on a is the manuscript's condition on vartheta, and holds for every allowed mask entry.

## 4. A mark-independent envelope

Hold the parent's boundary datum and exterior fixed. Let V be its interior, n=|V|, and P its projected boundary. Its coupling M:P->V has norm at most sqrt(3) and smallest singular value at least 1. In particular, it is injective. No cell port is on the parent's boundary.

For an arbitrary internal set A subset V, let E_A be coordinate inclusion. Allow references bounded by a fixed constant and strengths s_d in [s_*,1], s_*=exp(-C_0 L). They may depend on true potentials and auxiliary marks. Let G_A be this inverse. Form G_A' by restoring all references on A to their true values and setting their cell strengths to 1, without changing artificial probes. Then
\[
 (G_A')^{-1}=G_A^{-1}+E_A\Delta_AE_A^T,\qquad
 \|\Delta_A\|\le\Delta_*.
\]
The bound Delta_* depends only on the allowed diagonal ranges. Dissipativity gives
\[
 \|E_A^T G_A E_A\|\le s_*^{-1}.
\]
For example, the Ward identity bounds s_*||E_A^T G_A E_A u||^2 by Im(u^*E_A^T G_A E_Au), and Cauchy--Schwarz gives this compression bound.

Resolvent difference gives the exact identity
\[
 E_A^T G_A x
  =(I+E_A^T G_A E_A\Delta_A)E_A^T G_A'x.
\]
Thus, with the source input multiplier included in its boundary vector k-hat,
\[
 \sum_{d\in A}|S_{d,j}|^2
 \le C_L\|E_A^T(G_A')_{VP}\widehat k\|^2,
 \quad C_L=4(1+\Delta_*/s_*)^2.                            \tag{6}
\]
The factor 4 is from the scattering amplitude 2i times the two couplings. The inequality also uses s_d<=1.

Let
\[
 X_A=\|(G_A')_{VV}E_A\|_{\rm HS}^2.
\]
Unit absorption on A and Ward give X_A <= tr Im(G_A')_VV. Therefore (5) proves
\[
 \mathbb E_{V,\rm true}X_A\le C_h n.                       \tag{7}
\]
This replacement problem has only true real diagonals on V, so the independent-coordinate slicing used in (5) is applicable. It would not apply directly to the adaptive references of G_A.

Write H_V' for the V,V block of the replacement matrix, which has bounded operator norm. The V rows of its inverse identity give
\[
 M(G_A')_{PV}E_A=E_A-H_V'(G_A')_{VV}E_A.
\]
Injectivity of M with lower singular value 1 implies
\[
 \|(G_A')_{PV}E_A\|_{\rm HS}^2\le C(|A|+X_A).             \tag{8}
\]
Set
\[
 k_*=(\widehat T-iI_P)^{-1}\widehat k,\qquad \rho=\|k_*\|^2.
\]
The V,P block of G_A'(G_A')^{-1}=I gives
\[
 E_A^T(G_A')_{VP}\widehat k
 =-E_A^T(G_A')_{VV}Mk_*-iE_A^T(G_A')_{VP}k_*.
\]
Transpose symmetry and (8) bound its squared norm by
\[
 C\rho(|A|+X_A).                                        \tag{9}
\]
There is no bound on the norm of the exterior matrix or of k-hat in this estimate.

Define the envelope explicitly by
\[
 \mathfrak E(v_V)=C_L\sum_{A\subset V}
           \|E_A^T(G_A')_{VP}\widehat k\|^2.
\]
The empty term is zero. Each summand uses true potentials, the fixed mask, and fixed boundary/exterior data. It contains no internal selectors, acceptance uniforms, branch labels, or survival marks. Formula (6) proves domination simultaneously for every allowed adaptive choice. From (7)--(9),
\[
 \mathbb E_{V,\rm true}\mathfrak E
 \le C_L 2^n C C_h n\rho=:H_L\rho,
 \qquad \log H_L\le n\log2+C L+C\log(2+n).               \tag{10}
\]
Here n=(2L+1)^2-4, so log H_L <= C(1+L)^2. The count 2^n can also be obtained by summing binomial(n,r) over r; no factor from a continuum of reference choices occurs because (6) already bounds them all.

For null sets, first regularize every matrix strictly. For each fixed A, eliminate the fixed, generically invertible projected boundary block. The Hermitian real part of the resulting interior matrix is a fixed real symmetric matrix plus diag(v_V); its determinant is a polynomial with nonzero leading product. It is therefore invertible almost everywhere under the true product law. A kernel vector of a dissipative matrix is annihilated by both its Hermitian real and imaginary parts, so the replacement inverse exists almost everywhere as well. The artificial profiles need not be polynomial for this argument. A kernel vector in an original adaptive matrix vanishes on A by absorption. Replacing its diagonals and strengths therefore leaves it a kernel vector of the replacement. Thus existence of each replacement inverse implies existence for every original configuration on that set. Intersecting over the finitely many A gives one full-measure set before any adaptive choice. The inequalities pass to the unregularized matrices on this set; (5) uses Fatou. The boundary inverses are understood on their almost-everywhere set under the prescribed corner/side densities.

## 5. The boundary laws can be compared before integration

Fix actual corner values in their prescribed boxes, not just their labels. For any two allowed single-side vectors u,w, let
\[
 D_u=\mathcal T_u-iP,\quad D_w=\mathcal T_w-iP,\quad
 r_u=PD_u^{-1}k,\quad r_w=PD_w^{-1}k.
\]
Both matrices have -Im D >= P. Their difference is supported on the single-side subspace P_0 subset P, and
\[
 D_w-D_u=P\Delta P,\qquad \|\Delta\|\le2h+1=:K_B
\]
when tau<=1. This diagonal operator bound has no factor |B|. Resolvent difference and ||PD_w^{-1}P||<=1 give
\[
 \|r_w\|\le(1+K_B)\|r_u\|.
\]
Exchanging u,w gives the reverse bound. Consequently the two weights rho are within the squared factor (1+K_B)^2, pointwise for all such pairs. Integrating against any two probability laws on the side variables preserves this comparison; neither independence among the side coordinates nor a comparison of their densities is needed. Finally integrate the common corner law. Thus
\[
 \mathbb E_{B,\rm true}\rho
 \le(1+K_B)^2\mathbb E_{B,\rm branch}\rho.                 \tag{11}
\]
The zero-weight case is included by the two inequalities. Holding the corner values fixed is essential: changing a corner may act in a missing direction outside P and does not satisfy this resolvent argument.

## 6. Conditioning for a parent alternative

Fix an immediate parent D of side B=b_{l+1} within the current pass region. Freeze absence of selected strict ancestors, valid box identities of D and those ancestors, true potentials outside V_D union B_D, and the exterior auxiliary variables determining disjoint eligible tiles. Leave D's selector and all internal branch and survival choices unexposed. If the required ancestor event fails, no accepted child can contribute.

The relevant geometry can be checked directly for adjacent levels. Put b_l=s. Then L_{l+1}=s+L_l. The positive parent triple
\[
 (L_{l+1}+1,L_{l+1}-1),\quad
 (L_{l+1}-1,L_{l+1}+1),\quad (L_{l+1},L_{l+1})
\]
is the positive-corner triple of the extreme child centered at (s,s), translated by that center. Reflections handle the other corners. Once s>2b+3, each triple lies entirely inside that extreme child tile. Repeating down the hierarchy shows that an ancestor triple meeting a descendant tile is exactly its own corner triple. Also each child's V is contained in the parent's V. A child point outside the parent's square can only have one coordinate of modulus L_{l+1}+1 and the other of modulus at most L_{l+1}-1, which is on the parent's B; the clipped corner is on B as well. Thus child V union B is contained in parent V union B. Every immediate child center lies in the parent's V, and induction gives the same for all descendant centers.

The nested corner geometry therefore ensures that an exposed ancestor triple meeting D is one of D's own triples. A label needed by a disjoint exterior eligible tile either has no intersection with D or is this same already exposed label. Hence it creates no additional condition on V_D or on its single-side coordinates. Repeated labels are identical labels, not successive refinements. The remaining true law is independent uniforms on V_D and on the sides, with the four corner triples uniform in their fixed boxes. Fixed values in D outside V_D union B_D impose no further condition because those sites are disjoint from these triples.

Changing D's selector changes eligibility only inside D. Exterior active roots, references, restored values, and source inputs remain fixed. Their allowance tests can involve a corner of D only through the labels already exposed. Consequently eliminating the exterior gives the same passive boundary matrix and source vector in both alternatives. This conditioning does not retain any finer internal labels, acceptance statuses, or the signed adaptive datum of the preceding round.

Each immediate child has exactly one fresh Bernoulli-theta mark, assigned even when it is not accepted. There are 3^2=9 children. Any thinnable survivor in D requires at least one successful mark. The event J has probability
\[
 \mathbb P(J)=1-(1-\theta)^9\le9\theta.                    \tag{12}
\]
The same inequality follows from the sum of the nine individual success probabilities; no small-theta asymptotic is being used. The envelope in (10) is independent of these marks. Dropping internal eligibility/acceptance restrictions only enlarges a nonnegative upper bound. Therefore, conditionally on the frozen parent data,
\[
 \mathbb E\sum_{a\in\mathcal S_D}|S_{j,a}|^2
 \le9\theta H_L\,\mathbb E_{B,\rm true}\rho.              \tag{13}
\]
There is no factor 1/theta here and no conditioning on J before integrating the potentials.

In the other alternative, D is selected and accepted. Its conditional probability is exactly q_{l+1}p_{l+1}: the selector is independent, and integrating the likelihood and its acceptance uniform gives probability p_{l+1}, with the branch law conditional on acceptance. D is eligible and allowed under the frozen event. At level l it has not yet been thinned. In a second pass, D was untouched by the first pass, because both regions are unions of level-m tiles and l+1<=m. Thus this is part of the same current ensemble.

Applying assumption (1) gives
\[
 \mathbb E[1_{\{a_D\ {\mathrm{active}}\}}|S_{j,a_D}|^2]
 \ge c q_{l+1}p_{l+1}e^{-C(\log L)^2}
                                \mathbb E_{B,\rm branch}\rho. \tag{14}
\]
Combining (11), (13), and (14) proves the conditional transfer with coefficient theta times
\[
 K_l'\le C H_L e^{C(\log L)^2}(q_{l+1}p_{l+1})^{-1}.
\]
Since q_{l+1}=p_{l+1}=e^{-B^6}, its logarithm costs 2B^6. Independently, the product probability is e^{-B^6-B^6}=e^{-2B^6}. Formula (10) and L<B/2 give log K_l' <=2B^6+C B^2. Constants from the following final summation can be absorbed into that same bound.

## 7. From transfer to the energy cap

For a child root a in D,
\[
 |f_j-f_a|^2\le2|f_j-f(c_D)|^2+2h_D^2.
\]
The error term summed over j outside D is at most 2h_D^2 for each retained root, by unit scattering column mass. Its expectation is at most 2theta q_l p_l h_D^2 for each child, using acceptance incidence and independent survival. Summing gives at most 2theta B_l(f).

Apply the conditional transfer to the first term. f is deterministic after fixing geometry, so multiplication by |f_j-f(c_D)|^2 and conditional integration are permitted. For an active parent, f(c_D) is its port datum. Each parent is counted once at this level. Thus the oriented parent-to-exterior sum is bounded by the full sum of nonnegative ordered port pairs,
\[
 \sum_D\sum_{j\notin D}1_{\{a_D\ {\mathrm{active}}\}}
      |S_{j,a_D}|^2|f_j-f(c_D)|^2\le2\mathcal Q_{\rm current}(f).
\]
The factor 2 is also immediate from the definition Q=(1/2) times that ordered sum. Including the preceding factor 2 and enlarging K_l proves (2)--(3). At theta=0 there are no thinnable survivors, so the endpoint holds directly.

## 8. Missing cases and scope

Shared corners were fixed by their actual common labels before either alternative, then integrated with the same corner law. Correlated side draws were handled pointwise in (11). All internal subsets, including empty subsets and multiple surviving children, were included in the finite envelope. Its coefficients do not depend on survival marks. References can vary continuously because the replacement bound is uniform. Regularization and the finite-subset null-set argument precede adaptive choices. No independence after a branch tilt, or exterior norm bound, was assumed.

The local conclusion is conditional on (1). The transmitted lower bound, its profile/jitter estimates and weighted boundary good event, the subsequent thinning integration, screening, and the infinite-volume readout remain outside this result. No conclusion about general potential laws or exponential eigenfunction decay follows from this cap calculation.
