# Verification of the depth-varying catalog-row estimate

The result checked here is Lemma `row-depth`, together with its maximal premise `row-maximal`, in OpenAI, *Pointwise convergence of triple ergodic averages for mixing transformations* (October 4, 2026), [Section “Bessel rows with inputs varying in depth”](https://github.com/openai/math/blob/main/preprints/Pointwise-convergence-of-triple-ergodic-averages-for-mixing-transformations-October-4-2026/build/paper/sections/rows.tex). This is a finite operator lemma. Its verification does not establish the local four-linear estimate or the ergodic convergence theorem.

## Precise hypotheses

Let R be a bounded dyadic interval of positive length. There are finitely many birth labels v, with dyadic birth intervals J_v contained in R, measurable columns

\[
 \Phi_v(y)=(\phi_v(y),\gamma_v e_v)
 \quad(y\in J_v),\qquad
 \mathcal H=\mathcal H_0\oplus\ell^2(\mathcal V).
\]

The vectors e_v are distinct coordinate vectors and the nonzero constants gamma_v never change on descendants. A label is available on Q exactly when Q is contained in its birth interval. The same column is restricted to every descendant where it is used. For one D≥2, assume

\[
 \|\Phi_v\|_{\infty,J_v}\le D,\qquad
 |\gamma_v|\ge D^{-1},\qquad
 \sum_v1_{J_v}(y)\le D \quad\text{a.e. on }R.                 \tag{1}
\]

For rounds 1≤n≤N, let pi_n and sigma_n be finite dyadic partitions of R such that sigma_n refines pi_n and pi_{n+1} refines sigma_n. Each round has a finite set of row operators A_nu from L²(R;H) to a Hilbert space Y_nu. Different rounds have disjoint row indices. Every row has one whole support Q_nu in pi_n:

\[
 A_\nu=A_\nu1_{Q_\nu}.                                    \tag{2}
\]

On every cell K of sigma_n, every tested adjoint is a constant-coefficient combination of the available columns:

\[
 1_K A_\nu^*c=1_K\sum_{v:K\subset J_v}a_{\nu,K,v}(c)\Phi_v. \tag{3}
\]

There is no bound required on individual coefficients. Finally assume the joint Bessel inequality for every z in L²(R;H):

\[
 \sum_\nu\|A_\nu z\|^2\le B^2\|z\|_2^2.                  \tag{4}
\]

The input schedule F_s is strongly measurable, on a finite integer interval S partitioned into W deterministic nonempty consecutive blocks. On each block b assume, almost everywhere,

\[
 \max_{s\in b}\|F_s(y)\|
 +\sum_{s,s+1\in b}\|F_{s+1}(y)-F_s(y)\|\le W^{-1/2}.      \tag{5}
\]

Each round reads one F_{s_n}, with s_1≤⋯≤s_N in S. This is an ordering of read indices, separate from the support depth. All realized rows and columns are fixed while (4) is tested, even if their selection originally depended on the schedule.

Put

\[
 L_D=1+\lceil5\log_2 D\rceil,\qquad
 C_D=\frac83\sqrt{9+L_D^2}.
\]

Under these hypotheses the claimed conclusion is

\[
 \left(\sum_n\sum_{\nu\in\mathcal R_n}
             \|A_\nu F_{s_n}\|^2\right)^{1/2}
 \le C_D B|R|^{1/2}
 \le\frac{40}{3}B\log_2(2D)|R|^{1/2}.                     \tag{6}
\]

## Coefficient comparison

For any coefficients supported on labels available at a point, the private coordinates give the lower bound below. Cauchy–Schwarz, the column size and the path count in (1) give the upper bound:

\[
 D^{-1}\|a\|_{\ell^2}
 \le\left\|\sum_v a_v\Phi_v(y)\right\|_{\mathcal H}
 \le D^{3/2}\|a\|_{\ell^2}.                               \tag{7}
\]

Indeed, the squared private norm is sum_v |gamma_v|²|a_v|², whereas sum_v ||Phi_v(y)||²≤D³. This also proves uniqueness of coefficients. Because the labels and their private coordinates persist, the coefficient vector on a parent restricts unchanged to descendants, after extending it by zero in the common space ell²(V). Finitely many labels and tested adjoints permit one common exceptional null set.

## A maximal bound for tested adjoint sums

Fix any consecutive range of rounds and tests c_nu. Relabel its rounds as 1,…,M. Write

\[
 E=\sum_\nu\|c_\nu\|^2,\qquad
 g_n=\sum_{\nu\in\mathcal R_n}A_\nu^*c_\nu,\qquad
 S_j=\sum_{n=1}^j g_n,\qquad
 M_*(y)=\max_{0\le j\le M}\|S_j(y)\|.
\]

Restricting to any subfamily of rows preserves (4). Taking the adjoint of this restricted operator yields

\[
 \left\|\sum_{\nu\in U}A_\nu^*c_\nu\right\|_2^2
 \le B^2\sum_{\nu\in U}\|c_\nu\|^2                       \tag{8}
\]

for every subset U of row indices. This remains true for a subset selected after the tests are fixed; no probabilistic independence is involved.

Fix lambda>0 and set

\[
 T=2^{\lceil5\log_2D\rceil},\qquad
 \tau=\frac{\lambda}{4D^{3/2}}.
\]

Assign rows to buckets 1,…,T. At the start of the first round every point has bucket 1 and accumulated coefficient vector zero. Suppose the current bucket and vector are constant on cells of pi_n. Assign every row supported on Q to the bucket of that whole Q, unless its state is T+1. On each finer cell K of sigma_n, add the coefficient vector of g_n there. If its norm exceeds tau, complete that bucket, advance the bucket index and reset the vector to zero. Otherwise retain the vector. After the T-th completion, keep state T+1 and omit subsequent rows on that path.

The state after the round is constant on sigma_n cells, so it is constant on each support cell of the next round. This proves the induction. Old coefficient vectors remain valid on the finer cells by (7) and persistence. Each row is assigned once on its entire support, even if different observation cells within that support register different hits. This is the exact place where the order pi_n, sigma_n, pi_{n+1} is needed.

Let U_i be the resulting disjoint row subsets and v_i their full tested adjoint sums. From (8),

\[
 \left\|\sum_{i\in A}v_i\right\|_2^2
 \le B^2\sum_{\nu\in\bigcup_{i\in A}U_i}\|c_\nu\|^2,
 \qquad \sum_i\|v_i\|_2^2\le B^2E.                        \tag{9}
\]

Let Omega be the set of paths with T completed buckets. At y in Omega, v_i(y) is precisely the sum accumulated when bucket i completed. Later rows containing y have a larger bucket index, and rows not containing y vanish there by (2). Thus each of these T vectors has coefficient norm greater than tau. The lower inequality in (7) gives

\[
 T D^{-2}\tau^2|\Omega|
 \le\int_\Omega\sum_i\|v_i(y)\|^2dy
 \le B^2E,
\]

and hence

\[
 |\Omega|\le\frac{16D^5B^2E}{T\lambda^2}.                 \tag{10}
\]

Outside Omega, every S_j(y) is a prefix of the completed bucket sums plus the current unfinished sum. At the end of a non-hit round the unfinished coefficient norm is at most tau. At a hit round the new completed bucket belongs to the prefix and the unfinished vector is zero. The upper inequality in (7) therefore gives

\[
 M_*(y)\le\max_{0\le j\le T}\left\|\sum_{i=1}^jv_i(y)\right\|
                 +\lambda/4 \quad(y\notin\Omega).        \tag{11}
\]

Decompose each index prefix into disjoint dyadic blocks, at most one at each of the 1+log_2 T=L_D lengths. For one such length, (9), summed over the disjoint blocks, bounds the squared L² norm of their square function by B²E. Pointwise triangle inequality followed by Minkowski in L² gives

\[
 \left\|\max_{0\le j\le T}\left\|\sum_{i=1}^jv_i\right\|\right\|_2
 \le L_D B E^{1/2}.                                      \tag{12}
\]

Chebyshev, (10)–(12), and T≥D⁵ imply

\[
 \begin{aligned}
 |\{M_*>\lambda\}|
 &\le\frac{16B^2E}{\lambda^2}
             \left(\frac{D^5}{T}+\frac{L_D^2}{9}\right)\\
 &\le\frac{16(9+L_D^2)B^2E}{9\lambda^2}
   =\frac{C_D^2 B^2E}{4\lambda^2}.                        \tag{13}
 \end{aligned}
\]

The trivial bound |R| applies as well. For H=(C_D/2)B sqrt(E), direct integration, splitting at lambda=H/sqrt(|R|), gives

\[
 \|M_*\|_1
 \le\int_0^\infty\min\{|R|,H^2/\lambda^2\}\,d\lambda
 =2H|R|^{1/2}=C_D B|R|^{1/2}E^{1/2}.                     \tag{14}
\]

If H=0, (13) instead implies M_*=0 almost everywhere. Thus (14) covers B=0 and zero tests without division by zero. This proves the maximal premise for any consecutive range of rounds.

## Abel summation and the block cancellation

Use inner products linear in the first argument. Fix the tests once more. The rounds whose read indices belong to a particular input block form a consecutive range p,…,q, or there are no such rounds. On a nonempty range, define S_n=sum_{r=p}^n g_r. The exact finite identity is

\[
 \sum_{n=p}^q\langle F_{s_n},g_n\rangle
 =\langle F_{s_q},S_q\rangle
   +\sum_{n=p}^{q-1}\langle F_{s_n}-F_{s_{n+1}},S_n\rangle.
                                                                    \tag{15}
\]

Nondecreasing read indices traverse each edge of this input block at most once. Skipped indices are bounded by telescoping through the skipped edges, and repeated indices contribute zero. By (5), the absolute value of (15) is at most W^(-1/2) max_n ||S_n|| pointwise. Integrating (14) for this round range bounds the pairing from the block by

\[
 C_D B |R|^{1/2} W^{-1/2}E_b^{1/2},
\]

where E_b is the squared test norm on that block. Put E_b=0 for absent blocks. Cauchy–Schwarz gives

\[
 W^{-1/2}\sum_{b=1}^W E_b^{1/2}
 \le\left(\sum_{b=1}^W E_b\right)^{1/2}=E^{1/2}.           \tag{16}
\]

The integrated adjoint identity now bounds the full output pairing by C_D B |R|^(1/2) sqrt(E). Every pairing is integrable: (5) bounds each F_s in L², each tested adjoint is L², and there are finitely many terms. Duality in the finite Hilbert sum of the output spaces proves the first inequality in (6).

For the last inequality put x=log_2 D≥1. Since L_D≤5x+2 and

\[
 25(x+1)^2-[9+(5x+2)^2]=30x+12>0,
\]

one has C_D≤(40/3)log_2(2D), as claimed.

## Limits of this verification

The row lemma and its maximal premise hold under (1)–(5) and the stated ordering of partitions and reads. The proof uses no mixing assumption, ergodic theorem or estimate from the companion trilinear-Hilbert-transform paper. It allows empty rounds, several rows on one support, unbounded total catalog size away from each path, repeated read indices, absent input blocks, complex inputs and test-dependent bucket selection.

This lemma cannot be applied to an arbitrary Bessel array without its coefficient, support and refinement hypotheses. In particular, multiplying a row by a stopping mask on part of its support would produce a different row, for which (8) has not been assumed. The bucket construction above avoids that change by assigning whole rows before testing hits on the observation partition.

The local depth-variation theorem also requires the actual analytic constructions to meet these hypotheses and uses detection, separated-scale, localization, core and absorption estimates. Those steps, including the imported estimates from manuscript H, remain unverified here. No conclusion about the correctness of the three preprints' main theorems follows from this isolated check.
