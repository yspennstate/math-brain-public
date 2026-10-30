# B01 / A003 — signed-mismatch refund reduction

**Run:** `20261014T042403Z-fleet01-B01-signed-mismatch-refund-a003`  
**Primary packet:** A003, minimal target formulation  
**Stable gap:** `GU-ASYMMETRY-MISMATCH`  
**Claim version:** `B01-A003-SIGNED-MISMATCH-REFUND-v1`  
**Status:** exact reduction proved; aggregate inequality open; a natural coordinate allocation exactly refuted  
**Full FEI:** **OPEN**

## Result

Let

\[
B(f)=\sum_i B_i(f),\qquad
M(f)=\sum_i\bigl(K_i(f)-\Gamma_i(f)\bigr),
\]

so the source identity gives `G=B+M`, while `B<=H` and the reviewed bridge
gives

\[
H(f)\le 2\bigl(I(f)-\operatorname{Var}(f)\bigr)+2U(f).
\]

The following is an exact sufficient reduction.  For any fixed
`0<eta<=1` and `c<infinity`, if every genuine Boolean sign satisfies

\[
\boxed{M(f)+(1+\eta)U(f)\le cI(f),} \tag{SMR}_{c,\eta}
\]

then every such sign satisfies

\[
\boxed{G(f)\le(c+2)I(f)+(1-\eta)U(f)-2\operatorname{Var}(f)}
\]

and hence universal GU' with `(a,b)=(c+2,1-eta)`.  The reviewed induction
then gives

\[
U(f)\le\frac{c+2}{\eta}I(f),\qquad
H(f)\le\left(2+\frac{2(c+2)}{\eta}\right)I(f).
\]

I froze the concrete candidate

\[
\boxed{M(f)+\frac54U(f)\le2I(f).} \tag{SMR}_{2,1/4}
\]

It would give the explicit admissible pair

\[
(a,b)=\left(4,\frac34\right)
\]

and FEI constant `C=34`.  This candidate is **OPEN**, not a proved GU
inequality.

## Why this is smaller than the old gap statement

The whole positive spectral-label entropy `B` has been discharged using the
two reviewed inequalities `B<=H` and `H<=2(I-Var)+2U`.  What remains is only
the signed upper-set mismatch `M=sum_i(K_i-Gamma_i)`, and it must refund
strictly more than one copy of `U`.  A coefficient exactly one would leave
the forbidden endpoint `b=1`; any `eta>0` crosses the GU threshold.

The latest fixed-shared-block result does not remove this leaf.  Its
singleton potential already obeys the universal estimate
`Phi<=(2/ln 2)I`; the unresolved issue is repeated transport/ownership in
the signed `M` ledger, not the isolated `log |X|` estimate.

## Coordinate attack and exact obstruction

For `I(f)>0`, define a normalized allocation of `U` by

\[
u_i^*(f)=
\sum_{\substack{S\ni i\\S\ne\varnothing}}
\frac{p_S}{|S|}\log_2\frac{\pi(S)}{p_S}
+\frac{\operatorname{Inf}_i(f)}{I(f)}
p_\varnothing\log_2\frac1{p_\varnothing}.
\]

Then `sum_i u_i^*=U`.  The most direct coordinate proof of the frozen
candidate would be

\[
\Delta_iU-B_i+\frac54u_i^*\le2\operatorname{Inf}_i
\quad\text{for every }i. \tag{LOC}
\]

`LOC` is **false**.  On five bits, let the `+1` truth-table positions be the
set encoded by mask `2624023184` (least-significant bit is input zero), and
take zero-based coordinate `i=2`.  Then

\[
\operatorname{Inf}_i=\frac7{16}
\]

and numerically

\[
\Delta_iU-B_i+\frac54u_i^*-2\operatorname{Inf}_i
=0.1072928565\ldots>0.
\]

`CERTIFY_SIGNED_MISMATCH.py` proves the sign exactly.  It expresses the
quantity, after multiplying by `135168`, as one base-two logarithm of a
rational number and compares the resulting positive and negative integer
products.  The positive integer has 1,142,754 bits, the negative integer has
1,128,252 bits, and the exact comparison passes.  Thus the aggregate
candidate cannot be proved by this coordinate allocation; global
cancellation between coordinates is essential.

The same witness is not an aggregate falsifier:

\[
M+\frac54U=3.8757080815\ldots<6.875=2I.
\]

## Calibration and bounded tests

The four-bit truth vector

```text
(+,-,-,-,-,-,-,+,+,+,+,-,+,-,-,-)
```

has the exact values

\[
H=B=4,\quad U=I=2,\quad G=\frac{11}{2},\quad M=\frac32.
\]

Hence it is an exact equality case for the frozen aggregate candidate:

\[
M+\frac54U=4=2I.
\]

The constant `c=2` is therefore sharp if `eta=1/4` is retained.  Because
`G,U,I,B`, and hence `M`, are additive under disjoint Boolean products, all
tensor powers remain equality cases.

The checker performed the following bounded falsifier search:

- all 32,906 Boolean signs modulo output sign in dimensions one through four;
- 37,500 deterministic random signs in dimensions five through nine, seed
  `20261014`;
- point defects through dimension nine;
- odd majority through dimension eleven; and
- addressing functions with one, two, and three address bits.

No aggregate violation was found.  The maximum exhaustive ratio
`(M+5U/4)/I` through four variables was exactly `2`; the maximum random ratio
was `1.8551622406`.  These are **NUMERICAL** scope checks only and do not
prove the all-dimensional inequality.

## Tensor stability

For functions on disjoint blocks, the spectral subset laws are independent.
Therefore `U`, `G`, `I`, and `B=sum_i H(S_i|S_{-i})` are additive, so `M` is
additive.  Consequently `(SMR)_{c,eta}` is exactly stable under disjoint
products.  The equality calibration above shows that tensorization neither
improves nor damages the frozen constant.

## Exact remaining obstacle

Prove or refute the **aggregate** inequality `(SMR)_{2,1/4}`.  The next
analytic attempt must retain cross-coordinate cancellation in
`sum_i(K_i-Gamma_i)`; any proof that assigns the full `U` credit independently
to each coordinate through `u_i^*` is ruled out by the exact five-bit
witness.  A useful next mechanism is a pairwise/upper-cone transport in which
the excess at one coordinate is charged to `Gamma_j` or unused `u_j^*` at a
different coordinate, with the four-bit tensor equality case kept sharp.

## Sources and execution facts

- GU focus revision `2026-10-14.1`, Brain blob
  `9448198701fbfe0cceb72bda7a6837ebd59704f9`.
- A003 assignment blob `ac038a028831d59ad053dd56b2b527e2a71ffdee`.
- Source-reviewed GU-to-U induction and `H<=2I+2U`: B01 tensor/activation
  proof blob `980120689bdef11652e6e002c47651e08fc1a9e2`, which pins the original
  `U-universal` source blob `5797e9cc38598cbee391cc99d4b1abcd554b662e`.
- Latest B01 overlap proof blob
  `6fd58274bb6714e4e6e80acd93c4b8bbca03eb3c`.
- B19 fixed-block review blob
  `f2240e526944e57e1ef100f2b6e1d31ca252743f` at canonical commit
  `4a16555709214b313e181c00231efe8f6ac3c187`.

Commands: `python CHECK_SIGNED_MISMATCH.py` and
`python CERTIFY_SIGNED_MISMATCH.py`.  No protected source, paid compute,
public release, scheduler mutation, or subagent was used.  Exposed model:
Codex; reasoning-effort metadata: UNKNOWN.

