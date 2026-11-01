Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — the requested GPT-6/maximum setting is a preference, not authenticated runtime telemetry, so I do not claim it ran.**

# C0036: exact reflection symmetrization closes the `Z/6Z` adjacent-pair lower bound

Date: 2026-09-20 UTC  
Role: C03 / R7-03, native ID `6aabe7be74008191b526b109ee4e9e80`  
Source: Russell Lyons, *Determinantal Probability: Basic Properties and Conjectures* (ICM 2014), arXiv:1406.2707, §5.2, Conjecture 5.7.  
Status: **PROVED PARTIAL** relative to the full all-sofic-group/all-equivariant-positive-contraction conjecture. This note proves the previously missing `Z/6Z` adjacent-pair lower event inequality; it does **not** by itself prove full stochastic domination on `Z/6Z` for all increasing events.

## 1. Exact source target

Section 5.2 takes a sofic group `Gamma` and a `Gamma`-equivariant positive contraction

\[
0\le Q\le I\qquad\text{on }\ell^2(\Gamma).
\]

For a `Gamma`-equivariant operator,

\[
\operatorname{tr}_\Gamma(T)=\langle T\delta_e,\delta_e\rangle,
\]

and Lyons defines

\[
\operatorname{FK}_\Gamma(Q)=\exp\!\left(\operatorname{tr}_\Gamma\log|Q|\right).
\]

Conjecture 5.7 asks for stochastic domination on **all increasing events**:

\[
\operatorname{Ber}(\operatorname{FK}_\Gamma(Q))^{\otimes\Gamma}
\preccurlyeq P^Q
\preccurlyeq
\operatorname{Ber}\!\left(1-\operatorname{FK}_\Gamma(I-Q)\right)^{\otimes\Gamma},
\]

with the constants optimal. For finite `Gamma`, `tr_Gamma` is normalized matrix trace, so `FK_Gamma(Q)=(det Q)^{1/|Gamma|}`.

## 2. Inherited `Z/6Z` spectral-mixture reduction

Take `Gamma=Z/6Z`, and let the Fourier eigenvalues of the circulant contraction `Q` be

\[
\lambda_0,\ldots,\lambda_5\in[0,1],\qquad
p=(\lambda_0\cdots\lambda_5)^{1/6}.
\]

Let

\[
U_{\rm adj}=\{X\subseteq Z/6Z: X\text{ contains an adjacent pair of the six-cycle}\},
\]

and let `I=U_adj^c` be the independent-set event of `C_6`.

The prior R7-03 spectral-mixture calculation gives

\[
P^Q(I)=F(\lambda):=\mathbb E_\lambda f(J),
\]

where `J` includes each frequency independently with probability `lambda_j`, and the projection-DPP statistic `f` is exactly

\[
f(J)=1\quad(|J|\le1),\qquad f(J)=0\quad(|J|\ge4),
\]

for `|J|=2`,

\[
f(J)=\begin{cases}
5/6,&\text{frequency distance }1,\\
1/2,&\text{frequency distance }2,\\
1/3,&\text{frequency distance }3,
\end{cases}
\]

and for `|J|=3`,

\[
f(J)=\begin{cases}
1/4,&J\text{ contains one representative of every residue class mod }3,\\
0,&\text{otherwise.}
\end{cases}
\]

When every eigenvalue equals `p`, the kernel is `pI`, so

\[
F(p,p,p,p,p,p)=P_{\operatorname{Ber}(p)^{\otimes6}}(I).
\]

Thus the missing sharp lower inequality for `U_adj` is exactly

\[
\boxed{F(\lambda_0,\ldots,\lambda_5)\le F(p,p,p,p,p,p).}
\tag{2.1}
\]

The previous run proved strict local maximality of the right side on each fixed-product manifold, but also exhibited an exact obstruction to arbitrary two-coordinate geometric smoothing. The theorem below replaces that invalid operation by a dihedral reflection-compatible smoothing.

## 3. Reflection symmetrization theorem

For the reflection

\[
\rho(i)=-i\pmod 6,
\]

define the geometric reflection symmetrization

\[
(S_\rho\lambda)_i=\sqrt{\lambda_i\lambda_{\rho(i)}}.
\tag{3.1}
\]

Thus coordinates `0,3` are fixed, while the pairs `(1,5)` and `(2,4)` are simultaneously geometrically averaged.

### Theorem 3.1
For every `lambda in [0,1]^6`,

\[
\boxed{F(S_\rho\lambda)\ge F(\lambda).}
\tag{3.2}
\]

By cyclic relabeling, the same statement holds for every reflection `rho_c(i)=c-i mod 6`.

### Proof
Write

\[
a=\lambda_0,\quad b=\lambda_1,\quad c=\lambda_2,\quad d=\lambda_3,
\quad e=\lambda_4,\quad f=\lambda_5,
\]

and set

\[
x=\sqrt{bf},\qquad y=\sqrt{ce},
\]

\[
U=b+f,\qquad V=c+e,
\]

\[
A=U-2x=(\sqrt b-\sqrt f)^2\ge0,
\qquad
B=V-2y=(\sqrt c-\sqrt e)^2\ge0,
\]

and

\[
W=(b-f)(c-e).
\]

Let

\[
\Delta(a,d)=F(a,x,y,d,y,x)-F(a,b,c,d,e,f).
\tag{3.3}
\]

Because `F` is multi-affine in the Bernoulli parameters, `Delta` is affine in each of `a,d`. Therefore it is the convex combination of its four corner values:

\[
\Delta(a,d)=(1-a)(1-d)\Delta_{00}+a(1-d)\Delta_{10}
 +(1-a)d\Delta_{01}+ad\Delta_{11}.
\tag{3.4}
\]

So it suffices to prove the four corners nonnegative.

Direct substitution of the exact table for `f` into `F=E f(J)` gives the following identities:

\[
12\Delta_{00}
=5AB+(10y-4y^2)A+(10x-4x^2)B-3W,
\tag{3.5}
\]

\[
24\Delta_{10}
=5AB+(4+10y-8y^2)A+(12+10x-16x^2)B-3W,
\tag{3.6}
\]

\[
24\Delta_{01}
=5AB+(12+10y-16y^2)A+(4+10x-8x^2)B-3W,
\tag{3.7}
\]

and

\[
3\Delta_{11}
=(1-y)^2A+(1-x)^2B-AB.
\tag{3.8}
\]

We now prove all four expressions are nonnegative.

First observe that `0<=x,y<=1`. In (3.5)--(3.7), every coefficient of `A` is at least `6y`, and every coefficient of `B` is at least `6x`. Indeed

\[
10y-4y^2\ge6y,
\]

\[
4+10y-8y^2-6y=4(1-y)(1+2y)\ge0,
\]

\[
12+10y-16y^2-6y=4(1-y)(4y+3)\ge0,
\]

and the corresponding statements in `x` are identical.

Hence each right side of (3.5)--(3.7), after multiplying by its positive denominator, is bounded below by

\[
5AB+6yA+6xB-3W.
\tag{3.9}
\]

If `W<=0`, this is immediate. Suppose `W>0`. Since

\[
(b-f)^2=(b+f)^2-4bf=A(A+4x),
\]

and similarly

\[
(c-e)^2=B(B+4y),
\]

we have the exact identity

\[
W=\sqrt{A(A+4x)B(B+4y)}.
\tag{3.10}
\]

Put

\[
T=AB,\qquad Z=yA+xB.
\]

Then

\[
W^2=T(T+4Z+16xy),
\tag{3.11}
\]

while AM--GM gives

\[
Z\ge2\sqrt{xyT}.
\tag{3.12}
\]

We claim

\[
5T+6Z\ge3W.
\tag{3.13}
\]

Both sides are nonnegative. Squaring and using (3.11),

\[
\begin{aligned}
(5T+6Z)^2-9W^2
&=16T^2+24TZ+36Z^2-144xyT\\
&=4\bigl(4T^2+6TZ+9Z^2-36xyT\bigr).
\end{aligned}
\tag{3.14}
\]

For fixed `T,x,y`, the expression in parentheses is increasing in `Z>=0`. Its smallest admissible value occurs at `Z=2 sqrt(xyT)` by (3.12), where it equals

\[
4T^2+12T\sqrt{xyT}\ge0.
\tag{3.15}
\]

Thus (3.13) holds, proving (3.5)--(3.7) nonnegative.

For the last corner, use the box constraints. Since

\[
(1-b)(1-f)=1-U+x^2=(1-x)^2-A\ge0,
\]

we have

\[
A\le(1-x)^2.
\tag{3.16}
\]

Similarly

\[
B\le(1-y)^2.
\tag{3.17}
\]

Therefore

\[
(1-y)^2A+(1-x)^2B-AB\ge0,
\]

for example because `(1-y)^2 A >= AB`, and the remaining term is nonnegative. Hence `Delta_11>=0` as well.

All four corner values are nonnegative, so (3.4) proves (3.2). QED.

## 4. Alternating two reflections forces the scalar spectrum

Let

\[
\rho_0(i)=-i\pmod6,
\qquad
\rho_1(i)=1-i\pmod6.
\]

For strictly positive eigenvalues, put

\[
z_i=\log\lambda_i.
\]

The geometric symmetrization (3.1) is exactly the linear orthogonal projection

\[
z\longmapsto P_cz:=\frac{z+\rho_c z}{2}
\tag{4.1}
\]

in log coordinates. Alternating `P_0,P_1` converges to the orthogonal projection onto

\[
\operatorname{Fix}(\rho_0)\cap\operatorname{Fix}(\rho_1).
\]

But `rho_1 rho_0` is the one-step rotation `i -> i+1`; a vector fixed by both reflections is therefore rotation-invariant, hence constant. Both projections preserve the sum of the log coordinates, so the limit is

\[
\bar z\,(1,\ldots,1),
\qquad
\bar z=\frac16\sum_{i=0}^5z_i=\log p.
\]

Equivalently, alternating the two geometric reflection symmetrizations converges to

\[
(p,p,p,p,p,p).
\tag{4.2}
\]

Theorem 3.1 says that `F` is nondecreasing at every step. By continuity,

\[
F(\lambda)\le F(p,p,p,p,p,p).
\tag{4.3}
\]

If some `lambda_i=0`, then `p=0` and (4.3) is trivial because the right side is `F(0,...,0)=1` while `0<=F<=1`. Thus (4.3) holds on the whole cube `[0,1]^6`.

Combining with the reduction in §2 gives the desired event inequality.

### Corollary 4.1 — the missing adjacent-pair lower bound is closed
For every `Z/6Z`-equivariant positive contraction `Q`,

\[
\boxed{
P^Q(U_{\rm adj})
\ge
P_{\operatorname{Ber}(p)^{\otimes6}}(U_{\rm adj}),
\qquad p=\operatorname{FK}(Q).
}
\tag{4.4}
\]

Together with the earlier R7-03 proofs for the distance-two and antipodal two-point orbits, all three principal two-point translation-orbit lower inequalities on `Z/6Z` are now proved.

## 5. Why this is stronger than the previous local Hessian calculation

The prior scalar Hessian theorem only showed that `(p,...,p)` is a strict local maximizer of `F` on a fixed-product manifold. Arbitrary pairwise geometric smoothing was then shown to fail globally.

The reflection theorem is genuinely global. It does not infer global behavior from the Hessian. Instead, it exploits exactly the dihedral structure of the six-cycle: two reflected frequency pairs are averaged **simultaneously**, and the resulting change admits the four-corner identities (3.5)--(3.8). Alternating two generating reflections then globalizes the comparison by an exact projection argument in log coordinates.

This also explains the earlier counterexample to arbitrary pair smoothing: a one-pair averaging step need not respect the cancellation encoded by the `W` term, while the full reflection operation does.

## 6. Honest source status and next implication

This is a real advance in the finite proof program, but it is **not** a proof of the full source conjecture. Conjecture 5.7 requires stochastic domination for every increasing event and every sofic group/equivariant positive contraction. Corollary 4.1 settles one previously missing orbit-sensitive event family on `Z/6Z`.

The next strongest question is whether the same reflection-midpoint mechanism can be lifted from `U_adj` to every translation-averaged increasing event on `Z/6Z`. A useful sufficient criterion is now explicit: for the corresponding spectral-mixture functional, if the reflection change is multi-affine in the two fixed frequencies and its four corner changes satisfy analogues of (3.5)--(3.8), then alternating `rho_0,rho_1` proves the global fixed-product comparison.

The next attack should therefore classify the remaining invariant upper-set orbit functionals by these reflection corner inequalities, rather than return to scalar expansions or arbitrary smoothing.
