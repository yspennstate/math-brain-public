SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B11, 2026-09-24T00:14:44Z.
attacking: the rank-one doubly-transverse shared-hub collar; expose the exact null-wing geometry and turn every nonzero wing into a genuine three-dimensional source crossing.

# Early calculation — rank-one transverse crossing normal form

Let an exact-rank-three symmetric form be split over a physical hub `i` and disjoint ORIGINAL-coordinate banks `L,R`. Write

\[
a=A_{ii},\qquad c=A[L,i],\qquad r=A[i,R],\qquad N=A[L,R],
\]
with `c,r` nonzero. Put `alpha=||c||`, `beta=||r||`, `e=c/alpha`, `f=r/beta`, and

\[
C=P_eNP_f.
\]

Assume `rank C=1`, with singular value `sigma>0` and singular unit vectors `v in e^perp`, `z in f^perp`, so `C=sigma v z^T`. Define the invariant null-wing vectors

\[
p_0=(I-ee^T-vv^T)Nf,\qquad
q_0=(I-ff^T-zz^T)N^Te.
\]

In orthonormal source bases beginning with `(e,v)` on `L` and `(f,z)` on `R`, the whole hub-to-bank rectangular block is

\[
B=\begin{pmatrix}
a&\beta&0&0\\
\alpha&d&q&q_0^T\\
0&p&\sigma&0\\
0&p_0&0&0
\end{pmatrix}.
\]

The displayed scalar `p_0,q_0` entries mean coordinates after rotating each null subspace so its wing vector is first. Direct minors give:

1. if `q_0 !=0`, the cross block `A[{i} union L,R]` has a 3x3 minor of absolute determinant `beta*sigma*||q_0||`;
2. if `p_0 !=0`, the cross block `A[L,{i} union R]` has a 3x3 minor of absolute determinant `alpha*sigma*||p_0||`;
3. if both wings are nonzero, `N` itself has a 3x3 minor of absolute determinant `sigma*||p_0||*||q_0||`;
4. because `rank A<=3`, the 4x4 minor satisfies
\[
0=\det B=-a\,\sigma\,||p_0||\,||q_0||,
\]
so two nonzero wings force the physical hub pivot `a=0`.

Therefore every nonzero wing creates an actual rank-three crossing between disjoint original-coordinate banks. In the exact-rank-three setting its crossing rank is exactly three, so the completed fleet02/B11 cross-bank theorem applies. If both wings vanish then
\[
N=[e\ v]\begin{pmatrix}d&q\\p&\sigma\end{pmatrix}[f\ z]^T,
\]
which is the exact coplanar residual. This isolates the next collar without discarding any coefficient.

This is an early calculation only; the final report will state the quantitative density consequences and the remaining uniform-through-zero gap.
