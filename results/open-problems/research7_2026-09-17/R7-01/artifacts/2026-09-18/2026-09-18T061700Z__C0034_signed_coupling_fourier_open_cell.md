# C0034 — canonical signed coupling, an exact six-point positive cell, and deformation openness

Target: Russell Lyons, *Determinantal Probability: Basic Properties and Conjectures* (ICM 2014), Question 2.8; same question as Question 10.1 in *Determinantal Probability Measures* (2003).

This artifact continues the admitted R7-01 C0034 track.  It does **not** claim the unrestricted question is solved.  The frozen source-aware metric remains `R_univ >= 3`.

## 1. B14: a basis- and gauge-invariant canonical signed coupling

Let `E` be finite.  Let `H=H1 \oplus H2 <= C^E` with ranks `r1,r2`.  Choose orthonormal row matrices `V1,V2` spanning `H1,H2`, and put `W=[V1;V2]`.  For `|A|=r1`, `|B|=r2`, `A cap B=empty`, and `T=A union B`, define

`p_A = det V1[:,A]`, `q_B = det V2[:,B]`, `r_T = det W[:,T]`.

Let `eps(A,B)` be the sign in the block Laplace expansion obtained by moving the increasing list of `A` before the increasing list of `B` inside the increasing list of `T`.  Define

`s_{A,B} := eps(A,B) p_A q_B conjugate(r_T)`.

### Theorem 1 (canonical complex signed coupling)

The array `s` has exactly the three desired marginals:

1. for every `A`, `sum_{B disjoint A} s_{A,B}=|p_A|^2`;
2. for every `B`, `sum_{A disjoint B} s_{A,B}=|q_B|^2`;
3. for every `T`, `sum_{A disjoint B, A union B=T}s_{A,B}=|r_T|^2`.

Consequently `x^0_{A,B}=Re s_{A,B}` is a real signed solution of the exact coupling equations.  Therefore the source problem in finite dimensions is equivalent to the cone-shift question

`find k in ker(M) such that x^0+k >= 0`,

where `M` is the fixed marginal-incidence operator.

### Proof

The third identity is immediate from block Laplace expansion:

`r_T = sum_{A union B=T} eps(A,B) p_A q_B`.

Multiplying by `conjugate(r_T)` gives the desired sum `|r_T|^2`.

For the first identity, view the unit decomposable exterior vectors corresponding to the two orthogonal row spaces as

`p in wedge^{r1} C^E`, `q in wedge^{r2} C^E`.

Orthogonality of `H1` and `H2` implies that the wedge map `L_q:u -> u wedge q` is an isometry on `wedge^{r1}H1`, and its adjoint contraction sends `p wedge q` back to `p`.  In coordinates this is exactly

`conjugate(p_A)=sum_{B disjoint A} eps(A,B) q_B conjugate(r_{A union B})`.

Multiplying by `p_A` gives the first marginal identity.  Interchanging the two blocks gives the second.  Taking real parts preserves the real nonnegative marginals, proving the signed-solution statement.  QED.

### Invariance

This signed point is intrinsic.  Replacing `V1,V2` by `U1 V1,U2 V2` multiplies `p_A,q_B,r_T` by `det U1`, `det U2`, and `(det U1)(det U2)` respectively, so the factors cancel in `s_{A,B}`.  Multiplying coordinate vectors by arbitrary unit complex phases also cancels because every coordinate in `T=A union B` occurs once upstairs and once in `r_T`.  Coordinate permutations simply relabel the array with the Laplace sign.  Thus this is a genuine symmetry quotient of the coupling problem, not a basis-dependent ansatz.

The remaining obstruction is therefore sharply localized: destructive Pluecker interference can make some `Re s_{A,B}` negative, and the question is whether the kernel of the marginal map always contains enough circulation to remove all such negative atoms.

## 2. B16: exact solution at the first unknown ambient size `|E|=6`

Take `E=Z/6Z`, let `omega=exp(2 pi i/6)`, and let `F` be the unitary Fourier matrix

`F_{r,j}=6^{-1/2} omega^{rj}`.

Let

- `H1` be the span of Fourier rows `0,1`;
- `H2` be the span of rows `2,3`;
- `H3` be the span of rows `4,5`.

Then `C^6=H1 \oplus H2 \oplus H3` and each `Hr` has rank two.  For any edge `e={i,j}`, every one of the three rank-two projection DPPs has the same edge probability

`w_e = (1/36)|omega^j-omega^i|^2`.

Thus, according to cyclic distance `d(e) in {1,2,3}`,

`w_1=1/36`, `w_2=1/12`, `w_3=1/9`.

We now construct an exact simultaneous partition coupling of the three DPPs.

There are fifteen perfect matchings of `K6`.  Under the dihedral symmetry of the hexagon they fall into five distance-multiset types, with orbit sizes

- `(1,1,1)`: size 2;
- `(1,2,2)`: size 6;
- `(1,1,3)`: size 3;
- `(2,2,3)`: size 3;
- `(3,3,3)`: size 1.

Assign total probability masses to these five orbits respectively by

`1/20, 1/20, 3/20, 7/10, 1/20`,

uniformly inside each orbit.  Hence every perfect matching has positive probability and the smallest matching atom is `1/120`.

The expected numbers of distance-1, distance-2 and distance-3 edges are respectively

`1/2, 3/2, 1`.

Since there are respectively `6,6,3` edges in those distance classes, the edge-inclusion probabilities of the random perfect matching are

`1/12, 1/4, 1/3 = 3 w_e`.

Now, independently conditional on the matching, assign its three edges uniformly to colors `1,2,3`.  Every ordered colored matching therefore has positive probability, with minimum atom `1/720`.  Each color has edge marginal exactly `w_e`, so

`X_r ~ P^{Hr}` for `r=1,2,3`.

Because the colored sets partition `E`,

`X1 union X2 = E \ X3`.

Projection-DPP complement duality gives

`E \ X3 ~ P^{H3^perp}=P^{H1 \oplus H2}`.

Therefore `(X1,X2)` is an exact source-valid disjoint coupling with the required union marginal for this nontrivial `2+2` six-point instance.

This is the first ambient size not already covered by Lyons's source observation `|E|<=5`.

## 3. B5: the exact Fourier point has a full open neighborhood of solutions

For the `2+2` problem on six points, let `M` be the fixed `45 x 90` incidence matrix mapping the ninety ordered colored perfect-match atoms to:

- the fifteen `H1` pair marginals;
- the fifteen `H2` pair marginals;
- the fifteen four-set union marginals.

The exact checker records `rank(M)=38`.

There are seven independent universal affine relations.  Two are equality of the three total masses.  The remaining six are the vertex-incidence identities

`sum_{A contains i} a_A + sum_{B contains i} b_B = sum_{T contains i} c_T`,

with one dependence after the two total-mass relations are imposed.  Hence these seven relations span the full left kernel of `M`.

Every orthogonal decomposition `H1 \oplus H2` satisfies the same relations because its one-point DPP marginals obey

`diag(P_H)=diag(P_{H1})+diag(P_{H2})`.

Let `b0` denote the forty-five marginal vector of the Fourier point and `x0` the explicit colored-matching coupling above.  We have

`M x0=b0`, `min_j x0_j=1/720`.

Choose any linear right inverse

`R: im(M) -> R^90`.

For a nearby orthogonal decomposition, write its marginal vector as `b=b0+delta`.  The affine relations imply `delta in im(M)`.  Therefore

`x=x0+R delta`

satisfies `Mx=b`.  Since `R` is bounded in finite dimension, for all sufficiently small `||delta||` we have

`||R delta||_infinity < 1/720`,

and hence `x>0` coordinatewise.  The DPP marginal map is continuous in the subspaces, so this proves:

### Theorem 2 (open six-point positive cell)

There is a genuine open neighborhood of the Fourier decomposition in the flag manifold of orthogonal `2+2+2` decompositions of `C^6` such that **every** decomposition in that neighborhood answers Lyons Question 2.8 positively for the pair `(H1,H2)`.

This neighborhood is not confined to the Fourier symmetry locus or a tensor-product family; it is open in the full local parameter space.

## 4. What this does and does not prove

These results do **not** prove the universal rank-four case.  They produce three new pieces of structure:

1. a canonical, gauge-invariant signed coupling for every finite decomposition, reducing feasibility to removal of negative atoms by marginal-kernel circulations;
2. an exact strictly positive coupling at the first source-unknown ambient size `|E|=6`;
3. a full-dimensional open cell of nontrivial six-point `2+2` decompositions for which the source coupling exists.

The frozen metric therefore remains `R_univ >= 3`.  The first universal unresolved case is still total rank four with a `2+2` split.

The next decisive object is the boundary of the colored coupling polytope: one must either prove that the orthogonal/Pluecker image never crosses a nontrivial facet, or produce an exact orthogonal decomposition whose marginal vector lies beyond such a facet.
