# Root audit: complete regular-three-state Sidorenko surplus

2 October 2026 UTC. **PASS.** I read the complete final proof, valid
full-assignment generator, cycle-surplus generator, root-free transfer
regenerator, separate ant audit and its third independent implementation.
The full-assignment, transfer, cycle, ant and invalid-method reproducer
runs exited zero. The historical invalid root-fixed files remain
explicitly discarded and are not inputs to the theorem.

## Analytic coverage and normalization

For P=W/3 with row sum s, let a,b,c be its three off-diagonal entries.
The identity P=(s-a-b-c)I+aS01+bS02+cS12 is exact. If its identity
coefficient is negative, writing u=a+b+c-s converts it to
uK3+(a-u)S01+(b-u)S02+(c-u)S12. The three diagonal nonnegativity
constraints say exactly a,b,c>=u. Thus the two nonnegative generator
cones cover every symmetric nonnegative regular three-state host.
State relabeling permits all permutations of the three transpositions;
ordering their coefficients loses no host. The factor two in cone T is
only a scaling of coordinates.

Equal atom weights and fifteen edges on ten vertices give the density
factor 3^(15-10)=3^5. Every one of the 59,049 ten-vertex assignments is
included. Regularity alone would not justify fixing one state; the
invalid calculation is correctly rejected and reproduced separately.

The centered reflection sum has eigenvalues plus/minus sqrt(R), where
R=B^2+BC+C^2 in I and 4R in T. Adding the identity or K3 term gives
D plus/minus sqrt(R), or -D plus/minus 2sqrt(R). Their even fourth
and sixth moments have the displayed exact positive formulas. Direct
three-by-three matrix powers independently check these moments.

## Complete polynomial proof and sharpness boundaries

The integer polynomial

    18(F-s^15)-90s^11 E4-265s^9 E6

has 744 positive nonzero coefficients in I and 741 in T. All coefficients,
including absent terms, are checked by independent full polynomial maps.
The ant route integrates five right vertices after all 243 left labels;
the transfer route computes trace of a nine-state matrix to the fifth
power. Both reproduce the same complete 816 density coefficients in
each cone. This establishes the quantitative inequality on the entire
stated nonnegative domain, rather than on a parameter grid.

The minimum coefficient ratio is exactly 265/18 in both cones. It is
optimal for the specific coefficientwise subtraction, not proved to be
the best host-domain sixth coefficient. The fourth coefficient 5 is
sharp from the five literal four-cycles and a nonzero centered regular
perturbation. At fourth order all selected degree-one subgraphs vanish.
The perturbation is a valid strictly positive kernel near the constant.

The equal-diagonal host Wii=49/50, Wij=101/100 has centered eigenvalues
-1/100 and violates sixth coefficient 15 by the exact negative gap
-45549178945150001/500000000000000000000000000000. It satisfies the
proved bound and is not a counterexample to Sidorenko. Equality in the
proved inequality forces zero centered selfadjoint operator, hence a
constant kernel; the zero-edge-density case is separately immediate.

## Sources and honest scope

Rossman's general ladder transfer is prior art. General two-state Bethe
results and Csikvari--Lin's proper-coloring theorem include familiar
qualitative special hosts; none is presented here as a new resolution.
The exact quantitative three-state result's historical priority is
unverified. The source-host assumptions are equal atom measures,
regularity, symmetry and nonnegative entries; diagonal entries can
differ. No unequal atom, nonregular host, larger host or full graphon
extension has been established. The unrestricted ML10 problem remains
open in this campaign. Independent internal audits do not establish
external acceptance or novelty.
