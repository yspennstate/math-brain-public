# account03/B03 r37 deterministic checks

Run: `20260923T173714Z-account03-B03-QFORM-r37`.

## Algebra check

For the basis notation in REPORT.md,

`v_r=alpha sqrt(c)`, `h_r=w1 sqrt(c)`,
`v_k=alpha a_k+gamma b_k`, `h_k=w1 a_k+w2 b_k`,
`alpha w2-gamma w1=m`.

Direct expansion gives

`v_r h_k-v_k h_r
 =sqrt(c)[alpha(w1 a_k+w2 b_k)-w1(alpha a_k+gamma b_k)]
 =sqrt(c)b_k(alpha w2-gamma w1)
 =sqrt(c)b_k m`.

A 10,000-sample floating-point substitution check over random admissible coefficients gave maximum absolute residual `8.881784197001252e-16`.

For

`Q=(Hbar+h_r x+h_k z)^2/a+2 sigma U(v_r x+v_k z)`,

completion in `z` was checked against

`Q=(h_k^2/a)[z+(Hbar+h_r x)/h_k+a sigma U v_k/h_k^2]^2`
`  +2 sigma U(v_r-v_k h_r/h_k)x`
`  -2 sigma U v_k Hbar/h_k-a sigma^2 U^2 v_k^2/h_k^2`.

A 10,000-sample floating-point substitution check gave maximum absolute residual below `8.7e-13` (roundoff at randomly generated scales).

## Constant check

The Case-B determinant constant is

`d_*=3/8-1/(4sqrt(6))=0.2729379273840342...`,

and `d_*>1/4` since `sqrt(6)>2`.

With `L0=sqrt(e)`, the two target-normalized constants are

`C_A=16 sqrt(3e/2)=32.30820673030729...`,

`C_B=8 sqrt(L0/d_*) (3/2)^(1/4)=21.759778868475564...`.

Thus `C_B<C_A`, and Theorem 6.1 may use the single constant `16 sqrt(3e/2)`.

The partner collision coefficient is twice this:

`2 C_A=64.61641346061458...`.

## Scope check

The proof requires exactly the existing angular packet, `2/3<c<1`, and a heavy physical coefficient in the normalized strong-complement direction, `max b_j^2>=1/2`. It does not assert that this condition follows from the bare three-large-eigenvalue hypothesis. The complement `max b_j^2<1/2` is left explicit.

No pointwise quadratic-phase decay, rotated-coordinate independence, conditional sum/difference cap, arbitrary-joint coarea bound, or moment/support regularity assumption appears in the proof.

`QFORM_B03_R37_CHECK_PASS`
