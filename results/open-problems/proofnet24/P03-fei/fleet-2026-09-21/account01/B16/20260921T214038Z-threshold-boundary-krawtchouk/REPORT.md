# B16 FEI signed transport — exact threshold-boundary Krawtchouk reduction and a pointwise-credit obstruction

**Date:** 21 September 2026  
**Scope:** account01 / B16, signed transport / noise interpolation, APPROACH 10/13  
**Execution:** WITHOUT_VERIFIED_BRAIN  
**Full unrestricted FEI:** **OPEN / NOT PROVED**  
**Claim level:** exact source-side identities and a rigorous obstruction to a pointwise shell-sign payment. No novelty or publication-priority claim.

## 0. Why this run changes the preceding target

The newest all-account handoff `20260921T204926Z-sharp-kernel-and-current-obstruction.md`, scientific package `dfb0dffbe472f19a15e3c3b22bc563d527a979ab`, proves that the previously proposed all-Boolean Brownian closing estimate and even the actual positive finite half-band current estimate are false at universal `O(J)` scale. Its centered Boolean counterfamily has `J=8(D-1)/2^D` and `H<4I` while the live positive current is asymptotic to `4/[27(D-1)^3]`. Thus this is not a counterexample to FEI: it is a counterexample to throwing away the compensating signed R16/entropy/terminal credits.

This run therefore does **not** try again to prove

`N^2 E Q_M <= C J`

or a positive-current analogue. Instead it asks what the authentic Brownian threshold source looks like **before** one tries to spend the fixed-sign R32/R16 shell credits.

The other-account results substantively consumed are:

1. account02/B16 `20260921T184541Z-actual-current-parent-mask-incidence/REPORT.md`: the genuine post-cancellation current weights `e_R`, central weights `epsilon_R`, and exact nonreusing parent disintegration;
2. account04/B16 `20260921T184003Z-phase-switch-dirichlet/REPORT.md`: exact same-syndrome phase-switch reduction, distance-four cancellation, and the fact that fixed-time current is paid while the large Borel corridor remains open;
3. the account02 interactive half-band obstruction above, which forces the present method change.

I also use the preceding account01/B16 retained-shell feature theorem: for the threshold feature, the authentic terminal projector and Boolean phase switch leave the exact same-syndrome amplitude

\[
F_R(u)=\sum_{\substack{A\in C_0\setminus E,\ f_A=-1,\\R_A=R}}
\lambda^{\rm th}_{|A|}(u),
\]

with

\[
\mathbb E_S Q_{\mathsf M}(g_S)=4\sum_R\int_0^1F_R(u)^2\,du.
\tag{0.1}
\]

The purpose of this report is to compute the radial coefficient `lambda_k^th` exactly enough to see the signed structure that a compensating ledger must match.

---

## 1. Radial threshold notation

Let the truth-table cube have `N` coordinates (`N=2^n` in the FEI compiler). For a truth-table word `q in F_2^N`, put

\[
m(q)=\frac1N\sum_{x=1}^N(-1)^{q_x}.
\]

For `u in (0,1]`, define

\[
\theta_u(q)={\bf1}_{\{m(q)^2\ge u\}}.
\]

If `A subseteq [N]` has size `k`, radial symmetry makes

\[
\lambda_k^{\rm th}(u)=\widehat\theta_u(A)
\]

depend only on `k`.

Use the Krawtchouk convention

\[
K_k^{(N)}(j)
:=\sum_{\ell=0}^k(-1)^\ell
\binom{k}{\ell}\binom{N-k}{j-\ell}.
\tag{1.1}
\]

This is exactly the sum of the Walsh character `chi_A` over truth-table words of Hamming weight `j`.

For

\[
x_a:=\left(1-\frac{2a}{N}\right)^2,
\qquad 0\le a\le N/2,
\tag{1.2}
\]
then for almost every `u in (x_{a+1},x_a)` the threshold accepts exactly the two Hamming tails `j<=a` and `j>=N-a`.

---

## 2. PROVED — cumulative Krawtchouk collapse to one boundary value

### Lemma 2.1 — `P03-B16-KRAWTCHOUK-TAIL-BOUNDARY`

For every `N>=2`, `1<=k<=N`, and `0<=a<=N-1`,

\[
\boxed{
\sum_{j=0}^aK_k^{(N)}(j)=K_{k-1}^{(N-1)}(a).
}
\tag{2.1}
\]

### Proof

The generating function in the Hamming-weight index is

\[
\sum_{j=0}^N K_k^{(N)}(j)z^j
=(1-z)^k(1+z)^{N-k}.
\]

Taking cumulative sums divides the generating function by `1-z`:

\[
\sum_{a\ge0}\left(\sum_{j=0}^aK_k^{(N)}(j)\right)z^a
=(1-z)^{k-1}(1+z)^{N-k}.
\]

The coefficient of `z^a` on the right is precisely `K_{k-1}^{(N-1)}(a)`. QED.

The reflection identity

\[
K_k^{(N)}(N-j)=(-1)^kK_k^{(N)}(j)
\tag{2.2}
\]
then gives the exact threshold coefficient.

### Corollary 2.2 — exact threshold coefficient

For almost every `u in (x_{a+1},x_a)`,

\[
\boxed{
\lambda_k^{\rm th}(u)=0\quad(k\text{ odd}),
}
\tag{2.3}
\]
while for even `k>=2`,

\[
\boxed{
\lambda_k^{\rm th}(u)
=2^{1-N}K_{k-1}^{(N-1)}(a).
}
\tag{2.4}
\]

Thus the continuous Brownian threshold feature is actually a **boundary Krawtchouk polynomial of odd degree** on each threshold plateau. The terminal relation code already removes `k=0,2`, so in the retained shell the first relevant case is `k=4`, hence boundary degree three.

---

## 3. PROVED — exact discrete boundary energy for every signed radial combination

Let arbitrary real coefficients `c_{2r}` be given and put

\[
F(u)=\sum_r c_{2r}\lambda_{2r}^{\rm th}(u),
\qquad
P(a)=\sum_r c_{2r}K_{2r-1}^{(N-1)}(a).
\tag{3.1}
\]

The plateau width is

\[
x_a-x_{a+1}
=\frac{4(N-2a-1)}{N^2}.
\tag{3.2}
\]

Therefore Corollary 2.2 gives immediately

\[
\boxed{
\int_0^1F(u)^2du
=
\frac{2^{4-2N}}{N^2}
\sum_{a=0}^{N/2-1}(N-2a-1)P(a)^2.
}
\tag{3.3}
\]

Since every index `2r-1` is odd,

\[
P(N-1-a)=-P(a).
\]

Folding the two halves yields the equivalent symmetric form

\[
\boxed{
\int_0^1F(u)^2du
=
\frac{2^{3-2N}}{N^2}
\sum_{a=0}^{N-1}|N-1-2a|P(a)^2.
}
\tag{3.4}
\]

This is an exact identity, not an estimate.

### Authentic same-syndrome specialization

For an active syndrome `R`, define the retained frustrated relation counts

\[
c_{R,2r}
=\#\{A\in C_0\setminus E:\ f_A=-1,\ R_A=R,\ |A|=2r\},
\tag{3.5}
\]

and

\[
P_R(a)=\sum_{r\ge2}c_{R,2r}K_{2r-1}^{(N-1)}(a).
\tag{3.6}
\]

(The lower limit `r>=2` is the distance-four retained-shell fact.) Combining (0.1) and (3.4) gives the source-exact Brownian identity

\[
\boxed{
\mathbb E_S Q_{\mathsf M}(g_S)
=
\frac{2^{5-2N}}{N^2}
\sum_R\sum_{a=0}^{N-1}
|N-1-2a|P_R(a)^2.
}
\tag{3.7}
\]

No relation is positive-parted and no same-syndrome square is diagonalized relation-by-relation. Cancellation between different relation weights survives inside `P_R(a)`.

### Authentic current-weighted specialization

From account02/B16 and the newest current handoff, let

\[
e_R=2\left(\frac1{q_Rk_R}-\frac1{q_R^2}\right)
\]

on odd active syndromes, and let `W_cur` have Walsh multiplier `e_R/4`. Because the syndrome Fourier coefficient of the threshold phase switch is `-2F_R(u)`, the exact Brownian current source is

\[
\Gamma_{\rm cur}
=N^2\int_0^1\langle A(u),W_{\rm cur}A(u)\rangle du
=N^2\sum_R e_R\int_0^1F_R(u)^2du.
\]

Hence

\[
\boxed{
\Gamma_{\rm cur}
=
2^{3-2N}
\sum_R e_R
\sum_{a=0}^{N-1}|N-1-2a|P_R(a)^2.
}
\tag{3.8}
\]

The same formula holds for the central source with `e_R` replaced by the exact central multiplier `epsilon_R`. This is the current source in a finite discrete form that still retains all same-syndrome and cross-weight cancellation.

Equation (3.8) is **not** asserted to be `O(J)`: the new half-band obstruction proves that such a universal positive closing budget is false. Its use is that any legitimate R16/entropy compensation can now be asked to act on one explicit weighted boundary polynomial rather than on an arbitrary threshold MMD.

---

## 4. RIGOROUS OBSTRUCTION — fixed R32 shell parity cannot pay the Brownian threshold pointwise

A tempting next move would be to identify the sign of `lambda_{2r}^{th}(u)` with the fixed R32 shell sign `(-1)^r` and spend the `0 mod 4 / 2 mod 4` credits separately at each threshold `u`. Corollary 2.2 kills this strategy exactly.

Take `N=8`, `k=4`. Then

\[
K_3^{(7)}(0)=1,
\qquad
K_3^{(7)}(2)=-3.
\]

Thus

\[
\lambda_4^{\rm th}(u)=\frac1{128}>0
\quad\text{for }u\in(9/16,1),
\tag{4.1}
\]

where the accepted tail radius is `a=0`, but

\[
\lambda_4^{\rm th}(u)=-\frac3{128}<0
\quad\text{for }u\in(1/16,1/4),
\tag{4.2}
\]

where the accepted tail radius is `a=2`.

The relation degree has not changed: it is four in both intervals. Therefore there is **no fixed sign `sigma_4`** — in particular not the R32 sign `(-1)^{4/2}=+1` — for which

\[
\lambda_4^{\rm th}(u)=\sigma_4 w(u),\qquad w(u)\ge0,
\]

holds for all thresholds. The same phenomenon occurs at higher even degrees through the zeros of the odd boundary Krawtchouk polynomial.

### Consequence

The R16/R32 signed ledger cannot be coupled to the Brownian threshold bank by a pointwise-in-`u`, degree-parity payment. That proposed bridge is rigorously dead even before one reaches the large-dimensional counterfamily.

The correct object is the **integrated boundary quadratic form (3.7)/(3.8)**. Any successful compensation must preserve cross-threshold or cross-degree cancellation — for example through a discrete Krawtchouk/Christoffel–Darboux identity, a signed summation-by-parts formula, or by returning to the finite-band sine transform before spending the R16 credits.

---

## 5. Relation to the newest half-band obstruction

The new account02 obstruction says that the positive current itself can be polynomially larger than `J` on a family whose FEI ratio is harmless (`H<4I`). Equations (3.7)-(3.8) explain where a positive-only proof necessarily loses information: after the exact terminal projector, all remaining Brownian source energy is a square of boundary polynomials. It is positive. FEI can only survive this family through the compensating signed terms that the positive-current target discarded.

The present result does not yet identify the exact cancellation against `B_d` in

\[
H_{\rm nat}(f)=\kappa_2J(f)-\mathcal B_{d_h}+\mathcal Q_{d_h,<2}+R_{d_h}(f).
\]

It does, however, reduce the source that must be paired with that signed bank to the explicit sequence `P_R(a)` and proves that a simpler pointwise parity match cannot work.

---

## 6. Verification

The accompanying exact-rational checker does **not** rerun the settled read-once certificate. It verifies:

- 11,966 integer cumulative-Krawtchouk identities (2.1) for `2<=N<=32`;
- 2,992 exact two-tail threshold identities (2.3)-(2.4) over even ambient dimensions in that range;
- four independent exact rational instances of the boundary energy identity (3.4), including mixed signed coefficient vectors;
- the explicit `N=8,k=4` sign reversal `1/128 -> -3/128`.

All checks pass.

---

## 7. Next nonoverlapping B16 target

Do **not** retry a universal positive Brownian/current `O(J)` estimate and do not try another pointwise fixed-shell-sign comparison.

The next B16 step should insert the exact historical R16 high-resolvent/moment bank into (3.8) and derive a **discrete summation-by-parts / Christoffel–Darboux compensation identity** for the weighted boundary polynomial

\[
\sum_a |N-1-2a|P_R(a)^2.
\]

The first falsification test is the newest two-point-defect half-band counterfamily: the combined signed expression must collapse there to `O(J)` even though (3.8) alone is much larger. If the exact R16 coefficients cannot cancel the low boundary modes of `P_R`, this particular Brownian/Krawtchouk compiler route is dead and B16 should change mechanisms rather than repeat it.

**Full FEI remains OPEN / NOT PROVED.**
