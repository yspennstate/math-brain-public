# R18 — exact trinomial exclusion and target-specific Baker separation

**Run addendum:** `2026-09-16_12-50-30_UTC__R18__tri-baker-b91e`  
**Status:** **OPEN.** This strengthens the same R18 run; it does not decide the Lehmer reciprocal or Salem's fourth problem.

Parent checkpoint:

`proofnet24/R18-salem-bernoulli-convolutions/runs/2026-09-16/2026-09-16_12-50-00_UTC__R18__tri-geometry-a7c3__report.md`.

The parent report proved the 34/18/12 phase trichotomy and deterministic two-gap small-ball bounds. This addendum removes a remaining exact-zero ambiguity and upgrades nonzero two-gap packets to a **pointwise polynomial lower bound**, with no discrepancy floor.

## R18-GH-C006 — exact finite-window criterion for three-term Salem relations

**Status: PROVED, including an exact Lehmer exclusion.**

Let \(\theta>1\) be a Salem number with minimal polynomial \(m_\theta\), and suppose
\[
P(x)=q_1+q_2x^a+q_3x^{a+b},\qquad a,b\ge1,
\]
where \(q_i\in\mathbb Z\setminus\{0\}\) and \(|q_i|\le B\).

If one neutral conjugate \(z\) of \(\theta\) satisfies \(P(z)=0\), irreducibility gives
\[
m_\theta\mid P,
\]
so in particular
\[
P(\theta)=P(\theta^{-1})=0.
\]
From the real embedding \(\theta\),
\[
|q_3|\theta^{a+b}=|q_1+q_2\theta^a|
\le B+B\theta^a\le2B\theta^a,
\]
hence
\[
\boxed{\theta^b\le2B.}\tag{1.1}
\]
From \(\theta^{-1}\),
\[
|q_1|\le B\theta^{-a}+B\theta^{-(a+b)}\le2B\theta^{-a},
\]
so
\[
\boxed{\theta^a\le2B.}\tag{1.2}
\]
Therefore **every exact three-term relation lies in a finite gap box**
\[
\boxed{1\le a,b\le \left\lfloor\frac{\log(2B)}{\log\theta}\right\rfloor.}\tag{1.3}
\]
This is a reusable exact-relation criterion for any fixed Salem number and bounded coefficient alphabet.

### Lehmer, residual alphabet \(B=4\)

For Lehmer's polynomial
\[
m_L(x)=x^{10}+x^9-x^7-x^6-x^5-x^4-x^3+x+1,
\]
exact rational arithmetic gives
\[
m_L(147/125)=
-\frac{6476164282534478951}{931322574615478515625}<0.
\]
Since \(m_L\) has the unique Salem root \(\theta_L>1\), this gives
\[
\theta_L>147/125.
\]
Also, exactly,
\[
(147/125)^{13}>8.
\]
Hence
\[
\theta_L^{13}>8,
\]
and (1.1)--(1.2) imply
\[
\boxed{a,b\le12.}\tag{1.4}
\]

The run-specific exact checker works in the quotient ring
\[
\mathbb Z[x]/(m_L)
\]
and exhausts
\[
12\cdot12\cdot8^3=73,728
\]
choices of \((a,b,q_1,q_2,q_3)\), with each \(q_i\in\{\pm1,\pm2,\pm3,\pm4\}\). It finds
\[
\boxed{\text{zero exact three-term multiples of }m_L.}\tag{1.5}
\]
Thus for every such coefficient triple and every positive \(a,b\),
\[
\boxed{q_1+q_2z_s^a+q_3z_s^{a+b}\ne0}
\tag{1.6}
\]
for every neutral conjugate \(z_s\).

Artifact:

`proofnet24/R18-salem-bernoulli-convolutions/artifacts/2026-09-16_12-50-30_UTC__R18__tri-baker-b91e__checker.py`.

Its output SHA-256 is

`d380f6817b34af071e4fb2bad0b7382826f9c28cea1df205b01b59ca6d79ebc5`.

## R18-GH-C007 — no-floor polynomial separation for every nonzero short packet

**Status: PROVED, depending on C002 and C006 plus standard Baker-Wustholz.**

There exist constants
\[
C_L>0,\qquad T_L<\infty
\]
such that for every
\[
a,b\ge1,
\qquad q_i\in\{\pm1,\pm2,\pm3,\pm4\},
\]
the Lehmer four-neutral short vector from the parent run satisfies
\[
\boxed{
\|\mathbf A_q(a,b)\|_2
\ge C_L(1+a+b)^{-T_L}.
}
\tag{2.1}
\]

### Proof

It suffices to use one fixed neutral representative \(z=z_1\). Put
\[
f_q(u,v)=q_1+q_2u+q_3uv.
\]
By C006, the orbit point \((z^a,z^b)\) is never an exact zero of \(f_q\).

For a **strict triangle** coefficient class, C002 shows the two torus zeros are nondegenerate. Compactness plus the inverse function theorem therefore gives
\[
|f_q(u,v)|\ge c_q\,\operatorname{dist}((u,v),Z_q)
\tag{2.2}
\]
for all \((u,v)\in\mathbb T^2\).

For a **degenerate triangle** class, after a fixed phase shift the unique zero is represented by
\[
f=r_1-r_2e^{ix}-r_3e^{i(x+y)},\qquad r_1=r_2+r_3.
\]
Its real part is
\[
r_2(1-\cos x)+r_3(1-\cos(x+y)),
\]
which is bounded below by a positive constant times \(x^2+(x+y)^2\) near the unique zero. Compactness away from the zero gives globally
\[
|f_q(u,v)|\ge c_q\,\operatorname{dist}((u,v),Z_q)^2.
\tag{2.3}
\]
For a **nontriangle** class, C002 already gives a positive constant lower bound.

Every coordinate of every zero in \(Z_q\) is a fixed algebraic number on the unit circle: the strict zeros are given explicitly by the quadratic triangle formula in C002, and degenerate zeros have phases \(\pm1\) after fixed sign shifts.

Fix such an algebraic target \(\xi\). For the fixed algebraic \(z\), if \(z^n\ne\xi\), Baker-Wustholz applied to
\[
n\log z-\log\xi-2k\log(-1)
\]
with the appropriate winding integer \(k=O(n)\) gives constants \(c,\tau>0\) such that
\[
\boxed{|z^n-\xi|\ge c(1+n)^{-\tau}.}\tag{2.4}
\]
There are only finitely many coefficient classes, signs and target coordinates, so the constants can be made uniform.

For a given \((a,b)\), C006 excludes simultaneous equality with an exact zero target. Hence at least one of the two phase coordinates is separated from its target by (2.4). Combining with (2.2) or (2.3) yields (2.1), after enlarging the exponent in the degenerate case. The vector norm dominates the chosen scalar coordinate.

### General reusable form

For any fixed Salem number \(\theta\), fixed neutral conjugate \(z\), and finite coefficient alphabet, the same proof gives polynomial separation for all three-term packets provided the finite exact-relation search supplied by C006 finds no exact relation. Thus C006+C007 form a finite-verification criterion for a whole class of Salem short-packet problems.

## R18-GH-C008 — exponentially weighted short-packet reciprocal-square series closes

**Status: PROVED, depending on C007.**

For every fixed \(\sigma>0\),
\[
\boxed{
\sum_{a\ge1}\sum_{b\ge1}
 e^{-\sigma(a+b)}
 \|\mathbf A_q(a,b)\|_2^{-2}
<\infty
}
\tag{3.1}
\]
uniformly over the finite residual coefficient alphabet.

Indeed C007 gives
\[
\|\mathbf A_q(a,b)\|^{-2}
\le C_L(1+a+b)^{2T_L},
\]
and the polynomial factor is absorbed by \(e^{-\sigma(a+b)}\).

This closes the **nonzero three-term short-packet reciprocal-square/action problem** whenever the surrounding collision decomposition supplies any positive exponential action in \(a+b\). It does **not** close the six-defect reversal bridge, where a further long phase can cancel the already nonzero short amplitude.

## Updated GitHub ledger

| ID | Status | Content |
|---|---|---|
| R18-GH-C001--C005 | retained | Parent report |
| R18-GH-C006 | **PROVED** | Any exact bounded-coefficient Salem trinomial lies in a finite gap box; no Lehmer residual-alphabet exact trinomial exists |
| R18-GH-C007 | **PROVED** | Uniform no-floor polynomial lower bound for every Lehmer residual three-term short packet |
| R18-GH-C008 | **PROVED** | Every exponentially action-weighted short-packet reciprocal-square series converges |
| R18-GH-X001 | retained **DISPROVED ROUTE** | Final-return block contraction is not iterable |
| Lehmer reciprocal AC/singularity | **OPEN** | Not decided |
| Full Salem fourth classification | **OPEN** | Not decided |

## Next obligation

The strict/degenerate short-packet arithmetic is no longer the main obstruction: exact zeros are absent and every nonzero short packet has a polynomial lower bound. The next hard object is a **moving bridge target** of the form
\[
A_s(a,b)+\omega_s(a,b)z_s^c\overline{A_s(a,b)},
\]
where the target phase depends algebraically on \((a,b)\). A fixed-target Baker theorem is no longer enough because the target height grows with the short packet.

The next attack should therefore compare the moving target height to the available short-gap action, or else prove a certified transfer-operator superharmonic majorant as in C005. Exact target identities must remain separated from nonzero near-cancellation.

**No closure claim.**
