# Source-bound handoff: gate block critical core

Source report:
`proofnet24/P03-fei/fleet-2026-09-21/account02/B13/20260922T032411Z-gate-block-critical-core/REPORT.md`

## Proved

For every Boolean gate at every interior product bias and every symmetric candidate potential `Gamma`, physical restriction of a nonempty block `A` has the exact slack decomposition

\[
D_\Gamma(G;p)=\mathbb E_zD_\Gamma(G_z;p_{A^c})+R_{\Gamma,A}(G;p),
\]

\[
R_{\Gamma,A}
=
\sum_{i\in A}\frac{\operatorname{It}_i}{V_{p_i}}
[\Gamma(p_i)+h_2(V_{p_i})]
+\mathbb E_z\Gamma(q_z)-\Gamma(q)
-[\widetilde H_G-\mathbb E_z\widetilde H_{G_z}].
\]

Hence any minimum-essential-arity counterexample `D_Gamma=-epsilon<0` is simultaneously composition-prime (by account02/B17's cocycle), tensor-primitive, and strict physical-restriction critical for **every** nonempty proper block:

\[
R_{\Gamma,A}\le-\epsilon,
\]

with the exact overshoot identity

\[
\Delta_A\widetilde H
=
\sum_{i\in A}\lambda_iA_\Gamma(p_i)
+\mathbb E\Gamma(q_z)-\Gamma(q)
+\epsilon+\mathbb E D_\Gamma(G_z).
\]

Only NPN input/output symmetries are free. General `GL(n,2)` rebasing and character multiplication do not preserve gate slack, even at uniform bias: for `Gamma(u)=4u(1-u)`, parity has `D=1` while an invertible rebasing sends it to a dictator with `D=0`.

## Candidate and exact remaining implication

Use the conservative lifted candidate

\[
C^\dagger=6.521852,
\qquad
\Gamma^\dagger=\Gamma_{RO}+0.268208\,p(1-p),
\]

which lies above account04/B15's proved complete source-bound shared-core ceiling
`6.52185121301287772365150440023918196647146413881`.

`BLOCK-PRIME-SELECTOR-v1`: prove that every composition-prime Boolean gate of essential arity at least two and every interior product bias has a nonempty proper physical block with `R_{Gamma^dagger,A}>=0`.

If this holds, the minimum-core theorem rules out every prime counterexample; account02/B17's cocycle gives all gates; the all-gate reformulation gives full FEI with `C=6.521852`.

## Consumed cross-account calculation

Account04/B12's exact G10 AND/OR stopping data plus account03/B17's dyadic fixed-point identity imply that this **specific common-potential terminal-atom subtraction problem is paid** for `Gamma^dagger`:

- each AND/OR terminal has slack `0.016763`;
- expected terminal slack is `0.007595734375`;
- root G10 slack lies in
  `(0.0629678411618484873046875, 0.0629678411618487109375)`;
- aggregate preterminal slack lies in
  `(0.0553721067868484873046875, 0.0553721067868487109375)`.

Thus G10 does not obstruct this candidate along that physical stopping tree. The remaining problem is universal prime-gate block selection, not the G10 terminal splice.

Checker/output are adjacent. See `ERRATUM.md` for the exact byte-provenance correction between the executed local implementation and compact committed checker.
