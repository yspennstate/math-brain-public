SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B11, 2026-09-23T02:12:43Z.
attacking: the remaining opposite-sign branch through an original-coordinate opposite-diagonal pair exit and a minority-cone physical-pivot compiler.

# account03/B11 r22 — opposite-sign pair exit and minority-cone pivot

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260923T021243Z-account03-B11-QFORM-r22`  
**Status:** `ESSENTIAL_STEP_APPLIED / TWO_SUPPORTING_THEOREMS / PARTNER_RESULT_APPLIED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The full owner target is **not** proved here. The new result pays two concrete indefinite branches without rotating the random inputs, and narrows the exact-rank-three two-sheet obstruction to the near-null/low-cross-rank region.

## 1. Fresh sources actually used

Fresh `math-research-brain` main at startup was

`e83382e04b0966b933d698cdf95e0388dbc97312`,


The current owner continuation requires application of the volume-stability package

`yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`,
`proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`.

The sign-sensitive physical-fibre input used below is account01/B06,

`yspennstate/math-open-problems@ac50e5d5f2c3030c4bd87d5188117d92ceaf55a1`,
`proofnet24/QFORM-density/fleet-2026-09-22/account01/B06/20260922T233555Z-qform-r19-b06/REPORT.md`,

especially `QFORM-CURVATURE-WEIGHTED-PHYSICAL-FIBER-COVER-v1` and its two-sheet cone-only version.

The arbitrary-rank determinant-only physical-pair theorem used in Section 2 is

`yspennstate/math-open-problems@472b70df7d1edbb3afac23269bc2e4368ae0e371`,
`proofnet24/QFORM-density/interactive/20260922T225732Z-claude-synthesis/GEOMETRIC_SYNTHESIS.md`, Theorem 3.1.

The designated partner account04/B11 result actually applied is

`yspennstate/math-open-problems@4110bbfd21beffa0260a017d468b0a486af56db1`,
`proofnet24/QFORM-density/fleet-2026-09-22/account04/B11/20260922T222040Z-account04-B11-cone-envelope-r3/REPORT.md`.

No result below treats repository transport as native learned-memory ingestion.

## 2. Full-matrix opposite-diagonal pair exit

This first theorem is not restricted to exact rank three.

### Theorem 2.1 — `QFORM-OPPOSITE-DIAGONAL-PAIR-EXIT-v1`

Let `A` be any real symmetric matrix with

\[
s_3(A)\ge1.
\]

Suppose two ORIGINAL coordinates `i != j` satisfy, for some \(\eta>0\),

\[
A_{ii}\ge\eta,\qquad A_{jj}\le-\eta.
\tag{2.1}
\]

Then for every independent cap-one product input and every affine perturbation,

\[
\boxed{
\|p_{X^TAX+b^TX+c}\|_\infty
\le
\eta^{-1}\Big(9.2+\log_+(10000\eta)\Big).
}
\tag{2.2}
\]

In particular, at \(\eta=1/4\),

\[
\|p_Q\|_\infty<68.097.
\tag{2.3}
\]

### Proof

Take the physical principal pair

\[
B=\begin{pmatrix}A_{ii}&A_{ij}\\A_{ij}&A_{jj}\end{pmatrix}.
\]

Its determinant is strictly negative and

\[
D:=|\det B|
=A_{ij}^2-A_{ii}A_{jj}
\ge \eta^2.
\tag{2.4}
\]

Hence `B` is a nonsingular indefinite ORIGINAL-coordinate pair. The determinant-only pair theorem quoted above applies to the full ambient matrix, including arbitrary remaining spectrum, couplings and affine terms:

\[
\|p_Q\|_\infty
\le D^{-1/2}\Big[9.2+\log_+(10000\sqrt D)\Big].
\tag{2.5}
\]

The source theorem records that the right side is decreasing in `D>0`; insert `D>=eta^2` to obtain (2.2). No condition number of `B` appears. QED.

### Consequence for the indefinite proof map

At any fixed physical-diagonal threshold \(\eta\), an unpaid indefinite matrix can be assumed **not** to contain simultaneously a positive diagonal at least \(\eta\) and a negative diagonal at most \(-\eta\). Thus a genuinely remaining opposite-sign case must have one physical sign represented only by small diagonals, or have all diagonals small. This is exactly the regime where pair selection by determinant alone stops being automatic.

The classical opposite-sign rank-two control is retained: with only two large directions, a saddle such as `2XY` for centered unit uniforms has logarithmically unbounded density at zero. The third large spectral direction is used by the full-matrix pair theorem through the nontrivial Schur remainder; it is not silently discarded.

## 3. Exact-rank-three minority-cone pivot theorem

Now specialize to a genuinely rotated exact-rank-three signature `(2,1)` form

\[
A=R\Lambda R^T,\qquad R^TR=I_3,
\qquad \Lambda=\operatorname{diag}(\lambda_1,\lambda_2,-\mu),
\tag{3.1}
\]

with \(\lambda_1,\lambda_2,\mu\ge1\). Put

\[
L=\max(\lambda_1,\lambda_2,\mu).
\]

Let `r_i` be the `i`-th row of `R` and \(q_i=\|r_i\|\le1\).

### Theorem 3.1 — `QFORM-MINORITY-PHYSICAL-PIVOT-TWOSHEET-v1`

Assume some ORIGINAL physical diagonal has the minority sign:

\[
A_{ii}=r_i^T\Lambda r_i=-c_i<0.
\tag{3.2}
\]

Then the two-sheet/minority half-line satisfies

\[
\boxed{
\operatorname*{ess\,sup}_{t<0}p_Q(t)
\le8\sqrt{\pi e}\left(\frac{L}{c_i}\right)^2.
}
\tag{3.3}
\]

Consequently, if \(c_i\ge\eta L\),

\[
\boxed{
\|p_Q\|_\infty
\le
\max\{\pi\sqrt2,\,8\sqrt{\pi e}\eta^{-2}\}.
}
\tag{3.4}
\]

The first term is the completed ruled one-sheet bound. Numerically,

\[
\pi\sqrt2=4.4428829381\ldots,
\qquad
8\sqrt{\pi e}=23.3782589226\ldots.
\]

For signature `(1,2)`, reflect `Q -> -Q`: the same theorem applies when one physical diagonal has the sign of the unique positive eigenvalue, and the two half-lines exchange roles.

### Proof

The account01/B06 cone-cover theorem is expressed in the spectral-gradient variable `z`. Define the two-sheet cone

\[
\mathcal C_-:=\{z\ne0:z^T\Lambda^{-1}z<0\}.
\tag{3.5}
\]

Put

\[
D=\operatorname{diag}(\sqrt{\lambda_1},\sqrt{\lambda_2},\sqrt\mu),
\qquad z=Du.
\]

Then `z in C_-` means

\[
u_1^2+u_2^2-u_3^2<0,
\qquad |u_3|>\|(u_1,u_2)\|.
\tag{3.6}
\]

Set

\[
a=\sqrt\mu|r_{i3}|,
\qquad
b=\sqrt{\lambda_1r_{i1}^2+\lambda_2r_{i2}^2}.
\tag{3.7}
\]

Equation (3.2) is exactly

\[
c_i=a^2-b^2>0,
\tag{3.8}
\]

so `a>b`. For every `z=Du in C_-`,

\[
\begin{aligned}
|r_i\cdot z|
&=|(Dr_i)\cdot u|\\
&\ge a|u_3|-b\|(u_1,u_2)\|\\
&\ge(a-b)|u_3|\\
&\ge\frac{a-b}{\sqrt2}\|u\|\\
&\ge\frac{a-b}{\sqrt{2L}}\|z\|.
\end{aligned}
\tag{3.9}
\]

Moreover

\[
a-b=\frac{c_i}{a+b},
\qquad
a+b\le\sqrt2|Dr_i|\le\sqrt{2L}\,q_i.
\tag{3.10}
\]

Therefore the Euclidean cone margin

\[
m_i:=\inf_{z\in\mathcal C_-}\frac{|r_i\cdot z|}{\|z\|}
\]

obeys

\[
\boxed{m_i\ge\frac{c_i}{2Lq_i}.}
\tag{3.11}
\]

This is the sign-specific geometric step. The row is timelike precisely because its physical diagonal has the minority sign.

Now take the single cone-cover weight

\[
a_i=m_i^{-2},
\]

all other weights zero. Then on `C_-`,

\[
a_i(r_i\cdot z)^2\ge\|z\|^2.
\tag{3.12}
\]

The cone-only account01/B06 theorem therefore gives

\[
\operatorname*{ess\,sup}_{t<0}p_Q(t)
\le
\frac{2\sqrt\pi}{\sqrt{|\det\Lambda|}}
 m_i^{-2}\sqrt{q_i|\Lambda r_i|}\sqrt{M_i},
\tag{3.13}
\]

where `M_i` is the genuine two-dimensional ORIGINAL-product projection factor. Its proved bound is

\[
M_i\le e.
\tag{3.14}
\]

Because every eigenvalue magnitude is at least one,

\[
|\det\Lambda|=\lambda_1\lambda_2\mu\ge L,
\qquad
|\Lambda r_i|\le Lq_i.
\]

Hence

\[
\frac{\sqrt{q_i|\Lambda r_i|}}{\sqrt{|\det\Lambda|}}
\le q_i\le1.
\tag{3.15}
\]

Use (3.11), (3.14), (3.15):

\[
\operatorname*{ess\,sup}_{t<0}p_Q(t)
\le2\sqrt{\pi e}\,m_i^{-2}
\le8\sqrt{\pi e}\frac{L^2q_i^2}{c_i^2}
\le8\sqrt{\pi e}\left(\frac L{c_i}\right)^2.
\]

This proves (3.3). The completed one-sheet estimate is at most `pi sqrt(2)/s` with `s=min(lambda_1,lambda_2,mu)>=1`, hence at most `pi sqrt(2)`. Taking the larger half-line bound proves (3.4). QED.

### Why this addresses the rank-two logarithm

On the minority side, a physical row with `A_ii<0` has a linear functional `r_i dot z` that cannot vanish on the two-sheet cone except at the vertex: (3.11) gives a quantitative angular gap. In the physical-fibre identity, this creates a nonvanishing gradient partition before the one-dimensional fibre is integrated. The remaining two-dimensional transverse product projection has a genuine density cap, and its reciprocal-distance integral is finite. In rank two the analogous cone consists of lines and the reciprocal Jacobian integrates logarithmically; the third direction creates a two-dimensional transverse curvature payment.

No arbitrary joint projection density is substituted for product provenance: `M_i<=e` comes from the actual original-coordinate product marginal appearing in the account01/B06 theorem.

## 4. Designated partner applied at the exact-null boundary

The new cone-pivot theorem deliberately degenerates when `A_ii=0`. The designated account04/B11 theorem supplies a complementary exact-null case.

Take independent cap-one `X_1,X_2,X_3` and

\[
H_0=
\begin{pmatrix}
0&0&1\\
0&1&0\\
1&0&0
\end{pmatrix},
\qquad
Q=2X_1X_3+X_2^2.
\tag{4.1}
\]

Since `H_0^2=I`, `tr(H_0)=1`, and `det(H_0)=-1`,

\[
\operatorname{spec}(H_0)=\{1,1,-1\}.
\]

The partner's null-scalar theorem applies with

\[
L=M=|\alpha|=|\beta|=1,
\]

and gives the actual inequality

\[
\boxed{
\|p_Q\|_\infty
\le3\,2^{2/3}
=4.7622031559\ldots.
}
\tag{4.2}
\]

Thus the zero-diagonal boundary is not inherently singular once a genuine independent null scalar and transverse pair survive. What remains difficult is compiling that product provenance from an arbitrary near-null high-dimensional matrix.

## 5. Current volume-stability theorem applied

The current owner-required package proves the following exit. For disjoint ORIGINAL coordinate banks with cross block

\[
M=M_0+E,
\]

if

\[
s_3(M_0)\ge a>0,
\qquad
\max_i(P_{\operatorname{range}M_0})_{ii}\le\frac12,
\qquad
\|E\|_{op}\le\frac a{16},
\tag{5.1}
\]

then the **entire ambient quadratic-plus-affine form**, with arbitrary within-bank self curvature and arbitrary outside couplings, has a continuous `C_0` density satisfying

\[
\boxed{\|p_Q\|_\infty<23/a.}
\tag{5.2}
\]

This is not used as a small-random-variable perturbation. It retains the actual perturbed cross block in the Fourier/volume argument.

Combining (3.4) with (5.2) gives a precise residual description for the exact-rank-three indefinite chamber at any fixed universal thresholds `eta,a_0`: after removing the branches already paid, one may assume simultaneously

1. every physical diagonal carrying the minority spectral sign has magnitude `< eta L`;
2. no original-coordinate cross block satisfies the volume-stability certificate with `a>=a_0`;
3. any exact-null row not already paid by the designated partner lacks the required disjoint scalar/pair product provenance.

That is a genuine narrowing of the opposite-sign obstruction rather than a change to an easier subclass.

## 6. Worked genuinely rotated example

Take the orthogonal rotation in the `(1,3)` plane through `theta=pi/6` and

\[
\Lambda=\operatorname{diag}(1,1,-1).
\]

Then in original coordinates

\[
A=
\begin{pmatrix}
1/2&0&-\sqrt3/2\\
0&1&0\\
-\sqrt3/2&0&-1/2
\end{pmatrix},
\tag{6.1}
\]

whose spectrum is exactly `{1,1,-1}`. The physical pair on coordinates `{1,3}` has

\[
\det A_{\{1,3\}}=-1.
\]

The full-matrix pair theorem therefore gives

\[
\|p_Q\|_\infty
\le9.2+\log(10000)
=18.4103403719\ldots,
\tag{6.2}
\]

for **arbitrary** independent cap-one laws, despite the eigen-coordinates being a nontrivial rotation of the physical coordinates. This is a clean control showing the argument is not secretly diagonalizing the inputs.

## 7. Remaining gap and next mechanism

The full conjecture remains `OPEN / NOT PROVED / NOT DISPROVED`.

The first B11 obligation after this run is now the **near-null one-sign / low-cross-rank aggregate**:

- opposite-sign physical diagonals at a fixed scale are paid by Theorem 2.1;
- in exact rank three, a minority-sign diagonal separated from zero relative to the spectral maximum is paid directly on the difficult two-sheet side by Theorem 3.1;
- a current near-diffuse rank-three cross certificate is paid by (5.2);
- a canonical exact-null scalar/pair endpoint is paid by the designated partner.

The remaining case has no such fixed-scale certificate. The next step must aggregate many near-null original rows or a hub/star bank **before inversion**, retaining product provenance. Small operator-norm coefficients may not be discarded on unbounded inputs, and a bounded conditional density may not be treated as independence.

## 8. Regularity status

Theorems 2.1 and 3.1 establish essential boundedness in their stated scopes. The current volume-stability branch additionally supplies a continuous `C_0` representative. This run does **not** prove a universal continuity conclusion from the new cone-pivot theorem itself.

## 9. Rank-two control retained

For iid `Unif[-1/2,1/2]` variables `X,Y`,

\[
p_{2XY}(t)=\log\frac1{2|t|}
\]

near zero (on its support), so the opposite-sign rank-two problem is genuinely unbounded. None of the estimates above claim otherwise. Every bounded branch uses a third substantial direction through either the Schur remainder, two-dimensional transverse curvature, or a rank-three volume certificate.
