# C0130 — exact escape identity through the backward branching chain

Model actually running: GPT-5.6 Sol. Reasoning level: UNVERIFIED. This is not GPT-6 at maximum; authenticated runtime reasoning-effort telemetry and a binding model/effort selector are not exposed.

Date: 2026-09-18
Slot: R7-05
Target: `C0130`
Admission: `research7_2026-09-17/R7-05/admissions/2026-09-18T085400Z__C0130.md`
Canonical claim: `operations/claims/C0130.md`
Source: Elena Kosygina and Martin P. W. Zerner, *Excited random walks: results, methods, open problems*, Problem 3.12, p. 13.

Status of this artifact: **PARTIAL**, not a source-level solution. The new result below is an exact characterization for the i.i.d. bounded-cookie right-transient branch, plus a sharp obstruction to any formula depending only on the total drift parameter. The stationary atom is not yet evaluated in closed form for general stacks.

## 1. Setup

Work first under the standard one-dimensional i.i.d. bounded-cookie assumptions `(IID)+(BD)+(WEL)`. At each site `x`, the `j`-th visit uses a right-jump probability `omega(x,j)`; after the finite cookie depth `M` all probabilities are `1/2`. Let

\[
\delta=\mathbb E\left[\sum_{j=1}^{M}(2\omega(0,j)-1)\right].
\]

For `delta>1`, the walk is transient to the right under the source theorem. Write

\[
p_{\rm esc}:=P_0(X_n\neq0\text{ for every }n\ge1).
\]

At one site, expose an independent Bernoulli sequence with success probabilities given by the successive cookies, where success means a right step. For `m>=1`, let

\[
F_{x,m}:=\text{number of failures before the }m\text{-th success at site }x.
\]

The standard backward branching chain associated with the i.i.d. cookie law is

\[
Z_0=0,\qquad Z_{k+1}=F_{k+1,Z_k+1}.
\tag{1}
\]

For `delta>1` this countable-state chain is irreducible and positive recurrent; denote its unique stationary law by `pi`. This positive-recurrence fact is part of the pre-existing Basdevant–Singh/backward-branching machinery and is not being claimed as new here.

## 2. B2 — attack the negation: total drift `delta` cannot determine escape

The source-cited exact two-cookie formula of Zerner (2005), Theorem 18, says that when all cookies from the third visit onward are neutral,

\[
p_{\rm esc}
=
\frac{\mathbb E[\omega(0,1)]\,(\mathbb E[\delta_0]-1)_+}
{\mathbb E[\omega(0,1)(2\omega(0,2)-1)]}.
\tag{2}
\]

For a deterministic two-cookie stack `(p_1,p_2,1/2,1/2,...)` with `p_1,p_2>1/2`,

\[
\delta=2(p_1+p_2-1),
\qquad
p_{\rm esc}=\frac{\delta-1}{2p_2-1}.
\tag{3}
\]

Therefore the same `delta` can have different escape probabilities. Take

\[
(p_1,p_2)=\left(\frac45,\frac45\right)
\quad\text{and}\quad
(p_1,p_2)=\left(\frac7{10},\frac9{10}\right).
\]

Both have

\[
\delta=\frac65>1,
\]

but (3) gives respectively

\[
p_{\rm esc}=\frac{1/5}{3/5}=\frac13,
\qquad
p_{\rm esc}=\frac{1/5}{4/5}=\frac14.
\tag{4}
\]

Hence:

**Proposition 2.1.** Even within deterministic two-cookie i.i.d. environments, `p_esc` is not a function of `delta` alone.

This eliminates the most obvious one-parameter candidate formula before attempting a general proof.

## 3. B11 — dualize finite-interval escape into the backward branching chain

The useful exact object is the atom `pi(0)` of the stationary backward branching law.

### Theorem 3.1 (stationary-atom escape identity)

Assume `(IID)+(BD)+(WEL)` and `delta>1`. Let `pi` be the unique stationary distribution of the backward branching chain (1). Then

\[
\boxed{
P_0(X_n\neq0\ \forall n\ge1)
=
\mathbb E[\omega(0,1)]\,\pi(0).
}
\tag{5}
\]

For left transience, the reflected environment gives the symmetric formula

\[
\boxed{
P_0(X_n\neq0\ \forall n\ge1)
=
\mathbb E[1-\omega(0,1)]\,\pi^{-}(0),
}
\tag{6}
\]

where `pi^-` is the stationary law of the backward branching chain for the reflected cookie stacks.

### Proof

Fix `n>=2` and start the walk from site `1` with fresh stacks on the positive sites. Let

\[
T_a:=\inf\{k\ge0:X_k=a\}.
\]

On a realization of the cookie coin stacks at sites `1,...,n-1`, read the successful crossing of the interval `[0,n]` backward from `n`.

Set `U_n=0`. If `U_{j+1}` downcrossings from `j+1` to `j` occur before the first hit of `n`, then site `j` must provide exactly `U_{j+1}+1` successful jumps from `j` to `j+1`: one initial upcrossing plus one replacement for each later return from `j+1`. Therefore the number of failures at site `j` used before these successes is

\[
U_j=F_{j,U_{j+1}+1},
\qquad j=n-1,n-2,\ldots,1.
\tag{7}
\]

A failure at site `1` is precisely a jump `1->0`. Consequently

\[
\{T_n<T_0\}=\{U_1=0\}.
\tag{8}
\]

Because the site stacks are i.i.d., reversing the order of the independent stacks `1,...,n-1` does not change their joint law. Iterating (7) after this reversal is exactly the forward recursion (1). Thus

\[
U_1\overset d=Z_{n-1}
\quad\text{and hence}\quad
P_1(T_n<T_0)=P(Z_{n-1}=0).
\tag{9}
\]

For `delta>1`, right transience implies that on `{T_0=\infty}` every sufficiently large positive level is eventually hit. The events `{T_n<T_0}` decrease to `{T_0=\infty}` as `n->infinity`, so

\[
P_1(T_0=\infty)
=
\lim_{n\to\infty}P_1(T_n<T_0)
=
\lim_{n\to\infty}P(Z_{n-1}=0).
\tag{10}
\]

The irreducible positive recurrent chain `Z`, started at `0`, converges in distribution to `pi` (it is aperiodic because the weak ellipticity assumptions give a positive self-loop probability at `0`). Therefore the last limit is `pi(0)`.

Finally, for a right-transient walk started at `0`, the event of never returning to `0` must begin with a jump to `+1`; a first jump to `-1` would have to cross `0` again before the walk can tend to `+infinity`. Under `(IID)`, the fresh environment on the positive half-line is independent of the first cookie at `0`. Hence

\[
p_{\rm esc}
=
\mathbb E[\omega(0,1)]P_1(T_0=\infty)
=
\mathbb E[\omega(0,1)]\pi(0),
\]

which is (5). Reflection proves (6). QED.

### Two exact corollaries

First, Kac's formula for the positive recurrent chain gives

\[
\boxed{\pi(0)=\frac{1}{E_0\tau_0^+}},
\qquad
\tau_0^+:=\inf\{k\ge1:Z_k=0\}.
\tag{11}
\]

Thus the source escape probability is also a reciprocal mean-return-time observable of the backward branching chain.

Second, stationarity gives an exact balance identity at zero. Starting from state `i`, the next state is zero iff the first `i+1` Bernoulli trials at the next site are all successes. Therefore

\[
\boxed{
\pi(0)
=
\sum_{i\ge0}\pi(i)\,
\mathbb E\left[\prod_{j=1}^{i+1}\omega(0,j)\right].
}
\tag{12}
\]

For bounded depth `M`, the product after `M` simply acquires factors `2^{-(i+1-M)}`. Formula (12) makes the remaining obstruction explicit: beyond the special two-cookie cancellation, the escape atom depends on the full stationary tail of `pi`, not merely on `delta` or a finite collection of its moments.

### Check against the exact two-cookie formula

For the two deterministic examples in (4), (5) gives

\[
\pi(0)=\frac{p_{\rm esc}}{p_1}.
\]

Hence

\[
\pi_A(0)=\frac{1/3}{4/5}=\frac5{12},
\qquad
\pi_B(0)=\frac{1/4}{7/10}=\frac5{14}.
\tag{13}
\]

So the stationary atom itself distinguishes cookie stacks having the same total drift.

## 4. B5 — add a parameter and differentiate: exact two-cookie benchmark

The two-cookie formula gives a solvable deformation against which any `M>=3` perturbation theory must be checked.

Take a deterministic nonnegative two-cookie stack with

\[
p_i=\frac12+b_i,\qquad b_i>0,
\]

and scale all excitation by `t`:

\[
p_i(t)=\frac12+t b_i,\qquad 0<t\le1.
\tag{14}
\]

Let

\[
\delta_1=2(b_1+b_2),
\qquad
\delta(t)=t\delta_1.
\]

The right-transient side begins at

\[
t_c=\frac1{\delta_1}.
\]

For `t>t_c`, equation (3) becomes

\[
\boxed{
p_{\rm esc}(t)
=
\frac{t\delta_1-1}{2tb_2}.
}
\tag{15}
\]

Therefore

\[
\boxed{
p_{\rm esc}'(t)=\frac{1}{2b_2t^2}>0,
}
\tag{16}
\]

and the onset at the transience threshold is exactly linear:

\[
p_{\rm esc}(t)
=
\frac{\delta_1^2}{2b_2}(t-t_c)+O((t-t_c)^2).
\tag{17}
\]

Using (5), the stationary atom along the same ray is

\[
\boxed{
\pi_t(0)
=
\frac{t\delta_1-1}
{2tb_2(1/2+tb_1)}.
}
\tag{18}
\]

Thus the source problem for `M>=3` can be recast very concretely: compute the zero atom of an infinite-state stationary law, and in particular understand how that atom emerges from zero as the backward branching chain crosses its positive-recurrence boundary.

For a finite truncation of the chain, differentiating `pi_t P_t=pi_t` gives the exact sensitivity equation

\[
\pi_t'(I-P_t)=\pi_t P_t',\qquad \pi_t'\mathbf1=0.
\tag{19}
\]

Passing such a formula to the full chain near `delta=1` would require a justified resolvent/ergodicity estimate; no such uniform estimate is proved here. Equation (19) is therefore a map of the missing ingredient, not a theorem about differentiability of the infinite-state stationary law.

## 5. What this does and does not settle

The new exact identity (5) turns the escape question, in the i.i.d. bounded-cookie branch, into a single stationary-atom problem and proves convergence of a concrete sequence of finite-interval probabilities to that atom. It also gives the exact return-time representation (11) and balance equation (12).

It does **not** yet provide a closed formula for `pi(0)` for arbitrary cookie depth, does not handle the stationary-ergodic branch of the source problem, and does not move the frozen universal-depth metric. The source-level status remains OPEN/PARTIAL.

Frozen metric for this target:

\[
M_{\rm closed}: 2\longrightarrow2\qquad\text{(NO MOVEMENT)}.
\]

This is the first ordinary C0130 run, so its target-local unchanged streak becomes `0 -> 1`; no stagnation count is inherited from H0024.

## 6. Next mathematical attack

The smallest metric-moving case is **all i.i.d. bounded stacks neutral after visit 3**. For `M=3`, the transition kernel of `Z` is explicit but its stationary zero atom is not. The next nonrepeating run should attempt to derive a stationary generating-function equation for

\[
G(s)=\sum_{k\ge0}\pi(k)s^k
\]

that closes at `s=0`, or prove that a finite set of additional stationary observables is unavoidable. That will test whether the apparent `M=3` finite-state reduction is real or merely a countable-state reformulation.