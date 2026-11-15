RESOLVED_IN_LITERATURE
The weaker support statement is proved in a public author preprint (Shitov, 2025, Theorem 1); journal publication is unverified. The full atom conjecture is not resolved here.

Task F0006. Literature checked 13 November 2026.

Let M_n have independent uniform ±1 entries. Write D_n for the set of determinants of all n×n sign matrices, and B_m for the determinant set of all m×m binary matrices. Vu's Conjecture 6.8 asks for

\[
\sup_{x\ne0}\Pr(\det M_n=x)\le n^{-(1/2+o(1))n}.
\]

The supremum expresses the intended uniform interpretation, allowing x to depend on n. An integer x fixed independently of n is eventually excluded by the divisibility 2^{n−1} | det M_n.

The literature stopping condition is met for the weaker support question, with the publication-status qualification on line 2. Here RESOLVED_IN_LITERATURE means an existing publicly written proof; it does not certify a journal publication. No proof of the full atom conjecture was located in this bounded search. A large support alone gives no upper bound on the largest atom. Per the stopping instruction, the step 2–3 spectrum enumeration, probability enumeration, and Monte Carlo program were not undertaken.

The decisive reference is Yaroslav Shitov, *The range of 0-1 determinants is large*, public preprint uploaded 14 November 2025, DOI [10.13140/RG.2.2.32216.35842](https://doi.org/10.13140/RG.2.2.32216.35842). **Theorem 1, page 1**, states that, for every sufficiently large integer m,

\[
\{0,1,\ldots,\lfloor\exp(\tfrac12m\log m-7m\log\log m)\rfloor\}\subseteq B_m. \tag{1}
\]

I read the [six-page primary PDF](https://www.researchgate.net/profile/Yaroslav-Shitov/publication/397595060_The_range_of_0-1_determinants_is_large/links/691689a59d514a24b4323683/The-range-of-0-1-determinants-is-large.pdf). The [author's full-text record](https://www.researchgate.net/publication/397595060_The_range_of_0-1_determinants_is_large) labels it a preprint; a journal, acceptance, or peer-review status is not inferred from the DOI.

To transfer (1) to the stated problem, take any binary m×m matrix B and form

\[
H(B)=\begin{pmatrix}1&\mathbf1^T\\\mathbf1&J-2B\end{pmatrix}.
\]

Every entry is ±1. Subtract its first row from each other row to obtain

\[
\det H(B)=(-2)^m\det B. \tag{2}
\]

Conversely, row and column sign changes normalize any sign matrix to first row and column all 1. The same subtraction produces (2) for a binary core, up to sign. For m≥2, exchanging two rows of B changes its determinant's sign, so D_{m+1}=2^m B_m. Therefore, for large n,

\[
|D_n|\ge2\left\lfloor\exp\left(\tfrac12(n-1)\log(n-1)-7(n-1)\log\log(n-1)\right)\right\rfloor+1. \tag{3}
\]

In particular |D_n|≥n^{cn} for **every fixed 0<c<1/2 and all sufficiently large n**, including c=1/4. Independently, Hadamard's inequality and divisibility give

\[
|D_n|\le2\lfloor n^{n/2}/2^{n-1}\rfloor+1.
\]

The bounds show that log|D_n|/(n log n) tends to 1/2. Thus the weaker support statement has a near-optimal leading exponent in the literature.

I audited the proof's input and elementary identities rather than relying on its abstract. The published input is N. Alon and V. H. Vũ, *Anti-Hadamard matrices, coin weighing, threshold gates, and indecomposable hypergraphs*, J. Combin. Theory Ser. A **79** (1997), 133–160, [DOI 10.1006/jcta.1997.2780](https://doi.org/10.1006/jcta.1997.2780). Section 2.4 and its final remark in the [author-hosted paper](https://web.math.princeton.edu/~nalon/PDFS/av1.pdf) give binary unimodular matrices of every large order r, with an inverse entry of magnitude exp(½r log r − (2 log 2+o(1))r). The unimodularity matters: a large inverse entry alone would not supply the needed core.

Here is a reconstruction of the dimension and range calculation. Border a unimodular core C to obtain a binary matrix

\[
U_q=\begin{pmatrix}0&u\\v&C\end{pmatrix},\qquad
\det C=1,\qquad\alpha=\det U_q=-uC^{-1}v.
\]

Select u,v to locate the large inverse entry. For large q,

\[
\tfrac12q\log q-1.5q\le\log|\alpha|\le\tfrac12q\log q.
\]

A t×t matrix with first row (ε_0,…,ε_{t−1}), subdiagonal α, and all remaining diagonal entries 1 has determinant Σ ε_i(−α)^i. Signed base-|α| digits realize every integer of absolute value at most |α|^t−1.

Replacing each subdiagonal scalar by the core C adds q−1 rows and columns. Its Schur complement restores −uC^{-1}v=α, including when the scalar is off the diagonal. The resulting order is (t−1)q+1, with only the first row nonbinary. That row has a binary positional expansion in b=ceil(log_2|α|) digit rows. The positional gadget adds b−1 dimensions. Each of those b rows has entries in {−2,−1,0,1}, hence is w−u−v for binary rows u,v,w, and can be replaced by three binary rows at a cost of two further dimensions. The final order is at most

\[
(t-1)q+3\lceil\log_2|\alpha|\rceil. \tag{4}
\]

Set L=log N, q=ceil(N/L²), t=ceil(L²−3L). Formula (4) is

\[
N-\left(3-\frac{3}{2\log2}+o(1)\right)N/L<N,
\]

since the coefficient subtracted is about 0.836. For large N, monotonicity of ½q log q−1.5q gives the independent lower estimate

\[
t\log|\alpha|\ge N\left(\tfrac12L-\log L-3+\frac{3\log L+4.5}{L}\right).
\]

It exceeds ½N log N−7N log log N+1 eventually. Padding with an identity block preserves determinants and reaches order exactly N. This checks (1), including the ceiling correction in (4).

There are minor slips in intermediate text of the preprint. The first alphabet-conversion sentence reverses the factor 2^{n−1}. Remark 5 must define α as det U_q, since its bottom-right core has determinant 1. Corollary 8 needs a ceiling for its digit count: a maximum digit of magnitude 4 needs three binary places. The change adds at most three dimensions to its displayed bound and fits the slack above. The proof of Corollary 4 also reverses a comparison and names a cofactor location inconsistent with its border; selecting the actual large cofactor gives its conclusion. The corrected argument above retains the stated support theorem.

All **763 exact checks passed** in [code/audit_literature.py](code/audit_literature.py), using custom fraction-free Bareiss elimination and an independent SymPy determinant calculation. Results are in [data/literature_audit_checks.json](data/literature_audit_checks.json): 555 border conversions, 60 binary-row gadgets, 20 positional-row identities, 48 scalar substitutions including off-diagonal positions, and 80 signed-base determinant identities. Border checks cover every binary core of orders 1–3 and five seeded examples per order 4–8. These are finite checks of identities, not a computational proof of the asymptotic existence theorem. The run used one thread, inherited nice 15, and approximately 56 MB peak RSS.

The literature audit covered the requested directions as follows.

| Area | Source and relevance |
|---|---|
| Original statement | V. H. Vu, Probability Surveys **18** (2021), 179–200, [arXiv:2005.02797](https://arxiv.org/abs/2005.02797), Section 6, Conjecture 6.8. Downloaded and read Section 6 completely. The atom/support discussion is on arXiv PDF page 10, journal page 188. |
| Earlier spectra | R. Craigen, *The range of the determinant function on the set of n×n (0,1)-matrices*, J. Combin. Math. Combin. Comput. **8** (1990), 161–171; W. P. Orrick, *The maximal {-1,1}-determinant of order 15*, Metrika **62** (2005), 195–219, [arXiv:math/0401179](https://arxiv.org/abs/math/0401179); M. Živković, *Classification of small (0,1) matrices*, Linear Algebra Appl. **414** (2006), 310–346, [arXiv:math/0511636](https://arxiv.org/abs/math/0511636). Finite spectra and computations. |
| Later exponential range | Rikhav Shah, *Determinants of binary matrices achieve every integral value up to Ω(2^n/n)*, Linear Algebra Appl. **645** (2022), 229–236, [arXiv:2006.04701](https://arxiv.org/abs/2006.04701), [DOI 10.1016/j.laa.2022.03.024](https://doi.org/10.1016/j.laa.2022.03.024). Exponential rather than super-exponential. |
| Larger finite spectrum | Brent–Orrick–Osborn–Zimmermann, *Maximal determinants and saturated D-optimal designs of orders 19 and 37*, [arXiv:1112.4160](https://arxiv.org/abs/1112.4160), Section 8. Complete sign-determinant spectrum at order 13. |
| Newer spectrum algorithms | C. A. Sfyrakis, *Theoretical construction and algorithms specifying determinants of ±1 matrices of the spectrum* (2022), [DOI 10.1080/27684830.2022.2088079](https://doi.org/10.1080/27684830.2022.2088079). Finite-order constructions and algorithms. |
| Decisive range theorem | Shitov (2025), Theorem 1, stated and audited above; public preprint, journal publication unverified. |
| Size and limiting laws | Tao–Vu, *On random ±1 matrices: singularity and determinant*, [arXiv:math/0411095](https://arxiv.org/abs/math/0411095), gives typical-magnitude estimates. Nguyen–Vu, *Random matrices: Law of the determinant*, Ann. Probab. **42** (2014), 146–167, [arXiv:1112.0752](https://arxiv.org/abs/1112.0752), proves a quantitative central limit theorem for log absolute determinant. These do not give the conjectured lattice-atom estimate. |
| Jain–Sah–Sawhney | *Singularity of discrete random matrices*, [arXiv:2010.06554](https://arxiv.org/abs/2010.06554), and *Sharp invertibility of random Bernoulli matrices*, [arXiv:2010.06553](https://arxiv.org/abs/2010.06553). Singularity and least singular values; no full nonzero determinant-atom theorem was identified. |
| Cokernel laws | Nguyen–Wood, *Random integral matrices: universality of surjectivity and the cokernel*, [arXiv:1806.00596](https://arxiv.org/abs/1806.00596), Theorem 1.1; and *Local and global universality of random matrix cokernels*, [arXiv:2210.08526](https://arxiv.org/abs/2210.08526), Math. Ann. (2025). Group-distribution results. “Local” here does not mean a local limit theorem for each integer determinant. The former's all-prime balance condition fails for unnormalized sign entries at p=2; binary cores remove that obstruction, but fixed-group limits do not give the required uniform moving-determinant atom estimate. |
| 2025–2026 checks | Hunter–Kwan–Sauermann, *Exponential anticoncentration of the permanent*, [arXiv:2509.22577](https://arxiv.org/abs/2509.22577), also obtains exponential determinant anticoncentration. Shen, *Quantative universality for cokernels of matrices with symmetries*, [arXiv:2601.09704](https://arxiv.org/abs/2601.09704), concerns cokernel universality. Neither states the full requested bound. No matching determinant local limit theorem or full resolution was found in this bounded search. |

The requested OEIS sequence is [A089472](https://oeis.org/A089472/internal), counting **signed binary determinant values**, offset 0. At orders 0–10 its published values are

\[
1,2,3,5,7,11,19,43,91,227,587.
\]

The binary spectrum sizes at orders 7 and 8 are 43 and 91; the sign spectrum sizes at orders 7 and 8 are 19 and 43. These are literature data, not newly enumerated values. [A013588](https://oeis.org/A013588/internal) instead gives the first missing positive determinant. Values and provenance are saved in [data/literature_spectrum.csv](data/literature_spectrum.csv).

The required Vu PDF is local in sources/. Shitov's PDF was readable through the web PDF reader, but direct shell downloads returned HTTP 403; saved web extracts retain theorem and proof passages. Source details and hashes are in [sources/MANIFEST.md](sources/MANIFEST.md). [LOG.md](LOG.md) records progress. All task files stayed in this directory; no publication or push was made.

Task: “Open problem F0006” — 13 November 2026, 05:55 Asia/Tbilisi (task-file creation time; no separate message timestamp was supplied).
