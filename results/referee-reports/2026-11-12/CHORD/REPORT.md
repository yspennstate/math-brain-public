Overall verdict: SOUND

I found no mathematical gap or counterexample to either theorem or to the path lemma, with the spectral gap defined as in the paper. Both “the antipodal chords, and only they” and “every other chord strictly lowers the gap” are proved. This verdict concerns the mathematics; it does not certify the cited literature, which is not supplied locally. There is a false sentence about the scope of the Lean checks, identified below, but it does not affect a proof.

Line numbers below refer to the supplied `PAPER.tex`. I used no browsing, no other agents, and no author program as a computational oracle. New programs and their outputs are in this folder; the supplied files have not been edited.

## 1. Theorem 1 — SOUND

### Variational setup, lines 45–54

The normalization is correct. For the symmetric weighted Laplacian $L=D-A$,

\[
f^TLf=\sum_{\{i,j\}}c_{ij}(f_i-f_j)^2,
\qquad
\operatorname{Var}_D(f)=\sum_i d_i f_i^2-
\frac{(\sum_i d_i f_i)^2}{\sum_i d_i}.
\]

The positive eigenvalues of $D^{-1/2}LD^{-1/2}$ are the nonzero eigenvalues of $I-P$. Minimizing the quotient with this variance gives their smallest member, $1-\lambda_2(P)$. There is no missing factor of two. The cycle's first nonzero Laplacian eigenvalue is $2a$, while its random-walk gap is $a$.

### Half-turn and variance decomposition, lines 94–99

Let $B_E(u,v)=\sum_{\{i,j\}}c_{ij}(u_i-u_j)(v_i-v_j)$. The half-turn is an involution and preserves both $B_E$ and $\langle u,v\rangle_D=\sum_i d_i u_iv_i$. Thus

\[
B_E(f_+,f_-)=B_E(Tf_+,Tf_-)=-B_E(f_+,f_-)=0,
\]

and the identical argument gives $D$-orthogonality. Pairing $i$ with $i+m$ gives both

\[
\sum_i f_-(i)=0,\qquad \sum_i d_if_-(i)=0.
\]

The variance identity is valid even when $f_+$ has nonzero mean. For **every** constant $c$,

\[
\sum_i d_i(f_i-c)^2
=\sum_i d_i(f_+(i)-c)^2+\sum_i d_if_-(i)^2,
\]

because constants belong to the even sector. Taking the minimum over $c$ gives exactly line 98. In particular, the paper has not replaced a minimized variance by an uncentered sum.

### Even sector, lines 101–104

Subtracting the endpoint value $t$ preserves energy and variance and makes $g$ zero at both chord endpoints. Applying the path lemma separately on the two arcs yields

\[
\mathcal E(f_+)\ge 2a\sum_i g_i^2.
\]

Interior vertices occur once in this sum; endpoints occur twice in the arc sums but have value zero. The chord has zero energy. The choice $c=t$ in the minimum defining variance gives

\[
\operatorname{Var}_D(f_+)\le\sum_i d_i g_i^2=2\sum_i g_i^2.
\]

This is the needed direction: an upper bound on variance and a lower bound on energy imply $\mathcal E(f_+)\ge a\operatorname{Var}_D(f_+)$. No zero-mean assumption on $g$ is needed for the Dirichlet inequality.

### Odd sector, lines 106–112

The cycle Poincaré inequality requires ordinary counting mean zero, and the half-turn gives precisely that, independently of the weighted mean. It is therefore applied to the right function and measure. If $s=f_-(0)=-f_-(m)$, then

\[
\mathcal E(f_-)\ge 2a\sum_i f_-(i)^2+4ws^2,
\qquad
\sum_i d_if_-(i)^2=2\sum_i f_-(i)^2+2ws^2.
\]

The difference between the displayed lower bound on energy and $a$ times this norm is $2w(2-a)s^2\ge0$. The stated $a\le1$ is true because $m\ge2$, and is stronger than needed: $a\le2$ would suffice for this step. At $m=2$, $a=1$, so there is no boundary failure. Adding the sector bounds proves the lower bound for every nonconstant function, including functions with one constant or zero sector.

### Attainment, lines 114–116

The function $h(i)=\sin(\pi i/m)$ is nonzero for every $m\ge2$, has zero ordinary mean, and vanishes at both endpoints. Hence its weighted mean is also zero, the added chord contributes neither energy nor a degree correction to its norm, and

\[
Lh=2ah=aDh.
\]

It gives the opposite inequality $\gamma\le a$. This is an actual generalized eigenvector, not merely a test-vector heuristic. Together with the lower bound it proves equality for all finite $w>0$.

### Other chords and equation (strict), lines 119–127

For $\theta=2\pi/n$, $\alpha=\pi k/n$, and $f_i=\cos(\theta i-\alpha)$, the Fourier identities used in the paper give

\[
\sum_i f_i=0,\quad \sum_i f_i^2=n/2,\quad
f_0=f_k=t=\cos\alpha,\quad \mathcal E(f)=na.
\]

The weighted mean is generally **not** zero. The paper correctly subtracts its contribution:

\[
\sum_i d_if_i=2wt,\quad \sum_i d_if_i^2=n+2wt^2,\quad \sum_i d_i=2(n+w),
\]

\[
\operatorname{Var}_D(f)
=n+2wt^2-\frac{4w^2t^2}{2(n+w)}
=n\left(1+\frac{2wt^2}{n+w}\right).
\]

The resulting quotient is exactly the claimed bound. For $2\le k<m$, $0<\alpha<\pi/2$, so its denominator is strictly greater than one for every $w>0$. This proves $\gamma<a$, rather than only $\gamma\le a$.

For $k=2$ the same calculation applies. For $k=m-1$, when that chord exists, $t=\sin(\pi/n)>0$; its small size does not remove strictness. At $m=2$ there are no nonantipodal chords, so that clause is vacuous. At $m=3$ the only such chord is $k=2$; its bound is $(6+w)/(12+3w)<1/2$.

### “Only they,” “every other,” and weight limits

Rotation and reflection reduce every nonedge of the cycle to a representative $2\le k\le m$. All antipodal representatives have gap $a$; every remaining representative has gap strictly less than $a$. Thus both uniqueness of the maximizing class and strict lowering by every other chord are proved. “Only” means only the antipodal endpoint pairs, not a unique labeled chord. The fixed positive weight is essential; at $w=0$ all choices give the cycle again.

As $w\downarrow0$, the upper bound tends to $a$, consistently with continuity of the matrices and their eigenvalues. As $w\to\infty$, it tends to

\[
\frac{a}{1+2\cos^2\alpha},
\]

which is below $a$ for every nonantipodal chord. Independently, the true random-walk gap has limit

\[
\lim_{w\to\infty}\gamma=1-\cos\frac{\pi}{n-k}.
\]

To see this, use the symmetric normalized adjacency matrix. In the limit its endpoint block is a two-vertex edge of weight one, with eigenvalues $1,-1$; the other blocks are path adjacency matrices divided by two on $k-1$ and $n-k-1$ vertices. The largest eigenvalue below $1$ is $\cos(\pi/(n-k))$. For $k=m$ this gives $a$; otherwise it is smaller. This also explains why the finite-weight upper bound need not be sharp. The infinite-weight object is a limit, not an additional parameter value asserted in the theorem.

## 2. Theorem 2 — SOUND

### Kernel and quadratic form, lines 65–67 and 138–144

On an edge, the uniform-target acceptance probability gives $K_{ij}=c_{ij}/\max(d_i,d_j)$. The matrix is symmetric. Its off-diagonal entries do not exceed those of the proposal, so its diagonal entries are nonnegative and its rows sum to one. It is connected for finite $w>0$, so the variational characterization on ordinary mean-zero vectors applies.

The four cycle edges incident to the two chord endpoints each have weight $1/(2+w)=1/2-b/2$ in $K$; other cycle edges have weight $1/2$, and the chord has weight $b$. Since the endpoints are nonadjacent, these four edges are distinct. This remains true for $k=2$, where edges can share a neighboring vertex, and for $n=4,k=2$, where they are all four cycle edges. Self-loops contribute zero to the energy. Therefore

\[
f^T(I-K)f=\tfrac12\mathcal E_{\rm cyc}(f)
-\tfrac b2\sum_{\{i,j\}\in S}(f_i-f_j)^2+b(f_0-f_k)^2
\]

is correct, without an additional factor of two.

### Test function, algebra, and strictness, lines 144–152

For the same cosine test vector, the ordinary mean is zero and the chord term is zero. Write $c=\cos\alpha$, $s=\sin\alpha$. The two differences at endpoint zero are $ac-\sin\theta\,s$ and $ac+\sin\theta\,s$; reflection gives the same pair at the other endpoint. Squaring and summing gives

\[
S(f)=2[(ac-\sin\theta\,s)^2+(ac+\sin\theta\,s)^2]
=4(a^2c^2+\sin^2\theta\,s^2).
\]

The cycle contribution is $na/2$. Dividing the correction $-bS(f)/2$ by $\|f\|^2=n/2$ gives $-bS(f)/n$, hence exactly

\[
1-\lambda_2(K)\le a-\frac{4b}{n}
(a^2\cos^2\alpha+\sin^2\theta\sin^2\alpha).
\]

For $n\ge4$, $a>0$ and $\sin\theta>0$, and sine and cosine of $\alpha$ cannot both vanish. The bracket is strictly positive, including at the antipodal value $\alpha=\pi/2$, when it equals $\sin^2\theta$. Since $b>0$, the bound is strictly below $a$ for every allowed chord and every finite $w>0$. No strictness at the endpoint $w=0$ is asserted.

### Small cycles and limits

An independent exact calculation for $n=4,k=2$ gives the normalized-Laplacian spectra

\[
\operatorname{spec}(I-P)=
\left\{0,1,\frac{2(w+1)}{w+2},\frac{w+4}{w+2}\right\},
\]

\[
\operatorname{spec}(I-K)=
\left\{0,\frac2{w+2},\frac{2(w+1)}{w+2},\frac4{w+2}\right\}.
\]

Thus $\gamma=1=a$ and the Metropolis gap equals its stated upper bound $2/(w+2)<1$, for every $w>0$. For $n=6,k=3$, the Metropolis bound is also exact: $1/(w+2)<1/2$. These cases check the smallest $m$, not just an asymptotic regime.

As $w\downarrow0$, both $K$ and its bound tend to the cycle and $a$. As $w\to\infty$, the true Metropolis gap tends to zero: the four endpoint cycle transitions vanish, leaving three closed components (the endpoint pair and the two nonempty arc interiors). The stated upper bound need not tend to zero. For example, for $n=8,k=4$ its limit is $3/4-1/\sqrt2>0$. Consequently its relative error can be unbounded as $w\to\infty$. This is a limitation of sharpness, not a violation of the theorem.

The gap here is the ordinary gap $1-\lambda_2$, not the absolute gap $1-\max_{j\ge2}|\lambda_j|$. The paper defines it explicitly and qualifies “slower” in line 74 accordingly. No ordering of nonlazy total-variation mixing times follows. For example, $C_6+\{0,3\}$ is bipartite and has ordinary gap $1/2$ but absolute gap zero. This does not contradict either theorem.

## 3. Lemma 3 (path) — SOUND

Lines 83–90 are a complete finite-dimensional proof. With the endpoint values zero, the energy is exactly $g^TTg$ on the $m-1$ interior coordinates, with diagonal $2$ and neighboring entries $-1$. For $1\le j\le m-1$, direct use of the sine addition formula gives

\[
T(\sin(\pi ji/m))_{i=1}^{m-1}
=\bigl(2-2\cos(\pi j/m)\bigr)(\sin(\pi ji/m))_{i=1}^{m-1}.
\]

These eigenvalues are distinct and increasing because cosine decreases on $(0,\pi)$; the nonzero eigenvectors therefore form a basis. The smallest eigenvalue is $2a$. Equality is attained by $g_i=\sin(\pi i/m)$. For $m=2$, the matrix is the one-entry matrix $[2]$, and the inequality is equality for every allowed vector. There is no missing endpoint term or normalization.

## 4. Remark 4 (odd cycles) — SOUND

Lines 130–132 correctly extend equation (strict) to every chord of every odd cycle $n\ge5$, with $a=1-\cos(2\pi/n)$ and $2\le k\le(n-1)/2$. The same mean, norm, and energy identities hold, and $\cos(\pi k/n)>0$. Therefore **every** chord strictly lowers the ordinary random-walk gap. There is no antipodal pair and no equality class. The remark does not identify which odd-cycle chord maximizes the decreased gap, and I do not infer that optimization from a one-vector bound.

The proof of Theorem 2 also extends unchanged to those odd cycles: the four edges are distinct, $\sin(2\pi/n)>0$, and the same strictly smaller upper bound follows. There are no chords of a simple $C_3$ under the paper's definition. The half-turn proof of antipodal equality has no odd-cycle counterpart.

## 5. Remark 5 (scope of Metropolization) — SOUND for the stated restriction

Lines 155–157 correctly limit Theorem 2 to the proposal $D^{-1}A$ and uniform target. Other proposals or optimizations over kernels are not covered. The theorem also does not select the best chord among these slower Metropolis kernels. Whether “Diaconis's question allows any way of Metropolizing” is an exact description of the source cannot be verified from the supplied materials; see the citation assessment below.

## 6. Remark 6 (reported computations) — SOUND within the inspected scope

Lines 160–166 report finite checks, not a substitute for a proof. For $n=4,6,\ldots,16$ there are $1+2+\cdots+7=28$ chord representatives per weight. Three weights give 84 cases, of which $7\cdot3=21$ are antipodal and 63 are not. Those counts agree with `evidence/exact_matrix.json` and `evidence/exact_paths.json`. The latter is a summary, not a second saved collection of polynomials. I read both exact-check programs but did not run them or treat their success flags as proof.

The five weights from 0.01 to 1000 are present in `code/explore.py` and `evidence/exploration.json`. `code/numeric_check.py` uses a different five-weight grid, ending at 500, and also checks odd cycles. This is not an inconsistency in the stated existence of checks from 0.01 to 1000. The supplied Metropolis evidence contains 84 exact classifications and edge-form equalities. My independently reconstructed spectra and symbolic checks below agree with the mathematical conclusions, without certifying every archived run.

## What the Lean files prove

There are **two** supplied Lean sources.

1. `lean/E0095_PathLemma.lean`, lines 149–161, proves `path_dirichlet`: for a natural number $m$ and a real sequence $f$ with $f(0)=f(m)=0$,

   \[
   (2-2\cos(\pi/m))\sum_{i=0}^m f(i)^2
   \le\sum_{i=0}^{m-1}(f(i)-f(i+1))^2.
   \]

   Since the endpoints vanish, this is exactly the paper's path lemma, on its domain $m\ge2$. It also proves `path_dirichlet_sin_eq`, attainment by the sine sequence for $m>0$; on the paper's domain that sequence is nonzero, establishing sharpness. The source proves positivity and the sine recurrence in `sin_hyps`; these are not unproved assumptions in the final theorem. It uses a positive-ground-state/Picone argument rather than a full eigenbasis calculation. Boundary zero weights are handled explicitly in `edge_bound`, so there is no division-by-zero gap hidden in its application. Lean's extra degenerate cases $m=0,1$ do not affect the paper.

2. `lean/E0095_MHIdentity.lean`, lines 16–27, proves `edge_sum`, the real trigonometric identity

   \[
   2[(\cos(\theta-\alpha)-\cos\alpha)^2+
   (\cos(\theta+\alpha)-\cos\alpha)^2]
   =4[(1-\cos\theta)^2\cos^2\alpha+\sin^2\theta\sin^2\alpha],
   \]

   and `chord_energy`, the inequality

   \[
   2(1-\cos\theta)ws^2\le4ws^2\qquad(w\ge0).
   \]

   The first is the algebra at lines 148–149 of Theorem 2. The second is the comparison at line 110 of **Theorem 1**, using the sufficient bound $1-\cos\theta\le2$. It is not a second step of Theorem 2.

Neither source proves either spectral-gap theorem, the variational principle, the half-turn decomposition, the variance calculation, the four-edge interpretation, the mean-zero test-function identities, or strictness of the final bounds. In particular, the algebraic identity by itself does not prove that its left side is the graph's edge sum.

I found no `sorry` or added axiom in the supplied sources. The saved `E0095_PathLemma.out` reports only `propext`, `Classical.choice`, and `Quot.sound` and exit code zero for the path results. That is supplied compiler evidence, not an independent compilation during this audit. Neither `lean` nor `lake` is on this run's PATH, and there is no local Mathlib project; I did not install or fetch one. There is no analogous supplied compiler-output file for the two short identities. The exact scope of the source statements is nonetheless clear, and the underlying mathematics was independently checked above.

## Introduction and cited results

No cited research paper, original excerpt, or PDF is supplied in the folder. Under the no-browsing rule I cannot certify the bibliographic identifiers, precise hypotheses, dates, or accuracy of the summaries against the originals. The following is a restricted assessment of the text, not external source verification.

| Citation and lines | Assessment from the supplied text |
|---|---|
| Diaconis, 33–35 and 156–157 | The two described questions distinguish a full perfect matching from a single edge with stationary law held fixed. The current results are relevant restricted one-edge cases; they do not solve the matching problem or an optimization over all Metropolis proposals. The claim about “any way of Metropolizing” needs checking against the original question, which is absent. |
| Hermon–Sly–Sousi, 36–37 | A result about graphs with an added **random** matching is consistent with the cited title and with the stated application to cycles. It does not identify an optimal deterministic matching. Thus it does not conflict with line 79's open optimization question. Precise cutoff/mixing hypotheses are not given and are unverified here. |
| Eldan–Rácz–Schramm, 37–38 | The described phenomenon is the Braess-type decrease for the normalized/random-walk gap, consistent with the cited title. No probability value or random-graph regime is specified, so “substantial probability” cannot be checked quantitatively from this folder. It must not be read as a decrease of combinatorial algebraic connectivity. |
| Ghosh–Boyd, 39–40 | The attribution to edge selection for combinatorial algebraic connectivity is consistent with the title. Independently, the mathematical monotonicity sentence is correct: adding an edge adds $w(e_u-e_v)(e_u-e_v)^T\succeq0$ to the combinatorial Laplacian, and the variational minimum on $\mathbf1^\perp$ cannot decrease. This argument does not apply to the degree-normalized quotient. |
| Kim, 40 | The title explicitly concerns increasing algebraic connectivity by adding an edge, consistent with the description. No exact algorithmic or optimality guarantee is asserted here. Source verification remains outstanding. |
| Deng et al., 41–43 | The claimed exact resistance/Kirchhoff formulas and near-optimal algebraic-connectivity assertion are specific claims that cannot be inferred merely from the title or checked without the preprint. In particular, the bounded-conductance assumptions and meaning of “near-optimal” are not supplied. Treat this attribution as unverified, not as an established supporting theorem in this audit. Neither spectral-gap proof uses it. |

The introduction keeps combinatorial algebraic connectivity separate from the normalized random-walk gap, which is necessary and correct. I found no internal contradiction in these literature descriptions. Absence of sources is not evidence that the citations are correct or fabricated. The scope qualification in Remark 5 prevents the main theorem from being read as a solution for every stationary-law-preserving edge augmentation scheme.

## Independent checks: programs, commands, and outputs

### High-precision spectra and direct Rayleigh quotients

`referee_spectra.py` constructs an unordered cycle-plus-chord edge list, derives degrees and $L$ from it, and diagonalizes $D^{-1/2}LD^{-1/2}$ with `mpmath.eigsy` at 55 decimal digits. It separately constructs $K$ using the proposal entries and the MH acceptance rule, fills its diagonal from row sums, and diagonalizes $I-K$. It sorts by the eigensolver's increasing eigenvalue order, checks the zero eigenvalue, and takes the second smallest value. It also evaluates both test-vector Rayleigh quotients directly and compares them with the printed formulas. It imports no author code.

The main weight grid is

\[
0.01,\ 0.03,\ 0.1,\ 0.3,\ 1,\ 3,\ 10,\ 30,\ 100.
\]

Commands and saved standard output:

```text
python3 referee_spectra.py --sizes 4 6 8 10 12
    -> referee_spectra_small.out
python3 referee_spectra.py --sizes 20 30
    -> referee_spectra_large.out
python3 referee_spectra.py --sizes 5 7 9 11 13 21 31
    -> referee_spectra_odd.out
python3 referee_spectra.py --sizes 4 6 8 10 12 20 30 \
    --weights 0.00000001 100000000 --tag _extreme
    -> referee_spectra_extreme.out
```

Each command was run with BLAS/OpenMP thread limits set to one. All result rows are saved to `referee_spectra_n<N>.csv` and `referee_spectra_extreme_n<N>.csv`, with 45 significant digits, including the true gaps, both upper bounds, absolute and relative slack, and formula residuals.

The following table uses the maximum **bound / true gap** across all chords and grid weights at each size. A ratio of one means a sharp bound; these are separate maxima for the two chains, not necessarily at the same chord.

| $n$ | Cases | Largest walk-bound ratio | Largest MH-bound ratio |
|---:|---:|---:|---:|
| 4 | 9 | 1.000000 | 1.000000 |
| 6 | 18 | 1.128202 | 8.262839 |
| 8 | 27 | 1.164626 | 16.673031 |
| 10 | 36 | 1.164604 | 16.848301 |
| 12 | 45 | 1.151486 | 16.711203 |
| 20 | 81 | 1.147130 | 14.361671 |
| 30 | 126 | 1.161843 | 11.993926 |

Aggregate output, reproduced from `referee_summary.json`:

```text
Requested even-cycle grid: 342 cases; 63 antipodal, 279 nonantipodal.
Walk-bound violations: 0. MH-bound violations: 0.
Nonantipodal strict-decrease failures: 0. MH strict-decrease failures: 0.
Maximum antipodal |gamma-a|: 8.79386734945114e-56.
Maximum direct walk-quotient/formula residual: 5.09789411562385e-57.
Maximum direct MH-quotient/formula residual: 1.01957882312477e-56.
Smallest nonantipodal walk-bound slack: 5.21668932219956e-11.

Odd-cycle grid: 342 cases, all nonantipodal.
Both bound-violation counts and both strict-decrease-failure counts: 0.
Maximum direct quotient/formula residual over both chains: 2.03915764624954e-56.

Extreme-weight even-cycle grid: 76 cases; 14 antipodal, 62 nonantipodal.
Both bound-violation counts and both strict-decrease-failure counts: 0.
Maximum antipodal |gamma-a|: 5.09789411562385e-56.
```

The inequality tolerance was $10^{-45}$; direct strict comparisons were also made for nonantipodal walk gaps, and the summary checks strict MH decrease from saved numbers. Tiny negative slacks of order $10^{-56}$ in equality cases are eigensolver roundoff, not violations. These are high-precision numerical checks, not interval-certified eigenvalue enclosures. Universal claims are justified by the proofs, not by this finite grid.

Some representative values (rounded here; full precision is in the CSVs):

| $n,k,w$ | True walk gap | Walk bound | True MH gap | MH bound |
|---|---:|---:|---:|---:|
| 4, 2, 1 | 1.000000000000 | 1.000000000000 | 0.666666666667 | 0.666666666667 |
| 6, 2, 1 | 0.464151253332 | 0.466666666667 | 0.350575078645 | 0.361111111111 |
| 6, 3, 1 | 0.500000000000 | 0.500000000000 | 0.333333333333 | 0.333333333333 |
| 8, 4, 100 | 0.292893218813 | 0.292893218813 | 0.006521677220 | 0.047795179598 |
| 30, 2, 100 | 0.007608699930 | 0.008840117378 | 0.005887810168 | 0.021548414675 |
| 30, 14, 100 | 0.020668690875 | 0.021491143082 | 0.001357202018 | 0.016262833391 |
| 30, 15, 100 | 0.021852399266 | 0.021852399266 | 0.001350831728 | 0.016201775583 |

The least walk decrease on the requested nonantipodal grid occurs at $n=30,k=14,w=0.01$: $a-\gamma\approx1.59173751865\times10^{-7}>0$. Thus even the close-to-antipodal, small-weight case is resolved well above numerical noise. The walk bound's largest relative slack is about 16.46%, at $n=8,k=3,w=100$, where the true gap is $0.19783805473495815$ and the bound is $0.23040734121472166$. The worst MH ratio on the requested grid is about 16.8483, at $n=10,k=2,w=100$, with true gap $0.008001491274405215$ and bound $0.13481153338239005$. The bound is useful for strict decrease but can be a poor numerical estimate.

### Exact independent checks

`referee_exact.py` constructs full Laplacians from edge vectors and computes symbolic generalized determinants and MH characteristic polynomials for every chord of $C_4,C_6,C_8$, with a free positive symbol $w$. It also independently builds the Dirichlet path matrices for $m=2,\ldots,15$ and verifies their characteristic polynomials against $(-1)^{m-1}U_{m-1}(1-x/2)$. It checks the variance algebra and the four-edge squared-difference expansion symbolically.

```text
python3 referee_exact.py -> referee_exact.out and referee_exact.json
small_exact_cases: 6
path_m_values: 2,3,4,5,6,7,8,9,10,11,12,13,14,15
variance_identity: true
four_edge_identity: true
passed: true
seconds: 0.980
```

For example, the $C_4$ generalized determinant is

```text
4*x*(x-1)*(w*x-2*w+2*x-2)*(w*x-w+2*x-4)
```

and its MH characteristic polynomial is

```text
x*(w*x+2*x-4)*(w*x+2*x-2)*(w*x-2*w+2*x-2)/(w+2)^3.
```

These give the exact spectra displayed above. The free-$w$ determinants for all six cases are preserved in the output. Finding an exact antipodal root alone would not certify it as the gap; that ordering is supplied by the independent proof audit and the full numerical spectra.

`referee_summarize.py` reads the referee CSV files, counts strictness failures and bound violations, extracts the worst ratios and examples, and counts the supplied evidence records. Command: `python3 referee_summarize.py > referee_summary.out`; its machine-readable output is `referee_summary.json`.

`referee_forms.py` separately checks the half-turn identities in exact `Fraction` arithmetic, on a deterministic nonconstant vector for each of the seven requested even sizes and nine grid weights. Its 11 checks per case include orthogonality for both forms, both zero means, the minimized-variance decomposition, the even-sector variance estimate, and the odd-sector degree and chord-energy corrections. Command: `python3 referee_forms.py > referee_forms.out`. The saved output in `referee_forms.json` reports 63 cases, all passed, in 0.035 seconds. These finite instances corroborate the algebra; the general justification is the proof audit above.

Each numerical or symbolic invocation had a 240-second alarm. Recorded numerical runtimes were approximately 1.78 s, 26.18 s, 30.65 s, and 5.52 s for the four spectrum commands above. The computations used at most two simultaneous Python processes, one thread each, with inherited or reduced process priority. The largest matrices were $31\times31$; no large arrays, worker pools, GPU jobs, or installations were used. The report does not rely on any computation near the one-GB limit.

## Corrections and source checks

No mathematical correction to either theorem, equation (strict), or Lemma 3 is needed. The following are the specific wording issues or source checks that remain:

1. **`PAPER.tex`, lines 192–194:** “checked two algebraic steps of the proof of [Theorem 2] in Lean” is false for the supplied sources. `edge_sum` checks the calculation in Theorem 2; `chord_energy` checks the odd-sector comparison in Theorem 1. The separate path file also formalizes Lemma 3 and its sine equality case. Suggested replacement: “The path lemma and its sine equality case, the edge-sum identity in Theorem 2, and the chord-energy comparison in Theorem 1 were checked in Lean.” This is an error in describing the checks, not an error in the theorems.

2. **`lean/LEAN_E0095_README.md`, heading for `E0095_MHIdentity.lean`:** likewise replace “two algebraic steps in the proof of Theorem 2” with “one algebraic step in each of Theorems 1 and 2.” Do not suggest that the full graph-theoretic or variational statements are formalized.

3. **`PAPER.tex`, line 66:** the acceptance-ratio expression is literally undefined on a nonedge, where $P(i,j)=P(j,i)=0$. The rightmost formula $c_{ij}/\max(d_i,d_j)$ already defines the correct value zero. For a completely explicit definition, state the ratio formula on edges and set $K(i,j)=0$ on nonedges, or use just the rightmost formula. This is a support convention to clarify, not a gap in the subsequent proof.

4. **`PAPER.tex`, lines 33–35 and 156–157:** check the exact formulation of Diaconis's Question 4 against the source before claiming that it permits “any way of Metropolizing.” The current proof covers exactly one specified proposal. The paper states that restriction correctly; the broader source attribution was not verifiable locally.

5. **`PAPER.tex`, lines 41–43 and bibliography lines 206–207:** verify the Deng et al. preprint, its resistance/Kirchhoff assertions, and its quantitative “near-optimal” statement against the original. The supplied text does not provide the hypotheses or guarantee needed to check that summary. This is an outstanding source check, not a finding that the citation is false. The other bibliography entries also remain externally unverified under the no-browsing instruction.

The bounds can be loose, and the full matching problem and optimizations over other proposals remain outside the results. Those are stated limitations, not missing proof steps. Neither “only they” nor “every other chord strictly lowers the gap” needs weakening.

Task: “You are refereeing a mathematical paper that has been posted. Be a hard, independent referee”; report completed 12 November 2026, 19:34 +04.
