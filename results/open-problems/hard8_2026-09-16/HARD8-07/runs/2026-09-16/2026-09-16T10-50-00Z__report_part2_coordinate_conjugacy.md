# HARD8-07 — adjacent beta-frame conjugacy obstruction

**STATUS: OPEN / APPEND-ONLY STRENGTHENING AND NEXT-ATTACK CORRECTION**

This file strengthens, but does not overwrite,

`hard8_2026-09-16/HARD8-07/runs/2026-09-16/2026-09-16T10-38-04Z__report.md`

creation commit `71eb75abd1c2c10b5d0cd7a9dc7992078f6d4e8c`.

The main report ended by proposing a comparison of adjacent near-tail strip packings under the continued-fraction recurrence of beta. The calculation below shows that **beta-frame recurrence alone cannot provide the desired incompatibility**: adjacent frames are exactly unimodularly conjugate, preserve the represented denominator q, and preserve every alpha phase if the alpha frame is held fixed. Thus the only genuinely new cross-scale information can come from changing the alpha frame/modulus or from a frame-free dynamical invariant.

## 1. Exact adjacent-frame coordinate map

Keep
\[
D_{n+2}=d_{n+2}D_{n+1}+D_n
\]
and
\[
\eta_n=d_{n+2}+\frac1{\eta_{n+1}}.
\]
For an integer coefficient vector
\[
u=(z,v)\in\mathbb Z^2
\]
define
\[
q_n(u)=zD_n+vD_{n+1}.
\]
Put
\[
\boxed{
T_n(z,v)=(v-d_{n+2}z,\ z).
}
\tag{1.1}
\]
The matrix of \(T_n\) is
\[
\begin{pmatrix}
-d_{n+2}&1\\
1&0
\end{pmatrix},
\]
whose determinant is \(-1\). Hence \(T_n\) is a bijection of \(\mathbb Z^2\).

### Proposition 1.1 — denominator invariance

For every \(u\in\mathbb Z^2\),
\[
\boxed{
q_{n+1}(T_nu)=q_n(u).
}
\tag{1.2}
\]

#### Proof

If \(T_n(z,v)=(z',v')\), then
\[
\begin{aligned}
z'D_{n+1}+v'D_{n+2}
&=(v-d_{n+2}z)D_{n+1}+zD_{n+2}\\
&=vD_{n+1}+z(D_{n+2}-d_{n+2}D_{n+1})\\
&=vD_{n+1}+zD_n.
\end{aligned}
\]
QED.

Thus changing from the adjacent basis \((D_n,D_{n+1})\) to \((D_{n+1},D_{n+2})\) does not create a new family of q-values. It only changes integer coordinates.

## 2. Exact transformation of the beta-tail defect

Use the signed tail form
\[
\ell_n(z,v)=v-z\eta_n.
\]

### Proposition 2.1 — tail defect conjugacy

For every \((z,v)\),
\[
\boxed{
\ell_{n+1}(T_n(z,v))
=-\eta_{n+1}\ell_n(z,v).
}
\tag{2.1}
\]
Consequently
\[
\boxed{
s_{n+1}(T_nu)=\eta_{n+1}s_n(u),
}
\tag{2.2}
\]
where \(s_n=|\ell_n|\).

#### Proof

Let \(a=d_{n+2}\). Then
\[
\begin{aligned}
\ell_{n+1}(T_n(z,v))
&=z-(v-az)\eta_{n+1}\\
&=-\eta_{n+1}
\left(v-az-\frac z{\eta_{n+1}}\right)\\
&=-\eta_{n+1}(v-z\eta_n),
\end{aligned}
\]
because \(\eta_n=a+1/\eta_{n+1}\). QED.

Since the bounded-type hard core has
\[
1<\eta_{n+1}<A_\beta+1,
\]
the tail-strip width changes only by a bounded multiplicative factor.

The coefficient norm is also distorted only by a bounded factor:
\[
\boxed{
\|T_nu\|_\infty
\le(A_\beta+1)\|u\|_\infty,
}
\tag{2.3}
\]
and the inverse map
\[
T_n^{-1}(z',v')=(v',z'+d_{n+2}v')
\]
satisfies the same bound.

Therefore adjacent near-tail strips are not independent geometric objects; they are uniformly distorted images of one another under an exact integer change of basis.

## 3. Alpha phase is exactly invariant when its frame is fixed

Fix any alpha convergent frame, not necessarily the matched one:
\[
M=B_{m+1},
\qquad
A=A_{m+1}.
\]
Define
\[
\theta_{m,n}(z,v)
=
\frac{(zD_n+vD_{n+1})A}{M}\pmod1.
\]

### Proposition 3.1 — fixed-alpha phase conjugacy

For every \(u\in\mathbb Z^2\),
\[
\boxed{
\theta_{m,n+1}(T_nu)=\theta_{m,n}(u).
}
\tag{3.1}
\]

#### Proof

By Proposition 1.1, the represented integer q is identical in the two frames. The phase is a function only of q and the fixed pair \((A,M)\). QED.

Thus the pairwise phase distances used in the packing theorem of the main report are also exactly preserved under \(T_n\) when the alpha frame is held fixed.

## 4. Consequence: beta recurrence alone cannot contradict persistent packing

The main report proved that a genuine Littlewood counterexample forces near-tail portal phases to form constant-factor optimal circle packings at every admissible strip scale. A tempting next step was to compare the packing at stage \(n\) to that at \(n+1\).

Propositions 1.1–3.1 show that this comparison is tautological if the same alpha frame is used:

- the q-values are identical;
- the coefficient boxes change by at most a bounded factor;
- the beta-tail widths change by the bounded factor \(\eta_{n+1}\);
- the alpha phases are identical.

Hence **there is no independent packing constraint coming from the beta continued-fraction recurrence by itself**.

This is consistent with the earlier fixed-lattice theorem archived in the 07:43:41Z checkpoint: adjacent-convergent frames are coordinate systems on one fixed Littlewood lattice. The present calculation identifies the exact conjugacy on the new anisotropic strip variables.

## 5. Where genuine cross-scale information can still enter

The matched-scale argument in the main report uses
\[
M_n^*=B_{m_*(n)+1}
\]
with
\[
B_{m_*(n)+1}\le D_n<B_{m_*(n)+2}.
\]
When \(n\) changes, \(m_*(n)\) may also change. Therefore the only nontrivial phase change is not the beta basis transition but the replacement
\[
(A_{m+1},B_{m+1})
\longrightarrow
(A_{m'+1},B_{m'+1}).
\]

If \(m_*(n+1)=m_*(n)\), then the adjacent-stage packing conditions are literally conjugate and provide no new information beyond constant rescaling of \((R,S)\).

If \(m_*(n+1)>m_*(n)\), the same integers q are tested modulo a new alpha convergent denominator. Any useful incompatibility theorem must therefore quantify how a large near-tail q-set can be simultaneously near-critically packed under **two successive alpha modular phases**.

Equivalently, the next problem is intrinsically two-sided: one must couple the continued-fraction recurrence of alpha with the near-tail strip of beta. A one-sided beta recurrence argument cannot close the proof.

## 6. Revised next attack

The next bounded iteration should freeze a beta-resonant q-set and analyze an alpha-frame transition. Concretely, for consecutive alpha frames define
\[
\phi_m(q)=\frac{qA_{m+1}}{B_{m+1}}\pmod1,
\qquad
\phi_{m+1}(q)=\frac{qA_{m+2}}{B_{m+2}}\pmod1.
\]
The target is an exact transference statement of the following form:

> a set of \(N\) integers q coming from one beta-resonant strip cannot be simultaneously \(\gg 1/N\)-separated under both \(\phi_m\) and \(\phi_{m+1}\) across too many alpha-frame transitions, unless the q-set has a rigid congruence structure that itself produces a subcritical Littlewood portal.

No such theorem is proved here. The important completed step is the negative one: the previously proposed beta-only cross-scale comparison has been eliminated as a source of new information, so future work should not spend a run rediscovering that coordinate tautology.

The full classical Littlewood conjecture remains **OPEN**.