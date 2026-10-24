# r19 structural corollary — disjoint-minor Fourier branch versus a six-coordinate compound hub

This note records two deterministic consequences of the all-cross-minor theorem in `ADDENDUM_BALANCED_CROSSMINOR.md`. They sharpen the remaining structural debt without claiming the full conjecture solved.

## 1. Small disjointness produces a three-coordinate hitting hub

Let `w_(R,S)=det(B_[R,S])^2/W_3(B)` be the canonical probability law on nonzero physical `3x3` cross minors of an arbitrary cross block `B`, as in the addendum. Let

`delta_row=P(R cap R'=empty)`

for iid `(R,S),(R',S')~w`.

For a fixed row triple `H`, define

`r(H)=P(R cap H=empty)`.

Then, by Fubini,

`delta_row=E_(R',S') r(R')`.                                       (1.1)

Therefore some row triple `H` in the support satisfies

`r(H)<=delta_row`.                                                   (1.2)

Equivalently,

`sum_(R cap H=empty,S) det(B_[R,S])^2
 <=delta_row W_3(B).`                                               (1.3)

But the left side is exactly

`W_3(B_[I\H,J])`.                                                    (1.4)

Hence

`boxed{ W_3(B_[I\H,J]) <= delta_row W_3(B). }`                       (1.5)

Thus failure of the row-disjoint Fourier certificate is not an amorphous high-dimensional obstruction: deleting **three original row coordinates** destroys all but a `delta_row` fraction of the third compound Hilbert--Schmidt mass.

The transpose statement is identical. If

`delta_col=P(S cap S'=empty)`,

then there is a physical column triple `L` for which

`boxed{ W_3(B_[I,J\L]) <= delta_col W_3(B). }`                       (1.6)

If both disjointness parameters are small, choose `H,L` as above. By the union bound under `w`,

`P(R cap H != empty AND S cap L != empty)
 >=1-delta_row-delta_col`.                                          (1.7)

So at least that fraction of the **entire determinant-weighted three-volume** consists of minors touching both a fixed three-row hub and a fixed three-column hub. This gives a six-original-coordinate compound-incidence localization witness.

Combining with `QFORM-BALANCED-CROSSMINOR-ENTROPY-L1-v1` gives an exact dichotomy at any threshold `eta in (0,1)`:

* if `delta_row>=eta` or `delta_col>=eta`, the cross block has a continuous-density Fourier bound of order `eta^(-1/6) W_3(B)^(-1/6)`;
* if both are `<eta`, then at least `1-2eta` of its canonical three-minor mass touches a fixed row triple `H` **and** a fixed column triple `L`.

No individual minor size enters this dichotomy.

## 2. Global spectral three-volume: a random physical cut extracts the disjoint part

For the full real symmetric `A`, put

`T_3(A)=sum_(|R|=|S|=3) det(A_[R,S])^2=e_3(A^2).`                   (2.1)

If `A` has at least three singular values at least one (equivalently at least three eigenvalues of absolute value at least one), then

`T_3(A)>=s_1(A)^2 s_2(A)^2 s_3(A)^2>=1`.                            (2.2)

Split this total mass by the overlap size `h=|R cap S|`:

`T_3=T^(0)+T^(1)+T^(2)+T^(3)`.                                     (2.3)

Here `T^(0)` is the squared-minor mass on disjoint physical row/column triples.

Choose a random physical bipartition `[n]=I disjoint_union J`, each coordinate independently entering `I` or `J` with probability `1/2`, and let

`B=A[I,J]`.

For a fixed ordered pair of triples `(R,S)`, the event `R subset I, S subset J` has probability `2^(-6)` if `R cap S=empty`, and probability zero otherwise. Therefore the exact expectation identity is

`boxed{ E_(I,J) W_3(A[I,J]) = 2^(-6) T^(0). }`                      (2.4)

Consequently some physical cut satisfies

`W_3(A[I,J]) >= T^(0)/64`.                                         (2.5)

This is useful because the new Fourier theorem is expressed in `W_3(B)` and a determinant-weighted disjointness parameter, not in the smallest singular value of one selected local minor.

Thus the full structural problem can be organized without tiny-minor inversion:

1. If `T^(0)` has universal scale, extract a physical cut with aggregate `W_3` at universal scale using (2.5). Then either row/column disjointness is paid by the new L1 theorem, or (1.7) produces a fixed six-coordinate compound hub through which almost all cross three-volume passes.
2. If `T^(0)` is small, then by (2.2)--(2.3) a universal fraction of the spectral three-volume lies in the overlap-one, overlap-two, or principal-triple classes. Those are exactly the geometries addressed by the fleet's physical pivot/Schur, pair/hub, and principal-`3x3` mechanisms; the remaining work is to aggregate those overlap classes before inversion.

This does not yet prove that one of the paid overlap mechanisms receives a dimension-free fraction, so the full target stays OPEN. It does, however, reduce the all-disjoint-minor part of the spectral three-volume to a clean product-preserving Fourier-vs-finite-hub dichotomy.

## 3. Updated first unpaid implication

`QFORM-COMPOUND-HUB-OR-OVERLAP-COMPILER-v1`:

> Starting from `T_3(A)>=1`, use the decomposition (2.3). Pay the `T^(0)` branch by (2.4) plus the balanced-crossminor L1 theorem unless it yields the six-coordinate compound hub (1.7). On that hub branch, or when `T^(1)+T^(2)+T^(3)` dominates, route determinant mass to the already completed physical-pair, pivot/Schur, zero-diagonal/principal-triple, grouped-star, or ridge exits without selecting one tiny minor.

The full target-wide unweighted `L1` estimate remains OPEN; this note is a structural reduction, not a declaration of a complete proof.
