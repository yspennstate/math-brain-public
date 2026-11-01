Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — the requested GPT-6/maximum setting is a preference, not authenticated runtime telemetry, so I do not claim it ran.**

# C0036: arbitrary-`S_3` coset-factor domination and an exact obstruction to the Shapley-product route

Date: 2026-09-20 UTC  
Role: C03 / R7-03, native ID `6aabe7be74008191b526b109ee4e9e80`  
Canonical ownership: preserved; this is the explicitly complementary progress-first role registered in `operations/progress_first_2026-09-20/REGISTRY.md`.  
Status: **PROVED PARTIAL** relative to Lyons Conjecture 5.7. The arbitrary-`S_3` factor theorem below is proved analytically here, but it is not a full-process proof and has not yet received independent review.

## 1. Exact outside source target

Russell Lyons, *Determinantal Probability: Basic Properties and Conjectures*, Proc. ICM 2014, arXiv:1406.2707, Section 5.2, Conjecture 5.7.

Section 5.2 fixes a **sofic group** `Gamma`. The conjecture ranges over every `Gamma`-equivariant positive contraction

\[
0\le Q\le I\qquad\text{on }\ell^2(\Gamma),
\]

with

\[
\operatorname{tr}_\Gamma(T)=\langle T\delta_e,\delta_e\rangle,
\qquad
\operatorname{FK}_\Gamma(Q)=\exp\!\bigl(\operatorname{tr}_\Gamma\log|Q|\bigr),
\]

and asks for the sharp stochastic domination on **every increasing event**

\[
\mathbf P^{\operatorname{FK}_\Gamma(Q)I}
\preccurlyeq \mathbf P^Q
\preccurlyeq
\mathbf P^{I-\operatorname{FK}_\Gamma(I-Q)I}.
\tag{1.1}
\]

For finite `Gamma` of order `n`,

\[
\operatorname{FK}_\Gamma(Q)=(\det Q)^{1/n}.
\tag{1.2}
\]

The source states that the conjecture is open even for finite groups. A bounded fresh source check this run recovered arXiv:1406.2707. No absence claim from a bounded search is treated as a proof of worldwide openness.

The preceding R7-03 checkpoint proved a globally monotone determinant-preserving Schur-compensated path and then proposed a second route: average the product lower bounds obtained from all Schur-pivot orders, and try to dominate the uniform product law by a Shapley/generalized-permutahedron Jensen argument. This run first tests that candidate lemma exactly. It is false. I then change method in the same run and prove a new arbitrary-`S_3` quotient-factor theorem.

## 2. Exact counterexample to the proposed Shapley-product lemma

The failed candidate statement was:

> If `g(S)=log det Q_S` is the submodular principal-minor function, `x^pi` are its greedy vectors, and `p=(det Q)^(1/n)`, then the uniform mixture of product Bernoulli laws with parameters `exp(x^pi)` should stochastically dominate `Ber(p)^n` on all increasing events.

It is already false for a strict `C_4`-equivariant contraction.

Let `Q` be the Hermitian circulant `4 x 4` matrix

\[
Q=\frac1{1040}
\begin{pmatrix}
841&-87i&-9&87i\\
87i&841&-87i&-9\\
-9&87i&841&-87i\\
-87i&-9&87i&841
\end{pmatrix}.
\tag{2.1}
\]

Its Fourier eigenvalues are exactly

\[
\frac45,\qquad \frac{13}{20},\qquad \frac45,\qquad \frac{64}{65},
\tag{2.2}
\]

so `0<Q<I` and

\[
\det Q=\left(\frac45\right)^4,
\qquad p=(\det Q)^{1/4}=\frac45.
\tag{2.3}
\]

For each permutation `pi=(pi_1,...,pi_4)`, define the Schur-pivot parameters

\[
d_{\pi_j}^{\pi}
=\frac{\det Q_{\{\pi_1,\ldots,\pi_j\}}}
       {\det Q_{\{\pi_1,\ldots,\pi_{j-1}\}}},
\tag{2.4}
\]

and let

\[
\nu_Q=\frac1{24}\sum_{\pi\in S_4}
\bigotimes_{j=1}^4\operatorname{Ber}(d_j^\pi).
\tag{2.5}
\]

Consider the `C_4`-invariant increasing event

\[
\mathcal E=\{X:\ X\text{ contains at least one edge of the four-cycle}\}.
\tag{2.6}
\]

Exact rational evaluation of all 24 product laws gives

\[
\boxed{
\nu_Q(\mathcal E)
=\frac{3601344031929}{3907727525000}.
}
\tag{2.7}
\]

For the uniform comparator,

\[
\operatorname{Ber}(4/5)^{\otimes4}(\mathcal E)
=\frac{576}{625}.
\tag{2.8}
\]

The exact difference is

\[
\boxed{
\nu_Q(\mathcal E)-\operatorname{Ber}(4/5)^{\otimes4}(\mathcal E)
=-\frac{17655111}{3907727525000}<0.
}
\tag{2.9}
\]

Thus the Shapley-product lemma is **refuted even inside the actual determinantal principal-minor class and even for a transitive cyclic kernel**. The previous edgewise log-convexity observation is therefore insufficient for a Jensen theorem at the generalized-permutahedron barycenter. Principal-inclusion inequalities remain true, but they cannot be promoted to full stochastic domination through this route.

This is a proof-strategy obstruction, not a counterexample to Lyons: every individual pivot product law remains below `P^Q`; only their mixture fails to dominate the desired uniform product comparator on (2.6).

## 3. Change of method: arbitrary `S_3` and the two `A_3` cosets

Let

\[
S_3=\langle r,s:r^3=s^2=1,\ srs=r^{-1}\rangle,
\qquad H=A_3=\{e,r,r^2\}.
\]

The two left cosets are `H` and `sH`. In the `H`-Fourier decomposition an arbitrary Hermitian `S_3`-equivariant contraction has blocks

\[
Q_0=\begin{pmatrix}a_0&z_0\\z_0&a_0\end{pmatrix},
\qquad
Q_1=\begin{pmatrix}a_1&z\\\bar z&a_2\end{pmatrix},
\qquad
Q_2=\begin{pmatrix}a_2&\bar z\\z&a_1\end{pmatrix},
\tag{3.1}
\]

where `z_0` is real. Put

\[
r^2:=|z|^2,
\qquad
x:=\sqrt{a_0^2-z_0^2},
\qquad
d:=a_1a_2-r^2.
\tag{3.2}
\]

Positivity of `Q` and `I-Q` gives

\[
0\le x\le a_0\le1,
\tag{3.3}
\]

\[
0\le d\le a_1a_2,
\tag{3.4}
\]

and

\[
1-2a_0+x^2=(1-a_0)^2-z_0^2\ge0,
\tag{3.5}
\]

\[
e:=(1-a_1)(1-a_2)-r^2
=1-(a_1+a_2)+d\ge0.
\tag{3.6}
\]

The determinant factors are

\[
\det Q=x^2d^2,
\qquad
p:=(\det Q)^{1/6}=(xd)^{1/3},
\tag{3.7}
\]

and

\[
\det(I-Q)=(1-2a_0+x^2)e^2.
\tag{3.8}
\]

The restriction of the spatial kernel to either `A_3` coset has Fourier eigenvalues `a_0,a_1,a_2`. Therefore, with

\[
v:=(1-a_0)(1-a_1)(1-a_2),
\tag{3.9}
\]

one has

\[
\mathbf P^Q(X\cap H=\varnothing)
=\mathbf P^Q(X\cap sH=\varnothing)=v.
\tag{3.10}
\]

## 4. New theorem: the `A_3`-coset hit factor satisfies the sharp Lyons lower comparison

Define the two hit indicators

\[
Z_H:=\mathbf 1\{X\cap H\ne\varnothing\},
\qquad
Z_{sH}:=\mathbf 1\{X\cap sH\ne\varnothing\},
\tag{4.1}
\]

for `X~P^Q`, and set

\[
h:=1-(1-p)^3.
\tag{4.2}
\]

### Theorem 4.1
For **every** `S_3`-equivariant positive contraction `Q`, with no mean-zero, centrality, hidden-cyclic, or small-neighborhood assumption,

\[
\boxed{
\operatorname{Ber}(h)^{\otimes2}
\preccurlyeq
\mathcal L(Z_H,Z_{sH}).
}
\tag{4.3}
\]

Equivalently, every increasing event that depends only on which of the two `A_3` cosets are hit satisfies the sharp lower Lyons comparison obtained by projecting `Ber(p)^{\otimes6}` to those two hit bits.

The nontrivial event in (4.3) is the simultaneous-hit event

\[
\mathcal U_\times
:=\{X:X\cap H\ne\varnothing,\ X\cap sH\ne\varnothing\}.
\tag{4.4}
\]

For it,

\[
\boxed{
\mathbf P^Q(\mathcal U_\times)
\ge
\bigl[1-(1-p)^3\bigr]^2.
}
\tag{4.5}
\]

This closes one of the genuinely cross-coset invariant-event obligations for arbitrary `S_3`; it is not merely a principal inclusion inequality.

## 5. Proof of the simultaneous-hit inequality

By inclusion-exclusion and (3.8)--(3.10),

\[
\mathbf P^Q(\mathcal U_\times)
=1-2(1-a_0)(1-a_1)(1-a_2)
 +(1-2a_0+x^2)e^2.
\tag{5.1}
\]

We minimize the left side while keeping `x` and `d`, and therefore `p`, fixed.

### Step 1: balance `a_1,a_2`

Put

\[
s_1:=a_1+a_2,\qquad A:=a_1a_2.
\]

Then

\[
e=1-s_1+d
\]

is independent of `A`, while the only other occurrence of `A` in (5.1) is

\[
-2(1-a_0)(1-s_1+A).
\]

Thus (5.1) decreases as `A` increases. For fixed sum `s_1`, feasibility gives

\[
A\le \frac{s_1^2}{4},
\]

and replacing `A` by `s_1^2/4` preserves the constraints `d<=A` and `e>=0`. Hence the minimum occurs at

\[
a_1=a_2=:y=\frac{s_1}{2}.
\tag{5.2}
\]

Now

\[
0\le y\le1,
\qquad d\le y^2,
\qquad e=1-2y+d\ge0.
\tag{5.3}
\]

### Step 2: remove the quotient coupling

At fixed `x,d,y`, define `c=1-a_0`. The derivative of (5.1) with respect to `a_0` is

\[
2(1-y)^2-2e^2.
\tag{5.4}
\]

Because `d<=y^2<=y`,

\[
0\le e=1-2y+d\le1-y.
\tag{5.5}
\]

Therefore (5.4) is nonnegative. Since `x<=a_0`, the minimum occurs at

\[
a_0=x,
\tag{5.6}
\]

which is exactly `z_0=0` for the minimizing comparison point. Formula (5.1) becomes

\[
F(y)=1-2(1-x)(1-y)^2
 +(1-x)^2(1-2y+d)^2.
\tag{5.7}
\]

### Step 3: remove the standard-sector coupling

At fixed `x,d`, differentiating (5.7) gives

\[
F'(y)
=4(1-x)\Big[(1-y)-(1-x)(1-2y+d)\Big].
\tag{5.8}
\]

By (5.5) and `0<=1-x<=1`, the bracket is nonnegative. Hence `F` increases with `y`.

The constraint `d<=y^2` gives `y>=sqrt(d)`, and at the endpoint

\[
y=\sqrt d
\tag{5.9}
\]

the standard coupling vanishes as well. Therefore

\[
\mathbf P^Q(\mathcal U_\times)
\ge
\left[1-(1-x)(1-\sqrt d)^2\right]^2.
\tag{5.10}
\]

### Step 4: the final scalar inequality is Holder

Since

\[
p=(xd)^{1/3}=(x(\sqrt d)^2)^{1/3},
\]

generalized Holder applied to the two triples

\[
(x,\sqrt d,\sqrt d),
\qquad
(1-x,1-\sqrt d,1-\sqrt d)
\]

gives

\[
(xd)^{1/3}
+igl((1-x)(1-\sqrt d)^2\bigr)^{1/3}
\le1.
\tag{5.11}
\]

Thus

\[
(1-x)(1-\sqrt d)^2\le(1-p)^3.
\tag{5.12}
\]

Substituting into (5.10) proves (4.5).

Boundary cases follow directly by continuity.

## 6. Finish the full two-bit stochastic domination

There are only four nontrivial increasing event types on two bits: each coordinate event, their union, and their intersection.

For one coset,

\[
\mathbf P^Q(Z_H=0)=v.
\]

Since

\[
p^3=xd\le a_0a_1a_2,
\]
Holder gives

\[
(a_0a_1a_2)^{1/3}
+\bigl((1-a_0)(1-a_1)(1-a_2)\bigr)^{1/3}
\le1,
\]
so

\[
v\le(1-p)^3.
\tag{6.1}
\]

Hence each coordinate satisfies

\[
\mathbf P^Q(Z_H=1)\ge h,
\qquad
\mathbf P^Q(Z_{sH}=1)\ge h.
\tag{6.2}
\]

For the union event,

\[
\mathbf P^Q(Z_H\vee Z_{sH}=1)=1-\det(I-Q).
\tag{6.3}
\]

If `lambda_1,...,lambda_6` are the eigenvalues of `Q`, then generalized Holder gives

\[
\left(\prod_i\lambda_i\right)^{1/6}
+\left(\prod_i(1-\lambda_i)\right)^{1/6}
\le1.
\tag{6.4}
\]

Thus

\[
\det(I-Q)\le(1-p)^6,
\tag{6.5}
\]

which is exactly the union inequality for `Ber(h)^2`, because `1-h=(1-p)^3`.

The intersection inequality is (4.5). Hence (4.3) follows.

## 7. Dual upper theorem for complete-coset indicators

Let

\[
r_*:=(\det(I-Q))^{1/6},
\qquad q:=1-r_*.
\tag{7.1}
\]

Define the complete-coset indicators

\[
W_H:=\mathbf 1\{H\subseteq X\},
\qquad
W_{sH}:=\mathbf 1\{sH\subseteq X\}.
\tag{7.2}
\]

The complement of a `P^Q` configuration has DPP law `P^{I-Q}`. Applying Theorem 4.1 to `I-Q` says that the two vacancy-hit indicators dominate independent Bernoulli variables of density

\[
1-(1-r_*)^3=1-q^3.
\]

Complementing these two bits reverses stochastic order. Therefore

\[
\boxed{
\mathcal L(W_H,W_{sH})
\preccurlyeq
\operatorname{Ber}(q^3)^{\otimes2}.
}
\tag{7.3}
\]

In particular the increasing event that at least one `A_3` coset is completely occupied satisfies the exact upper Lyons comparator:

\[
\mathbf P^Q(H\subseteq X\ \text{or}\ sH\subseteq X)
\le 2q^3-q^6.
\tag{7.4}
\]

Thus the same argument closes a nontrivial upper-side orbit obligation as well.

## 8. What this changes and what remains open

The run has two substantive outcomes.

1. The random-order/Shapley-product route is dead in its proposed form. The exact `C_4` counterexample (2.1)--(2.9) shows that no generalized-permutahedron Jensen theorem of the required strength can follow merely from edgewise log-convexity plus the greedy-vector barycenter.

2. For **arbitrary `S_3`**, without any spectral-face restriction, the sharp Lyons lower comparison is now proved after projecting the process to the two indicators recording whether the `A_3` cosets are hit. By complement duality, the sharp upper comparison is also proved after projecting to the two indicators recording whether those cosets are completely occupied.

This is still not stochastic domination of the full six-point process. Events sensitive to the detailed pattern inside a hit coset remain unresolved. Therefore arbitrary `S_3` and full C0036 remain **PROVED PARTIAL**, not solved.

## 9. Next attack

Do not return to the refuted Shapley-product lemma. The next structural target is the full two-coset **count vector**

\[
\bigl(|X\cap H|,|X\cap sH|\bigr)\in\{0,1,2,3\}^2.
\]

Prove, or sharply delimit, stochastic comparison of this count vector against two independent `Bin(3,p)` variables. The theorem above establishes the extreme hit/full threshold faces of that `4 x 4` count lattice. The compensated-Schur identity from the preceding checkpoint gives an exact positive conditional correction for the remaining middle-count events. A count-vector theorem would close every increasing event depending only on the two coset counts and would cover a genuinely larger collection of the 76 invariant upper sets before returning to orientation-sensitive within-coset patterns.
