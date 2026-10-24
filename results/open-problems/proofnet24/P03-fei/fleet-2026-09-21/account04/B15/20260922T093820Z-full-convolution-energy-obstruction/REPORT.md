# account04/B15 — full Boolean-convolution L2 energy still loses the rare-event KL

**Run:** `20260922T093820Z-account04-B15-fei-r11`  
**Classification:** `ESSENTIAL_STEP_APPLIED / FULL_CONVOLUTION_L2_OBSTRUCTION`  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 0. Exact inherited remainder and mechanism change

This run follows owner control revision `2026-09-22.2` and the common all-gate FEI programme.  The newest completed account02/B15 result consumed is

`proofnet24/P03-fei/fleet-2026-09-21/account02/B15/20260922T085941Z-suspension-kl-no-loss/REPORT.md`.

It retains the entire negative relative-entropy credit after the exact influence I-projection.  For a nonempty biased spectral law `P=w^+`, its maximum-entropy conditional-product I-projection `Q_r`, and any proposed symmetric all-gate potential `Gamma`, the actual normalized unpaid remainder is exactly

\[
\boxed{
R_\Gamma=B_{\rm inf}^\Gamma+K_{\rm occ},
\qquad
K_{\rm occ}=D_{\rm KL,2}(P\|Q_r)=H_{\max}(r)-H(P),
}
\tag{0.1}
\]

where

\[
B_{\rm inf}^\Gamma=\sum_i r_i a_i-a_q-H_{\max}(r).
\tag{0.2}
\]

Thus the missing source-valid implication is to retain enough of `K_occ` to pay `[-B_inf^Gamma]_+`; no packet-integrality or credit-free interpolation is available.

The account02 suspension theorem also proves that, on the sparse one-point-defect suspensions used below, **every signed valuation-depth tail is exactly zero**.  Hence the valuation-tail bank supplies no positive payment on this family.

A fresh account03/B15 result,

`proofnet24/P03-fei/fleet-2026-09-21/account03/B15/20260922T092409Z-complement-packet-kl-gap/REPORT.md`,

proves a positive `c<1` KL gap from one complement packet, but correctly records that one packet can be exponentially small and proposes aggregating many Boolean convolution shifts or proving quantitative `c=1` lattice stability.

The present run executes that materially different continuation: **aggregate every nonzero Boolean convolution shift at once in the natural squared/Parseval energy.**  The result is a no-go theorem.  Even the full L2 family of convolution equations captures only `O(I)` on a genuine Boolean suspension where the indispensable KL is `Theta(m I)`.

## 1. Genuine Boolean sparse suspension

Fix `m>=2` and put

\[
p=2^{1-m}.
\tag{1.1}
\]

Let

\[
g_m(x)=1-2\mathbf 1_{\{x=0\}},
\qquad
F_m(y,x)=y g_m(x),
\tag{1.2}
\]

where `y` is a fresh unbiased bit.  Then `F_m` is balanced and Boolean.  The uniform Walsh coefficients of `g_m` are

\[
\widehat g_m(\varnothing)=1-p,
\qquad
\widehat g_m(T)=-p\quad(T\ne\varnothing).
\tag{1.3}
\]

Each old coordinate has influence `p`, so

\[
I(g_m)=mp,
\qquad
I(F_m)=1+mp.
\tag{1.4}
\]

The suspension I-projection of account02/B15 has the fresh coordinate deterministically active and the old coordinates independently active with probability `p`.  On the old-coordinate factor,

\[
Q_m(T)=p^{|T|}(1-p)^{m-|T|}.
\tag{1.5}
\]

The exact inherited quantities are

\[
H_{\max}=m h_2(p),
\qquad
K_{\rm occ}=m h_2(p)-H(g_m),
\tag{1.6}
\]

and at any finite balanced center `C=Gamma(1/2)`,

\[
B_{\rm inf}^C=C\,mp-mh_2(p).
\tag{1.7}
\]

Moreover

\[
H(g_m)=-(1-p)^2\log_2(1-p)^2+(2p-p^2)(2m-2).
\tag{1.8}
\]

Consequently

\[
\frac{H(g_m)}{mp}\to4,
\qquad
\frac{K_{\rm occ}}{mp}
=m-5+\frac1{\ln2}+o(1),
\tag{1.9}
\]

while every positive valuation-depth tail is zero and the folded-influence reserve satisfies `J(F_m)=mp`.

## 2. Aggregate all signed Boolean convolution equations

Use the **actual physical Fourier signs** from (1.3) on the I-projection magnitudes.  Define

\[
b_T=\operatorname{sgn}(\widehat g_m(T))\sqrt{Q_m(T)}.
\tag{2.1}
\]

For every shift `U subseteq [m]`, put

\[
C_m(U)=\sum_T b_T b_{T\triangle U}.
\tag{2.2}
\]

For an actual Boolean Walsh vector `a_T`, Booleanity `g^2=1` is exactly

\[
\sum_T a_Ta_{T\triangle U}=\mathbf1_{\{U=\varnothing\}}.
\tag{2.3}
\]

Thus the natural full squared convolution defect of the sign-aligned I-projection is

\[
\boxed{
\mathcal B_m:=\sum_{U\ne\varnothing} C_m(U)^2.
}
\tag{2.4}
\]

This uses **every** nonzero shift, not a selected packet or coordinate projection.

### Theorem 2.1 — exact full-shift energy

For `p=2^{1-m}`,

\[
\boxed{
\begin{aligned}
\mathcal B_m={}&-16(1-p)^{2m}+24(1-p)^m\\
&-8(1+p-2p^2)^m+(1+4p-4p^2)^m-1.
\end{aligned}
}
\tag{2.5}
\]

In particular,

\[
\boxed{
\mathcal B_m=4mp+O(m^2p^2),
\qquad
\frac{\mathcal B_m}{I(g_m)}\to4.
}
\tag{2.6}
\]

### Proof

Write

\[
A=\sqrt{1-p},\qquad B=\sqrt p,
\qquad
Z(x)=\prod_{i=1}^m(A+Bx_i).
\tag{2.7}
\]

The all-positive product amplitudes are the Walsh coefficients of `Z`.  Since the actual sign pattern is positive at the empty set and negative at every nonempty set, the sign-aligned I-projection amplitudes are the Walsh coefficients of

\[
G_m(x)=2A^m-Z(x).
\tag{2.8}
\]

Therefore

\[
C_m(U)=\widehat{G_m^2}(U).
\tag{2.9}
\]

Because the `b_T` have total squared mass one, `C_m(emptyset)=1`.  Parseval now gives

\[
\mathcal B_m=\mathbb E G_m^4-1.
\tag{2.10}
\]

Independence yields

\[
\mathbb EZ=A^m,
\qquad
\mathbb EZ^2=1,
\tag{2.11}
\]

\[
\mathbb EZ^3=[A(1+2p)]^m,
\qquad
\mathbb EZ^4=(1+4p-4p^2)^m.
\tag{2.12}
\]

Expanding `(2A^m-Z)^4`, using `A^2=1-p`, gives exactly (2.5).  Since `mp -> 0`, first-order binomial expansion of the four powers in (2.5) has constant term zero and linear term `4mp`; the remainder is `O(m^2p^2)`.  This proves (2.6).  QED.

The same computation applies to the full suspension: shifts containing the fresh `y` coordinate have zero autocorrelation because all I-projection amplitude mass contains `y`, while shifts in the old coordinates reproduce (2.2).  Hence no convolution energy is omitted by passing to the old factor.

## 3. Decisive no-go theorem

### Theorem 3.1 — no fixed quadratic full-shift price plus O(J) valuation reserve

Fix any finite real constants `A`, `L`, and finite center `C`.  Then for all sufficiently large `m`,

\[
\boxed{
B_{\rm inf}^C(F_m)+A\mathcal B_m+LJ(F_m)<0.
}
\tag{3.1}
\]

Yet the exact KL-retaining residual satisfies

\[
\boxed{
B_{\rm inf}^C(F_m)+K_{\rm occ}(F_m)
=C I(g_m)-H(g_m),
}
\tag{3.2}
\]

so for every fixed `C>4` the right side of (3.2) is positive for all sufficiently large `m`.

### Proof

Divide (3.1)'s left side by `I(g_m)=mp`.  Equations (1.7), (2.6), and `J(F_m)=mp` give

\[
C-\frac{h_2(p)}p+A(4+o(1))+L.
\tag{3.3}
\]

Since

\[
\frac{h_2(p)}p=m-1+\frac1{\ln2}+o(1),
\tag{3.4}
\]

(3.3) tends to `-infinity`.  Equation (3.2) is the exact account02/B15 suspension identity, and (1.9) gives its normalized limit `C-4`.  QED.

Equivalently,

\[
\boxed{
\frac{\mathcal B_m}{K_{\rm occ}(F_m)}\to0.
}
\tag{3.5}
\]

Thus the full family of signed Boolean convolution equations, when compressed into its natural unweighted quadratic/Parseval energy, loses the same rare-event logarithm that the exact negative KL retains.

## 4. What is refuted and what survives

**Refuted at universal scope:** any Interface-D transfer that replaces the exact dependence credit by a fixed dimension-independent multiple of the complete squared convolution defect, even after adding any fixed `O(J)` valuation reserve.  This includes the naive continuation “aggregate all complement/shift equations in L2 and pay the remainder from their total energy.”  It also rules out a `c=1` quantitative lattice-stability estimate of the form

\[
K_{\rm occ}\le A\mathcal B+L I
\tag{4.1}
\]

with fixed finite `A,L`.

**Not refuted:** the exact KL route; nonlinear or logarithmically weighted multi-shift statistics; source statistics that recover `K_occ` up to an additive `O(I)` loss; or FEI itself.  The obstruction is specifically to fixed quadratic compression of signed Booleanity.

The arithmetic lesson is sharp on this family.  The indispensable negative information credit is

\[
K_{\rm occ}=\Theta(mI),
\tag{4.2}
\]

all valuation-depth tails are **zero**, and even the complete convolution L2 energy is only

\[
\mathcal B=\Theta(I).
\tag{4.3}
\]

So the next viable Interface-D representation must preserve the **rare-event logarithm**: quantitatively, any coarsening `K_tilde <= K_occ` intended to combine with an `O(I)` arithmetic bank has to satisfy

\[
K_{\rm occ}-K_{\rm tilde}=O(I)
\tag{4.4}
\]

on these suspensions.  A bounded-energy Booleanity score cannot do that.

## 5. Independent calculation / falsification check

A standard-library checker independently enumerates all shifts for `m=2,...,6`, compares the direct sum (2.4) to the closed form (2.5), and prints normalized values farther out.  The largest direct-versus-formula discrepancy in those cases is below `4e-16`.

Representative normalized values `(B_m/I, K_occ/I, H/I)` are:

- `m=8`: `(3.174701975893502, 4.594262188037012, 3.842782591897924)`;
- `m=16`: `(3.992559373089739, 12.512401622344836, 3.930271404540879)`;
- `m=24`: `(3.999955654346498, 20.489137284805860, 3.953557670091778)`.

The checker is only a falsification/self-consistency test; Theorems 2.1 and 3.1 are analytic.

## 6. Handoff

**Consumed account02/B15 result:** `20260922T085941Z-suspension-kl-no-loss`, exact remainder `R=B_inf+K_occ`, suspension pullback, zero valuation tails, and no-loss requirement for the KL credit.

**Consumed account03/B15 result:** `20260922T092409Z-complement-packet-kl-gap`, especially its explicit proposal to aggregate many convolution shifts or attack the `c=1` branch.

**New proved inference:** even the complete unweighted squared convolution family is only `4I+o(I)` on the sparse suspension while `K_occ/I -> infinity`; therefore fixed quadratic aggregation plus any `O(J)` arithmetic reserve cannot pay the actual remainder.

**Remaining implication:** construct a source-valid statistic retaining the rare-event logarithm, i.e. recovering `K_occ` to additive `O(I)` on the suspension face, and compare it directly with `-B_inf`; or prove the all-gate inequality by another source-exact mechanism.  Do not spend another run merely rescaling the L2 convolution energy.

**Next recipients:** account02/B15 (exact KL/valuation lead), account03/B15 (conditional packet decomposition), and account03/B18 (Campaign-B integration).

No claim of novelty or publication priority is made.  No full FEI proof is claimed.
