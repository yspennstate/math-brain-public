# B11 / A053 — critical separation from low-ratio near tensors

**Run:** `20261012T011258Z-fleet01-B11-a053-neartensor`  
**Primary packet:** A053 (Near-tensor perturbations)  
**Attempt:** `A053-HI-NEARTENSOR-1`  
**Claim:** `B11-A053-HI-NEARTENSOR-SEPARATION-v1`  
**Gap:** `G-CRITICAL-NEARTENSOR`  
**Status:** structural theorem PROVED; independent review pending; full FEI OPEN.

## Frozen target and prior value

The previous A052 work proved that descendant-criticality makes
`Delta_i H-R I_i` the influence-weighted child-ratio loss.  It also proved
purity for exact critical tensor products.  Its precise remaining near-tensor
question was whether a tiny Boolean surgery can hide an arbitrary tensor core
while retaining true ratio criticality.  Qualitative tensor primitivity was
already known to be insufficient.

This run selects A053 and freezes the ordinary Fourier ratio `R=H/I`, actual
uniform physical restrictions, Hamming perturbation density `epsilon`, and the
factor block `A`.  No modified potential or non-Boolean spectral law is used.

## New theorem

Let `f` be a genuine Boolean function on `N` uniform physical bits and suppose
every nonconstant physical descendant `g` satisfies `R(g)<=R(f)=R`.  Let

`T(x_A,x_{A^c})=u(x_A)h(x_{A^c})`

with `|A|=a`, and suppose `Pr[f!=T]=epsilon<=1/16`.  Put
`t=2 sqrt(epsilon)`.  Then

\[
\boxed{
R\bigl(I(u)-2a\varepsilon\bigr)
\le H(u)+2h_2(t)+(2N-a)t.}
\]

When `2a epsilon<I(u)`, this gives the explicit ratio cap

\[
R\le\frac{H(u)+2h_2(2\sqrt\varepsilon)
 +(2N-a)2\sqrt\varepsilon}{I(u)-2a\varepsilon}.
\]

Thus full descendant-criticality, unlike primitivity, quantitatively detects a
low-ratio tensor factor after a small surgery.

## Proof and signed perturbation ledger

Write `d=f-T`.  Before taking absolute values, the exact signed Walsh identity
is

\[
\widehat f(S)^2-\widehat T(S)^2
=2\widehat T(S)\widehat d(S)+\widehat d(S)^2.
\]

Parseval gives `sum_S dhat(S)^2=4 epsilon`; factoring the difference of
squares gives spectral total variation at most `2 sqrt(epsilon)=t`.  The sharp
finite-alphabet entropy-continuity modulus, averaged over physical restriction
branches, gives

\[
|\Delta_AH(f)-\Delta_AH(T)|
\le2h_2(t)+(2N-a)t.
\]

The pivotality indicators for coordinate `i` can differ only if one endpoint
of the edge lies in the disagreement set, so
`|I_A(f)-I_A(T)|<=2a epsilon`.

Descendant-criticality is used at one exact line:

\[
\mathbb E_z H(f_{A=z})\le R\mathbb E_z I(f_{A=z}),
\qquad \Delta_AH(f)\ge R I_A(f).
\]

For the tensor, `Delta_AH(T)=H(u)` and `I_A(T)=I(u)`.  Combining the three
displayed relations proves the theorem.  The complete derivation is in
`NEAR_TENSOR_PERTURBATIONS.tex`.

## Explicit six-bit factor and polynomial exclusion radius

Let `phi` be the six-bit one-point defect.  Exact Walsh arithmetic gives

\[
I(\phi)=\frac3{16},\qquad
H(\phi)=\frac{961}{1024}\log_2\frac{1024}{961}
       +\frac{630}{1024}.
\]

Using `log(1+x)<=x` and `ln 2>2/3`,

\[
H(\phi)<\frac{1449}{2048},\qquad
4I(\phi)-H(\phi)>\frac{87}{2048}.
\]

It follows that every descendant-critical `f` with `H(f)/I(f)>4` satisfies

\[
\Pr[f\ne\phi h]>\frac1{2^{18}N^2}
\]

for every placement of the six-bit factor and every Boolean complementary
factor `h`.  The constants are deliberately conservative and fully analytic.

## Quantified primitivity control

For `T_m=phi^{tensor m}` on `N=6m` bits, flip one truth-table value to obtain
`G_m`.  The existing multiplicative-rectangle proof shows `G_m` is tensor-prime
for every `m>=3`.  Across each original whole-factor partition, however, its
normalized rectangle-defect probability is positive but at most `4*2^{-N}`.
So qualitative primitivity can be caused by an exponentially small interface.

For `m>=5`, `2^{-6m}<=1/(2^18(6m)^2)`.  The theorem therefore proves that
`G_m` is not descendant-critical with ordinary Fourier ratio above four.  This
does not refute FEI; it excludes this near-tensor obstruction family from a
hypothetical high-ratio critical class.

## Controls and limitations

- Equal-ratio critical tensors remain exact controls and are not excluded.
- The theorem does not extract a low-ratio factor from an arbitrary prime
  critical source.
- The one-point-surgery family has Shannon `H/I` tending to four; it is not an
  FEI counterexample.
- No raw hidden-curvature sum is bounded.  The paid quantity is the actual
  physical block entropy/influence comparison.
- The theorem uses actual Boolean truth tables throughout; no arbitrary
  spectral probability law is admitted.

## Verification

Command: `python3 verify_neartensor.py`.

The checker uses integer Walsh transforms and exact `Fraction` arithmetic for
the point-defect spectrum, influences, rational gap, continuity-budget
majorants for `6<=N<=256`, and the surgery-radius comparison for `5<=m<=40`.
It passed 865 assertions with no randomness.  Floating entropy values are
diagnostic only; the all-dimensional theorem and radius are analytic.

## Sources actually used

- Current B11 contract blob `faaa0875ddb129d134bb62abb513f3795e88b590`.
- Execution protocol blob `457358ff62cbf1141a72096bcabdf95bf18c1be2`.
- A052 critical-slack report blob
  `9f0d4ec16e611bc845c92b6b2173b0eae7d34ac7` and theorem blob
  `33850b3519c3e04e8ea1e59eef7d7d8ffe956b8a`.
- Historical ratio-critical near-tensor report blob
  `f72df6ef58bd07f99d9d4f39b0104b7077c354e4`; its entropy-continuity proof
  was reconstructed here for the ordinary `H/I` ratio.
- Primitive surgery source blob
  `000f6250c095d5a40870c6cfc3fabaf8f07c8d0e` for the rectangle certificate.

No novelty claim relative to unsearched literature is made.  This is a
source-bound campaign lemma.

## Remaining obstacle and routing

The exact unpaid step is to show that every tensor-prime descendant-critical
source with large ratio exposes a low-ratio physical factor/interface, or to
construct a genuine prime critical family avoiding all such block tests.
Route to A022, A054, A055, A090, A094, A096 and B20.  Independent acceptance
has not been performed.

Persistence receipts are recorded in `PROGRESS.json` after delivery.  Full FEI
remains OPEN.

