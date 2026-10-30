# Full-affine phase funding: independent review and actual-cost sharpening

Finite uniform Boolean signs, normalized Walsh spectrum, entropy bits.
Write a(h) for minimum influence over invertible linear input changes and
output-character multiplication (input shifts do not change any cost).
A055-RARE-CUBIC-PHASE-ORBIT-EXTREMAL-CORE-GUARD@1, statement SHA256
135a9c1248a6791dc3fa1b5447921597e2e45656c9e9e88957a24b9bd780876c,
is independently accepted HOLDS without repair at PROOF Sections1--2
and Section3's first paragraph (joint-orbit reduction). The large NAND
certificate and all-block embedding census are outside this acceptance.

## 1. Reconstructing the global basis comparison

For any sign h let w_h(v)=Pr[h(x)!=h(x+v)] and m_h(v)=min(w_h(v),1-w_h(v)).
The finite full-affine minimum is min_B sum_(v in B)m_h(v), over all
independent input direction bases. Any output-character assignment of
minorities on a chosen basis is simultaneously realizable by its dual.
Let Z_P be the subspace of constant-derivative directions of P. Translation
by v multiplies each Walsh coefficient by (-1)^(s dot v); it has a common
sign exactly when all support differences annihilate v. Thus codim Z_P
is the affine spectral dimension r of P. The centered cost m_P is constant
on each coset of Z_P, with zero cost exactly on Z_P.

If P=(-1)^p and deg_F2 p<=d, each nonconstant derivative polynomial has
degree<=d-1. The elementary Reed--Muller weight induction is: write a
nonconstant polynomial as x_j A+B. Wherever A=1 exactly one of the two
values is1; induction lower-bounds that fraction by2^(1-d). Apply the
same argument to the derivative's complement to bound BOTH signs. Thus
m_P(v)>=beta=2^(1-d) off Z_P, while characters have r0 and no quotient
cost. This is a centered derivative statement, not a physical-coordinate
count. It remains valid after every invertible affine input map.

Let delta=Pr[f=-1]. Union of the two negative endpoint events gives
w_f(v)<=2delta for EVERY direction. For delta<=1/4 this is already the
centered cost m_f(v). The XOR derivative identity implies
m_(fP)(v)>=m_P(v)-w_f(v), so
m_(fP)(v)-m_f(v)>=m_P(v)-2w_f(v)>=m_P(v)-4delta.       (1)
On Z_P these two centered costs are EXACTLY equal. If beta>=4delta,
all outside increments in(1) are nonnegative. Every basis has at least r
outside vectors. Applying this to an optimizing basis of fP and keeping
its full f-basis cost proves the source inequality
 a(fP)>=a(f)+r(beta-4delta).
Nonnegativity is precisely what licenses dropping extra quotient rows.

For the source entropy bound, shift P's support into a linear space W
of dimension r by multiplying P by one character. Convolution with its
coefficients acts orthogonally inside each W-coset, since multiplication
by a Boolean sign is a unitary Walsh operation. All coset squared norms
are preserved. The entropy of the coset label is unchanged and conditional
entropy on2^r points increases by at most r. Hence H(fP)-H(f)<=r, including
zero-mass cosets. Combining gives the source full-affine deficit gap.
Affine substitution preserves polynomial degree, so every element of the
joint degree<=d-phase/affine group is one such phase followed by an affine
input map and character. If I(f)=a(f), the source raw-root global deficit
optimality follows. No stationarity at descendants is licensed.

## 2. Sharpening: charge the phase's actual quotient-basis minimum

This narrow theorem is new author work, pending independent review.
Assume delta<=1/4 and m_P(v)>=4delta for all v outside Z_P, with the
condition vacuous if r0. Then

 a(fP)-a(f) >= a(P)-4delta*r,                            (2)
 H(fP)-H(f) <= r,                                       (3)
 [H(fP)-K a(fP)]-[H(f)-K a(f)]
             <=r-K[a(P)-4delta*r],  K>=0.               (4)

Proof: choose an optimizing full basis B for fP. Its images span the
r-dimensional quotient by Z_P, so choose a SUBSET C of EXACTLY r rows
whose quotient images are independent. Complete C with a basis of Z_P.
The result is a full basis, and its P-cost is sum_C m_P, because the
added rows cost0. Therefore sum_C m_P>=a(P). Sum(1) on C; all other
outside rows have nonnegative increments and rows in Z_P have zero
increments. The retained sum_B m_f is at least a(f). This proves(2).
The argument extracts independent quotient rows once; it never adds
multiple dependent parity swaps. This is stronger than the source charge
r*beta because a(P)>=r*beta. It includes characters, constants, ties,
rank0 and the equality beta=4delta. It does not assert a dimension-free
bound if the off-kernel minority condition is dropped.

For any allowed phase P the test K[a(P)-4delta*r]>=r suffices for full-
affine optimized deficit nonincrease; strict inequality implies strict
loss when r>0. This tests actual phase cost even when the crude degree
bound gives no strict margin. A class-wide raw-root normal form still
requires I(f)=a(f) and this test for EVERY allowed phase; one checked
phase is not a global normalization theorem.

An explicit strict certificate uses P=(-1)^(x1*x2*x3+x1*x4). Its affine
spectral rank is4, min positive centered derivative cost is1/4, and
its full affine minimum is5/4. For a point-negative four-bit f,
delta1/16, the old charge r(beta-4delta) is0 while(2) gives1/4.
At K20 equation(4) is at most -1. Primary uses the negative point0;
separate exhaustive-basis replay uses point1, so their observed actual
influence gains1 and1/2 concern DIFFERENT roots. Both exceed the same
certified1/4. This is a phase comparison, not a positive high-K witness.

## 3. Hardness boundary and first unsupported universal line

The source's rare arbitrary-core family has delta->0 and satisfies the
coarse cubic test at every fixed K>4, hence it also satisfies(4) for all
cubic phases. The same ORIGINAL paid pair and all complete terminals
stay in place. If the seed violates that fixed K, the optimized signed
pair reserve is strictly negative. These are not genuine least-dimensional
critical witnesses, despite their global cubic deficit/ratio normal form.

The new actual-cost charge strengthens a phase comparison and its exact
certification; it does not remove this counterguard or improve a universal
FEI constant. C019 still requires that EXACT nonnegative smaller-child
reserves plus original-pair signed alignment force enough UNUSED independent
quotient rank to pay one full original proper-pair bill, mixed rows and all
terminals included, from the SAME bank. This is the first unsupported
universal line. NEXT uses this exact excluded eligibility, rather than
another affine/phase endpoint that still admits arbitrary tensor cores.
