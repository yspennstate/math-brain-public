VERDICT: PROVED an improved almost-everywhere flat-torus gap limsup bound exceeding 2.021

The round-5 result holds. Its finite inequality, exact gain 131/196608,
and single-functional averaging argument were independently checked.

The new result is

\[
\limsup_i(x_{i+1}-x_i)\ge\Gamma
>\frac{121289}{60000}>2.021
\]

for almost every flat two-dimensional torus, with global sign pairs
identified and mean spacing one. The constant is specified exactly by

\[
c_0^4-4c_0^3+4c_0^2+24c_0-40=\frac{48}{121},\qquad
\Gamma=\frac{c_0^2+2c_0+6}{6},\qquad
\sqrt7-1<c_0<\frac74.
\]

There are infinitely many gaps larger than 2.021. At the exact endpoint
Gamma the assertion is a limsup bound. The new threshold exceeds
109/54, whereas the round-5 threshold is below 109/54.

The extension integrates the same adjacent-count inequality over moving
lengths a=1+u and t=1+w+2u. Its CDF terms cover consecutive windows
exactly, removing the earlier monotonicity loss. The gain is
eta(w)=w^2/2-11w^3/6, maximized in this family at w=2/11 with exact
value 2/363. The windows are [1,13/11] and [13/11,17/11], wholly within
the known quadratic branch. All triple weights remain nonnegative, so
the published averaged theorem controls their full sum along one
subsequence. The complete proof, including boundary terms, the extended
endpoint range and the almost-everywhere quantifiers, is in
[PROOF.md](PROOF.md).

The external input remains Theorem 1 and the recorded almost-everywhere
pair correlation in Christoph Aistleitner, Valentin Blomer and Maksym
Radziwiłł, *Triple correlation and long gaps in the spectrum of flat
tori*, [arXiv:1809.07881](https://arxiv.org/abs/1809.07881),
[published text](https://ems.press/content/serial-article-files/42560?nt=1).
Their full correlation proofs were not independently checked. The new
argument uses averaged triple convergence, with no individual-torus
triple limit.

Validation: the gain was derived from the moving deficit polynomial
and independently by subtracting exact antiderivative differences from
separately integrated pair and triple benchmarks. Optimization was
checked by differentiation and a square factorization. The scalar
integral was checked through its density and polynomial elimination.
The rational root comparison was checked using both expanded and
factored quartics. Finite count factors, moving-window Jacobians, early
exceptional gaps, all triple signs and the countable intersection were
audited in [LOG.md](LOG.md).

Commands: the initial web searches and primary-source opening finished
within five minutes. Shell reads used `OMP_NUM_THREADS=1 nice -n 15
/bin/cat`, `/bin/ls` and `rg`, apart from the initial discovery command.
The sandbox denied priority adjustment, so no numerical program was
run. This is an exact proof, with no computational experiment or script.
All authored files were saved with apply_patch in this folder. No git,
subagents, external writes or edits to previous folders were used.

What failed and what remains uncertain: the former endpoint restriction
G<=109/54 cannot contain the new threshold; the proof explicitly
extends the algebraic argument to G<=67/32. The optimality claim is
only for the specified consecutive-window family. Global optimality
and global novelty are not claimed. The bounded literature check found
no solution of the full two-dimensional problem; the opened
[Wooyeon Kim, Jens Marklof and Matthew Welsh paper](https://arxiv.org/abs/2601.03209)
still concerns pair correlation for three-dimensional boxes. The
nearest-neighbour law, all higher local statistics, and an explicit
Diophantine torus satisfying this improved bound remain unresolved.

Next worker: first audit equations (9), (25) and (26), then the exact
benchmark difference 1273/3993-1251/3993=2/363. For the next extension,
allow the moving interval to start at a length other than 1, retaining
dt/du=2 and consecutive windows. If the first window crosses 1,
integrate the two scalar branches separately. Optimize that enlarged
family and obtain a rational certificate before quoting an improved
decimal. The same one-functional averaging proof applies if all triple
weights remain nonnegative.

Task: “take the NEXT checkable step on this problem, building on that
work.” First recorded clock: 2026-11-15 10:54:25 Asia/Tbilisi; prompt
receipt time unavailable.
