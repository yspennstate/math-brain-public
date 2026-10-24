# Five crossings defeat the component-boundary comparison

Date: 2026-10-02. **Rigorous obstruction to a proposed method; novelty unverified.**

This note concerns the following proposed comparison. For a Boolean function
of a positive weighted score, decompose its attained positive and negative
score blocks into their maximal interval components. If (E_j^+) and
(E_j^-) are those components, let
\[
 B_+(f)=\sum_j I(1-2\mathbf 1_{E_j^+}),\qquad
 B_-(f)=\sum_j I(1-2\mathbf 1_{E_j^-}).
\]
The question was whether, for a fixed number (m) of actual sign jumps,
\[
 \min\{B_+(f),B_-(f)\}\le D_m I(f)
 \tag{1}
\]
could hold with a constant independent of dimension and positive weights.
It does not: **five actual sign jumps already give an unbounded ratio.**

This is not a counterexample to FEI. It obstructs this particular reduction
of arbitrary finite-crossing functions to disjoint parallel slabs.

## Construction

Let (n=2d\ge2), let (x\in\{-1,1\}^n), and introduce one further
coordinate (z\in\{-1,1\}). Define strictly positive weights
\[
 w_i=1+2^{-i}\quad(1\le i\le n),\qquad
 W=1+\sum_{i=1}^n w_i=n+2-2^{-n}.
\]
Write (s(x)=\sum_iw_ix_i). The full score is
\[
 T(z,x)=Wz+s(x).
\]
The two copies of the small-coordinate cube have disjoint score ranges:
(T(-1,x)\le-1) and (T(1,x)\ge1).

Let (v_i=1) for (i\le d) and (v_i=-1) for (i>d). It has
unweighted sum zero and weighted score
\[
 t=s(v)=1-2^{1-d}+2^{-n}.
\]
Set (\eta=2^{-n}). Define (F:\mathbb R\to\{-1,1\}) by the
five increasing breakpoints
\[
 a_1=-W+t-\eta,\quad a_2=-W+t+\eta,\quad a_3=0,
 \quad a_4=W+t-\eta,\quad a_5=W+t+\eta,
\]
with the successive labels
\[
 -,\ +,\ -,\ +,\ -,\ +.
\]
Endpoint labels may be assigned arbitrarily; no score is an endpoint.
Finally put (f(z,x)=F(T(z,x))).

Every score (s(x)) is an odd integer divided by (2^n), since its
integer part has that denominator and
\(\sum_i2^{-i}x_i\) has an odd numerator. Distinct points have distinct
scores: scores from different unweighted layers have disjoint ranges,
and within a layer the finite binary expansion is injective. Their
minimum possible spacing is therefore at least (2^{1-n}). Consequently
the interval ((t-\eta,t+\eta)) contains exactly (s(v)).

More concretely, (v) is the unique largest-score point in the central
Hamming layer. To maximize \(\sum_i2^{-i}x_i\) with exactly (d)
positive signs, one must choose the (d) largest perturbation weights.
All points with unweighted sum at most (-2) have score below (-1),
and all points with unweighted sum at least (2) have score above (1).
Thus, writing (L) and (U) for the sets below and above the hole,
\[
 \begin{aligned}
 L&=\{x:s(x)<t-\eta\}
   =\{x:\textstyle\sum_i x_i<0\}
      \cup\bigl(\{x:\textstyle\sum_i x_i=0\}\setminus\{v\}\bigr),\\
 U&=\{x:s(x)>t+\eta\}
   =\{x:\textstyle\sum_i x_i>0\}.
 \end{aligned}
 \tag{2}
\]
The sets (L,U,\{v\}) partition the small cube, and all three are
nonempty. In each score copy, the isolated point has the opposite label
from the rest of that copy. Hence all six alternating attained blocks are
nonempty, so there are exactly five actual sign jumps, even after empty
score pieces are removed and same-label adjacent blocks are merged.

The function has the particularly simple form
\[
 \boxed{f(z,x)=z\bigl(1-2\mathbf 1_{\{v\}}(x)\bigr).}\tag{3}
\]

## Actual influence

Flipping (z) always changes (f). For every small coordinate (i),
flipping (x_i) changes (f) exactly on the two small-cube vertices
(v) and (v^{\oplus i}). Thus, with (q=2^{-n}),
\[
 \boxed{I(f)=1+2nq.}\tag{4}
\]

## Both component sums

The three positive components are
\[
 E_1^+=\{z=-1,x=v\},\qquad
 E_2^+=\{z=1,x\in L\},\qquad
 E_3^+=\{z=1,x\in U\}.
\]
The three negative components are
\[
 E_1^-=\{z=-1,x\in L\},\qquad
 E_2^-=\{z=-1,x\in U\},\qquad
 E_3^-=\{z=1,x=v\}.
\]
They have the same summed influence, by the symmetry between the two
values of (z).

For any small-cube set (A) and either sign (sigma), the function
(g_A=1-2\mathbf 1_{\{z=\sigma,x\in A\}}) satisfies
\[
 I(g_A)=\Pr(A)+\tfrac12 I(1-2\mathbf 1_A).
 \tag{5}
\]
The first term is the (z)-influence; each small-coordinate influence
is half its corresponding small-cube influence.

Let (C_n=\binom n{n/2}). Every central-layer vertex has (d)
neighbors below that layer and (d) above it. For a cut that includes
all strictly lower layers and an arbitrary subset of the central layer,
each central vertex accounts for exactly (d) cut edges, regardless of
which side it occupies. No other edge crosses the cut. Therefore
\[
 I(1-2\mathbf 1_L)=I(1-2\mathbf 1_U)
     =\frac{2dC_n}{2^n}=\frac{nC_n}{2^n}.
 \tag{6}
\]
Also (I(1-2\mathbf 1_{\{v\}})=2nq). Summing (5) for the partition
(L,U,\{v\}), whose probabilities sum to one, gives
\[
 \boxed{B_+(f)=B_-(f)=1+\frac{nC_n}{2^n}+nq.}\tag{7}
\]
Combining (4) and (7),
\[
 \boxed{\frac{\min\{B_+(f),B_-(f)\}}{I(f)}
   =\frac{1+n\binom n{n/2}/2^n+n2^{-n}}
          {1+2n2^{-n}}.}\tag{8}
\]

## Divergence without an asymptotic approximation

For every (d\ge1),
\[
 \frac{\binom{2d}d}{4^d}\ge\frac1{2\sqrt d}.
\]
An induction proves this: it is equality at (d=1), and the ratio of
successive left sides is ((2d+1)/(2d+2)), which is at least
\(\sqrt{d/(d+1)}\), because the difference of their squares is
(1/[4(d+1)^2]>0).
Thus (nC_n/2^n\ge\sqrt{n/2}). Also (1+2n2^{-n}\le2) for
even (n\ge2). Formula (8) is at least
\[
 \frac{\sqrt{n/2}}2,
\]
which diverges. In fact it is asymptotic to (sqrt{2n/\pi}).
There can therefore be no dimension-free (D_5) in (1), nor a
dimension-free constant for the class with at most (m) crossings for
any (m\ge5).

## Why this says nothing against FEI

Equation (3) is a dictator multiplied by a one-point flip. Multiplication
by an independent dictator merely appends (z) to every Fourier set, so
it leaves spectral entropy unchanged. The spectral probabilities of the
small-cube factor are ((1-2q)^2) at the empty set and (4q^2) at
each of the (2^n-1) nonempty sets. Consequently
\[
 H(f)=(1-2q)^2\log_2\frac1{(1-2q)^2}
       +(2^n-1)4q^2(2n-2),
\]
which tends to zero, whereas (I(f)\) tends to one.

The obstruction comes from geometrically splitting both large label
regions around a very rare attained-score hole. Their component
boundaries see a central threshold of influence order (sqrt n),
although the Boolean function itself sees only the hole's tiny boundary.
Choosing the other label does not remove that effect in this construction.

The separately written [exact checker](verify_global_component_boundary_obstruction.py)
enumerates the weighted construction and all component boundaries in small
dimensions and checks the closed formulas above. Its
[results](global_component_boundary_obstruction_checks.json) are a finite
verification, not the proof of divergence.
