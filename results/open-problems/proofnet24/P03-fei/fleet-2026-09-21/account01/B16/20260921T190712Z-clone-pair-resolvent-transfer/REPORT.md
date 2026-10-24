# B16 FEI signed transport — clone-pair physical resolvent transfer

**Date:** 21 September 2026  
**Scope:** `account01 / B16`, signed transport / noise interpolation, APPROACH 10/13  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Status of unrestricted FEI:** **OPEN / NOT PROVED**  
**Claim level:** a new exact clone-pair mask-transfer identity, a dimension-free double-inverse-noise payment for authentic ordered-min slice pairs, and a sharp obstruction at codimension one. No novelty or publication-priority claim.

## 0. Entering state and exact target

This run did not revisit the settled read-once certificate. It continued from the current signed-current chain.

The relevant proved inputs are:

1. the signed parity-current double-resolvent has a positive disintegration by doubled parent clone-pairs; on the central syndrome band its parent masses `mu_j` satisfy
   \[
   \sum_j\mu_j=E_{\rm cen},\qquad
   \sum_j\mu_jJ(g_j)\le E_{\rm cen}\le \frac{11}{192}W;
   \tag{0.1}
   \]
2. each authentic ordered-min parent `g_j` is a one-subcube defect; the two slice clones created by one dummy split multiply back to `g_j`;
3. the physical product-noise mask-resolvent theorem pays an already-positive mask transfer by folded mask influence, but the previous handoff still lacked a **no-reuse push-forward of the actual pair curvature**.

The point below is to avoid applying the mask theorem separately to the two fine clones. The correlation-flow derivative already contains the paired second difference
\[
(I-\tau_{j0})(I-\tau_{j1}),
\]
and that exact pairing has much more cancellation than the sum of two singleton mask costs.

No R32 coefficient is positive-parted. The theorem is uniform in an arbitrary background mask, so all other syndrome smoothing may be conditioned on and averaged afterwards. R16/moment refunds and the terminal mixed difference are not spent here.

---

## 1. Slice-pair setup

Let `A` be an affine subcube of codimension `c` in an old physical cube:
\[
A=\{x:x_F=a\},\qquad |F|=c.
\]
Write the parent phase
\[
g(x)=1-2\mathbf 1_A(x).
\]
Append one dummy bit `z` and split `g` into the two authentic slices
\[
h_b(x,z)=1-2\mathbf 1_A(x)\mathbf 1_{\{z=b\}},\qquad b\in\{0,1\}.
\tag{1.1}
\]
Then
\[
\boxed{h_0h_1=g}
\tag{1.2}
\]
with `g` lifted trivially in `z`.

For any Boolean phase `H` on the enlarged cube and translations `u,v`, put
\[
Q_H(y;u,v)=H(y)H(y+u)H(y+v)H(y+u+v),
\]
\[
P_H(u,v)=\Pr_y[Q_H(y;u,v)=-1].
\tag{1.3}
\]
Define the clone-pair mask second difference
\[
\boxed{
\mathfrak D_{h_0,h_1}P_H
:=P_H+P_{Hg}-P_{Hh_0}-P_{Hh_1}.
}
\tag{1.4}
\]
This is exactly the physical multiplication counterpart of the syndrome operator `(I-tau_0)(I-tau_1)`.

---

## 2. `B16-CLONE-PAIR-PLAQUETTE-TRANSFER` — PROVED

### Theorem 2.1 — exact paired identity

For every Boolean background phase `H` and every `u,v`,
\[
\boxed{
\mathfrak D_{h_0,h_1}P_H(u,v)
=-\frac12\,\mathbb E_y
\Big[Q_H(y;u,v)(1-Q_{h_0}(y;u,v))(1-Q_{h_1}(y;u,v))\Big].
}
\tag{2.1}
\]
Consequently
\[
\boxed{
|\mathfrak D_{h_0,h_1}P_H(u,v)|
\le 2\Pr_y[Q_{h_0}=-1,\ Q_{h_1}=-1].
}
\tag{2.2}
\]

#### Proof

Use `P_K=(1-E Q_K)/2` and `Q_{KL}=Q_KQ_L`. The constants in (1.4) cancel, while the correlation terms give
\[
-\frac12E\,Q_H(1+Q_{h_0}Q_{h_1}-Q_{h_0}-Q_{h_1})
=-\frac12E\,Q_H(1-Q_{h_0})(1-Q_{h_1}).
\]
The last product equals four exactly on the event that both slice plaquettes are frustrated and zero otherwise. This proves (2.1)--(2.2). `square`

The identity is uniform in `H`. Thus `H` may already contain an arbitrary product of all other compiler masks; no marginal cost from those other masks appears in this step.

---

## 3. Exact geometry of simultaneous slice frustration

Write a translation on the enlarged cube as
\[
u=(u',\alpha),\qquad v=(v',\beta),\qquad \alpha,\beta\in\mathbb F_2.
\]
Let `D_t 1_A(x)=1_A(x) xor 1_A(x+t)`.

If `(alpha,beta)=(0,0)`, the four corners stay in one dummy slice, so the two slice plaquettes cannot both be frustrated.

For the three remaining cases one checks directly from the four dummy labels:

- `(alpha,beta)=(1,0)`: simultaneous frustration implies
  \[
  D_{v'}1_A(x)=D_{v'}1_A(x+u')=1;
  \]
- `(alpha,beta)=(0,1)`: it implies
  \[
  D_{u'}1_A(x)=D_{u'}1_A(x+v')=1;
  \]
- `(alpha,beta)=(1,1)`: it implies
  \[
  D_{u'+v'}1_A(x)=D_{u'+v'}1_A(x+u')=1.
  \]

For an affine codimension-`c` subcube, `D_t1_A` vanishes if `t_F=0`; otherwise `A` and `A+t` are disjoint and
\[
\Pr_x[D_t1_A(x)=1]=2^{1-c}.
\tag{3.1}
\]
Therefore
\[
\boxed{
\Pr[Q_{h_0}=-1,Q_{h_1}=-1]\le2^{1-c}.
}
\tag{3.2}
\]
Combining with (2.2), for `c>=2`,
\[
\boxed{
|\mathfrak D_{h_0,h_1}P_H(u,v)|
\le2^{2-c}
=\frac2cJ(g),
}
\tag{3.3}
\]
because the folded physical influence of a codimension-`c>=2` one-subcube defect is
\[
J(g)=c2^{1-c}.
\tag{3.4}
\]

The pointwise estimate alone is not enough for two inverse-noise singularities. The next theorem keeps the exact small-noise vanishing.

---

## 4. `B16-CLONE-PAIR-DOUBLE-RESOLVENT` — PROVED

Let `U_s,V_t` be independent physical-coordinate product-noise translations on the **enlarged** cube, with every coordinate present independently with probabilities `s,t in [0,1/2]` respectively.

### Theorem 4.1 — product-small-noise payment

For every Boolean background phase `H` and every authentic slice pair of a parent of codimension `c>=2`,
\[
\boxed{
\mathbb E_{U_s,V_t}
|\mathfrak D_{h_0,h_1}P_H(U_s,V_t)|
\le4st(1-st)J(g).
}
\tag{4.1}
\]
Consequently the double inverse-noise resolvent is dimension-free:
\[
\boxed{
\int_0^{1/2}\!\int_0^{1/2}
\frac{
\mathbb E|\mathfrak D_{h_0,h_1}P_H(U_s,V_t)|
}{st}\,ds\,dt
\le\frac{15}{16}J(g).
}
\tag{4.2}
\]

#### Proof

Let `alpha=U_s(z)` and `beta=V_t(z)`. They are independent Bernoulli variables with means `s,t`.

For `(alpha,beta)=(1,0)`, simultaneous slice frustration requires `V'_F != 0`. Hence, by (3.1), this case contributes at most
\[
s(1-t)\,[1-(1-t)^c]2^{1-c}
\le st(1-t)J(g).
\tag{4.3}
\]
The `(0,1)` case contributes at most
\[
st(1-s)J(g).
\tag{4.4}
\]
For `(1,1)`, simultaneous frustration requires `(U'+V')_F !=0`. On each old coordinate the XOR is present with probability
\[
r=s+t-2st.
\]
Thus this case contributes at most
\[
st[1-(1-r)^c]2^{1-c}
\le st(s+t-2st)J(g).
\tag{4.5}
\]
Summing (4.3)--(4.5),
\[
\mathbb E\Pr_y[Q_{h_0}=-1,Q_{h_1}=-1]
\le2st(1-st)J(g).
\tag{4.6}
\]
Equation (2.2) gives (4.1). Finally
\[
4\int_0^{1/2}\!\int_0^{1/2}(1-st)\,ds\,dt
=4\left(\frac14-\frac1{64}\right)
=\frac{15}{16},
\]
which proves (4.2). `square`

This is stronger than applying the generic mask-transfer theorem separately to the two slice clones. All other syndrome masks may be frozen into `H`, so their raw selector marginals never enter the bound.

---

## 5. Central-current consequence: a no-reuse parent payment

The current central disintegration assigns a positive mass `mu_j` to each doubled parent pair `j`, and the total parent bank obeys (0.1). The pair operator on that parent is exactly the second difference in (1.4). Therefore, for the **pure physical plaquette mask-translation component** of the central current, Theorem 4.1 may be applied atom-by-atom in the positive current measure and then integrated.

No other parent is charged by an atom attached to `j`; the arbitrary background generated by all other masks is absorbed into `H`. Hence
\[
\boxed{
\mathcal T_{\rm cen}^{\rm pair/plaq}
\le\frac{15}{16}\sum_j\mu_jJ(g_j).
}
\tag{5.1}
\]
Using (0.1),
\[
\boxed{
\mathcal T_{\rm cen}^{\rm pair/plaq}
\le\frac{15}{16}E_{\rm cen}
\le\frac{55}{1024}W.
}
\tag{5.2}
\]

This closes the specific **base-phase mask-transfer surcharge** for the central clone-pair plaquette current without paying the two fine slices separately and without any ambient-number-of-generators factor.

What (5.2) does **not** do:

- it does not identify the remaining signed compiler curl with the original function's entire plaquette source;
- it does not spend or bound the terminal mixed-difference component;
- it does not spend R16/moment refunds, negative entropy credits or dual-code multiplicity;
- it therefore does not close FEI.

It removes one narrower obstruction: once a central `D_j` plaquette term is already present in the positive post-cancellation current measure, translating through its authentic dummy slice pair costs at most one parent folded-mask budget, with the explicit resolvent constant `15/16`.

---

## 6. Sharp structural obstruction at codimension one

The hypothesis `c>=2` is essential for a projective parent-only payment.

Take `c=1`, so the parent `g` is a character modulo sign and therefore
\[
J(g)=0.
\]
Its two dummy slices `h_0,h_1` are codimension-two defects. Let the background `H=1`, let `u` be the old constrained coordinate and `v` the dummy coordinate. Then every such square has exactly one `h_0`-negative corner and exactly one `h_1`-negative corner, so
\[
P_{h_0}(u,v)=P_{h_1}(u,v)=1,
\qquad
P_1(u,v)=P_g(u,v)=0.
\]
Thus
\[
\boxed{
|\mathfrak D_{h_0,h_1}P_1(u,v)|=2
\quad\text{while}\quad J(g)=0.
}
\tag{6.1}
\]
No bound `|D|<=C J(g)` can hold at `c=1` for any finite `C`.

This is compatible with the authentic ordered-min relation basis: its displacement is `e_i+w` with `w!=0`, so the relation generators being transported here have codimension at least two. If a future compiler reintroduces a character parent, that channel must be annihilated/refunded before the projective parent payment is applied.

---

## 7. Why this is a genuine route change

The previous open push-forward tried to pay a random syndrome translation by the marginals of all masks selected by the smoothing kernel. Those marginals can be large and recreate dummy/ambient losses.

The theorem above instead differentiates **the exact correlated clone pair** first. The four selector states appear with signs `+,+,-,-`, producing the paired second difference (1.4). Conditioning on every other selected mask leaves the same bound. Thus only the one parent whose clone correlation is being differentiated is charged.

This is precisely the signed cancellation that is lost if the two clone masks are positive-parted before the correlation derivative.

---

## 8. Verification and next target

The companion exact-rational checker verifies:

- the pointwise simultaneous-slice bound through parent codimension five over every translation pair;
- the codimension-one obstruction;
- 64 rational product-noise tests for codimensions two through five on the grid `{1/8,1/4,3/8,1/2}^2`;
- the symbolic inverse-resolvent constant `15/16`.

The largest tested ratio of exact simultaneous-frustration expectation to the right side of (4.6) is `313/384`, at `c=2,s=t=1/8`.

**Next attack.** Keep the terminal mixed difference inside the same clone-pair correlation derivative and ask whether it admits an analogue of (2.1) with an event supported on simultaneous slice frustration. If yes, the same product-small-noise argument can transfer the full plaquette-plus-terminal `D_j` atom; if not, the exact failure term is the next object that must be paired with the retained terminal-band ledger.

Full unrestricted FEI remains **OPEN / NOT PROVED**.
