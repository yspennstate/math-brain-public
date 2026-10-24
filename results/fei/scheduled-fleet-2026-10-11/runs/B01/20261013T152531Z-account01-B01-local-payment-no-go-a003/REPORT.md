# B01 / A003 — exact no-go for coordinatewise upper-set payment

**Run:** `20261013T152531Z-account01-B01-local-payment-no-go-a003`  
**Primary packet:** A003, minimal target formulation  
**Stable gap:** `GU-ASYMMETRY-MISMATCH`  
**Attempt:** `B01-A003-LOCAL-PAYMENT-NO-GO-03`  
**Status:** exact finite falsifier, pending A086/A094 independent reproduction.  
**Full FEI:** **OPEN**.

## Result

For a physical coordinate (i), the source-pinned identity is

\[
 \Delta_iU=B_i-\Gamma_i+K_i,
 \qquad B_i=H(S_i\mid S_{-i}),
\]

with (K_i\ge0).  This run froze the most direct proposed payment

\[
 K_i\le \Gamma_i+c\operatorname{Inf}_i,
 \tag{L_c}
\]

which is equivalent to

\[
 \Delta_iU\le B_i+c\operatorname{Inf}_i.
\]

The proposed inequality is **false even for (c=4/3)**.  A genuine
five-bit Boolean function and its second physical coordinate satisfy

\[
 \frac{\Delta_iU-B_i}{\operatorname{Inf}_i}
 =1.3359233827857603925\ldots>{4\over3}.
\]

Thus the initially attempted coefficient-one lemma, and every local lemma
of the same form with (c\le4/3), is rigorously retired.  This is a stronger
obstruction than a floating search result: `CERTIFY_LOCAL_NO_GO.py` reduces
the sign to one exact integer comparison.

## Exact witness

Encode (x=(x_0,\ldots,x_4)\in\mathbb F_2^5) by
(x_0+2x_1+4x_2+8x_3+16x_4).  Let (f(x)=+1) precisely at

```text
{1,3,4,8,10,11,13,14,15,16,18,19,21,22,25,28,30}
```

and (-1) elsewhere.  Equivalently the truth mask is `1382935834`.
For coordinate (i=1) (zero based), the checker obtains

\[
\begin{aligned}
 \operatorname{Inf}_i&=7/16,\\
 \Delta_iU&=1.5620414139468923621750\ldots,\\
 B_i&=0.9775749339781221904469\ldots,\\
 \Delta_iU-B_i-{4\over3}\operatorname{Inf}_i
 &=0.0011331466354368383949\ldots>0.
\end{aligned}
\]

After multiplying the last expression by (3\cdot32^2), all logarithmic
weights are integers.  Its sign is the sign of

\[
 {7^{588}11^{96}17^{24}19^{624}23^{300}
  \over
  2^{3148}3^{276}5^{216}13^{540}}-1,
\]

and the numerator is an exact 6089-bit integer exceeding the exact
6086-bit denominator.  No floating-point comparison enters the proof.

## The surviving nonlocal candidate

Write (B=\sum_iB_i\le H).  The universal aggregate inequality

\[
 \boxed{G(f)\le H(f)+I(f)}                                      \tag{A}
\]

would be equivalent, using the exact restriction identity, to

\[
 \sum_i(K_i-\Gamma_i)\le I+(H-B).                              \tag{A'}
\]

The term (H-B\) is the global dual-entropy slack that a coordinatewise
argument discards.  The falsifier above is compatible with (A): it has

\[
 H+I-G=3.9940103914495344\ldots>0.
\]

`CHECK_AGGREGATE_PILOT.py` exhausts every Boolean sign modulo output sign
through four variables (32,906 functions) and checks 26,000 deterministic
random functions in dimensions five through seven.  It finds no violation
of (A).  This finite survival is **NUMERICAL**, not a proof.

## Movement relative to the nullity-two shield target

The preceding run proved (H,U\le2I) for every rank-((m-2)) shield and
froze (G\le3I) on that class.  Inequality (A), if proved on that class,
would imply the frozen bound immediately.  The present run does not prove
(A), so there is **no new class bound** and (G\le3I) remains open.

What moved is the proof architecture: a per-coordinate payment of the
upper-set mismatch by (B_i+c\operatorname{Inf}_i) cannot deliver the
coefficient-one (or (4/3)) bridge.  The next attempt must retain the
global slack (H-B), first on the rank-((m-2)) repetition law and then
without a class assumption.  Repeating local coefficient tuning below the
certified ratio is now excluded.

## Verification and scope

- `CERTIFY_LOCAL_NO_GO.py` is an exact Walsh/integer certificate and prints
  `PASS` only after comparing the two exact integers.
- `CHECK_AGGREGATE_PILOT.py` is a bounded falsifier search; it proves no
  all-dimensional statement.
- The witness is not an FEI counterexample and does not refute (A), GU', or
  the shield conjecture (G\le3I).
- Independent reproduction remains required before registry acceptance.

## Source pins

- Owner control revision `2026-10-12.1`, Brain control commit
  `40210272c19f43fed84f6a67653f9a04b0e11e28`; current `ORDER.md` blob
  `7c5e21945adef435e6b587909603dd96794a1ebe` and `CASE_TARGETS.json` blob
  `97e41262ebb4f09eec53630a918acae09efc9a48`.
- A003 assignment blob `ac038a028831d59ad053dd56b2b527e2a71ffdee`;
  execution protocol blob `457358ff62cbf1141a72096bcabdf95bf18c1be2`.
- Prior arbitrary-nullity-two package commit
  `99c60c7a5554f2a435016ad100ccb5d2d10a6bd0`.
- Source heads observed before save: canonical
  `b6d99fe02e696a8d4fa940176cc12801f0992c5a`; Brain
  `c370e653313aa379ffe8ea77614b288a2eb1fd6d`.

No literature-priority claim, protected source, paid compute, public release,
scheduler mutation, or subagent was used.  Exposed model: Codex; reasoning
effort metadata was not exposed.

