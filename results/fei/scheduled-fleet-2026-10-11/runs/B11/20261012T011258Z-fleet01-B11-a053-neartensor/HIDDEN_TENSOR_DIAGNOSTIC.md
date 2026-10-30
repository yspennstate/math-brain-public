# Hidden-tensor diagnostic for A053

The frozen structural test is full physical descendant-criticality for the
ordinary Fourier ratio `R=H/I`.  The new theorem proves that this test detects a
low-ratio tensor factor even after a small Boolean surgery.

For any tensor `T=u(x_A)h(x_{A^c})` and any descendant-critical `f` at Hamming
density `epsilon` from `T`,

`R(f)(I(u)-2|A|epsilon) <= H(u)+2h2(2sqrt(epsilon))+(2N-|A|)2sqrt(epsilon)`.

The interface is explicit and independent of the desired conclusion.  Its
three costs are:

1. the signed Fourier-law perturbation, retained as
   `2 a_S d_S+d_S^2` before taking absolute values;
2. the full parent/child spectral entropy continuity cost;
3. at most `2|A|epsilon` physical influence transport.

For the six-bit point-defect factor `phi`, exact Walsh arithmetic gives
`I(phi)=3/16` and the analytic estimate `H(phi)<1449/2048`.  Thus any
descendant-critical source with ratio above four must be farther than
`1/(2^18 N^2)` from `phi tensor h`.

This separates three notions that must not be conflated:

- exact tensor factorization is detected algebraically;
- tensor primitivity only says that at least one rectangle fails on each
  partition;
- descendant-criticality quantitatively excludes a whole Hamming
  neighborhood of a low-ratio tensor manifold.

The one-point-surgery family is tensor-prime, but across each original
whole-factor partition its rectangle-defect probability is at most
`4*2^{-N}`.  Hence visual connectedness or qualitative primitivity supplies no
dimension-independent curvature.  Full ratio criticality does: for the
ordinary `H/I` ratio it excludes the family for `N=6m`, `m>=5`.

The theorem does not exclude near tensors all of whose factors have ratio near
the critical root ratio.  Equal-ratio critical tensors remain exact controls.
The next live problem is to extract a low-ratio physical factor, or a paid
interface, from an arbitrary tensor-prime descendant-critical source.

