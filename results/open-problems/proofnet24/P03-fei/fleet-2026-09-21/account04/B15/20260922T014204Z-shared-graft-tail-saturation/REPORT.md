# B15 — infinite-tail saturation of the fixed depth-four shared-core FEI obstruction

**Run:** `20260922T014204Z-b15-gate-extremality-r33`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Outcome:** **ESSENTIAL_STEP_APPLIED / INFINITE-FAMILY TAIL CLOSED**.  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED**.

## 0. Live owner target and retained arithmetic input

The latest owner control (`2026-09-22.2`) supersedes this slot's older interface-D-only wording and directs all FEI workers to the common all-gate inequality

\[
\Gamma(p_{\rm out})+\widetilde H_G(p)
\le
\sum_i \operatorname{It}_i(G;p)
\frac{\Gamma(p_i)+h(V_{p_i})}{V_{p_i}},
\qquad V_u=4u(1-u).
\tag{G}
\]

The old read-once-potential / AND-extremality candidate has already been source-validly refuted by balanced gates, so this run does not repeat that falsification. It attacks the newest replacement obligation: analyze the iterated shared-coordinate obstruction as an **infinite family** before freezing another center cap.

Before following the newer owner target, I consumed the newest account02/B15 arithmetic handoff

`account02/B15/20260922T000114Z-harmonic-delete-kl-valuation/REPORT.md`.

Its exact unpaid deletion remainder is

\[
\boxed{
D_{\rm del}
=\beta H_2(\rho)-\mathbb E\log_2(K!)-\mathcal K_\rho,
\qquad \mathcal K_\rho\ge0,
}
\tag{0.1}
\]

with the one-time signed valuation reserve `R(f)<=2J(f)<=2I(f)`. The same report proves that recharging an unbounded valuation price at every deletion step is false on genuine Boolean addressing functions. Those factorial and KL credits remain retained exactly; nothing below assumes packet integrality or replaces a negative credit by a positive interpolation. The later owner control simply makes (G), rather than (0.1), the current shared implication.

## 1. Exact predecessor consumed

The direct peer input is

`account03/B15/20260922T012556Z-iterated-shared-graft/REPORT.md`, report blob
`aff93b999538a8b8baeab270ff739f405c79ee7c`.

That report consumes account01/B18's source-valid shared-core transformation and rigorously constructs actual finite balanced monotone Boolean gates `F3,...,F6`. It certifies

\[
\begin{aligned}
R_6^-&=6.521850949550448184840160538860511501288648868305895469222543106356953492372764166124613916792207343,\\
R_6^+&=6.521850949550448184840160538860511501288648871643878248179449753729219561943695052658106144512794690,
\end{aligned}
\tag{1.1}
\]

for

\[
R_r:=\frac{H(F_r)}{I(F_r)-1}.
\]

It also proves the exact recurrence. Put

\[
\alpha=\frac9{256},\qquad B=\frac{257}{256},\qquad d_0=\frac{133}{128},
\]

and let `c_r` be the designated singleton coefficient. Then

\[
I_{r+1}=\frac{261}{128}+\alpha(I_r^4-1)
=\frac{513}{256}+\alpha I_r^4,
\tag{1.2}
\]

\[
c_{r+1}=\frac{57}{256}+\frac{c_r^4}{256},
\tag{1.3}
\]

and

\[
\boxed{
R_{r+1}-R_r
=\frac{K(c_r^4)-d_0R_r}{D_r},
\qquad
D_r:=\alpha I_r^4+B=I_{r+1}-1,
}
\tag{1.4}
\]

where

\[
K(b)=H_{\rm core}(b)+\alpha[-\phi(b^2)+16(1-b^2)],
\qquad \phi(t)=-t\log_2t.
\tag{1.5}
\]

Every `F_r` is an actual finite balanced monotone Boolean function. This is the fixed **depth-four self-composition + nine-host shared-core graft** family; it is not ordinary disjoint composition and not a spectral relaxation.

## 2. New theorem — the entire remaining tail is at most 5.213e-30

### Lemma 2.1 — universal bound on the shared-core numerator

For every source-valid value of `b`,

\[
\boxed{K(b)\le\frac{153}{16}.}
\tag{2.1}
\]

**Proof.** `H_core(b)` is the entropy contribution of the 512 empty-fresh-coordinate Fourier masses in the physical shared-core construction. Their total mass is at most one by Parseval. For any 512 nonnegative masses `x_j` with total `t<=1`, concavity gives

\[
\sum_j -x_j\log_2x_j
\le t\log_2\frac{512}{t}\le9.
\]

Also `-phi(b^2)<=0` and `16(1-b^2)<=16`. Since `alpha=9/256`, (2.1) follows from

\[
K(b)\le9+16\frac9{256}=9+\frac9{16}=\frac{153}{16}.
\]
\(\square\)

### Lemma 2.2 — increment denominators grow at least geometrically after `F6`

The exact influence recurrence gives, by direct rational evaluation,

\[
I_6>10^8>\frac{16}{3}.
\tag{2.2}
\]

For every `I>=16/3`,

\[
\frac9{256}I^4\ge I^2,
\]

so (1.2) yields `I_next>=I^2`. Consequently, for every `r>=6`,

\[
\begin{aligned}
D_{r+1}
&=I_{r+2}-1\\
&\ge I_{r+1}^2-1\\
&=(I_{r+1}+1)(I_{r+1}-1)\\
&=(I_{r+1}+1)D_r
\ge2D_r.
\end{aligned}
\tag{2.3}
\]

Thus `D_{6+j}>=2^jD_6`.

### Theorem 2.3 — fixed-family supremum saturation

For every `m>=6`,

\[
\boxed{
R_m
\le
R_6^+ + \frac{153}{8D_6}.
}
\tag{2.4}
\]

**Proof.** If the numerator in (1.4) is negative, that step cannot increase `R`. If it is positive, `R_r>=0` and Lemma 2.1 give

\[
(R_{r+1}-R_r)_+
\le\frac{K(c_r^4)}{D_r}
\le\frac{153}{16D_r}.
\]

Summing positive increments only and using (2.3),

\[
R_m-R_6
\le
\frac{153}{16D_6}\sum_{j\ge0}2^{-j}
=\frac{153}{8D_6}.
\]
\(\square\)

The exact rational checker computes

\[
D_6
=3.6689705968441394100100955366294446\ldots\times10^{30}
\]

and hence

\[
\boxed{
\frac{153}{8D_6}
<5.212633760665824211111460651293\times10^{-30}.
}
\tag{2.5}
\]

Because `F6` itself belongs to the family and all certified earlier steps increased the ratio, the supremum of the **entire fixed depth-four shared-graft family** is rigorously trapped by

\[
\boxed{
6.5218509495504481848401605388605115012886488683\ldots
\le
\sup_{r\ge1}R_r
<
6.5218509495504481848401605388657241350493146959\ldots .
}
\tag{2.6}
\]

So every as-yet-uncomputed round of this exact family, all together, can improve the center cap by **less than 5.213e-30** beyond the certified `F6` endpoint (apart from the already displayed width of the `F6` entropy interval, which is much smaller than the stated tail scale).

## 3. Consequence for the gate campaign

This closes the replacement obligation left by account03/B15 for this specific mechanism. The fixed depth-four shared-core iteration does **not** hide another meaningful sequence of cap increases after `F6`; it is mathematically saturated to about 29 decimal places in the only direction relevant to future counterexamples.

Relative to the old read-once reference center `C0=6.4548`, the already certified `F6` value forces the scalar quadratic-margin floor

\[
\boxed{
4(R_6^- - C_0)
>
0.2682037982017927393606421554420460051545954732\ldots .
}
\tag{3.1}
\]

Theorem 2.3 also says that this **particular** fixed-depth-four family can force at most another `~2.09e-29` in that scalar margin. Therefore the fleet should not spend more runs merely certifying `F7,F8,...` for this same map.

This is **not** a universal FEI upper bound. Another prime gate, another shared-coordinate gadget, or a different self-composition depth may have a larger ratio. Full FEI still requires one finite all-gate/all-bias potential or an equivalent universal argument.

The mathematically useful successor is now one of two genuinely different tasks:

1. prove the all-prime/all-bias gate inequality for a candidate whose center safely dominates the whole interval (2.6), while retaining the exact composition cocycle; or
2. search a genuinely different shared-coordinate transform (different depth/core/gadget), not another round of the now-saturated depth-four map.

## 4. Reproduction and source scope

`CHECKER.py` is standard-library only. It starts from the exact `I(F2)` supplied by the peer recurrence, iterates the rational influence map through `I6`, computes `D6` exactly, and proves the tail bound (2.5). `CHECK_OUTPUT.txt` records the resulting exact-rational/decimal values. No huge Boolean truth table is enumerated.

Fresh primary-source checks still leave unrestricted FEI open. Potapov, arXiv:2609.21563 (18 September 2026), proves FEI for plateaued functions and partially bent functions, not arbitrary Boolean functions. González--MacManus--Pereyra, arXiv:2606.00246 (29 May 2026), explicitly retain a general restriction inequality whose universal validity would imply full FEI. The Numaro July 2026 lower-bound seed remains external prior work. I make **no novelty or publication-priority claim** for the tail theorem.

## 5. Status fields

- `consumed_peer_artifact`: account03/B15 `20260922T012556Z-iterated-shared-graft/REPORT.md`, blob `aff93b999538a8b8baeab270ff739f405c79ee7c`.
- `consumed_arithmetic_artifact`: account02/B15 `20260922T000114Z-harmonic-delete-kl-valuation/REPORT.md`; exact residual (0.1) retained with its negative KL/factorial credits.
- `applied_to_claim`: successor all-gate center-cap obstruction after `F6`; infinite tail of the exact fixed depth-four shared-coordinate family.
- `new_proved_inference`: all future positive gains in this family sum to less than `5.213e-30`; family supremum enclosed by (2.6).
- `mechanism_change`: analytic infinite-tail bound, not another finite graft round.
- `remaining_implication`: full all-prime/all-bias gate inequality above the complete known obstruction family, or a materially different shared-coordinate construction.
- `full_problem_change`: OPEN -> OPEN.
- `full_brain_connected`: false.
