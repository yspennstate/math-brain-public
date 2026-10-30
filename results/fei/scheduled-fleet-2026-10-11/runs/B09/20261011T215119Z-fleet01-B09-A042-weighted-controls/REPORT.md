# B09 / A042 — weighted-threshold endpoint controls in the two required orders

**Run ID:** `20261011T215119Z-fleet01-B09-A042-weighted-controls`  
**Primary packet:** A042 (Bias endpoint certificates)  
**Attempt:** `A042-attempt-02-weighted-controls`  
**Mathematical status:** `KNOWN_SOURCE_PROVED_RECONSTRUCTED_PENDING_REVIEW`  
**Full FEI:** **OPEN**

## 1. Bounded objective and source

The preceding A042 run proved the rare-bias lower obstruction for a biased
two-bit AND, but left three acceptance items open: the `q=m^{-2}` weighted
family, the iterated `eta=1/2, q->0, m->infinity` local-total-correlation
obstruction, and the uniformity/endpoint audit.

This run reconstructs those three items from the original argument at

`reports/fei-2026-10-11/source_material/reductions/paper/biased.tex`,
open-problems commit `10bd8f25e7f93509b1ccb4daf9d8999fcb776f98`, blob
`b620357b573b2906e8cb2df5966576c27ce3ffcd`.

No novelty is claimed for the source theorems.  The mathematical movement is
that A042's previously unfilled acceptance tests now have an explicit,
source-pinned endpoint certificate and a separate numerical reproducer.

## 2. Common genuine Boolean family

Let independent bits satisfy

\[
 X_0\sim\operatorname{Ber}(q_0),\qquad
 X_1,\ldots,X_m\sim\operatorname{Ber}(q),
\]

and put

\[
 A_m=\left\{mX_0+\sum_{j=1}^mX_j\ge m\right\},
 \qquad f_m=2\mathbf 1_{A_m}-1.
\]

For `q,eta in (0,1)`, set

\[
 a=q^m,qquad q_0=\frac{(1-\eta)a}{\eta+(1-\eta)a},
 \qquad \alpha=\Pr(A_m)=\frac{a}{\eta+(1-\eta)a}.
\]

The event is the disjoint union of the heavy branch `{X_0=1}` and the
all-light branch `{X_0=0,X_1=...=X_m=1}`.  Under
`Q=mu(.|A_m)`, `Q(X_0=0)=eta`; conditionally on `X_0=1` the light bits remain
i.i.d. Bernoulli `q`, while conditionally on `X_0=0` they are all one.
Consequently, in **nats**,

\[
 \operatorname{TC}(Q)
 =m\{h(\eta+(1-\eta)q)-(1-\eta)h(q)\},                 \tag{2.1}
\]

and

\[
 \frac{\mathcal I_\mu(f_m)}{4\alpha}
 =1-\eta-q_0+m\eta(1-q).                               \tag{2.2}
\]

These are exact for every interior parameter value.

## 3. KNOWN/PROVED: simultaneous weighted-family limit

Take

\[
 q=m^{-2},\qquad \eta=m^{-1},\qquad
 d=1+(m-1)a,qquad q_0=(m-1)a/d,\qquad \alpha=ma/d.
\]

Then (2.1)--(2.2) give

\[
 \frac{\alpha\operatorname{TC}(Q)}{\mathcal I_\mu(f_m)}
 =\frac{\ln m+1}{8}+O\!\left(\frac{\ln m}{m}\right).   \tag{3.1}
\]

Thus the event-total-correlation payment diverges.  The unit conversion is
literal: replacing nats by bits divides both `TC` and the right-hand leading
term by `ln 2`; no such conversion is applied to the influence denominator.

Let `V=4alpha(1-alpha)` and let `rho_i` be physical pivotal probabilities.
Here

\[
 \rho_0=1-a,\qquad \rho_{\rm light}=(1-q_0)q^{m-1},
\]

\[
 \frac{\mathcal I_0}{4\alpha}=1-\frac1m-q_0,qquad
 \frac{\sum_{j=1}^m\mathcal I_j}{4\alpha}=1-q.
\]

Both logarithmic-credit arguments exceed one:

\[
 \frac{4\rho_0}{V}=\frac{1-a}{\alpha(1-\alpha)},\qquad
 \frac{4\rho_{\rm light}}{V}=\frac{m}{1-\alpha}.
\]

Writing `L=ln(1/alpha)=2m ln m-ln m+ln d`, exact cancellation gives

\[
\begin{aligned}
 D_m={}&\frac{V\ln(1/V)-\sum_i\mathcal I_i
             \ln^+(4\rho_i/V)}{4\alpha}\\
 ={}&(1-\alpha)[L-\ln4-\ln(1-\alpha)]\\
 &-\left(1-\frac1m-q_0\right)
       [L+\ln(1-a)-\ln(1-\alpha)]\\
 &-(1-q)[\ln m-\ln(1-\alpha)].                         \tag{3.2}
\end{aligned}
\]

Since `a=m^{-2m}`, every term containing `aL`, `q_0L`, or `alpha L`
vanishes.  Hence

\[
 \frac{V\ln(1/V)-\sum_i\mathcal I_i\ln^+(4\rho_i/V)}
      {\mathcal I_\mu(f_m)}
 =\frac12\ln m-\ln2+O\!\left(\frac{\ln m}{m}\right).  \tag{3.3}
\]

This refutes only the **coefficient-one** pivotal-credit estimate, even after
an added `O(I)` term.  It does not refute any larger credit multiplier.

The genuine corrected FEI quantity behaves differently.  Let `g` be the sign
of the conjunction of the light bits.  In **bits**,

\[
 \Delta(g)=4a[m(1-q)-1+a],
\]

\[
 \mathcal H_\mu^+(g)
 =2\Delta(g)+8ma(q-a)\log_2(1/q).                       \tag{3.4}
\]

The outer two-input OR has `Delta_o=4q_0a(1-q_0)(1-a)=O(ma^2)` and
`H_o^+=O(ma^2)`.  Exact disjoint composition gives

\[
 \Delta(f_m)=\Delta_o+(1-q_0)\Delta(g),\qquad
 \mathcal H_\mu^+(f_m)=\mathcal H_o^++(1-q_0)\mathcal H_\mu^+(g).
\]

Therefore

\[
 \boxed{\mathcal H_\mu^+(f_m)/\Delta_\mu(f_m)\longrightarrow2}. \tag{3.5}
\]

Equations (3.1), (3.3), and (3.5) establish the requested contrast: both
auxiliary payments diverge while the genuine corrected entropy/deficit ratio
has the finite limit two.  This is not a counterexample to generalized FEI or
to uniform FEI.

## 4. KNOWN/PROVED: exact iterated local-TC obstruction

Now use a **different** regime: fix `m`, take `eta=1/2`, and only then let
`q downarrow 0`.  Here

\[
 q_0=\frac{q^m}{1+q^m},\qquad
 \alpha=\frac{2q^m}{1+q^m}.
\]

Under `Q`, the limiting law is the equal mixture of
`(1,0,...,0)` and `(0,1,...,1)`.  For a heavy-light pair,

\[
 I_Q(X_0;X_j)
 =h\!\left(\frac{1+q}{2}\right)-\frac12h(q)\longrightarrow\ln2. \tag{4.1}
\]

For two distinct light bits, the four joint masses are

\[
 \frac{1+q^2}{2},\quad \frac{q(1-q)}2,\quad
 \frac{q(1-q)}2,\quad \frac{(1-q)^2}{2},
\]

so direct substitution in mutual information also gives
`I_Q(X_i;X_j)->ln 2`.  Meanwhile

\[
 \frac{\mathcal I_0}{\alpha}=4\left(\frac12-q_0\right)\to2,
 \qquad
 \frac{\mathcal I_j}{\alpha}=2(1-q)\to2.               \tag{4.2}
\]

There are `m` other coordinates for every coordinate.  Combining
(4.1)--(4.2), for every `j in {0,...,m}`,

\[
 \lim_{q\downarrow0}
 \frac{\alpha\sum_{k\ne j}I_Q(X_j;X_k)}{\mathcal I_j(f_m)}
 =\frac{m\ln2}{2}.                                      \tag{4.3}
\]

Only after taking this fixed-`m` limit do we send `m->infinity`.  Thus no
universal `K` can make the proposed local payment hold for even one selected
coordinate.  This concerns conditional-input total correlation; it does not
settle the open existential spectral-coordinate selection problem.

## 5. Endpoint and uniformity audit

- At `q=0`, the formula forces `q_0=alpha=0`; the event is null and `f_m` is
  constant.  All deterministic coordinates are contracted before ratios are
  formed.  The raw ratios are `0/0`, not endpoint values.
- At `q=1`, every light bit is deterministic and the event is certain; again
  contract the deterministic function before using any ratio.
- At `eta=0`, `q_0=1` and the event is certain.  At `eta=1`, `q_0=0` and the
  heavy coordinate is deleted, leaving the all-light conjunction.
- Equations (3.1)--(3.5) are a simultaneous one-parameter sequence with
  arity `m`, weights `(m,1,...,1)`, and biases fixed as displayed.  Their
  error terms are statements along that sequence; they do not assert a
  uniform theorem over arbitrary weights or product biases.
- Equation (4.3) is an iterated limit.  It is proved for each fixed `m` and
  then `m` grows.  No interchange of limits and no `q`-uniform-in-`m` rate is
  claimed.
- The prior two-bit AND expansion is uniform only for its fixed companion
  bias `q` on compact subsets away from `0` and `1/2`; it is not used to
  justify either weighted-family limit here.

## 6. Reproducer

`verify_weighted_limits.py` evaluates the exact formulas with 180-digit
`Decimal` arithmetic.  It checks finite `m` values for all three weighted
ratios and both heavy/light local-TC coordinate ratios.  Randomness: none.

Command:

```text
python verify_weighted_limits.py
```

The output is archived as `CHECK.out`.  The code is a reproducer, not the
proof of the asymptotic statements.

## 7. Packet and review status

**A042 mathematical acceptance items:** met by the pinned source proof and the
explicit reconstruction above.

**A042 deliverable acceptance:** pending the required independent reviews by
A091 and A090.  No review was performed in this run.  This author-side
reconstruction must not be counted as independent acceptance.

**Remaining full-FEI obstruction:** these examples kill three proposed
normalization payments but leave the universal corrected biased-gate inequality
and the uniform-cube FEI conjecture open.  The next B09 action should move to
A045 to adversarially audit biased realizability and the exact domain of the
gate-potential formulation, using this A042 certificate as a guard.

