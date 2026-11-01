# Eight-state ML10 checkpoint and global-route boundaries

2 October 2026. No external publication or Git mutation was performed here.

## Strongest completed claim

For every p>=0 on F2^3, uniform host measure, and W(x,y)=8p_(x+y),

    t(ML10,W)>=(sum p)^15.

The full final proof is `continuation_20261002_cube8_sidorenko_FINAL.md`.
The pre-audit proof is preserved separately as
`continuation_20261002_cube8_sidorenko_proof.md`.
The separate full PASS audit is `cube8_k_independent_audit.md`, with
manifest-hashed exact regenerators listed there. Historical novelty is
unverified. The unrestricted graphon problem remains unresolved here.

The proof uses standard nonnegative binary-character expansion to average
one host coordinate whenever its four pair preferences have even parity.
Exact AGL(3,2) order coverage proves that only one of thirty affine strict
order orbits has odd preference parity in every direction. Its density
gap P becomes coefficientwise positive after multiplication by L^2, where
L is the sum of the seven genuine ordering gaps. The constant-host case
L=0 is handled directly, so no division occurs at zero.

Complete independent checks agree on all:

- 262144 group-valued flows /3964 Fourier coefficients;
- 134217728 rooted assignments /89168 host-weight coefficients;
- 170406 raw exceptional-chamber coefficients, including367 negatives;
- 345312 positive degree17 multiplier coefficients;
- 40320 strict orders /1344 exceptional orders, exactly one affine orbit.

The qualitative Klein4 bound needed by the smoothing step follows by
repeated elementary averaging for EVERY bipartite source. It is a
rederivation using standard tools, not a new qualitative theorem claim.
The earlier quantitative Klein4 Schur/cycle results retain their scope.

## Exact failed quantitative extension

The four-state coefficients5 and14 do not extend to all eight-state
Boolean convolution hosts. Let p0=0 and p_g=1/7 otherwise. Then s=1,
all seven centered Fourier modes are -1/7, and

    F=688615849984/678223072849,
    F-[1+5 sum r^4+14 sum r^6]=-58807078/678223072849<0.

The host still satisfies Sidorenko (F>1). This is solely an obstruction
to transferring the stronger cycle-surplus statement. The exact record
is `continuation_20261002_cube8_coefficient14_obstruction.json`.

## Global binary-coordinate route: actual calculations and gap

A possible broader route would prove averaging inequality for ML10 even
when the conditional first-coordinate contrast b(u) has mixed signs.
For any quotient group the first-coordinate expansion has coefficients
C_k indexed by Eulerian edge subsets of ML10, with k in{0,4,6,8,10}.
For the four-state quotient, the complete3964-term flow polynomial gives
these coefficient polynomials exactly. Files:

- `continuation_20261002_cube8_colored_cycle_search.py/.json`:
  100 numerical starts per C4,C6,C8,C10, with a>0 and arbitrary
  odd-orientation b (not constrained by |b|<=a). No substantial negative
  value found; this is numerical evidence only and proves nothing.
- `continuation_20261002_cube8_colored_partial_walsh.py/.json`:
  exact transform of all C_k to quotient host-a variables and
  Fourier-b variables. It retains all coefficients, including negatives.
- `continuation_20261002_cube8_C4_coefficient_sos_search.py/.json`:
  numerical sign search in the27 symmetry representatives of C4's
  host-a coefficient quartics. It finds an actually negative quartic
  at exponent(9,1,1,0), so coefficientwise quartic positivity fails.
- `continuation_20261002_cube8_C4_host_sos.py/.json`:
  exact conversion to host-b variables and the elementary paired-square
  sufficient SOS test.112 of364 host-a coefficient quartics fail that
  sufficient criterion. The polynomial is retained, not discarded.
- `continuation_20261002_cube8_C4_ordered_a_sos.py/.json`:
  ordering host a (valid S4 affine symmetry) still leaves42 of364
  coefficient quartics failing that same sufficient criterion.
- `continuation_20261002_cube8_C4_boundary_search.py/.json`:
  numerical sphere optimization of full C4 near a=(1,epsilon,epsilon,0),
  epsilon from.5 to.0001. No substantial negative value found.

The exact key obstruction, in HOST b variables, is that the a0^9 a1 a2
coefficient of C4 is

    81920 b1^2 b2^2 +163840 b0 b1 b2 b3.

It equals -81920 at b=(-1,1,1,1). Thus no claim of coefficientwise
nonnegativity or coefficientwise quartic SOS is made. This does not
prove the FULL C4 polynomial negative: different a monomials may combine
to yield a nonnegative quartic. The global positivity step remains open.

The odd-orientation pair-difference coefficient test is likewise not a
proof: `continuation_20261002_cube8_pair_smoothing_coefficients.py/.json`
contains103212 positive even-orientation coefficients but29092 negative
odd-orientation coefficients. The even half is already covered by the
analytic standard averaging lemma. The script is preserved as scratch
provenance, not used to claim the odd half.

The raw exceptional-chamber cycle-surplus tests also failed to prove
positivity: `continuation_20261002_cube8_last_chamber_cycles.py/.json`
retains5851 negative coefficients after subtracting the fourth-cycle
coefficient5, and10342 after also subtracting sixth coefficient14. The
latter stronger assertion is actually false by the rational witness
above; mere negative coefficients alone were not treated as witnesses.

## Regenerators and arithmetic

Author's exact sources are:

- `continuation_20261002_cube8_vertex_polynomial.cpp/.tsv`;
- `continuation_20261002_cube8_flow_and_smoothing.py/.json`;
- `continuation_20261002_cube8_walsh_audit.cpp/.tsv/.json`;
- `continuation_20261002_cube8_coverage.py/.json`;
- `continuation_20261002_cube8_last_chamber.py/.json`;
- `continuation_20261002_cube8_last_chamber_polya.py/.json`;
- `continuation_20261002_cube8_polya_cpp_audit.cpp/.tsv/.json`.

K's separate full route begins with fundamental cycles on C10 plus its
five diameters, runs inverse rather than forward Walsh butterflies,
filters affine maps by ternary law rather than matrix columns, and
multiplies by L^2 directly using7 squares and21 cross terms. See its
stable audit and source manifest for complete reproducible commands.
No floating-point optimizer participates in the completed theorem.
