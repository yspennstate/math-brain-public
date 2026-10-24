# FEI: directional compression and a shared-control obstruction

Research continuation for Yitzchak Shmalo — 20 September 2026.

**Status: the unrestricted Friedgut–Kalai Fourier entropy–influence conjecture remains unproved in this work.** This report gives a self-contained directional restriction theorem, its robust version, a normal form, and an explicit counterexample to a proposed shared-control gluing inequality. The finite checker was executed. No independent review, proof-assistant formalization, or publication-priority clearance is claimed.

## 1. What the current project has established, and what is being added

The current P03 entrypoint explicitly records full FEI as open. Its positive quadratic-symmetry continuation treats

\[
F(x)=(-1)^{Q(x)}\prod_{t=1}^m h_t(x_{U_t}),
\]

where the physical coordinate groups \(U_t\) are disjoint, \(Q\) is arbitrary quadratic, and each \(h_t\) is \(d_t\)-part-symmetric. Its conclusion is

\[
H(F)\le (12.04+\log_2 d_*)J(F),\qquad d_* =\max_t d_t.
\]

The number of factors does not enter the constant. The value 12.04 is supplied by the published O'Donnell–Wright–Zhou symmetric-function theorem, not by this project. Overlapping arbitrary high-degree cores and arbitrary affine input mixing are not covered by that result.

The subsequent P03 reports establish a certificate-based max-splicing theorem for quadratically coupled disjoint cores, and exact zero-cost splitting when two children have equal squared Fourier spectra. In particular, signed translation symmetries can be eliminated by physical coordinate restrictions at zero Fourier-entropy cost. The companion NM13-02 report supplies a derivative-spectral-flat selector and a restricted connected high-degree family, with direct constant

\[
\kappa_2=8-3\log_2 3+\frac{2}{\ln 2}=6.130502579614458\ldots.
\]

All these reports retain restrictions on their hypotheses. Their constants are not bounds for all Boolean functions.

The present additions are:

* A nonconstant low-degree approximation to a derivative in **any input direction** forces a quantitatively influential **physical coordinate**, which need not be the original direction.
* An approximately constant directional derivative gives an explicit small-entropy-cost physical split. The exact case recovers, rather than replaces, the existing signed-symmetry quotient theorem.
* The directions whose derivatives have degree at most \(d\) form a linear subspace. Its dimension can be removed by a paid physical restriction tree, with constant independent of that dimension.
* For \(d=2\), a minimal-dimensional counterexample to any candidate FEI constant \(C\ge\kappa_2\) must have no nonzero quadratic-derivative direction. A normal form explains precisely what is removed.
* Local entropy decrements are **not subadditive under products sharing a control coordinate**, even when all other coordinate blocks are disjoint. An explicit 11-variable Boolean witness is verified with rational logarithm enclosures.

The numerical value \(\kappa_2\), the local entropy estimates, minimum-weight argument, and stopping-tree induction are not claimed as new ingredients. The extension developed here is their application to non-coordinate directional derivatives, robust certificates, and physical-coordinate compression. Its independent publication novelty has not been established.

## 2. Notation and retained one-step identities

Work on \(\mathbb F_2^n\). Let \(f=(-1)^P\), where \(P\) is the unique multilinear algebraic normal form over \(\mathbb F_2\). All polynomial degrees in this report are **algebraic degrees over \(\mathbb F_2\)**, not real Fourier degrees.

Use normalized Walsh coefficients and entropy in bits:

\[
\widehat f(S)=2^{-n}\sum_x f(x)(-1)^{S\cdot x},\quad
H(f)=\sum_S\widehat f(S)^2\log_2\frac1{\widehat f(S)^2}.
\]

Zero-mass terms are zero. Write

\[
\alpha_i(f)=\Pr[f(x)\ne f(x+e_i)],\quad
j_i(f)=\min\{\alpha_i(f),1-\alpha_i(f)\},
\]
\[
I(f)=\sum_i\alpha_i(f),\qquad J(f)=\sum_i j_i(f).
\]

If \(f^0,f^1\) are the physical restrictions at coordinate \(i\), define

\[
\Delta_iH(f)=H(f)-\frac{H(f^0)+H(f^1)}2.
\]

The retained erasure/recombination identity is

\[
\Delta_iH(f)=B_i(f)+\operatorname{JS}(P_i,Q_i),\qquad
B_i(f)=H(S_i\mid S_{-i}),
\tag{2.1}
\]

where \(S\) has law \(\widehat f^{\,2}\), and \(P_i,Q_i\) are the squared Fourier laws of the two children. Consequently

\[
0\le\Delta_iH(f)\le2,
\tag{2.2}
\]

because both a binary conditional entropy and an equally weighted Jensen–Shannon divergence are at most one bit. The stronger retained estimates are

\[
B_i(f)\le h_2(j_i(f)),\qquad
\operatorname{JS}(P_i,Q_i)\le\frac{2}{\ln2}j_i(f),
\tag{2.3}
\]

where \(h_2\) is binary entropy. The latter bound has a self-contained scalar proof in the erasure report.

For completeness, if a fiber of the parent spectrum has real coefficients \(u,v\), its JS contribution, in nats, is bounded by

\[
(u^2+v^2)-|u^2-v^2|=2\min(u^2,v^2).
\]

Indeed, putting \(z=2|uv|/(u^2+v^2)\), the required scalar bound is

\[
\frac{(1+z)\ln(1+z)+(1-z)\ln(1-z)}2
\le1-\sqrt{1-z^2}.
\]

Both sides vanish at zero, and the right derivative minus the left derivative is \(z/\sqrt{1-z^2}-\operatorname{artanh}z\), a nonnegative function since its derivative is \((1-z^2)^{-3/2}-(1-z^2)^{-1}\ge0\). Summation and division by \(\ln2\) prove (2.3).

The physical influence identity and its folded counterpart are

\[
I(f)=\alpha_i(f)+\frac{I(f^0)+I(f^1)}2,
\tag{2.4}
\]
\[
\frac{J(f^0)+J(f^1)}2\le J(f)-j_i(f).
\tag{2.5}
\]

For (2.5), average every remaining coordinate's physical influence over the restriction and use concavity of \(t\mapsto\min(t,1-t)\).

Multiplication by an appropriate Walsh character preserves Fourier entropy and changes \(I\) to \(J\). Thus the universal FEI statement with \(I\) and the universal statement with \(J\) are equivalent with the same constant. No analogous invariance under arbitrary linear changes of physical coordinates is assumed.

### Local payment constant

For \(0<\eta\le1/2\), define

\[
\mathcal L(\eta)=
\min\left\{\frac2\eta,
\frac{h_2(\eta)}\eta+\frac2{\ln2}\right\}.
\tag{2.6}
\]

The function \(h_2(t)/t\) is decreasing on \((0,1/2]\), since its derivative is \(\log_2(1-t)/t^2<0\). Therefore, whenever \(j_i(f)\ge\eta\),

\[
\Delta_iH(f)\le\mathcal L(\eta)j_i(f).
\tag{2.7}
\]

This follows separately from (2.2) and (2.3), and then by taking the better bound. In particular,

\[
\mathcal L(1/4)=4h_2(1/4)+2/\ln2=\kappa_2<6.130503.
\tag{2.8}
\]

This payment estimate and its numerical constant already occur in the companion work. The elementary coarser payment at \(j_i\ge1/4\) is \(8j_i\).

## 3. Robust directional derivative lemma

Define additive and multiplicative directional derivatives by

\[
D_vP(x)=P(x)+P(x+v),\qquad
\mathcal D_v f(x)=f(x)f(x+v)=(-1)^{D_vP(x)}.
\]

Addition of polynomials is over \(\mathbb F_2\).

### Lemma 3.1: minimum weight

If a nonzero multilinear polynomial \(R\) has degree at most \(s\), then

\[
\Pr[R(x)=1]\ge2^{-s}.
\tag{3.1}
\]

**Proof.** The nonzero constant has weight one. Otherwise choose a variable on which \(R\) depends and write \(R=A+x_jB\), with nonzero \(B\) of degree at most \(s-1\). Wherever \(B=1\), exactly one of the two choices of \(x_j\) gives \(R=1\). Induction gives \(\Pr[R=1]\ge\frac12\Pr[B=1]\ge2^{-s}\). This is the standard binary polynomial minimum-weight argument. ∎

### Theorem 3.2: a nonconstant low-degree directional certificate

Suppose \(v\ne0\), \(d\ge1\), and a **nonconstant** polynomial \(q\) of degree at most \(d\) satisfies

\[
\Pr[\mathcal D_v f(x)\ne(-1)^{q(x)}]\le\varepsilon.
\tag{3.2}
\]

For every physical coordinate \(j\) for which \(D_{e_j}q\not\equiv0\),

\[
\boxed{j_j(f)\ge2^{-d}-\varepsilon.}
\tag{3.3}
\]

At least one such physical coordinate exists. When \(\varepsilon<2^{-d}\), the coordinate can be queried with

\[
\boxed{
\Delta_jH(f)\le\mathcal L(2^{-d}-\varepsilon)j_j(f).
}
\tag{3.4}
\]

**Proof.** Put \(g_j(x)=f(x)f(x+e_j)\). Commutation of translations gives

\[
g_j(x)g_j(x+v)
=\mathcal D_v f(x)\mathcal D_v f(x+e_j).
\tag{3.5}
\]

The right side differs from \((-1)^{D_{e_j}q(x)}\) on a set of measure at most \(2\varepsilon\). This uses the union bound and translation invariance, not independence.

Because \(D_{e_j}q\) is nonzero and has degree at most \(d-1\), Lemma 3.1 gives

\[
\Pr[g_j(x)\ne g_j(x+v)]
\ge2^{-(d-1)}-2\varepsilon.
\tag{3.6}
\]

On the other hand, for any sign function \(g\), a disagreement under a measure-preserving translation requires at least one endpoint in either chosen sign class. Applying this to the minority sign class gives

\[
\Pr[g(x)\ne g(x+v)]
\le2\min\{\Pr[g=1],\Pr[g=-1]\}.
\tag{3.7}
\]

Since \(\Pr[g_j=-1]=\alpha_j(f)\), (3.6) and (3.7) imply (3.3). Nonconstancy of \(q\) supplies a coordinate with nonzero derivative. Equation (3.4) follows from (2.7). ∎

The direction \(v\) may involve many input coordinates. No change of the physical influence basis is made. The queried coordinate \(j\) can be different from every natural pivot used to represent \(v\).

### Exact quadratic consequence

If \(D_vP\) is nonconstant of degree at most two, then some physical coordinate satisfies

\[
j_j(f)\ge\tfrac14,\qquad
\Delta_jH(f)\le\kappa_2j_j(f).
\tag{3.8}
\]

If \(D_vP\) is nonconstant affine, the same argument gives \(j_j=1/2\), and the simpler bound \(\Delta_jH\le4j_j\).

## 4. Approximately constant derivatives and zero-cost directions

The nonconstant hypothesis in Theorem 3.2 cannot simply be removed. Constant directional derivatives instead give an isospectral mechanism.

### Theorem 4.1: approximate signed translation

Suppose \(v\ne0\), \(\sigma\in\{-1,1\}\), and

\[
\Pr[f(x+v)\ne\sigma f(x)]\le\varepsilon\le\tfrac12.
\tag{4.1}
\]

For every physical coordinate \(i\) with \(v_i=1\),

\[
\boxed{
\Delta_iH(f)\le
\min\left\{2,h_2(\varepsilon)+\frac{2\varepsilon}{\ln2}\right\}.
}
\tag{4.2}
\]

In particular, exact signed translation symmetry gives \(\Delta_iH(f)=0\).

**Proof.** Write \(x=(x_i,z)\) and \(v=(1,t)\). Let \(g(z)=f(0,z)\), \(h(z)=f(1,z)\). The error indicator in (4.1) is invariant under translation by \(v\), which exchanges the two physical slices. Therefore its density on either slice equals its global density. In particular,

\[
\Pr[h(z+t)\ne\sigma g(z)]\le\varepsilon.
\tag{4.3}
\]

Writing \(a_T=\widehat g(T)\) and \(b_T=\widehat h(T)\), Parseval implies

\[
A:=\sum_T|a_Tb_T|
\ge\left|\mathbb E[\sigma g(z)h(z+t)]\right|
\ge1-2\varepsilon.
\tag{4.4}
\]

Put \(M=(1-A)/2\le\varepsilon\). The exact Hellinger-fiber representation from the preceding P03 report is

\[
w_T=\frac{a_T^2+b_T^2}{2},\quad
m_T=\frac{(|a_T|-|b_T|)^2}{4},\quad
\sum_Tw_T=1,\quad\sum_Tm_T=M,
\]
\[
B_i(f)=\sum_Tw_T h_2(m_T/w_T).
\tag{4.5}
\]

By concavity of binary entropy, \(B_i(f)\le h_2(M)\). The same scalar JS/Hellinger inequality gives \(\operatorname{JS}(P_i,Q_i)\le2M/\ln2\). Since \(M\le\varepsilon\le1/2\), monotonicity yields (4.2), together with (2.2). ∎

A further available refinement is \(M\le\min\{\varepsilon,j_i(f)\}\), because \(\sum_T|a_Tb_T|\ge|\langle g,h\rangle|=|1-2\alpha_i|\).

**Scope warning.** The error term in (4.2) is an absolute entropy charge, not automatically a constant multiple of the queried physical influence. Its weighted sum along a restriction tree has not been uniformly controlled. Treating \(\varepsilon\log(1/\varepsilon)\) as \(O(\varepsilon)\) would be an invalid closure of the full argument.

## 5. A subspace of low-degree directions and its normal form

For \(d\ge0\), define

\[
V_d(P)=\{v\in\mathbb F_2^n:\deg(D_vP)\le d\}.
\tag{5.1}
\]

The zero polynomial is included. Thus zero is always a member.

### Proposition 5.1: linearity and invariance under low-degree additions

The set \(V_d(P)\) is a vector subspace. If \(R\) has degree at most \(d+1\), then

\[
V_d(P+R)=V_d(P).
\tag{5.2}
\]

**Proof.** The derivative identity

\[
D_{v+w}P(x)=D_vP(x)+D_wP(x+v)
\]

shows closure under addition because translations preserve degree bounds. For (5.2), every derivative \(D_vR\) has degree at most \(d\). Adding it cannot create or cancel a term of degree greater than \(d\). ∎

In particular, \(V_2\) is unchanged by any quadratic or cubic twist. This is stronger invariance than merely character multiplication, but **it is an algebraic statement about the certificate space, not invariance of total influence**.

### Proposition 5.2: normal form modulo degree \(d+1\)

If \(r=\dim V_d(P)\), choose an invertible linear coordinate map \(x=A(y,z)\), with \(y\in\mathbb F_2^r\), whose first \(r\) columns form a basis of \(V_d(P)\). Then

\[
\boxed{P(A(y,z))=R(z)+Q(y,z),\qquad\deg Q\le d+1.}
\tag{5.3}
\]

Moreover \(V_d(R)=\{0\}\) in the residual \(z\)-space.

**Proof.** In the new algebraic coordinates every derivative with respect to a \(y\)-coordinate has degree at most \(d\). A monomial containing that coordinate would contribute its uniquely corresponding monomial of degree one less to the derivative. Hence no monomial of total degree greater than \(d+1\) contains a \(y\)-coordinate. Set \(R(z)=P(A(0,z))\); all monomials of \(Q=P\circ A-R\) contain at least one \(y\)-coordinate and therefore have degree at most \(d+1\).

If a nonzero \(z\)-direction gave a derivative of \(R\) of degree at most \(d\), its derivative of \(P\circ A=R+Q\) would have the same bound. This would enlarge the already full \(r\)-dimensional subspace, a contradiction. ∎

An invertible linear substitution preserves algebraic degree bounds in both directions. The substitution in (5.3) is used to describe structure only. The entropy/influence transfer below uses actual physical coordinate restrictions in the original basis.

## 6. Physical-coordinate compression theorem

For \(d\ge1\), set

\[
\kappa_d=\mathcal L(2^{-d}).
\tag{6.1}
\]

For \(d=0\), the corresponding exact signed-symmetry cost is zero.

### Theorem 6.1

Let \(r=\dim V_d(P)\). There is an adaptive physical coordinate restriction tree of depth exactly \(r\), with leaves on \(n-r\) physical variables, such that every queried node satisfies either

\[
\Delta_iH=0
\]

or

\[
\Delta_iH\le\kappa_d j_i.
\tag{6.2}
\]

For \(d=0\), every queried node has zero decrement. If all leaves satisfy \(H\le C_0J\), then

\[
\boxed{H(f)\le\max\{C_0,\kappa_d\}J(f).}
\tag{6.3}
\]

The same direct transfer holds with \(I\) in place of \(J\), given leaf certificates with \(I\).

**Proof.** Maintain an inherited subspace of directions with derivatives of degree at most \(d\). Initially it is \(V_d(P)\), of dimension \(r\).

At a node of depth \(k<r\), the inherited space has dimension at least \(r-k>0\), so choose a nonzero direction \(v\). If \(D_vP\) is constant, choose any pivot coordinate \(i\) with \(v_i=1\). Theorem 4.1 with zero error gives zero entropy decrement. If \(D_vP\) is nonconstant, Theorem 3.2 with zero error supplies a physical coordinate \(i\) with \(j_i\ge2^{-d}\), and (2.7) gives (6.2).

After fixing this coordinate, keep the directions satisfying \(v_i=0\). Intersecting with a coordinate hyperplane loses at most one dimension. Such directions project injectively onto the residual physical cube, and differentiation in them commutes with restriction. Their restricted derivatives still have degree at most \(d\). Thus the inherited space at every child has dimension at least \(r-k-1\). This constructs the claimed depth-\(r\) tree.

For the transfer let \(C=\max\{C_0,\kappa_d\}\). Induct upward from the leaves. At a paid node,

\[
\begin{aligned}
H(f_v)
&=\frac{H(f_v^0)+H(f_v^1)}2+\Delta_iH(f_v)\\
&\le C\frac{J(f_v^0)+J(f_v^1)}2+Cj_i(f_v)\\
&\le CJ(f_v),
\end{aligned}
\]

using (2.5). At a zero-cost node the same estimate holds without the positive charge. The proof with \(I\) uses (2.4) and \(j_i\le\alpha_i\). ∎

The theorem does not need \(r\) to remain the full derivative-space dimension at later nodes. Restrictions can create additional low-degree directions; retaining only the inherited subspace suffices.

### Corollary 6.2: restriction on a minimal counterexample

Fix \(C\ge\kappa_2\). A Boolean function of the smallest dimension violating \(H(f)\le CJ(f)\) must satisfy

\[
\boxed{V_2(P)=\{0\}.}
\tag{6.4}
\]

Equivalently, for every nonzero direction \(v\), the polynomial \(D_vP\) has degree at least three. The same minimal-counterexample assertion holds for \(H\le CI\).

Indeed, any nonzero direction in \(V_2\) provides either a zero-cost split or a split paid at constant \(\kappa_2\). Both smaller children satisfy the candidate inequality by minimality, so the parent also satisfies it, a contradiction.

This extends the preceding signed-translation reduction, which excludes only constant directional derivatives. It does **not** show that every irreducible core satisfies FEI. For example, the single monomial \(P=x_1x_2x_3x_4\) already has \(V_2(P)=\{0\}\), while its sign function is easy to handle by other existing certificates. Absence of low-degree directions is a necessary condition for this minimal counterexample, not a characterization of difficult functions.

The present constant also does not improve every bounded-degree result. In particular, combining marginal entropy with polynomial minimum weight already gives direct degree-dependent FEI bounds. The purpose of this compression is to transfer other available leaf certificates without paying for the number of removable directions.

## 7. An explicit obstruction to shared-control subadditivity

A tempting extension of the existing independent-core results is the following statement. Suppose \(a(t,x)\) and \(b(t,y)\) have disjoint residual blocks \(x,y\) but share one physical control \(t\). One might hope that

\[
\Delta_tH(a b)\le\Delta_tH(a)+\Delta_tH(b).
\tag{7.1}
\]

**Equation (7.1) is false for Boolean functions.** The shared control is essential; ordinary tensorization on entirely disjoint variables is not being refuted.

Let

\[
u_k(x)=1-2\mathbf1_{\{0^k\}}(x),
\]

and define

\[
a_k(t,x)=
\begin{cases}1,&t=0,\\u_k(x),&t=1,\end{cases}
\qquad
F_k(t,x,y)=a_k(t,x)a_k(t,y).
\tag{7.2}
\]

Put \(\delta=2^{-k}\). A split with one constant child and another child whose disagreement probability is \(s\) has exact entropy decrement

\[
\begin{aligned}
\mathcal F(s)
&=2s(1-s)+q_s h_2(s^2/q_s)
+h_2(W_s/2)-\tfrac12h_2(W_s),\\
W_s&=4s(1-s),\qquad q_s=1-W_s/2.
\end{aligned}
\tag{7.3}
\]

This is the character-child formula already proved in the preceding P03 max-splicing report. It follows by separating the zero Fourier atom from the rest; all dependence on the shape of the remaining spectrum cancels between parent and children.

The two children of \(F_k\) are \(1\) and \(u_k(x)u_k(y)\). Independence of the residual physical blocks gives disagreement probability \(2\delta(1-\delta)\). Hence

\[
\Delta_tH(a_k)=\mathcal F(\delta),\qquad
\Delta_tH(F_k)=\mathcal F(2\delta(1-\delta)).
\tag{7.4}
\]

For \(k=5\), exact rational logarithm enclosures certify

\[
\boxed{
0.00239650700679
<\mathcal F(31/512)-2\mathcal F(1/32)
<0.00239650700680.
}
\tag{7.5}
\]

Thus the individual factors have six variables and their shared-control product has eleven variables. Equation (7.5) gives an explicit positive failure margin.

There is also a direct spectral check that avoids any reliance on the scalar derivation. Since the entropy of the independent product \(u_k(x)u_k(y)\) is \(2H(u_k)\),

\[
\Delta_tH(F_k)-2\Delta_tH(a_k)=H(F_k)-2H(a_k).
\tag{7.6}
\]

The checker computes all integer Walsh coefficients for the six- and eleven-variable truth tables, verifies Parseval, encloses both entropies, and obtains the same positive interval.

This counterexample arose after exploratory tests of small child spectra passed. Those earlier tests are not evidence for a universal gluing theorem. The failed conjecture is retired rather than silently used in the directional proof; Sections 3–6 do not depend on it.

## 8. Executed verification and its limitations

Run `python verify_directional_compression.py`. The script needs Python 3.10 or later and NumPy. Its assertion arithmetic is integer or rational; displayed rounded decimals are not used to decide signs.

The executed output `verification.json` records:

* All **65,812 Boolean functions in dimensions one through four**, with **984,884 nonzero function/direction pairs**. The exact directional inequality was checked for degree bounds one and two, including **1,724,992 coordinate certificates**.
* **8,438,032** subspace-closure implications and **2,365,568** restriction-inclusion checks in the same finite cubes.
* All **230,160** triples \((f,v,q)\) in dimensions one through three with nonzero \(v\) and quadratic-or-lower \(q\); the positive-error-margin cases give **1,592** nonconstant certificates and **3,488** coordinate assertions.
* **36** explicit compression trees in dimensions five through eight: 32 seeded high-degree cores with affine scrambling and cubic additions, plus four affine roots. The trees have **572 internal nodes**, including **96 paid nodes** and **476 zero-cost nodes**, and **608 leaves**. The normal form was checked at all 36 roots.
* **2,540** approximate signed-symmetry triples and **4,324** pivot-affinity assertions through dimension three.
* An exact integer Walsh calculation and independent rational-interval scalar calculation for the shared-control counterexample. The computational entropy-gap enclosure has width less than \(6.157\times10^{-49}\); the wider transparent decimal interval (7.5) is rigorously verified. The constant \(\kappa_2\) is enclosed between 6.1305025796144 and 6.1305025796145.

For rational \(1\le t\le2\), logarithms are enclosed using

\[
\ln t=2\sum_{j=0}^{N-1}\frac{z^{2j+1}}{2j+1}+R_N,
\quad z=\frac{t-1}{t+1},\quad
0\le R_N\le\frac{2z^{2N+1}}{(2N+1)(1-z^2)}.
\]

Range reduction puts \(z\le1/3\); the script takes \(N=48\) and also encloses \(\ln2\) rationally. Division by its positive interval encloses base-two logarithms.

These finite checks support the written derivations but do not establish an all-dimensional theorem by themselves. They are not a new exhaustive atlas of all Boolean functions in dimensions five through eleven, and they are not Lean or another proof-assistant formalization. No earlier repository checker was replayed in this continuation.

## 9. Exact remaining gap in the full conjecture

A retained universal reduction is

\[
B(f)=\sum_i H(S_i\mid S_{-i}),\qquad
K_E=\sup_{f\text{ nonconstant}}\frac{B(f)}{I(f)}.
\]

The existing erasure proof establishes

\[
K_E\le C_{\rm FEI}\le K_E+\frac2{\ln2}
\tag{9.1}
\]

in the extended real sense. Finiteness of \(K_E\) is equivalent to FEI. Equation (9.1) quantifies over **all Boolean functions in all dimensions**; it is not the false pointwise bound \(H(f)\le B(f)+(2/\ln2)I(f)\).

Neither the new directional compression nor the preceding core-splicing theorems prove \(K_E<\infty\). The directions needed for exact compression need not exist. Approximate constant directions can leave a logarithmic accumulated error. The remaining high-degree cores still require a uniform entropy allocation, either directly or through a genuinely controlled adaptive tree.

In particular, every physical derivative is trivially approximated by a constant to error \(j_i\), after choosing its majority sign. Feeding that fact into Theorem 4.1 alone gives a charge comparable to \(j_i\log(1/j_i)\), not a uniform multiple of \(j_i\). Small influences therefore do not automatically close the robust route. Likewise, allowing \(d\) to grow with the remaining dimension makes \(\kappa_d\) grow; this is not a universal constant.

The correct continuation target is a uniform rule for the surviving cores that either produces a paid split, reaches an already certified leaf, or gives a **proved, summable** error budget. Assuming such a rule is exactly the unproved step. The present results narrow a structural part of the search and eliminate one attractive but false recombination shortcut; they do not establish that the full conjecture is close to completion.

## 10. Source ledger and delivery status

The following are the actual repository sources used. Paths are relative to `yspennstate/math-open-problems`, branch `master`. A subset of the newest long reports was read where sufficient for the statements used; this is not a claim to have independently audited every historical file in the repository.

**Current entrypoint.** `proofnet24/P03-fei/README.md`, blob `9201da45afcf21156ae078cc505d37b57a1ae4b7`. Retains full OPEN status and the retired absolute-overlap, resolvent, pointwise-erasure, and fixed-coefficient affine-drift shortcuts.

**Erasure identity and universal reduction.** `proofnet24/P03-fei/solo-2026-09-17/ERASURE_REDUCTION.md`, blob `770f1fc8438b360549ed89480cb260768d839923`. Read in full. Supplies (2.1), the JS bound, and (9.1).

**Quadratic symmetry.** `proofnet24/P03-fei/continuations/2026-09-20-quadratic-symmetry/REPORT.md`. Main theorem and its physical-deletion proof were read. The entrypoint supplies the current index and verification scope. This continuation does not change its disjoint-core hypotheses.

**Certified-core splicing and character-child formula.** `proofnet24/P03-fei/runs/2026-09-20/2026-09-20T11-28-37+0300__fei-certified-core-max-splicing.md`, blob `af89172d17d120ae1fdaad52674bd6e452f77099`, creation commit `ec4ad2a720641cc025b2c2f63c9fc79bc0e59da9`. Its initial 240 lines were read, including the scalar formula reused in (7.3).

**Isospectral splicing, Hellinger defect, and signed translations.** `proofnet24/P03-fei/runs/2026-09-20/2026-09-20T12-28-55+0300__fei-isospectral-splicing-symmetry-quotient.md`, blob `3421c0cbfd22031554befb962ec92cd0c8bb45b9`, creation commit `7b445599e2165c53ae44c5f728d0538192e1edc1`. The Hellinger and quotient arguments were read through the commit and source ranges. Its exact zero-cost result is retained.

**Companion physical derivative selector.** `proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20T12-07-26+0300__guarded-derivative-spectral-selector.md`, blob `46641e4c2467a7d9638328b744713615ed092ab0`. Initial 240 lines were read. The numerical constant in (2.8) and the high-influence local entropy payment were already present there. Its spectral-flat physical derivative condition differs from the non-coordinate low-degree directional condition used here.

**External primary source.** María José González, Paul MacManus, and María Cristina Pereyra, *Further evidence towards the Fourier Entropy-Influence conjecture*, arXiv:2606.00246v2, revised **9 June 2026**. Its abstract and HTML introduction were checked on 20 September 2026. It treats full FEI as a conjecture and proves restricted stopping-tree classes; the stopping-tree framework is not new here. The current arXiv history says 9 June, correcting a 2 June date appearing in one inherited companion report. Reference: `https://arxiv.org/abs/2606.00246`.

The published symmetric-function input is Ryan O'Donnell, John Wright, and Yuan Zhou, *The Fourier Entropy–Influence Conjecture for certain classes of Boolean functions*, ICALP 2011, as credited by the quadratic-symmetry report. Bounded searches did not establish whether the directional compression theorem or the gluing counterexample already appears elsewhere; priority remains unverified.

**Delivery.** This package was created in the current conversation. The available GitHub connector exposed read actions, not writes; a Git CLI connection attempt failed to resolve `github.com`. Consequently no new remote commit or scheduled-worker uptake is claimed. An append-only patch adds the report, checker, actual output, and a handoff without altering existing proofs, schedules, ownership, or finite-dimensional metrics. Its application is a separate, unperformed step.
