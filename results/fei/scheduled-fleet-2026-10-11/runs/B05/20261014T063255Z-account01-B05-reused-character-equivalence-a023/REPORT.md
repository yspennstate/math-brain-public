# B05 / A023 — reused balancing character is universal activation in disguise

**Run:** `20261014T063255Z-account01-B05-reused-character-equivalence-a023`  
**Primary packet:** A023  
**Stable gap:** `GU-ASYMMETRY-MISMATCH`  
**Claim version:** `B05-A023-REUSED-CHARACTER-EQUIVALENCE-v1`  
**Status:** **PROVED route obstruction pending independent review**  
**Full FEI:** **OPEN**

## Frozen candidate and prior bound

The preceding accepted proper-class transfer uses two fresh signs:
\(\mathcal T(q)=A(yq)\), and for \(c\ge3/2+\eta\),

\[
L_{c,\eta}(\mathcal T(q))\le\frac12L_{c,\eta}(q),
\qquad L_{c,\eta}=M+(1+\eta)U-cI.
\]

This run tested the next mandated hypothesis removal: replace the fresh
balancing sign \(y\) by one existing physical coordinate \(x\), keeping only
the selector fresh.

## Result

The substitution does not produce a broader proper class. Multiplication by
\(x\) is an involution on Boolean functions, so

\[
\{A(xq):q\text{ Boolean}\}=\{A(r):r\text{ Boolean}\}.
\]

After closing under the selector restriction, this family contains every
Boolean function. Therefore an all-core, restriction-closed reused-character
extension is already universal GU rather than an intermediate A023 theorem.

`PROOF.md` also derives the complete signed surcharge. With
\(W_x(q)=U(xq)-U(q)\),

\[
L(xq)-L(q)=\mathcal D_xW(q)+(1+\eta)W_x(q)
-c(1-2\operatorname{Inf}_x(q)),
\]

and substitution into the accepted activation recurrence gives equation (8)
there. This is the precise smaller unpaid inequality; it keeps the whole
physical Fourier slice and every terminal term.

The former half-contraction cannot survive reuse. For \(q=x\), one has
\(xq=1\), \(A(xq)=1\), and

\[
L(A(xq))-\frac12L(q)=\frac c2>0
\]

for every \(c>0\) and every \(\eta\). This refutes only the direct transfer
template, not cone preservation, GU, or FEI.

## Before/after scope

- Before: fresh \(y,z\), exact half-contraction, arbitrary changing core.
- After: removing freshness of \(y\) is proved equivalent to unrestricted
  activation over arbitrary cores; the exact additional signed slice term is
  isolated; universal half-contraction is refuted.
- Remaining viable target: prove the weaker cone-preserving inequality
  \(L(A(xq))\le0\) under \(L(q)\le0\), with a zero terminal reserve, first on
  one nontrivial restriction-closed class. Any universal arbitrary-core
  version must be treated as a universal GU candidate and independently
  reviewed as such.

## Verification

`CHECK.py` uses exact rational Walsh coefficients. It exhausts all 276
Boolean functions through three inputs and all 804 coordinate choices,
checking involution/surjectivity, \(B\)-invariance, the influence identity,
and the signed \(G\)-drift identity. It also checks the exact character
falsifier for three positive values of \(c\).

Command: `python CHECK.py`

```text
status=PASS
boolean_cores_checked=276
coordinate_checks=804
signed_identity_checks=2412
half_contraction_exact_witness_checks=3
max_float_identity_error=0.000e+00
```

The proof is analytic; computation is corroborative. Independent A087/A094
review and native Brain ingestion are not claimed.
