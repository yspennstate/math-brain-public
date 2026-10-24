# B19 / A094 independent review — balanced-preconditioned activation

**Run:** `20261014T054525Z-account01-B19-balanced-preconditioned-review-a094`  
**Primary packet:** A094, proof-chain challenger  
**Reviewed claim:** `B05-A023-BALANCED-PRECONDITIONED-ACTIVATION-v1`  
**Stable gap:** `GU-ASYMMETRY-MISMATCH`  
**Verdict:** **ACCEPTED AT DECLARED PROPER-CLASS SCOPE**  
**Full FEI:** **OPEN**

## Exact candidate, quantifiers, and prior status

For every genuine Boolean \(q\), fresh independent uniform signs \(y,z\),
every \(0<\eta\le1\), and every \(c\ge3/2+\eta\), define

\[
\mathcal T(q)(z,y,x)=1\quad(z=+1),\qquad
\mathcal T(q)(z,y,x)=yq(x)\quad(z=-1).
\]

With

\[
L_{c,\eta}=M+(1+\eta)U-cI,\qquad M=G-B,
\]

the audited claim is

\[
L_{c,\eta}(\mathcal T(q))\le\frac12L_{c,\eta}(q). \tag{T}
\]

Before this claim, the exact fair-activation recurrence was accepted, but
the sharp helper \(L_{2,1/4}\le0\) had been refuted by a genuine five-bit
Boolean function.  B05 proposed (T) as a replacement transfer using a fresh
balancing character.

## Independent reconstruction

`PROOF_AUDIT.md` reconstructs every step.  Multiplication by \(y\)
relabels the Fourier support, preserving \(U,G,B,M\) and increasing
\(I\) by exactly one.  The balanced core \(yq\) has only the singleton
coefficient \(\widehat{yq}(\{y\})=m=\mathbb E q\).  Substitution into
the accepted signed activation identity gives

\[
L_{c,\eta}(\mathcal T(q))-\frac12L_{c,\eta}(q)
=d(m)+1+\eta-c,
\]

where

\[
d(m)=R(0)-\frac{R(m)+R(-m)}2-\frac12T(1,m^2).
\]

The scalar proof is correct:

\[
d(m)\le\frac{m^2}{2}\le\frac12.
\]

The balancing-coordinate and selector influence debits contribute separate
halves of the total \(-c\); no credit is reused.

## GU consequence

The residual is output-sign invariant and additive on disjoint products.
Thus any base class with \(L\le0\) remains admissible under disjoint
products and repeated fresh applications of \(\mathcal T\).  At
\(\eta=1/4,c=7/4\),

\[
M+\frac54U\le\frac74I.
\]

Using the original proved bridge
\(H\le2(I-\operatorname{Var})+2U\), this gives

\[
G\le\frac{15}{4}I+\frac34U-2\operatorname{Var}
\le\frac{15}{4}I+\frac34U.
\]

This is an explicit \((a,b)=(15/4,3/4)\) pair on the generated class only.

## Adversarial scope checks

Revealing the balancing input produces \(A(q)\) or \(A(-q)\), the
unbalanced activation excluded by (T).  Therefore the class is not
restriction-closed and the source GU induction cannot convert this
proper-class bound into \(U\le15I\) or an FEI constant.

The result also retains:

- two fresh uniform physical inputs at every activation;
- disjointness for product closure;
- an already-paid child residual \(L(q)\le0\).

It does not cover biased selectors, reused coordinates, overlapping cores,
or arbitrary leaves with unpaid residuals.  “Changing core” is valid only
in this inherited-residual sense.  This scope is already stated in the
producer proof, so no repair was required and this review remains
independent.

## Independent computation

`REPRODUCE.py` does not import the producer checker.  It reconstructs Walsh
coefficients directly from character sums, recomputes \(U,I,G,B,M\) from
truth tables, and checks physical restrictions and tensor additivity.

Command:

```text
python3 REPRODUCE.py
```

Output:

```text
status=PASS
scalar_checks=500001
boolean_cores_checked=1302
transfer_identity_checks=1302
physical_restriction_checks=12404
product_additivity_checks=256
max_identity_error=1.332e-14
max_transfer_residual=-0.403940979960974
max_scalar_gap=0.000e+00
max_scalar_gap_h=0.00000000
seed=202610140544
```

The all-dimensional result is analytic; floating evaluation is only
corroborative.

## Mathematical delta and next unpaid step

The B05 claim advances from author-proved to one independent acceptance at
its exact proper-class scope.  It removes arbitrary core bias and internal
core structure from a fresh balanced activation node, with constants
independent of dimension and depth.

The universal gap is unchanged: a fresh balancing character cannot be
replaced by a reused physical coordinate, and its two restriction children
are uncontrolled unbalanced activations.  The next action for A087/A090 is
to test the proposed reused-coordinate replacement against the accepted
A025 degree-shift counterfamily while retaining the complete signed
slice charge.

No second end-to-end GU review exists, native ingestion is not claimed, and
full FEI remains open.
