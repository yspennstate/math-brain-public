SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet04, slot B11, 2026-09-23T11:16:08Z.
attacking: indefinite exact-rank-three exterior-area aggregation through disjoint physical triples.

# B11 — disjoint-volume compiler for the two-sheet chamber

## Status

A new exact determinant identity and density compiler closes every exact-rank-three indefinite form that has either one quantitatively large physical row-pair area or two disjoint physical triples with quantitative spectral volume. Arbitrary same-side quadratic blocks, outside coordinates, outside couplings, and conditioning-generated affine terms are retained. The unrestricted theorem remains open; continuity is separate.

## 1. Completed fleet01/B11 theorem applied

Let
[
A=RMR^T,qquad R^TR=I_3,
]
where (M) has signature ((2,1)) or ((1,2)), and let
[
s=min_k|lambda_k(M)|>0.
]
For physical rows (r_i,r_j), put
[
g_{ij}=det!egin{pmatrix}
langle r_i,r_iangle&langle r_i,r_jangle\
langle r_j,r_iangle&langle r_j,r_jangle
end{pmatrix}
=|r_iwedge r_j|_2^2.
]

Fleet01/B11, run `20260923T091549Z-fleet01-B11-QFORM-auto11`, commit `a9b0a2b16818dec0774806220bb7dba73670ba99`, proves the exact pair-extension identity
[
|det A[{i,j},{i,j}]|,|lambda_{m Schur}|
=|det M|,g_{ij},
]
and the full-line compiler
[
oxed{;
|p_{X^TAX}|_infty
le {128sqrt2over ssqrt{g_{ij}}}.
;}
	ag{1.1}
]
This is used at an actual inequality below. It already absorbs the convex/two-sheet logarithmic singularity; the ruled half-line theorem is not being promoted beyond its scope.

In particular, if
[
g_*:=max_{i<j}g_{ij}gegamma,
]
then
[
oxed{;
|p_{X^TAX}|_infty
le {128sqrt2over ssqrtgamma}
< {181.020over ssqrtgamma}.
;}
	ag{1.2}
]

## 2. New exact cross/principal determinant identity

Let (S,T) be disjoint triples of original coordinates. Write (R_S,R_T) for the corresponding (3	imes3) row matrices and define
[
Delta_S=|det A[S,S]|,qquad
Delta_T=|det A[T,T]|.
]

### Theorem 2.1

For every such disjoint pair,
[
oxed{;
|det A[S,T]|^2=Delta_SDelta_T.
;}
	ag{2.1}
]

### Proof

Since (A[S,T]=R_SMR_T^T),
[
det A[S,T]=det(R_S)det(M)det(R_T).
]
Also
[
det A[S,S]=det(M)det(R_S)^2,
qquad
det A[T,T]=det(M)det(R_T)^2.
]
Taking absolute values proves (2.1). No random-coordinate rotation occurs. (square)

This identity is sign compatible: both principal determinants have the sign of (det M), while the cross determinant may have either orientation. Only its absolute value enters the density estimate.

## 3. Dense-self-coupling disjoint-volume compiler

Fleet04/B09 proved at commit `c0d3f34e557a374f41b2639994c43af4f950b682` that an invertible physical (3	imes3) cross block (C=A[S,T]) between disjoint original-coordinate triples gives
[
|p_{X^TAX}|_inftyle3|det C|^{-1/3},
	ag{3.1}
]
with arbitrary dense same-side blocks and arbitrary outside completion.

Combining (2.1) and (3.1) yields the new branch
[
oxed{;
|p_{X^TAX}|_infty
le3(Delta_SDelta_T)^{-1/6}.
;}
	ag{3.2}
]

Equivalently, let
[
v_S=det(R_SR_S^T)=det(R_S)^2,qquad
v_T=det(R_TR_T^T)=det(R_T)^2.
]
Since (|det M|ge s^3),
[
|det A[S,T]|
=|det M|sqrt{v_Sv_T}
ge s^3sqrt{v_Sv_T}.
]
Therefore
[
oxed{;
|p_{X^TAX}|_infty
le {3over s}(v_Sv_T)^{-1/6}.
;}
	ag{3.3}
]
If both (v_S,v_Tge
u), then
[
oxed{;
|p_{X^TAX}|_infty
le {3over s
u^{1/3}}.
;}
	ag{3.4}
]

The proof conditions only on coordinates outside (Scup T). Thus the two physical (3	imes3) self blocks may be arbitrarily dense and large, and all induced affine terms are retained.

## 4. Sign-spliced exact-rank-three consequence

Claude's ruled theorem gives, for signature ((2,1)),
[
p_Q(y)mathbf1_{{yge0}}le{pisqrt2over s},
	ag{4.1}
]
and after replacing (Q) by (-Q), the reflected half-line statement for signature ((1,2)). This is only the one-sheet contribution.

The opposite convex/two-sheet contribution is paid on either of the following independent full-line exits:

1. a row-pair area (g_{ij}gegamma), by (1.2);
2. two disjoint triple volumes (v_S,v_Tge
u), by (3.4).

Consequently, on the union of these chambers,
[
oxed{;
|p_Q|_infty
le
min!left{
{128sqrt2over ssqrt{g_*}},
,
{3over s}(v_Sv_T)^{-1/6}
ight},
;}
	ag{4.2}
]
where the second term is included when such disjoint triples exist. The half-line estimate (4.1) remains a sharper sign-specific supplement, not the justification for (4.2).

## 5. What remains

For an exact-rank-three Parseval frame,
[
sum_{i<j}g_{ij}=3,
qquad
sum_{|S|=3}v_S=1
]
by Cauchy--Binet. Thus exterior area and triple volume cannot disappear; they may only diffuse over many physical coordinates.

The remaining structural chamber is now precise:

- every individual pair area (g_{ij}) is small;
- no two disjoint physical triples simultaneously carry quantitative volume;
- the existing balanced-cut volume theorem fails its leverage gate.

This is an exterior-volume clustering problem. It must be converted into disjoint original-coordinate banks for a three-bank or pair-plus-square receiver. Selecting one “best” minor cannot close it: flat disjoint-bank examples make every fixed physical minor small while collective bank smoothing stays uniform.

The full conjecture remains open, as does the interface from exact rank three to arbitrary nonseparable additional spectrum. No small matrix tail is treated as a small random quadratic error.

## Pins

- fleet04/B11 assignment blob: `b28c36216bdc5e78b1ba93b36befb30136fe0b5f`.
- request blob: `165c570ecb4dcc6299c38fc3298771e4a8339dac`.
- memory protocol blob: `0d902d56688f4b5c575f5b921ddf9f6709e88312`.
- fleet01/B11 source commit: `a9b0a2b16818dec0774806220bb7dba73670ba99`.
- fleet04/B09 source commit: `c0d3f34e557a374f41b2639994c43af4f950b682`.
- execution label: `WITHOUT_VERIFIED_BRAIN`.
