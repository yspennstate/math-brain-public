# B18 — the fixed depth-four shared-core falsifier family saturates after F6

**Outcome:** `ESSENTIAL_STEP_APPLIED / MECHANISM_CLOSED_FOR_THIS_EXACT_ITERATION`. **Full uniform-cube FEI remains OPEN / NOT PROVED.**

**Execution:** `WITHOUT_VERIFIED_BRAIN`. Authenticated repository controls and scientific sources were read through the authorized GitHub connector; no native cognitive-brain retrieval/runtime entered the proof.

## 1. Fresh control and target change

Fresh owner control revision `2026-09-22.2` was reread before delivery. Its FEI convergence target supersedes the older account02/B18 Campaign-C signed-compiler prompt. The owner's proposed AND/decomposable extremality has already been source-validly falsified by the arity-ten balanced gate and then by stronger shared-coordinate gates. This run therefore does not return to the retired signed-current NET surrogate. It consumes the newest completed other-account falsifier family and proves the first missing integration statement forced by it: whether its exact depth-four shared-core recurrence can keep raising the all-gate center cap materially.

The all-gate reformulation remains the exact target: a finite FEI constant is equivalent to a symmetric nonnegative potential `Gamma` satisfying the universal gate inequality `(G)` for every Boolean gate and product bias. For a balanced gate at uniform bias, any such potential must satisfy

\[
H(G)\le \Gamma(1/2)(I(G)-1),
\qquad
R(G):=\frac{H(G)}{I(G)-1}\le \Gamma(1/2).
\tag{1.1}
\]

Thus explicit balanced Boolean gates give rigorous lower bounds on every possible center cap.

## 2. Named completed OTHER-account result consumed

I use account03/B15,

`proofnet24/P03-fei/fleet-2026-09-21/account03/B15/20260922T012556Z-iterated-shared-graft/REPORT.md`,

which in turn source-binds account01/B18's exact nine-host shared-core transform. It proves four further positive depth-four rounds and certifies

\[
6.521850949550448184840160538860511501288648868305895\ldots
<R_6
<6.521850949550448184840160538860511501288648871643879\ldots .
\tag{2.1}
\]

In particular

\[
C_{\rm FEI}>6.5218509495504481848401605388605.
\tag{2.2}
\]

The same source gives the exact recurrence ingredients. Write

\[
\alpha=\frac9{256},\qquad B=\frac{257}{256},\qquad d_0=\frac{133}{128},
\]

\[
\phi(x)=-x\log_2x,
\qquad
K(b)=H_{\rm core}(b)+\alpha\bigl[-\phi(b^2)+16(1-b^2)\bigr].
\tag{2.3}
\]

For the depth-four iteration, if the current balanced gadget has influence `I_r`, excess ratio `R_r`, and designated singleton coefficient `c_r`, then

\[
I_{r+1}=\frac{261}{128}+\alpha(I_r^4-1),
\qquad
c_{r+1}=\frac{57}{256}+\frac{c_r^4}{256},
\tag{2.4}
\]

and

\[
R_{r+1}-R_r
=\frac{K(c_r^4)-d_0R_r}{\alpha I_r^4+B}.
\tag{2.5}
\]

Every member is an actual finite balanced monotone Boolean gate; no arbitrary spectral relaxation is used.

## 3. New exact general-depth identity

The same source formulas immediately extend from depth four to **any integer self-composition depth `m>=1`** before applying the identical nine-host graft.

### Proposition 3.1 — depth currency identity

Let a balanced Boolean gadget have

\[
R=\frac{H}{I-1},
\]

influence `I>1`, and designated singleton Fourier coefficient `c`. Take its depth-`m` disjoint self-composition, then apply the source-exact nine-host shared-core graft. The resulting balanced Boolean gate has

\[
I'=\frac{261}{128}+\alpha(I^m-1),
\qquad
c'=\frac{57}{256}+\frac{c^m}{256},
\tag{3.1}
\]

and exactly

\[
\boxed{
R'-R=\frac{K(c^m)-d_0R}{\alpha I^m+B}.
}
\tag{3.2}
\]

In particular, for fixed `(R,c,m)`, the **sign** of the improvement is independent of the current influence `I`; influence only controls the size of the step.

### Proof

Balanced depth-`m` self-composition has

\[
I_A=I^m,
\qquad
H_A=H\frac{I^m-1}{I-1}=R(I^m-1),
\qquad
c_A=c^m.
\]

The source-exact graft formulas give

\[
H'=K(c^m)+\alpha R(I^m-1),
\qquad
I'=\frac{261}{128}+\alpha(I^m-1).
\]

Since

\[
I'-1=\alpha I^m+B
\]

and `alpha+B=d_0`, subtracting `R` from `H'/(I'-1)` gives (3.2). No approximation is present. `square`

This identity is useful because it separates the only two currencies of this construction: the numerator `K(c^m)-d_0R`, which decides whether a depth can improve the obstruction at all, and the denominator `alpha I^m+B`, which suppresses the size once influence is large.

## 4. New theorem: the exact depth-four family has less than 1e-26 total movement after F6

The account03 report correctly warned not to freeze a universal potential at the latest finite witness before analyzing the iteration. The following closes that warning for the **fixed depth-four map itself**.

### Lemma 4.1 — uniform bound on the shared-core source term

For every `0<=b<=1`,

\[
0\le K(b)\le \frac{153}{16}.
\tag{4.1}
\]

### Proof

The source core has nine pairwise disjoint host edges, hence eighteen host vertices. The physical function whose normalized Walsh coefficients enter `H_core(b)` has magnitude `1` on the other 494 vertices and magnitude `b` on those eighteen vertices. Therefore its total squared Fourier mass is

\[
M(b)=\frac{494+18b^2}{512}\le1.
\]

There are 512 Fourier atoms. For any nonnegative masses summing to `M<=1`, entropy concavity gives

\[
\sum_s -p_s\log_2p_s
\le M\log_2\frac{512}{M}\le9,
\]

because `M(9-log_2 M)` is increasing on `[0,1]`. Thus `0<=H_core(b)<=9`.

For `x in [0,1]`, convexity of `x log x` gives

\[
-x\ln x\le1-x,
\]

so

\[
\phi(x)\le\frac{1-x}{\ln2}<16(1-x).
\]

Hence

\[
0\le-\phi(b^2)+16(1-b^2)\le16.
\]

Using `alpha=9/256` proves

\[
0\le K(b)\le9+16\frac9{256}=\frac{153}{16}.
\]
`\square`

### Theorem 4.2 — depth-four saturation after F6

Continue the account03/B15 depth-four recurrence from `F_6` indefinitely. Then the sequence `R_r` converges and

\[
\boxed{
\sum_{r=6}^{\infty}|R_{r+1}-R_r|<10^{-26}.
}
\tag{4.2}
\]

Consequently every later gate in this exact fixed-depth family satisfies

\[
\boxed{
R_r<6.52185094955044818484016055
\qquad(r\ge6).
}
\tag{4.3}
\]

The same bound holds for its limiting ratio.

### Proof

Put

\[
D_r=\alpha I_r^4+B,
\qquad
L_r=\frac{K(c_r^4)}{d_0},
\qquad
w_r=\frac{d_0}{D_r}.
\]

Equation (2.5) becomes the exact affine update

\[
R_{r+1}=(1-w_r)R_r+w_rL_r.
\tag{4.4}
\]

Lemma 4.1 gives

\[
0\le L_r\le\frac{153/16}{133/128}=\frac{1224}{133}<9.204.
\tag{4.5}
\]

The peer interval (2.1) puts `R_6` strictly inside the same interval. We next bound the denominators using only exact rational inequalities from the source recurrence. Account01/B18 gives

\[
I_2=rac{784028312243315011737}{295147905179352825856}>rac{53}{20}.
\]

Since `x -> 261/128+alpha(x^4-1)` is increasing for positive `x`, successive exact comparisons give

\[
I_3>\frac{37}{10},
\qquad
I_4>8,
\qquad
I_5>140,
\]

and

\[
I_6>
\frac{261}{128}+\frac9{256}(140^4-1)
=13505627.00390625
>13{,}500{,}000.
\tag{4.6}
\]

Thus

\[
D_6>\alpha(13{,}500{,}000)^4.
\tag{4.7}
\]

In particular `w_6<1`. For every `r>=6`, `I_r>=13,500,000` implies

\[
I_{r+1}>\alpha I_r^4\ge2I_r
\]

and `alpha I_r^4>=B`. Therefore

\[
D_{r+1}
=\alpha I_{r+1}^4+B
\ge16\alpha I_r^4
\ge8D_r.
\tag{4.8}
\]

Inductively `0<w_r<1`, so (4.4)-(4.5) keep every later `R_r` in `[0,1224/133]`. Therefore

\[
|K(c_r^4)-d_0R_r|
=d_0|L_r-R_r|
\le\frac{153}{16},
\]

and

\[
|R_{r+1}-R_r|\le\frac{153}{16D_r}.
\]

Using (4.8) and then (4.7),

\[
\sum_{r=6}^{\infty}|R_{r+1}-R_r|
\le
\frac{153}{16D_6}\sum_{j=0}^{\infty}8^{-j}
<
\frac{8}{7}\frac{153/16}{(9/256)(13{,}500{,}000)^4}
<10^{-26}.
\]

This proves absolute convergence and (4.2). Adding `10^-26` to the peer's rigorous upper endpoint in (2.1) gives the safe displayed bound (4.3). `\square`

## 5. What this changes and what it does not

**FULL-PROBLEM CHANGE:** none. The theorem above does not produce any finite universal upper bound; unrestricted FEI remains **OPEN**.

**MECHANISM CHANGE:** yes. The newest shared-coordinate lower-bound mechanism is no longer left with the vague obligation “keep iterating depth four and see whether the center rises again.” For the exact source-valid depth-four recurrence, all post-`F6` movement combined is below `1e-26`. The finite witness lower bound (2.2) is therefore essentially the full value of **that exact iteration mechanism**.

This does **not** upper-bound other mechanisms. Proposition 3.1 shows precisely where a stronger same-core construction can still enter: choose another integer depth `m` for which `K(c^m)-d_0R>0`, change the shared core, or use a different gate/bias construction. Nor does saturation of one lower-bound family imply any universal all-gate inequality.

The old AND/decomposable extremality candidate remains refuted. The new universal obligation is still to construct a finite-cap symmetric potential satisfying `(G)` for every gate and every product bias, or equivalently to prove another dimension-independent FEI upper bound. Any candidate center must exceed the certified lower bound (2.2).

## 6. Ledger

- **PROVED (inherited, gate reformulation):** full FEI is equivalent to the all-gate potential inequality `(G)`.
- **REFUTED (inherited, account03/B12 + account04/B13):** AND/decomposable extremality at the read-once potential; a balanced monotone composition-prime ten-input gate already violates it.
- **PROVED (inherited, account01/B18):** source-exact shared-core transformation and depth-four recurrence.
- **PROVED (inherited, account03/B15):** four further positive depth-four rounds through `F6`, giving the certified lower bound (2.2).
- **PROVED (this run):** exact arbitrary-depth identity (3.2).
- **PROVED (this run):** source-term bound `0<=K<=153/16`.
- **PROVED (this run):** fixed-depth-four tail after `F6` is absolutely less than `10^-26`; no materially larger center obstruction can come from merely continuing that exact recurrence.
- **OPEN:** whether another depth/core/gate produces a larger lower obstruction; more importantly, any finite universal upper bound for all Boolean gates/biases.

## 7. Literature and scope boundary

A fresh 22 September 2026 literature check finds Potapov's 18 September 2026 theorem for plateaued Boolean functions (sharp class constant 4) and partially bent functions (sharp class constant 2), and González--MacManus--Pereyra's 2026 restriction/stopping framework whose key universal restriction inequality is explicitly conditional. These are compatible with the repository status `OPEN / NOT PROVED` for unrestricted FEI. A search miss is not used as a novelty claim, and no publication-priority claim is made for the saturation lemma.

## 8. Operational boundary

The managed account02 B01--B20 inventory is fully enabled and hourly-valid in the exposed scheduler; no B18 scheduler mutation was made. The canonical brain login write for this invocation was denied by the platform safety layer and was not bypassed or fabricated. Scientific work is saved only in this own B18 research path. Model self-report: `GPT-5.6 Sol`; requested effort: maximum actually supported; configured/known effort: `UNKNOWN / NOT_EXPOSED`; provider reasoning usage: `null / NOT_EXPOSED`. Elapsed execution is recorded separately in the sanitized receipt and is not pure thinking time.
