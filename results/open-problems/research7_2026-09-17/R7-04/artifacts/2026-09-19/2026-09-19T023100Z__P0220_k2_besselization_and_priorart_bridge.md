# P0220 — explicit two-coordinate Bessel law and prior-art bridge

Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

Target: David Aldous, *A one-dimensional drift-jump particle process*, maintained problem page posted February 2018, <https://www.stat.berkeley.edu/~aldous/Research/OP/left_Hamm.html>.

Historical source: David Aldous and Persi Diaconis, unfinished notes *Patience Sorting, Longest Increasing Subsequences and a Continuous Space Analog of the Simple Asymmetric Exclusion Process* (8 July 1993), Sections 4.1–4.2, <https://www.stat.berkeley.edu/~aldous/Research/OP/patience.pdf>.

This artifact is deliberately conservative about novelty. The 1993 notes already contain the stationary representation (42), the exact `k=2` pile-top distribution (45), the two-coordinate density factorization (47)–(48), and the Laplace transform of the gap density. The Bessel forms below are exact simplifications and cross-checks of that historical calculation, not claims that the `k=2` law is new. The source-level contribution under investigation remains the all-finite-dimensional Plancherel/Schur/Fredholm identification proved in the preceding R7-04 artifacts.

## 1. Historical inputs and notation

Write the stationary ordered particles as

\[
0<X_1<X_2<\cdots.
\]

The 1993 notes prove in equation (42) that, for every fixed `k`,

\[
(X_1,\ldots,X_k)\overset d=
(\Gamma(B(1)),\ldots,\Gamma(B(k))),
\]

where `Gamma(1),Gamma(2),...` are the successive points of an independent rate-one Poisson process on the positive half-line and `B(j)` are the stabilized patience-pile top labels.

For `k=2`, their equation (45) gives

\[
\Pr\{B(2)=b\}=\frac{1}{b(b-2)!},\qquad b=2,3,\ldots.
\]

Their equations (47)–(48) give, for `0<x_1<x_2`,

\[
p_2(x_1,x_2)=e^{-x_1}a(x_2-x_1),
\]

where, with `q(u,i)=e^{-u}u^i/i!`,

\[
a(u)=\sum_{i=0}^{\infty}q(u,i)
\left(\frac1{(i+1)!}-\frac1{(i+2)!}\right).
\]

Thus the notes already contain the essential factorization. We now put it into a compact Bessel form and derive several exact consequences that can be compared directly with the Plancherel/Fredholm description.

## 2. Method B4 — prove a weaker object completely: a closed two-coordinate Bessel law

### Proposition 2.1 (Bessel form of the historical gap density)

For `u>0`,

\[
\boxed{
 a(u)=e^{-u}
 \left[
 \frac{I_1(2\sqrt u)}{\sqrt u}
 -
 \frac{I_2(2\sqrt u)}{u}
 \right],
}
\]

where `I_nu` is the modified Bessel function of the first kind. Consequently

\[
\boxed{
 p_2(x_1,x_2)
 =e^{-x_2}
 \left[
 \frac{I_1(2\sqrt{x_2-x_1})}{\sqrt{x_2-x_1}}
 -
 \frac{I_2(2\sqrt{x_2-x_1})}{x_2-x_1}
 \right]
}
\]
for `0<x_1<x_2`.

#### Proof

The Bessel series are

\[
I_1(2\sqrt u)
 =\sum_{i\ge0}\frac{u^{i+1/2}}{i!(i+1)!},
\qquad
I_2(2\sqrt u)
 =\sum_{i\ge0}\frac{u^{i+1}}{i!(i+2)!}.
\]

Therefore

\[
\frac{I_1(2\sqrt u)}{\sqrt u}
-\frac{I_2(2\sqrt u)}{u}
=\sum_{i\ge0}\frac{u^i}{i!}
\left(\frac1{(i+1)!}-\frac1{(i+2)!}\right).
\]

Multiplying by `e^{-u}` gives exactly the historical equation (48). Since `p_2(x_1,x_2)=e^{-x_1}a(x_2-x_1)` and `x_1+(x_2-x_1)=x_2`, the displayed density follows. QED.

### Corollary 2.2 (independent first particle and gap)

Let

\[
G:=X_2-X_1.
\]

Then

\[
\boxed{X_1\sim\operatorname{Exp}(1),\qquad X_1\perp G,\qquad G\text{ has density }a.}
\]

This is already implicit in the historical factorization `p_2(x_1,x_2)=e^{-x_1}a(x_2-x_1)` together with their check `\int_0^\infty a(u)du=1`.

### Proposition 2.3 (closed gap survival)

For `u>=0`,

\[
\boxed{
\Pr(G>u)=e^{-u}\frac{I_1(2\sqrt u)}{\sqrt u},
}
\]
with the value at `u=0` understood by continuity as `1`.

#### Proof

Put

\[
g(u):=\frac{I_1(2\sqrt u)}{\sqrt u}
      =\sum_{i\ge0}\frac{u^i}{i!(i+1)!}.
\]

Termwise differentiation gives

\[
g'(u)=\sum_{i\ge0}\frac{u^i}{i!(i+2)!}
      =\frac{I_2(2\sqrt u)}{u}.
\]

Hence

\[
-\frac{d}{du}\bigl(e^{-u}g(u)\bigr)
=e^{-u}[g(u)-g'(u)]
=a(u).
\]

The boundary values are `e^{-u}g(u)->0` as `u->infinity` and `g(0)=1`, so this is precisely the survival function of `G`. QED.

### Proposition 2.4 (fully explicit two-coordinate joint survival)

For `s,t>=0`,

\[
\boxed{
\Pr(X_1>s,\,X_2>t)
=
\begin{cases}
 e^{-s}, & s\ge t,\\[3pt]
 e^{-t} I_0(2\sqrt{t-s}), & 0\le s<t.
\end{cases}
}
\]

#### Proof

If `s>=t`, the ordering `X_2>X_1` makes `X_1>s` imply `X_2>t`, so the probability is `e^{-s}`.

For `s<t`, use Corollary 2.2 and split according to whether `X_1<t`:

\[
\begin{aligned}
\Pr(X_1>s,X_2>t)
&=\int_s^t e^{-x}\Pr(G>t-x)\,dx+\int_t^\infty e^{-x}\,dx\\
&=e^{-t}\left[
1+\int_0^{t-s}\frac{I_1(2\sqrt u)}{\sqrt u}\,du
\right].
\end{aligned}
\]

The identity

\[
\frac{d}{du}I_0(2\sqrt u)=\frac{I_1(2\sqrt u)}{\sqrt u}
\]

and `I_0(0)=1` give the result. QED.

Differentiating the `s<t` formula once in each threshold recovers Proposition 2.1, which is a direct internal consistency check.

### Proposition 2.5 (joint Laplace transform and low moments)

For `alpha,beta>=0`,

\[
\boxed{
\mathbb E e^{-\alpha X_1-\beta X_2}
=
\frac{1+\beta-\beta\exp\!\bigl((1+\beta)^{-1}\bigr)}
     {1+\alpha+\beta}.
}
\]

Moreover

\[
\boxed{
\mathbb E X_1=1,\quad
\mathbb E(X_2-X_1)=e-1,\quad
\mathbb E X_2=e,
}
\]

and

\[
\boxed{
\operatorname{Var}(X_1)=1,\quad
\operatorname{Var}(X_2-X_1)=4e-e^2-1,\quad
\operatorname{Var}(X_2)=4e-e^2,
\quad
\operatorname{Cov}(X_1,X_2)=1.
}
\]

#### Proof

The 1993 notes already calculate the Laplace transform of `a`:

\[
\int_0^\infty a(u)e^{-\beta u}\,du
=1+\beta-\beta\exp\!\left(\frac1{1+\beta}\right).
\]

Independence of `X_1` and `G=X_2-X_1` gives

\[
\mathbb E e^{-\alpha X_1-\beta X_2}
=
\mathbb E e^{-(\alpha+\beta)X_1}\,
\mathbb E e^{-\beta G},
\]

which is the stated transform. Differentiation at zero gives the moments. Equivalently, from `B(2)` one gets `E B(2)=e` and `E B(2)^2=3e`, while conditional Gamma moments give the same formulas. QED.

## 3. Method B17 — match the low-dimensional coefficients to the Plancherel-growth representation

The preceding R7-04 work identified the stationary particles with first-row hitting times of a rate-one poissonized Plancherel growth process:

\[
(X_1,X_2,\ldots)\overset d=(\tau_1,\tau_2,\ldots),
\qquad
\tau_k:=\inf\{t:\Lambda_1(t)\ge k\}.
\]

For the two-threshold survival event and `0<=s<t`, the strong Markov property at time `s` plus the condition `\tau_1>s` says that no Plancherel-growth arrival has occurred by time `s`. During the remaining interval of length `u=t-s`, the event `\tau_2>t` is exactly that the Young diagram has first row of length `<2`.

There is exactly one partition of each size `n` with first row `<2`, namely the column `(1^n)`, and its standard-tableau dimension is `f^{(1^n)}=1`. Under rate-one poissonized Plancherel measure,

\[
\Pr\{\Lambda(u)=(1^n)\}
=e^{-u}\frac{u^n}{(n!)^2}.
\]

Therefore

\[
\Pr(\tau_1>s,\tau_2>t)
=e^{-s}e^{-u}\sum_{n\ge0}\frac{u^n}{(n!)^2}
=e^{-t}I_0(2\sqrt{t-s}),
\]

which matches Proposition 2.4 coefficient by coefficient.

This is an important normalization check: the `k=2` formula obtained directly from the 1993 patience-pile calculation agrees exactly with the later Plancherel-growth representation and with the equal-time discrete-Bessel normalization used in the previous Fredholm artifact.

Published context, checked 2026-09-19:

- M. Nica, *Decorated Young Tableaux and the Poissonized Robinson-Schensted Process*, arXiv:1404.4015 / SPA 127 (2017), identifies the poissonized RS Young-diagram trajectory as a Schur process and as nonintersecting Poisson walkers. The searchable text contains no occurrence of `Aldous`, `patience`, or `Hammersley`; thus this paper is powerful machinery but not, from the bounded text search, an explicit citation to the present source problem.
- A. Borodin and G. Olshanski, *Stochastic dynamics related to Plancherel measure on partitions*, arXiv:math-ph/0402064 / J. Math. Sci. 144 (2007), gives dynamical Plancherel correlations and discrete-Bessel structure.
- M. Marciniak, L. Maslanka, P. Sniady, *Poisson limit theorems for the Robinson-Schensted correspondence and for the multi-line Hammersley process*, arXiv:2005.13824 / Adv. Appl. Math. 145 (2023), studies a different bulk/bottom-row scaling regime. Its Theorem 1.1 concerns Poisson limits of bottom rows and its Hammersley interpretation is the classical/multi-line Hammersley process; this is not the fixed-leftmost-pile drift-jump stationary vector posed by Aldous in 2018.

Hence the low-dimensional coefficients line up with the known Plancherel machinery, while no bounded search hit yet identifies the exact Aldous 2018 finite-leftmost-pile stationary law with the Schur/Fredholm formula.

## 4. Method B22 — read the failures, not only the successes

The 1993 notes make the historical bottleneck unusually explicit.

1. Equation (42) already gives the stationary vector as `Gamma(B(i))`.
2. Equation (43) gives an automatic balance equation for the stationary density `p_k`, immediately followed by the authors' statement that it seemed impossible to extract useful information from that equation.
3. Section 4.2 explicitly solves `k=2`: equations (45)–(48) give `B(2)`, `p_2`, and the gap density; later on the same section calculates the gap Laplace transform.
4. The notes say it would be attractive if the limiting spatial sequence were Markov in `i`, but that this appears false. The preceding R7-04 exact computation independently found a hidden-shape obstruction to a naive one-step hitting-time Markov compression.

This identifies the precise historical gap: **not `k=2`, and not existence, but extracting an explicit all-`k` law from the stabilized-pile representation.** The previous R7-04 Schur/Fredholm representation attacks exactly that bottleneck by changing category from the balance PDE to Plancherel growth / determinantal gap probabilities.

The most relevant post-1993 papers found in the bounded search develop all of the needed integrable machinery, but in adjacent language. Nica's paper explicitly says its multi-time Young-diagram law is a Schur process, while Borodin–Olshanski compute dynamical Plancherel/discrete-Bessel correlations. The 2020/2023 Marciniak–Maslanka–Sniady paper is a particularly important false friend: despite the phrase “multi-line Hammersley process” and an explicit stationary Poisson limit, it studies bottom rows in a large-`n` scaling window, whereas Aldous's 2018 problem freezes the first `k` patience piles and applies the exponential time/space transformation that yields the drift `dX_i/dt=X_i`.

Thus the current prior-art classification remains:

- historical `k=2`: **KNOWN in the 1993 notes**;
- general Plancherel/Schur/determinantal machinery: **KNOWN**;
- exact source-specific composition from Aldous's stationary vector to the all-finite-dimensional half-line Fredholm formula: **not located in the bounded 2026-09-19 search, but a search miss is not evidence of novelty**.

## 5. Consequences for the source-level proof package

The two-coordinate calculation is useful for auditing the general formula, but it does **not** advance the frozen metric `K_Bessel`, which was already `infinity` after all scalar marginals were derived.

What it does establish is a sharp compatibility triangle:

1. Aldous–Diaconis 1993 pile-top formula;
2. rate-one Plancherel first-row hitting times;
3. the extended-Bessel/Schur Fredholm law from the preceding R7-04 artifact.

All three give the same exact `k=2` survival law

\[
\Pr(X_1>s,X_2>t)
=
\begin{cases}
e^{-s},&s\ge t,\\
e^{-t}I_0(2\sqrt{t-s}),&s<t.
\end{cases}
\]

This removes a normalization concern from the preceding all-dimensional formula and clarifies exactly which part of the low-dimensional answer was already present historically.

## 6. Honest status

`P0220`: **OPEN / PARTIAL** under the repository protocol.

The all-dimensional Fredholm formula remains a mathematically complete candidate answer to the literal source request, but source closure is not asserted because:

- an exact source-specific prior-art priority check is still incomplete;
- no independent P26 full-proof audit has passed;
- no distinct OTHER-track full-proof audit has passed;
- no audit-complete self-contained paper package exists.

Frozen metric in this run: `K_Bessel = infinity -> infinity` (**NO MOVEMENT**).

This is the second consecutive ordinary unchanged P0220 run after the metric saturated.

Next nonrepeating methods proposed for the next ordinary research iteration: **B8 / B19 / B26** — discretize the Fredholm event to a finite determinant hierarchy, make the source formula an executable constructive algorithm for arbitrary finite thresholds, and hunt for a small sporadic normalization/sign failure before any closure packaging.
