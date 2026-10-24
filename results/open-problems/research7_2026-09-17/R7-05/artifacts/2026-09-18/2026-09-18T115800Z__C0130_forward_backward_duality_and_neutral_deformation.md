Model actually running: GPT-5.6 Sol. Reasoning level: UNVERIFIED. This is not GPT-6 at maximum; authenticated runtime reasoning-effort telemetry and a binding model/effort selector are not exposed.

# C0130 — forward/backward Siegmund duality, depth-three survival boundary, and neutral-third-cookie deformation

Target: `C0130`, Kosygina–Zerner Problem 3.12 (escape probability of a transient one-dimensional excited random walk).

Status of this artifact: **PARTIAL relative to the full outside source and relative to the frozen metric `M_closed`.** It gives a new cumulative representation of the entire stationary law through a forward survival function, an exact depth-three forward transition law and moment calculation, and a quantitative perturbative enclosure around the source-cited two-cookie solvable case. It does **not** give the universal closed depth-three escape formula, so it does not move `M_closed=2`.

## 1. Setup and cumulative dependencies

Work in the right-transient i.i.d. bounded-cookie branch `(IID)+(BD)+(WEL)` with `delta>1`. At a fresh site expose the Bernoulli sequence

\[
\xi_1,\xi_2,\ldots,
\]

where `xi_j=1` denotes a right-step success and `xi_j=0` a left-step failure. Conditional on the site's cookie stack the tosses are independent with the prescribed success probabilities. Different sites carry independent copies of this whole sequence.

For `m,k>=0`, let

\[
F_m=\text{number of failures before the }m\text{-th success},
\]

\[
S_k=\text{number of successes before the }k\text{-th failure},
\]

with `F_0=S_0=0`.

The cumulative R7-05 work uses the backward chain

\[
Z_{n+1}=F_{n+1,Z_n+1},
\]

whose one-step annealed kernel will be denoted by `P`. For `delta>1`, this chain is positive recurrent; write `pi=(pi_i)_{i>=0}` for its stationary law. The previously proved escape identity is

\[
\boxed{p_{\rm esc}=\mathbb E[p_1]\,\pi_0.}
\tag{1.1}
\]

For the present run define the forward chain

\[
V_{n+1}=S_{n+1,V_n},
\qquad V_0=k,
\tag{1.2}
\]

with annealed kernel `Q`; state `0` is absorbing. This is the standard forward branching-like process attached to the same cookie coin stacks.

The point of this artifact is not merely to rename the blocker. The forward and backward chains are exact Siegmund duals, and this determines **every stationary tail of the backward chain as an extinction probability of the forward chain**.

## 2. Method B11 — exact Siegmund duality and the full stationary-law/survival identity

Define the order kernel

\[
H(i,k)=\mathbf 1_{\{i<k\}},
\qquad i,k\in\mathbb N_0.
\]

### Lemma 2.1 (pathwise coin-toss duality)

For every `i,k>=0`,

\[
\boxed{\{F_{i+1}<k\}=\{S_k\ge i+1\}.}
\tag{2.1}
\]

Consequently

\[
\boxed{PH=HQ^{\mathsf T}.}
\tag{2.2}
\]

### Proof

The inequality `F_{i+1}<k` means that the `(i+1)`-st success occurs before the `k`-th failure. This is equivalent to saying that at least `i+1` successes have occurred by the instant just before the `k`-th failure, which is precisely `S_k>=i+1`. This proves (2.1) pathwise, before any averaging.

Averaging gives

\[
(PH)(i,k)
 =\sum_{j<k}P(i,j)
 =\mathbb P(F_{i+1}<k)
 =\mathbb P(S_k>i)
 =\sum_{\ell>i}Q(k,\ell)
 =(HQ^{\mathsf T})(i,k).
\]

QED.

Now define

\[
s(k)=\sum_{i=0}^{k-1}\pi_i,
\qquad k\ge0,
\tag{2.3}
\]

with the empty sum `s(0)=0`.

### Theorem 2.2 (backward stationary law = increments of forward survival)

Under `(IID)+(BD)+(WEL)` and `delta>1`,

\[
\boxed{
s(k)=\mathbb P_k(V_n>0\text{ for every }n\ge0)}
\tag{2.4}
\]

for every `k>=0`. Equivalently, if `sigma_0=inf{n>=0:V_n=0}`, then

\[
\boxed{
\mathbb P_k(\sigma_0<\infty)
 =\sum_{i\ge k}\pi_i.
}
\tag{2.5}
\]

In particular,

\[
\boxed{\pi_i=s(i+1)-s(i)\quad(i\ge0).}
\tag{2.6}
\]

### Proof

Stationarity `pi P=pi` and the duality (2.2) imply

\[
\pi H=\pi PH=\pi HQ^{\mathsf T}.
\]

The `k`-th coordinate of `pi H` is exactly `s(k)`, so

\[
\boxed{s(k)=\sum_{\ell\ge0}Q(k,\ell)s(\ell).}
\tag{2.7}
\]

Thus `s` is a bounded `Q`-harmonic function with `s(0)=0` and `s(k)\uparrow1` as `k\to\infty`.

Set

\[
q(k)=1-s(k)=\sum_{i\ge k}\pi_i.
\]

Then `q` is also bounded `Q`-harmonic, `q(0)=1`, and `q(k)\downarrow0`.

It remains only to identify this harmonic function with the extinction probability. Under `(WEL)`, for every fixed positive integer `K`,

\[
\varepsilon_K:=\min_{1\le j\le K}Q(j,0)>0.
\tag{2.8}
\]

Indeed, `Q(j,0)` is the annealed probability that the first `j` tosses at a fresh site are all failures, and the left-direction part of `(WEL)` gives positive probability to a stack whose left probabilities are all positive; a finite product on that event is positive.

Therefore, on the event that `V` never hits `0`, the chain cannot visit `{1,\ldots,K}` infinitely often: at each such visit the conditional probability of absorption on the next step is at least `epsilon_K`, so surviving infinitely many visits has probability zero. Since `K` was arbitrary,

\[
V_n\longrightarrow\infty
\quad\text{on }\{\sigma_0=\infty\}.
\tag{2.9}
\]

Because `q(V_n)` is a bounded martingale, it converges almost surely and in `L^1`. On `{sigma_0<infinity}`, it is eventually `q(0)=1`; on `{sigma_0=infinity}`, (2.9) and `q(k)->0` give limit `0`. Hence

\[
q(k)=\mathbb E_k[\lim_n q(V_n)]
=\mathbb P_k(\sigma_0<\infty),
\]

which proves (2.4)–(2.6). QED.

### Consequence for the source escape event

At `k=1`,

\[
\boxed{\pi_0=s(1)=\mathbb P_1(\sigma_0=\infty),}
\tag{2.10}
\]

so the cumulative escape formula becomes

\[
\boxed{
p_{\rm esc}=\mathbb E[p_1]\,s(1).}
\tag{2.11}
\]

The forward survival relation itself is consistent with the standard forward-branching description of right excursions in the excited-random-walk literature. What is new **for this R7-05 proof route** is the exact use of Siegmund duality to identify the *entire* stationary law by (2.6). No publication-novelty claim is made.

## 3. Method B18 — translate the depth-three blocker into a forward survival/scale problem

Now specialize to cookie depth `M=3`. Let

\[
K=\xi_1+\xi_2+\xi_3,
\qquad a_r=\mathbb P(K=r),\quad 0\le r\le3,
\tag{3.1}
\]

and let

\[
T(z)=\frac1{2-z}.
\]

After the first three tosses all remaining coins are fair. Conditional on `K=r`, among the first three tosses there were `3-r` failures. If the forward chain starts from `k>=3`, it therefore needs

\[
k-(3-r)=k-3+r
\]

additional fair failures. Let `G_1,G_2,...` be i.i.d. numbers of fair successes before one fair failure. Then

\[
\mathbb E[z^{G_1}]=T(z),
\qquad
\mathbb E G_1=1,
\qquad
\operatorname{Var}(G_1)=2,
\]

and pathwise in distribution, conditional on `K=r`,

\[
\boxed{
S_k\overset d=r+\sum_{m=1}^{k-3+r}G_m,
\qquad k\ge3.
}
\tag{3.2}
\]

Hence the exact tail-row PGF of the forward kernel is

\[
\boxed{
\mathbb E[z^{S_k}]
=T(z)^{k-3}\sum_{r=0}^3a_r\bigl(zT(z)\bigr)^r,
\qquad k\ge3.
}
\tag{3.3}
\]

This is the forward analogue of the Möbius PGF formula used in the previous backward-chain calculation.

Since

\[
\mathbb EK=\frac{\delta+3}{2},
\]

(3.2) gives the exact first two conditional-scale moments

\[
\boxed{\mathbb E[S_k-k]=\delta,}
\tag{3.4}
\]

and

\[
\boxed{
\operatorname{Var}(S_k)
=2k+\delta-3+4\operatorname{Var}(K),
\qquad k\ge3.
}
\tag{3.5}
\]

Thus the forward process is a critical geometric branching mechanism with a bounded migration term: at large state it has constant positive drift `delta` and variance coefficient `2k`. Its diffusion-scale heuristic is the squared-Bessel-type process

\[
dY_t=\delta\,dt+\sqrt{2Y_t}\,dB_t.
\tag{3.6}
\]

This is the exact conceptual dual of the backward process used in the source's ballisticity proof, whose large-state drift is `1-delta`. Equation (3.6) is only a diagnostic here; the exact statements are (3.2)–(3.5).

### The depth-three boundary condition becomes local in `s(1),s(2)`

The preceding R7-05 balance theorem proved

\[
c_0\pi_0+c_1\pi_1=\delta-1,
\tag{3.7}
\]

where

\[
c_0=\mathbb E\!\left[
 p_1(2p_2-1)+(2p_3-1)(p_1+p_2-p_1p_2)
\right],
\]

\[
c_1=\mathbb E[p_1p_2(2p_3-1)].
\]

Using (2.6), `pi_0=s(1)` and `pi_1=s(2)-s(1)`. Therefore (3.7) is exactly

\[
\boxed{
(c_0-c_1)s(1)+c_1s(2)=\delta-1.
}
\tag{3.8}
\]

This is a Robin-type boundary relation for the unique forward survival harmonic function with

\[
s(0)=0,
\qquad
s(k)\to1.
\]

The formerly opaque censored-chain ratio is now

\[
\boxed{
\kappa=\frac{\pi_1}{\pi_0}
=\frac{s(2)-s(1)}{s(1)}.
}
\tag{3.9}
\]

So the exact missing ingredient can be stated without stationary measures at all: evaluate the first two values of the bounded survival/scale function for the critical geometric branching process with the cookie-induced bounded migration law (3.3). This is genuinely a different mathematical category from another stationary-moment identity.

It also explains why the old gamma homogeneous mode was not a bookkeeping accident. The missing connection coefficient is the finite-state anchoring of a scale function whose large-state behavior is governed by the critical `variance ~ 2k` mechanism.

## 4. Method B6 — deform from the exactly solved neutral-third-cookie face

The dual formulation suggests perturbing away from the source-cited two-cookie face and measuring exactly how much room remains for the unknown connection coefficient.

Take a deterministic stack

\[
p_1=a,
\qquad p_2=b,
\qquad p_3=\frac{1+x}{2},
\qquad p_j=\frac12\ (j\ge4),
\tag{4.1}
\]

with

\[
\frac12<a,b<1,
\qquad
0\le x<1,
\qquad
2a+2b-3>0.
\tag{4.2}
\]

The final inequality says that the base two-cookie environment `x=0` is already right-transient.

Put

\[
d=2a+2b-3,
\qquad
A=a(2b-1),
\qquad
D=a+b-ab,
\qquad
C=ab.
\tag{4.3}
\]

Then

\[
\delta(x)-1=d+x,
\]

and the exact depth-three coefficients reduce to

\[
c_0(x)=A+xD,
\qquad
c_1(x)=xC.
\tag{4.4}
\]

The balance equation is therefore

\[
\boxed{
(A+xD)\pi_0(x)+xC\pi_1(x)=d+x.
}
\tag{4.5}
\]

At `x=0`, the second term disappears and recovers the exact two-cookie value

\[
\boxed{\pi_0(0)=\frac dA.}
\tag{4.6}
\]

For `x>0`, the unresolved coefficient is present, but probability alone already gives a sharp first-order enclosure around the solved face.

### Theorem 4.1 (quantitative neutral-third-cookie enclosure)

For every stack (4.1)–(4.2),

\[
\boxed{
L(x)\le\pi_0(x)\le U(x),
}
\tag{4.7}
\]

where

\[
\boxed{
U(x)=\frac{d+x}{A+xD},
}
\tag{4.8}
\]

and

\[
\boxed{
L(x)=
\frac{d+x(1-C)}{A+x(D-C)}.
}
\tag{4.9}
\]

Moreover their exact width is

\[
\boxed{
U(x)-L(x)
=
\frac{x\,ab(1-a)\bigl[(3-2b)-x(1-b)\bigr]}
     {(A+xD)(A+x(D-C))}.
}
\tag{4.10}
\]

Consequently

\[
\boxed{\pi_0(x)=\frac dA+O_{a,b}(x)\quad(x\downarrow0),}
\tag{4.11}
\]

and therefore

\[
\boxed{
p_{\rm esc}(x)=a\frac dA+O_{a,b}(x).}
\tag{4.12}
\]

### Proof

Because `pi_1>=0`, (4.5) gives

\[
(A+xD)\pi_0(x)\le d+x,
\]

which is (4.8).

Also `pi_1<=1-pi_0`. Hence

\[
d+x
\le
(A+xD)\pi_0+xC(1-\pi_0)
=xC+[A+x(D-C)]\pi_0.
\]

Since

\[
D-C=a+b-2ab=a(1-b)+b(1-a)>0,
\]

we obtain (4.9).

Subtracting the two rational functions and factoring gives

\[
U(x)-L(x)
=
\frac{xC\{(A-d)+x(D-1)\}}
     {(A+xD)(A+x(D-C))}.
\]

The two elementary identities

\[
A-d=(1-a)(3-2b),
\qquad
D-1=-(1-a)(1-b)
\]

give exactly (4.10). The bracket in (4.10) stays positive for `0<=x<1`, and both bounds converge to `d/A`; this proves (4.11). Finally (1.1), with deterministic first cookie `a`, gives (4.12). QED.

### A derivative window without assuming differentiability

The enclosure also yields rigorous one-sided difference-quotient bounds. If a right derivative exists, it must lie in the interval whose endpoints are

\[
L'(0)=
\frac{(1-C)A-d(D-C)}{A^2},
\tag{4.13}
\]

\[
U'(0)=
\frac{A-dD}{A^2}.
\tag{4.14}
\]

No differentiability of the infinite-state stationary law is assumed or claimed. The width between these slopes is

\[
U'(0)-L'(0)
=\frac{ab(1-a)(3-2b)}{A^2}.
\tag{4.15}
\]

Thus the first nontrivial response to a third cookie is already localized to a finite interval using only the exact boundary law. Determining the actual slope is equivalent to determining the neutral-face value of the survival ratio `s(2)/s(1)`, i.e. the same scale-function connection coefficient rather than a new independent obstruction.

## 5. Exact blocker after the three recovery methods

The recovery changed the representation materially but did not close the frozen metric.

Before this run the unresolved scalar was presented as

\[
\kappa=\frac{B_{01}}{B_{10}}
\]

for the backward chain censored on `{0,1}`.

After B11/B18 it has the equivalent forward form

\[
\boxed{
\kappa
=\frac{s(2)-s(1)}{s(1)},
\qquad
s(k)=\mathbb P_k(V\text{ survives}).
}
\tag{5.1}
\]

The full backward stationary distribution is simultaneously determined by the same survival scale through `pi_i=s(i+1)-s(i)`. Therefore the blocker is no longer an unnamed infinite stationary law: it is one explicitly defined bounded harmonic scale function for the forward critical geometric branching mechanism (3.3).

B6 further proves that this connection coefficient can affect the escape probability only at linear order when the third cookie is switched on from neutrality, with the exact enclosure (4.7)–(4.10). But it does not evaluate that coefficient.

Accordingly:

\[
\boxed{M_{\rm closed}:2\longrightarrow2\quad\text{(NO MOVEMENT)}.}
\]

This is a restricted theorem/reduction package, not a solution of Kosygina–Zerner Problem 3.12 and not a universal depth-three formula.

## 6. Literature/noncircularity note

The forward branching process and its relation to right excursions are standard in the excited-random-walk literature; Peterson's work on strict monotonicity explicitly uses the same `S_k` forward process, while Kosygina–Zerner/Basdevant–Singh use the backward branching process for hitting-time and speed questions. The proof above does not import an unproved peer lemma for the new identity: (2.1) is pathwise and Theorem 2.2 follows directly from stationarity, `(WEL)`, and bounded martingale convergence.

The September 18, 2026 bounded search also found Patrick Carper's September 5, 2026 paper on a branching process with geometric emigration and the distinct “have your cookie and eat it” walk. That paper computes escape probabilities for its own self-interacting model; it is not evidence of a solution of the finite-cookie Problem 3.12 considered here. A bounded search miss is not a novelty or worldwide-openness certificate.

## 7. Next mathematical target

The next route should not return to stationary moments or merely increase the finite truncation height. The precise object to attack is now the forward scale function `s` for (3.3). A useful next triple should seek one of:

1. an exact current/Wronskian identity for the forward survival harmonic equation;
2. a special-function scale comparison exploiting the geometric offspring law and the cubic migration PGF;
3. a rigorous extremal principle that evaluates `s(2)/s(1)` from a finite-dimensional variational object.

Any of these must actually determine or squeeze the fixed connection coefficient beyond the already certified finite-truncation interval before it counts as progress toward `M_closed=3`.