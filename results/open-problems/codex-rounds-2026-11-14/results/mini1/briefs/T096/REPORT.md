VERDICT: PROVED external fields can arbitrarily reduce the heat-bath spectral gap of a frustrated triangle

For the three-spin law

\[
 \mu_{K,b}(x)\propto
 \exp\{-K\sum_{i<j}x_ix_j+b\sum_i x_i\},
\]

the rate-one-per-site heat-bath gap at zero field is exactly
γ(K,0)=1−½tanh(2K)≥1/2. At uniform field b=K the gap is less than 9/[2(1+e^{2K})]. Therefore γ(K,K)/γ(K,0)<9e^{−2K}. A uniform field can make this fixed-size frustrated system much slower.

The exact field gap is also derived in [PROOF.md](PROOF.md). At K=log 2 it is (72−√1765)/65≈0.461355337305, compared with the zero-field gap 19/34≈0.558823529412. Both discrete uniform-site gaps are these numbers divided by three. A separate no-jump argument gives a continuous-time worst-start mixing lower bound exceeding (1+e^{2K})log(12/7)/3.

This rules out the general shortcut that zero field always minimizes the heat-bath gap, and even a comparison up to an absolute constant independent of the interactions. The strict example persists on a positive-probability neighborhood for three-spin Gaussian disorder. It does **not** contradict the SK conjecture, give a new interval of β, or establish an obstruction for typical disorder as n grows. No novelty claim is made for the small-system calculation.

Reproduction:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 nice -n 15 python3 check_triangle.py > triangle_output.txt 2>&1
```

The final run passed in approximately 0.56 seconds, using 68,583,424 bytes peak RSS. The sandbox denied the `nice` adjustment; the process checked that it inherited nice=20, already below the requested priority. The calculation used one thread, no GPU, and matrices of order eight.

Artifacts: [proof](PROOF.md), [verification script](check_triangle.py), [full output](triangle_output.txt), [numerical data](triangle_data.csv), [exact characteristic polynomials](triangle_exact.json), and [work log](LOG.md). All eight eigenvalues in both fields agree with the analytic formulas to within 2×10⁻¹⁵. Exact rational characteristic polynomials at K=log 2 provide a second check; a singleton Rayleigh quotient independently establishes exponential gap deterioration. Small-K examples were checked and can have the opposite gap comparison.

The bounded literature search found a substantial omitted **zero-field** spectral-gap claim throughout β<1 by OpenAI, dated September 24, 2026. Its original citation entry and hosting page were opened, but the PDF body could not be extracted; this proof was not audited. The claim is discussed in Section 1.2 of **Hang Du, Brice Huang, Sidhanth Mohanty, Amit Rajaraman**, [arXiv:2610.17717v1](https://arxiv.org/html/2610.17717v1), whose full text was opened. Their own result concerns simulated annealing. Details, other field special cases, and access limits are in [SOLVED_ELSEWHERE.md](SOLVED_ELSEWHERE.md). No complete arbitrary-field solution was located.

What failed or remains uncertain: deterministic field monotonicity fails; an extension for typical SK matrices was not proved. The recent zero-field preprint's correctness was not independently checked. The literature search was bounded and cannot certify absence of another result.

Next worker: pursue an explicitly disorder-dependent field comparison or a direct estimate along field tilts, rather than assuming zero field is the worst field. One concrete target is a lower bound, uniform over 0≤s≤1, on the heat-bath gap for μ_s(x)∝exp{β∑g_{ij}x_ix_j/√n+s h·x}, on a high-probability SK event. The triangle shows why such a statement must use properties of that event or impose quantitative interaction restrictions. First audit the precise zero-field input before importing it.

Task: “push this problem forward by one checkable piece” — 2026-11-14, 21:16 +04 (session-start clock).
