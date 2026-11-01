# C0034 — a unified cut-parity theorem and an exact two-cut gluing no-go theorem

Target: Russell Lyons, *Determinantal Probability: Basic Properties and Conjectures*, ICM 2014, Question 2.8 (same endpoint as Question 10.1 in Lyons 2003).

Scope: the first unresolved finite core, an orthogonal decomposition

\[
\mathbb C^6=H_1\oplus H_2\oplus H_3,\qquad \dim H_r=2,
\]

with color-\(r\) projection-DPP edge law

\[
w^r_e=|\Delta^r_e|^2,\qquad e\in\binom{[6]}2.
\]

This artifact proves a complete restricted theorem about all cut facets currently isolated on this core and then proves that every compatibility test involving only two cuts and their symmetric difference is automatically satisfiable. It does **not** solve Lyons's unrestricted source problem; the frozen source metric remains `R_univ >= 3`.

## 1. B3 — one occupation-parity theorem contains all known cut facets

Choose orthonormal row matrices \(U_r\in\mathbb C^{2\times6}\) spanning \(H_r\), and stack them to a unitary \(U\in\mathbb C^{6\times6}\). For a coordinate set \(X\subset[6]\), let \(D_X\) be the coordinate projection and define

\[
Q_X:=UD_XU^*.
\]

Then \(Q_X\) is a rank-\(|X|\) orthogonal projection on the six adapted basis coordinates. Split those six coordinates into the three two-element blocks \(B_1,B_2,B_3\) corresponding to \(H_1,H_2,H_3\). Let

\[
S_X\sim\mathbb P^{Q_X},\qquad N_r:=|S_X\cap B_r|\in\{0,1,2\}.
\]

Because \(Q_X\) is a projection,

\[
N_1+N_2+N_3=|X|\qquad\text{almost surely}. \tag{1.1}
\]

For each color define the crossing and noncrossing edge masses

\[
c_r(X):=\sum_{|e\cap X|=1}w^r_e,
\qquad
t_r(X):=\sum_{e\subset X}w^r_e+\sum_{e\subset X^c}w^r_e.
\]

Since each color law has total mass one, \(c_r+t_r=1\).

### Theorem 1.1 (exact cut-parity representation)

For every \(X\subset[6]\) and every color \(r\),

\[
\boxed{\ t_r(X)=\Pr(N_r\text{ is even}),\qquad c_r(X)=\Pr(N_r\text{ is odd}).\ } \tag{1.2}
\]

#### Proof

The diagonal \(2\times2\) block \((Q_X)_{rr}\) equals \(U_rD_XU_r^*\). By Cauchy--Binet,

\[
\det (Q_X)_{rr}=\sum_{e\subset X}|\det U_r[:,e]|^2
=\sum_{e\subset X}w^r_e.
\]

For a projection DPP, \(\Pr(N_r=2)=\det(Q_X)_{rr}\). Similarly

\[
I_2-(Q_X)_{rr}=U_rD_{X^c}U_r^*,
\]

so

\[
\Pr(N_r=0)=\det(I_2-(Q_X)_{rr})
=\sum_{e\subset X^c}w^r_e.
\]

Adding gives \(t_r=\Pr(N_r\in\{0,2\})\); subtracting from one gives \(c_r=\Pr(N_r=1)\). QED.

### 1.1 Even cuts: the entire `2+4` crossing orbit

If \(|X|=2\) or \(4\), (1.1) implies that the parity vector

\[
Z_X=(1_{N_1\text{ odd}},1_{N_2\text{ odd}},1_{N_3\text{ odd}})
\]

has even Hamming weight. Hence it takes values only in

\[
000,\ 110,\ 101,\ 011.
\]

Writing \(p_r=c_r(X)=\Pr((Z_X)_r=1)\), the four atom probabilities are forced to be

\[
\lambda_{000}=1-\frac{p_1+p_2+p_3}{2}, \tag{1.3}
\]
\[
\lambda_{110}=\frac{p_1+p_2-p_3}{2},\quad
\lambda_{101}=\frac{p_1+p_3-p_2}{2},\quad
\lambda_{011}=\frac{p_2+p_3-p_1}{2}. \tag{1.4}
\]

Therefore

\[
p_r\le p_s+p_t\qquad(\{r,s,t\}=\{1,2,3\}), \tag{1.5}
\]

and

\[
p_1+p_2+p_3\le2. \tag{1.6}
\]

The three inequalities (1.5), over the fifteen `2+4` cuts, are exactly the previously certified 45-element crossing colored facet orbit.

### 1.2 Odd balanced cuts: the entire `3+3` internal orbit and the blossom

If \(|X|=3\), define instead

\[
T_X=(1_{N_1\text{ even}},1_{N_2\text{ even}},1_{N_3\text{ even}})=1-Z_X.
\]

Because \(N_1+N_2+N_3\) is odd, \(T_X\) again has even Hamming weight. Applying (1.3)--(1.6) with \(p_r=t_r(X)\) gives

\[
t_r(X)\le t_s(X)+t_t(X) \tag{1.7}
\]

and

\[
t_1(X)+t_2(X)+t_3(X)\le2. \tag{1.8}
\]

The inequalities (1.7), over the ten unordered `3+3` cuts and three singled colors, are exactly the 30-element balanced colored facet orbit already proved separately.

The sum inequality (1.8) is the uncolored three-set blossom. Indeed, write

\[
m_e=w^1_e+w^2_e+w^3_e.
\]

The uncolored degree equations give \(m(E(X))=m(E(X^c))\) for \(|X|=3\), and therefore

\[
t_1+t_2+t_3=m(E(X))+m(E(X^c))=2m(E(X)).
\]

Thus (1.8) is exactly \(m(E(X))\le1\).

Consequently a **single auxiliary projection-DPP parity theorem simultaneously proves all 85 nontrivial cut facets currently isolated on the six-point core**: 45 crossing colored facets, 30 balanced colored facets, and 10 uncolored blossom facets.

### 1.3 Uniform sum-of-squares certificate

The four numbers in (1.3)--(1.4) are not abstract barycentric variables. They are exactly probabilities of parity patterns of the projection DPP \(S_X\). If \(Z\) is an orthonormal-row matrix spanning `range(Q_X)`, then Cauchy--Binet gives

\[
\Pr(S_X=J)=|\det Z[:,J]|^2.
\]

Hence every \(\lambda_z\) is a sum of squared maximal minors over the subsets \(J\) having block-parity pattern \(z\). In particular,

\[
p_s+p_t-p_r=2\lambda_{z(r=0,s=t=1)}\ge0, \tag{1.9}
\]

and

\[
2-(p_1+p_2+p_3)=2\lambda_{000}\ge0. \tag{1.10}
\]

Thus the whole 85-facet cut family has one uniform Plücker sum-of-squares explanation.

## 2. B19 — local cut reconstruction becomes an explicit algorithm

Equations (1.3)--(1.4) show that the one-cut problem is algorithmically solved. Given any candidate colored edge marginals satisfying the affine normalization, compute the three cut masses \(p_1,p_2,p_3\). There is exactly one probability law on the four allowed parity states with those one-bit marginals, and its atoms are the \(\lambda\)'s above.

Therefore nonnegativity of that local cut law is **equivalent** to the four tetrahedral inequalities

\[
p_r\le p_s+p_t,\qquad p_1+p_2+p_3\le2.
\]

For a true orthogonal/Plücker point, Theorem 1.1 realizes the reconstructed law by the actual auxiliary DPP \(S_X\). Thus the known cut inequalities are not merely necessary inequalities: they are the complete one-cut consistency conditions.

What remains is global gluing. The 90 colored perfect-match atoms must realize *all* cut parity laws simultaneously.

## 3. B20 — exact two-cut gluing polytope

We now ask whether two local cut laws can expose a new obstruction.

For a deterministic colored perfect matching \(M\), let

\[
Z_X(M)\in\mathbb F_2^3
\]

be the vector whose color-\(r\) bit records whether the color-\(r\) matching edge crosses \(X\). Cut indicators obey the exact cocycle identity

\[
\boxed{\ Z_{X\triangle Y}=Z_X\oplus Z_Y.\ } \tag{3.1}
\]

The parity of \(Z_X\) is fixed by \(|X|\bmod2\). Each parity coset contains four states and is canonically an affine copy of \(G=\mathbb F_2^2\). After translating the three relevant cosets, the two-cut gluing problem is therefore the following universal finite model:

> Given marginal laws of \(U,V,W\in G\), does there exist a joint law supported on \(W=U\oplus V\)?

There are 16 atoms \((u,v,u\oplus v)\). Eliminating one state from each four-state marginal leaves a nine-dimensional affine marginal polytope.

### Theorem 3.1 (complete exact H-description of the XOR three-marginal polytope)

The nine-dimensional convex hull of the 16 atoms \((u,v,u\oplus v)\), \(u,v\in\mathbb F_2^2\), has exactly 24 facets:

1. the 12 marginal nonnegativity facets;
2. for each of the three nonzero linear characters \(\ell:G\to\mathbb F_2\), the four parity-tetrahedron facets

\[
q_A\le q_B+q_C,\quad
q_B\le q_A+q_C,\quad
q_C\le q_A+q_B,\quad
q_A+q_B+q_C\le2, \tag{3.2}
\]

where

\[
q_A=\Pr(\ell(U)=1),\quad q_B=\Pr(\ell(V)=1),\quad q_C=\Pr(\ell(W)=1).
\]

The accompanying exact-arithmetic checker exhausts all \(\binom{16}{9}=11440\) possible nine-vertex affine bases, recovers every supporting hyperplane, obtains exactly these 24 facets, and verifies that the tight atoms of every listed inequality affinely span dimension eight.

### Theorem 3.2 (two-cut gluing cannot find the missing C0034 obstruction)

Let \(x^1,x^2,x^3\) be any three **nonnegative probability distributions on the edges of \(K_6\)**. For any cuts \(X,Y\), construct the unique four-state local parity laws for \(X,Y,X\triangle Y\) whenever their one-cut tetrahedron inequalities hold. Then those three local laws always admit a joint coupling satisfying (3.1).

#### Proof

By Theorem 3.1 it suffices to verify marginal nonnegativity and the 12 inequalities (3.2). Marginal nonnegativity is part of the hypothesis/local reconstruction.

Fix a nonzero character \(\ell\) on the four-state cut-parity coset. Up to the deterministic parity translation of the coset, \(\ell(Z_X)\) is the crossing indicator of one fixed color edge. Thus for a random edge \(E_r\sim x^r\),

\[
\ell(Z_X)=1_{E_r\text{ crosses }X}\oplus\text{constant}.
\]

But for every deterministic edge \(e\),

\[
1_{e\text{ crosses }(X\triangle Y)}
=1_{e\text{ crosses }X}\oplus1_{e\text{ crosses }Y}. \tag{3.3}
\]

Therefore the three Bernoulli bits appearing under \(\ell\) are already jointly realized by the single random edge \(E_r\). Every Bernoulli XOR triple necessarily satisfies exactly the four tetrahedron inequalities (3.2). Hence every character facet in Theorem 3.1 holds. The complete H-description then gives the desired four-state XOR coupling. QED.

## 4. Consequence: the first missing obstruction is genuinely higher-order

Theorem 3.2 rules out an entire proof/search architecture. A new six-point colored facet cannot be detected by checking one cut at a time, nor by checking a pair of cuts together with their symmetric difference. All such tests are automatically satisfied once the individual color edge marginals are nonnegative and the already-known one-cut conditions hold.

Therefore any remaining six-point obstruction must use at least one of the following:

1. simultaneous consistency around **at least three independent cuts** (a genuine higher gluing cycle);
2. an equivalent global obstruction in the 52-dimensional kernel of the 90-atom marginal map;
3. a non-cut interaction functional not generated by the parity characters above.

This is the exact failure point of the natural cut-decomposition algorithm. It is stronger than merely observing that a global decomposition has not yet been found.

## 5. Metric and scope

These theorems settle all known cut facets and completely eliminate two-cut/XOR gluing as a source of new facets, but they do not prove that the 85 cut facets plus nonnegativity and affine equations are the full 37-dimensional colored perfect-matching marginal polytope. They also do not produce a source-valid counterexample.

Hence the source-level frozen metric remains

`R_univ >= 3 -> R_univ >= 3` — **NO MOVEMENT**.

This is a complete restricted theorem on the first unresolved six-point rank-`2+2` core, not a solution of Lyons Question 2.8.
