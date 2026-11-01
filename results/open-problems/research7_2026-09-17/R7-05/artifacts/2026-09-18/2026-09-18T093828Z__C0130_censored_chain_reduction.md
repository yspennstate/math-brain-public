# C0130 — finite censored-chain reduction for bounded-cookie escape probabilities

Model actually running: GPT-5.6 Sol. Reasoning level: UNVERIFIED. This is not GPT-6 at maximum; authenticated runtime reasoning-effort telemetry and a binding model/effort selector are not exposed.

Target: `C0130`, Kosygina–Zerner Problem 3.12 (escape probability for a transient one-dimensional excited random walk).

Status of this artifact: **PARTIAL relative to the full outside source**. It proves an exact reduction for every i.i.d. bounded finite-cookie law in the right-transient regime and a certified finite-state approximation scheme for rational finite-support laws. It does **not** claim a closed cookie-polynomial formula for arbitrary depth, does not cover every stationary-ergodic source setting, and therefore does not close Problem 3.12.

## 1. Setup

At each site let the cookie stack be an i.i.d. copy of

\[
(p_1,\ldots,p_M,1/2,1/2,\ldots),\qquad M\ge2,
\]

with the usual weak ellipticity hypotheses under which the standard backward branching-like chain is irreducible. Put

\[
\delta=\mathbb E\sum_{j=1}^M(2p_j-1)>1.
\]

For a fresh site let `F_m` be the number of failures before the `m`-th success in the cookie Bernoulli sequence, annealed over the site stack, and let

\[
Z_{n+1}=F_{n+1,Z_n+1}
\]

be the backward chain, with transition kernel `P`. In the right-transient regime it is positive recurrent; write `pi` for its stationary law. The preceding R7-05 artifact proved

\[
\boxed{p_{\rm esc}=\mathbb E[p_1]\,\pi_0.}
\tag{1.1}
\]

The new result below replaces the full infinite stationary law by the stationary law of a finite censored chain.

## 2. Method B3 — prove something stronger: the arbitrary finite-depth boundary formula

Define the finite boundary

\[
S=\{0,1,\ldots,M-2\}.
\]

For `r in S` set

\[
m_r=\mathbb E[F_{r+1}],
\qquad
c_r=m_r+\delta-r-1.
\tag{2.1}
\]

### Theorem 2.1 (finite boundary/censoring formula)

Let

\[
\tau_S^+=\inf\{n\ge1:Z_n\in S\}
\]

and define the `(M-1) x (M-1)` censored transition matrix

\[
B_{rs}=\mathbb P_r(Z_{\tau_S^+}=s),\qquad r,s\in S.
\tag{2.2}
\]

Let `nu` be the unique stationary probability vector of `B`. Then

\[
\boxed{
\pi_r=
\frac{\delta-1}{\sum_{j\in S}\nu_jc_j}\,\nu_r,
\qquad r\in S.
}
\tag{2.3}
\]

In particular,

\[
\boxed{
p_{\rm esc}
=
\mathbb E[p_1]
\frac{(\delta-1)\nu_0}{\sum_{j\in S}\nu_jc_j}.
}
\tag{2.4}
\]

Thus, for every finite cookie depth, the escape probability depends on the infinite backward chain only through the return kernel to the finite set `S`.

### Proof, Part A: a finite-mean-free drift balance

Let

\[
K=\sum_{j=1}^M Y_j
\]

be the number of successes among the first `M` cookie tosses, and let `a_k=P(K=k)`. For `i>=M-1`, after those first `M` tosses there are `M-K` failures and `i+1-K` successes still required from fair Bernoulli trials. Hence

\[
\mathbb E[s^{F_{i+1}}]
=Q(s)T(s)^{i+1},
\tag{2.5}
\]

where

\[
T(s)=\frac1{2-s},
\qquad
Q(s)=\sum_{k=0}^M a_k s^{M-k}(2-s)^k.
\]

If

\[
G(s)=\sum_{i\ge0}\pi_i s^i,
\qquad
P_r(s)=\mathbb E[s^{F_{r+1}}],
\]

stationarity gives

\[
G(s)=
\sum_{r\in S}\pi_rP_r(s)
+Q(s)T(s)
\left(
G(T(s))-\sum_{r\in S}\pi_rT(s)^r
\right).
\tag{2.6}
\]

Write `x=1-s`. As in the preceding depth-three argument,

\[
0\le \frac{G(T(s))-G(s)}{1-s}\le1
\]

termwise after averaging, and dominated convergence yields

\[
\frac{G(T(s))-G(s)}{1-s}\longrightarrow0.
\tag{2.7}
\]

No stationary first moment is assumed.

Also

\[
Q(1-x)=1+\delta x+O(x^2),
\qquad
T(1-x)=1-x+O(x^2),
\]

so

\[
Q(s)T(s)=1+(\delta-1)x+O(x^2).
\]

For fixed `r in S`,

\[
P_r(1-x)=1-m_rx+o(x),
\qquad
T(1-x)^r=1-rx+O(x^2).
\]

Subtract the tail term in (2.6), divide by `x`, and let `x downarrow 0`. The left side tends to `-(delta-1)` by (2.7), while the `r`-th boundary term tends to `-c_r`. Therefore

\[
\boxed{
\sum_{r\in S}\pi_rc_r=\delta-1.
}
\tag{2.8}
\]

This is the arbitrary-depth version of the three-cookie balance from the previous run.

### Proof, Part B: the conserved harmonic measures

For each `s in S`, define

\[
h_s(i)=\mathbb P_i(Z_{\tau_S}=s),
\qquad
\tau_S=\inf\{n\ge0:Z_n\in S\}.
\tag{2.9}
\]

Because the chain is irreducible positive recurrent, `tau_S<infinity` almost surely from every state. Hence

\[
h_s(r)=\mathbf 1_{\{r=s\}},\quad r\in S,
\]

and

\[
Ph_s(i)=h_s(i),\quad i\notin S.
\tag{2.10}
\]

For `r in S`, one step followed by the first return to `S` gives

\[
Ph_s(r)=B_{rs}.
\tag{2.11}
\]

Stationarity of `pi` and boundedness of `h_s` imply

\[
0=\sum_i\pi_i(Ph_s(i)-h_s(i))
 =\sum_{r\in S}\pi_r(B_{rs}-\mathbf 1_{\{r=s\}}).
\]

Thus the boundary row vector `pi_S=(pi_r)_{r in S}` satisfies

\[
\boxed{\pi_SB=\pi_S.}
\tag{2.12}
\]

Since `B` is irreducible and stochastic, its invariant probability vector is unique, so

\[
\pi_r=a\nu_r
\]

for a single scalar `a=pi(S)`. Substitute this in (2.8):

\[
a\sum_{r\in S}\nu_rc_r=\delta-1.
\]

This proves (2.3), and (1.1) gives (2.4). QED.

## 3. Method B12 — what is conserved

The functions `h_s` are the missing conserved observables. Stopped on entry to `S`, each

\[
h_s(Z_{n\wedge\tau_S})
\]

is a bounded martingale. The entire vector of boundary harmonic measures is therefore conserved through every excursion outside `S`. Equation (2.12) says exactly that the stationary mass seen on the boundary must be stationary for the excursion-return chain.

This is stronger than trying successive polynomial moments of `Z`: polynomial drift identities keep introducing unknown tail moments, whereas the harmonic-measure invariants remove the whole tail at once and retain only a finite `(M-1)`-state trace chain.

For `M=2`, `S={0}`, `nu_0=1`; (2.4) reduces to the source-cited Zerner formula.

For `M=3`, `S={0,1}`. Write

\[
B=
\begin{pmatrix}
1-B_{01}&B_{01}\\
B_{10}&1-B_{10}
\end{pmatrix}.
\]

Then

\[
\nu_0=\frac{B_{10}}{B_{01}+B_{10}},
\qquad
\nu_1=\frac{B_{01}}{B_{01}+B_{10}},
\]

and therefore

\[
\boxed{
p_{\rm esc}
=\mathbb E[p_1](\delta-1)
\frac{B_{10}}{c_0B_{10}+c_1B_{01}}.
}
\tag{3.1}
\]

Equivalently, if `kappa=B_{01}/B_{10}`,

\[
\pi_0=\frac{\delta-1}{c_0+c_1\kappa}.
\tag{3.2}
\]

This identifies the single missing scalar in the previous three-cookie report: it is not an arbitrary stationary atom, but the ratio of the two excursion-return probabilities of the censored chain.

## 4. Method B29 — compactify the tail and obtain certified finite brackets

The only remaining infinite object in (2.4) is `B`. It has a direct exact truncation with an explicit point at infinity.

Fix `N>=M` and put

\[
T_N=\{M-1,M,\ldots,N-1\}.
\]

For `s in S`, define on `T_N`

\[
\ell_{s,N}(i)
=\mathbb P_i(Z_{\tau_{S,N}}=s),
\]

where

\[
\tau_{S,N}=\inf\{n\ge0:Z_n\in S\text{ or }Z_n\ge N\}.
\]

Also define

\[
e_N(i)=\mathbb P_i(Z_{\tau_{S,N}}\ge N).
\]

Then by the strong Markov property and `0<=h_s<=1`,

\[
\boxed{
\ell_{s,N}(i)
\le h_s(i)
\le \ell_{s,N}(i)+e_N(i).
}
\tag{4.1}
\]

Both functions solve finite linear systems on `T_N`:

\[
\ell_{s,N}(i)
=P(i,s)+\sum_{j\in T_N}P(i,j)\ell_{s,N}(j),
\tag{4.2}
\]

\[
e_N(i)
=P(i,[N,\infty))+\sum_{j\in T_N}P(i,j)e_N(j).
\tag{4.3}
\]

For `r in S`, insert these bounds after the first step to obtain exact lower and upper bounds on every `B_{rs}`. Because `tau_S<infinity` almost surely, the path maximum before `tau_S` is finite almost surely, so

\[
e_N(i)\downarrow0
\]

for each fixed `i`, and the first-step tail from a fixed boundary state also tends to zero. Consequently the finite brackets converge to the exact censored matrix `B`.

If the cookie law has finite rational support and rational cookie probabilities, every transition probability entering (4.2)–(4.3), including `P(i,[N,infinity))`, is rational: after the finitely many cookies, the remaining failures have a negative-binomial law with parameter `1/2`. Hence every finite bracket is an exact rational certificate.

This gives a deterministic certified algorithm for the finite-depth i.i.d. problem: increase `N`, solve rational linear systems, bracket `B`, solve the finite censored stationary problem, and insert the result into (2.4). It is an arbitrary-precision computation, not a new closed symbolic formula.

## 5. Exact three-cookie demonstration: deterministic `(4/5,4/5,4/5)`

For

\[
p_1=p_2=p_3=\frac45,
\]

we have

\[
\delta=\frac95,
\qquad
c_0=\frac{132}{125},
\qquad
c_1=\frac{48}{125},
\qquad
\mathbb E[p_1]=\frac45.
\]

The exact-rational truncation checker archived with this artifact gives, at `N=12`,

\[
0.24442620065696785<\kappa<0.24929359720638114,
\]

and therefore

\[
\boxed{
0.555686401697734
< p_{\rm esc}<
0.556589661919537.
}
\tag{5.1}
\]

The endpoints are exact rationals in the archived checker output. This strictly improves the previous balance-only interval

\[
\frac{52}{105}\le p_{\rm esc}\le\frac{20}{33}.
\]

The `N=8,10,12` exact intervals are nested in the correct direction; the checker terminates with `ALL_EXACT_CHECKS_PASS`.

## 6. Scope and blocker after this run

What is now proved:

1. The infinite stationary-law problem at arbitrary finite cookie depth reduces exactly to a finite censored chain on `M-1` states.
2. The missing depth-three scalar is exactly `B_{01}/B_{10}`.
3. Rational finite-support stacks admit certified rational brackets converging to the exact escape probability.

What is **not** proved:

1. A closed cookie-polynomial or special-function expression for the censored matrix `B` at arbitrary depth.
2. The broader stationary-ergodic source scope outside the i.i.d. finite-cookie class.
3. Any source-level closure or publication novelty claim.

Accordingly the frozen metric remains `M_closed=2`: the new theorem is a general exact reduction and certified algorithm, but not yet the metric's required universal closed formula at depth three.
