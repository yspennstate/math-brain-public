# B18 FEI proof integration — exact parent-mask pivotization into the signed physical sink

**Date:** 21 September 2026  
**Scope:** `account03 / B18`, joint interface C  
**Execution:** **WITHOUT_VERIFIED_BRAIN**  
**Status of unrestricted FEI:** **OPEN / NOT PROVED**  
**Claim level:** exact universal theorem for the authentic one-subcube parent masks, plus an exact compatibility reduction. No novelty or publication-priority claim.

## 0. Exact implication attacked

The joint interface C asks account03/B18 to connect account02's authentic post-syndrome parent/mask representation to the signed physical curvature sink without silently assuming product noise or the uniform ordered-flag law.

The cross-account artifact used substantively is

`account02/B16/20260921T184541Z-actual-current-parent-mask-incidence/REPORT.md`.

It proves that, after legitimate same-syndrome signed aggregation, the central compiler has nonnegative authentic parent masses
\[
\mu_j=\sum_{R:\,j\ {\rm doubled}}
\frac{\varepsilon_{q_R,k_R}}{r_R}b_R^2,
\qquad
\sum_j\mu_j=E_{\rm cen},
\]
and the corresponding coarse parent phase \(g_j\) is a one-subcube defect. It also proves
\[
\sum_j\mu_j J(g_j)\le E_{\rm cen}\le \frac{11}{192}W.
\]
Account02/B18 then proved that an arbitrary physical pair measure can be paid by the plaquette frustration of such a mask, but it left open the compatibility with account03's **signed** derivative-curvature sink.

The statement proved below closes precisely that parent-side compatibility arrow. It does **not** construct the still-missing authentic source-to-positive-pair measure from the finite live Borel compiler.

## 1. Authentic one-subcube masks have constant derivative orientation

Let
\[
Q=\{x\in\mathbb F_2^n:x_F=a_F\},\qquad c=|F|,
\]
and let
\[
g_Q(x)=1-2\,1_Q(x).
\]
For a physical coordinate \(i\), on the quotient \(x_i=0\) put
\[
d_i(y)=\frac{g_Q(0,y)-g_Q(1,y)}2\in\{-1,0,1\}.
\]

### Theorem 1 — constant-orientation derivative row — PROVED

If \(i\notin F\), then \(d_i\equiv0\). If \(i\in F\), then
\[
d_i(y)=\sigma_i\,1\{y_{F\setminus\{i\}}=a_{F\setminus\{i\}}\},
\qquad \sigma_i\in\{-1,+1\}
\]
with \(\sigma_i\) independent of \(y\).

Hence for every \(w\) with \(w_i=0\), the opposite-orientation overlap
\[
o_i(w)=\Pr[d_i(y)=-d_i(y+w)\ne0]
\]
vanishes identically. Therefore the signed curvature
\[
\kappa_i(w)=\mathbb E(d_i(y)-d_i(y+w))^2
\]
equals the unsigned support-disagreement probability for this authentic mask.

**Proof.** If \(i\notin F\), flipping \(i\) cannot change membership in \(Q\). If \(i\in F\), an \(i\)-edge meets \(Q\) exactly when every other defining coordinate equals its prescribed bit. On every such edge the endpoint in \(Q\) is always the endpoint with \(x_i=a_i\), so the sign of the oriented derivative is fixed. The claimed formula and \(o_i=0\) follow. \(\square\)

For \(c\ge2\),
\[
\boxed{
\kappa_i(w)
=
2^{2-c}
1\{i\in F,\ w_{F\setminus\{i\}}\ne0\}.
}
\tag{1.1}
\]
For \(c=1\), \(g_Q\) is a character up to sign and every \(\kappa_i(w)=0\).

Thus the orientation bank that is essential for a generic Boolean function costs **nothing** on the authentic parent masks themselves.

## 2. Every frustrated arbitrary pair has an exact physical pivot

Account02/B18 proved for a one-subcube mask (indeed for every affine-subspace defect) that
\[
P_{g_Q}(u,v)
=
2^{2-c}
1\{u_F,v_F\ {\rm are\ linearly\ independent}\}.
\tag{2.1}
\]

### Theorem 2 — deterministic parent-pair pivotization — PROVED

For every \(u,v\in\mathbb F_2^n\):

* if \(u_F,v_F\) are dependent, then \(P_{g_Q}(u,v)=0\);
* if \(u_F,v_F\) are independent, choose any \(i\in F\) with
  \((u_i,v_i)\ne(0,0)\), and define
  \[
  w=
  \begin{cases}
  v,&(u_i,v_i)=(1,0),\\
  u,&(u_i,v_i)=(0,1),\\
  u+v,&(u_i,v_i)=(1,1).
  \end{cases}
  \tag{2.2}
  \]
  Then \(w_i=0\), \(w_{F\setminus\{i\}}\ne0\), and
  \[
  \boxed{P_{g_Q}(u,v)=\kappa_i(w)=2^{2-c}.}
  \tag{2.3}
  \]

**Proof.** Equation (2.1) gives the dependent case. In the independent case, the definition (2.2) cancels the chosen pivot bit, so \(w_i=0\). If \(w_{F\setminus\{i\}}=0\), then the two projected vectors \(u_F,v_F\) would be equal or one would be zero, contradicting independence. Equation (1.1) therefore gives \(\kappa_i(w)=2^{2-c}\), which is (2.1). \(\square\)

The pivot can be made deterministic, for example by choosing the least defining coordinate with a nonzero pair \((u_i,v_i)\). No random order, product-noise law, or averaging argument is required.

## 3. Exact compatibility with the account02 authentic parent bank

For \(c\ge2\), the folded physical influence of the mask is
\[
J(g_Q)=c\,2^{1-c}.
\]
Thus on every pivotized frustrated pair,
\[
\boxed{
\kappa_i(w)=P_{g_Q}(u,v)
=\frac{2}{c}J(g_Q)\le J(g_Q).
}
\tag{3.1}
\]
The universal constant one is sharp at \(c=2\). For \(c=1\), both sides are zero.

Let \(\Lambda_j\) be any finite nonnegative measure on ordered physical pairs \((u,v)\) with total mass at most \(\mu_j\). Push its rank-two part forward by the deterministic map (2.2), discarding the zero-cost dependent part. Call the resulting measure \(\widetilde\Lambda_j\) on physical pivots \((i,w)\). Then
\[
\boxed{
\int P_{g_j}(u,v)\,d\Lambda_j
=
\int \kappa^{g_j}_i(w)\,d\widetilde\Lambda_j
\le \mu_j J(g_j).
}
\tag{3.2}
\]
Summing the **actual** account02/B16 parent masses gives
\[
\boxed{
\sum_j\int \kappa^{g_j}_i(w)\,d\widetilde\Lambda_j
\le
\sum_j\mu_jJ(g_j)
\le E_{\rm cen}
\le\frac{11}{192}W.
}
\tag{3.3}
\]

This is the requested interface-C compatibility result: once the authentic compiler has produced a positive parent-indexed pair measure with the already-derived parent masses, its mask contribution lands exactly in a signed physical derivative-curvature sink, with no orientation loss and no requirement that the pair law equal the uniform ordered-flag law.

### Gauge compatibility

For \(c\ge2\), every nonzero coordinate influence of a one-subcube defect is \(2^{1-c}\le1/2\), so the minimizing-character gauge does not alter these physical derivative rows. For \(c=1\), the mask is itself a character modulo sign and the plaquette/signed-curvature cost is zero. Thus the reduction introduces no hidden character-gauge expenditure.

## 4. What remains unpaid

The following arrow is still **OPEN / UNPAID**:
\[
\boxed{
\text{authentic finite-live-window signed double-resolvent source}
\Longrightarrow
\{\Lambda_j\ge0:\ \Lambda_j(G\times G)\le\mu_j\}.
}
\tag{4.1}
\]
This is the signed/PSD source-to-physical-pair contraction. It must preserve the live Borel window, nested terminal subtraction, dual-code multiplicity, negative credits, moment/R16 refunds, and no-reuse bookkeeping.

The present theorem removes a different obstruction: **given** such a positive parent-indexed pair representation, there is no further mismatch between account02's arbitrary parent-mask pairs and account03's signed physical sink.

A stronger shortcut is deliberately not claimed. A generic arbitrary pair measure can be singular (even a point mass), so it need not equal or be dominated by the uniform ordered-flag law used in the generic \(f\)-level signed-flag theorem. The special one-subcube geometry is what supplies the pointwise payment (3.1).

## 5. Refutation attempt and exact finite check

The likely failure mode was an orientation mismatch: a physical pivot could reproduce plaquette support disagreement while the signed derivative reversed on overlap, producing the \(4o_i\) term seen for generic Boolean parity. Theorem 1 rules this out exactly for authentic one-subcube parent masks.

`check_parent_signed_pivotization.py` exhaustively checks every coordinate-subcube defect through dimension five, every affine location, every ordered pair of translations, and every physical-pivot flag. Exact integer/Fraction arithmetic gives:

```
PASS
pair_cases=270088
zero_pair_cases=92320
flag_cases=22266
max_P_over_J=1
sharp_codim2_cases=17976
```

The computation verifies the rank-two formula, vanishing opposite-orientation overlap, deterministic pair-to-pivot equality, and sharp constant one. It is falsification/self-check evidence; the all-dimensional result is the symbolic proof above.

## 6. Classification and next recipient

**PROVED:** exact constant-orientation derivative form for authentic one-subcube parents; exact arbitrary-pair-to-signed-pivot map; exact measure pushforward identity; parent-side payment by the already-proved authentic bank \(\sum_j\mu_jJ(g_j)\le11W/192\).

**CONDITIONAL:** inserting (3.3) into the complete compiler still requires the positive parent-indexed pair measures in (4.1).

**REFUTED/DEAD SHORTCUT:** treating an arbitrary compiler pair law as if it were the uniform ordered-flag law is unnecessary and unjustified; singular pair measures are allowed. The pointwise one-subcube theorem replaces that requirement.

**OPEN:** (4.1), then the live-window/no-reuse terminal and credit bookkeeping, and finally unrestricted FEI.

**Consumed peer artifact:** `account02/B16/20260921T184541Z-actual-current-parent-mask-incidence/REPORT.md`, together with account02/B18's `20260921T190755Z-affine-subspace-plaquette-payment/REPORT.md`.

**Applied to claim:** interface C, authentic parent-mask pair response \(\to\) account03 signed physical curvature sink.

**Remaining implication:** construct the genuine finite-window signed/PSD source-to-positive-pair contraction with parent masses bounded by the exact \(\mu_j\).

**Next recipient:** account03/B16 for the two-copy finite-window polarization, and account02/B16/B18 for the authentic-source representation side.

**Full unrestricted FEI remains OPEN / NOT PROVED.**
