# Independent equality witness for w348's statement L1

This derivation uses STATEMENT_FIRST.md, not w348's proof. It was saved
before opening any paired proof artifact. The independent localization
obstructions were already on disk before STATEMENT_FIRST.md was opened.

Let 1<=p<=q and H contain orthonormal vectors e_0,e_1. Use W=R.
Let N=p+q. For a bit string of length N, let a be the number of ones
among positions 1,...,p, and b the number of ones in the last q positions.
Define the coefficient tensor

    T_bitstring = (-1)^a / binom(q,p-a), if a+b=p;
                  0, otherwise.

It is nonzero and separately symmetric in the two required blocks.
Its associated bihomogeneous polynomial is

    (x_0 y_1 - x_1 y_0)^p y_0^(q-p).

Let P_q symmetrize the first q positions. If c is the number of ones
in those q positions, and r in the last p positions, then P_q T is zero
unless c+r=p. Otherwise, averaging all arrangements in the first block
gives

    (P_q T)_bitstring =
      [1/binom(q,c)] sum_a (-1)^a binom(p,a)
                         binom(q-p,c-a)/binom(q,p-a).

The sum ranges over admissible a; binomial coefficients outside their
ordinary ranges are zero. Since c<=p here, the summand identity is

    binom(p,a) binom(q-p,c-a)/binom(q,p-a)
      = binom(c,a) binom(q-p+a,c)/binom(q,p).

The alternating sum of binom(c,a) binom(q-p+a,c) is (-1)^c:
it is the c-th finite difference of the polynomial
z -> binom(q-p+z,c), whose leading coefficient is 1/c!.
Consequently

    (P_q T)_bitstring = (-1)^c /
                         [binom(q,p) binom(q,c)].

Let U be the tensor obtained by moving the original q-block to the
front and the p-block to the end. Its coefficients are
(-1)^r/binom(q,p-r)=(-1)^(p-c)/binom(q,c). Therefore

    P_q T = (-1)^p U/binom(q,p),
    ||P_q T|| = ||T||/binom(q,p).

All coefficient tensors use the ordinary ordered-index Hilbert norm.
The block permutation is an isometry. Tensoring with any fixed nonzero
element of W retains the equality. Thus, if w348 proves the proposed
upper bound, its constant binom(q,p) is optimal already for dim H=2.
The argument is an equality witness; it does not independently prove
the upper bound for every T.

# Missing second block symmetry

For p=1,q=2 take

    T=(e_0 tensor e_1-e_1 tensor e_0) tensor e_0.

The first p positions are symmetric (vacuously), ||T||^2=2, and P_q T=0.
The last q positions are not symmetric. Thus the second block symmetry
cannot simply be removed.

# A safe stability bound, conditional on L1

Let Q symmetrize the last q positions and delta=||T-QT||. If T is
symmetric in its first p positions, then U=QT has both required
symmetries. Indeed the two symmetrizers act on disjoint blocks and
commute. With C=binom(q,p), L1 and contraction of P_q give

    ||T|| <= ||U||+delta
           <= C||P_q U||+delta
           <= C||P_q T||+(C+1)delta.

This is a valid conditional bound; optimal stability constants are not
claimed. The bound includes the error caused by symmetrizing the q-block
before applying P_q. An unaccounted delta term is a proof gap.

Review state: independently derived by w349; w350 check pending. This
does not establish the universal analytic tilt-derivative estimate
needed for P0017.
