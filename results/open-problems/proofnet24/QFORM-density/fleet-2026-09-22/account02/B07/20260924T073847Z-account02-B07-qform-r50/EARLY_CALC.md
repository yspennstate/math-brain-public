SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B07, 2026-09-24T07:38:47Z.
attacking: account03/B07 r49 pair-block normal form — close the bounded-support block-diagonal-plus-rank24 spectral subproblem without selecting a minor, then sharpen the unpaid matched-bank receiver.

# First unpaid implication

`QFORM-R49-H62-R4-OPTAIL-RECEIVER-v1`.

After the completed r49 physical-E3 payment and on its moderate same-bank-star-energy branch, either a bounded original-coordinate principal core pays the full ambient essential density, or there is a physical set H contained in the matched bank S with |H|<=62 such that, for L=S\H,

    dist_op(A[L,L], {symmetric matrices of rank <=4}) < 0.001631502080283948.

The remaining receiver must consume this state while retaining the live global T|S separator, its true nonzero cross tail, arbitrary A[T,T], all H couplings, all outside couplings and all additional spectral directions. The separate r49 branch sum_good ||A[K,S\K]||_F^2>1 remains an explicit alternative. No single coordinate minor may be selected/inverted as a surrogate for the aggregate determinant packet.

# Core calculation

Suppose on a union C of literal physical matched pairs

    A[C,C] = B_pair + R + E,
    rank(R)<=r,   ||E||_op<=eta,

where B_pair is symmetric and block diagonal on the physical 2x2 pairs. For d>0 define

    nu_d(B_pair) = sum_K #{j in {1,2}: s_j(B_K)>=d}.

If nu_d(B_pair)>=r+3, select a minimal collection C0 of pair blocks whose cumulative count is at least r+3. Then C0 uses at most r+3 pairs, hence |C0|<=2(r+3). Let U be the spectral/singular subspace of B_pair[C0,C0] belonging to singular values >=d. Thus dim U>=r+3 and ||B_pair x||>=d||x|| for x in U. Since rank R[C0,C0]<=r,

    dim(U intersect ker R[C0,C0])
      >= dim U + dim ker R - |C0|
      >= (r+3)+(|C0|-r)-|C0| = 3.

For every x in that intersection, (B_pair+R)x=B_pair x, hence ||(B_pair+R)x||>=d||x||. The max-min formula for singular values gives

    s_3(B_pair[C0,C0]+R[C0,C0]) >= d,

and Weyl perturbation gives

    s_3(A[C0,C0]) >= d-eta.

Using the completed physical-fiber receiver, whenever d>eta,

    ||p_{X^TAX}||_infinity
      <= 2 sqrt(6 pi |C0|)/(d-eta)
      <= 2 sqrt(12 pi (r+3))/(d-eta).

This is aggregate singular-direction accounting through a low-rank cancellation; no individual minor is chosen.

# r49 specialization

r49 gives, on the unpaid E_star<=1 branch,

    A[S,S]=B_pair+R_24+E_S,
    rank R_24<=24,
    ||E_S||_F < D0 = 5.438340267613160e-4,

with R_24 equal to one global rank<=4 symmetric carrier plus a rank<=20 term supported on at most ten exceptional physical coordinates.

Take d=2D0=0.001087668053522632. If nu_d(B_pair)>=27, the preceding theorem supplies a principal core on at most 54 original coordinates with

    s_3 >= D0,
    ||p_Q||_infinity < 117330.53743.

Otherwise nu_d<=26. Delete every good pair whose B_pair block has operator norm >=d (at most 26 such pairs), and also delete the at most ten exceptional physical coordinates. The deleted set H has size at most 52+10=62. On L=S\H every surviving pair block has norm <d; the exceptional rank<=20 term vanishes; and ||E_S[L,L]||_op<D0. Therefore

    dist_op(A[L,L], rank<=4) < d+D0 = 3D0
      = 0.001631502080283948.

This is the sharpened unpaid state above.
