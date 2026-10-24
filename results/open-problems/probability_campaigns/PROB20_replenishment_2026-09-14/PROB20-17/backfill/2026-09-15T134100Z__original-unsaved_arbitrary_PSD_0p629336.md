# PROB20-17 backfill — original unsaved run: arbitrary PSD n=4 factor 0.6293369187589889

**ORIGINAL RUN STATUS: PARTIAL.**

**Recovery provenance.** This file backfills an authentic earlier completed task response/writeup from this conversation that was not present in the GitHub task directory during bounded recovery. It is historical recovered work, not a claim of prior persistence. The mathematical content is preserved below in cumulative form.

For `n=4`, write
\[
S:=\sum_{\sigma\in S_4}\|A_{\sigma(1)}A_{\sigma(2)}A_{\sigma(3)}A_{\sigma(4)}\|,
\qquad
R:=\sum_{i,j,k,\ell=1}^4\|A_iA_jA_kA_\ell\|.
\]
The sharp conjecture is `3R>=32S`. This run proved
\[
\boxed{\frac{R/256}{S/24}\ge0.6293369187589889\ldots}
\]
for arbitrary PSD matrices in arbitrary finite dimension.

Set
\[
a_i=\|A_i\|,\quad p_{ij}=\|A_iA_j\|,\quad P=\sum_{i<j}p_{ij}^2,
\]
\[
E=\sum_{i<j}a_i^2a_j^2,\qquad Q=\sum_i a_i^4.
\]
Then `S<=4P`, `P<=E<=3Q/2`.

## Nonadjacent 2+1+1 aggregate
For a distinct ordered quadruple `(A,B,C,D)`, let `N=||ABCD||`, `q=||BCBA||`, `a=||A||`, `d=||D||`, `p_CD=||CD||`. The IKW Cauchy/Heinz inequality gives
\[
N^2\le\|ABCBA\|\,\|DCD\|\le q\,a d\,p_{CD}.
\]
Summing square roots over all 24 permutations and applying Cauchy gives
\[
S^2\le C_{13}\cdot 4\sqrt{PE},
\]
so
\[
\boxed{C_{13}=C_{24}\ge\frac{S^2}{4\sqrt{PE}}.}
\]
Together with the endpoint-repeat bound `C_{12}+C_{34}>=2S`,
\[
\boxed{Q_{211}\ge2S+\frac{S^2}{2\sqrt{PE}}.}
\]

## Alternating 2+2 lemma
For PSD `A,B`, with `a=||A||`, `b=||B||`, `p=||AB||`, let `r=rho(AB)=||B^{1/2}AB^{1/2}||`. Since
\[
p^2=\|BA^2B\|\le a\|BAB\|\le ab r,
\]
we have `r>=p^2/(ab)`. Therefore
\[
\boxed{\|ABAB\|,\|BABA\|\ge\frac{p^4}{a^2b^2}.}
\]
For the six `2+2` words from each unordered pair, the other four contribute at least `p^2` each, so
\[
Q_{22}\ge4P+2\sum_{i<j}\frac{p_{ij}^4}{a_i^2a_j^2}
\ge4P+\frac{2P^2}{E}.
\]

## 3+1 aggregate
Using the earlier ALT two-matrix lemma and scalar AM-GM, the pair `{i,j}` contributes at least
\[
8\frac{p_{ij}^3}{a_i a_j}.
\]
With weights `w_ij=a_i^2a_j^2` and `r_ij=p_ij/(a_i a_j)`, weighted power mean gives
\[
\sum w_{ij}r_{ij}^3\ge\frac{P^{3/2}}{E^{1/2}},
\]
so
\[
\boxed{Q_{31}\ge\frac{8P^{3/2}}{\sqrt E}.}
\]

## Scalar relaxation
Combining the occupancy layers,
\[
R\ge3S+\frac{S^2}{2\sqrt{PE}}+4P+\frac{2P^2}{E}+\frac{8P^{3/2}}{\sqrt E}+Q.
\]
Normalize
\[
s=S/P,\qquad e=E/P,\qquad q=Q/P.
\]
Then `0<s<=4`, `e>=1`, `q>=2e/3`, and
\[
\frac RS\ge3+\frac{s}{2\sqrt e}+\frac{4+2/e+8/\sqrt e+q}{s}.
\]
The relaxed minimum occurs at `q=2e/3`, `s=4`, reducing to
\[
F(e)=4+\frac4{\sqrt e}+\frac1{2e}+\frac e6,
\qquad e\ge1.
\]
Writing `x=sqrt(e)`, the unique minimizer solves
\[
x^4-12x-3=0.
\]
Numerically `x=2.367337963300214`, `e=5.604289032482405`, and
\[
R/S\ge6.712927133429215\ldots,
\]
which yields the normalized factor
\[
0.6293369187589889\ldots.
\]

**Open gap:** sharp `n=4` remains unproved, and therefore the all-`n` conjecture remains open.

**Failed/conditional routes recorded in the original writeup:** termwise repeated-word domination fails; projection cross-compression does not extend verbatim to arbitrary positive contractions; purely linear word-norm relaxations are weak; the stronger candidate `||ABAB|| >= ||AB||^3/(||A||||B||)` remained unproved and was not used.

**Verification level in original run:** self-contained algebraic check plus random diagnostics; no independent human/formal verification.
