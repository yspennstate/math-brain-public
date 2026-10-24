# Independent review of `B11-A052-DEGREE-TWO-EXTREMAL-v1`

## Frozen statement

For every finite uniform cube and every Boolean sign of Fourier degree at
most two,

\[
G(f)\le 2I(f),\qquad H(f)\le 2I(f).
\]

Consequently a dimension-minimal positive-residual counterexample to
\(G\le4I+3U/4\), if one exists, has degree at least three.

## Verdict

**PASS at the stated restricted scope.**  No material repair is needed.
Universal GU and full FEI remain open.

## Line-by-line reconstruction

1. Fourier degree equals the degree of the unique multilinear real
   polynomial on the cube.  The Nisan--Szegedy junta theorem gives at most
   \(d2^{d-1}\) relevant variables, hence at most four for \(d=2\).
2. Adding or removing dummy variables leaves \(p,\pi,U,I,G,H\) unchanged.
   This was checked directly for all 111 four-bit representatives after
   adding a fifth dummy variable (444 independent identities).
3. Global output sign leaves the squared spectrum and every quantity above
   unchanged, so fixing one truth-table value to +1 covers all functions.
4. Independent integer Walsh enumeration of all \(2^{15}\) representatives
   gives exactly 111 functions with no level-three or level-four
   coefficient.
5. The author's rational certificate was audited at the arithmetic level.
   Its upper-set zeta transform is correct; restrictions preserve the order
   of the remaining bits; `G=nU-sum_i E U(child)` matches the definition.
   The factorization of every rational logarithm into powers of 2 and odd
   primes is exact.  The atanh partial sum is below `ln(m)`, and its displayed
   geometric tail bounds the omitted positive series.  Division by the
   independently enclosed positive `ln(2)` uses the correct endpoint in all
   three sign cases.  Thus the reported signs are rigorous, not floating
   decisions.
6. A separate implementation using integer Walsh numerators and 100-digit
   logarithms reproduces 25 equality and 86 strict cases for each inequality,
   with minimum positive slacks 2 and 1 respectively.  These large gaps also
   independently guard against a boundary ambiguity in the interval code.
7. For the frozen residual
   \(R=G-4I-3U/4\), the class theorem gives
   \(R\le-2I-3U/4<0\) for every nonconstant degree-two function.  If a
   universal counterexample exists, minimum dimension exists because every
   Boolean function is finite-dimensional.  For a relevant coordinate,
   every child has smaller dimension and
   \[
   R(f)-\mathbb E R(f_{i,\pm})
    =\Delta_iG-4\operatorname{Inf}_i-\tfrac34\Delta_iU.
   \]
   Since the child residual average is nonpositive, the claimed critical
   child inequality follows.  Tensor-prime reduction is not needed for the
   degree exclusion itself.

## GU-to-FEI implication checked from the source reduction

On a restriction-closed class satisfying `G<=aI+bU`, assume inductively
`U<=cI` on every proper restriction.  With `m` relevant coordinates,

\[
\sum_i\mathbb E U(f_{i,\pm})=mU-G,
\qquad
\sum_i\mathbb E I(f_{i,\pm})=(m-1)I.
\]

Taking \(c=a/(1-b)\) gives

\[
(m-b)U\le[c(m-1)+a]I=c(m-b)I,
\]

so \(U\le aI/(1-b)\).  Together with the reviewed Boolean-granularity
bound \(H\le2(I-\operatorname{Var})+2U\le2I+2U\), this yields

\[
H\le\left(2+\frac{2a}{1-b}\right)I.
\]

For the degree-two class, `(a,b)=(2,0)` therefore gives `U<=2I` and the
generic `H<=6I`; the direct certificate validly improves the latter to
`H<=2I`.

## First unsupported universal line

The review does not supply any estimate for degree at least three.  The
first unsupported universal line remains the quantitative high-degree row
cut

\[
D_{\ge2}+\tfrac12V_1
\le \left(4-\frac2{\ln2}\right)I+\frac34U
   +\frac2{\ln2}Q_{\ge3}
\]

on tensor-prime positive-residual Boolean functions.  Merely knowing that a
counterexample has one nonzero coefficient of degree at least three gives no
uniform lower bound on \(Q_{\ge3}\), so the reviewed theorem cannot close
this line.

## Source pins

- Author report blob: `3b9e92745954e94ae1e5eb3c71cdff10412ef62e`.
- Author proof blob: `68e7b1dfe5ad019ccdbdad23670f47b1bfaf93e4`.
- Author verifier blob: `66f5ac9203526d7fe6ffb660dd32b7316903a787`.
- Author output blob: `ea326a82f1ad7c8ebf7a8afdbf3936373b4b911a`.
- Nisan--Szegedy, *Computational Complexity* 4 (1994), DOI
  `10.1007/BF01263419`; the theorem states dependence on at most
  \(d2^{d-1}\) variables.
- Restriction-induction source checked in
  `B01/20261013T092317Z-account01-B01-partial-star-defect-gu-a003/`
  (`PARTIAL_STAR_DEFECT_GU.md`, blob
  `75acb37f53ec75be5f1496b776d60cad1afecd9b`).

