# C0036 / R7-03 — global `Z/6Z` adjacent-orbit theorem by reflection symmetrization

Date: 2026-09-20 UTC  
Role: C03, native ID `6aabe7be74008191b526b109ee4e9e80`  
Status: **PROVED PARTIAL** relative to Lyons Conjecture 5.7. This note proves the previously missing sharp lower-Fuglede–Kadison inequality for the adjacent-pair increasing event on `Z/6Z`; it does **not** claim full stochastic domination for every increasing event or the all-group source conjecture.

## 1. Exact source target

The outside source is Russell Lyons, *Determinantal Probability: Basic Properties and Conjectures* (ICM 2014), arXiv:1406.2707, §5.2, Conjecture 5.7. In the section's equivariant/sofic-group setting, let `Gamma` act by left translation on `ell^2(Gamma)` and let

\[
0\le Q\le I
\]

be a `Gamma`-equivariant positive contraction. The group trace of an equivariant operator is

\[
\operatorname{tr}_\Gamma(T)=\langle T\delta_e,\delta_e\rangle,
\]

and the Fuglede–Kadison determinant is

\[
\operatorname{FK}_\Gamma(Q)
=\exp\bigl(\operatorname{tr}_\Gamma\log|Q|\bigr).
\]

Conjecture 5.7 asks for

\[
\operatorname{Ber}(\operatorname{FK}_\Gamma(Q))^{\otimes\Gamma}
\preccurlyeq P^Q
\preccurlyeq
\operatorname{Ber}\!\left(1-\operatorname{FK}_\Gamma(I-Q)\right)^{\otimes\Gamma}
\]

for every such `Q`, with optimal constants. Stochastic domination means the corresponding inequality for every increasing event. The source explicitly says the conjecture is open even for finite groups.

This note concerns `Gamma=Z/6Z`. For a circulant contraction `Q`, let

\[
\lambda=(\lambda_0,\ldots,\lambda_5)\in[0,1]^6
\]

be its Fourier eigenvalues and

\[
p=(\lambda_0\cdots\lambda_5)^{1/6}=\operatorname{FK}(Q).
\]

Let

\[
U_{\rm adj}=\{X\subseteq Z/6Z:\ X\text{ contains an edge of }C_6\}
\]

and let `I=U_adj^c` be the independent-set event.

The previous R7-03 spectral-mixture reduction proved that, if `J` is the independent Bernoulli spectral set with inclusion probabilities `lambda_i`, then

\[
P^Q(I)=F(\lambda):=\mathbb E_\lambda f(J),
\]

where `f` is the exact projection-DPP table

\[
f(J)=1\quad(|J|\le1),\qquad f(J)=0\quad(|J|\ge4),
\]

for `|J|=2`,

\[
f(J)=\frac56,\frac12,\frac13
\]

when the cyclic frequency distance is respectively `1,2,3`, and for `|J|=3`,

\[
f(J)=\frac14
\]

exactly when the three frequencies represent all three residue classes modulo `3`, otherwise `0`.

For the scalar spectrum `(p,...,p)`, the DPP is iid Bernoulli(`p`), so the missing lower-domination inequality is exactly

\[
F(\lambda)\le F(p,p,p,p,p,p).
\tag{1.1}
\]

Equivalently,

\[
P^Q(U_{\rm adj})\ge
6p^2-6p^3-3p^4+6p^5-2p^6.
\tag{1.2}
\]

The previous run proved strict local stability of (1.1) at the scalar spectrum but also gave an exact counterexample to unrestricted two-coordinate geometric smoothing. The theorem below supplies the missing global operation.

## 2. Reflection-compatible geometric symmetrization

Define the reflection about the antipodal frequency axis `{0,3}` by

\[
\rho(i)=-i\pmod 6.
\]

For `lambda in [0,1]^6`, define

\[
S_0\lambda=
\bigl(
\lambda_0,
\sqrt{\lambda_1\lambda_5},
\sqrt{\lambda_2\lambda_4},
\lambda_3,
\sqrt{\lambda_2\lambda_4},
\sqrt{\lambda_1\lambda_5}
\bigr).
\tag{2.1}
\]

This preserves the product of the six eigenvalues.

### Theorem 2.1 — reflection symmetrization increases the independent-set functional

For every `lambda in [0,1]^6`,

\[
\boxed{F(\lambda)\le F(S_0\lambda).}
\tag{2.2}
\]

The same statement holds for every cyclic translate of `S_0`.

### Proof

We prove the axis `{0,3}` case. Put

\[
a=\lambda_0,\qquad d=\lambda_3.
\]

For positive entries in the two reflected pairs write

\[
\lambda_1=b e^s,\quad \lambda_5=b e^{-s},\qquad
\lambda_2=c e^t,\quad \lambda_4=c e^{-t},
\]

with `b,c in (0,1]`. The zero cases follow by continuity.

Because the table `f` is dihedrally invariant, the Laurent expansion of `F` in the two asymmetry variables has the form

\[
F=C+2A_s\cosh s+2A_t\cosh t
+2A_+\cosh(s+t)+2A_-\cosh(s-t).
\tag{2.3}
\]

Direct expansion from the displayed exact table gives

\[
A_+=\frac{bc}{12}(4ad+a+d-2),
\qquad
A_-=\frac{bc}{3}(ad+a+d-2),
\]

hence

\[
A_+-A_-=\frac{bc}{4}(2-a-d)\ge0.
\tag{2.4}
\]

Thus, for fixed `|s|,|t|`, the original `F` is largest when `st>=0`, because then the larger coefficient multiplies `cosh(|s|+|t|)` rather than `cosh(|s|-|t|)`. Since we need to prove that symmetrization does not decrease `F`, it is enough to handle the worst case `s,t>=0`.

Let

\[
\Delta(a,d):=F(S_0\lambda)-F(\lambda).
\]

The exact product-measure expression for `F` is multi-affine in the six `lambda_i`. The symmetrized coordinates in (2.1) do not depend on `a,d`, so `Delta(a,d)` is bilinear in `(a,d)`. Therefore

\[
\Delta(a,d)
=(1-a)(1-d)\Delta_{00}
+(1-a)d\Delta_{01}
+a(1-d)\Delta_{10}
+ad\Delta_{11},
\tag{2.5}
\]

where `Delta_rs=Delta(r,s)`. It suffices to prove all four corner quantities nonnegative.

#### Corner `(a,d)=(0,0)`

Put

\[
x=\sinh(s/2),\qquad y=\sinh(t/2).
\]

Exact expansion of (2.3) gives

\[
\Delta_{00}
=\frac{2bc}{3}\Big[
(5-2c)x^2+(5-2b)y^2+10x^2y^2
-6xy\sqrt{1+x^2}\sqrt{1+y^2}
\Big].
\tag{2.6}
\]

Set

\[
\xi=\tanh(s/2)=\frac{x}{\sqrt{1+x^2}},\qquad
\eta=\tanh(t/2)=\frac{y}{\sqrt{1+y^2}}.
\]

Multiplying the bracket in (2.6) by the positive factor `(1-xi^2)(1-eta^2)` transforms it into

\[
(5-2c)\xi^2+(5-2b)\eta^2
+2(b+c)\xi^2\eta^2-6\xi\eta.
\tag{2.7}
\]

Since `b,c<=1`,

\[
(5-2c)\xi^2+(5-2b)\eta^2
\ge2\sqrt{(5-2c)(5-2b)}\,\xi\eta
\ge6\xi\eta.
\]

The remaining quartic term in (2.7) is nonnegative, so `Delta_00>=0`.

#### Corner `(a,d)=(1,1)`

The same exact expansion gives

\[
\frac{\Delta_{11}}4
=\frac13\Big[
 b(1-c)^2x^2+c(1-b)^2y^2-4bcx^2y^2
\Big].
\tag{2.8}
\]

The contraction constraints `b e^s<=1` and `c e^t<=1` imply

\[
x^2\le\frac{(1-b)^2}{4b},
\qquad
y^2\le\frac{(1-c)^2}{4c}.
\tag{2.9}
\]

Using the second inequality,

\[
4bcx^2y^2\le b(1-c)^2x^2,
\]

so the bracket in (2.8) is at least `c(1-b)^2y^2>=0`. Hence `Delta_11>=0`.

#### Mixed corner `(a,d)=(0,1)`

For the worst orientation `s,t>=0`, write each reflected pair in high/low form

\[
(\lambda_1,\lambda_5)=(m,mt^2),
\qquad
(\lambda_2,\lambda_4)=(n,nu^2),
\]

where `m,n,t,u in [0,1]`. Symmetrization changes these pairs to `(mt,mt)` and `(nu,nu)`. Put

\[
T=1-t,\qquad U=1-u.
\]

Direct exact expansion of the finite table gives

\[
\begin{aligned}
\Delta_{01}
={}&A T^2+B U^2-\frac{mn}{2}TU
+\frac{mn}{12}TU\,H(T,U),
\end{aligned}
\tag{2.10}
\]

where

\[
A=\frac{m(6+5n-8n^2)}{12},
\qquad
B=\frac{n(2+5m-4m^2)}{12},
\tag{2.11}
\]

and

\[
H(T,U)
=(16n-2)T+(8m-2)U-(4m+8n-1)TU.
\tag{2.12}
\]

Because `H` is bilinear on the unit square,

\[
h:=\min_{[0,1]^2}H
=\min\{0,16n-2,8m-2,8n+4m-3\}.
\tag{2.13}
\]

By AM–GM,

\[
AT^2+BU^2\ge2\sqrt{AB}\,TU.
\]

Thus

\[
\Delta_{01}
\ge mnTU\left[
\frac16\sqrt{\frac{(6+5n-8n^2)(2+5m-4m^2)}{mn}}
-\frac12+\frac{h}{12}
\right].
\tag{2.14}
\]

It remains to show that the bracket is nonnegative. Set

\[
A_0=6+5n-8n^2,
\qquad
B_0=2+5m-4m^2.
\]

For all `m,n in [0,1]`,

\[
A_0\ge3n,
\qquad B_0\ge3m,
\tag{2.15}
\]

because

\[
A_0-3n=2(1-n)(4n+3),
\quad
B_0-3m=2(1-m)(2m+1).
\]

Now consider the four possible values of `h`.

1. If `h=0`, then (2.15) gives `A_0B_0/(mn)>=9`, hence the square root in (2.14) is at least `3`; the bracket is nonnegative.

2. If `h=16n-2`, then necessarily `n<=1/8`. We need

\[
\sqrt{A_0B_0/(mn)}\ge4-8n.
\]

Here `A_0>=6` and `B_0>=3m`, so `A_0B_0/(mn)>=18/n`; while `(4-8n)^2<=16`. The claim follows (with the `n=0` boundary by continuity).

3. If `h=8m-2`, then necessarily `m<=1/4`. We need

\[
\sqrt{A_0B_0/(mn)}\ge4-4m.
\]

Now `A_0>=3n` and `B_0>=2`, so `A_0B_0/(mn)>=6/m>=24`, whereas `(4-4m)^2<=16`.

4. If `h=8n+4m-3`, then `8n+4m<=3`, so `n<=3/8` and `m<=3/4`. Hence `A_0>=6`, `B_0>=2`, and `mn<=9/32`. Therefore

\[
\frac{A_0B_0}{mn}
\ge\frac{12}{9/32}=\frac{128}{3}
>\frac{81}{4}
\ge\left(\frac{9-8n-4m}{2}\right)^2,
\]

which is exactly what (2.14) requires in this case.

Thus `Delta_01>=0`.

#### Mixed corner `(a,d)=(1,0)`

The formula is obtained from the preceding one by the symmetry

\[
(m,T)\longleftrightarrow(n,U).
\]

The same proof gives `Delta_10>=0`.

All four corners are nonnegative. Equation (2.5) therefore gives `Delta(a,d)>=0` for every `a,d in [0,1]`, proving (2.2). Cyclic translation of the frequency indices proves the corresponding statement for the other two antipodal reflection axes. QED.

## 3. Iterating the reflection theorem reaches a solved periodic spectrum

Assume first all `lambda_i>0`; zero eigenvalues are recovered by continuity (and the lower product density is then `p=0`, so the desired increasing-event inequality is in any case trivial).

Write

\[
x_i=\log\lambda_i.
\]

The three vertex-axis symmetrizations act linearly on the log spectrum:

- axis `{0,3}` averages `(x_1,x_5)` and `(x_2,x_4)`;
- axis `{1,4}` averages `(x_0,x_2)` and `(x_3,x_5)`;
- axis `{2,5}` averages `(x_0,x_4)` and `(x_1,x_3)`.

Each operation preserves the sums

\[
x_0+x_2+x_4,
\qquad
x_1+x_3+x_5,
\tag{3.1}
\]

and Theorem 2.1 says that each operation weakly increases `F`.

Cycle through the three axes indefinitely. On each parity class, these are ordinary pairwise arithmetic averages on the three edges of a triangle. The squared deviation from the class mean decreases by exactly a positive multiple of the squared difference of the pair being averaged. Consequently the only possible limit set has all three even logarithms equal and all three odd logarithms equal. Hence the sequence converges to

\[
\lambda^{(\infty)}=(e,o,e,o,e,o),
\tag{3.2}
\]

where

\[
e=(\lambda_0\lambda_2\lambda_4)^{1/3},
\qquad
o=(\lambda_1\lambda_3\lambda_5)^{1/3}.
\tag{3.3}
\]

By continuity of `F`,

\[
F(\lambda)\le F(\lambda^{(\infty)}).
\tag{3.4}
\]

The limiting spectrum is period two:

\[
\lambda_{j+2}^{(\infty)}=\lambda_j^{(\infty)}.
\]

The previously proved R7-03 periodic-spectrum theorem therefore decomposes its `Z/6Z` DPP into three independent copies of the corresponding `Z/2Z` DPP. The full sharp lower Lyons domination is already proved on order two, so, with

\[
p=(e^3o^3)^{1/6}=\sqrt{eo}
=(\lambda_0\cdots\lambda_5)^{1/6},
\]

we have for the decreasing independent-set event

\[
F(\lambda^{(\infty)})
\le F(p,p,p,p,p,p).
\tag{3.5}
\]

Combining (3.4) and (3.5) proves (1.1).

## 4. The closed adjacent-orbit theorem

### Theorem 4.1

For every `Z/6Z`-equivariant positive contraction `Q`, with

\[
p=\operatorname{FK}(Q),
\]

the increasing event that the DPP contains an adjacent pair satisfies

\[
\boxed{
P^Q(U_{\rm adj})
\ge
\operatorname{Ber}(p)^{\otimes6}(U_{\rm adj})
=6p^2-6p^3-3p^4+6p^5-2p^6.
}
\tag{4.1}
\]

This is a complete arbitrary-spectrum proof of the order-six adjacent-pair orbit inequality; no spectral symmetry, perturbative assumption, or finite grid remains.

Together with the earlier R7-03 proofs for the distance-two and distance-three pair orbits, the `Z/6Z` principal two-point orbit ledger moves

\[
\boxed{2/3\longrightarrow3/3.}
\]

## 5. What this does and does not prove

This run closes the exact orbit/event obstruction isolated in the preceding `Z/6Z` work. It also explains why the earlier arbitrary two-coordinate smoothing failed: the correct monotone operation must average **both** reflection pairs simultaneously. Repeating the three compatible reflections does not converge directly to the scalar spectrum; it converges to a two-periodic spectrum, but that is enough because the periodic-spectrum lifting theorem reduces it to the already solved order-two group.

The result is still **PROVED PARTIAL** relative to Conjecture 5.7. The source requires stochastic domination for **every** increasing event and for all source groups/operators. The earlier exact orbit-poset enumeration found 44 invariant upper sets on `Z/6Z`; closing all three principal two-point orbit events does not by itself certify all 44 upper sets. No full `Z/6Z` stochastic-domination claim, no `S_3` theorem, and no all-group resolution is asserted here.

## 6. Next mathematical attack

The reflection mechanism is now available as a reusable comparison tool. The strongest next step is to classify which of the remaining `Z/6Z` invariant upper-set spectral-mixture functionals are monotone under the same three reflection symmetrizations. Any such event is immediately reduced to the solved two-periodic family. The first target should be the minimal three-point orbit-sensitive upper sets not already implied by cardinality thresholds or the index-two coset lift. If reflection monotonicity fails for one of them, the exact failure identifies the next genuinely new gluing mechanism rather than returning to local Hessians or unrestricted pair smoothing.
