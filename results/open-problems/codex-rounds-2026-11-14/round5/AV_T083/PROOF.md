# Smooth rows on depth inputs with a smaller catalog loss

This verifies Lemma `smooth-depth` in OpenAI, *Pointwise convergence of triple ergodic averages for mixing transformations* (October 4, 2026), [rows.tex](https://github.com/openai/math/blob/main/preprints/Pointwise-convergence-of-triple-ergodic-averages-for-mixing-transformations-October-4-2026/build/paper/sections/rows.tex), and sharpens its dependence on the number of carriers. It is the raw scheduled-input step used in `lem:hbase-scale`, [base.tex](https://github.com/openai/math/blob/main/preprints/Pointwise-convergence-of-triple-ergodic-averages-for-mixing-transformations-October-4-2026/build/paper/sections/base.tex), lines 535–578. The ordinary Bessel inequality for the selected analytic array is a hypothesis here; the scalar construction that supplies it is not verified.

## Statement

Let R be a bounded dyadic interval, with the spatial depth of R equal to an integer s_R. Let N be a finite set of carrier labels, and fix measurable functions m_v on R with |m_v|≤1. Each carrier is the same function at every interval using its label. Let E be any finite set of pairs (I,v), with I a dyadic subinterval of R; a pair occurs at most once. Its depth is s(I)=s_R+log_2(|R|/|I|).

For each selected pair let ω_{I,v} belong to C¹ of the closed interval I, with

\[
 \int_I\omega_{I,v}=0,\qquad
 \|\omega_{I,v}\|_\infty+|I|\|\omega'_{I,v}\|_\infty\le A.
 \tag{1}
\]

Define the scalar row

\[
 W_{I,v}f=|I|^{-1/2}\int_I m_v(y)\omega_{I,v}(y)f(y)\,dy.
\]

Assume the ordinary selected-array Bessel bound

\[
 \sum_{(I,v)\in E}|W_{I,v}f|^2\le B^2\|f\|_{L^2(R)}^2
 \quad\text{for every }f\in L^2(R).                         \tag{2}
\]

Let S be a finite interval of integers containing every s(I), partitioned into W nonempty deterministic consecutive blocks. Suppose the measurable scalar schedule f_s satisfies, on each block b and almost everywhere,

\[
 \max_{s\in b}|f_s(y)|+
 \sum_{s,s+1\in b}|f_{s+1}(y)-f_s(y)|\le W^{-1/2}.          \tag{3}
\]

Set

\[
 d=2+\#N,\quad h_0=\lceil10\log_2(2d)\rceil,\quad
 C_d=\frac83\sqrt{9+(1+\lceil5\log_2d\rceil)^2}.
\]

Then

\[
\begin{split}
 \left(\sum_{(I,v)\in E}|W_{I,v}f_{s(I)}|^2\right)^{1/2}
 \le C_d\big[&\sqrt{h_0+1}(B+3A)\\
       &+2A\sqrt d\sqrt{h_0+3}\,2^{-h_0}\big]|R|^{1/2}       \tag{4}
\end{split}
\]

and in particular

\[
 \left(\sum_{(I,v)\in E}|W_{I,v}f_{s(I)}|^2\right)^{1/2}
 \le140(B+A)\big(\log_2(2d)\big)^{3/2}|R|^{1/2}.            \tag{5}
\]

The manuscript gives 760(B+A)(log_2(2d))²|R|^{1/2}. The change comes from combining disjoint output coordinates in square sum, instead of by the triangle inequality.

## The row estimate used

The catalog-row lemma verified in round 4 is used in its following form. Suppose augmented rows have whole supports in a dyadic partition π_n and tested adjoints are constant-coefficient combinations of persistent columns on a finer observation partition σ_n. Suppose π_{n+1} refines σ_n. A persistent column has one private coordinate of magnitude at least D^{-1}, norm at most D, and there are at most D columns on any spatial path. If the joint ordinary row norm is at most b, and round n reads F_{s_n} from a schedule satisfying (3) in Hilbert norm with nondecreasing s_n, then

\[
 \left(\sum_n\sum_{\rho\text{ in round }n}
             |A_\rho F_{s_n}|^2\right)^{1/2}
 \le C_D b|R|^{1/2},\qquad
 C_D\le\frac{40}{3}\log_2(2D).                             \tag{6}
\]

All rows and columns are fixed when the ordinary operator norm is tested. The [round-4 proof](~/codex_op_1114r4/briefs/AV_T083/PROOF.md) proves (6) from these structural and Bessel hypotheses; it was independently rechecked in this session. Below every application supplies the whole-support and partition hypotheses explicitly.

## Dyadic bump differences and their ordinary norms

Use inner products linear in the first variable. Extend each bump by zero outside I. Let E_h be conditional expectation on the full depth-h partition of R. Exact mean zero gives E_{s(I)} overline(ω_{I,v})=0. For h≥1 define

\[
 q_{I,v,h}=|I|^{-1/2}
       (E_{s(I)+h}-E_{s(I)+h-1})\overline{\omega_{I,v}},
 \quad
 q_{I,v,0}=|I|^{-1/2}E_{s(I)+h_0}\overline{\omega_{I,v}}.
\]

Each q_h is supported on the whole interval I and is constant on depth-(s(I)+h) cells. For h≥1 it lies in the martingale difference space at that depth. The difference between the averages on a child and its parent is at most the oscillation on the parent, which by (1) is at most A2^{-(h-1)}. Multiplying by |I|^{-1/2} and taking the L² norm on I gives

\[
 \|q_{I,v,h}\|_2\le2A2^{-h}.                              \tag{7}
\]

For fixed v,h the q_{I,v,h} are orthogonal as I varies: different support depths have different martingale difference spaces, and intervals at the same depth are disjoint. Uniqueness of the pair (I,v) is used here. Their analysis operator consequently has norm at most 2A2^{-h}. Multiplication by the fixed m_v is a contraction. Summing squared norms over the carrier labels gives the physical lag operator bound

\[
 b_{\mathrm{phys},h}\le2A\sqrt{\#N}\,2^{-h}.                \tag{8}
\]

The derivative bound also gives uniform convergence of dyadic bump averages on I. Thus

\[
 |I|^{-1/2}\overline\omega_{I,v}
      =q_{I,v,0}+\sum_{h>h_0}q_{I,v,h},\qquad
 q_{I,v,0}=\sum_{h=1}^{h_0}q_{I,v,h}.                       \tag{9}
\]

By (8), the physical lag series converges in operator norm. Subtracting its tail from the selected row operator in (2) proves

\[
 b_{\mathrm{phys},0}
 \le B+2A\sqrt{\#N}\,2^{-h_0}\le B+A.                     \tag{10}
\]

Indeed 2^{-h_0}≤(2d)^{-10}, d≥2 and #N≤d imply 2sqrt(#N)2^{-h_0}≤1. Zero extension creates no boundary error, because all conditional-expectation cells used here are descendants of I.

## Augmentation and realization of the row hypotheses

In H=C⊕ℓ²(N), use the root-born persistent columns

\[
 \Phi_v(y)=(\overline{m_v(y)},e_v).
\]

Their norms are at most sqrt(2), their private constants equal one, and the number on any path is #N. They meet the catalog budget D=d. Lift the input to F_s=(f_s,0), preserving (3). Define augmented rows

\[
 \widetilde W_{I,v,h}Z
       =\langle Z,q_{I,v,h}\Phi_v\rangle_{L^2(R;H)}.
\]

On F_s this equals ⟨m_v f_s,q_{I,v,h}⟩, the physical row for that bump piece. The conjugations therefore reproduce the original integral in W after summing (9).

For the private part of a lag operator, orthogonality for each fixed label and then the orthogonal private coordinates give norm at most 2A2^{-h}. Combining this with (8) by Cauchy–Schwarz across the physical and private input summands yields

\[
 \|\widetilde W_h\|
 \le2A\sqrt{\#N+1}\,2^{-h}\le2A\sqrt d\,2^{-h}
 \quad(h>h_0).                                            \tag{11}
\]

For the initial sum the private norm is at most
2A sum_{h=1}^{h_0}2^{-h}≤2A, by (9). With (10) this gives

\[
 \|\widetilde W_0\|\le B+3A.                              \tag{12}
\]

Fix a piece, with observation offset ℓ=h_0 for the initial sum or ℓ=h for a lag. Split support depths into residue classes modulo ℓ+1. Within a class, group all rows of support depth s in one round; its support partition is the full depth-s partition of R and its observation partition is the full depth-(s+ℓ) partition. Empty support cells have no rows. The next selected support depth is at least s+ℓ+1, so its partition refines the preceding observation partition. Every row is supported on its original whole I. Its adjoint on each observation cell is a constant scalar times the same persistent Φ_v. The round reads F_s and the reads increase. Restricting the ordinary array to a residue class preserves (11) or (12). This supplies every hypothesis of (6), with no stopping mask or change to the original rows.

## Combining classes and summing the tail

Let V_0 and V_h be the output vectors on the scheduled inputs in the common finite coordinate space ℓ²(E). For a fixed piece, different residue classes contain disjoint pairs (I,v). Consequently their zero-extended output vectors are orthogonal in ℓ²(E). If b is the ordinary norm of this piece, (6) gives

\[
 \|V\|_{\ell^2(E)}^2
   =\sum_{c=0}^{\ell}\|V_c\|_{\ell^2(E)}^2
   \le(\ell+1)C_d^2b^2|R|.                               \tag{13}
\]

The orthogonality here concerns output coordinates, and does not require the carriers to be orthogonal as functions. Equations (11)–(13) imply

\[
 \|V_0\|\le\sqrt{h_0+1}C_d(B+3A)|R|^{1/2},\qquad
 \|V_h\|\le2AC_d\sqrt d\sqrt{h+1}2^{-h}|R|^{1/2}.
\]

For an integer n≥0, geometric series give

\[
 \sum_{h>n}2^{-h}=2^{-n},\qquad
 \sum_{h>n}(h+1)2^{-h}=(n+3)2^{-n}.
\]

The second identity follows also by putting h=n+j and using
sum_{j≥1}j2^{-j}=2. Weighted Cauchy–Schwarz now gives

\[
 \sum_{h>n}\sqrt{h+1}2^{-h}
 \le\left(\sum_{h>n}2^{-h}\right)^{1/2}
      \left(\sum_{h>n}(h+1)2^{-h}\right)^{1/2}
 =\sqrt{n+3}\,2^{-n}.                                    \tag{14}
\]

The series of scheduled output vectors is therefore summable in norm. Its rowwise sum equals the original output by (9). Minkowski over the pieces, followed by (14) with n=h_0, proves (4).

## The numerical constant

Put l=log_2(2d)≥2. Since h_0=ceil(10l), one has h_0+1≤11l and h_0+3≤12l. Also

\[
 \sqrt d\,2^{-h_0}\le d(2d)^{-10}
      \le2^{-19}<1/100.
\]

Thus the bracket in (4) is at most

\[
 [3\sqrt{11}+(1/50)\sqrt{12}](B+A)\sqrt l
 <(21/2)(B+A)\sqrt l.
\]

For a rational check, sqrt(11)<10/3 and sqrt(12)<7/2, so the square bracket is less than 10+7/100<21/2. Using C_d≤(40/3)l from (6) gives (5), since (40/3)(21/2)=140.

## Scope and edge cases

If E is empty the output is zero, including when N is empty. If A=0 every bump vanishes. If B=0, the assumed inequality forces each original row to be zero; the proof and bound remain valid. Missing depths and empty residue classes only reduce the number of terms in (13). Complex carriers, overlapping carrier functions and arbitrarily small support cells are allowed. The row lemma imposes no bound on the constant coefficients q_h on observation cells.

The hypothesis that a carrier is fixed over all its intervals is essential to (8). So are the selected-array Bessel bound (2), exact bump mean zero, and at most one row per pair (I,v). No estimate for a larger unselected array is assumed.

In `lem:hbase-scale`, this verifies the implication from its asserted selected Bessel bound and finite fixed-carrier catalog to its raw scheduled-input bound. If log(2d) is polynomial in the stated scalar complexity, the power 3/2 remains bounded by a polynomial. It does not prove the scalar Weyl alternative, pooled coefficient envelopes, the selected-array Bessel bound itself, compression for projected inputs, or the completed separated-scale lemma. The main ergodic theorems remain unverified.
