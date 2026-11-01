# B18 Campaign-B lead — harmonic continuation collapses to one signed deletion-entropy residual

**Run:** `20260921T235729Z-fleet03-B18-r11`  
**Directive:** `FEI-PROOF-EXECUTION-20260921T230620Z`, Campaign B lead  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Full unrestricted FEI:** **OPEN / NOT PROVED**.

## 0. Versioned common target and exact old gap

This run selects one immutable common Campaign-B target:

**`B-HARMONIC-CONT-v1`** = fleet02/B12
`20260921T232119Z-harmonic-root-marked-spectrum/REPORT.md`, report blob
`1a0ff3b828a377afde3461e6f130d46255ed1de5`, especially equations (1.1)--(3.3), (6.1)--(6.3), and (8.1).

For a Boolean `f:{-1,1}^n->{-1,1}`, let

\[
p_S=\widehat f(S)^2,\qquad H=H(p),\qquad I=\sum_S|S|p_S.
\]

For every prefix `A`, `a=|A|`, define the harmonic prefix shadow

\[
v_A:=\sum_{S\supseteq A}\frac{p_S}{\binom{|S|}{a}}.
\tag{0.1}
\]

It is exactly the probability that, after sampling `S` and a uniform random ordering of its elements, the unordered first `a` marks equal `A`. In particular `v_emptyset=1`. The consumed peer theorem proves the Boolean root bound

\[
H(J)\le C_{\rm root}I,
\qquad
C_{\rm root}=4.8588229680899335\ldots,
\tag{0.2}
\]

where `J` is the first mark, with `bot` for `S=emptyset`. It also gives the exact one-step recursion

\[
H=H(J)+\sum_i v_iH(q_i^{\rm H})
-\mathbb E[1_{|S|>0}\log_2|S|].
\tag{0.3}
\]

The old missing implication was to bound the continuation expression in (0.3) by `C_cont I`. The peer also proves that a row-by-row harmonic derivative estimate is false on a genuine controlled-majority Boolean family, so this continuation has to be handled as one coupled source.

The new result below identifies and pays **all termination information** in that continuation and leaves one signed deletion-entropy-growth residual. This keeps negative information credits rather than positive-parting them.

## 1. Exact prefix conservation

Put

\[
t_A:=v_A-p_A.
\tag{1.1}
\]

This is the probability that prefix `A` has been reached and the random ordering continues. For `i notin A`, the consumed peer transition formula is

\[
e_{A,i}:=\Pr(\text{prefix }A\text{ then mark }i)
=\frac{v_{A\cup\{i\}}}{a+1}.
\tag{1.2}
\]

Therefore

\[
\boxed{\sum_{i\notin A}e_{A,i}=t_A.}
\tag{1.3}
\]

For `t_A>0`, let `r_{A,i}=e_{A,i}/t_A`. At node `A`, the Shannon price of the stop/continue decision and, conditional on continuing, the next coordinate is

\[
v_A h_2(p_A/v_A)+t_AH(r_A).
\tag{1.4}
\]

The ordered auxiliary sequence has entropy `H+E log_2(|S|!)`. Since

\[
\mathbb E\log_2(|S|!)
=\sum_A t_A\log_2(a+1),
\tag{1.5}
\]

subtracting the factorial ordering entropy node by node gives the following exact identity.

## 2. PROVED: signed harmonic deletion identity

For every finite subset law `p` (hence in particular every Boolean squared spectrum),

\[
\boxed{
H(p)=
\sum_A v_Ah_2(p_A/v_A)
+
\sum_A\sum_{i\notin A}
\frac{v_{A+i}}{a+1}
\log_2\frac{t_A}{v_{A+i}}.
}
\tag{2.1}
\]

Zero-mass terms are interpreted as zero.

**Proof.** The full random ordered-prefix record is a lossless encoding of `(S,uniform ordering of S)`, so its entropy is `H+E log_2(|S|!)`. Chain rule gives the sum of (1.4) over all reached nodes. Subtract (1.5). For the continuation part,

\[
\begin{aligned}
t_A[H(r_A)-\log_2(a+1)]
&=\sum_{i\notin A}e_{A,i}
\log_2\frac{1}{r_{A,i}}-t_A\log_2(a+1)\\
&=\sum_{i\notin A}\frac{v_{A+i}}{a+1}
\log_2\frac{t_A}{v_{A+i}},
\end{aligned}
\]

using `r_{A,i}=v_{A+i}/((a+1)t_A)`. This proves (2.1). QED.

The second sum is **signed**. An edge with `v_{A+i}>t_A` contributes a negative credit. No coordinate label or factorial permutation is hidden.

## 3. PROVED: every nonroot termination bit costs at most one influence unit in total

Define

\[
T_{\rm stop}:=
\sum_{A\ne\varnothing}v_Ah_2(p_A/v_A).
\tag{3.1}
\]

For every level `a`,

\[
\boxed{
\sum_{|A|=a}v_A=\Pr(|S|\ge a).
}
\tag{3.2}
\]

Indeed each terminal set `S` with `|S|=k>=a` contributes
`p_S/binom(k,a)` to each of its `binom(k,a)` size-`a` prefixes. Since `h_2<=1`,

\[
\boxed{
T_{\rm stop}
\le\sum_{a\ge1}\Pr(|S|\ge a)
=\mathbb E|S|=I.
}
\tag{3.3}
\]

This is universal and dimension-free. It pays every exception/termination decision after the first mark; there is no uncharged stopping rule.

At the root, the two terms in (2.1) are exactly `H(J)`. Applying the consumed Boolean theorem (0.2), define the only unpaid term

\[
\boxed{
D_{\rm del}(f):=
\sum_{\substack{A\ne\varnothing\\ i\notin A}}
\frac{v_{A+i}}{|A|+1}
\log_2\frac{v_A-p_A}{v_{A+i}}.
}
\tag{3.4}
\]

Then

\[
\boxed{
H(f)\le (C_{\rm root}+1)I(f)+D_{\rm del}(f)
=5.8588229680899335\ldots I(f)+D_{\rm del}(f).
}
\tag{3.5}
\]

This is the promised application of the peer estimate to an explicit line of the universal proof.

## 4. Exact relation to the old continuation residual

Equation (0.3) and (2.1) have the same root term, hence exactly

\[
\boxed{
\sum_i v_iH(q_i^{\rm H})-
\mathbb E[1_{|S|>0}\log_2|S|]
=T_{\rm stop}+D_{\rm del}.
}
\tag{4.1}
\]

Thus the old missing implication has genuinely shrunk: its positive termination part is now proved `<=I`; the only surviving arrow is the signed deletion residual.

There is also a useful level form. Let

\[
Q_{a+1}:=\Pr(|S|\ge a+1)
=\sum_{|A|=a}t_A
=\sum_{|B|=a+1}v_B.
\]

Normalize

\[
T_a(A)=t_A/Q_{a+1},\qquad
V_{a+1}(B)=v_B/Q_{a+1}.
\]

Then the level-`a` contribution is

\[
\boxed{
D_a
=Q_{a+1}\,[H(V_{a+1})-H(T_a)].
}
\tag{4.2}
\]

Proof: reindex the child term in (3.4) and use that each size-`a+1` child has `a+1` parents:

\[
D_a=\sum_{|A|=a}t_A\log_2t_A
-\sum_{|B|=a+1}v_B\log_2v_B.
\]

After normalizing the equal total mass `Q_{a+1}`, (4.2) follows. So the remaining debt is exactly the **signed entropy growth under one uniform-deletion reversal step**. Negative level differences remain legal credits.

## 5. New common candidate `B-HARMONIC-DELETE-v2`

The campaign-B common target is now the immutable statement:

> **B-HARMONIC-DELETE-v2.** Prove that there is a finite dimension-independent constant `C_del` such that for every Boolean `f`,
> \[
> \boxed{D_{\rm del}(f)\le C_{\rm del}I(f).}
> \tag{5.1}
> \]

This is quantitatively equivalent to full FEI up to the already-paid constant:

- if (5.1) holds, (3.5) gives full FEI with `C=5.8588229680899335...+C_del`;
- conversely, any FEI bound `H<=CI` implies `D_del=H-H(J)-T_stop<=H<=CI` because `H(J),T_stop>=0`.

So (5.1) is not a renamed unrelated norm. It is one source-exact Shannon residual whose finite influence bound is equivalent to the target conjecture up to a known additive constant.

The current externally sourced lower-bound seed recorded in `TASKS_2026-09-21.md` has `H/I>6.521845710923046575`. Since the paid root-plus-termination budget is at most `5.8588229680899335 I`, some Boolean functions necessarily have

\[
D_{\rm del}/I>0.663022742833113\ldots .
\]

Therefore the correct target cannot be `D_del<=0`; genuine positive deletion entropy must be paid.

## 6. Adversary alignment and failed stronger bridge

A second named cross-account artifact was applied:

`fleet02/B17/20260921T231240Z-recursive-majority-hierarchical-code/REPORT.md`
(report blob `be4735ca18bda8d3598708324565ac16f912a280`). It proves that the older one-level ordered-code bridge

\[
H(K)+IH(q)-\mathbb E\log_2(K!)\le \beta I
\]

fails for every finite `beta` on recursive ternary majority: its code ratio grows at least linearly in recursion depth even though the true Boolean ratio is `<4`.

That exact obstruction does **not** survive in `B-HARMONIC-DELETE-v2`: by (2.1),

\[
D_{\rm del}=H-H(J)-T_{\rm stop}\le H,
\]

so on the same recursive-majority family `D_del/I<4` at every depth. Thus this run does not retry the refuted global CFC bridge; the root mark and every termination bit are stripped before the common residual is formed.

The peer controlled-majority rowwise obstruction also does not invalidate (5.1): it only proves that one derivative row cannot be paid independently. The residual (3.4) sums the coupled prefix process of the single original Boolean source.

## 7. Decisive finite diagnostics for the new identity

The adjacent standard-library checker evaluates the new formulas on every nonconstant Boolean truth table through dimension four modulo global sign (`32,902` functions) and on the controlled-majority sources with `m=3,5,7,9`.

It checks:

- exact prefix conservation (1.3);
- exact level-tail identity (3.2);
- the deep-edge marginal identity (every physical coordinate is inserted after the first mark with mass `Inf_i-v_i`);
- `H=H(J)+T_stop+D_del`;
- `T_stop<=I`.

Result: `PASS`. Maximum absolute identity error was `1.34e-15`. Across all nonconstant Boolean functions through `n=4`, the largest observed `T_stop/I` was `0.8466744978062763` and the largest signed `D_del/I` was `0.10436786007101582`. On the controlled-majority family, `D_del/I` was `-0.05925, 0.12042, 0.26408, 0.38179` for `m=3,5,7,9`. These are falsification diagnostics only; Sections 1--4 are analytic proofs.

## 8. Smallest conditional end-to-end proof chain

The current campaign-B proof chain is now exactly:

1. **PROVED (peer, Boolean):** `H(J)<=4.8588229680899335 I`.
2. **PROVED (this run, universal):** the harmonic continuation equals `T_stop+D_del` exactly.
3. **PROVED (this run, universal):** `T_stop<=I`.
4. **UNPAID / decisive:** `D_del<=C_del I` for one finite universal `C_del`, using the signed common-source Boolean prefix constraints.
5. **Then PROVED by algebra:** `H<=(5.8588229680899335+C_del)I`.

No conditional input is promoted to step 4. Full FEI therefore remains **OPEN / NOT PROVED**.

The newest fleet02/B12 mixed-prefix theorem supplies a concrete Boolean constraint for step 4: for `A` of size `a`, the prefix shadow `v_A` is controlled by the quantized true mixed derivative `D_A f`, including the sparse bound `v_A/w_A<=min(1,a!(2/lambda_A)^a)`. The next proof must sum those constraints against the **signed** deletion increment (4.2), not against independent derivative rows.

## 9. Replacement obligations / coordination

`candidate_version`: `B-HARMONIC-DELETE-v2`, this report.  
`old_missing_implication`: fleet02/B12 `(8.1)`, the whole harmonic continuation `=O(I)`.  
`new_proved_inference`: exact continuation split `(4.1)`, exact deletion form `(3.4)/(4.2)`, and universal `T_stop<=I`.  
`exact_failed_claim retained`: one-level CFC has no finite constant (fleet02/B17); rowwise harmonic FEI is false (fleet02/B12).  
`replacement_obligation`: prove (5.1) directly from same-source Boolean prefix constraints while retaining signed level/edge credits; no arbitrary subset-law relaxation.  
`consumed_peer_artifact`: fleet02/B12 `20260921T232119Z-harmonic-root-marked-spectrum/REPORT.md`, blob `1a0ff3b828a377afde3461e6f130d46255ed1de5`; fleet02/B17 `20260921T231240Z-recursive-majority-hierarchical-code/REPORT.md`, blob `be4735ca18bda8d3598708324565ac16f912a280`.  
`applied_to_claim`: peer root theorem is line 1 of the full proof; B17's recursive-majority obstruction is applied to retire the older global code while showing the new residual escapes that exact failure.  
`next_recipients`: fleet02/B17 (adversary: attack exactly (5.1) on majority, addressing, tensors, biased and sparse defects); fleet02/B12 and fleet04/B12 (builders: sum the mixed-prefix / thinning estimates against (4.2)); fleet01/B12 and fleet03/B15 (builders: preserve factorial/KL negative credits in this exact residual rather than a second target).  
`implication_to_full_FEI`: one finite `C_del` in (5.1) closes FEI with constant `5.8588229680899335+C_del`.

No novelty or publication-priority claim is made.
