# B01 / A004 — all-eta reused-activation cone wedge

**Run:** `20261014T071439Z-account01-B01-reused-cone-wedge-a004`  
**Primary packet:** A004, constant and unit ledger  
**Stable gap:** `GU-ASYMMETRY-MISMATCH`  
**Claim:** `B01-A004-REUSED-CONE-WEDGE-v1`  
**Status:** **PROVED PARAMETERIZED ROUTE OBSTRUCTION, PENDING INDEPENDENT REVIEW**  
**Universal GU / full FEI:** **OPEN**

## Exact candidate and GU implication

The candidate sufficient estimate is

\[
M(f)+(1+\eta)U(f)\le cI(f),\qquad 0<\eta\le1. \tag{SMR}_{c,\eta}
\]

The source-checked reduction writes `G=B+M`, uses `B<=H` and
`H<=2(I-Var)+2U`, and obtains

\[
G\le(c+2)I+(1-\eta)U-2\operatorname{Var}.
\]

Hence `SMR(c,eta)` would prove GU with
`(a,b)=(c+2,1-eta)` and FEI constant
`2+2(c+2)/eta`.  No such universal pair is proved here.

## Mathematical delta

B19 had exactly certified one failure at `(c,eta)=(7/4,1/4)` for the
four-bit mask `10049` followed by multiplication by coordinate `3` and fair
activation.  This run derives its entire parameter region.

For the child `q` and activated output `F`,

\[
L_{c,\eta}(q)\le0\iff c\ge c_q(\eta)=\frac{23}{16}+\eta,
\]

while

\[
L_{c,\eta}(F)\le0\iff
c\ge c_F(\eta)=1.505684707963186\ldots
+1.336806053967517\ldots\eta.
\]

The exact affine difference is positive for every `eta>=0`:

\[
c_F-c_q=D_0+D_1\eta,
\]

\[
176D_0=\log_2\frac{2^{907}3^{360}}
 {5^{180}13^{208}17^{68}}>0,
\qquad
88D_1=\log_2\frac{2^{160}}{3^9 5^{50}}>0.
\]

Therefore every GU-relevant `0<eta<=1` has a nonempty interval

\[
c_q(\eta)\le c<c_F(\eta)
\]

on which the child residual is paid but fair activation produces a positive
residual.  Reused-coordinate zero-cone induction fails throughout this
wedge.  Moreover, the output `F` alone proves that any universal
`SMR(c,eta)` theorem must have `c>=c_F(eta)`.

This is a strict extension from one parameter point to an all-eta affine
wedge.  It does not rule out larger `c`; in particular `(2,1/4)` remains
outside the obstruction.

## Verification

`CHECK_WEDGE.py` uses exact rational Walsh arithmetic and rational
prime-exponent entropy expressions.  `CHECK_WEDGE.out` records the exact
threshold coefficients and integer-product sign certificates.  No floating
sign is used in the proof.

## Remaining obstacle and next action

The unpaid universal leaf remains: prove `SMR(c,eta)` for some finite `c`
and `eta>0`, or replace it by a smaller signed aggregate estimate.  The next
bounded test should tensor or rare-suspend the exact `F` witness while
retaining the terminal reserve, to determine whether the lower bound
`c_F(eta)` amplifies or stays finite.  A finite wedge is not a GU or FEI
counterexample.

Fresh independent review is required from A086 or A090 because B19
contributed the seed witness and B01 derived the parameter extension.
