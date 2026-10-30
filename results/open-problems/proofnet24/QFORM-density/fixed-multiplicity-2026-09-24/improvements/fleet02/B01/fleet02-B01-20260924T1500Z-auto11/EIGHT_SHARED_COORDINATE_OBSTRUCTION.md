# Eight-direction obstruction: overlap volume is not disjoint third crossing volume

Run: `fleet02-B01-20260924T1500Z-auto11`.  
Status: **proved counterexample to a tempting reduction; not a counterexample to the eight-eigenvalue density theorem.**

## Statement

There exists a real symmetric 8-by-8 matrix A with (s_8(A)=1) such that:

1. A has a nonzero overlap-one bordered third minor of the exact type counted by (W_{2,1}^{\times});
2. every literal disjoint physical crossing block (A_{I,J}), for (I\cap J=\varnothing), has rank at most two, hence (Z_3(A_{I,J})=0).

Therefore neither (s_8(A)\ge1) nor positive overlap-one third volume can be converted, without a new analytic argument, into the disjoint (Z_3) currency consumed by the marginal-free q=3 crossing theorem.

## Construction

Let
[
B=
\begin{pmatrix}
0&0&1&0&1\\
0&0&0&1&0\\
1&0&0&0&1\\
0&1&0&0&0\\
1&0&1&0&0
\end{pmatrix}.
]
The coordinates {1,3,5} form the adjacency matrix of a triangle, with eigenvalues 2,-1,-1. The coordinates {2,4} form (egin{psmallmatrix}0&1\\1&0end{psmallmatrix}), with eigenvalues 1,-1. Hence
[
\operatorname{spec}(B)=\{2,1,-1,-1,-1\},
]
so all five singular values are at least one.

Take S={1,2}, T={3,4}, h=5. Then
[
B_{S,T}=I_2,
qquad
B_{S\cup\{5\},,T\cup\{5\}}
=
\begin{pmatrix}
1&0&1\\
0&1&0\\
1&0&0
\end{pmatrix},
]
whose determinant is -1. Thus the overlap-one bordered volume is genuinely nonzero.

Now put
[
A=B\oplus I_3.
]
Then all eight singular values of A are at least one, so (s_8(A)=1).

For any disjoint coordinate partition I|J, the last three diagonal singleton coordinates contribute zero to the crossing block. Only the first five coordinates can contribute. Since those five active coordinates are split between I and J, one side contains at most two of them. Therefore
[
\operatorname{rank} A_{I,J}\le2
]
for every literal disjoint cut, and consequently (Z_3(A_{I,J})=0) for every such cut.

## Consequence

The overlap theorem in the nine-eigenvalue manuscript is genuinely new algebraic information, not disguised disjoint third crossing volume. A threshold-eight proof cannot simply cite the existing q=3 disjoint-bank receiver. The shared physical index h must be handled once, with its dependence preserved.

This example has easy physical pivots, so it is **not** a counterexample to an eight-eigenvalue density bound and it is **not** a model of the final no-pivot s8 chamber. Its role is narrower and exact: it falsifies the dependency shortcut “nonzero W overlap => usable disjoint (Z_3) packet.”

The remaining analytic target is a product-preserving estimate for
[
\det A_{S\cup\{h\},T\cup\{h\}}
=\det(A_{S,T})
\left(A_{hh}-A_{h,T}A_{S,T}^{-1}A_{S,h}\right)
]
that treats h as one original random coordinate and remains uniform under arbitrary same-bank curvature and affine terms.
