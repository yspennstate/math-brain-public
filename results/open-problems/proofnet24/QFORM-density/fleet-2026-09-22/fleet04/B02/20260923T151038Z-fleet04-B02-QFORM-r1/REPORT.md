SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet04, slot B02, 2026-09-23T15:10:38Z.
attacking: apply D′, D5, and optimized sharp Hausdorff–Young to the same strengthened original-coordinate cross cut.

# fleet04/B02 — strong-cut D5-or-optimized-HY compiler

Programme: \`QFORM-DENSITY-3EIG-20260922\`  
Run: \`20260923T151038Z-fleet04-B02-QFORM-r1\`  
Status: **ESSENTIAL_STEP_APPLIED / FULL QFORM OPEN / GLOBAL CONTINUITY OPEN**

## 1. Exact inputs

The live matrix is the physical cut constructed in fleet04/B20 at

\`yspennstate/math-open-problems@c6f29397b3d45a7cf7ab67633a5451767b478912\`.

For every \(A\in N3(1/64)\) with \(s_3(A)\ge1\), it supplies ORIGINAL-coordinate banks \(J,K\) and

\[
 M=A[J,K],\qquad
 E:=\|M\|_F^2>\frac{11907}{16384}=:c_3. \tag{1.1}
\]

The completed fleet01/B02 theorem actually consumed is \`QFORM-OPTIMIZED-TWOPLUSTAIL-L1-v1\` at

\`yspennstate/math-open-problems@7fbdcedec6fdb0dc4afa1f771f168db1cb4a4b8c\`.

For squared singular values \(x_1\ge x_2\ge\cdots\), put

\[
 T_2=\sum_{r\ge3}x_r,\qquad R_{\rm tail}=T_2/x_3. \tag{1.2}
\]

Let \(h_L,h_R\) be the maximum physical-coordinate leverages of the top-two left and right singular planes. For either orientation define

\[
 \beta=\sqrt{3/R_{\rm tail}},\qquad
 A(h,\beta)=\big(\sqrt h+\beta\sqrt{1-h}\big)^2 \tag{1.3}
\]

in the admissible branch. If \(A_*=\min(A(h_L,\beta),A(h_R,\beta))<3/4\), set \(q_*=\max(1,2A_*)\). The completed theorem gives

\[
 \|p_Q\|_\infty
 \le C(A_*)[x_1x_2T_2]^{-1/6},\qquad
 C(A)=\frac{3e}{(3-2q_*)\sqrt{q_*}}, \tag{1.4}
\]

and

\[
 \int_{\mathbb R}|\phi_Q(t)|\,dt
 \le2\pi C(A_*)[x_1x_2T_2]^{-1/6}. \tag{1.5}
\]

All same-bank quadratic terms, outside couplings, affine terms, signs, and extra spectrum are retained. The random variables are never rotated.

I also retain Claude's corrected D′ theorem: when every third-volume marginal on one orientation is at most \(a<3/4\),

\[
 \|p_Q\|_\infty
 \le
 \frac{6\sqrt e}{\sqrt{2a}(3-4a)}
 E_3(M)^{-1/6}. \tag{1.6}
\]

The unrestricted D5 theorem is used exactly as in fleet04/B20.

## 2. Same-matrix D5 split

Let

\[
 S_4=x_1+x_2+x_3+x_4. \tag{2.1}
\]

The distinct-draw fifth-volume argument on the actual block \(M\) gives

\[
 S_4\le\frac{63}{64}E
 \quad\Longrightarrow\quad
 e_5(M^TM)\ge\frac{E^5}{120\cdot64^4}. \tag{2.2}
\]

D5 therefore yields the concrete full-ambient estimate

\[
 \boxed{\|p_Q\|_\infty<116.502.} \tag{2.3}
\]

Every D5-unpaid state on this same matrix satisfies

\[
 S_4>\frac{63}{64}E. \tag{2.4}
\]

## 3. New strong-cut sharp-HY exit

Assume the D5-unpaid branch (2.4), and exclude for the moment the two low-rank tubes

\[
 x_2<\frac E{64}
 \quad\text{or}\quad
 T_2<\frac E{64}. \tag{3.1}
\]

Since \(x_1\ge S_4/4\), equations (2.4) and (3.1) imply

\[
 x_1>\frac{63E}{256},\qquad
 x_2\ge\frac E{64},\qquad
 T_2\ge\frac E{64}. \tag{3.2}
\]

Hence

\[
 \boxed{x_1x_2T_2>
 \frac{63}{1048576}E^3
 >
 \frac{63}{1048576}c_3^3.} \tag{3.3}
\]

Now suppose

\[
 R_{\rm tail}\ge225,\qquad \min(h_L,h_R)\le\frac12. \tag{3.4}
\]

Then \(\beta\le\sqrt3/15\). The optimized marginal envelope is bounded by

\[
 A_0=
 \frac12\left(1+\frac{\sqrt3}{15}\right)^2
 =0.6221367205045919\ldots, \tag{3.5}
\]

so

\[
 q_*=2A_0=1.24427344100918\ldots,\qquad
 C(A_0)=14.29394117441255\ldots. \tag{3.6}
\]

Applying the completed fleet01/B02 theorem (1.4) to the actual inequality (3.3) gives

\[
 \|p_Q\|_\infty
 <
 C(A_0)
 \left(\frac{1048576}{63}\right)^{1/6}
 c_3^{-1/2}
 =84.7235238114\ldots. \tag{3.7}
\]

Thus

\[
 \boxed{\|p_Q\|_\infty<84.724} \tag{3.8}
\]

and the density is continuous and vanishes at infinity. Moreover,

\[
 \boxed{\int_{\mathbb R}|\phi_Q(t)|\,dt<532.334.} \tag{3.9}
\]

This is the required equation-level consumption of fleet01/B02.

## 4. D′ versus sharp-HY on the same matrix

At the same marginal cap \(a=A_0\), D′ gives the coefficient

\[
 \frac{6\sqrt e}{\sqrt{2A_0}(3-4A_0)}
 =17.3394271408\ldots. \tag{4.1}
\]

Using the identical product floor (3.3), D′ therefore gives

\[
 \boxed{\|p_Q\|_\infty<102.775.} \tag{4.2}
\]

The optimized sharp-HY coefficient is smaller:

\[
 84.724<102.775<116.502. \tag{4.3}
\]

These are three estimates on the same literal source-coordinate matrix, not comparisons across incompatible reductions:

- D5 pays when the top-four energy is dispersed;
- D′ pays the gated third-volume branch;
- optimized sharp-HY pays the same gated branch more sharply and supplies genuine Fourier \(L^1\).

## 5. Exhaustive surviving geometry on the strengthened cut

Combining the two splits proves:

### Theorem — \`QFORM-N3-STRONGCUT-D5-OR-HY-v1\`

Every \(A\in N3(1/64)\) satisfying the target spectral hypothesis has an ORIGINAL-coordinate cross block \(M\) for which at least one of the following holds:

1. **D5 paid:** \(\|p_Q\|_\infty<116.502\);
2. **optimized-HY paid:** continuous \(C_0\) density, \(\|p_Q\|_\infty<84.724\), and \(\int|\phi_Q|<532.334\);
3. **near rank one:** \(x_2<E/64\);
4. **near rank two:** \(T_2<E/64\);
5. **low tail stable rank:** \(T_2/x_3<225\);
6. **double physical hub:** \(h_L>1/2\) and \(h_R>1/2\).

All six alternatives concern the same physical cut with \(E>11907/16384\). No singular tail is deleted.

## 6. Remaining implication and corrections

The first unproved edge is

\`QFORM-STRONGCUT-LOWRANK-LOWSTABLERANK-OR-DOUBLEHUB-PAYMENT-v1\`.

The live difficulty is not lack of cross energy: the cut has fixed energy \(>0.7267\). It is the conjunction of top-four concentration with either a near-rank-one/two tube, insufficient collective tail, or heavy physical anchors on both singular planes. Existing grouped and Schur receivers pay exact-rank-one or genuine-pivot subcases, but arbitrary same-bank leakage and a nonzero transverse tail are not covered uniformly.

Corrections preserved:

- no independence after a singular-vector rotation;
- no arbitrary-joint coarea theorem;
- no worst conditional-density supremum;
- no pointwise scalar quadratic-phase estimate;
- no deletion of a small quadratic tail on unbounded inputs;
- no inference that a heavy singular-vector coordinate automatically creates an invertible physical pivot.

The full conjecture and global continuity remain open.
