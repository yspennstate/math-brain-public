# A quantitative rank-one-host inequality for the ten-vertex Möbius ladder

2 October 2026. This is a restricted-host theorem, not a solution of the
Möbius-ladder case of Sidorenko's conjecture. Historical novelty of the
restricted theorem is unverified; low-rank/two-state cases may follow from
existing methods. The complete negative-perturbation argument below closes
the specific gap left in the earlier local checkpoint.

Let H have left and right vertices indexed by Z/5Z, with an edge i_a j_b
exactly when b−a is −1,0,1. It has ten vertices and fifteen edges. Let
W be a nonnegative bounded regular kernel on a probability space, normalized
so its degree is one. Assume its centered part has rank one:

    W(x,y)=1+lambda f(x)f(y),
    integral f=0, integral f^2=1.

For lambda=0 the kernel is constant and all statements below are immediate.
For nonzero lambda, boundedness and nonnegativity ensure the needed third
moment exists. Put m=integral f^3.

## Theorem

For every such W,

    t(H,W) >= 1+5 lambda^4+2 lambda^6.

Equivalently, since t(C4,W)=1+lambda^4 and t(C6,W)=1+lambda^6,

    t(H,W) >= 1+5[t(C4,W)−1]+2[t(C6,W)−1].

In particular this proves Sidorenko and a strict quantitative forcing bound
within this host class. It applies to arbitrary measurable f, rather than
assuming that the host has two equal-size parts or that f takes two values.

## 1. Exact finite expansion

Expand each of the fifteen edge factors as 1+lambda f_u f_v. A selected
edge subset with a vertex of degree one integrates to zero. Each remaining
nonisolated vertex has degree two or three, contributing respectively one
or m. Since H is cubic, these are all possibilities. The number of
degree-three vertices is even: the degree sum is even and the degree-two
contribution is even. Thus a subset with n2 degree-two vertices and n3=2k
degree-three vertices contributes

    lambda^(n2+3k) m^(2k).

The exact degree-pair counts are obtained independently by all 2^15 edge
subsets in `continuation_20261002_rankone_certificate.py/.json`:

    (n2,n3): count
    (0,0):1, (4,0):5, (6,0):15, (8,0):30, (10,0):13,
    (4,2):5, (5,2):10, (6,2):60, (7,2):70, (8,2):95,
    (4,4):15, (5,4):60, (6,4):145,
    (3,6):10, (4,6):75, (2,8):15, (0,10):1.

These counts match the earlier checkpoint but are independently regenerated
here; the positivity argument that follows is new to this continuation.
If lambda>=0, every term is nonnegative, so already
t(H,W)>=1+5lambda^4+15lambda^6.

## 2. Positivity controls the odd moment in the negative case

Suppose lambda=−z<0. Nonnegativity implies |f|<=z^(−1/2) almost everywhere.
Indeed, if a positive-measure set had f greater than z^(−1/2), its square
product set would have 1−z f(x)f(y)<0; the same reasoning applies to −f.
Since integral f^2=1, this also gives z<=1.

Write A=z^(−1/2)>=1. The pointwise nonnegative polynomial
(A−f)(f+1/A)^2 gives, after taking expectations and using the first two
moments,

    0<=A−1/A−m.

Applying the same argument to −f gives |m|<=A−1/A. Consequently, with

    r=z m^2,

we have the exact constraint

    0<=r<=(1−z)^2,  0<z<=1.

No atomless diagonal condition is being used: positivity on a product of
two positive-measure level sets proves the essential bound.

## 3. Control every negative term

Substitute lambda=−z and m^2=r/z in the exact expansion. It becomes

    t(H,W)−1=z^4 F(z,r),

where

    F=5+15z^2+30z^4+13z^6
      +r(−5z^2+10z^3−60z^4+70z^5−95z^6)
      +r^2(15z^4−60z^5+145z^6)
      +r^3(10z^5−75z^6)+15z^6r^4−z^6r^5.

There are exactly six negative monomials. Discarding the other positive
terms is legitimate, provided all six negative terms are explicitly
controlled. Using r<=(1−z)^2 and z(1−z)<=1/4,

    5z^2 r <=5z^2;
    60z^4 r <=(15/4)z^2;
    95z^6 r <=(1520/729)z^2 <(21/10)z^2;
    60z^5 r^2 <=(15/16)z^2;
    75z^6 r^3 <=(75/256)z^2;
    z^6 r^5 <=(1/256)z^2.

For the third line, max_{0<=z<=1} z^4(1−z)^2=16/729 at z=2/3.
For the fourth line, z^3(1−z)^4<=[z(1−z)]^3<=1/64.
For the last two lines use z^4(1−z)^6 and z^4(1−z)^10, both at most
[z(1−z)]^4<=1/256. The second line uses z^2(1−z)^2<=1/16.

The six rational bounds sum to

    5+15/4+21/10+15/16+75/256+1/256=3867/320<13.

Thus the original positive 15z^2 term alone absorbs all negative terms,
leaving at least (933/320)z^2. In fact the argument proves the stronger

    F(z,r)>=5+(933/320)z^2+30z^4+13z^6.

Multiplying by z^4 proves the stated theorem, with slack. This also checks
the extreme cases r=0, z=1 and the two-point extremizers of the moment
constraint. No unverified sign of a cubic-core term enters the proof.

## What remains open

For a general regular kernel W, its centered part can have several positive
and negative eigenfunctions, and the degree-three vertices contribute a
full mixed third-moment tensor rather than one scalar m. The constraint
above then has no directly established multivariate replacement controlling
all mixed terms. This theorem therefore does not imply the full Möbius
Sidorenko inequality, Rossman's pseudo-positive spectrum conjecture, or the
unrestricted fifteen-edge inequality.

Primary status and tools are credited in `checkpoint.md`. The exact ladder
transfer and Perron lower bound are Rossman's prior results. The 2025 EJC
primary article identifies this ten-vertex case as open; the inspected July
2026 tensor-transfer paper states equivalences and does not solve it.
