# B16 FEI signed transport — parity-safe Hardy/R16 weight bridge

**Date:** 21 September 2026  
**Scope:** `account04 / B16`, FEI signed transport proof  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Status of unrestricted FEI:** **OPEN / NOT PROVED**  
**Claim level:** exact signed algebraic reduction plus a conditional payment corollary. No novelty or publication-priority claim.

## 0. Fresh entering state

This run continues the newest compatible signed-transport chain rather than an older shortcut.

The account04 first-hit reduction writes the common-order fluctuation as an internal Bernoulli-curvature bank plus a radial moment bank. For each active q-flip `v`,
\[
m_v(t)=\sum_{A:v\in R_A} c_A t^{q_A-1},
\qquad q_A=|R_A|,
\]
and every frustrated `q_A` is positive and odd. The account01 Hardy handoff proves
\[
\operatorname{Var}_{[0,1]}m_v
=\|D(I+D)^{-1}m_v\|_2^2
\]
and the exact dyadic decomposition
\[
\operatorname{Var}_{[0,1]}m_v
=\frac12V_{-,v}+\frac12V_{+,v}+B(m_v)^2.
\]
The newly arrived account01 high-resolvent compression also proves
\[
\Delta_{\infty,>2}
=\sum_Sp_S\log\frac3{2+p_S}
\le 2\log(3/2)J
\]
and hence an aggregate R16 bank floor
\[
\mathcal B_d\ge
[\kappa_2-2\log(3/2)-\varepsilon_d]J,
\qquad
\kappa_2=\frac23+\operatorname{artanh}(1/2).
\]

The calculation below identifies the **low radial half** with exactly the scalar collision weights appearing in R16. It does not yet prove the remaining signed moment domination between the q-flip first-hit demand and the authentic R16 deposits.

---

## 1. Signed same-degree aggregation

For each physical q-flip coordinate `v`, group the signed relation coefficients by the odd first-hit support size:
\[
a_{v,q}:=
\sum_{\substack{A:v\in R_A\\q_A=q}}c_A,
\qquad q\in\{1,3,5,\ldots\}.
\]
No absolute value is taken. In particular `0 mod 4` R32 debits and `2 mod 4` R32 credits remain combined inside `a_{v,q}`.

Put
\[
u_{v,q}:=\frac{q-1}{q}a_{v,q}.
\]
The Hardy transfer function `(q-1)/q` annihilates `q=1` exactly. Therefore the first nonzero radial degree is `q=3`.

Define the signed collision-demand coefficients
\[
\boxed{
\Gamma_j:=
\sum_v
\sum_{\substack{q+r=j\\q,r\ {\rm odd}}}
u_{v,q}
u_{v,r}.
}
\tag{1.1}
\]
The individual `Gamma_j` need not be nonnegative.

Expanding back through the relation supports gives the dual-code form
\[
\boxed{
\Gamma_j
=
\sum_{\substack{A,B\\q_A+q_B=j}}
|R_A\cap R_B|
\frac{(q_A-1)(q_B-1)}{q_Aq_B}
c_Ac_B.
}
\tag{1.2}
\]
Using the inherited syndrome identity
\[
|R_A\cap R_B|
=\frac{q_A+q_B-q_{A\triangle B}}2,
\]
this becomes
\[
\boxed{
\Gamma_j
=
\frac12
\sum_{\substack{A,B\\q_A+q_B=j}}
(j-q_{A\triangle B})
\frac{(q_A-1)(q_B-1)}{q_Aq_B}
c_Ac_B.
}
\tag{1.3}
\]
Thus the new demand sequence keeps the exact even symmetric-difference channel of the common-order Ward kernel.

---

## 2. `P03-B16-HARDY-R16-PARITY-WEIGHT-BRIDGE` — PROVED

Let
\[
\mathcal L_-:=
\frac12\sum_vV_{-,v}
\]
be the actual low-half contribution in the law-of-total-variance decomposition of the radial bank.

### Theorem

For every finite signed first-hit relation family with odd `q_A`,
\[
\boxed{
\mathcal L_-
=
\sum_{\substack{j\ge6\\ j\ {\rm even}}}
\frac{\Gamma_j}{(j-1)2^{j-1}}.
}
\tag{2.1}
\]

These are **exactly** the R16 high-resolvent scalar weights
\[
w_j=\frac1{(j-1)2^{j-1}}
\]
at even collision order.

### Proof

The account01 Hardy identity gives, after `t=u/2`,
\[
V_{-,v}
=
\int_0^1
\left[
\sum_q2^{-(q-1)}
u_{v,q}u^{q-1}
\right]^2du.
\]
Expand the square:
\[
V_{-,v}
=
\sum_{q,r}
\nu_{v,q}
u_{v,r}
\frac{2^{-(q+r-2)}}{q+r-1}.
\]
Multiplication by the `1/2` from the total-variance decomposition turns the coefficient into
\[
\frac1{(q+r-1)2^{q+r-1}}.
\]
Set `j=q+r` and sum over `v`; this is exactly (2.1).

Because `q,r` are odd, `j` is even. Because the Hardy multiplier kills `q=1`, every nonzero term has `q,r>=3`, hence `j>=6`. No odd R16 order appears, and neither the `j=2` nor `j=4` R16 channel is touched. QED.

### Borel-integrated form

The proof is pointwise in any Borel scale on which `c_A=c_A(s)`. With any nonnegative integrable Borel weight, Fubini gives the same identity after replacing `Gamma_j` by its signed integrated value. No scale-dependent first-hit order is introduced.

---

## 3. Exact tail constant

The inherited R16 first-separation bound is
\[
0\le D_{d,j}\le jJ.
\]
The full positive-even coefficient envelope is
\[
\sum_{\substack{j\ge2\\j\ {\rm even}}}
\frac{j}{(j-1)2^{j-1}}
=
\frac23+\operatorname{artanh}(1/2)
=\kappa_2.
\tag{3.1}
\]
But the Hardy low-half demand starts only at `j=6`. Hence its reachable R16 envelope is
\[
\begin{aligned}
\kappa_{\ge6}
&:=
\sum_{\substack{j\ge6\\j\ {\rm even}}}
\frac{j}{(j-1)2^{j-1}}\\
&=\kappa_2-1-\frac16\\
&=\operatorname{artanh}(1/2)-\frac12\\
&=\boxed{\frac{\log3-1}{2}}
=0.0493061443340548\ldots.
\end{aligned}
\tag{3.2}
\]
So the exact coefficient geometry localizes the low radial demand to a very small part of the old even R16 envelope.

This is a coefficient-envelope statement, not yet a payment theorem for the authentic q-flip demand.

---

## 4. Precise remaining signed bridge

The new exact sufficient inequality is now
\[
\boxed{
\sum_{\substack{j\ge6\\j\ {\rm even}}}
w_j\Gamma_j
\le
\sum_{\substack{j\ge6\\j\ {\rm even}}}
w_jD_{d,j},
\qquad
w_j=\frac1{(j-1)2^{j-1}}.
}
\tag{4.1}
\]

If (4.1) is proved for the authentic Borel-integrated first-hit coefficients at the chosen completed prefix, then
\[
\boxed{
\mathcal L_-
\le
\frac{\log3-1}{2}\,J.
}
\tag{4.2}
\]

This implication preserves all signs inside `Gamma_j`; it does not require `Gamma_j>=0` termwise.

Combining (4.2) with the newly proved account01 bank floor gives, conditionally,
\[
\mathcal B_d-\mathcal L_-
\ge
\left[
\frac76-2\log\frac32-\varepsilon_d
\right]J.
\tag{4.3}
\]
The limiting coefficient is
\[
\frac76-2\log\frac32
=0.355736450450338\ldots.
\]
For `d>=3`, where `epsilon_d<=1/32`, the remaining aggregate reserve is still greater than `0.32448 J`.

Thus **if** (4.1) is established, the low radial half fits strictly inside the already-proved aggregate R16 reserve. It would not need the terminal endpoint or the odd R16 refunds. The hard radial burden would then be localized to the high half `V_+` plus the signed bridge scalar `B(m)^2`, exactly where the terminal/Shapley machinery is authorized to act.

No such conclusion is claimed before (4.1) is proved.

---

## 5. Negative credits survive the low-half projection

A tempting stronger shortcut would be to assert `Gamma_j>=0` and compare collision orders separately. That is false.

For one first-hit coordinate take
\[
a_3=-2,\qquad a_5=1.
\]
Then
\[
\nu_3=-\frac43,\qquad \nu_5=\frac45,
\]
so
\[
\Gamma_6=\frac{16}{9},\qquad
\Gamma_8=-\frac{32}{15},\qquad
\Gamma_{10}=\frac{16}{25},
\]
while the total low-half contribution remains positive:
\[
\frac12V_-=\frac{149}{16800}.
\]
Therefore the `j=8` term is a genuine signed refund. Any proof of (4.1) should preserve the weighted sum rather than positive-part every collision order.

The inherited genuine q=3 opposite-sign Borel diagnostic gives the same message in an admissible Boolean configuration. For the two `+1/8,-1/8` relations with overlap two, the full radial cross refund is
\[
-\frac1{180},
\]
and its low-half contribution is exactly
\[
\boxed{-\frac1{5760}},
\]
the factor `2^{-(3+3-1)}=1/32` predicted by (2.1). Thus negative R32 credit remains negative after the Hardy/R16 projection.

---

## 6. What changed in the proof obligation

Before this calculation the low-half Hardy square and R16 alternating moment bank only had a qualitative “same exponential scale” resemblance.

Now the scalar weights agree **exactly**, the parity support is explicit, the first two positive-even R16 channels are proved absent from the low radial demand, and the remaining mismatch is a single signed dual-code moment domination (4.1).

This is compatible with the newest high-resolvent compression: that result says not to re-pay the whole R16 high-resolvent channel order by order. The present theorem instead identifies a small-resolvent transport sub-demand whose coefficient geometry can, conditionally, fit inside the aggregate R16 reserve that remains after the high-resolvent channel has already been accounted for.

The next attack is therefore not another generic norm estimate. It is to prove (4.1) directly from the authentic pointwise Borel coefficients
\[
c_A(s)=2N(-1)^{|A|/2}
\sin^{|A|}(s/N)\cos^{N-|A|}(s/N),
\]
using
\[
q_{A\triangle B}\ {\rm even},
\qquad
|R_A\cap R_B|=\frac{q_A+q_B-q_{A\triangle B}}2,
\]
and the R16 first-separation moment representation, before integrating in the Borel scale. If that signed weighted domination fails on an admissible Boolean family, preserve the counterexample and change mechanism.

**Full FEI remains OPEN / NOT PROVED.**

---

## 7. Exact self-check

`check_hardy_r16_weight_bridge.py` uses only standard-library exact rational arithmetic for the algebraic identities. It verifies:

- 625 signed coefficient vectors on degrees `q=3,5,7,9`;
- the exact identity `(1/2)V_- = sum_j Gamma_j/((j-1)2^(j-1))`;
- 49 `q=1` cases showing exact Hardy annihilation of the constant first-hit mode;
- parity (`j` even) and first nonzero collision order (`j=6`);
- an explicit signed collision refund (464 of the 625 test vectors have at least one negative `Gamma_j`);
- the genuine q=3 opposite-sign diagnostic `-1/180 -> -1/5760`;
- the closed-form tail constant `(ln 3 - 1)/2`.

Observed output is stored in `verification.json`. The checker is falsification evidence; Theorem (2.1) and the closed-form series identity are proved analytically above.
