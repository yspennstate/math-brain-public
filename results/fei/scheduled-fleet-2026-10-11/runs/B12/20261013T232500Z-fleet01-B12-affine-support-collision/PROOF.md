# Affine-support collision theorem

For a real function `r` on the Boolean cube, write

\[
 \mathcal E(r)=\sum_S\widehat r(S)^2
 \log_2\frac1{\widehat r(S)^2},\qquad
 \mathcal I(r)=\sum_S|S|\widehat r(S)^2.
\]

The previous A058 run showed that an arbitrary support mask can admit a
signing with smaller raw Fourier entropy.  That destroys the natural complete
shared-coordinate telescope.  This run changes mechanism: it identifies the
exact support geometry for which that entropy concentration is impossible.

## Theorem 1: affine masking pays the collision exactly

Let `A` be any affine subspace of `F_2^n` of codimension `r`, let
`q=1_A`, and put `p=2^{-r}`.  For every Boolean `F`,

\[
 \boxed{\mathcal E(Fq)\le H(F)+\mathcal E(q)
       =H(F)+2rp.}
\]

### Proof

Let `L` be the annihilator of the direction space of `A`; `|L|=2^r=1/p`.
Partition the Fourier cube into cosets `C` of `L`.  On one coset write

\[
 e_C=\sum_{S\in C}\widehat F(S)^2,
 \qquad
 y_C=\sum_{S\in C}\widehat{Fq}(S)^2.
\]

Convolution by `qhat` is the rank-one character projection on each coset.
Consequently every coefficient of `Fq` in `C` has the same squared magnitude
`p y_C`, and

\[
 0\le y_C\le e_C,qquad \sum_Ce_C=1,qquad \sum_Cy_C=p.
\]

It follows that

\[
 \mathcal E(Fq)=\sum_C\bigl[y_C\log_2(1/y_C)+r y_C\bigr]
 =\mathcal E(y)+rp.
\]

Put `rho_C=y_C/p`.  If `p<1`, put
`sigma_C=(e_C-y_C)/(1-p)`.  Then `e=p rho+(1-p)sigma`, so concavity of
Shannon entropy gives

\[
 H(e)\ge pH(\rho)+(1-p)H(\sigma)\ge pH(\rho).
\]

Therefore

\[
 \mathcal E(y)=pH(\rho)+p\log_2(1/p)
 \le H(e)+rp\le H(F)+rp.
\]

Combining the last two displays proves the claim.  The cases `p=0,1` follow
directly.  Finally, `qhat` has `2^r` coefficients of magnitude `p`, hence
`E(q)=2rp`.

## Theorem 2: affine support prevents signed entropy concentration

Let `b` be any real function supported on `A` with `|b|=q`.  Then the squared
Fourier magnitudes of `b` are constant within every coset of `L`.  If `rho`
is their normalized coset-energy law, then exactly

\[
 \boxed{\mathcal E(b)=2rp+pH(\rho)\ge2rp=\mathcal E(q).}
\]

Thus for every Boolean realization `F=a+hb` (so `hb=Fq` pointwise),

\[
 \boxed{
 \widetilde J=H(F)-\mathcal E(hb)+\mathcal E(b)
 \ge \mathcal E(b)-\mathcal E(q)\ge0.}
\]

This is precisely the endpoint nonnegativity that failed for the six-point
non-affine support in the preceding run.  Coordinate restriction preserves
affine support (or makes it empty), so this class is restriction hereditary.

## Theorem 3: a sharp physical-influence payment

Assume every physical coordinate is transverse to `A`: flipping any one
coordinate moves `A` to a disjoint parallel coset.  For every signing `b` as
above,

\[
 \mathcal I_i(b)=p/2,qquad \mathcal I(b)=np/2.
\]

There are `2^{n-r}` annihilator cosets, so `H(rho)<=n-r`.  Theorem 2 gives

\[
 \mathcal E(b)\le2rp+p(n-r)=p(n+r)\le2pn=4\mathcal I(b).
\]

Hence

\[
 \boxed{\mathcal E(b)\le4\mathcal I(b).}
\]

The constant `4` is sharp: a one-point support has
`E(b)=4 I(b)`.  The theorem is uniform in ambient dimension, codimension,
support density, overlap count, and the signing on `A`.  Transversality is
also preserved by every nonempty physical-coordinate restriction.

This supplies a genuine shared-variable collision/source ledger for affine
disagreement supports.  It does not by itself close the full adaptive
hierarchy: the remaining root term can still contain terminal output entropy,
and a universal function need not have affine disagreement support.

## Exact falsifier outside the class

The natural attempted extension

\[
 \mathcal E(Fq)\le H(F)+\mathcal E(q)
\]

is false for arbitrary indicators.  Load the corrected X007 seven-bit
Boolean `F` and take `q` to be the complement of its one-point-defect
multiplier.  The exact Walsh numerator histograms are

\[
\begin{array}{c|c}
F&2^{60},6^{48},26^{16},30^4\\
Fq&3^{60},7^{48},25^{16},29^4\\
q&1^{127},127^1.
\end{array}
\]

They give

\[
 H(F)+\mathcal E(q)-\mathcal E(Fq)
 =-0.122617694991922\ldots<0.
\]

The sign is certified by exact integer comparison.  After multiplication by
`128^2`, the prime-log exponent vector is

\[
\{2:196608,3:-9576,5:32800,7:4704,
 13:-21632,29:6728,127:-32258\}.
\]

The product from the positive exponents is strictly smaller than that from
the negative exponents.  Any repair of the form `+c H(2q-1)` needs
`c>=0.294682136281410...` on this witness alone.

Full FEI remains **OPEN**.
