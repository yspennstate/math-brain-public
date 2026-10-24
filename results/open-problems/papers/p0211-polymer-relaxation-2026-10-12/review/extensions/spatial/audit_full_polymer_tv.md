# Independent audit of the arbitrary-start polymer TV argument

Audited on 12 October 2026 against `07_stronger_sector_certificate.tex`, `08_count_lyapunov_smoothing.tex`, and `09_full_polymer_tv_upper.tex` in `polymer_extensions/tv/`, together with the stationary estimates in `02_count_theorem_and_stationarity.tex`.

**Result: the argument passes.** For fixed (b>0), it proves the claimed upper bound

\[
 t_{\rm mix}^{M}(\varepsilon)
 \le C_b\sqrt n\bigl((\log n)^2+\log(1/\varepsilon)\bigr),
 \qquad \beta=b/n,
\]

for sufficiently large (n). The logarithmic gap from the endpoint lower bound remains; this is not a proof of worst-case cutoff.

## Sector certificate

The ratios of (h_\ell(k)=1/(k+A)_\ell), (A=\sqrt{bn}), yield precisely the three nonnegative terms displayed in file 07. For (k\le A), the allowed range (\ell\le k) gives (n-k-\ell\ge n/2) and (k+A+\ell\le3A). For (k\ge A\ge2), ((k-1)/(k+A-1)\ge1/3). Therefore the lowest rate in degree (\ell) is at least (\ell\sqrt\beta/6). All missing endpoint terms have zero coefficients.

## Count smoothing

The exact quotient for (V=(p(r)/p)^{3/4}) is correct at both endpoints. The algebraic inequality between its principal negative part and (W=(\sqrt\lambda-\sqrt\mu)^2) is valid. The first coefficient error is (O_b(A^{-1})) for (k\le2A) and at most (W/4) in the remaining range for sufficiently large (n). The second error is (O_b(A^{-1})) uniformly, including the vanishing birth rate at (k=n).

The stationary-weight comparison (\log V\le C_b(1+AW)) is justified centrally by the exact drift zero and the Gaussian ratio estimate; below (A/2), (W\ge c_b) and the total log-weight cost is (O_b(A)); above (2A), summing consecutive weight ratios costs at most (C_b k^2/A), while (AW\ge c_b k^2/A). The logarithmic singularity near (k=n) contributes only (O(n)) after summation.

Jensen's inequality applies to (x\log x), giving exponential decay of (\log\mathbb E V) at rate (c_b/A). The resulting uniform bound on (\mathbb E V) after (C_bA\log n) implies (q(k)\le C_b(p(k)/p(r))^{3/4}). The previously proved Gaussian/geometric tails yield (p(r)\asymp_b A^{-1/2}) and (\sum\sqrt p\le C_bA^{1/4}). Thus the density norm (M=\sum q^2/p\le C_bA) follows with the correct exponent.

## Positivity compression and Nash inequality

On a cardinality layer, the orthogonal projector onto degree (\ell) has constant diagonal (d_\ell/\binom nk); this follows from permutation invariance and the trace. Positive semidefiniteness bounds every absolute kernel entry by the same diagonal. Positivity of the lifted density then gives

\[
 \|P_\ell F\|_2^2\le d_\ell\sum_kp(k)\overline F(k)^2.
\]

The telescoping sum of dimensions is (\binom nd). No invariance of the polymer density under the cut semigroup or an individual harmonic projection is needed.

For the actual polymer density, reversibility and the stationary energy identity give (R'=-2\mathcal E_M=-2\mathcal E_B). Applying the degree lower bound only to this instantaneous energy proves the differential inequality in file 09. The separate estimate (R\le2^nM_*) is also valid by positivity on each layer.

When (R>16M_*n^2), the chosen (d=\lfloor\log(R/M_*)/(2\log n)\rfloor) is an allowed nonterminal degree for large (n), and the low-degree mass is at most (R/4). The resulting differential inequality reduces (R) to a polynomial threshold within (2g^{-1}(\log n)^2). Ordinary spectral-gap decay then supplies the stated (\varepsilon) dependence. All constants may depend on fixed (b), as the theorem permits.

No correction was required. This audit verifies the mathematical deductions in these files; it is not a priority claim for the resulting mixing bound.
