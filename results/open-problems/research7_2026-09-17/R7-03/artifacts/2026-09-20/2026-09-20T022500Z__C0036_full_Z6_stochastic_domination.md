Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — the requested GPT-6/maximum setting is a preference, not authenticated runtime telemetry, so I do not claim it ran.**

# C0036: candidate full two-sided Lyons domination theorem on `Z/6Z`

Date: 2026-09-20 UTC  
Role: C03 / R7-03, native ID `6aabe7be74008191b526b109ee4e9e80`  
Canonical ownership: preserved; C03 is an explicitly complementary progress-first role.  
Status: **CANDIDATE FULL PROOF for the restricted group `Gamma=Z/6Z`; PROVED PARTIAL relative to the full source Conjecture 5.7.**

## 1. Exact source target

The outside source is Russell Lyons, *Determinantal Probability: Basic Properties and Conjectures*, Proc. ICM 2014, arXiv:1406.2707, §5.2, Conjecture 5.7.

Section 5.2 fixes a **sofic group** `Gamma`. Conjecture 5.7 concerns a `Gamma`-equivariant positive contraction

\[
0\le Q\le I\qquad\text{on }\ell^2(\Gamma),
\]

where `Gamma` acts by translation and equivariance means that `Q` commutes with that action. For a `Gamma`-equivariant operator,

\[
\operatorname{tr}_\Gamma(T)=\langle T\delta_e,\delta_e\rangle,
\]

and the Fuglede--Kadison determinant is

\[
\operatorname{FK}_\Gamma(Q)
 =\exp\!\left(\operatorname{tr}_\Gamma\log|Q|\right).
\]

The conjecture asks for stochastic domination on **all increasing events**:

\[
\mathbf P^{\operatorname{FK}_\Gamma(Q)I}
\preccurlyeq \mathbf P^Q
\preccurlyeq
\mathbf P^{I-\operatorname{FK}_\Gamma(I-Q)I},
\tag{1.1}
\]

with both product-density bounds optimal. The source explicitly says this is open even for finite groups. For a finite group of order `N`, the group trace is normalized matrix trace and

\[
\operatorname{FK}_\Gamma(Q)=(\det Q)^{1/N}.
\]

The present note proves (1.1) for the complete restricted case `Gamma=Z/6Z`.

## 2. Inherited result and the new objective

The preceding run proved the lower-product inequality for the last unresolved principal two-point orbit event on `Z/6Z`, namely the event that the configuration contains an adjacent pair of the six-cycle. Its proof introduced a global spectral reflection symmetrization.

The remaining question was whether that reflection method applies to **every** increasing event, which would upgrade an event-level result to full stochastic domination of the entire finite process.

That upgrade is completed here by an exact finite cone certificate.

## 3. Fourier mixture representation

Let `Gamma=Z/6Z`, and let

\[
\lambda=(\lambda_0,\ldots,\lambda_5)\in[0,1]^6
\]

be the Fourier eigenvalues of a circulant positive contraction `Q`. Put

\[
p=(\lambda_0\lambda_1\cdots\lambda_5)^{1/6}
 =\operatorname{FK}_{\Gamma}(Q).
\tag{3.1}
\]

For a frequency set `J subset Z/6Z`, let `P_J` denote the orthogonal projection onto the Fourier modes in `J`. Lyons's spectral-mixture theorem gives

\[
\mathbf P^Q=\mathbb E_\lambda\,\mathbf P^{P_J},
\tag{3.2}
\]

where the frequencies are included independently with

\[
\Pr(j\in J)=\lambda_j.
\]

Thus for any spatial event `E`, if

\[
h_E(J):=\mathbf P^{P_J}(E),
\]

then

\[
H_E(\lambda):=\mathbf P^Q(E)=\mathbb E_\lambda h_E(J).
\tag{3.3}
\]

In particular, `H_E` is multi-affine in the six spectral coordinates.

## 4. Why invariant increasing events suffice

Both `P^Q` and `Ber(p)^{\otimes 6}` are translation invariant. To prove

\[
\operatorname{Ber}(p)^{\otimes6}\preccurlyeq \mathbf P^Q,
\tag{4.1}
\]

it is enough to test translation-invariant increasing functions. Indeed, for any bounded increasing `f`, average it over the six translations:

\[
\bar f(X)=\frac16\sum_{g\in\Gamma}f(gX).
\]

Then `bar f` is increasing and translation invariant, and both invariant measures have the same expectation of `f` and `bar f`.

Any translation-invariant increasing function factors through the finite poset of translation orbits in `2^Gamma`. By the layer-cake decomposition of an isotone function on a finite poset, it is a nonnegative linear combination of indicators of translation-invariant upper sets. Therefore it is enough to test every translation-invariant increasing **event**.

Exact orbit enumeration gives:

\[
\boxed{14\text{ translation orbits and }44\text{ translation-invariant upper sets}.}
\tag{4.2}
\]

The attached exact checker reconstructs these numbers from the group action rather than hard-coding them.

## 5. Reflection symmetrization for a general event

Fix the spectral reflection

\[
\rho(i)=-i\pmod6.
\]

Write

\[
a=\lambda_0,\quad b=\lambda_1,\quad c=\lambda_2,\quad d=\lambda_3,
\quad e=\lambda_4,\quad f=\lambda_5,
\]

and define

\[
x=\sqrt{bf},\qquad y=\sqrt{ce}.
\]

The reflected geometric symmetrization is

\[
S_\rho\lambda=(a,x,y,d,y,x).
\tag{5.1}
\]

Set

\[
A=b+f-2x=(\sqrt b-\sqrt f)^2,
\qquad
B=c+e-2y=(\sqrt c-\sqrt e)^2,
\tag{5.2}
\]

and

\[
W=(b-f)(c-e).
\tag{5.3}
\]

The box constraints imply

\[
0\le A\le(1-x)^2,\qquad 0\le B\le(1-y)^2,
\tag{5.4}
\]

because

\[
(1-b)(1-f)=(1-x)^2-A\ge0
\]

and similarly for `B`. Also

\[
W^2=A(A+4x)B(B+4y).
\tag{5.5}
\]

For every spatial event `E`, the projection laws for `J` and `rho J` are identical: the two Fourier projection kernels are complex conjugates, hence all principal minors, and therefore the entire DPP laws, coincide. Consequently

\[
h_E(J)=h_E(\rho J),
\]

and `H_E` is invariant under the simultaneous spectral reflection

\[
(b,c,e,f)\leftrightarrow(f,e,c,b).
\tag{5.6}
\]

Because `H_E` is multi-affine in `a,d`, the reflection difference

\[
\Delta_E(\lambda):=H_E(\lambda)-H_E(S_\rho\lambda)
\tag{5.7}
\]

is a convex combination of its four corner values at `(a,d) in {0,1}^2`.

At each corner, simultaneous-reflection invariance and multi-affinity force the exact normal form

\[
\boxed{
\Delta=\alpha(x,y)A+\beta(x,y)B+\gamma AB+\eta W,
}
\tag{5.8}
\]

where `alpha,beta` have degree at most two and `gamma,eta` are rational constants. This is not an ansatz: the checker derives it from the invariant multi-affine basis

\[
1,U,V,P,Q,UV,W,QU,PV,PQ,
\]

with `U=b+f`, `V=c+e`, `P=bf=x^2`, `Q=ce=y^2`.

## 6. Positivity lemmas for the corner form

We use four elementary certificates.

### Lemma 6.1 — no `W`, nonnegative mixed coefficient
If `eta=0`, `gamma>=0`, and `alpha,beta>=0` on `[0,1]^2`, then `Delta>=0`.

This is immediate from `A,B>=0`.

### Lemma 6.2 — no `W`, negative mixed coefficient absorbed by the box
Suppose `eta=0`, `gamma<0`, `beta>=0`, and

\[
\alpha+\gamma(1-y)^2\ge0.
\]

Then

\[
\Delta=A(\alpha+\gamma B)+\beta B\ge0
\]

because `B<=(1-y)^2` and `gamma<0`.

### Lemma 6.3 — generic `W` certificate
Let `q=|eta|`. If

\[
\gamma\ge q,
\qquad
\alpha\ge2qy,
\qquad
\beta\ge2qx,
\tag{6.1}
\]

then `Delta>=0`.

**Proof.** Put `T=AB` and `Z=yA+xB`. From AM--GM,

\[
Z\ge2\sqrt{xyT}.
\]

Using (5.5),

\[
|W|^2=T(T+4Z+16xy).
\]

Hence

\[
(T+2Z)^2-|W|^2
=4(Z^2-4xyT)\ge0,
\]

so `T+2Z>=|W|`. Therefore

\[
\Delta
\ge q(T+2Z-|W|)\ge0.
\]

### Lemma 6.4 — three exceptional algebraic families
The finite certificate leaves only three exceptional forms up to exchanging `x` and `y`.

#### Type E49

\[
\alpha=\frac12-\frac y4,
\quad
\beta=\frac12-\frac x4,
\quad
\gamma=\eta=-\frac18.
\]

Thus

\[
8\Delta=(4-2y)A+(4-2x)B-AB-W.
\tag{6.2}
\]

The worst sign is `W=|W|`. Write

\[
r=\sqrt A,\ s=\sqrt{A+4x},\ t=\sqrt B,\ u=\sqrt{B+4y}.
\]

Then `|W|=rstu`, `x=(s^2-r^2)/4`, `y=(u^2-t^2)/4`, and `s,u<=2`. The right side of (6.2), with `W` replaced by `|W|`, becomes

\[
r^2\left(4-\frac{u^2}{2}\right)
+t^2\left(4-\frac{s^2}{2}\right)-rstu.
\]

Twice this expression is nonnegative by AM--GM because

\[
(8-u^2)(8-s^2)\ge s^2u^2
\]

is equivalent to `s^2+u^2<=8`, which follows from `s,u<=2`.

#### Type E59 and its swap
After multiplying by `24`, the worst-sign lower bound is

\[
2a+18b+19T-3|W|,
\qquad
 a=yA,\quad b=xB,\quad T=AB.
\]

Indeed the discarded pieces are `36y(1-y)A` and `20x(1-x)B`, both nonnegative. The square difference is

\[
\begin{aligned}
&(2a+18b+19T)^2-9W^2\\
&\qquad=4\left[(a-9b)^2+88T^2+10Ta+162Tb\right]\ge0.
\end{aligned}
\tag{6.3}
\]

The swapped case is identical.

#### Type E66 and its swap
After multiplying by `24`, the worst-sign lower bound is

\[
2a+18b+11T-3|W|.
\]

Here the discarded coefficient pieces are again nonnegative, using

\[
8+22x-12x^2-18x=4(1-x)(3x+2)\ge0.
\]

Now

\[
\begin{aligned}
&(2a+18b+11T)^2-9W^2\\
&\qquad=4\left[(a-9b)^2+28T^2+2Ta+90Tb\right]\ge0.
\end{aligned}
\tag{6.4}
\]

Again the exchanged form is identical.

This proves all exceptional families.

## 7. Exact exhaustive corner certificate for all 44 invariant upper sets

The accompanying script

`research7_2026-09-17/R7-03/code/2026-09-20T022500Z__z6_full_domination_certificate.py`

performs the following steps using exact symbolic arithmetic:

1. constructs the 14 translation orbits of subsets of `Z/6Z`;
2. constructs the orbit inclusion poset and enumerates all 44 invariant upper sets;
3. constructs the exact normalized six-point Fourier matrix over `Q(sqrt(3),i)`;
4. computes every projection-DPP mass
   \[
   \mathbf P^{P_J}(X)=|\det F[X,J]|^2
   \]
   exactly and verifies it is a nonnegative rational number;
5. computes `h_E(J)` for every invariant upper set `E`;
6. derives all four `(a,d)` reflection corners for each event;
7. derives the normal form (5.8) exactly;
8. certifies every coefficient inequality by exact degree-`(2,2)` Bernstein coefficients on `[0,1]^2`, or matches one of the explicitly proved exceptional forms above.

The executed exact output is

```text
Z6_TRANSLATION_ORBITS=14
Z6_INVARIANT_UPPER_SETS=44
CORNER_CERTIFICATES=176
UNIQUE_CORNER_FORMS=72
W_generic=38
eta0_negative_absorb=22
eta0_positive=110
exception_E49=2
exception_E59=1
exception_E59_swap=1
exception_E66=1
exception_E66_swap=1
ALL_EXACT_CERTIFICATES_PASS
```

Thus for every translation-invariant increasing event `E`,

\[
\boxed{H_E(\lambda)\ge H_E(S_\rho\lambda).}
\tag{7.1}
\]

By cyclic relabeling the same holds for every dihedral reflection.

## 8. Alternating reflections proves the full lower stochastic domination

Let

\[
\rho_0(i)=-i,
\qquad
\rho_1(i)=1-i\pmod6.
\]

For positive eigenvalues put `z_i=log lambda_i`. Geometric reflection symmetrization is the orthogonal projection

\[
z\mapsto\frac{z+\rho_c z}{2}.
\]

Alternating the projections for `rho_0,rho_1` converges to their common fixed space. Since `rho_1 rho_0` is the one-step rotation, the common fixed space consists exactly of constant vectors. The log sum is preserved, so the limit is

\[
(\log p,\ldots,\log p).
\]

Every invariant increasing event probability is nonincreasing under each symmetrization by (7.1). Continuity gives

\[
\mathbf P^Q(E)\ge \mathbf P^{pI}(E)
\]

for every invariant increasing event. Section 4 upgrades this to **every** increasing event. If some eigenvalue vanishes, then `p=0` and the lower product measure is the deterministic empty configuration, so the statement is trivial.

Therefore

\[
\boxed{
\operatorname{Ber}(\operatorname{FK}(Q))^{\otimes6}
\preccurlyeq \mathbf P^Q
\qquad(\Gamma=\mathbb Z/6\mathbb Z).
}
\tag{8.1}
\]

## 9. Upper domination and sharpness

For a finite DPP, complementing the random configuration sends kernel `Q` to `I-Q`. Apply (8.1) to `I-Q`:

\[
\operatorname{Ber}(\operatorname{FK}(I-Q))^{\otimes6}
\preccurlyeq \mathbf P^{I-Q}.
\]

Taking complements reverses the order and yields

\[
\boxed{
\mathbf P^Q
\preccurlyeq
\operatorname{Ber}(1-\operatorname{FK}(I-Q))^{\otimes6}.
}
\tag{9.1}
\]

The lower density is optimal because the full-set event has

\[
\mathbf P^Q(X=\Gamma)=\det Q=\operatorname{FK}(Q)^6.
\]

Any larger Bernoulli density would assign larger probability to that increasing event. The upper density is optimal by the empty-set event, equivalently by applying the same argument to `I-Q`.

Hence the complete restricted theorem is:

### Theorem 9.1
For every `Z/6Z`-equivariant positive contraction `Q` on `ell^2(Z/6Z)`,

\[
\boxed{
\operatorname{Ber}(\operatorname{FK}(Q))^{\otimes6}
\preccurlyeq \mathbf P^Q
\preccurlyeq
\operatorname{Ber}(1-\operatorname{FK}(I-Q))^{\otimes6},
}
\]

and both constants are sharp.

## 10. Honest source status and next bottleneck

This is **not** a full proof of Lyons Conjecture 5.7, whose source quantifies over all source-admissible groups and equivariant positive contractions. It is a candidate full proof for the entire finite group `Z/6Z`, improving the prior event-by-event ledger to full process domination.

The next mathematically meaningful order-six bottleneck is the nonabelian regular group `S_3`. It has more subset orbits than `Z/6Z`, and the cyclic Fourier one-dimensional spectral parametrization is unavailable. The natural next attack is therefore not another cyclic expansion: it is to decompose an `S_3`-equivariant positive contraction into irreducible representation blocks, identify the appropriate reflection/automorphism averaging operation, and test whether the invariant-event cone admits a finite corner certificate analogous to the one above.

Independent review is still required before treating the restricted theorem as externally established. The full-source status remains **PROVED PARTIAL**.
