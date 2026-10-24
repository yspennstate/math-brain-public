# HARD7-04 — collared subcritical lower component theorem

**Status:** theorem-sized route result / **PARTIAL pending independent audit and source-scope reconciliation**.  This note proves the matching lower leading constant for a deterministic barely-subcritical configuration model under the exponential fourth-moment collar already established for the exact post-giant remainder.  Combined with the earlier HARD7-04 stopping-time reduction and sharp upper bound, it fills the remaining second-largest-component *size* obligation on this track.  It does **not** by itself satisfy the repository closure protocol, and it does not assert that every possible interpretation of the source phrase “discrete duality principle” has been audited.

## 1. Deterministic theorem

Let `d_1,...,d_n` be a deterministic degree sequence with even

\[
L_n:=\sum_{v=1}^n d_v,
\]

and write

\[
Q_n:=\frac1{L_n}\sum_v d_v(d_v-2),
\qquad
R_n:=\frac1{L_n}\sum_v d_v(d_v-2)^2.
\]

Assume, for some `epsilon_n downarrow 0`,

\[
Q_n=-\varepsilon_n+o(\varepsilon_n),
\qquad
N_n:=n\varepsilon_n^3\longrightarrow\infty,
\tag{1.1}
\]

that the empirical degree law converges to a nondegenerate critical law `D` with

\[
\frac{L_n}{n}\to\mu:=\mathbb ED\in(0,\infty),
\qquad
\frac1n\sum_v d_v^3\to\mathbb ED^3<\infty,
\qquad
R_n\to R_*>0,
\tag{1.2}
\]

and that for one fixed number

\[
\frac1{R_*}<\lambda<\frac2{R_*}
\tag{1.3}
\]

we have the exponential collar

\[
\boxed{
\frac{\varepsilon_n}{n}\sum_v d_v^4e^{\lambda\varepsilon_n d_v}\longrightarrow0.
}
\tag{1.4}
\]

Let `CM(d)` be the configuration model and `L_1` its largest component order.

### Theorem 1.1

For every fixed `delta>0`,

\[
\boxed{
\mathbb P\!\left(
L_1<
(1-\delta)\frac{2R_*}{\varepsilon_n^2}\log N_n
\right)\longrightarrow0.
}
\tag{1.5}
\]

The proof counts only tree components whose vertex degrees are at most a fixed scaled cutoff `a/epsilon_n`.  The cutoff is used only to remove the no-slack `2/R_*` endpoint from the second moment; the collar makes the discarded drift and variance negligible at the exact scales needed below.

---

## 2. Tail removal at a fixed scaled cutoff

Fix any constant `a>0` and put

\[
K_n:=\left\lfloor\frac a{\varepsilon_n}\right\rfloor,
\qquad
H_n:=\{v:d_v\le K_n\}.
\]

For `j=1,2,3`, on `d_v>K_n`,

\[
d_v^j
\le \left(\frac{\varepsilon_n}{a}\right)^{4-j}d_v^4,
\]

and `e^{lambda epsilon_n d_v}>=1`.  Hence (1.4) gives

\[
\frac1n\sum_{v\notin H_n}d_v=o(\varepsilon_n^2),
\qquad
\frac1n\sum_{v\notin H_n}d_v^2=o(\varepsilon_n),
\qquad
\frac1n\sum_{v\notin H_n}d_v^3=o(1).
\tag{2.1}
\]

Let

\[
L_{n,a}:=\sum_{v\in H_n}d_v.
\]

Then

\[
\frac{L_{n,a}}{L_n}=1-o(\varepsilon_n^2),
\tag{2.2}
\]

and, if the size-biased retained law is

\[
q_{n,a}(d):=\frac{d\,n_d\mathbf1_{d\le K_n}}{L_{n,a}},
\]

its first centered moment and variance satisfy

\[
\mathbb E_{q_{n,a}}(D-2)
=-\varepsilon_n+o(\varepsilon_n),
\tag{2.3}
\]

\[
\operatorname{Var}_{q_{n,a}}(D)=R_*+o(1).
\tag{2.4}
\]

Indeed, removing the tail changes the numerator of `Q_n` by at most the `d^2+2d` tail in (2.1), and changes the numerator of `R_n` by at most a constant multiple of the `d^3+d^2+d` tail.

A useful additional consequence of (1.4) is

\[
\sum_v d_v^4=o(n/\varepsilon_n).
\tag{2.5}
\]

No limit `a downarrow 0` is needed later: every fixed positive `a` already preserves the leading drift and `R_*` by (2.1).

---

## 3. Exact tree coefficient

For a set `S` of `k>=2` vertices to be a tree component, all its half-edges must be internal and

\[
\sum_{v\in S}d_v=2k-2.
\tag{3.1}
\]

For prescribed degrees satisfying (3.1), the number of internal pairings that form a tree is

\[
(k-2)!\prod_{v\in S}d_v.
\tag{3.2}
\]

To see (3.2), the number of labelled trees with degree sequence `(d_v)_{v in S}` is

\[
\frac{(k-2)!}{\prod_{v\in S}(d_v-1)!}
\]

by the Prüfer code, and the incident tree edges can be assigned to the `d_v` labelled half-edges at `v` in `d_v!` ways.

Let `T_k` count tree components of order `k` all of whose degrees are at most `K_n`.  Define

\[
F_n(z,w):=
\prod_{v\in H_n}(1+z d_v w^{d_v}),
\tag{3.3}
\]

and

\[
C_n(k,s):=[z^kw^s]F_n(z,w).
\]

Uniform pairing therefore gives the exact identity

\[
\boxed{
\mathbb ET_k
=(k-2)!\,
\frac{(L_n-2k+1)!!}{(L_n-1)!!}
\,C_n(k,2k-2).
}
\tag{3.4}
\]

This identity contains no iid approximation and no sampling-with-replacement step.

---

## 4. One-color coefficient saddle

Put

\[
A_n(t):=\sum_{v\in H_n}d_ve^{td_v}.
\tag{4.1}
\]

For a target size `k` in the logarithmic window used below, write

\[
m_k:=2-\frac2k.
\]

There is a unique positive `theta_{n,k}` satisfying

\[
\frac{A_n'(\theta_{n,k})}{A_n(\theta_{n,k})}=m_k.
\tag{4.2}
\]

Moreover, uniformly over that window,

\[
\theta_{n,k}=\frac{\varepsilon_n}{R_*}+o(\varepsilon_n).
\tag{4.3}
\]

To verify this, let `kappa_n(t)=log(A_n(t)/L_{n,a})`.  Then (2.3)--(2.4) give

\[
\kappa_n'(0)=2-\varepsilon_n+o(\varepsilon_n),
\qquad
\kappa_n''(0)=R_*+o(1).
\]

For `0<=t<=lambda epsilon_n`, the third derivative is bounded by a constant multiple of

\[
1+\frac1{L_{n,a}}
\sum_v d_v^4e^{\lambda\varepsilon_n d_v}
=o(\varepsilon_n^{-1})
\tag{4.4}
\]

by (1.4).  Since `1/k=o(epsilon_n)` in the target window, Taylor's theorem proves (4.2)--(4.3).

The corresponding Legendre cost is

\[
J_{n,k}
:=\theta_{n,k}m_k
-\log\frac{A_n(\theta_{n,k})}{L_{n,a}}
=\frac{\varepsilon_n^2}{2R_*}+o(\varepsilon_n^2)
\tag{4.5}
\]

uniformly in the same window.

Set

\[
r_{n,k}:=\frac{k}{A_n(\theta_{n,k})},
\qquad
x_v:=r_{n,k}d_ve^{\theta_{n,k}d_v}.
\tag{4.6}
\]

At the target scale

\[
k=\Theta(\varepsilon_n^{-2}\log N_n)
\]

we have

\[
\max_{v\in H_n}x_v
=O\left(\frac{\log N_n}{N_n}\right)=o(1).
\tag{4.7}
\]

Indeed `r_{n,k}=Theta(k/n)` and `d_v<=a/epsilon_n`.

Now let independent Bernoulli variables `B_v` have

\[
\mathbb P(B_v=1)=p_v:=\frac{x_v}{1+x_v},
\]

and write

\[
U:=\sum_{v\in H_n}B_v,
\qquad
V:=\sum_{v\in H_n}d_vB_v.
\]

Coefficient extraction gives the exact identity

\[
C_n(k,2k-2)
=F_n(r_{n,k},e^{\theta_{n,k}})
 r_{n,k}^{-k}e^{-\theta_{n,k}(2k-2)}
\mathbb P(U=k,V=2k-2).
\tag{4.8}
\]

The linear terms are centered by construction:

\[
\sum_vx_v=k,
\qquad
\sum_vd_vx_v=2k-2.
\tag{4.9}
\]

Replacing `x_v` by `p_v` shifts both means by `O(k^2/n)`.  Since

\[
\frac{k^{3/2}}n
=O\left(\frac{(\log N_n)^{3/2}}{N_n}\right)=o(1),
\tag{4.10}
\]

these shifts are `o(sqrt(k))`.

### Lemma 4.1 (two-dimensional local lower bound)

There is a fixed integer `g>=1`, depending only on two positive-mass atoms of the limiting degree law, and a constant `c>0` such that, uniformly for target-window sizes satisfying

\[
k\equiv2\pmod g,
\tag{4.11}
\]

\[
\boxed{
\mathbb P(U=k,V=2k-2)\ge\frac c k.
}
\tag{4.12}
\]

#### Proof

Because the limiting size-biased law has mean `2` and positive variance `R_*`, the limiting ordinary degree law has positive mass at degree `1` and positive mass at some fixed degree `b>=3`: if there were no degree `1`, every positive size-biased degree would be at least `2`, and mean exactly `2` would force the size-biased law to be degenerate at `2`, contradicting `R_*>0`.  Fix such a `b` and take `g=b-1`.

For all large `n`, both the degree-`1` and degree-`b` classes contain a positive linear number of vertices.  For each of those vertices, `p_v=Theta(k/n)`.  Hence each of the two fixed classes contributes `Theta(k)` Bernoulli variance.  The covariance matrix of `(U,V)` consequently has both eigenvalues bounded above and below by positive multiples of `k`; by (2.3)--(2.4) its determinant is `(R_*+o(1))k^2`.

The Lindeberg condition holds because

\[
\frac{K_n}{\sqrt{k}}
=O\left(\frac a{\sqrt{\log N_n}}\right)\to0.
\tag{4.13}
\]

For completeness, Fourier inversion supplies the local form.  For one fixed degree class `d`, its characteristic factor has modulus bounded by

\[
\exp\{-c_0\sum_{v:d_v=d}p_v(1-p_v)
\operatorname{dist}(u+dv,2\pi\mathbb Z)^2\}.
\]

The degree-`1` and degree-`b` classes therefore give exponential suppression away from the finitely many dual-lattice points where both `u+v` and `u+bv` are multiples of `2pi`.  In neighborhoods of those points of radius `O(k^{-1/2})`, Taylor expansion of the log characteristic function is uniform: the cubic remainder is bounded, after the `k^{-1/2}` rescaling, by

\[
O(k^{-3/2})\sum_vp_v(1+d_v^3)
= o(1),
\tag{4.14}
\]

because `sum p_v d_v^3=O((k/n) sum d_v^4)=o(k/epsilon_n)` by (2.5), while `epsilon_n sqrt(k)~sqrt(log N_n)`.  Thus each contributing dual-lattice neighborhood converges to the same nondegenerate Gaussian integral.  The target point belongs to the lattice whenever `k=2 mod (b-1)`, and the mean displacement is `o(sqrt(k))` by (4.10).  Fourier inversion therefore gives in fact a positive constant times `k^{-1}(1+o(1))`, which implies (4.12).  `square`

Next expand the nonlocal part of (4.8).  With

\[
B_n(t):=\sum_{v\in H_n}d_v^2e^{2td_v},
\]

we have, by `log(1+x)=x-x^2/2+O(x^3)`,

\[
\log F_n(r_{n,k},e^{\theta_{n,k}})
=k-\frac{k^2}{2}
\frac{B_n(\theta_{n,k})}{A_n(\theta_{n,k})^2}+o(1),
\tag{4.15}
\]

because

\[
\sum_vx_v^3
\le C_a r_{n,k}^3\sum_vd_v^3
=O(k^3/n^2)
=O((\log N_n)^3/N_n^2)=o(1).
\tag{4.16}
\]

Also

\[
\log\frac{(L_n-2k+1)!!}{(L_n-1)!!}
=-(k-1)\log L_n+\frac{(k-1)^2}{L_n}+o(1),
\tag{4.17}
\]

since `k^3/L_n^2=o(1)`.

Finally the critical finite-population cancellation survives the tilt.  From (2.1), the third-moment bound, (2.5), `theta=O(epsilon_n)`, and the fixed cutoff,

\[
\frac{L_nB_n(\theta_{n,k})}
{A_n(\theta_{n,k})^2}
=2+O(\varepsilon_n).
\tag{4.18}
\]

Indeed `A_n(theta)/L_n=1+O(epsilon_n)`, while

\[
B_n(\theta)
=\sum_{v\in H_n}d_v^2+O(n\varepsilon_n)
=L_n(2+O(\varepsilon_n)).
\]

Therefore

\[
\frac{k^2}{L_n}
-\frac{k^2}{2}
\frac{B_n(\theta_{n,k})}{A_n(\theta_{n,k})^2}
=O\left(\frac{\varepsilon_n k^2}{n}\right)+o(1)
=O\left(\frac{(\log N_n)^2}{N_n}\right)+o(1)
=o(1).
\tag{4.19}
\]

Combining (3.4), (4.8), Lemma 4.1, Stirling, (4.5), (4.15)--(4.19), and (2.2) yields uniformly over admissible target-window sizes

\[
\boxed{
\mathbb ET_k
\ge c_1 L_n k^{-5/2}
\exp\left\{-\frac{\varepsilon_n^2}{2R_*}k+o(\log N_n)\right\}.
}
\tag{4.20}
\]

The factor `L_{n,a}/L_n=1-o(epsilon_n^2)` contributes only `o(log N_n)` to the exponent because `k=O(epsilon_n^{-2}log N_n)`.

---

## 5. Abundance in a short size window

Fix `delta>0` and let

\[
K_n^0:=
\left\lfloor
(1-\delta)\frac{2R_*}{\varepsilon_n^2}\log N_n
\right\rfloor,
\qquad
J_n:=\lfloor\varepsilon_n^{-2}\rfloor.
\tag{5.1}
\]

Let `I_n` be the integers in `[K_n^0,K_n^0+J_n]` satisfying `k=2 mod g`, and put

\[
Z_n:=\sum_{k\in I_n}T_k.
\]

There are `Theta(epsilon_n^{-2})` such sizes.  Across this whole window the additional Cramér exponent is only `O(1)`.  Since

\[
n=\frac{N_n}{\varepsilon_n^3},
\qquad
k^{-5/2}=\Theta\left(
\frac{\varepsilon_n^5}{(\log N_n)^{5/2}}
\right),
\]

(4.20) gives

\[
\boxed{
\mathbb EZ_n
\ge
\frac{N_n^{\delta+o(1)}}{(\log N_n)^{5/2}}
\longrightarrow\infty.
}
\tag{5.2}
\]

The size window is essential: a single-size expectation carries an extra `epsilon_n^2` prefactor, which need not diverge in the full barely-subcritical regime.

---

## 6. Two-color coefficient and second moment

It remains to show that the abundance in (5.2) is not concentrated on strongly overlapping candidates.  Distinct components are disjoint, so the exact joint count is naturally encoded by a two-color product.

For sizes `k,l` and target sums `s=2k-2`, `t=2l-2`, define

\[
G_n(z,w,u,y)
:=\prod_{v\in H_n}
(1+z d_vw^{d_v}+u d_vy^{d_v}).
\tag{6.1}
\]

The coefficient of `z^k w^s u^l y^t` sums the degree weights over ordered pairs of disjoint vertex sets.  Consequently

\[
\mathbb E[T_kT_l;\text{two distinct components}]
=(k-2)!(l-2)!
\frac{(L_n-2k-2l+3)!!}{(L_n-1)!!}
D_n(k,s;l,t),
\tag{6.2}
\]

where `D_n` is the coefficient in (6.1).

Let `theta=theta_{n,k}`, `phi=theta_{n,l}` and

\[
r=\frac{k}{A_n(\theta)},
\qquad
q=\frac{l}{A_n(\phi)},
\]

and write

\[
x_v=rd_ve^{\theta d_v},
\qquad
y_v=qd_ve^{\phi d_v}.
\]

Use at each vertex the three-category law with probabilities proportional to `1,x_v,y_v`.  The exact analogue of (4.8) expresses `D_n` as `G_n` times the probability that the two colored vertex counts and degree sums equal `(k,s,l,t)`.

The same Fourier argument as Lemma 4.1, now in four dimensions, gives a uniform local limit.  The degree-`1` and degree-`b` classes smooth both colors, the four covariance eigenvalues are `Theta(k)` (recall `k/l` stays bounded in the short window), and the off-diagonal color covariances are negligible.  More explicitly,

\[
\operatorname{Cov}(U_1,U_2)=O(kl/n)=o(k),
\]

and the worst degree-sum cross covariance is bounded by

\[
O\left(\frac{kl}{n^2}\sum_v d_v^4\right)
=o\left(\frac{kl}{n\varepsilon_n}\right)
=o(k)
\tag{6.3}
\]

because `k/(n epsilon_n)=O(log N_n/N_n)`.  The mean shifts caused by mutual exclusion are `O(kl/n)=o(sqrt(k))` by (4.10), and the same Lindeberg estimate (4.13) applies.  Therefore the four-dimensional local probability divided by the product of the two one-color local probabilities tends to `1`, uniformly for `k,l in I_n`.

The logarithm of the remaining coefficient ratio is

\[
\log G_n-\log F_{n,\theta}-\log F_{n,\phi}
=-rq\sum_{v\in H_n}d_v^2e^{(\theta+\phi)d_v}+o(1),
\tag{6.4}
\]

because all mixed cubic terms are `O(k^3/n^2)=o(1)`.

On the pairing side,

\[
\log
\frac{(L_n-2k-2l+3)!!(L_n-1)!!}
{(L_n-2k+1)!!(L_n-2l+1)!!}
=\frac{2kl}{L_n}+o(1).
\tag{6.5}
\]

Finally, exactly as in (4.18),

\[
\frac{L_n\sum_{v\in H_n}d_v^2e^{(\theta+\phi)d_v}}
{A_n(\theta)A_n(\phi)}
=2+O(\varepsilon_n).
\tag{6.6}
\]

Here the endpoint `theta+phi~2epsilon_n/R_*` causes no loss because all counted vertices satisfy `d_v<=a/epsilon_n`, so the exponential factor in (6.6) is bounded by a constant depending only on `a`; the untruncated collar is not invoked at the endpoint.

Combining (6.4)--(6.6),

\[
\frac{
\mathbb E[T_kT_l;\text{distinct}]
}{\mathbb ET_k\,\mathbb ET_l}
=
\exp\left\{
O\left(\frac{\varepsilon_nkl}{n}\right)+o(1)
\right\}
=1+o(1)
\tag{6.7}
\]

uniformly on the window, since

\[
\frac{\varepsilon_nkl}{n}
=O((\log N_n)^2/N_n)\to0.
\]

Summing (6.7) gives

\[
\mathbb E[Z_n(Z_n-1)]
\le(1+o(1))(\mathbb EZ_n)^2.
\tag{6.8}
\]

Because `EZ_n->infinity`, (5.2) and (6.8) imply

\[
\frac{\operatorname{Var}Z_n}{(\mathbb EZ_n)^2}\to0,
\qquad
\mathbb P(Z_n=0)\to0.
\tag{6.9}
\]

Thus with high probability there is a tree component of order at least `K_n^0`, proving Theorem 1.1.

---

## 7. Application to the exact post-giant remainder

The preceding HARD7-04 stopping-time reduction and collar theorem establish, for the exact random sleeping degree sequence after the giant, with probability tending to one,

\[
L_n^{post}/n\to\mu,
\qquad
Q_n^{post}=-\varepsilon_n+o_p(\varepsilon_n),
\qquad
R_n^{post}\to_pR_*,
\tag{7.1}
\]

preservation of the limiting degree law and finite third moment, and for every fixed `lambda<2/R_*`,

\[
\frac{\varepsilon_n}{n}
\sum_{v\in S_n^{post}}
 d_v^4e^{\lambda\varepsilon_n d_v}
\to_p0.
\tag{7.2}
\]

Choose one fixed `lambda` satisfying (1.3).  The `o_p` statements may be placed on a single good event with probability `1-o(1)` and deterministic tolerances tending to zero.  Every bound in Sections 2--6 is uniform on that event once `mu,R_*,a,lambda` and the two fixed limiting atoms are fixed.  Conditional on the revealed giant history, the unexplored half-edges are a uniform perfect matching, hence exactly a configuration model on that residual degree sequence.  Applying Theorem 1.1 conditionally gives

\[
\boxed{
L_1^{post}\ge
(1-o_p(1))
\frac{2R_*}{\varepsilon_n^2}
\log(n\varepsilon_n^3).
}
\tag{7.3}
\]

The earlier HARD7-04 Cramér-collar theorem gives the matching upper bound

\[
L_1^{post}\le
(1+o_p(1))
\frac{2R_*}{\varepsilon_n^2}
\log(n\varepsilon_n^3),
\tag{7.4}
\]

and the completed-component stopping reduction identifies `L_1^{post}` with the original graph's second-largest component with probability `1-o(1)`.  Hence the combined route gives the size statement

\[
\boxed{
|C_{2,n}|
=(1+o_p(1))
\frac{2R_*}{\varepsilon_n^2}
\log(n\varepsilon_n^3).
}
\tag{7.5}
\]

under the admitted finite-third-moment barely-supercritical configuration-model hypotheses.

Equation (7.5) is a **source-level proof candidate for the second-largest-component size question**, not a repository closure declaration.  Closure still requires a source-scope audit, prior-art confirmation for this exact lower theorem, and the two independent OTHER-track audits required by `CONTROL.md`.

---

## 8. Route diagnosis

The previous endpoint obstruction was real for the *untruncated* second moment: squaring the Cramér weight probes `2 theta/epsilon -> 2/R_*`, exactly where the post-giant exponential collar has no slack.  The fixed scaled cutoff resolves it without changing the leading rate:

1. the collar makes the discarded `d,d^2,d^3` masses respectively `o(n epsilon^2)`, `o(n epsilon)`, `o(n)`;
2. the one-color Cramér saddle remains at `theta~epsilon/R_*` with rate `epsilon^2/(2R_*)`;
3. on the retained range, the two-color weight at `theta+phi~2epsilon/R_*` is bounded by `e^{O(a)}`;
4. the exact pairing correction cancels the exact quadratic finite-population correction, leaving only `O(epsilon kl/n)=o(1)`;
5. fixed positive-mass degree atoms provide the lattice smoothing needed for the local coefficient lower bound.

This is the bridge that was missing from the STUCK2 report.