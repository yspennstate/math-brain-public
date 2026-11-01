# B01 / A003 — balanced sublinear-terminal reduction

**Run:** `20261014T051405Z-fleet01-B01-balanced-smr-reduction-a003`  
**Primary packet:** A003, minimal target formulation  
**Stable gap:** `GU-ASYMMETRY-MISMATCH`  
**Claim version:** `B01-A003-BALANCED-SUBLINEAR-SMR-v1`  
**Status:** **PROVED reduction pending independent review; universal inequality OPEN**  
**Full FEI:** **OPEN**

## Exact candidate and prior bound

Write

\[
M(f)=G(f)-B(f)=\sum_i(K_i-\Gamma_i).
\]

The sharp candidate `M+(5/4)U<=2I` was refuted by B05 and independently
certified by B19 on a genuine five-bit fair activation.  Its residual is
`0.0923435545007156...` bits, so it cannot be used to derive GU `(4,3/4)`.
The surviving general reduction was only

\[
M+(1+\eta)U\le cI
\quad\Longrightarrow\quad
G\le(c+2)I+(1-\eta)U.
\]

This run freezes the strictly relaxed operational target

\[
\boxed{M(h)+(1+\eta)U(h)\le cI(h)+e_N}
\tag{BAL-SMR-o(N)}
\]

for every **balanced** Boolean `h` on `N` inputs, with one
`0<eta<=1`, one finite `c>=0`, and one absolute sequence satisfying
`|e_N|/N->0`.

## Main result

`PROOF.md` proves that `BAL-SMR-o(N)` is sufficient for the exact universal
signed-mismatch inequality with the same `c,eta`, hence for

\[
(a,b)=(c+2,1-\eta),
\qquad
H\le\left(2+\frac{2(c+2)}\eta\right)I.
\]

The proof uses the balanced hardness lift

\[
h_t(y,x^{(1)},\ldots,x^{(t)})
=y\prod_{j=1}^t f(x^{(j)}).
\]

For every Boolean seed `f`, exact Fourier relabelling and disjoint-product
factorization give

\[
U(h_t)=tU(f),\quad G(h_t)=tG(f),\quad B(h_t)=tB(f),
\quad M(h_t)=tM(f),\quad I(h_t)=tI(f)+1.
\]

Applying the balanced estimate, dividing by `t`, and letting `t->infinity`
removes both the balancing cost `c/t` and every sublinear terminal
`e_{tn+1}/t`.  The converse is immediate with `e_N=0`, so this is an exact
hardness equivalence, not a proof of the unpaid inequality.

This advances the earlier A002 balancing ledger: that report proved only
`H(yf)=H(f)` and `I(yf)=I(f)+1` and explicitly recorded loss of restriction
criticality.  The present proof establishes the quantities actually needed
for GU: `U,G,B,M` are invariant under the lift.

## What the refuted helper teaches after the reduction

Let `F` be the certified five-bit activation witness and put
`H_t=yF^{otimes t}`.  Then `H_t` is balanced and

\[
L_{2,1/4}(H_t)=t(0.0923435545007156\ldots)-2.
\]

Thus the old helper fails with positive linear density even inside the
balanced class.  No `o(N)` terminal can repair it.  At `eta=1/4`, every
surviving theorem of this form must have

\[
c\ge2.067158948727793\ldots.
\]

This is only a necessary lower bound for the signed-mismatch route.  The
same five-bit witness has positive slack for GU `(4,3/4)` and does not
disprove GU or FEI.

## Failed mechanism preserved

Before changing mechanism, I iterated fresh fair activation of the exact
four-bit equality core.  The normalized requirement

\[
c_d=\frac{M+(5/4)U}{I}
\]

rose from `2` to `2.0671589487...` at depth one, then fell below `2` at
depth two and continued downward through depth ten.  Therefore repeated
activation of this fixed core does not amplify the one-node defect.  This
numerical pilot is archived in `ACTIVATION_CHAIN_PILOT.py/.out`; it prompted
the distinct tensor-plus-balancing mechanism above.  No asymptotic claim is
made from the pilot.

## Verification and parameter accounting

`CHECK_BALANCED_REDUCTION.py` exhausts all 278 Boolean signs through three
inputs.  It verifies balance and the exact lift identities for `U,I,G,B,M`,
and checks all six additive quantities for 484 disjoint tensor pairs drawn
from all signs through two inputs.

Command:

```text
python CHECK_BALANCED_REDUCTION.py
```

Output:

```text
status=PASS
boolean_signs_checked=278
lift_identity_checks=1668
tensor_identity_checks=2904
max_abs_error=0.000e+00
random_seed=None
```

The finite checker uses direct Walsh arithmetic with binary64 logarithms and
is corroborative.  The all-dimensional result is the analytic proof.

All dependence is explicit: `c` and `eta` must be absolute; the only
permitted terminal may depend on dimension but must be `o(N)`.  Bias is
removed exactly by the lift.  Tensor depth tends to infinity only after a
fixed seed dimension is chosen.  No overlap, reused physical coordinate,
activation probability, or finite maximum is assumed.

## Exact remaining obstacle and next action

No absolute `c,eta` and sublinear terminal have been proved.  The smallest
named unpaid inequality is now `BAL-SMR-o(N)`: prove it for balanced Boolean
spectra, retaining the signed aggregate `sum_i(K_i-Gamma_i)`, or construct a
balanced family with residual density unbounded for every fixed `c,eta`.

The concrete next action is to exploit `p_emptyset=0` in the balanced class
to rewrite the aggregate upper-set mismatch as a transport among nonempty
cones, allowing an `O(log N)` or other sublinear terminal, while testing the
balanced family `yF^{otimes t}` first.  A005 should audit the lift and limit;
A086 or A094 should independently reconstruct equations (3)--(8) in
`PROOF.md`.

## Execution facts

Sources actually read and immutable pins are in `SOURCE_PINS.md`.  No
protected source, paid compute, public release, scheduler mutation, email,
deployment, live-store mutation, or subagent was used.  Exposed model:
Codex; reasoning-effort metadata: UNKNOWN.  Saved, mirrored, independently
reviewed, and natively ingested are distinct; independent review and native
ingestion are not claimed.
