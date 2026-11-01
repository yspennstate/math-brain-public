# B17 FEI new proof mechanism: Palm-deletion transport for the spectral sample

**Model:** GPT-5.6 Sol (self-report). **Reasoning level configured:** UNKNOWN_NOT_EXPOSED; maximum actually supported was requested.  
**Date:** 2026-09-21.  
**Status of full FEI:** **OPEN / NOT PROVED.**  
**Brain status:** `WITHOUT_VERIFIED_BRAIN` — no genuine authenticated brain retrieval/context was used in this mathematical derivation.  
**Fresh mathematical source:** `yspennstate/math-open-problems` `master` at `e307ec41bc0fc3532a42ae38acac28adb6d75c94`.  
**Prior B17 route deliberately not repeated:** `fleet03/B17/2026-09-21-signed-diagonal-comparison/REPORT.md` (signed variable-identification defect transport).

## Route chosen first

This is a new refinement of **APPROACHES route 14 (coding / point-process transfer)**, with a different mechanism from the prior signed-diagonal work:

> **Palm-deletion route.** Encode every Boolean function as a translation-invariant projection determinantal point process (DPP) on the Fourier cube. The nonconstant spectral sample is exactly the location of the one point deleted when that projection DPP is coupled to its reduced Palm process, conditioned on the deleted point not being the origin. FEI becomes an entropy-versus-Hamming-transport inequality for this Palm deletion location.

The out-of-box moves used here were: **11 (dualize), 18 (say it in another language), 21 (ask who else has this shape)**. I attacked two tempting consequences immediately and found exact Boolean counterexamples, so this report does not promote generic DPP negative dependence or spectral-size concentration into a false FEI lemma.

## 1. Exact projection representation

Let `G=(F_2)^n`, identified with Fourier subsets of `[n]`, and let `N=2^n`. Let

\[
f:\{-1,1\}^n\to\{-1,1\},\qquad A=\{x:f(x)=-1\},\qquad \mu=|A|/N.
\]

Negating `f` does not change its Fourier-squared law, entropy, or influence, so one may take `0<mu<=1/2` when convenient. Let `U` be the normalized Walsh-Hadamard matrix and define

\[
K=U\,\mathrm{diag}(1_A)\,U^*.
\]

Then `K` is an orthogonal projection of rank `|A|`, and translation invariance on `G` gives

\[
K_{S,T}=\widehat{1_A}(S\triangle T),\qquad K_{S,S}=\mu.
\]

Since `f=1-2 1_A`, writing `a_R=\widehat f(R)`,

\[
a_\varnothing=1-2\mu,\qquad a_R=-2K_{\varnothing,R}\quad(R\ne\varnothing). \tag{1}
\]

Therefore the spectral law `p_R=a_R^2` is

\[
p_\varnothing=(1-2\mu)^2,
\qquad
p_R=4|K_{\varnothing,R}|^2\quad(R\ne\varnothing). \tag{2}
\]

Let

\[
V:=1-p_\varnothing=4\mu(1-\mu).
\]

Conditioning the spectral sample `S` on being nonempty gives

\[
q_R:=\Pr[S=R\mid S\ne\varnothing]
=\frac{|K_{\varnothing,R}|^2}{\mu(1-\mu)},\qquad R\ne\varnothing. \tag{3}
\]

This is already a complete algebraic equivalence; no finite check is used.

## 2. PROVED using a standard DPP coupling theorem: q is a Palm-deletion location

Take the finite DPP `X` on the Fourier cube with correlation kernel `K`. For a point `u` with `K(u,u)>0`, its reduced Palm DPP has kernel

\[
K^u(v,w)=K(v,w)-\frac{K(v,u)K(u,w)}{K(u,u)}. \tag{4}
\]

For finite DPPs, the stochastic-covering/Palm coupling theorem gives a coupling with `X^u subset X` and `X\X^u` containing at most one point. Møller--O'Reilly, *Couplings for determinantal point processes and their reduced Palm distributions with a view to quantifying repulsiveness*, arXiv:1806.07347v6, records this finite-space consequence and the difference intensity

\[
\Pr[v\in X\setminus X^u]=\frac{|K(u,v)|^2}{K(u,u)}. \tag{5}
\]

Here `K` is a projection, so

\[
\sum_v\frac{|K(u,v)|^2}{K(u,u)}
=\frac{(K^2)(u,u)}{K(u,u)}=1.
\]

Because the difference has at most one point and expected size exactly one, it has **exactly one point almost surely**. Call it `Y`. At `u=emptyset`,

\[
\Pr[Y=R]=\frac{|K_{\varnothing,R}|^2}{\mu}. \tag{6}
\]

In particular `Pr[Y=emptyset]=mu` and, for `R != emptyset`,

\[
\boxed{
\Pr[Y=R\mid Y\ne\varnothing]
=\frac{|K_{\varnothing,R}|^2}{\mu(1-\mu)}
=q_R.
} \tag{7}
\]

So the nonempty Fourier spectral sample is **exactly the Palm-deletion point conditioned not to be the origin**.

This is the useful new bridge: FEI is not being compared to the entropy of the whole DPP. It is about the spatial profile of the single unit of occupancy removed by Palm conditioning.

## 3. PROVED: exact FEI reformulation as an entropy-cost inequality for the deletion point

From `p_emptyset=1-V` and `p_R=V q_R` for `R != emptyset`,

\[
H(f)=h_2(V)+V H(q), \tag{8}
\]

and

\[
I(f)=V\,\mathbb E_q |R|. \tag{9}
\]

Thus, for every nonconstant Boolean `f`, FEI with constant `C` is equivalent to

\[
\boxed{
H(q)+\frac{h_2(V)}{V}
\le C\,\mathbb E_q|R|,
} \tag{10}
\]

where `q` is the conditional Palm-deletion law in (7).

Equivalently, if `Y` is the point removed from the projection DPP under the Palm coupling,

\[
H(Y\mid Y\ne\varnothing)
+\frac{h_2(4\mu(1-\mu))}{4\mu(1-\mu)}
\le
C\,\mathbb E[|Y|\mid Y\ne\varnothing]. \tag{11}
\]

The second term is an explicit bias price. The genuinely difficult part is therefore a **metric description-length bound for where Palm conditioning sends the missing particle**.

A second exact interpretation follows from the DPP pair correlation. For `R != emptyset`,

\[
\Pr[\varnothing,R\in X]=\mu^2-|K_{\varnothing,R}|^2,
\]

so

\[
q_R
=\frac{\mu^2-\Pr[\varnothing,R\in X]}{\mu(1-\mu)}. \tag{12}
\]

Hence `q` is the normalized **pair-repulsion deficit profile** of this stationary projection DPP.

## 4. Refutation attempt 1: generic spectral-size concentration is false by an exponentially large margin

A tempting route would be to prove a Poisson-like moment inequality for `K=|S|`, for example

\[
\operatorname{Var}(K)\le \mathbb E K
\quad\text{or}\quad
\mathbb E[K(K-1)]\le (\mathbb E K)^2. \tag{13}
\]

This would make entropy-cost estimates much easier. It is **REFUTED** by the exact one-point Boolean family.

Let `A={x_0}`. Then `mu=1/N`, and for every nonempty Fourier set `R`,

\[
|K_{\varnothing,R}|=1/N,
\qquad
p_R=4/N^2.
\]

Therefore

\[
I=\mathbb E K=\frac{2n}{N},
\qquad
\mathbb E K^2=\frac{n(n+1)}{N},
\]

and

\[
\frac{\operatorname{Var}(K)}{I}
=\frac{n+1}{2}-\frac{2n}{N}\longrightarrow\infty. \tag{14}
\]

Even more strongly,

\[
\frac{\mathbb E[K(K-1)]}{I^2}
=\frac{n-1}{n}\,2^{n-2}. \tag{15}
\]

Concrete exact values:

| n | Var(K)/I | E[K(K-1)]/I^2 |
|---:|---:|---:|
| 4 | 2 | 3 |
| 8 | 71/16 = 4.4375 | 56 |
| 16 | 17407/2048 = 8.49951171875 | 15360 |

So any proof that needs the unconditioned spectral size to be sub-Poisson, or even to have variance `O(I)`, is dead.

This is not a threat to FEI. Here `q` is uniform on the `N-1` nonempty subsets,

\[
H(q)=\log_2(N-1),
\qquad
\mathbb E_q|R|=\frac{nN}{2(N-1)}, \tag{16}
\]

and the full ratio satisfies `H(f)/I(f)<4` for every `n` and tends to `4`. One quick proof uses
`h_2(V) <= V log_2(e/V)` with `V=4(N-1)/N^2`:

\[
H(f)
\le V\log_2\!\frac{e(N-1)}V
=V(2n-2+\log_2 e)
<2nV
<4I(f). \tag{17}
\]

So the correct route must control **description length directly**, not concentration of `|S|`.

## 5. Refutation attempt 2: DPP negative association does not transfer to q

A second tempting shortcut is: the projection DPP is strongly negatively dependent, so perhaps the conditional deletion law `q`, viewed as a random subset of Fourier coordinates, is pairwise negatively correlated or negatively associated. That is also **REFUTED** by a three-bit Boolean function.

Define

\[
f(x_1,x_2,x_3)=
\begin{cases}
1,&x_3=-1,\\
x_1x_2,&x_3=+1.
\end{cases}
\]

Its exact Fourier expansion is

\[
f=\frac12+\frac12x_1x_2-\frac12x_3+\frac12x_1x_2x_3. \tag{18}
\]

Thus `mu=1/4`, `V=3/4`, and conditioned on being nonempty, the spectral sample is uniform on

\[
\{\{1,2\},\{3\},\{1,2,3\}\}. \tag{19}
\]

Consequently

\[
\Pr_q(1\in S)=\Pr_q(2\in S)=\frac23,
\qquad
\Pr_q(1,2\in S)=\frac23,
\]

so

\[
\operatorname{Cov}_q(1_{1\in S},1_{2\in S})
=\frac23-\frac49
=\boxed{\frac29}>0. \tag{20}
\]

Therefore the deletion-location law `q` is not even universally pairwise negatively correlated. Generic entropy theorems for negatively associated random subsets cannot simply be applied to `q`, despite the negative dependence of the underlying DPP itself.

## 6. What remains alive

The DPP bridge itself survives both attacks. What died are two overly strong shortcuts:

- **REFUTED:** control FEI through Poisson/sub-Poisson concentration of spectral size.
- **REFUTED:** transfer the DPP's negative association directly to the conditional deletion law `q`.

The surviving target is sharper and genuinely metric:

> **Palm-deletion entropy-cost problem.** For the special stationary projection DPPs `K=U diag(1_A) U*` on the Hamming cube, control the entropy of the unique Palm-deletion location, conditioned away from the origin, by its expected Hamming distance, while paying the explicit bias term in (11).

This is equivalent to FEI, so merely restating it is not a proof. The point of the route is that it exposes additional machinery unavailable in the raw Fourier statement: reduced-Palm rank-one updates, stochastic covering couplings, projection geometry, and point-process transport.

## 7. Concrete next attack

Do **not** enumerate all Boolean functions again. The next run on this route should try to make the Palm coupling constructive along cube coordinates.

For the deletion point `Y`, reveal its coordinate bits sequentially and seek a coupling-specific inequality of the form

\[
\sum_{i=1}^n H(1_{i\in Y}\mid Y_{<i},\,Y\ne\varnothing)
\le C_0\sum_{i=1}^n \Pr(i\in Y\mid Y\ne\varnothing), \tag{21}
\]

where the order is allowed to depend on the projection/Palm coupling, not merely on the one-point marginals of `q`. The n=3 counterexample shows that a proof cannot come from negative association of the bits. The one-point family shows it cannot come from small variance. The next structural input to test is the **rank-one Palm update itself**: after conditioning/revealing one cube coordinate, determine whether the remaining deletion vector is again the difference point of a lower-dimensional pair of nested projection DPPs, with an exact budget identity. If that recursion holds with a bounded entropy charge, it would turn the abstract point-process representation into a genuine sequential-compression proof mechanism (APPROACHES 1 + 14).

## 8. Literature boundary

The DPP Palm coupling used above is established, not claimed new: Jesper Møller and Eliza O'Reilly, arXiv:1806.07347v6, with the finite strong-Rayleigh/stochastic-covering case traced there to Pemantle--Peres. A bounded search for `Fourier entropy influence + determinantal point process / Palm` did not surface an FEI paper using this specific projection-Palm deletion reformulation. **No novelty or priority claim is made** without a deeper literature search.

## Claim ledger

**PROVED:**
1. Every Boolean function yields the translation-invariant projection kernel (1)-(3).
2. Using the standard finite DPP Palm coupling theorem, its nonempty spectral sample equals the unique Palm-deletion location conditioned away from the origin, (7).
3. FEI is exactly the Palm deletion entropy-cost inequality (10)-(11).
4. The one-point family has unbounded `Var(|S|)/I` and exponentially large second-factorial-moment ratio while `H/I<4` and tends to `4`.
5. The explicit three-bit function (18) gives positive coordinate covariance `2/9` under `q`.

**REFUTED-LEMMA:**
1. Universal sub-Poisson spectral-size concentration.
2. Universal pairwise negative correlation / negative association of the conditional deletion law `q`.

**CONDITIONAL / OPEN:**
A useful sequential entropy-cost inequality exploiting the rank-one Palm update has not been proved. Full FEI remains OPEN.
