# R11 pre-code idea note — U071/U072 and C089

Track: R11 / I0054.  This note is deliberately committed before any checker code.

## New route

The apparent cubic aliasing threshold in U070 is not a genuine barrier.  Move the harmonic-grid error problem into the higher-derivative exponential-sum category.

For the compact logit multiplication map on the active interval `[1/2,4/5)`, write

\[
g(x)=\log\frac{x}{1-x},\qquad L=\log4.
\]

For every odd integer `p>=3`,

\[
g^{(p)}(x)=(p-1)!\{x^{-p}+(1-x)^{-p}\}>0.
\]

For a nonzero Fourier mode `r` of the fractional-logit coordinate, the discrete phase is

\[
\phi_N(s)=\frac{r b_N}{L}g(s/N),
\]

(up to an optional harmless linear Fourier mode in `s/N`), so

\[
|\phi_N^{(p)}(s)|\asymp_{p,r} b_N/N^p
\]

uniformly for `s/N in [1/2,4/5]`.

The standard p-th derivative van der Corput estimate, with `P=2^{p-1}`, gives for every subinterval of the active harmonic grid

\[
\frac1N\left|\sum e^{2\pi i\phi_N(s)}\right|
\ll_{p,r}
\left(\frac{b_N}{N^p}\right)^{1/(2P-2)}
+
N^{-2/P+p/(2P-2)} b_N^{-1/(2P-2)}.
\tag{1}
\]

### U071 candidate

Induct on odd `p`.  U070 is the base `p=3`.  For odd `p>=5`, split into:

* `b_N <= N^{p-3}`: then `b_N=o(N^{p-2})`, so the already-proved `(p-2)` case applies;
* `b_N>N^{p-3}`: the second term in (1) is at most
  \[
  N^{-2/P+3/(2P-2)}=o(1),
  \]
  since `P>4`, while the first term is `o(1)` whenever `b_N=o(N^p)`.

Thus, for every fixed odd `p>=3`, `b_N=o(N^p)` should suffice for the complete CTCS(infinity) finite-restriction path limit.  In particular every polynomial branch schedule `b_N=O(N^A)` is covered by choosing an odd `p>A`.

### U072 candidate: variable derivative order

The cited higher-derivative estimate states that its implied constant is independent of `p`; the explicit derivative-ratio factor can also be controlled.  On `[1/2,4/5]`,

\[
\min g^{(p)}=(p-1)!2^{p+1},\qquad
\frac{\max g^{(p)}}{\min g^{(p)}}\le (5/2)^p
\]

for odd `p`.

Let `D_N=floor(log_2 N)`.  Once possible, choose `p_N` to be the largest odd `p>=5` with

\[
2^{2p}\le D_N,
\]

and set `p_N=5` before this set is nonempty.  Define

\[
b_N=N^{p_N-2}.
\]

Then

\[
p_N=\tfrac12\log_2\log_2 N+O(1),
\qquad
P_N=2^{p_N-1}=O(\sqrt{\log N}),
\]

and the p-th derivative scale is

\[
\lambda_N\asymp_r (p_N-1)!2^{p_N}N^{-2}=N^{-2+o(1)}.
\]

Consequently both normalized terms in the p-th derivative estimate tend to zero because `log N/P_N -> infinity`; the explicit `mu^{2/P}` factor is harmless since `log mu=O(p_N)`.  This would give a genuinely superpolynomial branch hierarchy,

\[
\log b_N=\left(\frac{1}{2\log2}+o(1)\right)(\log N)(\log\log N).
\]

This is stronger than merely crossing the cubic scale.

### C089 candidate

Use exactly the U072 schedule above in the same harmonic-clock / compact-logit paintbox construction.  Fresh colors at each proposal preserve exact hidden-label lumpability.  If the Fourier error vanishes, every fixed split generator tends to the CTCS beta rate; finite-state uniformization then gives complete path total-variation convergence on every fixed visible restriction, hence finite-state J1 and the projective CTCS(infinity) limit.

For small `N`, the schedule sets `p_N=5`, hence `b_4=4^3=64`.  An exact finite witness at `N=4` will be computed only after this idea note is frozen.  It should separate C089 from source CTCS(4) and from C088 under the frozen relabeling/global-rescaling convention.

## Methods actually being used

* **#1 CHANGE THE CATEGORY:** the cubic-grid question becomes a higher-derivative exponential-sum problem.
* **#18 SAY IT IN ANOTHER LANGUAGE:** discrete split-rate convergence is rewritten as weighted Fourier/Weyl cancellation of fractional logit phases.
* **#19 MAKE IT AN ALGORITHM:** the variable-order rule `p_N`, followed by `b_N=N^{p_N-2}`, is an explicit deterministic compiler rather than an existence argument.

## Proof obligations before promotion

1. State and apply the p-th derivative estimate with all exponents correct.
2. Use bounded-variation partial summation to pass from unweighted exponential sums to the smooth harmonic-clock weight.
3. Use finite Fourier approximation in the fractional-logit coordinate; treat the active-interval endpoints separately.
4. Prove U071 by odd-p induction and U072 with the variable-order estimates above.
5. Prove the full finite-generator -> whole-path TV -> J1/projective limit implication, not a marginal limit.
6. Produce an exact rational `N=4` non-equivalence certificate for C089 and execute an exact checker.
7. Keep source status PARTIAL absent the required two outside audits and because `operations/claims/I0054.md` remains `PENDING_ADMISSION, not READY`.
