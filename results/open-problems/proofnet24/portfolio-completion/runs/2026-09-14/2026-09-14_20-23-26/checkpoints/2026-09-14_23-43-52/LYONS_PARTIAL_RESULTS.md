# Verified restricted cases of determinantal entropy concavity

Research note, 14 September 2026. The general conjecture remains unresolved in this run. The results below are session derivations with proofs and recorded audits; historical novelty is not established.

For a complex Hermitian positive contraction \(0\le K\le I\) on a finite coordinate set \(E\), let \(P_K\) be the determinantal law characterized by
\[
P_K(S\subseteq X)=\det K_S,
\]
and let \(H(K)\) be its Shannon entropy, using natural logarithms. [Lyons's Conjecture 2.6](https://arxiv.org/pdf/1406.2707) asks whether \(H\) is concave on the whole contraction set. [Gu's rank-one result](https://sevenkplus.com/data/dpp.pdf) is established prior work.

The following statements have complete proofs in this packet:

1. Full concavity for two sites, with the sharp interior bound \(D^2H(K)[D,D]\le-8\det D\) when \(\det D>0\).
2. In any dimension, concavity when the varying entries lie in a fixed two-coordinate principal block and all other entries remain fixed.
3. In any dimension, concavity when the principal block complementary to one coordinate remains fixed; its incident row and column may vary together.
4. Through dimension five, concavity along every direction with at most one positive and at most one negative eigenvalue.
5. In any dimension, every fixed nonzero Hermitian line through an interior diagonal kernel is strictly concave on a sufficiently small interval around that kernel. This is a local statement along each fixed line.
6. In any dimension, joint concavity when a two-coordinate principal block varies freely and its entire cross matrix is a fixed matrix multiplied by one complex scalar, with a strict mutual-information chord bound whenever that scalar changes.

These are different restrictions. None allows arbitrary sums of its permitted directions without a separate control of mixed Hessian terms. In particular, the fourth statement does not include positive semidefinite directions of rank two.

## 1. Two sites: the full theorem

Write
\[
K=\begin{pmatrix}a&c\\\bar c&b\end{pmatrix},\qquad
D=\begin{pmatrix}u&v\\\bar v&s\end{pmatrix},\qquad 0<K<I.
\]
The exact atom probabilities are
\[
x=(1-a)(1-b)-|c|^2,\quad y=a(1-b)+|c|^2,\quad
z=(1-a)b+|c|^2,\quad w=ab-|c|^2.
\]
They are positive, sum to one, and satisfy \(yz-xw=|c|^2\). With \(\delta=\det D\), direct differentiation along \(K+tD\) gives
\[
(x'',y'',z'',w'')=2\delta(1,-1,-1,1),
\]
and hence
\[
H''=-\mathcal I+2\delta L,\qquad
\mathcal I=\sum_{p\in\{x,y,z,w\}}\frac{(p')^2}{p},\qquad
L=\log\frac{yz}{xw}\ge0.
\tag{1}
\]
This already proves \(H''\le0\) when \(\delta\le0\).

If \(\delta>0\), the direction is definite. Negation preserves its second variation, so take \(D>0\). Set
\[
A=\frac{\operatorname{adj}K}{\sqrt w},\qquad
B=\frac{\operatorname{adj}(I-K)}{\sqrt x},\qquad
T=\frac{y+z}{2\sqrt{xw}}\ge1.
\]
Both \(A,B\) are positive definite of determinant one. The two extreme Fisher terms alone give
\[
\begin{aligned}
\mathcal I
&\ge (\operatorname{tr}AD)^2+(\operatorname{tr}BD)^2\\
&\ge\tfrac12[\operatorname{tr}(A+B)D]^2
\ge2\det(A+B)\det D.
\end{aligned}
\tag{2}
\]
The last step applies arithmetic-geometric mean to the two eigenvalues of \((A+B)^{1/2}D(A+B)^{1/2}\), and needs no commutativity. The two-dimensional determinant identity yields
\[
\det(A+B)=2+\frac{y+z}{\sqrt{xw}}=2+2T.
\]
Also \(L\le2\log T\). Substituting into (1),
\[
H''\le-4\delta(1+T-\log T)\le-8\delta.
\tag{3}
\]
Equality is attained at \(K=I_2/2,D=I_2\); the coefficient eight is sharp. The exact minimum of the two extreme Fisher terms over \(D>0,\det D=1\) is \(2\det(A+B)\), attained at \(D=\sqrt{\det(A+B)}(A+B)^{-1}\). No minimum of the full four-atom Fisher expression is asserted by this calculation.

Integrating the nonpositive Hessian proves concavity on strict segments. For closed contractions, use \(K_j^\epsilon=(1-2\epsilon)K_j+\epsilon I\) and pass to the limit. Each atom is polynomial in the entries, and \(-p\log p\) is continuous at zero. When \(\det(K_1-K_0)>0\), (3) also gives
\[
H((1-t)K_0+tK_1)\ge(1-t)H(K_0)+tH(K_1)
  +4\det(K_1-K_0)t(1-t).
\tag{4}
\]

The complete derivation and independent audit, including equality and complex phases, are in [agent016](agents/016.md) and [agent018](agents/018.md).

## 2. A fixed two-coordinate block in any dimension

Write the kernel in blocks for \(E=U\sqcup O\), where \(|U|=2\), and suppose only \(K_{UU}\) varies. For an outside atom \(Y\subseteq O\), put
\[
Q_Y=K_{OO}-I_{O\setminus Y},\qquad
q_Y=(-1)^{|O\setminus Y|}\det Q_Y.
\]
The numbers \(q_Y\) are the fixed outside probabilities. If \(q_Y>0\), the conditional law on \(U\) is determinantal with kernel
\[
C_Y=K_{UU}-K_{UO}Q_Y^{-1}K_{OU}.
\tag{5}
\]
Indeed inclusion-exclusion in the absent outside coordinates, followed by the Schur complement, gives
\[
P(W\subseteq X,\ X\cap O=Y)=q_Y\det(C_Y)_{WW},\qquad W\subseteq U.
\]
The conditional kernel is a positive contraction: this follows by conditioning on included outside coordinates first, using a positive Schur complement, then excluding the others by the complementary Schur complement. Continuity covers boundary kernels with \(q_Y>0\); zero-weight atoms are omitted.

For \(K_{UU}(t)=K_{UU}(0)+td\), formula (5) gives \(C_Y(t)=C_Y(0)+td\) with the same direction in every conditional law. The entropy chain rule is
\[
H(K(t))=H((q_Y)_Y)+\sum_{Y:q_Y>0}q_YH(C_Y(t)).
\]
The first term and weights are fixed. The two-site theorem proves concavity, including boundary segments. If \(\det d>0\), the chord improvement is \(4\det d\,t(1-t)\), since the weights sum to one. Agent018 gives the full conditional-kernel derivation.

## 3. Fixing the complementary block of one coordinate

For a real set function \(f\), let \(\widehat f\) denote its Boolean Möbius coefficients. Its determinantal expectation is the polynomial
\[
F_f(K)=\mathbb E_K f(X)=\sum_{S\subseteq E}\widehat f(S)\det K_S.
\tag{6}
\]
Choose an original coordinate \(i\), write \(R=E\setminus\{i\}\), and set
\[
K=\begin{pmatrix}a&b^*\\b&C\end{pmatrix},\quad
f_0(T)=f(T),\quad g(T)=f(T\cup\{i\})-f(T).
\]
Bordered determinants in (6) give the exact identity
\[
F_f(K)=F_{f_0}(C)+aF_g(C)-b^*Q_g(C)b,
\quad Q_g(C)=\nabla F_g(C).
\tag{7}
\]
The gradient is with respect to the real trace pairing on Hermitian matrices. If \(g\) is increasing, then \(Q_g(C)\ge0\) for \(0<C<I\). This follows from the established determinantal stochastic-domination theorem: increasing a positive-contraction kernel in Loewner order increases the expectation of every increasing set function. Applying it to \(C+sww^*\) and differentiating gives \(w^*Q_g(C)w\ge0\). This input is [Lyons's Theorem 2.9](https://arxiv.org/pdf/1406.2707).

At an interior base kernel freeze \(f(S)=-\log p_S(K)\), where \(p_S\) are exact atom probabilities. This function is supermodular. To check it, put \(L=K(I-K)^{-1}>0\), so \(p_S=\det(I-K)\det L_S\); the two-by-two Schur complement gives
\[
p_{T\cup\{i\}}p_{T\cup\{j\}}\ge p_Tp_{T\cup\{i,j\}}.
\]
Thus \(g=\Delta_i f\) is increasing. Along a direction
\[
D=\begin{pmatrix}\alpha&v^*\\v&0\end{pmatrix},
\]
with \(C\) fixed, differentiating (7) twice yields \(D^2F_f(K)[D,D]=-2v^*Q_g(C)v\). The entropy Hessian is therefore
\[
D^2H(K)[D,D]
=-\sum_S\frac{(Dp_S[D])^2}{p_S}-2v^*Q_g(C)v\le0.
\tag{8}
\]
The table \(f\) is frozen during this auxiliary differentiation. Integration and the same common regularization prove the stated slice concavity on the closed contraction set. [Agent010](agents/010.md) contains the derivation; [agent017](agents/017.md) independently reconstructs it both by Möbius expansion and conditional binary entropy.

## 4. Arbitrarily oriented indefinite rank-two directions through dimension five

For supermodular \(f\), define
\[
q_f(K;u,v)=D^2F_f(K)[uu^*,vv^*].
\]
We show \(q_f\ge0\) when \(|E|\le5\). Dependent vectors give zero; otherwise orthonormalizing their plane scales \(q_f\) by the nonnegative Gram determinant. Hence take \(u,v\) orthonormal and put \(U=\operatorname{span}(u,v)\), \(R=P_{U^\perp}\).

The mixed coefficient of each principal determinant depends only on the compression of \(K\) orthogonal to the restricted vectors \(u_S,v_S\). Extending such perpendicular vectors by zero puts them in \(U^\perp\). Thus
\[
q_f(K;u,v)=q_f(RKR;u,v).
\tag{9}
\]
Diagonalize this compression as \(\sum_{j=1}^{n-2}\lambda_jw_jw_j^*\). Separate affinity in the \(\lambda_j\) expresses (9) as a convex combination of values at projections onto spans of subsets of the \(w_j\).

For a rank-zero compressed projection, (6) gives
\[
q_f(0;u,v)=\mathbb E_{Y\sim P_U}\widehat f(Y)\ge0,
\]
because \(|Y|=2\) and \(\widehat f(\{i,j\})=\Delta_i\Delta_jf(\varnothing)\). For a rank-one projection onto a unit vector \(w\perp U\), Cauchy-Binet gives
\[
q_f(ww^*;u,v)
=\mathbb E_{Y\sim P_U}\widehat f(Y)
 +\mathbb E_{Z\sim P_{U\oplus[w]}}\widehat f(Z).
\tag{10}
\]
Established stochastic domination for nested projection subspaces couples \(Y\subset Z\). Their sizes are two and three. Writing \(Y=\{i,j\},Z=\{i,j,k\}\), their coupled sum of coefficients is
\[
\widehat f(ij)+\widehat f(ijk)=\Delta_i\Delta_jf(\{k\})\ge0.
\]
This proves (10) nonnegative in every ambient dimension.

Complementation sends \(f\) to the supermodular function \(f^c(S)=f(E\setminus S)\) and gives \(F_f(K)=F_{f^c}(I-K)\). The two derivative signs cancel. By (9), a compressed projection of rank \(r\) may therefore be replaced by one of rank \(n-2-r\). For \(n\le5\), every projection term reduces to rank zero or one. Hence \(q_f\ge0\).

Finally freeze the supermodular \(f=-\log p_K\) as before. For \(D=\lambda uu^*-\mu vv^*\), with \(\lambda,\mu\ge0\), pure rank-one second derivatives vanish and
\[
D^2H(K)[D,D]
=-\sum_S\frac{(Dp_S[D])^2}{p_S}-2\lambda\mu q_f(K;u,v)\le0.
\]
Integration and common regularization prove the finite-segment claim, including the boundary. [Agent019](agents/019.md) gives the full compression proof, exact rational identity checks, and the unresolved higher-dimensional obligation.

## 5. Exact quartic loss at an interior diagonal kernel

Let \(D=\operatorname{diag}(p_i)\), with \(0<p_i<1\), and let \(A\ne0\) be a Hermitian matrix with zero diagonal. Put \(v_i=p_i(1-p_i)\) and \(h(p)=-p\log p-(1-p)\log(1-p)\). Then
\[
H(D+tA)=\sum_i h(p_i)
-\frac{t^4}{2}\sum_{i<j}\frac{|A_{ij}|^4}{v_iv_j}+O(t^6).
\tag{11}
\]
This implies strict concavity on a sufficiently short interval along this fixed line, even though its second derivative at zero vanishes.

Here is the full argument for the leading term. Let \(\mu=\bigotimes_i\operatorname{Bernoulli}(p_i)\), and define the centered contrasts \(z_i=(X_i-p_i)/v_i\), \(z_J=\prod_{i\in J}z_i\). The mixed-column determinant formula gives the exact density polynomial
\[
\frac{P_{D+tA}(X)}{\mu(X)}
=1+\sum_{\varnothing\ne J}t^{|J|}\det(A_J)z_J=:1+u_t.
\]
The zero diagonal eliminates its singleton terms. Product independence gives \(\mathbb E_\mu z_Jz_L=0\) for \(J\ne L\), and \(\mathbb E_\mu z_J^2=\prod_{i\in J}v_i^{-1}\). The marginals are unchanged, so the cross-entropy against \(\mu\) is constant and
\[
H(D+tA)=H(D)-\mathbb E_\mu[(1+u_t)\log(1+u_t)].
\]
There are finitely many positive atoms near zero, so this expression is analytic. Write \(u_t=t^2F_2+t^3F_3+\cdots\), with
\[
F_2=-\sum_{i<j}|A_{ij}|^2z_iz_j.
\]
The expansion \((1+u)\log(1+u)=u+u^2/2-u^3/6+\cdots\), normalization \(\mathbb E u_t=0\), and orthogonality give
\[
\mathbb E[(1+u_t)\log(1+u_t)]
=\frac{t^4}{2}\mathbb E F_2^2+O(t^6)
=\frac{t^4}{2}\sum_{i<j}\frac{|A_{ij}|^4}{v_iv_j}+O(t^6).
\]
The fifth coefficient vanishes because \(\mathbb E F_2F_3=0\); every cubic power of \(u_t\) has order at least six. This proves (11). The coefficient sum is strictly positive, and analytic differentiation gives \(H''(t)=-6t^2\sum_{i<j}|A_{ij}|^4/(v_iv_j)+O(t^4)<0\) for sufficiently small nonzero \(t\). Integrating the derivative proves strict concavity across zero as well.

For a general Hermitian direction with a nonzero diagonal entry, the same density calculation instead yields \(H''(0)=-\sum_i A_{ii}^2/v_i<0\), so local strict concavity follows by continuity. Thus every fixed nonzero Hermitian line is covered. [Agent023](agents/023.md) contains the all-order formula, independently checked finite polynomial identities, and examples showing that later coefficients need not all be negative or even. The parent independently checked the product-contrast proof. This controls the derivative along the line from \(D\); it does not prove concavity for every independent direction at every nearby kernel.

## 6. A scaled cross matrix in any dimension

Fix two actual point coordinates \(U\), their complement \(O\), a Hermitian outside contraction \(C\), and an arbitrary complex \(2\times|O|\) matrix \(B\). Then
\[
\mathcal H(A,z)=H(P_{K(A,z)}),\qquad
K(A,z)=\begin{pmatrix}A&zB\\\bar zB^*&C\end{pmatrix}
\tag{12}
\]
is jointly concave on the closed convex domain where \(A=A^*\), \(z\in\mathbb C\), and \(0\le K(A,z)\le I\). The entire cross matrix shares one scalar; its entries cannot vary independently.

Here is a finite-chord proof, including a quantitative strictness statement. Initially assume the endpoint kernels are strict contractions. For an outside atom \(Y\subset O\), put
\[
Q_Y=C-P_{O\setminus Y},\quad
q_Y=(-1)^{|O\setminus Y|}\det Q_Y>0,\quad
D_Y=BQ_Y^{-1}B^*.
\]
The \(q_Y\) are the fixed outside probabilities. Inclusion-exclusion on absent outside sites and a Schur complement give the conditional inside kernel
\[
M_Y(A,z)=A-|z|^2D_Y.
\tag{13}
\]
Each is a strict contraction. Indeed, conditioning first on included sites gives a positive Schur complement \(T\) with \(T\le K<I\). Conditioning next on excluded sites gives
\(T_{UU}+T_{UZ}(I-T_{ZZ})^{-1}T_{ZU}\); its complement is a Schur complement of \(I-T>0\). This also proves the assertion for empty included or excluded sets. No fixed sign of \(D_Y\) is assumed.

For \(s\ge0\), the full kernel \(K(A,\sqrt{s})\) is strict exactly when
\[
A-sBC^{-1}B^*>0,\qquad
I-A-sB(I-C)^{-1}B^*>0.
\tag{14}
\]
Hence the feasible \((A,s)\) domain is convex, and at fixed \(A\) it contains the interval from zero to any feasible \(s\). By the two-site theorem, the function
\[
F_A(s)=\sum_Yq_YH_2(A-sD_Y)
\]
is concave in \(s\) on that interval. The chain rule gives
\(\mathcal H(A,z)=H(P_C)+F_A(|z|^2)\), and \(F_A(0)=H_2(A)\).

For endpoints \((A_j,z_j)\) and \(0<t<1\), set
\[
\begin{aligned}
A_t&=(1-t)A_0+tA_1,&z_t&=(1-t)z_0+tz_1,\\
\bar s&=(1-t)|z_0|^2+t|z_1|^2,&
\Delta&=t(1-t)|z_1-z_0|^2.
\end{aligned}
\]
Equation (14) proves feasibility of \(\bar K=K(A_t,\sqrt{\bar s})\). Its conditional kernels are convex combinations of the endpoint conditional kernels. The two-site theorem therefore gives
\[
H(P_{\bar K})\ge(1-t)\mathcal H(A_0,z_0)+t\mathcal H(A_1,z_1).
\tag{15}
\]
If \(\bar s>0\), write \(\alpha=\Delta/\bar s\in[0,1]\). Since \(|z_t|^2=(1-\alpha)\bar s\), concavity of \(F_{A_t}\) between zero and \(\bar s\) gives
\[
F_{A_t}(|z_t|^2)-F_{A_t}(\bar s)
\ge\alpha\,[H_2(A_t)-F_{A_t}(\bar s)]
=\alpha I_{P_{\bar K}}(X\cap U;X\cap O).
\]
Combining this with (15) proves
\[
\mathcal H(A_t,z_t)-(1-t)\mathcal H(A_0,z_0)-t\mathcal H(A_1,z_1)
\ge\frac{\Delta}{\bar s}I_{P_{\bar K}}(X\cap U;X\cap O)\ge0.
\tag{16}
\]
If \(\bar s=0\), both scalars vanish, so ordinary two-site concavity applies.

For closed endpoints, replace every kernel by \((1-2\varepsilon)K+\varepsilon I\). This keeps one fixed outside block and one fixed cross matrix, with scalars multiplied by \(1-2\varepsilon\). The ratio \(\Delta/\bar s\) is unchanged, and the auxiliary kernel is regularized in the same way. Letting \(\varepsilon\downarrow0\) proves its feasibility and (16) by continuity of finite-law entropy and mutual information. Inverses are used only in the strict proof.

If \(B\ne0\) and \(z_0\ne z_1\), some cross entry satisfies
\[
\operatorname{Cov}_{P_{\bar K}}(\mathbf1_{i\in X},\mathbf1_{j\in X})
=-\bar s|B_{ij}|^2<0.
\]
The two subsets are dependent, so their mutual information is positive. Thus every interior point of the chord has strict entropy inequality, including for boundary endpoints. The argument was developed by coordinator011 from agent036's three-site case; [agent045](agents/045.md) independently audited the all-dimensional proof, supplied (16), and checked the exact conditional identities on a genuinely complex five-site example. The parent independently reviewed that full report. The same proof lifts any proved \(k\)-site concavity theorem to a \(k\)-coordinate block, but only \(k=2\) is used unconditionally here.

## What the proofs do not establish

The general Lyons conjecture is unresolved here, including unrestricted directions in dimensions three and above. The supermodular mixed-derivative lemma above first leaves an unresolved compressed rank-two projection case in dimension six. The bounded numerical search in `computations/dpp_supermodular_projection_search.py` found no counterexample among its 100 sampled real configurations; this is not a proof of that lemma. Positivity on decomposable exterior two-vectors also does not establish positivity of the full exterior-square operator.

Arbitrary unitary rotation is not a symmetry of the entropy problem. For example, \(\operatorname{diag}(1,0)\) has entropy zero, while the unitarily conjugate projection with every entry \(1/2\) has entropy \(\log2\). Coordinate restrictions above cannot be removed by rotating the kernel.

No theorem in this note is claimed to have been formally checked in Lean, externally refereed, or cleared for worldwide priority. Exact proofs, audit disagreements and their resolutions, and current source limitations are preserved in the accompanying reports and final claim ledger.
