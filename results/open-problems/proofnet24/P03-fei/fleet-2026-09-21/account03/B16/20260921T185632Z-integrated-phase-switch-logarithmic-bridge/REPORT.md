# B16 FEI signed transport — integrated phase-switch logarithmic bridge

**Date:** 21 September 2026  
**Scope:** `account03 / B16`, FEI signed transport proof  
**Execution:** **WITHOUT_VERIFIED_BRAIN**  
**Status of unrestricted FEI:** **OPEN / NOT PROVED**  
**Claim level:** exact signed Borel-in-time identities, a terminal-aware entropy representation, an exact finite-window kernel, and two route obstructions. No claim of a complete FEI proof, novelty, or publication priority.

## 0. Fresh state, required read order, and route change

This run obeyed the live owner order `FEI-SEVEN-TASKS-2026-09-21`. Before new mathematics it read, in order,

1. `proofnet24/P03-fei/continuations/2026-09-21-readonce-certificate/TASKS_2026-09-21.md`,
2. `REPORT.md`,
3. `APPROACHES.md`.

The read-once branch still says unrestricted FEI is open, the old `6.4547837` global target is too small, and the previously proposed cancellation constant `2.2273918583` is refuted. Nothing below uses either refuted constant.

Fresh compatible signed-transport inputs were then recovered from current `master`, including:

- account04/B16's **global phase-switch Dirichlet reduction and quartic dual-code cancellation**, which proves that after exact signed same-syndrome aggregation the current is controlled by a phase-switch square and that the quadratic phase response vanishes for every residual code `E <= C0`;
- account02/B16's actual current parent-mask incidence package;
- account03/B18's exact physical ordered-flag square bank;
- the inherited exact Borel/R32 representation and the live finite corridor
  \[
  4\int_{40}^{S_f}G_{\rm live}(s)\,s^{-3}\,ds,\qquad
  S_f=2\sqrt{N/J(f)}.
  \]

A newer B18 transverse-near-subcube theorem was also read to avoid duplicating its restriction/derivative-support route.

The present run changes route.  Instead of bounding the phase switch at each Borel time and then integrating an envelope, it **integrates the exact signed phase switch first**.  The distance-four quadratic cancellation is precisely what makes that operation finite.  This produces a logarithmic kernel and an entropy-difference identity retaining the terminal code subtraction.

No R32 coefficient is absolute-valued before the cancellation.  The R16 moment-refund bank, negative `2 mod 4` entropy credits, dual-code multiplicity, original-coordinate geometry, and the pre-existing terminal-band payment are not spent in the proofs below.

---

## 1. Setup

Let
\[
V=\mathbb F_2^n,\qquad N=|V|=2^n,
\]
and
\[
C_0=RM(1,n)^\perp.
\]
Let `E <= C0` be any residual relation code and write
\[
P=E^\perp.
\]
For a Boolean phase \(u:V\to\{\pm1\}\) and a truth-table word \(r\in\mathbb F_2^V\), put
\[
c_r(u):=\frac1N\sum_{x\in V}u(x)(-1)^{r_x}.
\tag{1.1}
\]
The exact dual-code Borel potential from the live compiler is
\[
\Phi_{E,s}(u)
=
\frac{2N}{|P|}
\sum_{r\in P}\cos\!\bigl(s\,c_r(u)\bigr).
\tag{1.2}
\]

Fix the actual Boolean phase \(f\), and split
\[
\Omega_\pm=\{x:f(x)=\pm1\}.
\]
For a twist \(h\), define
\[
A_r^\pm
=
\frac1N
\sum_{x\in\Omega_\pm}h(x)(-1)^{r_x}.
\tag{1.3}
\]
Then
\[
c_r(h)=A_r^++A_r^-,
\qquad
c_r(fh)=A_r^+-A_r^-.
\tag{1.4}
\]

The fresh phase-switch theorem gives
\[
\Phi_{E,s}(h)-\Phi_{E,s}(fh)
=
-\frac{4N}{|P|}
\sum_{r\in P}
\sin(sA_r^+)\sin(sA_r^-).
\tag{1.5}
\]

Because \(E\le C_0\) has no weight-two word,
\[
\boxed{
\sum_{r\in P}A_r^+A_r^-=0.
}
\tag{1.6}
\]
This identity is the only cancellation needed for the first theorem below.

---

## 2. PROVED — exact full-time logarithmic kernel

Define, for \(c\in\mathbb R\),
\[
\mathcal C(c)
:=
\int_0^\infty
\frac{
\cos(cs)-1+\frac12c^2s^2\mathbf 1_{\{s<1\}}
}{s^3}\,ds.
\tag{2.1}
\]

### Lemma 2.1

For \(c\ne0\),
\[
\boxed{
\mathcal C(c)
=
\frac{c^2}{2}
\left(
\log|c|+\gamma-\frac32
\right),
}
\tag{2.2}
\]
with the continuous value \(\mathcal C(0)=0\).

### Proof

Differentiate twice under the integral:
\[
\mathcal C''(c)
=
\int_0^\infty
\frac{\mathbf1_{\{s<1\}}-\cos(cs)}{s}\,ds
=
\gamma+\log|c|.
\tag{2.3}
\]
The last equality is the standard cosine-integral identity.  Since
\(\mathcal C(0)=\mathcal C'(0)=0\), integrating twice gives (2.2). \(\square\)

For \(a,b\in\mathbb R\), use
\[
\sin(as)\sin(bs)
=
\frac12\{\cos((a-b)s)-\cos((a+b)s)\}.
\tag{2.4}
\]
The individual integral against \(s^{-3}\) diverges at zero whenever
\(ab\ne0\), but a signed family satisfying \(\sum \alpha_j a_jb_j=0\)
has a finite sum.

### Theorem 2.2 — `P03-B16-SIGNED-LOG-KERNEL`

If a finite signed packet satisfies
\[
\sum_j\alpha_j a_jb_j=0,
\tag{2.5}
\]
then
\[
\boxed{
\int_0^\infty
\frac{\sum_j\alpha_j\sin(a_js)\sin(b_js)}{s^3}\,ds
=
\frac14
\sum_j\alpha_j
\left[
(a_j-b_j)^2\log|a_j-b_j|
-
(a_j+b_j)^2\log|a_j+b_j|
\right].
}
\tag{2.6}
\]
The convention is \(0^2\log0:=0\).

### Proof

Insert (2.4) into the regularized primitive (2.1).  The difference of
the two quadratic regularizers for one pair is
\[
\frac14\bigl((a-b)^2-(a+b)^2\bigr)s^2
=-ab\,s^2.
\]
After summing, (2.5) kills that entire regularization.  Formula (2.2)
then gives (2.6); the common
\((\gamma-\frac32)\bigl((a-b)^2-(a+b)^2\bigr)\) term also vanishes by
(2.5). \(\square\)

This theorem is deliberately **signed**.  It is not true as a finite
termwise-absolute integral.

---

## 3. PROVED — codewise integrated phase switch is an entropy increment

Put
\[
\psi(t)=
\begin{cases}
t^2\log(1/t^2),&t\ne0,\\
0,&t=0.
\end{cases}
\tag{3.1}
\]
For \(P=E^\perp\), define the normalized dual-code entropy functional
\[
\boxed{
\mathscr H_E(u)
:=
\frac{N}{|P|}
\sum_{r\in P}\psi(c_r(u)).
}
\tag{3.2}
\]

### Theorem 3.1 — `P03-B16-INTEGRATED-PHASE-ENTROPY`

For every \(E\le C_0\), every Boolean \(f,h\),
\[
\boxed{
\int_0^\infty
\frac{\Phi_{E,s}(h)-\Phi_{E,s}(fh)}{s^3}\,ds
=
\frac12
\left[
\mathscr H_E(fh)-\mathscr H_E(h)
\right].
}
\tag{3.3}
\]

### Proof

Set \(a=A_r^+\), \(b=A_r^-\).  By (1.6), the family with uniform
weights satisfies the quadratic-cancellation hypothesis of Theorem
2.2.  Multiplying (2.6) by the factor \(-4N/|P|\) from (1.5) gives
\[
-\frac{N}{|P|}
\sum_r
\left[
(a-b)^2\log|a-b|
-
(a+b)^2\log|a+b|
\right].
\]
Since
\[
t^2\log|t|=-\frac12\psi(t)
\]
and \(a-b=c_r(fh)\), \(a+b=c_r(h)\), this is exactly (3.3). \(\square\)

So the entire Borel-time integral, including the previously awkward
large-\(s\) range, is an exact entropy increment.  This is an identity,
not an estimate.

---

## 4. PROVED — the dual-code entropy is a coset average of ordinary Fourier entropy

Let
\[
P_0=C_0^\perp=RM(1,n).
\]
Because \(E\le C_0\), \(P_0\le P\).

### Theorem 4.1 — `P03-B16-DUAL-COSET-ENTROPY`

Choose one representative \(q\) from each coset in \(P/P_0\).  Then
\[
\boxed{
\mathscr H_E(u)
=
\mathbb E_{q\in P/P_0}
H_{\rm nat}\!\left(u(-1)^q\right).
}
\tag{4.1}
\]

In particular,
\[
\boxed{
\mathscr H_{C_0}(u)=H_{\rm nat}(u).
}
\tag{4.2}
\]

### Proof

Fix one coset \(q+P_0\).  Every element of \(P_0=RM(1,n)\) is an
affine character: one linear Fourier frequency and one constant bit.
Hence
\[
c_{q+a}(u)
\]
runs through the ordinary Fourier coefficients of \(u(-1)^q\), each
twice with opposite sign.  Since \(\psi\) is even,
\[
\sum_{r\in q+P_0}\psi(c_r(u))
=
2H_{\rm nat}(u(-1)^q).
\tag{4.3}
\]
There are \(|P|/(2N)\) cosets.  Multiplying (4.3) by \(N/|P|\)
therefore produces exactly the uniform coset average (4.1).
Equation (4.2) is the one-coset case. \(\square\)

This keeps the **full dual-code multiplicity**.  No representative
is counted as though it were a single relation.

---

## 5. PROVED — retained terminal-aware entropy bridge

Now take the live retained pair
\[
E_0=C_0,\qquad E_1=D_d,
\]
with
\[
P_0=RM(1,n),\qquad P_1=D_d^\perp,
\]
and retained potential
\[
\Psi_s=\Phi_{C_0,s}-\Phi_{D_d,s}.
\tag{5.1}
\]

Define the terminal-aware entropy defect
\[
\boxed{
\mathscr D_d(u)
:=
H_{\rm nat}(u)-\mathscr H_{D_d}(u).
}
\tag{5.2}
\]

### Corollary 5.1 — `P03-B16-RETAINED-INTEGRATED-ENTROPY-BRIDGE`

For every Boolean twist \(h\),
\[
\boxed{
\int_0^\infty
\frac{\Psi_s(h)-\Psi_s(fh)}{s^3}\,ds
=
\frac12
\left[
\mathscr D_d(fh)-\mathscr D_d(h)
\right].
}
\tag{5.3}
\]

### Proof

Subtract Theorem 3.1 for \(E=C_0\) and \(E=D_d\), then use
\(\mathscr H_{C_0}=H_{\rm nat}\). \(\square\)

This is the main advance of the run.  The exact signed terminal
subtraction survives the entire Borel integration and becomes one
difference of terminal-aware entropy defects.  There is no
pointwise absolute value and no separate payment for the terminal
code.

It is **not** yet a proof of FEI.  A signed full-line endpoint identity
does not by itself control positive turnover on the finite live
corridor.

---

## 6. PROVED — exact finite Borel-window kernel

For \(c\in\mathbb R\) and \(s>0\), define
\[
\boxed{
J_c(s)
=
-\frac{\cos(cs)}{2s^2}
+\frac{c\sin(cs)}{2s}
-\frac{c^2}{2}\operatorname{Ci}(|c|s),
}
\tag{6.1}
\]
with the continuous \(c=0\) value
\[
J_0(s)=-\frac1{2s^2}.
\]

Direct differentiation gives
\[
J_c'(s)=\frac{\cos(cs)}{s^3}.
\tag{6.2}
\]

Therefore, for \(0<A<B<\infty\),
\[
\boxed{
\int_A^B
\frac{\sin(as)\sin(bs)}{s^3}\,ds
=
\frac12
\left[
J_{a-b}(B)-J_{a-b}(A)
-J_{a+b}(B)+J_{a+b}(A)
\right].
}
\tag{6.3}
\]

Consequently every live retained phase-switch window admits an **exact
signed finite sum of explicit cosine-integral kernels**.  This is the
window-sensitive object that must be controlled next; replacing it by
the full-line endpoint loses information.

### Corollary 6.1 — a free tail bound for this bridge

For every code \(E\le C_0\),
\[
|\Phi_{E,s}(u)|\le2N.
\]
Hence for \(S>0\),
\[
\left|
\int_S^\infty
\frac{\Phi_{E,s}(h)-\Phi_{E,s}(fh)}{s^3}\,ds
\right|
\le
\frac{2N}{S^2}.
\tag{6.4}
\]
For the retained difference of two codes,
\[
\boxed{
\left|
\int_S^\infty
\frac{\Psi_s(h)-\Psi_s(fh)}{s^3}\,ds
\right|
\le
\frac{4N}{S^2}.
}
\tag{6.5}
\]
At the inherited canonical endpoint
\[
S_f=2\sqrt{N/J(f)},
\]
the right side is exactly
\[
\boxed{J(f).}
\tag{6.6}
\]

This is only a tail bound for the **phase-switch bridge**.  It is not
being booked against the historical R16 or terminal-band ledgers, and
it is not asserted to pay the original live compiler quantity without
the still-missing bridge.

---

## 7. REFUTED route 1 — absolute-value before quadratic cancellation

A tempting move is to replace the signed code average in (1.5) by
its termwise absolute value and then integrate.  This is structurally
invalid for the integrated route.

If \(ab\ne0\),
\[
\frac{|\sin(as)\sin(bs)|}{s^3}
=
\frac{|ab|}{s}+O(s)
\qquad(s\downarrow0).
\]
Therefore
\[
\boxed{
\int_0^1
\frac{|\sin(as)\sin(bs)|}{s^3}\,ds
=\infty.
}
\tag{7.1}
\]

The finite quantity in Theorem 3.1 exists **because**
\(\sum_r A_r^+A_r^-=0\) is used before integration.  Thus any proof
that absolutizes the dual-code summands before this cancellation
destroys the mechanism completely, not merely by a bad constant.

The numerical checker illustrates the logarithmic divergence for
\(a=.7,b=.2\):
the truncated absolute integral from `eps` to `1` is approximately

- `0.6386297868` at `eps=1e-2`,
- `1.2833529945` at `eps=1e-4`,
- `1.9280768205` at `eps=1e-6`.

---

## 8. REFUTED route 2 — full endpoint control alone cannot control a finite corridor

Even an exact or tiny full-line integral does not bound a chosen
finite Borel window without additional structure.

A synthetic signed packet (not asserted to be an admissible FEI code
packet) was chosen with
\[
(a_1,b_1)=(.70,.20),\quad
(a_2,b_2)=(.43,.17),\quad
(a_3,b_3)=(.58,-.13),
\]
and coefficients
\[
\alpha_1=1,\qquad
\alpha_2\approx1.31698432376600791,\qquad
\alpha_3\approx3.13357498762990953.
\]
They were solved to satisfy simultaneously
\[
\sum_j\alpha_ja_jb_j=0
\tag{8.1}
\]
and
\[
\int_0^\infty
\frac{\sum_j\alpha_j\sin(a_js)\sin(b_js)}{s^3}\,ds=0.
\tag{8.2}
\]
Nevertheless
\[
\boxed{
\int_{40}^{150}
\frac{\sum_j\alpha_j\sin(a_js)\sin(b_js)}{s^3}\,ds
\approx
-5.65004706956442323\times10^{-5}\ne0.
}
\tag{8.3}
\]

This does not refute any FEI statement.  It refutes only the shortcut
“control the full integrated endpoint, therefore every live subwindow
is controlled.”  A successful proof must use the actual code/physical
geometry in the finite-window kernel (6.3), or a separate monotonicity
that synthetic packets do not possess.

---

## 9. Falsification checks actually run

`check_b16_integrated_phase_switch.py` was executed before delivery.

It verified:

1. the cosine-integral primitive (6.3) on three signed frequency
   pairs, with maximum numerical discrepancy below `2.1e-54`;
2. a three-term signed packet with quadratic moment below `3.4e-52`;
3. its closed full-line kernel value
   `-0.0202806865378956031`, against direct integration to cutoff
   `2000`, differing by about `4.05e-11`;
4. a genuine nested-code example at `n=2` with
   `P0=RM(1,2)` and `P1=F_2^4`, for which the entropy bridge is exactly
   `-ln 2` to 50-digit precision;
5. the endpoint-zero/window-nonzero packet in Section 8.

These are self-checks/falsification checks, not an independent audit
and not a finite certificate for unrestricted FEI.

---

## 10. What is proved, conditional, open, and refuted

### PROVED

- `P03-B16-SIGNED-LOG-KERNEL`, Theorem 2.2.
- `P03-B16-INTEGRATED-PHASE-ENTROPY`, Theorem 3.1.
- `P03-B16-DUAL-COSET-ENTROPY`, Theorem 4.1.
- `P03-B16-RETAINED-INTEGRATED-ENTROPY-BRIDGE`, Corollary 5.1.
- Exact finite-window cosine-integral kernel (6.3).
- Tail bound (6.5), giving `<=J(f)` at the canonical `S_f` for this
  retained phase-switch bridge.

### CONDITIONAL

If the exact finite-window signed kernel generated by the authentic
same-syndrome/double-resolvent compiler can be dominated by the
already-proved physical ordered-flag square bank with an absolute
constant, then the current signed expenditure closes dimension-free.
No such domination is claimed here.

### REFUTED AS ROUTES

- Termwise absolute integration before distance-four quadratic
  cancellation: it diverges at zero.
- Using the full-line endpoint identity alone to control an arbitrary
  finite Borel window: a synthetic exact counterpacket shows this
  implication is false without additional structure.

### OPEN

Full unrestricted uniform-cube FEI.  In particular, this report does
not prove that the authentic live corridor is bounded by `O(J)`, and
does not convert the endpoint identity into a monotone positive
compiler payment.

---

## 11. Next attack

The next B16 attack should **polarize the finite-window kernel rather
than return to pointwise envelopes**.

The global current bound from the fresh phase-switch theorem is
\[
\mathcal E_{\rm cur}(s)
\le
\frac19\,
\mathbb E_S
[\Psi_s(g_S)-\Psi_s(fg_S)]^2.
\tag{11.1}
\]
Expand the square before integrating the authentic current/Borel
weight.  Products of cosine differences reduce to cosines of
pairwise sums and differences, so the same regularized logarithmic /
finite-`Ci` kernel acts on a **two-copy dual-code coupling**.

The concrete target is:

> derive the exact two-copy kernel for (11.1), keep the nested
> `C0-D_d` signs and the common twist `g_S`, and identify its
> off-diagonal part with a positive original-coordinate
> q-flip/ordered-flag discrepancy already paid by the B18 physical
> square bank.

This route has the correct structural requirements:

- signed R32 cancellation is used before squaring/integration;
- distance-four cancellation removes the divergent quadratic mode;
- dual-code multiplicity stays exact;
- the terminal code is subtracted inside the same kernel;
- R16 refunds and negative entropy credits are not re-used;
- the target is window-sensitive, so it avoids the endpoint-only
  obstruction in Section 8.

If this two-copy polarization fails to produce a positive physical
kernel, preserve the exact counterexample and move to a genuinely
different route rather than taking absolute relation sums.

**Full unrestricted FEI remains OPEN / NOT PROVED.**
