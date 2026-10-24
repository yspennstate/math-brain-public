# B16 FEI campaign A — arbitrary-residual OR-lift adversary and exact short-circuit critical descent

**Run:** `20260922T001028Z-account04-B16-fei-A-r15`  
**Execution:** **WITHOUT_VERIFIED_BRAIN**  
**Status:** **ESSENTIAL_STEP_APPLIED / structured adversary repaired. Full uniform-cube FEI remains OPEN / NOT PROVED.**

## 0. Live assignment and exact inputs

Fresh owner control exposed the later execution reset

`scheduled_tasks/work/shared/fei-joint-proof-2026-09-21/EXECUTION_RESET_20260921T230620Z.md`
(blob `8506e4aaed072e37d9402e1cce947ff4daf1ce22`), which supersedes the older interface-C duty and assigns account04/B16 to campaign A: construct adversarial joint-derivative examples against the current coverage/exception step and then attempt a source-valid repair.

Scientific master was resolved during this run at `cf09d030492582ee706c983750769488b97d6037` before this delivery. The completed inputs used are:

1. `proofnet24/P03-fei/fleet-2026-09-21/account02/B14/20260921T230653Z-asymmetric-shortcircuit-ledger/REPORT.md` (reported blob `242a3fddee17db5ed1d723962b76c8659f623d6a`). It proves the asymmetric full-block branch and, on total proxy error at most `q/16`, a random-order first-mismatch tree with folded drift at least `15rq/16` and small residual pivotality entropy.
2. `proofnet24/P03-fei/fleet-2026-09-21/account04/B13/20260921T2325Z-asymmetric-exception-compiler/REPORT.md` (directory tree at the observed master: `387a9cd6cd08af1968f632da503e5d0c25c32e72`). It localizes the remaining low-defect obstruction to positive-defect / outside-false-positive-heavy rows and explicitly names the upper corrected-entropy cost of the same short-circuit tree as the next unpaid arrow.
3. `proofnet24/P03-fei/fleet-2026-09-21/account01/B14/20260921T224055Z-adaptive-pivotality-selector/REPORT.md` (reported blob `585cbdfc282e636c95b70bd479d4c720b19f1948`). It proves the adaptive corrected-ratio compiler and uses the exact corrected decrement `E_T` of a physical tree.
4. `proofnet24/P03-fei/fleet-2026-09-21/account01/B18/20260921T2205Z-folded-cooling-compiler/REPORT.md` (blob `9f2bb40584be20e5e440e7f3913873c34858bc91`). It fixes the character-invariant corrected functional `mathcal F=H-mathcal C` and the physical-restriction critical-core framework.
5. The preceding B16 adversary is `proofnet24/P03-fei/fleet-2026-09-21/account04/B16/20260921T231428Z-majority-terminal-critical-descent/REPORT.md`, blob `4a2b23ce2a98054d761260fc6c757a2703bb50fc`.

No benchmark gold, remote compute, or workflow dispatch was used.

## 1. Adversary: one accurate proxy can hide an arbitrary residual event

Work on independent physical coordinates

- a pivot `x in {+-1}`,
- `r>=2` proxy coordinates `Z`,
- an arbitrary block `W`.

Let `Q={Z=a}` be one coordinate atom of density

`q=2^{-r}`.

Let `R=R(W)` be **any** Boolean event of density `s`. Put

`E = Q union R`

and define the gated dictator

`F_{Q,R}(x,Z,W)=x` on `E`, and `F_{Q,R}=+1` on `E^c`.

Equivalently `F_{Q,R}=x^{1_E}`. The `x`-pivotality event is exactly `E`.

Relative to the proxy `Q`,

`E^- = 0`,

`E^+ = (1-q)s`,

and

`p_x = q+(1-q)s`.

Thus choosing

`(1-q)s <= q/16`                                                     (1.1)

places the row exactly in the fixed-relative outside-pollution regime left to the short-circuit mechanism.

For every proxy coordinate `z_k`, a `z_k`-edge can change `F_{Q,R}` only when `x=-1`, `R=0`, and that edge crosses the atom `Q`. Hence

`Inf_{z_k}(F_{Q,R}) = q(1-s)`,

so

`I_Z = r q(1-s) <= r p_x`.                                          (1.2)

The key adversarial point is that **R is arbitrary**. Its internal boundary, joint-derivative depth, Fourier geometry, and restriction complexity are unconstrained. Therefore a top-row statement of the form “a `q/16` proxy leaves a structurally simple residual” is false: the residual can encode an arbitrary Boolean event on fresh coordinates.

This does not refute the account02/B14 short-circuit theorem. It identifies exactly what a source-valid repair has to exploit: cancellation in the parent-to-child entropy ledger, not a claim that the residual event is itself simple.

## 2. The physical first-mismatch tree has only two genuine leaf types

Let `T_Q` query the `r` proxy literals in any fixed order and stop at the first mismatch with `a`.

- On the all-match branch, of total probability `q`, the leaf function is the character `x`.
- On every mismatch branch, `Q` is impossible, all unqueried proxy coordinates become irrelevant, and the leaf function is

`F_R(x,W)=x` on `R`, `+1` off `R`.

Thus all mismatch leaves reduce to the same genuine Boolean function `F_R`. Consequently

`Delta_T H = H(F_{Q,R})-(1-q)H(F_R)`,                               (2.1)

and similarly for folded influence and the corrected functional.

For every `W` coordinate, its influence in the parent is exactly `(1-q)` times its influence in `F_R`; these terms cancel in the folded drift. Since `r>=2` and (1.1), all displayed pivot/proxy influences are at most `1/2`. Therefore

`boxed{ D_T = J(F_{Q,R})-(1-q)J(F_R) = q[1+r(1-s)]. }`              (2.2)

In particular the drift is on the exact `rq` scale without making any assumption on the complexity of `R`.

## 3. Exact Fourier cancellation: the arbitrary residual spectrum disappears

Let `u=1_R` and write its Walsh coefficients as `b_B`, with

`b_empty=s`,

`sum_{B nonempty} b_B^2 = s(1-s)`.

The indicator `e=1_{Q union R}=u+(1-u)1_Q` has Fourier coefficients, up to harmless atom signs,

- `ehat(empty,empty)=p=q+(1-q)s`;
- `ehat(empty,B)=(1-q)b_B` for `B nonempty`;
- `|ehat(A,empty)|=q(1-s)` for every `A nonempty` in the proxy block;
- `|ehat(A,B)|=q|b_B|` for `A nonempty`, `B nonempty`.

For a gated dictator `1-e+x e`, every nonempty coefficient of `e` appears twice in the Boolean spectrum with equal squared mass. Put

`ell(t)=-t log_2 t`, `M=2^r-1=q^{-1}-1`, `p=q+(1-q)s`.

A direct entropy subtraction gives the exact identity

`boxed{
Delta_T H =
 ell((1-p)^2)+ell(p^2)
 -(1-q)[ell((1-s)^2)+ell(s^2)]
 +2s(1-s)[ell((1-q)^2)+M ell(q^2)]
 +2M ell(q^2(1-s)^2).
}`                                                                    (3.1)

All terms involving the individual values `b_B^2` cancel. Only their total mass `s(1-s)` remains. Therefore **the short-circuit entropy cost is completely independent of the Fourier entropy, dimension, joint-derivative depth, or internal geometry of the hidden residual R**.

This is the source-valid cancellation missing from the naive recursive-residual picture.

## 4. Universal coefficient five on the entire adversarial OR-lift family

### Theorem 4.1

Assume `r>=2` and `(1-q)s<=q/16`. Then

`boxed{ Delta_T H <= 5 D_T. }`                                      (4.1)

Consequently, for the current corrected functional `mathcal F`,

`boxed{ E_T := mathcal F(F_{Q,R})-(1-q)mathcal F(F_R) <= 5 D_T. }`   (4.2)

The second inequality uses only the already established source-exact corrected-decrement identity at each physical restriction node: corrected decrement is `B-Q_refund <= B <= Delta H`. Summing over the adaptive tree preserves the inequality.

### Proof of (4.1)

From `(1-q)s<=q/16` and `r>=2`,

`s <= q/[16(1-q)] <= q/12 <= 1/48`,

`p <= 17q/16`, and `q<=1/4`.

Drop the negative term in (3.1). Use

`-log_2(1-t) <= t/[(1-t) ln 2]`

and `p>=q=2^{-r}`. The first two positive terms obey

`ell((1-p)^2)+ell(p^2)
 <= 2p/ln2 + 2p^2 r
 <= [17/(8 ln2)]q + [289/512] q r.`                         (4.3)

For the nonconstant residual Fourier mass,

`ell((1-q)^2) <= 2q(1-q)/ln2`,

`M ell(q^2)=2q(1-q)r`,

and `s(1-q)<=q/16`, so

`2s(1-s)[ell((1-q)^2)+M ell(q^2)]
 <= (q^2/4)(r+1/ln2)
 <= (1/16) q r + [1/(16 ln2)]q.`                           (4.4)

Finally,

`2M ell(q^2(1-s)^2)
 =4q(1-q)(1-s)^2[r+log_2(1/(1-s))].`

Since `s<=1/48`,

`log_2(1/(1-s)) <= 4q/(47 ln2)`,

hence

`2M ell(q^2(1-s)^2)
 <= 4qr + [4/(47 ln2)]q.`                                  (4.5)

Combining (4.3)--(4.5),

`Delta_T H
 <= (2369/512) q r
 + [(17/8+1/16+4/47)/ln2] q
 < 4.627 q r + 3.279 q.`                                    (4.6)

Also `s<=1/48` gives

`D_T=q[1+r(1-s)] >= q[1+47r/48].`                           (4.7)

Since

`2369/512 < 235/48 = 5*(47/48)`

and

`(17/8+1/16+4/47)/ln2 < 5`,

(4.6)--(4.7) imply `Delta_T H < 5D_T`. QED.

## 5. Critical-core consequence: arbitrary hidden contamination of this form cannot be a high-ratio obstruction

Let the current state be restriction-maximal for the corrected ratio

`rho = mathcal F/J`.

Every leaf of `T_Q` is a genuine physical restriction descendant, so ratio maximality gives

`E_T >= rho D_T`.

Theorem 4.1 gives `E_T<=5D_T`, and `D_T>0`. Therefore

`boxed{ rho <= 5. }`                                                   (5.1)

Hence **no corrected-ratio critical core with ratio above five can contain an arbitrary-residual OR-lift row of the form above**, even though the false-positive residual itself may have completely arbitrary Boolean complexity.

This is stronger than trying to recurse on the residual event: it pays the whole proxy-peeling step before any claim about residual structure is made.

It also explains why an adversarial residual does not contradict the account02/B14 programme. The correct invariant is not “residual complexity decreases”; it is the exact parent-to-child entropy cancellation (3.1).

## 6. Relation to the previous B16 majority adversary and to the live A gap

The previous B16 run showed that recursive ternary majority can be terminal for coordinate-subcube certification and can have an unbounded normalized positive depth-defect bank, while a source-valid physical restriction excludes exact balanced ternary-majority composites from a corrected-ratio maximizer.

The present theorem handles a different obstruction: **fixed-relative outside pollution can hide an arbitrary residual hard event**. A coverage proof cannot infer low joint-derivative defect, near-subcube structure, or a small exceptional bank inside that residual. Nevertheless, for the exact independent OR-lift geometry, the same realizable first-mismatch tree has corrected cost at most five times its exact folded drift, so high-ratio criticality excludes the entire family.

What remains open is the genuinely interacting outside-pollution case, where the false-positive set is not an independent residual `R(W)` and the Fourier coefficients do not factor into the cancellation (3.1). A next source-valid target is to quantify the deviation from (3.1) by an overlap/interference term that can be charged to the existing asymmetric exceptional ledger or folded activation bank, without replacing it by raw second-factorial moment or by a positive joint-derivative bank.

Full unrestricted FEI remains **OPEN / NOT PROVED**.
