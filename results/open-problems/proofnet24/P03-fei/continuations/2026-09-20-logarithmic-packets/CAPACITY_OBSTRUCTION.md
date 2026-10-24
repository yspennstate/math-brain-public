# Even all directional coefficient capacities do not imply FEI

20 September 2026. Companion to `REPORT.md`.

**This is a counterexample to a real-valued relaxation, not to FEI.** It uses the preceding Hadamard construction but replaces its independent control labels by all pairs from two families of control blocks. This change makes every Fourier-coefficient/influence inequality hold, in every input direction, while erasure entropy divided by spectral energy remains unbounded. Exact Booleanity is not obtained. Publication priority and independent review are not claimed.

## 1. The constraint being tested

For an exactly Boolean function f, every Fourier coefficient and every direction v obey

\[
|\widehat f(S)|\le
\begin{cases}
\alpha_f(v),&S\cdot v=1,\\
1-\alpha_f(v),&S\cdot v=0,
\end{cases}
\qquad \alpha_f(v)=\Pr[f(x)\ne f(x+v)].
\tag{1}
\]

The first case is obtained by taking the Fourier coefficient of `(f-f(.-v))/2`; the second by using `(f+f(.-v))/2`. Both functions have absolute value equal to their squared value, pointwise. For any normalized real function, the corresponding spectral directional energy is

\[
\alpha^{\rm sp}_u(v)=\sum_{S:S\cdot v=1}\widehat u(S)^2.
\]

It is not generally a disagreement probability. The following family satisfies (1) with alpha replaced by this spectral energy **for every S and every v**, not merely for the coordinate directions. It also has dyadic Fourier coefficients and arbitrarily many exact low-order identities for u squared. Nevertheless its B/I ratio diverges.

## 2. An explicit bilinear-control family

Take q=2^k with k>=2, K=q^2, and m=3K/4. Let U_1,...,U_q and V_1,...,V_q be the parity characters of 2q mutually disjoint physical blocks, each of size w>=1. The m physical data signs x_i are independent of those blocks. Index pairs (a,b) by the binary group F_2^(2k), and choose m distinct nonzero columns i of its Walsh matrix H, so H_(a,b),i=(-1)^((a,b) dot i). Put

\[
L_{ab}(x)=\frac1{2q}+\frac1K\sum_{i=1}^m H_{(a,b),i}x_i,
\qquad
G(x,y)=\sum_{a,b}U_aV_bL_{ab}(x).
\tag{2}
\]

Let C_ab be the union of the a-th U block and b-th V block. The complete Fourier spectrum is

\[
\widehat G(C_{ab})=\frac1{2q},\qquad
\widehat G(C_{ab}\cup\{i\})=\frac{H_{(a,b),i}}K.
\tag{3}
\]

All other coefficients vanish. Unlike the earlier independent-centre example, the centres now overlap systematically. Each has width 2w, and each control coordinate belongs to q centres.

### Theorem

The functions in (2) satisfy

\[
\mathbb EG^2=1,\qquad I_{\rm sp}(G)=2w+\frac34,
\tag{4}
\]
\[
\boxed{B(G)=\frac34\log_2(1+K/4)
+\frac{3K}{16}\log_2(1+4/K).}
\tag{5}
\]

Every control coordinate has spectral energy 1/q and every data coordinate has spectral energy 1/K. All inequalities (1), with spectral directional energy, hold in every direction. Furthermore

\[
\widehat{G^2}(A)=0\quad(1\le |A|\le2w-1),
\qquad \mathbb E G^4\le9,
\qquad \|G\|_\infty\le q.
\tag{6}
\]

Every physical restriction fixing at most 2w-1 coordinates has squared norm exactly one. The functions are not Boolean. For fixed w,

\[
\boxed{\frac{B(G)}{I_{\rm sp}(G)}>
\frac3{8w+3}\log_2(1+K/4)\longrightarrow\infty.}
\tag{7}
\]

One may also let w tend to infinity with w=o(log K), so the number of exact square-cancellation identities tends to infinity while the ratio still diverges.

## 3. Normalization, entropy, and failure of Booleanity

Walsh-column orthogonality gives, for every fixed data assignment,

\[
\sum_{a,b}L_{ab}(x)^2=\frac14+\frac mK=1.
\tag{8}
\]

The control characters U_a V_b are distinct and orthogonal. Thus E_control G^2=1, proving normalization. The spectral law is a product of a uniform pair (a,b) and a data label Z, where

    Pr[Z=empty]=1/4,   Pr[Z={i}]=1/K.

This proves all coordinate energies in (4). No two distinct control centres differ by one physical bit. Therefore control-coordinate erasure terms vanish. For each data coordinate, summing the K centre/leaf edges gives E(1/4,1/K). Summing over m proves (5).

In G squared, the diagonal terms give (8). The product of two distinct centre characters contains either two or four complete control blocks. Multiplication of the L polynomials adds zero, one, or two data coordinates. Every remaining nonconstant Fourier label thus contains at least 2w control coordinates. This proves the cancellation in (6). Conditional expectation on any set of fewer than 2w physical coordinates retains only the constant square coefficient, proving the stronger restriction statement.

For fixed data, Cauchy-Schwarz and (8) give |G|<=sum_ab|L_ab|<=q. For the fourth moment, condition on V and apply the Rademacher fourth-moment inequality to the U sum:

    E_U G^4 <= 3 (sum_a (sum_b L_ab V_b)^2)^2.

For any two rows r,s of L, Cauchy-Schwarz and the same fourth-moment bound imply

    E_V [(r dot V)^2 (s dot V)^2] <= 3 ||r||_2^2 ||s||_2^2.

Sum over rows and use (8) to obtain E G^4<=9.

Finally, when all U and V parities equal +1, the nonzero Walsh columns sum to zero, so G=q/2 for every data assignment. Since q>=4, these are values at least two on a positive-measure set. Thus G is not Boolean. The q=2 endpoint is intentionally excluded: it can collapse to an exact addressing-type Boolean function and would not prove non-Booleanity by this argument.

## 4. Proof of every-direction coefficient capacity

A physical direction v induces signs s_a on the U blocks, t_b on the V blocks, and d_i on the data variables. Let bars denote averages over a or b. Let d_empty=1. Under the squared Fourier law,

\[
\mathbb E[(-1)^{S\cdot v}]
=\bar s\,\bar t\,c_D,
\qquad c_D=\frac14+\frac1K\sum_i d_i\in[-1/2,1].
\tag{9}
\]

For any supported label S, inequality (1) is equivalent to

\[
|\widehat G(S)|\le
\Pr_{T\sim\widehat G^2}[T\cdot v=S\cdot v].
\tag{10}
\]

Fix a centre (a,b). Each of s_a bar s and t_b bar t belongs to [-1+2/q,1], because the average includes the designated sign itself. Their product R therefore belongs to [-1+2/q,1]. For the centre label (with empty data label), its agreement probability in (10) is `(1+R c_D)/2`. Since q>=4, the ranges imply

    R c_D >= -1+2/q,

so the agreement probability is at least 1/q. Its coefficient has magnitude 1/(2q), which is smaller.

For a data label i, the corresponding aligned data correlation d_i c_D belongs to [-1+2/K,1]. Indeed, if d_i=+1 its range is [-1/2+2/K,1]; if d_i=-1 its range is [-1+2/K,1/2]. Multiplying by R gives

    R d_i c_D >= -1+2/K,

because K>=q. Therefore the agreement probability for that leaf is at least 1/K, exactly its coefficient magnitude. Zero Fourier coefficients trivially satisfy (1). This covers every physical direction, including directions mixing control and data variables and those flipping several bits in a control block. No counting only of unit directions is substituted for this assertion.

## 5. What the construction rules out, and what it does not

The packet proof in the main report uses exact Booleanity through coefficient capacities such as (1). Those inequalities suffice for the stated bounded-incidence packet theorem, but the present family proves that they cannot, by themselves, establish a universal global B<=C I inequality. Adding Parseval, dyadic coefficients, bounded fourth moment, all directional versions of (1), and any prescribed finite range of exact square-convolution constraints still does not suffice.

This does not refute the bounded-incidence packet bound. For the full family of centres here, the uniform incidence load is Lambda=q/(2w), which is unbounded with q at fixed w. The sharp abstract packet estimate is actually exact: its E=3/4 and L/E=q/2 give B=(3/4)Theta(q/2). Thus neither the packet theorem nor its logarithmic sharpness is contradicted.

The missing step cannot simply be to repackage coefficientwise capacities while discarding the remaining Boolean constraints. The pointwise statement `(D_i f)^2=|D_i f|` and the complete signed convolution equations contain more information. This note does not prove that those additional identities yield a universal allocation. It isolates a precise insufficiency, not an FEI disproof or full proof.

## 6. Executed checks and provenance

`verify_capacity_obstruction.py` checks the sparse Walsh construction, its complete signed square convolution, exact energies, nontrivial erasure edges, coefficient capacities and restriction normalization in the stated finite cases. It separately checks every combinatorial direction type for q=4,8,16 by integer inequalities, retaining the status of each designated centre and data sign. These compressed types cover all directions in those cases; huge truth tables are not generated. Analytic parameter evaluations are not enumerations of their functions. See the actual JSON for counts.

This construction was developed after the main packet report, which did not assert that coefficient capacity alone closes FEI. It uses the preceding conversation's Hadamard columns and logarithmic data law, but changes the centre geometry from independent labels to a complete bipartite family. The argument in Section 4 and the proof of (4)--(7) are supplied here; no inaccessible earlier report is required as a mathematical premise. Standard Walsh orthogonality and Rademacher fourth moments are not new ingredients. No publication-priority or independent-audit claim is made.
