# B17 FEI interface C — exact Boolean signed-resolvent sign reversal and a head/tail compensation ledger

**Run:** `20260921T220508Z-fleet03-B17-r11-fei-c`  
**Scope:** fleet03/B17, joint FEI interface C exact-Boolean adversary  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full uniform-cube FEI:** **OPEN / NOT PROVED**  
**Claim level:** one exact admissible Boolean counterexample to a tempting interface-C positivity bridge, plus a source-exact replacement ledger for the same witness. No publication-priority claim.

## 0. Route chosen before the computation

**NEW ROUTE `C-SIGNED-SCALE-OSCILLATION`.** Instead of trying another positive contraction of the compiler current into physical flags, keep the authentic Boolean-minus-comparator signed gate packet and attack its *resolvent-scale sign*. The test is: can the finite-resolvent gate difference itself be treated as a nonnegative debit, or must finite low/high windows cancel before any physical payment?

This is materially different from the preceding B17 moment-order obstruction and from the killed positive-current contractions. The calculation below uses one explicit admissible Boolean phase and one genuine `RM(1,4)` code extension; it is not another exhaustive FEI sweep.

## 1. Named completed peer result consumed

**consumed_peer_artifact:** fleet04/B16,
`proofnet24/P03-fei/fleet-2026-09-21/fleet04/B16/20260921T213921Z-finite-resolvent-rkhs-refund/REPORT.md`.

That report proves, at the authentic precompression gate level, for `M` containing `RM(1,n)`, gate bit `g=1_Q`, and Boolean phase `b_f`, the exact signed packet

\[
G_{M,g,f}(s)=\mathbb E_{m\in M}\big[\sin(su_f(m))\sin(sv_f(m))-\sin(su_0(m))\sin(sv_0(m))\big],
\]

and the exact finite-resolvent identity

\[
R_M(t)-R_{M+\langle g\rangle}(t)
=\frac N2\,\mathbb E_m\!\left[
\Phi_t((u_f+v_f)^2)-\Phi_t((u_f-v_f)^2)
-\Phi_t((u_0+v_0)^2)+\Phi_t((u_0-v_0)^2)
\right],
\tag{1.1}
\]
with `Phi_t(x)=x/(x+t)`. It also proves that distance four kills the quadratic term and that

\[
G(s)=\frac{2C_4}{N^4}s^4+O(s^6),
\tag{1.2}
\]
where `C_4` is the number of first-separated frustrated weight-four relations.

**applied_to_claim:** I apply (1.1) and (1.2) to an exact Boolean construction to test whether either the signed packet or its finite-resolvent windows may be promoted to a nonnegative debit merely because the scalar sine kernel is PSD and the quartic first separator is positive.

## 2. Exact admissible Boolean construction

Index the physical cube `F_2^4` lexicographically as integers `0,...,15`, with binary order `0000,0001,...,1111`. Let

\[
M=RM(1,4),\qquad N=16.
\]

Thus `M` consists of the 32 affine Boolean masks. Its dual is

\[
D=M^\perp=RM(2,4),
\]

with minimum nonzero weight four.

Take the gate face

\[
Q=\{0,3,4,7,9,10,12,15\},
\]

and `g=1_Q`. Exact enumeration of the 32 affine masks verifies `g\notin M`, so `M+<g>` is a genuine extension. Take the Boolean function

\[
f(x)=(-1)^{b_f(x)},\qquad
\{x:b_f(x)=1\}=F:=\{0,1,3,5,10,12,14,15\}.
\]

Both `Q` and `F` have eight points. No relaxed spectral law is used: `f` is an actual Boolean truth table.

For `z\in\{0,b_f\}` and `m\in M`, define integer numerators `U_z=16u_z`, `V_z=16v_z`. The exact pair multisets are

\[
\begin{array}{c|c}
(U_f,V_f)&\text{multiplicity}\\\hline
(2,-2),(-2,2)&12\text{ each}\\
(6,2),(-6,-2),(-2,-6),(2,6)&2\text{ each}
\end{array}
\tag{2.1}
\]

and

\[
\begin{array}{c|c}
(U_0,V_0)&\text{multiplicity}\\\hline
(0,0)&22\\
(-4,4),(4,-4)&4\text{ each}\\
(8,8),(-8,-8)&1\text{ each}.
\end{array}
\tag{2.2}
\]

The exact dual-code weight distribution is

\[
1+140z^4+448z^6+870z^8+448z^{10}+140z^{12}+z^{16}.
\tag{2.3}
\]

For this `(M,g,f)`, exact enumeration gives

\[
C_4=24,
\qquad \frac{2C_4}{N^4}=\frac3{4096}>0.
\tag{2.4}
\]

Thus this witness does **not** evade the peer quartic theorem by making the first separator vanish.

## 3. PROVED — the genuine signed finite-resolvent gate difference changes sign

Let

\[
\Delta_R(t):=R_M(t)-R_{M+\langle g\rangle}(t).
\]

From (2.1), the `f`-part of the expectation in (1.1) is

\[
A_f(t)=\frac14\Phi_t(1/4)-\Phi_t(1/16),
\tag{3.1}
\]

while from (2.2), the comparator part is

\[
A_0(t)=-\frac14\Phi_t(1/4)+\frac1{16}\Phi_t(1).
\tag{3.2}
\]

Since `N/2=8`, direct rational simplification gives the exact formula

\[
\boxed{
\Delta_R(t)
=8(A_f(t)-A_0(t))
=\frac{9(4t-1)}{2(t+1)(4t+1)(16t+1)}.
}
\tag{3.3}
\]

Every denominator is positive for `t>0`. Therefore

\[
\boxed{
\Delta_R(t)<0\quad(0<t<1/4),\qquad
\Delta_R(1/4)=0,\qquad
\Delta_R(t)>0\quad(t>1/4).
}
\tag{3.4}
\]

For an exact rational check,

\[
\boxed{\Delta_R(1/16)=-108/85.}
\tag{3.5}
\]

### Consequence: a genuine finite resolvent window is negative

An antiderivative normalized at zero is

\[
P(T)=\int_0^T\Delta_R(t)\,dt
=\log(4T+1)-\frac12\log(16T^2+17T+1).
\tag{3.6}
\]

Hence

\[
\boxed{
\int_{1/16}^{1/8}\Delta_R(t)\,dt
=\log\frac{2\sqrt{51}}{15}<0,
}
\tag{3.7}
\]

because `(2 sqrt(51))^2=204<225=15^2`.

This is an exact admissible Boolean counterexample to the candidate bridge

> **REFUTED:** every authentic finite-resolvent compiler gate/window is a nonnegative debit merely because the scalar finite-resolvent sine kernel is PSD.

The scalar kernel remains PSD exactly as fleet04/B16 proved. What fails is moving the Boolean-minus-comparator subtraction *inside* that positivity conclusion.

## 4. PROVED — even the Borel-time packet has both signs despite a positive quartic seed

The pair tables also give the exact trigonometric polynomial

\[
\boxed{
G(s)=\frac12\cos(s/4)-\frac14\cos(s/2)+\frac1{32}\cos s-\frac9{32}.
}
\tag{4.1}
\]

Its Taylor expansion begins

\[
G(s)=\frac3{4096}s^4-\frac5{131072}s^6+O(s^8),
\tag{4.2}
\]

whose quartic coefficient agrees exactly with (2.4) and the peer first-separator theorem. But

\[
G(\pi)=-\frac5{16}+\frac{\sqrt2}{4}>0,
\qquad
G(3\pi)=-\frac5{16}-\frac{\sqrt2}{4}<0.
\tag{4.3}
\]

Thus the positive `C_4` seed controls only the small-time germ. Higher signed relations reverse the sign at finite time. This is precisely the situation in which relationwise absolute values or a positive-current replacement destroy a real cancellation.

## 5. Replacement executed — exact head/tail compensation rather than positive window payment

After refuting finite-window positivity, the replacement mechanism is to keep the **signed resolvent scale** and carry a co-located tail refund before physical compression.

For this exact Boolean gate, (3.6) has the stronger property

\[
16T^2+17T+1-(4T+1)^2=9T>0,
\]
so

\[
P(T)<0\quad\text{for every finite }T>0.
\tag{5.1}
\]

At the same time,

\[
\lim_{T\to\infty}P(T)=0,
\]
which proves

\[
\boxed{\int_0^\infty\Delta_R(t)\,dt=0.}
\tag{5.2}
\]

Therefore the entire negative low-resolvent head is refunded *exactly* by the positive high-resolvent tail:

\[
\boxed{
\mathcal C(T)
:=\int_T^\infty\Delta_R(t)\,dt
=-P(T)
=\frac12\log\frac{16T^2+17T+1}{(4T+1)^2}>0.
}
\tag{5.3}
\]

This gives a concrete replacement ledger: do not require a finite window to be positive; propagate the signed head together with its exact high-scale companion until the Borel/entropy endpoint or until an independently justified R16/terminal credit is inserted. For this witness the companion is not hypothetical: (5.3) is its exact value.

This is consistent with, and makes concrete, the cross-account warning that the compensation must enter before final positivity. It is **not yet a universal payment theorem**: the remaining job is to identify, for every source gate of a putative high-ratio FEI core, a source-exact nonreused companion whose signed head/tail/R16/terminal combination admits the required original-coordinate `J` payment.

## 6. Boundary and FEI sanity checks

The construction is deliberately a bridge adversary, not an FEI counterexample. The Walsh transform of `f` has exactly four nonzero coefficients, all of squared mass `1/4`. Hence exactly

\[
H(f)=2,\qquad I(f)=5/2,\qquad H(f)/I(f)=4/5.
\tag{6.1}
\]

So no claim about disproving FEI follows from this example. Other boundary checks are exact:

- `M=RM(1,4)` has 32 masks and `D=M^perp` has 2048 words with minimum nonzero weight four;
- `g\notin M`, so the gate is not a degenerate repeated generator;
- `C_4=24>0`, so the sign reversal survives a genuinely positive quartic first separator;
- the sign change of `Delta_R` occurs at the exact threshold `t=1/4`;
- the negative finite window (3.7) and zero full integral (5.2) exhibit a real scale cancellation, not floating-point noise.

## 7. Exact checker

The standard-library checker `check_exact_resolvent_sign.py` reconstructs `RM(1,4)`, enumerates its dual exactly, verifies the pair tables, `g notin M`, `C_4=24`, the rational gate identity at several rational values including `-108/85`, and the exact Fourier boundary check. Its executed source SHA-256 is

`85921a6e198cb146bb739c0c9f04375368f04dea9e85c288329eca4d4fb49603`.

The archived output begins `EXACT_PASS`; output SHA-256 is

`b2bc713197c461ed7219a4ecb4794b8dc5d2c5065b1e06d23efe6a52afca7dd0`.

## 8. Status and handoff

**PROVED:** the exact construction and formulas (2.1)--(6.1).  
**REFUTED:** universal nonnegativity of authentic signed finite-resolvent gates/windows after the Boolean-minus-comparator subtraction.  
**NOT REFUTED:** fleet04/B16's scalar RKHS PSD theorem, signed full-time Borel identities, compensated signed bounds, critical-core-only bounds, or FEI itself.  
**Full FEI:** **OPEN**.

**remaining_implication:** prove a universal source-exact bound for the *compensated* signed scale ledger — finite low-window source plus its nonreused high-resolvent/R16/entropy/terminal companion — into original-coordinate physical cost, preferably after the existing restriction-critical reduction. Any argument that first forces each authentic finite window nonnegative is now dead.

**next_recipient:** `fleet03/B16` for the live signed-resolvent/window transfer and `fleet03/B18` for integration with the authentic parent/mask and terminal ledgers; `fleet02/B16` should use the exact sign-changing gate as a regression adversary for proposed companion credits.
