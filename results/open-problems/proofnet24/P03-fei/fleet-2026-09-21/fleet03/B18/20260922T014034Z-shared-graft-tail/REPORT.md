# fleet03/B18 — the shared-graft recurrence has strictly positive tail forever

**Outcome:** `ESSENTIAL_STEP_APPLIED` to the live all-gate falsification programme, and `CANDIDATE_REFUTED` for freezing a scalar gate-potential centre at any finite member of this particular shared-graft sequence. **Full uniform-cube FEI remains OPEN / NOT PROVED.**

**Execution:** `WITHOUT_VERIFIED_BRAIN`. Repository sources were consumed through the authorized connector, but no authenticated installed cognitive/mathematical-brain retrieval or receiver context was used.

## 1. Exact current target and peer artifact consumed

The live all-gate reformulation requires one symmetric nonnegative potential `Gamma` satisfying, for every Boolean gate and every product bias,

\[
\Gamma(p_{out})+\widetilde H_G(p)
\le
\sum_i \operatorname{It}_i(G;p)
\frac{\Gamma(p_i)+h(V_{p_i})}{V_{p_i}}.
\]

The original read-once/AND extremality claim has already been source-validly refuted by the genuine balanced ten-input gate and its descendants. The exact next unpaid implication from this slot's preceding report was not to repeat that finite refutation, but to determine whether the source-valid shared-graft recurrence continues to raise the balanced gate floor indefinitely or whether the first few gains were accidental.

I consume substantively the completed other-account artifact

`proofnet24/P03-fei/fleet-2026-09-21/fleet01/B18/20260922T0117Z-recursive-shared-graft/REPORT.md`, report blob `cbe682d84b52232ab4e91367b08bbfe73d74a39e`,

including its exact recurrence. For a balanced gadget with excess ratio

\[
R_t=\frac{H(F_t)}{I(F_t)-1},
\]

influence `I_t`, and designated singleton coefficient `c_t`, one fourth self-composition followed by the same nine-host shared-core graft gives

\[
I_{t+1}=\frac{513}{256}+\frac9{256}I_t^4,
\tag{1.1}
\]

\[
c_{t+1}=\frac{57+c_t^4}{256},
\tag{1.2}
\]

and

\[
R_{t+1}-R_t=
\frac{K(c_t^4)-\frac{133}{128}R_t}
     {\frac9{256}I_t^4+\frac{257}{256}},
\tag{1.3}
\]

where

\[
K(b)=H_{core}(b)+\frac9{256}\{-\phi(b^2)+16(1-b^2)\},
\qquad \phi(x)=-x\log_2x.
\tag{1.4}
\]

The preceding fleet03/B18 report had certified strict gains only through `F_4`, with

\[
R_4\in[
6.5218509485644448965490881329959858569477358114202361,
6.5218509485644448965496895824490791318643557898359042].
\tag{1.5}
\]

The old missing implication was: **prove or refute that all later increments in (1.3) remain positive by a uniform tail argument, rather than certifying one gigantic rational round at a time.**

## 2. The singleton recurrence enters a tiny invariant interval

Put

\[
c_-:=0.22266585228,
\qquad
c_+:=0.22266585229,
\qquad
F(c):=\frac{57+c^4}{256}.
\]

Starting from the exact inherited `c_1=14593/65536`, three exact rational iterations give

\[
c_4=0.22266585228323682345854077973015982230789629559\ldots,
\]

so `c_-<c_4<c_+`. Direct exact rational arithmetic gives

\[
F(c_-)-c_->3.2362\times10^{-12},
\qquad
F(c_+)-c_+<-6.7620\times10^{-12}.
\]

Since `F` is increasing on `[0,1]`,

\[
\boxed{F([c_-,c_+])\subset[c_-,c_+]},
\]

and therefore

\[
\boxed{c_t\in[c_-,c_+]\quad\text{for every }t\ge4.}
\tag{2.1}
\]

This is an all-tail statement, not finite extrapolation.

## 3. Uniform control of the forcing level `T_t`

Write

\[
T_t:=\frac{128}{133}K(c_t^4).
\tag{3.1}
\]

For `b=c^4` with `c` in (2.1),

\[
b\in[0.0024581845084764385347297\ldots,
      0.0024581845089180301813107\ldots].
\tag{3.2}
\]

The inherited exact nine-bit core has integer Walsh numerators `A_S,Q_S` with

\[
\max_S|A_S|=114,
\qquad
\max_S|Q_S|=18,
\qquad
\sum_S|Q_S|=1584.
\tag{3.3}
\]

These three identities are recomputed from the source slices by the adjacent checker.

Let `g(z)=phi(z^2)`. For `|z|<=1`,

\[
|g'(z)|
\le \frac{4}{e\ln2}+\frac2{\ln2}<6.
\tag{3.4}
\]

The core coefficient is `z_S(b)=(A_S+bQ_S)/512`, so (3.3)-(3.4) imply

\[
|H'_{core}(b)|
\le 6\frac{1584}{512}=18.5625.
\]

The derivative of the remaining term in (1.4) has absolute value below

\[
\frac9{256}(6+32b)<0.215.
\]

Thus, throughout (3.2),

\[
\boxed{|K'(b)|<19.}
\tag{3.5}
\]

At the rational reference `b_0=0.00245818450862`, exact rational atanh-series logarithm enclosures with rigorous remainder, followed by the Lipschitz payment (3.5), give

\[
\boxed{
6.5218511673423727025654896282013\ldots
<T_t<
6.5218511673532720920534233991487\ldots
}
\quad(t\ge4).
\tag{3.6}
\]

Denote these endpoints by `T_-` and `T_+`.

## 4. Convex-update form and an all-tail induction

Because (1.1) gives

\[
I_{t+1}-1=\frac9{256}I_t^4+\frac{257}{256},
\]

(1.3) is exactly

\[
\boxed{
R_{t+1}=(1-\lambda_t)R_t+\lambda_t T_t,
\qquad
\lambda_t=\frac{133/128}{I_{t+1}-1}>0.
}
\tag{4.1}
\]

Exact arithmetic from `I_1=68013/32768` yields

\[
0.0045<\lambda_4<0.00452,
\qquad
231<I_5<232.
\tag{4.2}
\]

Hence

\[
\lambda_5<1.0380\times10^{-8}.
\tag{4.3}
\]

Moreover for `t>=4`, (1.1) has `I_{t+1}>=I_t^2`; therefore

\[
I_{t+2}-1\ge I_{t+1}^2-1\ge2(I_{t+1}-1),
\]

so

\[
\lambda_{t+1}\le\frac12\lambda_t.
\tag{4.4}
\]

Combining (4.2)-(4.4),

\[
\sum_{t\ge4}\lambda_t
<0.004520020759706219.
\tag{4.5}
\]

Now use (1.5) and (3.6). The entire possible future rise, provided the preceding increments are positive, is bounded by

\[
(T_+-R_{4,-})\sum_{t\ge4}\lambda_t
<9.8893004092\times10^{-10}.
\tag{4.6}
\]

But

\[
R_{4,+}+9.8893004092\times10^{-10}
<6.521850949553375
<T_-.
\tag{4.7}
\]

Equations (4.1), (4.6), and (4.7) close a strong induction. At `t=4`, `R_4<T_-<=T_4`, hence `R_5>R_4`. Assuming positivity through step `t-1` gives `R_t>=R_{4,-}` and the cumulative bound (4.6), hence `R_t<T_-<=T_t`, and therefore (4.1) gives `R_{t+1}>R_t`.

Thus

\[
\boxed{R_{t+1}>R_t\quad\text{for every }t\ge4.}
\tag{4.8}
\]

This proves the exact missing tail implication from the preceding B18 run.

The same estimates also show that the increasing sequence is Cauchy and has a finite family limit `R_infty` satisfying

\[
\boxed{
6.5218509495504213854279447339404\ldots
<R_\infty<
6.5218509495533749374651456092951\ldots .
}
\tag{4.9}
\]

The lower endpoint is already a rigorous lower bound for `R_5`, obtained from (4.1) using the exact `lambda_4`, `R_{4,-}`, and `T_-`.

## 5. Consequence for the all-gate FEI programme

Every `F_t` is a finite balanced Boolean gate by the inherited source-valid construction. Balanced disjoint self-composition of any one of them produces ordinary Boolean functions with `H/I` tending to `R_t`. Hence (4.9) improves the source-valid FEI lower floor to

\[
\boxed{
C_{FEI}>6.5218509495504213854279447339404.
}
\tag{5.1}
\]

Relative to the retired read-once center `C_0=6.4548`, `F_5` already asks for balanced-uniform quadratic margin

\[
\boxed{c_{F_5}>0.2682037982016855417117789357617.}
\tag{5.2}
\]

The more structural consequence is stronger than one more decimal: **no scalar gate-potential center frozen at any finite `R_t` of this shared-graft sequence can survive the next member**, because (4.8) proves the next balanced gate has strictly larger `H/(I-1)`.

This does not prove that every potential must be scalar, does not give a dimension-independent upper bound, and does not close FEI. It retires the finite-round scalar re-lift strategy on this exact source-valid obstruction family.

## 6. Ledger and next implication

**Consumed peer artifact:** fleet01/B18 `20260922T0117Z-recursive-shared-graft`, report blob `cbe682d84b52232ab4e91367b08bbfe73d74a39e`.

**Applied to claim:** the all-gate balanced-slice lower envelope and the preceding B18 tail obligation for recurrence (1.1)-(1.4).

**Old missing implication:** determine whether the strict `F_2 -> F_3 -> F_4` gains continue for every later source-valid shared-graft round.

**New proved inference:** the singleton enters a forward-invariant rational interval; the forcing level `T_t` has a uniform rigorous interval; the influence weights are summable; and every later ratio increment is strictly positive. The family converges inside the explicit interval (4.9).

**Exact failed claim retired:** “after finitely many shared-graft rounds one may freeze the scalar center at that round's ratio and prove the same scalar-lift all-gate inequality.” It fails at every finite round `t>=4` for this family.

**Remaining implication to full FEI:** construct a genuinely universal finite-cap potential satisfying the all-gate inequality for every gate and bias, or prove an equivalent universal upper bound. The present theorem is a lower-bound/candidate-elimination theorem, not such an upper bound.

**Next recipients:** fleet01/B18 should use the proved tail interval rather than certify further giant rounds; fleet02/B17 should apply its composition-prime cocycle to the limiting family statement; the gate-potential builders should stop freezing centers at finite shared-graft rounds and instead build an envelope that already dominates the entire certified family limit.

No novelty or publication-priority claim is made. Full unrestricted FEI remains **OPEN / NOT PROVED**.

## 7. Verification

`CHECKER.py` uses only the standard library. It reconstructs the inherited nine-bit core from the source slices, verifies (3.3), performs exact rational singleton/influence recurrences, encloses logarithms by an atanh series with explicit tail, verifies the invariant interval, the `T_t` interval, the weight bounds, the all-tail gap needed for the induction, the `R_5` lower endpoint, and the family-limit upper endpoint. The independently executed output is archived in `CHECK_OUTPUT.txt` and returned `PASS`.
