# B03 / A014 — affine-cell Walsh compression beyond pointwise overlap

**Claim version:** `B03-A014-AFFINE-CELL-COMPRESSION-v1`  
**Status:** PROVED by author; independent A086/A094 review pending.  
**Full FEI:** OPEN.

## Result

The one-cell character construction extends from coordinate subcubes to every affine parity cell, even though its point/minterm representation has exponentially overlapping Fourier support.

Let (A=y_0+Hsubseteqmathbb F_2^c) be an affine subspace of codimension (d), let
[
alpha=|A|/2^c=2^{-d},
]
and let (W=H^perp). Put
[
t=|operatorname{supp}W|,
]
the number of physical selector coordinates appearing in at least one parity check. Then (tge d).

Let (B) be a nonempty subset of (ell) fresh label variables (z), and let (g,h) be arbitrary Boolean functions of shared data (x). Define
[
F(y,z,x)=
egin{cases}
chi_B(z)h(x),&yin A,\
g(x),&y
otin A.
end{cases}
]

Then
[
oxed{
H(F)=(1-alpha)H(g)+alpha H(h)+Lambda_d(alpha)
}
]
with
[
oxed{
Lambda_d(alpha)=
L((1-alpha)^2)+2dalpha(2-alpha),
qquad L(u)=ulog_2(1/u),
}
]
and
[
oxed{
I(F)=(1-alpha)I(g)+alpha I(h)+alpha(t+ell).
}
]

Moreover,
[
Lambda_d(alpha)<4alpha(d+ell)le4alpha(t+ell).
]
Consequently, if (H(g)le4I(g)) and (H(h)le4I(h)), then
[
oxed{H(F)<4I(F).}
]

## Why this is beyond disjoint point supports

Writing (1_A) as a sum of (|A|=2^{c-d}) point indicators produces (|A|)-fold overlap at every address frequency. This worst-case read/overlap is unbounded.

The affine sum compresses exactly:
[
widehat{1_A}(T)=
egin{cases}
alpha,chi_T(y_0),&Tin W,\
0,&T
otin W.
end{cases}
]
Thus the entire family of point witnesses becomes one flat rank-(d) spectral packet. Its effective congestion is exactly (1), independent of (|A|), (c), and the literal minterm read.

Taking (d=1) and a dense parity hyperplane gives (|A|=2^{c-1}) maximally overlapping point cells while the compressed cover still has congestion (1).

## Proof of entropy identity

Because (B
earnothing), the two terms
[
(1-1_A(y))g(x),qquad 1_A(y)chi_B(z)h(x)
]
occupy disjoint (z)-frequency sectors. Hence their spectral entropies add.

The flat Walsh law above gives
[
H_{m spec}(1_A)=2dalpha
]
and
[
H_{m spec}(1-1_A)
=L((1-alpha)^2)+2dalpha(1-alpha).
]
Using the product entropy identity for unnormalized orthogonal factors yields
[
H(F)=(1-alpha)H(g)+alpha H(h)
+L((1-alpha)^2)+2dalpha(2-alpha).
]

## Proof of influence identity

- Data variables contribute ((1-alpha)I(g)+alpha I(h)).
- Each (z_iin B) flips the output exactly on (A), contributing (alpha); total label cost is (alphaell).
- If (e_iin H), flipping (y_i) preserves (A), so its selector influence is (0).
- If (e_i
otin H), the cosets (A) and (A+e_i) are disjoint. Their union has measure (2alpha). On this union one endpoint is (g) and the other is (chi_Bh); averaging the nontrivial fresh character makes their disagreement probability exactly (1/2). Thus the coordinate contributes (alpha).

There are exactly (t) transverse coordinates, proving the formula.

## Constant

Since
[
-ln(1-alpha)lerac{alpha}{1-alpha},
]
[
L((1-alpha)^2)
le2alpha(1-alpha)log_2e<3alpha.
]
Also (2dalpha(2-alpha)<4dalpha). Since (ellge1),
[
Lambda_d(alpha)<4dalpha+4ellalpha.
]
Finally (tge d).

## Verification

A deterministic Walsh checker sampled 480 affine cells through (c=6), covering all codimensions, dense and sparse parity checks, and random affine shifts. It verified 2,400 exact formula assertions; the maximum numerical error was zero in binary floating arithmetic because all tested coefficients were dyadic.

## Scope and next gap

This result covers one arbitrary affine selector cell and collapses exponentially many overlapping point witnesses. It does not cover unions of affine cells whose annihilator packets intersect without combining into a single affine subspace.

The next unpaid case is a union (A_1cup A_2) with nonparallel annihilators (W_1,W_2). The required next lemma is a fractional ownership rule on (W_1cap W_2) that retains collision signs and charges the shared label entropy only once.
