Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — the requested GPT-6/maximum setting is a preference, not authenticated runtime telemetry, so I do not claim it ran.**

# C0036: a single-gauge-pair stochastic symmetrization theorem and a central generalized-dihedral lift

Date: 2026-09-20 UTC  
Role: C03 / R7-03, native ID `6aabe7be74008191b526b109ee4e9e80`  
Canonical ownership: preserved; this is the explicitly complementary progress-first role registered in `operations/progress_first_2026-09-20/REGISTRY.md`.  
Captured fresh master before this artifact: `b77247874fa28680ca4aa15ff694dd22dd33b763`.  
Previous own full-process milestone: `research7_2026-09-17/R7-03/artifacts/2026-09-20/2026-09-20T022500Z__C0036_full_Z6_stochastic_domination.md`.  
Status: **PROVED PARTIAL relative to the full source; CANDIDATE FULL PROOF for the central `S_3` source class.**

## 1. Exact source target

The source is Russell Lyons, *Determinantal Probability: Basic Properties and Conjectures*, Proc. ICM 2014, arXiv:1406.2707, §5.2, Conjecture 5.7.

Section 5.2 fixes a **sofic group** `Gamma`, with `E=Gamma`. The operator is a `Gamma`-equivariant positive contraction

\[
0\le Q\le I\qquad\text{on }\ell^2(\Gamma),
\]

where equivariance means commuting with the translation action. For a `Gamma`-equivariant operator,

\[
\operatorname{tr}_\Gamma(T)=\langle T\delta_e,\delta_e\rangle,
\qquad
\operatorname{FK}_\Gamma(Q)=\exp\bigl(\operatorname{tr}_\Gamma\log|Q|\bigr).
\]

Writing `P^Q` for the determinantal law, the conjecture is the **full stochastic-domination statement on every increasing event**

\[
\boxed{
\mathbf P^{\operatorname{FK}_\Gamma(Q)I}
\preccurlyeq \mathbf P^Q
\preccurlyeq
\mathbf P^{I-\operatorname{FK}_\Gamma(I-Q)I},
}
\tag{1.1}
\]

with both product densities optimal. For a finite group of order `N`,

\[
\operatorname{FK}_\Gamma(Q)=(\det Q)^{1/N}.
\tag{1.2}
\]

The source explicitly says Conjecture 5.7 is open even for finite groups. Nothing below is represented as a full-source solution.

## 2. Inherited progress and why the method changes here

The immediately preceding R7-03 work obtained a candidate full proof of (1.1) for `Gamma=Z/6Z`, after the earlier arbitrary-pair geometric smoothing route was shown to fail and was replaced by cycle-compatible reflection symmetrization. Earlier R7-03 work also proved an exact subgroup-support lift: if the convolution kernel of an equivariant `Q` is supported in a subgroup `H`, then `P^Q` factors over right cosets of `H`, and the ambient Fuglede--Kadison density equals the subgroup density.

The first nonabelian group of order six is `S_3`. Instead of repeating a six-variable orbit expansion, this note proves a structural stochastic-order lemma that can remove one gauge-swapped spectral pair **at the level of the entire process**. It then combines that lemma with the subgroup-support mechanism to prove the full sharp Lyons bounds for every **central** `S_3`-equivariant contraction. The same argument gives a general central generalized-dihedral lifting theorem.

## 3. A single-gauge-pair theorem for arbitrary finite DPPs

We begin with a statement that does not use a group.

### Theorem 3.1 (single diagonal-gauge eigenpair symmetrization)

Let `E` be a finite ground set and let `D` be a diagonal unitary involution on `ell^2(E)`, so `D^2=I`. Let `Q` be a positive contraction. Assume there is an orthogonal decomposition

\[
\ell^2(E)=W\oplus \operatorname{span}\{u,v\}
\tag{3.1}
\]

such that

1. `W` is `D`-invariant;
2. `Q|_W` commutes with `D|_W`;
3. `u,v` are orthonormal eigenvectors of `Q`, with
   \[
   Qu=au,\qquad Qv=bv,\qquad a,b\in[0,1];
   \]
4. after changing the phase of one vector if necessary,
   \[
   Du=v,\qquad Dv=u.
   \]

Put

\[
g=\sqrt{ab}
\]

and define

\[
\widetilde Q
=Q|_W\oplus g I_{\operatorname{span}\{u,v\}}.
\tag{3.2}
\]

Then

\[
\boxed{\mathbf P^{\widetilde Q}\preccurlyeq \mathbf P^Q.}
\tag{3.3}
\]

Moreover

\[
\det \widetilde Q=\det Q.
\tag{3.4}
\]

#### Proof

Because `Q|_W` and `D|_W` commute and are normal, choose an orthonormal basis `w_1,...,w_m` of `W` consisting simultaneously of `Q`-eigenvectors and `D`-eigenvectors. Let their `Q`-eigenvalues be `lambda_1,...,lambda_m`.

Use the standard spectral-mixture representation of a finite determinantal process: independently retain each `Q`-eigenvector with probability equal to its eigenvalue, and conditional on the retained eigenvectors use the projection DPP onto their span.

Fix any increasing event `A subseteq 2^E`. Condition on an arbitrary retained subset `R subseteq {w_1,...,w_m}` of the `W`-basis. Write

\[
h_{00}=\mathbf P^{P_R}(A),
\]
\[
h_{10}=\mathbf P^{P_R+P_u}(A),\qquad
h_{01}=\mathbf P^{P_R+P_v}(A),
\]
\[
h_{11}=\mathbf P^{P_R+P_u+P_v}(A).
\tag{3.5}
\]

Since projection kernels are ordered when their ranges are nested, the determinantal monotonicity theorem gives

\[
h_{00}\le h_{10}\le h_{11},
\qquad
h_{00}\le h_{01}\le h_{11}.
\tag{3.6}
\]

Also `P_R` commutes with `D`, and

\[
D(P_R+P_u)D=P_R+P_v.
\]

Conjugation of a kernel by a diagonal unitary leaves every principal minor unchanged, hence leaves the entire DPP law unchanged. Therefore

\[
h_{10}=h_{01}=:h_1.
\tag{3.7}
\]

Conditional on `R`, the event probability under `Q` is

\[
F(a,b)
=h_{00}(1-a)(1-b)
+h_1\bigl(a(1-b)+b(1-a)\bigr)
+h_{11}ab.
\tag{3.8}
\]

Under `widetilde Q` it is the same expression with `(a,b)` replaced by `(g,g)`. Since `g^2=ab`, the `h_{11}` coefficients are identical. A direct subtraction gives

\[
\begin{aligned}
F(a,b)-F(g,g)
&=(a+b-2g)(h_1-h_{00})\\
&=(\sqrt a-\sqrt b)^2(h_1-h_{00})\ge0.
\end{aligned}
\tag{3.9}
\]

This holds after conditioning on every `R`; averaging over the independent `W`-mixture proves (3.3) for every increasing event `A`. Finally, the only two changed eigenvalues have product

\[
g^2=ab,
\]

which proves (3.4). `QED`

### Remarks

- The theorem is a **full-process stochastic domination theorem**, not an inclusion-probability comparison.
- It does not require `widetilde Q <= Q` in Loewner order; in general that operator inequality need not hold.
- The key point is that there is exactly one nontrivial gauge-swapped eigenpair. With several simultaneously swapped pairs, the one-pair conditioning identity (3.9) cannot simply be iterated unless the unsmoothed complement remains gauge invariant.

## 4. Central generalized-dihedral lifting

Let `A` be a finite abelian group of odd order and set

\[
\Gamma=\operatorname{Dih}(A)=A\rtimes\{1,s\},
\qquad sas=a^{-1}\quad(a\in A).
\tag{4.1}
\]

Let

\[
\varepsilon:\Gamma\to\{\pm1\}
\]

be the quotient character, equal to `+1` on `A` and `-1` on the reflection coset. Let `D_epsilon` denote multiplication by this character on `ell^2(Gamma)`.

We call a `Gamma`-equivariant convolution operator **central** when its convolution kernel is a class function, equivalently when it is a central element of the finite group algebra.

### Theorem 4.1 (central odd generalized-dihedral lift)

Assume Lyons's lower product bound is valid for every `A`-equivariant positive contraction on `ell^2(A)`. Then for every **central** `Gamma`-equivariant positive contraction `Q`,

\[
\boxed{
\mathbf P^{\operatorname{FK}_\Gamma(Q)I}
\preccurlyeq \mathbf P^Q.
}
\tag{4.2}
\]

If the lower theorem on `A` is available also after replacing a kernel by its complement `I-K` (in particular, if the full two-sided Lyons theorem is known on `A`), then

\[
\boxed{
\mathbf P^{\operatorname{FK}_\Gamma(Q)I}
\preccurlyeq \mathbf P^Q
\preccurlyeq
\mathbf P^{I-\operatorname{FK}_\Gamma(I-Q)I}.
}
\tag{4.3}
\]

Both constants in (4.3) are optimal.

#### Proof

Because `|A|` is odd, the only character `theta` of `A` satisfying `theta=theta^{-1}` is the trivial character. The irreducible representations of `Gamma` are therefore:

1. the trivial one-dimensional representation `1`;
2. the quotient/sign representation `epsilon`;
3. for each unordered pair `{theta,theta^{-1}}` of nontrivial characters of `A`, one two-dimensional induced representation `pi_theta`.

Twisting by `epsilon` interchanges `1` and `epsilon`. Each `pi_theta` is fixed up to equivalence by the twist:

\[
\pi_\theta\otimes\varepsilon\simeq\pi_\theta.
\tag{4.4}
\]

Indeed, in a standard basis one may take

\[
\pi_\theta(a)=
\begin{pmatrix}
\theta(a)&0\\0&\theta(a)^{-1}
\end{pmatrix},
\qquad
\pi_\theta(s)=
\begin{pmatrix}0&1\\1&0\end{pmatrix},
\]

and conjugation by `diag(1,-1)` changes the reflection matrix to its negative while leaving every `pi_theta(a)` unchanged.

Since `Q` is central, Schur's lemma says that `Q` acts by a scalar on each irreducible isotypic component of the regular representation. Write its eigenvalues on the one-dimensional `1` and `epsilon` spaces as

\[
a,b\in[0,1].
\]

Let `W` be the direct sum of all the two-dimensional-isotypic components. Multiplication by `epsilon` swaps the normalized `1`- and `epsilon`-character vectors, preserves `W`, and, because `Q` is scalar on each isotypic component, commutes with `Q|_W`.

Thus Theorem 3.1 applies. Replace `a,b` by

\[
g=\sqrt{ab}
\]

and leave all of `W` unchanged; call the resulting contraction `widetilde Q`. Then

\[
\mathbf P^{\widetilde Q}\preccurlyeq\mathbf P^Q,
\qquad
\det\widetilde Q=\det Q.
\tag{4.5}
\]

Moreover `widetilde Q` now commutes with `D_epsilon`. If `widetilde q` denotes its convolution kernel, then

\[
(D_\varepsilon\widetilde QD_\varepsilon)(x,y)
=\varepsilon(x)\varepsilon(y)\widetilde q(x^{-1}y)
=\varepsilon(x^{-1}y)\widetilde q(x^{-1}y).
\]

Equality with `widetilde Q` implies

\[
\widetilde q(h)=0\qquad(h\notin A).
\tag{4.6}
\]

Hence `widetilde Q` is supported on `A`. The two right cosets of `A` reduce it, the two diagonal blocks are unitarily identical copies of an `A`-equivariant contraction `K`, and therefore

\[
\mathbf P^{\widetilde Q}=\mathbf P^K\otimes\mathbf P^K.
\tag{4.7}
\]

Also

\[
\det\widetilde Q=(\det K)^2.
\]

Since `|Gamma|=2|A|`, (4.5) gives

\[
\operatorname{FK}_\Gamma(Q)
=\operatorname{FK}_\Gamma(\widetilde Q)
=(\det K)^{1/|A|}
=\operatorname{FK}_A(K).
\tag{4.8}
\]

By the assumed lower theorem on `A`,

\[
\operatorname{Ber}(\operatorname{FK}_A(K))^{\otimes A}
\preccurlyeq \mathbf P^K.
\]

Taking the product of the two coset couplings and using (4.7)--(4.8) yields

\[
\operatorname{Ber}(\operatorname{FK}_\Gamma(Q))^{\otimes\Gamma}
\preccurlyeq\mathbf P^{\widetilde Q}
\preccurlyeq\mathbf P^Q,
\]

which proves (4.2).

Apply the same lower result to `I-Q`. Complementation sends `P^{I-Q}` to `P^Q` and reverses stochastic order, which gives the upper inequality in (4.3).

For sharpness, on a finite group the full-set event has probability

\[
\mathbf P^Q(X=\Gamma)=\det Q=\operatorname{FK}_\Gamma(Q)^{|\Gamma|}.
\]

Thus no larger lower product density can be dominated by `P^Q`. Applying the same argument to the empty-set event, equivalently to `I-Q`, proves sharpness of the upper density. `QED`

## 5. Unconditional nonabelian corollary: central `S_3`

Take

\[
A=C_3,
\qquad
\Gamma=\operatorname{Dih}(C_3)\cong S_3.
\]

For completeness, the needed `C_3` lower theorem is elementary and does not require importing the later `Z/5Z` certificate. Translation acts transitively on each cardinality layer of `2^{C_3}`, so after averaging an increasing test over translations it depends only on `|X|`. If the three eigenvalues of a `C_3`-equivariant contraction are `lambda_1,lambda_2,lambda_3` and

\[
p=(\lambda_1\lambda_2\lambda_3)^{1/3},
\]

then the DPP cardinality has the law of

\[
\xi_1+\xi_2+\xi_3,
\qquad
\xi_i\sim\operatorname{Bern}(\lambda_i)
\]

independently. Its three nontrivial upper tails dominate those of `Bin(3,p)`:

- at level `3`, equality holds because `lambda_1 lambda_2 lambda_3=p^3`;
- at level `2`,
  \[
  \Pr(|X|\ge2)=e_2-2p^3\ge3p^2-2p^3
  \]
  by AM--GM on `lambda_1lambda_2`, `lambda_1lambda_3`, `lambda_2lambda_3`;
- at level `1`, generalized Holder gives
  \[
  p+\bigl((1-\lambda_1)(1-\lambda_2)(1-\lambda_3)\bigr)^{1/3}\le1,
  \]
  hence
  \[
  \Pr(|X|\ge1)\ge1-(1-p)^3.
  \]

Thus the sharp lower product domination holds on `C_3`; applying it to the complement gives the upper bound.

Theorem 4.1 therefore yields:

### Corollary 5.1

For every **central** `S_3`-equivariant positive contraction `Q`,

\[
\boxed{
\operatorname{Ber}(\operatorname{FK}_{S_3}(Q))^{\otimes S_3}
\preccurlyeq \mathbf P^Q
\preccurlyeq
\operatorname{Ber}\bigl(1-\operatorname{FK}_{S_3}(I-Q)\bigr)^{\otimes S_3}.
}
\tag{5.1}
\]

Both constants are sharp.

This is a full stochastic-domination statement for an infinite three-parameter family of nonabelian equivariant kernels, not a single finite example and not merely an inclusion-event inequality.

An explicit spectral description makes the mechanism transparent. A central `S_3` convolution operator has eigenvalues

\[
a\quad\text{on the trivial representation},
\qquad
b\quad\text{on the sign representation},
\qquad
c\quad\text{on the four-dimensional standard isotypic component}.
\]

Thus

\[
\det Q=ab c^4,
\qquad
\operatorname{FK}_{S_3}(Q)=(ab c^4)^{1/6}.
\]

The single-pair theorem replaces `(a,b)` by `(sqrt(ab),sqrt(ab))`; the standard eigenvalue `c` is untouched. Equality of the trivial and sign eigenvalues kills the transposition-coset coefficient, leaving two identical `C_3` blocks with Fourier eigenvalues

\[
\sqrt{ab},\ c,\ c.
\]

Their common subgroup FK density is

\[
(\sqrt{ab}\,c^2)^{1/3}=(ab c^4)^{1/6},
\]

exactly the original ambient density.

## 6. A broader corollary already available inside the R7-03 package

Theorem 4.1 is not specific to `S_3`. It says:

\[
\boxed{
\text{full Lyons on odd abelian }A
\Longrightarrow
\text{full Lyons for central kernels on }\operatorname{Dih}(A).
}
\tag{6.1}
\]

The current R7-03 package contains a written candidate full theorem for `A=C_5`. Consequently the same argument gives a **conditional-on-that-inherited-candidate** full theorem for every central contraction on the nonabelian dihedral group of order ten. This corollary should inherit the verification label of the `C_5` theorem; it is not promoted here to independently audited status.

## 7. What remains for arbitrary `S_3`: one operator-geometric midpoint statement

The centrality restriction can be isolated exactly. Let `H=A_3=C_3` and let `D` be multiplication by the sign character. In an `H`-Fourier basis an arbitrary `S_3`-equivariant Hermitian convolution operator has the three paired blocks

\[
Q_0=
\begin{pmatrix}a_0&z_0\\ z_0&a_0\end{pmatrix},
\qquad
Q_1=
\begin{pmatrix}a_1&z\\ \bar z&a_2\end{pmatrix},
\qquad
Q_2=
\begin{pmatrix}a_2&\bar z\\ z&a_1\end{pmatrix}.
\tag{7.1}
\]

The sign gauge changes each off-diagonal entry to its negative. For positive definite interior points, the Kubo--Ando geometric midpoint

\[
G:=Q\#(DQD)
\tag{7.2}
\]

is `H`-supported and has blocks

\[
G_0=\sqrt{a_0^2-z_0^2}\,I_2,
\tag{7.3}
\]

and, writing

\[
r=\sqrt{1-\frac{|z|^2}{a_1a_2}},
\]

\[
G_1=\operatorname{diag}(a_1r,a_2r),
\qquad
G_2=\operatorname{diag}(a_2r,a_1r).
\tag{7.4}
\]

The two `H`-coset blocks are therefore inversion-conjugate `C_3` kernels and have the same determinant. Also

\[
\det G=\det Q.
\tag{7.5}
\]

Hence the following single statement would close **all** of `S_3`:

\[
\boxed{
\mathbf P^{Q\#(DQD)}\preccurlyeq\mathbf P^Q
\quad\text{for every }S_3\text{-equivariant positive contraction }Q.
}
\tag{7.6}
\]

Indeed, once (7.6) holds, the already proved `C_3` theorem applies independently on the two cosets of `G`, with the same FK density as `Q`, and transitivity gives the full lower product bound. Complementation then gives the full upper bound.

There is meaningful evidence short of (7.6), but it must not be mislabeled as stochastic domination. The operator geometric mean obeys the compression inequality

\[
P_S(A\#B)P_S
\le
(P_SAP_S)\#(P_SBP_S)
\]

for a coordinate compression. Taking `A=Q`, `B=DQD` and determinants gives, for every `S subseteq S_3`,

\[
\det G_S
\le
\sqrt{\det Q_S\det(D_SQ_SD_S)}
=\det Q_S.
\tag{7.7}
\]

Thus **every principal inclusion event** is ordered in the desired direction. But principal-inclusion inequalities do not by themselves imply full stochastic domination, because a general upper-set indicator has an inclusion--exclusion expansion with mixed signs. Therefore (7.7) is recorded only as a reduction/consistency check, not as closure.

The next attack should target (7.6) directly, using the three-block form (7.1)--(7.4), rather than reverting to another cardinality calculation or another local Hessian expansion.

## 8. Obligation ledger

Full-source metric: **UNCHANGED**. Conjecture 5.7 still quantifies over arbitrary source-admissible sofic groups and arbitrary equivariant positive contractions.

New mathematical obligations/results in this run:

- `single diagonal-gauge eigenpair full-process symmetrization`: **PROVED**;
- `central odd generalized-dihedral lift from the abelian subgroup theorem`: **PROVED**;
- `central S_3 full sharp two-sided Lyons domination`: **CANDIDATE FULL PROOF for this restricted source class**;
- `arbitrary S_3`: **OPEN in this work**, reduced to the explicit midpoint stochastic-order statement (7.6);
- `all-group C0036`: **PROVED PARTIAL only**.

No independent P26/OTHER audit is claimed here. The mathematics should continue while such review follows.