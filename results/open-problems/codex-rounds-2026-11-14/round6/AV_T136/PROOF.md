# Finite-depth signed compression

## Independent recheck of the preceding scalar calculation

Under the regularity assumptions in round 5, write M=G_z, A=G_zz, B=G_zzz and P=A+cM^2. Along dζ=√k dW+ukM du the space-time generator gives DM=0, DA=−ukA² and D(M²)=kA². Thus DP=(c−u)kA², with stochastic coefficient √k(B+2cMA). For two copies sharing noise until v, the product drift contributes 2χ³k₀∫₀ᶜ(c−u)du=χ³k₀c²+O(c³), and the common quadratic variation contributes g²k₀²∫₀ᵛu du=g²k₀²v²/2+O(c³). Hence E[P_A P_B]=χ²+χ³k₀c²+g²k₀²v²/2+O(c³).

A second derivation conditions at the split. E[P_A]=χ+χ²k₀c²/2+O(c³), and E[P_A|ζ_v]=χ+(g/2)(ζ_v²−k₀v)+O_L²(c²). The independent-futures covariance is the variance of this conditional mean. Since Var(ζ_v²)=2k₀²v²+O(v³), the same coefficient g²k₀²/2 follows. At v=0 the formula is the square of the mean; at v=c it is the one-branch second moment.

For the sharper triple estimate, condition at the earlier split h. The conditional function E[(P_A−χ)M_C|ζ_h=z] is odd and has derivative bounded by C(c+z²)(1+|z|)^C. Multiplication by M(h,z)=O(z) and Eζ_h²=O(h), Eζ_h⁴=O(h²) gives O(ch+h²)=O(ch). The martingale identity for M_B M_C supplies χ³k₀h, including exact vanishing at h=0. The formal size weights of the five leading monomials are −4,−4,−3,−3,−2; adding 1−j/6 to their θ derivatives cancels each. These claims retain round 5's regularity and parameter-regularity assumptions.

## 1. Finite statement

Fix a finite hierarchy of positive masses
\[
 m_0=c,\quad m_1,\ldots,m_d=a.
\]
For physical hierarchies these are nondecreasing. Insert an empty step if necessary, so that \(c\) is a level and the future after \(c\) has the displayed levels. Terminal spins are scalar Ising spins. A common field source \(z\) couples linearly to the spin in the terminal Hamiltonian; its terminal continuation is \(a^{-1}\log\cosh(a z)\), with any later Gaussian field included in its argument. Future Gaussian transitions are the normalized positive transitions of the finite hierarchy. Denote the continuation at \(c\) by \(V_c(z)\), and put
\[
 R_k(z)=e^{-cV_c(z)}\partial_z^k e^{cV_c(z)},\qquad
 s_k(z)=R_k(z)/c\quad(k\ge1).
 \tag{1}
\]

Fix a finite skeleton below \(c\), with distinct cut blocks \(A=1,\ldots,D\). There are \(j\) labeled edges joining distinct blocks; multiple edges are allowed. Their \(2j\) endpoints are distinct slots, even if their eventual terminal labels coincide. All internal placements above \(c\) are summed, with no restriction on cross-edge coincidences. Keep the skeleton allocation coefficient, explicit edge weights, and any common projected pair tests outside this sum.

For a partition \(\pi\) of the \(j\) edges, let \(k_{A,P}\) count the endpoints of part \(P\) in block \(A\), and let
\[
 D_\pi=\sum_{P\in\pi}\#\{A:k_{A,P}>0\}.
\]
In a product of scalar moments, each part is evaluated on its own restricted topology, using a separate copy of its positive law. This is the convention in Section 2 of the limiting-law manuscript. In particular, coincident terminal labels belonging to different parts do not identify the random spin draws in the two expectations.

**Finite compression identity.** With these conventions, the internal signed sum of the ordinary scalar cumulant of the \(j\) pair variables is exactly
\[
 \sum_{\pi}(-1)^{|\pi|-1}(|\pi|-1)!\,
 c^{D_\pi}
 \prod_{P\in\pi}
 \mathbb E_{\mathrm{low},P}
       \prod_{A:k_{A,P}>0}s_{k_{A,P}}(\zeta_c^A).
 \tag{2}
\]
Here \(\mathbb E_{\mathrm{low},P}\) is the positive prefix law on the restriction of the fixed skeleton to the blocks used by \(P\). This proves the finite-depth version of (E5), for every finite \(j\). It asserts neither the continuous-path passage nor the estimates for the skeleton measure or the spin-model projection.

## 2. Marked finite trees and their coefficients

Let \(S\) be a nonempty finite set of slots, all in one cut block. An internal marked shape \(T\) consists of a partition of \(S\) into children at level 1, partitions of those child sets at level 2, and so on through level \(d\). A final child set is one terminal label, possibly containing several slots. Children are unordered; their disjoint slot sets distinguish them. A node \(B\) at level \(\ell<d\) has \(q_B\) occupied children. Define
\[
 W_m(T)=a^{|S|}
       \prod_{\ell=0}^{d-1}\ 
       \prod_{B\text{ at level }\ell}
       (m_\ell/m_{\ell+1})^{\underline{q_B}},
 \qquad
 p^{\underline q}=\prod_{i=0}^{q-1}(p-i).
 \tag{3}
\]
Restriction \(T|U\), for nonempty \(U\subseteq S\), intersects every node with \(U\) and removes empty nodes, retaining all mass levels and terminal coincidences.

The coefficient (3) is the labeled real-power source rule, without any integer-replica assumption. To see it, at a node write the child integral as \(I(z)\), its next mass as \(b\), and its incoming mass as \(v\). Its exponential continuation is \(I(z)^{v/b}\). For labeled derivatives \(D_S\),
\[
 D_S I^p=
 \sum_{\rho\in\mathcal P(S)}
 p^{\underline{|\rho|}}I^{p-|\rho|}
 \prod_{B\in\rho}D_B I,\qquad p=v/b.
 \tag{4}
\]
This identity follows by induction on \(|S|\). A new derivative either hits one existing \(D_B I\), enlarging that child set, or hits \(I^{p-q}\), creating a new child with coefficient \(p-q\). These are exactly the two ways to extend a partition; each final partition occurs once. There is no additional \(q!\).

Divide (4) by \(I^p\). Each factor \(D_B I/I\) is the normalized child integral with the indicated source derivatives. Apply the same argument recursively at every occupied child. At a terminal leaf, differentiating its spin integral \(k\) times produces \(a^k\) times the positive moment of the product of its \(k\) spin slots. Multiplying over terminal leaves gives \(a^{|S|}\); the nonterminal factors are the falling factorials in (3). The unused child integrals cancel in the normalized expression. Consequently
\[
 R_{|S|}(z)=
 \sum_T W_m(T)\,
       \mathbb E_{T,z}\prod_{s\in S}\tau_s.
 \tag{5}
\]
The sum is finite. The expectation is under the ordinary positive future law on that topology, conditional on the field at \(c\). Repeated slots at one terminal label are powers of the same spin in that one expectation.

For finite Gaussian clocks, all differentiations under the integrals are justified locally in \(z\): terminal spin factors are bounded, and their finitely many derivatives are bounded by constants times an exponential of a linear function of the Gaussian increments. Successive finite log-Laplace operations remain finite and smooth. Positive real powers are differentiated on strictly positive integrals. Thus (4)–(5) apply directly at physical real masses.

If \(d=0\), there is just one terminal node of mass \(a=c\). Formula (5) is the terminal derivative rule, with coefficient \(a^{|S|}\). This is also the starting case of the preceding induction.

## 3. Common-refinement identity, with cross-part coincidences

Partition \(S\) into nonempty colored sets \(S_1,\ldots,S_r\). For each color fix an internal marked shape \(T_i\) on \(S_i\). Then
\[
 \sum_{\substack{T\text{ on }S\\T|S_i=T_i\ (1\le i\le r)}}
       W_m(T)
       =\prod_{i=1}^r W_m(T_i).
 \tag{6}
\]
The sum includes common children and common terminal leaves across different colors.

Here is a coefficientwise proof. Set \(p_\ell=m_\ell/m_{\ell+1}\). First take each \(p_\ell\) to be a positive integer. There is a finite regular tree with \(p_\ell\) named children at each level-\(\ell\) node. The number of assignments of the slots \(S\) to its terminal leaves inducing exactly the marked shape \(T\) is
\[
 N_p(T)=\prod_{\ell,B}p_\ell^{\underline{q_B}}.
 \tag{7}
\]
Indeed the \(q_B\) children have distinct slot sets, and assigning those sets injectively to the \(p_\ell\) named children has precisely that falling-factorial count. The choices at distinct nodes multiply.

For each color independently, choose an assignment inducing \(T_i\). Combining these color assignments gives one assignment of \(S\). Distinct colors may choose the same named child or terminal leaf. Conversely, restricting a combined assignment to each color recovers that unique tuple of color assignments. This is a bijection, so
\[
 \sum_{T:T|S_i=T_i}N_p(T)=\prod_i N_p(T_i).
 \tag{8}
\]
Both sides of (8) are polynomials in the independent variables \(p_0,\ldots,p_{d-1}\). They agree on all positive-integer tuples, so they agree as polynomials. Explicitly, hold all but the first variable at positive integers and use the one-variable fact that a nonzero polynomial has finitely many roots; then repeat for each coefficient in the remaining variables. This proves equality at every real tuple. Multiplying by \(a^{|S|}=\prod_i a^{|S_i|}\) proves (6) for all positive masses.

Only the marked counting coefficients are continued in this argument. The positive scalar laws, their fields, and their dependence on masses are not continued from integer ratios. They are the real-mass laws in (5). One may equivalently attach independent formal symbols to every tuple of restricted shapes in (6); the identity holds for each symbol separately.

As a minimal nontrivial check, take a single step \(c\to a\) and two singleton colors. There are two common shapes. The coincident terminal shape has weight \(ca\), and the distinct-terminal shape has weight \(c(c-a)\). Their sum is \(c^2\), the product of the two one-slot weights. At physical \(0<c<a\), the distinct-terminal term is negative. Dropping the coincident shape would invalidate (6). For a depth with several levels, the same two-slot identity telescopes through all intermediate masses.

## 4. Application to a product of moments

Fix one edge partition \(\pi\). Each full internal placement induces a shape in every used cut block. Its scalar coefficient is a product of positive moments indexed by \(P\in\pi\). The moment for \(P\) depends only on the restriction to \(P\)'s endpoint slots. Unobserved branches disappear because their future transition kernels integrate to one.

The precise external skeleton normalization is as follows. With incoming root mass \(\rho>0\), let \(W_{\mathrm{cut}}\) be the allocation coefficient of the distinct \(D\) cut labels, with terminal mass \(c\). It has a terminal factor \(c^D\), times the falling factorials at nodes strictly below the cut. The coefficient of a full placement is therefore
\[
 W_{\mathrm{full}}
 =\frac{W_{\mathrm{cut}}}{c^D}
       \prod_{A=1}^D W_m(T_A).
 \tag{8a}
\]
This follows by splitting the product (3) into nodes below and above the cut; its terminal factor is \(a^{2j}\). Thus the external skeleton coefficient is exactly \(W_{\mathrm{cut}}/c^D\), as in the manuscript, rather than \(W_{\mathrm{cut}}\). This statement does not divide by \(W_{\mathrm{cut}}\), so zero falling-factorial coefficients cause no problem.

Expand the internal sum, grouping first by the tuple of restricted shapes seen by all parts. In each cut block apply (6), coloring the slots according to their parts. The total coefficient of each tuple is the product of the separate part coefficients. This is valid even when two parts use the same cut block, and even when terminal labels across parts coincide in a contributing full shape. No such coincidence is deleted or assigned a new spin expectation.

The internal sum therefore factors into one source sum for each part and each block used by that part. Conditional on its cut-prefix fields, distinct blocks have independent future transitions. Formula (5) gives \(R_{k_{A,P}}(\zeta_c^A)\) for the sum inside block \(A\). Integrating the conditional product under the prefix law of the restricted skeleton gives
\[
 \prod_{P\in\pi}
 \mathbb E_{\mathrm{low},P}
       \prod_{A:k_{A,P}>0}R_{k_{A,P}}(\zeta_c^A).
 \tag{9}
\]
Separate parts have separate expectations, as required by the original product-of-moments coefficient. Equation (9) does not replace a product of expectations by an expectation of a product under one shared prefix law.

Using \(R_k=cs_k\), equation (9) is
\[
 c^{D_\pi}
 \prod_{P\in\pi}
 \mathbb E_{\mathrm{low},P}
       \prod_{A:k_{A,P}>0}s_{k_{A,P}}(\zeta_c^A).
 \tag{10}
\]
Finally, at every fixed topology the ordinary joint cumulant is
\[
 \kappa(X_1,\ldots,X_j)=
 \sum_{\pi\in\mathcal P(\{1,\ldots,j\})}
 (-1)^{|\pi|-1}(|\pi|-1)!
 \prod_{P\in\pi}\mathbb E\prod_{e\in P}X_e.
 \tag{11}
\]
All sums are finite, so expand (11) before regrouping. Substitution of (10) proves (2).

The allocation below \(c\) remains the fixed skeleton coefficient throughout. With an auxiliary root mass \(\rho\), this coefficient depends only on the skeleton, not the internal placements. Thus the same identity holds after dividing that coefficient by \(\rho\) and taking its per-root limit, whenever that skeleton limit is defined. The internal identity introduces no additional root normalization.

## 5. Repeated edges and a shared cut block

For two separately labeled copies of \(AB\), the one-part term has endpoint multiplicities two in each block and \(D_\pi=2\). The two-part term uses each block twice and has \(D_\pi=4\). Equation (2) becomes
\[
 c^2\mathbb E_{\mathrm{low}}[s_2(\zeta_c^A)s_2(\zeta_c^B)]
 -c^4\bigl(\mathbb E_{\mathrm{low}}[s_1(\zeta_c^A)s_1(\zeta_c^B)]\bigr)^2.
 \tag{12}
\]
This is exactly the repeated-edge coefficient stated after (E5). It includes both terminal coincidences within each block and all distinct-terminal placements.

There is a direct numerical check with exact fractions. Set \(a=1,c=1/8\), no future field increments, and fixed terminal means \(\mu_A=1/3,\mu_B=2/5\). Elementary differentiation gives
\[
 R_1=c\mu,\qquad R_2=c(1-\mu^2)+c^2\mu^2.
\]
Thus \(R_{2,A}=65/576\), \(R_{2,B}=43/400\), and
\[
 R_{2,A}R_{2,B}-(R_{1,A}R_{1,B})^2
 =\frac{2795-1}{230400}=\frac{1397}{115200}.
 \tag{12a}
\]
Independently enumerate the four choices of coincident or distinct terminal labels in the two blocks. A coincident placement has weight \(c\), a distinct placement \(c(c-1)\). When both coincide the pair-variable covariance is \(1-\mu_A^2\mu_B^2\); when only \(A\) coincides it is \(\mu_B^2(1-\mu_A^2)\), and symmetrically for \(B\). When neither coincides it is zero. The weighted sum is
\[
 c^2(1-\mu_A^2\mu_B^2)
 +c^2(c-1)\{\mu_A^2+\mu_B^2-2\mu_A^2\mu_B^2\}
 =\frac{1397}{115200},
 \tag{12b}
\]
the same value without using the source derivative formula.

For \(AB,AC\), the one-part term is
\[
 c^3\mathbb E_{\mathrm{low}}[s_2(\zeta_c^A)s_1(\zeta_c^B)s_1(\zeta_c^C)],
 \tag{13}
\]
whereas the two-part term is
\[
 -c^4
 \mathbb E_{\mathrm{low},AB}[s_1(\zeta_c^A)s_1(\zeta_c^B)]\,
 \mathbb E_{\mathrm{low},AC}[s_1(\zeta_c^A)s_1(\zeta_c^C)].
 \tag{14}
\]
The cut block \(A\) is counted twice in (14), and its fields in the two expectations are separate draws on their respective restricted prefix trees. Treating them as one field would change the original scalar cumulant convention.

## 6. Limits of the conclusion

The finite identity holds at repeated masses, with zero Gaussian increments, with terminal coincidences, and at arbitrary finite degree. No parity assumption or low-cut expansion is needed for (2). The source derivative rule retains nonbinary forks and repeated terminal slots.

This does not prove uniform derivative bounds or convergence of signed allocations as the number of hierarchy levels grows. It also does not prove that the projected spin-model tests depend only on the skeleton, the skeleton density bound \(c^{-1}\prod dv_s/c\), or commutation with the physical clock derivative. Those are distinct analytic statements. Consequently the full coefficient estimate (E4), centered allocation estimate (E2)–(E3), stopped pressure increment, and SK limiting-law claim remain unchecked here.
