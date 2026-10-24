SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account04, slot B10, 2026-09-24T10:15:10Z.

# account04/B10 r2 — product-projection sectional obstruction and fresh-longitudinal payment

Programme: \`QFORM-DENSITY-3EIG-20260922\`  
Run: \`20260924T101510Z-account04-B10-QFORM-r2\`  
Status: **ESSENTIAL_STEP_APPLIED / NEW PRODUCT-PROJECTION COUNTEREXAMPLE TO THE PROPOSED SECTIONAL INTERFACE / NEW FRESH-LONGITUDINAL DENSITY PAYMENT / FULL QFORM OPEN**.

The target remains independent ORIGINAL real coordinates with probability densities at most one and an arbitrary real symmetric coefficient matrix having at least three eigenvalues of modulus at least one. No moment, support, log-concavity, iid, post-rotation independence, arbitrary-joint coarea, conditional-density cap, or coefficient deletion is used. Continuity is separate.

## 1. Source boundary

The newest designated partner used here is account01/B10 at

\`yspennstate/math-open-problems@1439f3ecb30a49b8363552d780159306f4b9c56f\`.

Its theorem \`QFORM-PARABOLIC-PULLBACK-SECTIONAL-RECEIVER-v1\` treats

\[
Q=2(sH+aZ)L+V^2,
\]

where \(H\) is independent of \((Z,L,V)\), by the quantity

\[
M_R(\varrho)
=\int_{0<|\ell|\le R}|\ell|^{-3/4}
 \int_{\mathbb R}\left(\int_{\mathbb R}
 \varrho(z,\ell,v)^2\,dv\right)^{1/2}dz\,d\ell.
\]

It proves

\[
\|p_Q\|_\infty
\le 2^{-1/4}K_H^{3/4}s^{-3/4}M_R(\varrho)
   +\frac{K_H}{2sR}.
\tag{1.1}
\]

Its exact-null corollary proves that, when the longitudinal \(Z\)-term is absent before estimation and \((L,V)\) has joint-density cap \(K_2\) and \(L\)-marginal cap \(K_L\),

\[
\|p_Q\|_\infty
\le 5\,2^{2/5}K_H^{4/5}s^{-4/5}(K_2K_L)^{2/5}.
\tag{1.2}
\]

The harmonic target-valid near-coloop normal form comes from account02/B10 at

\`yspennstate/math-open-problems@174f2ac95a7e63dc88172bc6fcf5b319e8613d44\`:

\[
Q=2(\sqrt c\,H+\sqrt\rho\,Z)L+V^2,
\qquad 0<\rho<1/64,\quad c=1-\rho,
\tag{1.3}
\]

where \((Z,L,V)\) are orthogonal linear forms of the SAME leaf product bank. The majority-sign levels are already bounded there; the shared-bank minority/two-sheet side remains open.

## 2. The proposed product-projection sectional estimate is false

### Theorem 2.1 — \`QFORM-PRODUCT-PROJECTION-SECTIONAL-COUNTEREXAMPLE-v1\`

For every integer \(N\ge1\), there are three independent ORIGINAL random variables \(X_N,Y_N,W\), each with a probability density bounded by one, and an orthonormal triple

\[
Z=\frac{X_N+Y_N}{\sqrt2},\qquad
V=\frac{X_N-Y_N}{\sqrt2},\qquad
L=W,
\tag{2.1}
\]

whose joint density \(\varrho_N\) satisfies

\[
\boxed{M_1(\varrho_N)\ge 2^{5/4}\sqrt N.}
\tag{2.2}
\]

Consequently no dimension-free estimate \(M_1(\varrho)\le C\) can hold for all orthonormal three-dimensional projections of cap-one product laws. This is a counterexample to the proposed proof interface, not to the QFORM conjecture.

### Proof

Put \(\delta=1/N\). Choose pairwise disjoint intervals \(I_i,J_j\), \(1\le i,j\le N\), each of length \(\delta\), so far apart that all \(N^2\) intervals

\[
\frac{I_i+J_j}{\sqrt2}
\]

are disjoint. For example, take their centers at \(4^i\) and \(4^{N+j}\). Let

\[
f_N=\mathbf1_{\cup_i I_i},\qquad
g_N=\mathbf1_{\cup_j J_j},\qquad
h=\mathbf1_{(0,1)}.
\tag{2.3}
\]

Each is a normalized probability density capped by one. Take \(X_N,Y_N,W\) independent with these densities.

The map \((x,y)\mapsto(z,v)=((x+y)/\sqrt2,(x-y)/\sqrt2)\) is orthogonal, so the \((Z,V)\)-density is the indicator of \(N^2\) rotated \(\delta\)-squares. Write \(z_{ij}\) for the \(z\)-center of the square from \(I_i\times J_j\). In coordinates \(s=z-z_{ij}\), \(t=v-v_{ij}\), that square is

\[
|s|+|t|\le\frac{\delta}{\sqrt2}.
\tag{2.4}
\]

For

\[
|s|\le\frac{\delta}{2\sqrt2},
\]

the \(v\)-section therefore has length at least \(\delta/\sqrt2\). Because the \(z\)-projections of the \(N^2\) squares are disjoint,

\[
\begin{aligned}
\int_{\mathbb R}
 \left(\int_{\mathbb R}p_{Z,V}(z,v)^2\,dv\right)^{1/2}dz
&\ge N^2\frac{\delta}{\sqrt2}
       \left(\frac{\delta}{\sqrt2}\right)^{1/2}\\
&=\frac{\sqrt N}{2^{3/4}}.
\end{aligned}
\tag{2.5}
\]

Since \(L=W\) has density \(\mathbf1_{(0,1)}\) and is independent of \((Z,V)\),

\[
M_1(\varrho_N)
= \left(\int_0^1\ell^{-3/4}\,d\ell\right)
  \int_{\mathbb R}\|p_{Z,V}(z,\cdot)\|_2\,dz
\ge 4\frac{\sqrt N}{2^{3/4}}
=2^{5/4}\sqrt N.
\]

This proves (2.2). The coefficient vectors in (2.1) are literally orthonormal in the original three-coordinate product space; no post-rotation independence is asserted or needed. QED.

## 3. What survives: a fresh-longitudinal theorem

The failure above comes from integrating an irrelevant fragmented \(Z\)-direction in the exact-null limit. If the longitudinal direction is genuinely fresh, it can be convolved with the hub before invoking the account01/B10 exact-null theorem.

### Theorem 3.1 — \`QFORM-FRESH-LONGITUDINAL-PARABOLIC-PAYMENT-v1\`

Let \(H,Y\) be independent ORIGINAL cap-one variables, independent of a leaf product bank. Let \((L,V)\) be an orthonormal two-dimensional projection of that disjoint leaf bank. For \(s>0\) and arbitrary \(a\in\mathbb R\), set

\[
Q=2(sH+aY)L+V^2.
\tag{3.1}
\]

Then \(Q\) has an essentially bounded density and

\[
\boxed{
\|p_Q\|_\infty
\le 10\,\min\{s^{-1},|a|^{-1}\}^{4/5}
}
\tag{3.2}
\]

when \(a\ne0\), while for all \(a\), including \(a=0\),

\[
\boxed{\|p_Q\|_\infty\le10s^{-4/5}.}
\tag{3.3}
\]

In particular, if \(s=\sqrt c\) and \(c>63/64\),

\[
\boxed{
\|p_Q\|_\infty
<10(64/63)^{2/5}<10.064.
}
\tag{3.4}
\]

### Proof

Put \(T=sH+aY\). It is independent of \((L,V)\). Its density is the convolution of the scaled densities, hence

\[
\|p_T\|_\infty
\le s^{-1},
\qquad
\|p_T\|_\infty\le |a|^{-1}\quad(a\ne0).
\tag{3.5}
\]

Apply the exact-null corollary (1.2) with the independent hub variable \(T\), coefficient \(s_{\rm new}=1\), and \(K_H=\|p_T\|_\infty\). The source-valid projection bounds are

\[
K_L\le\sqrt2,\qquad K_2\le2.
\tag{3.6}
\]

Thus

\[
5\,2^{2/5}K_H^{4/5}(K_2K_L)^{2/5}
\le 10K_H^{4/5},
\tag{3.7}
\]

which gives (3.2)-(3.3). QED.

This is a full-law bound on its exact separated-bank scope. It does not apply to (1.3), because there \(Z,L,V\) come from the same leaf bank.

## 4. Corrected proof frontier

Theorem 2.1 rules out the proposed next step

\[
\text{product projection}\Longrightarrow M_1(\varrho)\le C.
\]

Therefore (1.1) cannot close the shared-bank harmonic survivor through an \(a\)-uniform sectional estimate. Theorem 3.1 shows that the same parabolic receiver completely pays the fresh-longitudinal branch, so the remaining obstruction is genuinely the shared-bank dependence.

Any successful continuation must retain the nonzero longitudinal modulation \(aZL\) instead of estimating uniformly in \(a\). A corrected interface must do at least one of the following:

1. exploit cancellation or mixing in \(z\) proportional to \(|a\ell|\);
2. quotient out the \(z\)-direction continuously as \(a\to0\), reverting to the two-dimensional exact-null theorem without paying its fragmentation;
3. use a two-copy product-source inequality in which the \(z\)-fragmentation is charged against the nonzero modulation.

The one-sided ruled estimate remains applicable only to its majority-sign levels. It is not a solution of the minority/two-sheet side.

## 5. Status

- Product-projection sectional \(M_1\) conjecture: **DISPROVED**, even for a literal orthonormal projection of three independent cap-one variables.
- Fresh-longitudinal parabolic branch: **PROVED**, with \(\|p_Q\|_\infty<10.064\) at the live near-coloop scale.
- Shared-bank harmonic minority/two-sheet branch: **OPEN**.
- Arbitrary exact rank-three coupled case: **OPEN**.
- Full QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.
- Continuity: not claimed by the new essential-density payment.

Source pins: Claude refreshed source \`b0cbc2233369b6a3f366cf569d425f485f123e1c\`; account01/B10 \`1439f3ecb30a49b8363552d780159306f4b9c56f\`; account02/B10 \`174f2ac95a7e63dc88172bc6fcf5b319e8613d44\`; brain login commit \`5bea9d3820e4745549aa1b7f1e0999d9b775178d\`.

Repository publication is transport, not verified native ingestion.
