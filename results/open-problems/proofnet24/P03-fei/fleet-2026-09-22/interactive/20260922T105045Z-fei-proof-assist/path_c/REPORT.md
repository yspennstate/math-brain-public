# Robust trigger clusters and quantitative physical child slack

**Date:** 22 September 2026.  
**Programme:** full uniform-cube Fourier entropy–influence, Path C.  
**Classification:** `ESSENTIAL_STEP_APPLIED / ROBUST_CLUSTER_CHILD_SLACK`.  
**Full FEI:** **OPEN / NOT PROVED.**

## 1. Result and its place in the common argument

The current stopping argument leaves a genuine finite-dimensional extremal Boolean function of ratio

\[
\rho=\mathcal F(f)/\mathcal J(f)>K,
\qquad \mathcal F=H-\mathcal P,\quad
\mathcal P=\sum_i\mathfrak j(q_i),\quad
\mathcal J=\sum_iq_i,
\]

where character centering makes \(q_i=\operatorname{Inf}_i(f)\le1/2\) and

\[
\mathfrak j(q)=1-h_2(1/2+\sqrt{q(1-q)}).
\]

This report proves a structural and quantitative restriction on the robust derivative rows of that *same* extremal function.

At the live robustness threshold \(\eta=1/16\):

1. Two mutually triggering robust rows have **exactly the same closed trigger core**, including compatible literal assignments. Reciprocal components are cliques.
2. A one-way trigger between robust cliques increases their common subcube mass by a factor of at least **16**. Thus the contracted trigger graph is acyclic and its arrows decrease trigger codimension by at least four.
3. A robust clique \(C\) with at least two rows yields actual physical restrictions to \(C\) that are signed one-point defects on a quantified fraction of the outside assignments.
4. Full ratio extremality converts those physical branches into the linear-in-influence child slack
   \[
   \boxed{
   \mathbb E_z[\rho\mathcal J(f_z)-\mathcal F(f_z)]
   \ge \frac78(\rho-r_{|C|})\sum_{i\in C}q_i,
   \qquad r_m<2.
   }
   \tag{1.1}
   \]
   Here the queried block is the actual complement of \(C\), and \(r_m\) is the exactly computable \(\mathcal F/\mathcal J\) ratio of the \(m\)-variable one-point defect.
5. All-block criticality also supplies a genuine fractional nonreuse theorem on any trigger-independent selected row family: all its robust demands can be assigned to trigger-coordinate surplus capacities simultaneously. Failure of that transport supplies an affordable physical block.

The report does **not** bound the entropy cost of exposing the complement of \(C\). It does not sum the slack of overlapping complement queries or the costs of paths sharing a sink. Thus (1.1) is a new quantitative input to the missing stopping argument, not full FEI closure.

## 2. Exact source premises

All repository links below point to `yspennstate/math-open-problems`.

- **Terminal core and physical block inequality:** [commit 85ffa60](https://github.com/yspennstate/math-open-problems/blob/85ffa60db26997421d980b1f86c03d82259504ca/proofnet24/P03-fei/fleet-2026-09-21/account02/B13/20260922T075416Z-all-block-terminal-core/REPORT.md), especially §§2–4. For a physical block \(A\),
  \[
  D_A=\mathcal J(f)-\mathbb E_z\mathcal J(f_z)
  =\sum_{i\in A}q_i+\sum_{j\notin A}c_j(A),
  \]
  \[
  \Delta_A\mathcal F\le B_A-W_A,\quad
  B_A=H(X_A\mid X_{A^c}),\quad
  W_A=\sum_{j\notin A}\mathfrak j'(q_j)c_j(A).
  \]
  Full ratio extremality means every Boolean function on at most the chosen dimension has ratio at most \(\rho\); proper restriction children therefore have nonnegative slack \(\rho\mathcal J-\mathcal F\).
For clarity, write \(r_j(z)=\operatorname{Inf}_j(f_z)\) before centering the child. Then \(c_j(A)=q_j-\mathbb E\min(r_j(z),1-r_j(z))=\mathbb E(2r_j(z)-1)_+\). The source uses \(U_A=\sum_{k\in A}h_2(q_k)-W_A\); all-block terminality at level \(K>2\) means \(U_A\ge KD_A\) for every nonempty physical block. The sharper \(B_A-W_A\) remains the entropy-increment upper bound used in (7.3).

- **Robust rows and trigger polarization:** [commit fdbfbcc](https://github.com/yspennstate/math-open-problems/blob/fdbfbcc1beed0db4cb6d13c8d61fd92db53a8113/proofnet24/P03-fei/fleet-2026-09-21/account04/B12/20260922T081051Z-terminal-trigger-surplus/REPORT.md). Its bound \(c_i(F_i)\ge q_i-\varepsilon_i\) is used in §8.
- **Pair-selected physical stopping:** [commit 54004a5](https://github.com/yspennstate/math-open-problems/blob/54004a5887b551482292a6a173d688da4b9fbfe7/proofnet24/P03-fei/fleet-2026-09-22/account01/B12/20260922T101952Z-account01-B12-r11/REPORT.md). The present clique structure and child slack address its missing robust-trigger cover/selection step.
- **Canonical adaptive selector:** [commit 4a17483](https://github.com/yspennstate/math-open-problems/blob/4a1748352ae7e31c4941f91c3f6a81a5a6928421/proofnet24/P03-fei/fleet-2026-09-22/account02/B20/20260922T103102Z-account02-B20-fei-r17/REPORT.md). A block selected deterministically from the current function and decoded physical history has zero conditional address entropy. The present results require no hidden spectral selector.
- **Selected-pair occurrence KL:** [commit fc42e79](https://github.com/yspennstate/math-open-problems/blob/fc42e79e7f6e43ba79986fda86d1f75d10ec1a20/proofnet24/P03-fei/fleet-2026-09-22/account03/B19/20260922T103024Z-b19-fei-r11/REPORT.md). Its normalized single-pair KL credit remains available, but is not summed or spent in this report.

No raw hidden-curvature bound, fixed all-gate potential, bounded trigger degree, or replacement of ratio extremality by terminality is assumed.

## 3. Robust supports and exact Boolean integrability

Write \(f=(-1)^b\), with \(b:\{0,1\}^n\to\{0,1\}\), and use addition modulo two for Boolean derivatives. Put

\[
E_i(x)=\Delta_i b(x)=b(x)\oplus b(x\oplus e_i).
\]

This is the derivative support indicator, independent of \(x_i\), and \(\mathbb E E_i=q_i\). For every robust row choose an actual coordinate subcube

\[
Q_i(x)=\mathbf1[x_{F_i}=a_i],\quad
F_i\subseteq[n]\setminus\{i\},\quad
s_i=2^{-|F_i|},
\]

with

\[
\varepsilon_i=\Pr(E_i\ne Q_i)\le\eta q_i,
\qquad 0\le\eta<1/4.
\tag{3.1}
\]

All these objects live on one uniform physical cube; extending a quotient-cube indicator constantly in the missing coordinate changes no probabilities. Since \(|s_i-q_i|\le\varepsilon_i\),

\[
(1-\eta)q_i\le s_i\le(1+\eta)q_i.
\tag{3.2}
\]

The key source-valid identity is simply commutation of Boolean derivatives:

\[
\boxed{\Delta_jE_i=\Delta_iE_j.}
\tag{3.3}
\]

Approximating either derivative by the derivative of its subcube costs at most two endpoint errors:

\[
\Pr(\Delta_jE_i\ne\Delta_jQ_i)\le2\varepsilon_i.
\tag{3.4}
\]

If \(j\notin F_i\), then \(\Delta_jQ_i=0\). If \(j\in F_i\), then

\[
\Delta_jQ_i=R_{i,j}:=\mathbf1[x_{F_i\setminus\{j\}}=a_i|_{F_i\setminus\{j\}}],
\quad \Pr(R_{i,j}=1)=2s_i.
\tag{3.5}
\]

## 4. Reciprocal rigidity and one-way influence jumps

### Lemma 4.1 — separation of distinct coordinate subcubes

If \(Q,R\) are distinct nonempty coordinate subcubes, then

\[
\mu(Q\triangle R)\ge\frac{\mu(Q)+\mu(R)}3.
\tag{4.1}
\]

**Proof.** Suppose \(\mu(Q)\le\mu(R)\). If their sizes differ, their dyadic sizes give \(\mu(R)\ge2\mu(Q)\), and \(\mu(Q\triangle R)\ge\mu(R)-\mu(Q)\ge(\mu(Q)+\mu(R))/3\). If their sizes agree but they differ, their intersection is empty or has at most half their common size. Their symmetric difference is therefore at least that common size, which is stronger. ∎

### Theorem 4.2 — reciprocal rows have exactly equal stripped subcubes

If \(j\in F_i\) and \(i\in F_j\), then

\[
R_{i,j}=R_{j,i},\qquad
F_i\setminus\{j\}=F_j\setminus\{i\},\qquad s_i=s_j,
\tag{4.2}
\]

and the literal assignments agree on the common stripped coordinates.

**Proof.** Equations (3.3)–(3.5) give

\[
\mu(R_{i,j}\triangle R_{j,i})
\le2(\varepsilon_i+\varepsilon_j)
\le\frac{2\eta}{1-\eta}(s_i+s_j).
\]

Distinct stripped subcubes would, by Lemma 4.1, have difference at least \(2(s_i+s_j)/3\). This contradicts \(\eta/(1-\eta)<1/3\). Equal coordinate subcubes have identical constrained-coordinate sets and literal assignments. ∎

### Theorem 4.3 — one-way triggers climb influence

If \(j\in F_i\) but \(i\notin F_j\), then for \(\eta>0\)

\[
\boxed{q_j\ge\frac{1-2\eta}{\eta}q_i.}
\tag{4.3}
\]

**Proof.** Let \(p_{ij}=\Pr(\Delta_jE_i=1)=\Pr(\Delta_iE_j=1)\). On the triggering side,

\[
p_{ij}\ge2s_i-2\varepsilon_i\ge2q_i-4\varepsilon_i
\ge2(1-2\eta)q_i.
\]

On the nontriggering side, \(p_{ij}\le2\varepsilon_j\le2\eta q_j\). Combine them. If \(\eta=0\), a one-way trigger between positive robust rows is impossible. ∎

## 5. Clique cores, acyclic scale ascent, and a path charge

Define a directed graph on robust rows by \(i\to j\) when \(j\in F_i\) and \(j\) is robust. Use reciprocal adjacency when both arrows occur. Set \(N_i=\{i\}\cup F_i\).

Theorem 4.2 gives \(N_i=N_j\) on each reciprocal edge. Along any reciprocal path these sets stay equal. Every pair of distinct vertices with the same such set triggers one another. Consequently each reciprocal component \(C\) is a clique with one common core

\[
N_C=C\sqcup T_C,\qquad F_i=N_C\setminus\{i\}\ (i\in C),
\quad s_C=2^{-(|N_C|-1)}.
\tag{5.1}
\]

For a singleton clique, its own internal literal is arbitrary and does not affect its derivative-support subcube. For a clique with at least two vertices, the literal assignments are compatible with one assignment \(a_C\) on \(N_C\): for each coordinate use any row other than that coordinate; Theorem 4.2 proves agreement whenever two rows supply it. For a two-vertex clique the stripped comparison fixes the common outside literals, and the two opposite rows separately supply the two internal literals.

At \(\eta=1/16\), an inter-clique arrow \(C\to D\) satisfies

\[
\frac{s_D}{s_C}
\ge14\frac{1-\eta}{1+\eta}
=\frac{210}{17}>12.
\]

Both masses are powers of two, so in fact

\[
\boxed{s_D\ge16s_C,\qquad |N_D|-1\le |N_C|-1-4.}
\tag{5.2}
\]

This proves acyclicity without assuming that the actual influences are equal within a clique. An inactive coordinate cannot occur as a trigger of a positive robust row: its mixed derivative is zero, whereas (3.4)–(3.5) give the strictly positive lower bound \(2(1-2\eta)q_i\) on that mixed derivative. If every active row is robust, a sink clique has \(T_C=\varnothing\): an outside trigger would be a robust vertex creating an outgoing arrow.

For one directed clique path \(C_0\to\cdots\to C_\ell\), choose any representative \(i_r\in C_r\). The geometric mass increase gives a dimension-independent *single-path* charge:

\[
\sum_{r=0}^{\ell}q_{i_r}
\le\frac1{1-\eta}\sum_{r=0}^{\ell}s_{C_r}
\le\frac{16}{15(1-\eta)}s_{C_\ell}
\le\boxed{\frac{272}{225}q_{i_\ell}}.
\tag{5.3}
\]

This is not a global cover estimate: different paths may merge, and (5.3) cannot be summed with a repeatedly charged sink.

### Corollary 5.1 — exact subcube derivatives classify the whole Boolean function

Suppose every active centered derivative support is an exact coordinate subcube, so \(\eta=0\) for every active row. Then

\[
\boxed{f=\pm\prod_C\left(1-2\mathbf1[x_C=a_C]\right)}
\tag{5.4}
\]

on disjoint coordinate blocks \(C\), with irrelevant coordinates omitted. Before character centering, an arbitrary character factor may also occur. In particular,

\[
H(f)\le4\mathcal J(f)\le4I(f).
\tag{5.5}
\]

**Proof.** By Theorem 4.3 at \(\eta=0\), no trigger between active rows is one-way. An inactive coordinate cannot be a trigger either: its Boolean derivative is zero, so (3.3) would contradict the nonzero stripped subcube derivative. Thus every reciprocal clique is closed, \(N_C=C\), and the cliques are disjoint. Its compatible assignment supplies the monomial sign in (5.4), whose derivative support on each \(i\in C\) equals \(E_i\) exactly. Multiplying \(f\) by all these signs makes every Boolean derivative zero, hence leaves a constant. Fourier entropy and influence add across disjoint products. The point-defect estimate \(H_m<4J_m\), proved in §7, gives (5.5); the character-only case has zero Fourier entropy. ∎

The conclusion is a known easy class for FEI; no novelty claim is made for that class. The structural content here is the deduction of its disjoint factorization from the exact derivative-support hypothesis. At positive \(\eta\), one-way edges can occur and this factorization must not be asserted.

## 6. Physical fibers of a robust clique

Let \(C\) have size \(m\ge2\), let \(T=N_C\setminus C\), \(t=|T|\), and let \(a_C\) be the compatible core assignment. Define the actual Boolean monomial sign

\[
M_N(x)=1-2\mathbf1[x_{N_C}=a_C],\qquad h=fM_N.
\]

For every \(i\in C\), the derivative support of \(M_N\) is exactly \(Q_i\). Multiplication XORs derivative support indicators, hence

\[
\operatorname{Inf}_i(h)=\Pr(E_i\ne Q_i)=\varepsilon_i.
\tag{6.1}
\]

Restrict all original coordinates outside \(C\), with the genuine uniform physical law. For an outside assignment \(z\), write \(h_z,f_z\) for the resulting \(m\)-variable functions. The ordinary influence identity gives

\[
\mathbb E_z I(h_z)=\sum_{i\in C}\varepsilon_i=:\varepsilon_C.
\tag{6.2}
\]

### Lemma 6.1 — minimum nonzero influence on an \(m\)-cube

Every nonconstant \(m\)-variable Boolean function satisfies

\[
I\ge m2^{1-m}=:J_m.
\tag{6.3}
\]

**Proof.** Its nontrivial Boolean cut in the cube has at least \(m\) boundary edges. For completeness, this edge-connectivity bound follows by induction after splitting by the last bit. If both half-cuts are nontrivial, the internal boundary is at least \(2(m-1)\ge m\). If exactly one is nontrivial, its internal boundary is at least \(m-1\), and there is at least one cross edge. If both are trivial, a nontrivial whole cut separates the two entire half-cubes and has \(2^{m-1}\ge m\) edges. The case \(m=1\) starts the induction. Divide the edge count by \(2^{m-1}\). ∎

Thus

\[
\Pr_z(h_z\text{ nonconstant})\le\varepsilon_C/J_m.
\tag{6.4}
\]

The activation event \(z_T=a_T\) has probability \(2^{-t}\). On that event, \((M_N)_z\) is the one-point defect \(M_C\); off that event it is constant. Therefore, on every active fiber for which \(h_z\) is constant,

\[
f_z=\pm M_C.
\]

### Theorem 6.2 — quantitative point-defect branches

\[
\boxed{
\Pr_z(f_z=\pm M_C\text{ via a constant error fiber})
\ge 2^{-t}-\frac{\varepsilon_C}{J_m}
\ge\frac{1-2\eta}{1-\eta}2^{-t}.
}
\tag{6.5}
\]

**Proof.** Subtract all bad fibers from the activation event. Since every row has common subcube mass \(s=2^{-(m+t-1)}\), (3.2) gives \(\varepsilon_C\le\eta ms/(1-\eta)\). Also \(ms=2^{-t}J_m\). ∎

At \(\eta=1/16\) the fraction is \((14/15)2^{-t}\). This statement uses actual physical branch probabilities, not spectral sample labels.

## 7. Full extremality converts these branches into linear child slack

The \(m\)-variable one-point defect has \(q=2^{1-m}\), \(J_m=mq\), Fourier empty mass \((1-q)^2\), and \(2^m-1\) other masses \(q^2\). Define

\[
H_m=-(1-q)^2\log_2(1-q)^2-(2^m-1)q^2\log_2q^2,
\]
\[
r_m=\frac{H_m-m\mathfrak j(q)}{mq}.
\tag{7.1}
\]

For all \(m\ge2\), \(r_m<2\). Here are elementary proofs of the two estimates needed. With \(v=1-(1-q)^2<2q\), the inequality \(-x\log_2x\le(1-x)/\ln2\) gives

\[
H_m\le v(2m-2+1/\ln2)<4mq.
\]

Also \(\mathfrak j(q)\ge2q\) on \([0,1/2]\). To verify concavity directly, put \(x=\sqrt{q/(1-q)}\). Its derivative is

\[
\mathfrak j'(q)=\frac{2}{\ln2}
\left(1-\sum_{k\ge1}\frac{2x^{2k}}{(2k-1)(2k+1)}\right),
\]

which decreases as \(q\) increases. Therefore \(\mathfrak j\) is concave, and its chord between \((0,0)\) and \((1/2,1)\) gives the claim. Subtracting \(m\mathfrak j(q)\ge2mq\) proves \(r_m<2\).

Now assume **full ratio extremality with \(\rho>4\)**, and let \(C\) be proper. Every child after querying \(A=[n]\setminus C\) has nonnegative slack

\[
L_z:=\rho\mathcal J(f_z)-\mathcal F(f_z)\ge0.
\]

Every good active child of Theorem 6.2 has slack exactly \((\rho-r_m)J_m\). Consequently,

\[
\mathbb E_zL_z
\ge (ms-\varepsilon_C)(\rho-r_m).
\]

Since \(J_C:=\sum_{i\in C}q_i\le ms+\varepsilon_C\),

\[
ms-\varepsilon_C\ge J_C-2\varepsilon_C\ge(1-2\eta)J_C.
\]

### Theorem 7.1 — robust clique child slack

\[
\boxed{
\mathbb E_z[\rho\mathcal J(f_z)-\mathcal F(f_z)]
\ge(1-2\eta)(\rho-r_m)J_C
>(1-2\eta)(\rho-2)J_C.
}
\tag{7.2}
\]

At \(\eta=1/16\) and \(\rho>4\), the last quantity exceeds \(7J_C/4\).

If \(C=[n]\), then \(T=\varnothing\) and there is only one outside fiber. Equation (6.4) bounds its bad probability by \(\eta/(1-\eta)<1\); that probability is zero or one, hence zero. Thus \(f=\pm M_C\), so \(\rho=r_m<2\), already contradicting \(\rho>4\).

For a proper clique, retain the slack in the exact restriction identity:

\[
\Delta_A\mathcal F
=\rho D_A+\mathbb E_zL_z.
\]

The imported physical block upper bound therefore forces the quantitative critical-core inequality

\[
\boxed{
B_A-W_A-\rho D_A
\ge(1-2\eta)(\rho-r_m)J_C.
}
\tag{7.3}
\]

This strengthens mere all-block terminality for this particular complement query. An actual block estimate with a smaller left side would eliminate the core. Exposing the complement may still be expensive; (7.3) does not prove otherwise.

## 8. A genuine nonreuse transport theorem for selected rows

Call a robust row family \(R\) *trigger-independent* if

\[
F_i\cap R=\varnothing\quad(i\in R).
\tag{8.1}
\]

This permits arbitrarily shared trigger coordinates. At terminal level \(K>2\), set

\[
\sigma_k=h_2(q_k)-Kq_k\ge0,
\qquad d_i=(K+\mathfrak j'(q_i))(q_i-\varepsilon_i).
\tag{8.2}
\]

### Theorem 8.1 — shared triggers have a simultaneous fractional payment

For any trigger-independent \(R\) in an all-block-terminal function, there are numbers \(x_{ik}\ge0\), supported on \(k\in F_i\), such that

\[
\sum_{k\in F_i}x_{ik}=d_i\quad(i\in R),
\qquad
\sum_{i\in R:k\in F_i}x_{ik}\le\sigma_k\quad(k\notin R).
\tag{8.3}
\]

**Proof.** For every \(S\subseteq R\), let \(A=\bigcup_{i\in S}F_i\). Then \(A\cap S=\varnothing\). Conditional Jensen shows that crossing \(c_i(A)\) is nondecreasing under refinement of the revealed physical block, so

\[
c_i(A)\ge c_i(F_i)\ge q_i-\varepsilon_i\quad(i\in S).
\]

All-block terminality rearranges to

\[
\sum_{k\in A}\sigma_k
\ge\sum_{j\notin A}(K+\mathfrak j'(q_j))c_j(A)
\ge\sum_{i\in S}d_i.
\tag{8.4}
\]

These are exactly the finite capacitated Hall conditions. A network with source-to-row capacities \(d_i\), unrestricted row-to-trigger arcs, and trigger-to-sink capacities \(\sigma_k\) therefore saturates every row demand by max-flow/min-cut. Its edge flows give (8.3). ∎

Conversely, at a state with nonnegative \(\sigma_k\), failure of this transport gives a cut \(S\) violating (8.4). Its actual block \(A=\bigcup_{i\in S}F_i\) satisfies \(U_A<KD_A\), so it is an affordable physical stopping block. If a \(\sigma_k\) is negative, that singleton is already affordable. Canonically choose the first such cut and block; this incurs no hidden selector label cost.

One representative from each clique in an antichain of the contracted robust-trigger DAG gives an admissible trigger-independent family. Selecting all vertices of a mutual clique does not: querying their triggers would expose the other target rows. Neither the clique loss nor the cost of covering many DAG antichains is silently discarded.

## 9. Checks and a concrete nontrivial hierarchy

`CHECKER.py` independently computes derivative supports, mixed-derivative commutation, subcube approximations, reciprocal cores, common literals, physical fiber classifications, and exact influence masses. It includes exhaustive Boolean gates through dimension three and an explicit eleven-variable function

\[
b(x)=x_0x_1x_2x_3\ \oplus\ x_0x_4x_5\cdots x_{10}.
\tag{9.1}
\]

At \(\eta=1/16\), all rows are robust and centered. The first core is \(\{0,1,2,3\}\) with subcube mass \(1/8\); the second reciprocal clique is \(\{4,\ldots,10\}\), whose common closed trigger core also contains coordinate 0 and has subcube mass \(1/128\). Its one-way arrow goes to the first clique. The shared row 0 has influence \(67/512\), approximation error \(1/128\), and is still robust. Other first-core rows have influence \(1/8\), and second-clique rows have influence \(1/128\).

This example confirms that influence values need not be identical within a robust clique and that different cliques can share a coordinate through a one-way trigger. It is not asserted to be ratio-critical and is not a counterexample to FEI. It prevents an invalid strengthening of the structural theorem to “all robust rows form independent exact tensor factors.”

The executed checker returned `PASS`: 276 exhaustive Boolean gates through dimension three, 592 robust rows, and 280 reciprocal components; the eleven-variable two-clique hierarchy has one inter-clique arrow. Its two actual good-active fiber probabilities are \(127/128\) and \(1/2\), respectively. The explicit physical child-slack tests pass with \(\rho=10\), a coefficient separately verified to dominate those tested child ratios; the example itself is not claimed to be a ratio maximizer. The point-defect formula was checked through \(m=128\), in addition to the analytic bound \(r_m<2\).

## 10. What is still needed for full FEI

The advance is linear physical child slack and exact robust-trigger structure. The surviving global obligations are explicit:

1. Pay the entropy cost of a complement/trigger query using the new slack, or prove a cheaper physical query with an equivalent gain.
2. Cover enough robust influence by the selected cliques/trigger-independent families while retaining actual reach probabilities and sink capacities. A single-path geometric bound is not a global bound when paths merge.
3. Handle singleton robust cliques, nonrobust rows, and arbitrarily small influences without a dimension factor.

The proof of Theorem 7.1 specifically uses full ratio extremality to make all other child slacks nonnegative. All-block terminality or tensor primitivity alone is insufficient for that step. No refuted raw-\(U_4\) estimate or fixed-potential candidate is revived.

**Full FEI remains open.**
