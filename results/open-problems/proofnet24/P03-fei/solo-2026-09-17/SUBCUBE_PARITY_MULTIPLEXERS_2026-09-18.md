# FEI with constant four for distinct-parity subcube multiplexers

Status: proved below and self-checked; publication novelty **UNVERIFIED**. This
is a full FEI theorem for a structured class containing ordinary addressing
and allowing data parities of arbitrary degree. It is not a proof of the full
Friedgut--Kalai conjecture.

All logarithms are base two.

## 1. Class and theorem

Split the variables into selector bits `x in {+1,-1}^m` and data bits
`y in {+1,-1}^k`. Partition the selector cube into nonempty subcubes

    {+1,-1}^m = disjoint union over j of C_j.           (1)

If `C_j` has codimension `r_j`, its density is

    delta_j=2^(-r_j).                                  (2)

Assign to the cells pairwise distinct data subsets `D_j subseteq [k]`. On
each cell choose a sign times a selector character

    sigma_j(x)=s_j chi_(T_j)(x),   s_j in {+1,-1}.      (3)

Only the restriction of this character to `C_j` matters. Define

    f(x,y)=sigma_j(x) chi_(D_j)(y)  when x in C_j.      (4)

Then `f` is Boolean and

    H(f)=2H(J)<=4 I_x(f)<=4 I(f),                       (5)

where `J(x)=j` is the cell label, `H(f)` is the entropy of the squared Fourier
law, and `I_x` is total influence in the selector coordinates.

Thus the full Fourier entropy--influence inequality holds with constant four
on this class, independently of the number of cells, the selector dimension,
the data dimension, and the degrees `|D_j|` of the selected parities.

The constant four is asymptotically sharp for this class. Take every selector
cell to be a point and assign it a distinct data singleton: this is the usual
addressing function on `m` address bits and `2^m` data bits. Then

    H(f)=2m,   I_x(f)=m/2,   I_y(f)=1,

so

    H(f)/I(f)=4m/(m+2) -> 4.                            (6)

The constant four here is a proved class bound. It must not be confused with
the false universal proposal `B<=4I`, refuted elsewhere in this folder.

## 2. Exact spectral law

Put

    v_j(x)=1_(C_j)(x) sigma_j(x).                       (7)

Since the data labels are distinct, (4) has the data-character expansion

    f(x,y)=sum_j v_j(x) chi_(D_j)(y),                   (8)

with no collision between two terms at the same data Fourier subset. Parseval
in the selector variables gives

    Pr[Y=D_j]=sum_S vhat_j(S)^2=E_x v_j(x)^2=delta_j.  (9)

An indicator of a codimension-`r_j` subcube has exactly `2^(r_j)` nonzero
Fourier coefficients, all of magnitude `delta_j`. Multiplication by the
character in (3) merely translates this Fourier support. Therefore,
conditional on `Y=D_j`, the selector spectral subset `X` is uniform on
`2^(r_j)` points, and

    H(X|Y=D_j)=r_j=log(1/delta_j).                     (10)

Also `Y` identifies `j`, by distinctness of the `D_j`, so

    H(Y)=H(J)=sum_j delta_j log(1/delta_j)
          =sum_j delta_j r_j.                         (11)

Combining (9)--(11) gives the exact identity

    H(f)=H(Y)+H(X|Y)=2H(J).                            (12)

This is the nonreuse mechanism: the same prefix-code quantity appears once
as the entropy of the selected parity and once as the within-cell selector
spectrum. There is no logarithmic marginal overcount.

## 3. Paying the partition entropy by selector influence

For selector direction `i`, write

    eta_i=Pr_x[J(x) != J(x flipped at i)].             (13)

For each cell, the cube edge-isoperimetric inequality gives

    sum_i Pr[1_(C_j)(x) != 1_(C_j)(x flipped at i)]
       >=2 delta_j log(1/delta_j).                     (14)

In fact equality holds for a subcube, but the inequality is enough. Every
edge on which the label changes is counted for exactly two cell indicators.
Summing (14) over `j` and dividing by two yields

    sum_i eta_i >= H(J).                               (15)

If a selector edge changes the label from `j` to `l`, then `D_j!=D_l`.
Distinct Boolean characters are orthogonal, even after either is multiplied
by a sign. Hence

    Pr_y[sigma_j(x)chi_(D_j)(y)
          !=sigma_l(x')chi_(D_l)(y)]=1/2.              (16)

Edges inside one cell can only add nonnegative disagreement. Consequently

    Inf_i(f)>=eta_i/2,
    I_x(f)>=H(J)/2.                                    (17)

Equations (12) and (17) prove (5).

## 4. Relation to the earlier selector lemma

`SELECTOR_CHARGING_2026-09-18.md` assumed that `f` was affine in every data
bit. Booleanity then forced the input to select either the constant or one
signed data bit. The present theorem allows the selected object to be any
parity `chi_(D_j)`, including degree growing with `k`, and proves the full
spectral entropy bound rather than only the data-coordinate erasure bound.

Ordinary addressing is the special case in which every selector cell is a
point and each point selects a distinct data singleton. More generally, (1)
can be a variable-depth prefix partition: large cells use short selector
descriptions and small cells use long descriptions. Identity (12) exactly
matches those variable code lengths.

## 5. Exact boundary of the proof

Three hypotheses do real work.

1. **Distinct data parities.** If two cells use the same `D_j`, their selector
   Fourier coefficients add before squaring, so `Y` no longer identifies the
   cell and (9)--(12) do not hold as written.
2. **Subcube cells.** For an arbitrary cell `A_j`, the normalized spectrum of
   `1_(A_j)sigma_j` need not have entropy `log(1/delta_j)`; entropic uncertainty
   gives the opposite inequality. Bounding that conditional entropy is a
   partial-Boolean FEI problem, which earlier notes prove is FEI-hard in
   general.
3. **A single character on each cell.** If a fiber `f(x,·)` is an arbitrary
   Boolean data function, its Fourier coefficients overlap those of other
   fibers. The clean label law is replaced by a mixture with interference.

Thus the theorem removes the earlier degree-one limitation only in the exact
nonoverlapping regime. It does not justify a general higher-degree label
partition and does not close the full conjecture.

## 6. A broader erasure lemma retained for future use

The subcube assumption is unnecessary if one asks only for data-coordinate
erasure. Suppose merely that

    f(x,y)=sigma(x) chi_(D(x))(y)                      (18)

for an arbitrary label map `D(x)` and sign `sigma(x)`. The coefficient
functions `v_A=sigma 1_{D=A}` still have disjoint physical supports and

    Pr[Y=A]=Pr[D=A].                                   (19)

Therefore

    B_y(f)=sum_l H(Y_l|X,Y_(-l))
       <=sum_l H(Y_l|Y_(-l))<=H(Y)=H(D).               (20)

The last inequality follows by ordering the coordinates and using
`H(Y_l|Y_(-l))<=H(Y_l|Y_1,...,Y_(l-1))`.

The same edge-isoperimetric partition argument gives

    H(D)<=sum_i eta_i<=2I_x(f),                        (21)

because distinct parity labels differ on half of the data cube. Hence

    B_y(f)<=2I_x(f)                                    (22)

for arbitrary parity multiplexers. This strictly extends the earlier
degree-one data lemma. It still leaves selector erasure uncontrolled; the
subcube-character hypotheses are what turn it into the full entropy theorem
(5).

`check_subcube_parity_multiplexers.py` verifies the exact spectral law,
entropy identity, erasure bound and influence inequality on several unequal
subcube partitions using exact rational Walsh coefficients and outward
rational logarithm intervals. Universal assertions are proved above, not by
finite computation. The check is not an independent audit.
