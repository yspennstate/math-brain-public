Model actually run: GPT-5.6 Sol; reasoning level UNVERIFIED. GPT-6 / maximum reasoning was requested as a preference, but no authenticated model-effort selector or guaranteed full-hour execution is exposed here, so I do not claim it.

# P03-A analytic proof report — finite-second-moment critical profile and an exact support-free branch-tail identity

**Status:** PROVED PARTIAL / NEW MOMENT-WEAKENING AND SUPPORT-FREE STRUCTURAL THEOREM CANDIDATE. Not independently audited. The full Lyons–Pemantle–Peres conjecture remains open.

**Native role:** P03-A, `6aa7b398af30819181ca50ba3c4e6c33`, complementary analytic recursive/derivative role under `operations/progress_first_2026-09-20/OWNER_DIRECTIVE.md` and `REGISTRY.md`. Canonical ownership was checked on assignment and is not changed here. P03-B retains regeneration/coupling/path-score work; I consumed its latest `2026-09-20T1320Z__uniform-child-loop-contraction-and-recursive-selection.md` only for continuity and do not duplicate its quenched return-loop analysis. Old D0047 history is untouched.

**Captured master immediately before this write:** `7c7b34d032a4eef7e44cf494fdeb4afc681a0eb3`.

**Inherited P03-A checkpoint:** `probability_campaigns/progress_first_2026-09-20/P03/analytic/2026-09-20T1308Z__uniform-scaled-terminal-strip-for-bounded-support-and-explicit-K3.md`.

That report proved a quantitative terminal monotonicity strip uniformly over each fixed bounded support, but its quantitative secant control still depended on a hard support cutoff. The present run attacks the support-free limit directly. The main gains are:

1. the normalized critical escape probability is identified in `W_2` under only a finite second offspring moment;
2. the critical escape and speed slopes previously proved with a third-moment hypothesis are recovered under only `E nu^2<infinity`;
3. the finite branch-vector identity is extended exactly to arbitrary unbounded support and its tail is charged by a finite-variance functional.

The fixed source-level metric remains

`R_full: 1 -> 1`.

The intermediate obligation moves from “remove the support cutoff at criticality” to the sharper remaining task “upgrade the support-free value/asymptotic control to a support-free secant derivative estimate strong enough for an entire terminal monotonicity interval.”

---

## 1. Source convention and bounded current-source refresh

At a non-root vertex with `k` children I use reciprocal **parent bias** `lambda`:

\[
P_\lambda(x,x^*)=\frac{\lambda}{\lambda+k},\qquad
P_\lambda(x,x_i)=\frac1{\lambda+k}.
\]

Thus increasing `lambda` weakens the outward bias. For a no-leaf offspring law

\[
P(\nu=0)=0,\qquad m:=E\nu>1,
\]

the transient critical point is `lambda=m`, and the LPP conjecture asks that the speed `ell_lambda` be nonincreasing as `lambda` increases through the transient interval.

The external range was not reset to the old high-bias cutoff. A bounded literature refresh on 20 September 2026 again found the broad later theorem of He Song, Longmin Wang and Kainan Xiang, *The speed of a biased walk on a Galton-Watson tree without leaves is monotonic for low values of bias*, J. Appl. Probab. 62 (2025), 1044–1052, DOI `10.1017/jpr.2024.113`: if the minimum offspring is `d>=2`, strict decrease holds for

\[
0\le\lambda\le \frac{d}{1+\sqrt{1-1/d}}.
\]

Bowditch–Tokushige, arXiv:1906.07913 and arXiv:2006.03433, provide differentiability / analyticity in ballistic regimes but not the missing global sign.

For critical linear response, Ben Arous–Hu–Olla–Zeitouni, *Einstein relation for biased random walk on Galton-Watson trees* (2013), assume an exponential offspring moment in their continuous-time theorem; their introduction explicitly remarks that an extension to offspring laws with only moment bounds is natural but is not treated there. The result below is a one-sided **discrete-time** critical calculation and is not represented as a full replacement for their Einstein relation.

No checked 2026 source-wide resolution surfaced. This is bounded negative evidence, not a novelty certificate.

---

## 2. Escape recursion and theorem statements

Let `B_lambda` be the quenched probability, from a child-root, of never hitting its parent. If `B_1,B_2,...` are iid copies and

\[
S_\nu=\sum_{i=1}^{\nu}B_i,
\]
then

\[
\boxed{
B_\lambda\stackrel d=\frac{S_\nu}{\lambda+S_\nu}.
}
\tag{2.1}
\]

Write

\[
\delta:=m-\lambda,\qquad e_\delta:=E B_{m-\delta},
\qquad X_\delta:=\frac{B_{m-\delta}}{e_\delta},
\qquad Y_\delta:=\sum_{i=1}^{\nu}X_{\delta,i}.
\tag{2.2}
\]

Also put

\[
a:=m-1,
\qquad f_2:=E[\nu(\nu-1)].
\tag{2.3}
\]

Throughout the new theorem assume only

\[
\boxed{E\nu^2<\infty.}
\tag{2.4}
\]

No third or fourth offspring moment is assumed.

### Theorem 2.1 — critical escape profile in `W_2`

Let `W` be the unique mean-one finite-second-moment fixed point of the Galton–Watson smoothing map

\[
W\stackrel d=\frac1m\sum_{i=1}^{\nu}W_i,
\tag{2.5}
\]

equivalently the `L^2` limit of the normalized Galton–Watson additive martingale `Z_n/m^n`. Then, as `delta downarrow0`,

\[
\boxed{
W_2(\mathcal L(X_\delta),\mathcal L(W))\longrightarrow0.
}
\tag{2.6}
\]

In particular,

\[
\boxed{
E X_\delta^2\longrightarrow
\frac{f_2}{m(m-1)}.
}
\tag{2.7}
\]

### Theorem 2.2 — finite-second-moment critical escape scale

Under the same assumptions,

\[
\boxed{
\frac{E B_{m-\delta}}{\delta}
\longrightarrow\frac{m-1}{f_2}.
}
\tag{2.8}
\]

Thus the third-moment hypothesis in the inherited `0603Z` escape asymptotic is unnecessary.

### Theorem 2.3 — exact support-free branch-tail identity

For every sufficiently small `delta>0` (so `lambda=m-delta>1`), define branch weights `h_n,g_j` in Section 5 below and

\[
T_j=P(\nu>j),\qquad
A_j=E[(\nu-m)\mathbf 1_{\{\nu>j\}}].
\tag{2.9}
\]

Then `A_j>=0`,

\[
\sum_{j\ge1}T_j=m-1,
\qquad
\sum_{j\ge1}A_j=\operatorname{Var}(\nu),
\tag{2.10}
\]

and Aidekon's escape-tilted effective offspring mean `M_delta` satisfies the exact infinite-support identity

\[
\boxed{
q_\delta:=m-M_\delta
=
\frac{\sum_{j\ge1}A_jx_j}
{1-\sum_{j\ge1}T_jx_j}
=
 e_\delta\frac{K_\delta}{\bar h_\delta},
}
\tag{2.11}
\]

where

\[
x_j=\frac{e_\delta g_j}{h_1},\qquad
K_\delta=\sum_{j\ge1}A_jg_j,
\qquad
\bar h_\delta=E[h_\nu].
\tag{2.12}
\]

This is the exact unbounded-support extension of the finite vector identity from `1308Z`.

### Theorem 2.4 — finite-second-moment critical speed slope

As `lambda up-arrow m`, equivalently `delta downarrow0`,

\[
\boxed{
M_{m-\delta}
=m-\frac{\operatorname{Var}(\nu)}{f_2}\,\delta+o(\delta),
}
\tag{2.13}
\]

and

\[
\boxed{
\ell_{m-\delta}
=
\frac{m-1}{2f_2}\,\delta+o(\delta).
}
\tag{2.14}
\]

Therefore for every fixed `r in (0,1)` there is `delta_r>0` such that

\[
\boxed{
\ell_{m-\delta}>\ell_{m-r\delta}
\qquad(0<\delta<\delta_r).
}
\tag{2.15}
\]

Equation (2.14) is an actual weakening of the inherited `E nu^3<infinity` hypothesis to `E nu^2<infinity`. It is still an asymptotic / fixed-ratio comparison result, not a whole terminal-interval monotonicity theorem.

---

## 3. Uniform normalized second moment without a third moment

At criticality the `lambda=m` walk is recurrent, hence `B_lambda downarrow0` almost surely and `e_delta downarrow0` as `delta downarrow0`.

Let

\[
v_\delta:=E X_\delta^2.
\]

From (2.1), using `B=S/(lambda+S)<=S/lambda`,

\[
E B^2
\le
\frac{E S_\nu^2}{\lambda^2}
=
\frac{m E B^2+f_2 e_\delta^2}{\lambda^2}.
\]

Thus whenever `lambda^2>m`,

\[
\boxed{
v_\delta
\le
\frac{f_2}{\lambda^2-m}.}
\tag{3.1}
\]

Since `m>1`, this gives a uniform second-moment bound for all sufficiently small `delta` and

\[
\limsup_{\delta\downarrow0}v_\delta
\le
v_*:=\frac{f_2}{m^2-m}
=
\frac{f_2}{m(m-1)}.
\tag{3.2}
\]

No `E nu^3` term appears.

---

## 4. Identification of every critical subsequential limit

The normalized recursion is

\[
\boxed{
X_\delta\stackrel d=
\frac{Y_\delta}{m-\delta+e_\delta Y_\delta}.
}
\tag{4.1}
\]

Take any sequence `delta_n downarrow0`. The uniform second-moment bound makes the laws of `X_{delta_n}` tight. Along a subsequence let

\[
X_{\delta_n}\Rightarrow X.
\]

Because the first moments are uniformly integrable and `E X_delta=1`,

\[
E X=1.
\tag{4.2}
\]

Conditional on any fixed offspring value `nu=k`, iid child vectors converge weakly, and truncating the fixed offspring law at a large `k` shows

\[
Y_{\delta_n}\Rightarrow Y:=\sum_{i=1}^{\nu}X_i.
\]

Moreover

\[
P(e_{\delta_n}Y_{\delta_n}>\epsilon)
\le \frac{m e_{\delta_n}}\epsilon\longrightarrow0,
\]
so the denominator in (4.1) converges to `m` in probability. Hence every weak subsequential limit satisfies

\[
\boxed{
X\stackrel d=\frac1m\sum_{i=1}^{\nu}X_i.}
\tag{4.3}
\]

By lower semicontinuity, `E X^2<infinity`. Taking second moments in (4.3),

\[
E X^2
=
\frac{m E X^2+f_2}{m^2},
\]
therefore necessarily

\[
\boxed{E X^2=v_*}. 
\tag{4.4}
\]

Combining (4.4) with the limsup bound (3.2) gives

\[
\liminf_{\delta\downarrow0}v_\delta\ge v_*,
\]
so in fact

\[
\boxed{v_\delta\to v_*}. 
\tag{4.5}
\]

There is also uniqueness of the limiting law, not only uniqueness of its second moment. On the class of mean-one probability laws with finite second moment, let

\[
\mathcal T(\mu)=\mathcal L\left(\frac1m\sum_{i=1}^{\nu}Z_i\right),
\qquad Z_i\stackrel{iid}\sim\mu.
\]

If `(Z_i,Z_i')` are iid optimal `W_2` couplings of two mean-one laws, then the differences have mean zero and

\[
E\left(\sum_{i=1}^{\nu}(Z_i-Z_i')\right)^2
=m E(Z_1-Z_1')^2.
\]

Therefore

\[
\boxed{
W_2(\mathcal T\mu,\mathcal T\mu')
\le m^{-1/2}W_2(\mu,\mu').}
\tag{4.6}
\]

Since `m>1`, `mathcal T` is a strict contraction. Its unique mean-one finite-second-moment fixed point is the normalized Galton–Watson martingale limit `W`. Thus all subsequential limits coincide with `W`; weak convergence plus (4.5) upgrades to

\[
W_2(\mathcal L(X_\delta),\mathcal L(W))\to0.
\]

This proves Theorem 2.1.

---

## 5. Exact mean-escape scale from a companion identity

Put

\[
r_\delta:=\frac{e_\delta}{\delta}.
\]

Since `E X_delta=1`, (4.1) gives

\[
1=E\frac{Y_\delta}{m-\delta+e_\delta Y_\delta}.
\]

Using `E Y_delta=m`, subtract `(m-delta)` times the preceding identity from `E Y_delta=m`:

\[
\delta
=
 e_\delta E\frac{Y_\delta^2}{m-\delta+e_\delta Y_\delta}.
\]

Hence the exact companion identity is

\[
\boxed{
\frac1{r_\delta}
=E\frac{Y_\delta^2}{m-\delta+e_\delta Y_\delta}.}
\tag{5.1}
\]

The `W_2` convergence of `X_delta` implies `W_2` convergence of the random sums `Y_delta` to

\[
Y_0:=\sum_{i=1}^{\nu}W_i,
\]
indeed under the common-offspring optimal coupling

\[
E|Y_\delta-Y_0|^2
=m W_2(\mathcal L(X_\delta),\mathcal L(W))^2.
\tag{5.2}
\]

Thus `Y_delta^2` is uniformly integrable and

\[
E Y_\delta^2\to E Y_0^2.
\]

For a fixed lower bound `lambda_0>0`,

\[
0\le
\frac{Y_\delta^2}{m-\delta}
-
\frac{Y_\delta^2}{m-\delta+e_\delta Y_\delta}
=
\frac{e_\delta Y_\delta^3}
{(m-\delta)(m-\delta+e_\delta Y_\delta)}.
\]

No third moment is needed: rewrite the right side as

\[
\frac{Y_\delta^2}{m-\delta}
\frac{e_\delta Y_\delta}{m-\delta+e_\delta Y_\delta}.
\]

The second factor is bounded by `1` and converges to zero in probability, while the first factor is uniformly integrable. Therefore the expectation of the difference tends to zero. Consequently

\[
\frac1{r_\delta}
\longrightarrow
\frac1m E Y_0^2.
\tag{5.3}
\]

Using `E W=1` and (2.7),

\[
E Y_0^2
=m\frac{f_2}{m(m-1)}+f_2
=\frac{mf_2}{m-1}.
\]

Substituting into (5.3) yields

\[
\boxed{
r_\delta\to\frac{m-1}{f_2}.}
\tag{5.4}
\]

This proves Theorem 2.2.

---

## 6. Exact infinite-support branch-tail identity

Now use Aidekon's speed representation in the near-critical region `lambda>1`. With `a=m-1`, define for `n>=1`

\[
D_{n,\delta}
:=a-\delta+e_\delta\sum_{i=0}^{n}X_{\delta,i},
\tag{6.1}
\]

\[
h_n(\delta)
:=E\frac{X_{\delta,0}}{D_{n,\delta}}.
\tag{6.2}
\]

By exchangeability of the `n+1` child escape variables, Aidekon's weight can be written

\[
c_n(\lambda)=e_\delta h_n(\delta).
\tag{6.3}
\]

For `j>=1` define

\[
g_j(\delta)
:=E\frac{X_{\delta,0}X_{\delta,j+1}}
{D_{j,\delta}D_{j+1,\delta}}.
\tag{6.4}
\]

Adding one branch gives the exact telescoping identity

\[
\boxed{h_j-h_{j+1}=e_\delta g_j.}
\tag{6.5}
\]

Let

\[
x_j:=\frac{e_\delta g_j}{h_1}.
\]

Then for every finite `n`,

\[
\frac{h_n}{h_1}=1-\sum_{j=1}^{n-1}x_j.
\tag{6.6}
\]

Define

\[
T_j=P(\nu>j),
\qquad
A_j=E[(\nu-m)\mathbf1_{\{\nu>j\}}].
\tag{6.7}
\]

The coefficient `A_j` is nonnegative. One convenient proof is the covariance identity with an independent copy `nu'`:

\[
2A_j
=E[(\nu-\nu')
(\mathbf1_{\{\nu>j\}}-\mathbf1_{\{\nu'>j\}})]\ge0.
\tag{6.8}
\]

Since `nu>=1`, Tonelli gives

\[
\sum_{j\ge1}T_j
=E(\nu-1)=m-1,
\tag{6.9}
\]

and, under `E nu^2<infinity`,

\[
\sum_{j\ge1}A_j
=E[(\nu-m)(\nu-1)]
=\operatorname{Var}(\nu).
\tag{6.10}
\]

Aidekon's effective offspring mean is

\[
M_\delta
=\frac{E[\nu h_\nu]}{E[h_\nu]}.
\tag{6.11}
\]

Substitute (6.6), first for the denominator and then for the centered numerator. Because all tail coefficients in the resulting sums are nonnegative, Tonelli / monotone convergence justifies passage from finite truncations to infinite support. One obtains

\[
\frac{E[h_\nu]}{h_1}
=1-\sum_{j\ge1}T_jx_j,
\tag{6.12}
\]

and

\[
m-M_\delta
=
\frac{\sum_{j\ge1}A_jx_j}
{1-\sum_{j\ge1}T_jx_j}.
\tag{6.13}
\]

Equivalently, with

\[
K_\delta:=\sum_{j\ge1}A_jg_j,
\qquad
\bar h_\delta:=E[h_\nu],
\tag{6.14}
\]

we have the particularly useful exact form

\[
\boxed{
q_\delta:=m-M_\delta
=e_\delta\frac{K_\delta}{\bar h_\delta}.}
\tag{6.15}
\]

This proves Theorem 2.3.

### Core-tail error bound

The identity is not merely formal. Since `D_{j,delta}>=a-delta` and `X_{delta,0}` is independent of `X_{delta,j+1}`,

\[
0<g_j(\delta)
\le\frac{E[X_{\delta,0}X_{\delta,j+1}]}
{(a-\delta)^2}
=\frac1{(a-\delta)^2}.
\tag{6.16}
\]

Hence for any integer `J>=1`,

\[
\boxed{
0\le
K_\delta-\sum_{j=1}^{J-1}A_jg_j(\delta)
\le
\frac{V_J}{(a-\delta)^2},}
\tag{6.17}
\]

where

\[
V_J:=\sum_{j\ge J}A_j
=E[(\nu-m)(\nu-J)_+]
\downarrow0.
\tag{6.18}
\]

The last convergence follows from `sum_j A_j=Var(nu)<infinity`. Thus an unbounded offspring tail can be made arbitrarily cheap in the **value** of the exact critical tilt using only finite variance. This is the support-free core-tail bridge that was missing from `1308Z`.

---

## 7. Critical limit of the branch-tail functional with only a second moment

For fixed `n`, `D_{n,delta}->a` in probability. The `W_2` convergence from Theorem 2.1 and the lower bound `D_{n,delta}>=a-delta` imply

\[
\boxed{h_n(\delta)\longrightarrow\frac1a.}
\tag{7.1}
\]

Also for every fixed `j`, products of two independent normalized escape variables converge in `L^1`, so

\[
\boxed{g_j(\delta)\longrightarrow\frac1{a^2}.}
\tag{7.2}
\]

There are uniform summable dominators:

\[
0<h_n(\delta)\le\frac1{a-\delta},
\tag{7.3}
\]

and (6.16). Therefore dominated convergence with respect to the fixed offspring law and with respect to the summable coefficients `A_j` gives

\[
\boxed{
\bar h_\delta\longrightarrow\frac1a,
\qquad
K_\delta\longrightarrow
\frac{\operatorname{Var}(\nu)}{a^2}.}
\tag{7.4}
\]

Using (6.15),

\[
\boxed{
\frac{q_\delta}{e_\delta}
\longrightarrow
\frac{\operatorname{Var}(\nu)}a.}
\tag{7.5}
\]

Combine (7.5) with the escape scale (5.4):

\[
\boxed{
\frac{q_\delta}{\delta}
\longrightarrow
\frac{\operatorname{Var}(\nu)}{f_2}.}
\tag{7.6}
\]

Since `q_delta=m-M_delta`, this is exactly (2.13).

A useful check is

\[
f_2
=E[\nu(\nu-1)]
=\operatorname{Var}(\nu)+m(m-1),
\]
so the critical defect left for actual forward speed is

\[
1-\frac{\operatorname{Var}(\nu)}{f_2}
=
\frac{m(m-1)}{f_2}>0.
\tag{7.7}
\]

---

## 8. Finite-second-moment speed asymptotic

Aidekon's representation is

\[
\ell_\lambda
=\frac{M_\lambda-\lambda}{M_\lambda+\lambda}.
\tag{8.1}
\]

With `lambda=m-delta` and `M=m-q_delta`,

\[
M-\lambda
=\delta-q_\delta
=
\frac{m(m-1)}{f_2}\,\delta+o(\delta),
\tag{8.2}
\]

while `M+lambda->2m`. Hence

\[
\boxed{
\ell_{m-\delta}
=\frac{m-1}{2f_2}\,\delta+o(\delta).}
\tag{8.3}
\]

This proves Theorem 2.4.

For any fixed `r in (0,1)`, subtracting the expansions at `delta` and `r delta` gives

\[
\ell_{m-\delta}-\ell_{m-r\delta}
=
\frac{m-1}{2f_2}(1-r)\delta+o(\delta)>0
\]
for all sufficiently small `delta`, proving (2.15).

### Sanity check: regular tree

If `nu=d` deterministically, then `f_2=d(d-1)` and (8.3) gives coefficient `1/(2d)`. The exact regular-tree speed

\[
\ell_\lambda=\frac{d-\lambda}{d+\lambda}
\]
has exactly this critical slope.

---

## 9. Heavy-tailed example genuinely outside the previous theorem

The moment weakening is nonempty. Let

\[
P(\nu=1)=\frac12,
\]

and for `n>=1`,

\[
P(\nu=n+1)
=\frac12\frac{n^{-7/2}}{\zeta(7/2)}.
\tag{9.1}
\]

Then

\[
E\nu^2<\infty,
\qquad
E\nu^3=\infty.
\]

Thus none of the inherited finite-third-moment terminal proofs applies. Here

\[
m
=1+\frac12\frac{\zeta(5/2)}{\zeta(7/2)}
\approx1.5952990747,
\]

and

\[
f_2
=\frac12\frac{\zeta(3/2)+\zeta(5/2)}{\zeta(7/2)}
\approx1.7545681019.
\]

Therefore the new theorem gives

\[
\boxed{
\ell_\lambda
=0.1696426243\,(m-\lambda)+o(m-\lambda)
}
\tag{9.2}
\]

from the transient side, together with `W_2` convergence of the normalized escape profile. This example also has minimum offspring one, so it lies outside the `d>=2` source-uniform low-parent-bias theorem.

---

## 10. Why this still does not prove a whole terminal interval under only finite variance

The new finite-variance argument controls the **value** of the critical tilt sharply enough to identify its first-order limit. It does not yet provide a uniform secant estimate

\[
|q_\delta-q_\eta
-\theta(\delta-\eta)|
\le o(1)|\delta-\eta|
\quad\text{with}\quad
\theta=\frac{\operatorname{Var}(\nu)}{f_2}
\tag{10.1}
\]
for all arbitrarily close `delta,eta` in a terminal interval.

That distinction is essential. A remainder `o(delta)` cannot simply be differentiated. The earlier finite-third-moment and bounded-support reports obtained `O_Lip(delta^2)` control by differentiating / coupling branch weights with enough integrability to pay for an additional offspring factor. Under only a second moment, the infinite tail in the derivative of `K_delta` is the unresolved object.

The core-tail estimate (6.17) shows that the **amplitude** of the tail is harmless:

\[
K_\delta^{tail}(J)
\le V_J/(a-\delta)^2,
\qquad V_J\downarrow0.
\]

But amplitude alone does not bound a quotient

\[
\frac{K_\delta^{tail}(J)-K_\eta^{tail}(J)}{\delta-\eta}
\]
when `delta-eta` is arbitrarily small. A new monotonicity, bounded-variation, or amortized-derivative estimate on the weighted tail is required.

This is the exact remaining gap; claiming whole-interval monotonicity from (8.3) would be invalid.

---

## 11. Next analytic attack

The next run should work directly with the support-free aggregate

\[
K_\delta
=\sum_{j\ge1}A_jg_j(\delta)
\]
rather than controlling every branch coordinate separately.

The concrete plan is:

1. **Finite core:** for fixed `J`, use the `W_2` critical profile and the exact denominators to derive a secant bound for `sum_{j<J}A_jg_j` requiring only second moments; all constants may depend on `J`.
2. **Tail:** seek a one-sided or bounded-variation inequality for `g_j(delta)` as a function of `delta` which, after weighting by `A_j`, costs only `sum A_j=Var(nu)` rather than `sum j A_j` (the latter is essentially a third-moment demand).
3. **Possible bridge from P03-B:** its new theorem says complete stacks of returning descendant loops move in the favorable direction for `beta d>1`. For minimum offspring `d>=2`, test whether that favorable sign can be translated into a one-sided derivative estimate for the large-`j` part of `g_j`; this would leave only the finite analytic core to control. Do not duplicate P03-B's path coupling itself.
4. If the tail derivative genuinely requires more than finite variance, quantify the weakest extra moment or Orlicz modulus needed and prove a terminal monotonicity theorem at that threshold rather than reverting to a hard support cutoff.

A successful version of item 2 would upgrade the present finite-second-moment asymptotic into a support-free whole terminal interval and would strictly improve the `0906Z` finite-third-moment terminal theorem.

---

## 12. Obligation ledger

- **Full LPP conjecture:** unchanged, `R_full: 1 -> 1`.
- **Current broad published interval:** inherited Song–Wang–Xiang `d>=2` interval; unchanged.
- **Critical escape profile:** improved from moment asymptotics to exact `W_2` identification under `E nu^2<infinity`.
- **Critical escape slope:** assumption weakened from `E nu^3<infinity` to `E nu^2<infinity`.
- **Critical speed slope:** assumption weakened from `E nu^3<infinity` to `E nu^2<infinity`.
- **Branch-vector identity:** upgraded from fixed bounded support to an exact countable support-free tail identity.
- **Core-tail value control:** new finite-variance bound (6.17).
- **Whole terminal monotonicity interval under finite variance:** still open; the missing object is a support-free secant/derivative bound for the weighted tail.

No publication, email, Drive action, force-push, history rewrite, peer overwrite, or ownership change was performed.
