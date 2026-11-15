# T102 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
Session start: 15 November 2026, approximately 04:52 Asia/Tbilisi.

## 1. Orientation and literature check

Read REPORT.md, LOG.md, PROOF.md and both complete scripts in the original
and round-3 folders, without running their scripts (they write beside
themselves). Read the startup memory index and compute_state.json. The latter
reports warn / owner_away_open with saturated CPU. All calculations here will
be small, single-process, single-thread, under nice -n 15. No subagents, git,
or writes outside this folder. The current folder-only order overrides the
global requests to write mesh/checklist/brain state; those tools are not run.

The web search began about 04:52 and ended about 04:54, within five minutes.
Queries: `"2604.14122" resistance exponent percolation`;
`"incipient infinite cluster" "resistance exponent" 2026 spectral dimension`;
`"percolation" "spectral dimension" "2026" "resistance"`;
`"Alexander" "Orbach" "2026" "two-dimensional"`.
Opened https://arxiv.org/abs/2604.14122 and
https://arxiv.org/html/2604.14122v1. The first lists only v1, 15 April 2026.
The latter's Corollaries 1.3–1.4 and “Explicit lengths” discussion still
leave beta_res unidentified. Exact authors: Irina Đanković, Maarten Markering,
Jason Miller, Yizheng Yuan. No newer solution located. This bounded search
cannot certify absence of a later solution.

## 2. Independent re-derivation of round 3

For any zero-sum boundary demand h of total positive mass t, couple its
positive and negative parts. Summing the corresponding minimum-energy
dipole flows and applying the energy-norm triangle inequality gives
sqrt(Q(h)) <= t sqrt(diam_R(S)). Minimizing
a(1-lambda)^2+b lambda^2 over lambda gives ab/(a+b). Summing two corrections
in a layer costs at most twice their separate energies. These are precisely
the round-3 two-layer and many-layer bounds. The signs agree: the local
wired flows have total interface divergence -delta, so repairs need +delta.

Independently, in its sharpness example contract the four unit edges. The
quotient is three parallel resistors L,K,K, whereas an original path has
length L+3. With K=L^2 this sandwiches R_full/L between quantities tending
to 1. The scalar wired sum is 2K/(K+1)+1/2=O(1). The two mismatch terms,
computed from the tree paths, have sum asymptotic to L/2. Hence the claimed
sharpness ratio tends to 2. The corrected round-3 result holds.

A fresh exact verification in this folder will use prescribed-divergence
Kirchhoff equations rather than round 3's unit-voltage solver.

## 3. Chosen extension (before calculation)

Resolve the circuit-boundary case named by round 3. Assign each complete
open interface circuit to the inner adjacent layer. This should guarantee
a finite repair regardless of other shell components. Repair each mismatch
on its own circuit; these supports are edge-disjoint, so the earlier factor
2 should disappear. Derive the exact circuit repair energy from cumulative
boundary current and test the resulting bound on the SAME finite networks
as their scalar wired sums. Also test whether this stronger geometric
assumption alone can force a bounded gluing ratio.

Why: this is a concrete missing geometric case in the previous report and
replaces worst-pair diameters by the energy of the actual mismatch. It does
not supply a percolation tail estimate. The circuit hypothesis, edge
ownership, component constraints, and any deterministic obstruction must
be made explicit. No claim of a new general network principle is intended.

## 4. Circuit bound and first exact run

Wrote PROOF.md and check_circuits.py. The proof gives

    R_full <= A + sum_i Q_{C_i}(delta_i),
    Q_C(h) = sum_j rho_j (H_j-Hbar)^2 <= (W/4) TV(h)^2,

where H_j is the cumulative signed boundary demand along the circuit,
W=sum rho_j, and Hbar=sum rho_j H_j/W. Circuit edges have zero current in
every local wired optimum. Adding one repair per circuit has no energy
cross terms, either with the optima or with other repairs. In fact circuit
edges may be divided between the adjacent layers: a whole circuit in one
layer is sufficient but unnecessary. This handles cases where both old
ordinary layer diameters are infinite.

For k nested circuits of lengths 2L_j connected in series by unit bridges,
the separately wired sum is A=k+1 and the full resistance is
k+1+(1/2)sum L_j. The circuit bound is exact. This is a planar unit-resistor
family of maximum degree 3. Thus nested circuit connectivity alone does
not imply a universal bounded gluing ratio. This is an abstract planar
network family, with no IIC probability claim or claim of a prescribed
triangular-lattice embedding.

Command (04:59–05:00):

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B check_circuits.py
```

Exit 0. All exact checks passed. Output saved to circuit_results.json:

- Independently rechecked the previous 255 interface configurations
  (210 positive corrections), 729 weighted star pairs, and all 11
  sharpness-family cases, through L=1024.
- 1,222 weighted-circuit/demand tests: cumulative formula equals exact
  prescribed-divergence Kirchhoff solution and pairwise-variance formula;
  rotating and reversing circuit indexing preserve the value.
- All 3,600 square-interface networks: all 15 nonempty source neighbor
  sets, all 15 nonempty sink neighbor sets, and all 16 circuit-edge
  ownership assignments. 656 attain the circuit upper bound, including
  240 zero corrections; 328 have both old diameters infinite. All bounds
  and explicit repaired flows pass on the same networks as the wired sums.
- The square with opposite single-vertex attachments and alternating
  circuit-edge ownership has A=2, R=3, D=Q_C=1 and both old diameters
  infinite, as claimed.
- 336 networks with 1–3 nested circuits, two choices of unit circuit
  length, bridge resistances 1 or 3, and two edge-ownership rules. All
  attain the circuit bound. An additional component disjoint from both
  terminal sets is retained and carries zero current.
- For two circuits of length 2L and three unit bridges, L=2,3,4,8,16
  give R=L+3, A=3, and D=Q_total=L exactly.
- At even lengths N=4,6,8,12,16,20, the alternating demand of TV 1
  gives Q=1/N, while an antipodal unit dipole gives Q=N/4.

The script uses exact rational symmetric LDL^T solves, independently of
round 3's unit-voltage solve and the original report's Gauss–Jordan solve.
It explicitly checks each solved linear system, vertex conservation,
orthogonality, actual circuit-flow feasibility, and the energy identity.
Elapsed 3.0945 seconds; peak RSS 17,416,192 bytes; one process, standard
library only, CPU limit 90 seconds and wall alarm 120 seconds. The requested
nice command warned that setpriority was denied; inherited nice=20 was
verified. No calculation approached the resource limits.

## 5. Attempts to break the result and independent counts

Checked the delicate cases explicitly:

1. A circuit edge assigned to either side still has zero local wired
   current. Splitting a circuit repair across the two layers leaves total
   divergence zero on that interface in each restriction. Every correction
   is an actual flow; componentwise conservation is retained.
2. The circuit formula was derived by minimizing a constant circulation,
   by weighted pairwise variance, and for dipoles by the parallel law for
   the two arcs. Rotation and reversal pass exact tests, including odd and
   weighted cycles.
3. The nested-circuit examples were solved by series/parallel reduction
   and independently by the full Laplacian, with no block contraction.
   A=k+1 and D=sum L_j/2 agree exactly. Connectivity of nested circuits
   alone cannot imply a bounded gluing ratio.
4. Alternating demand on an even unit circuit has TV=1 and Q=1/N;
   an antipodal unit dipole has TV=1 and Q=N/4. Length times TV squared
   can therefore exceed the actual energy by a factor N^2/4.
5. The new bound need not be smaller than the previous harmonic diameter
   bound: interior shortcuts may give cheaper repairs. Its benefits are
   explicit evaluation, no factor 2, and no finite-side diameter hypothesis.

Added independent enumeration checks without solving a network:

- Weighted demand count is twice sum over n=3,...,7 of
  sum_{j=0}^{floor(n/2)} n!/[j!^2(n-2j)!] = 1,222.
- Square count is 15*15*16=3,600; equal profiles give 15*16=240 zero
  corrections.
- For each edge ownership, let s_1,...,s_q be its side's interface-only
  component sizes. The number of source-neighbor sets connecting the
  interface is product_j(2^{s_j}-1). Summing the products of the two sides'
  complementary disconnected-set counts gives 328. These components were
  computed by a separate union-find implementation.
- Equality occurs precisely when the circuit repair potential is constant
  on each hub's neighbor set. This voltage criterion gives 41 neighbor-set
  pairs and hence 41*16=656 networks, independently of full-network energy.
- Nested-network count is 2*sum_{k=1}^3 2^k*2^{k+1}=336.

Reran the Section 4 main command with these audit assertions. Exit 0;
all mathematical output unchanged. Final elapsed 2.9471 seconds, peak RSS
17,334,272 bytes, verified nice 20. Output is circuit_results.json.

Also ran a separate small command under the same thread/nice environment,
reading the old matching_results.json and the new circuit_results.json.
It compared all 11 sharpness-family L,R,D,D_over_sum values as exact
fractions, and the 255,210,729 case counts. Its executable body was:

```python
import json, os, resource
from pathlib import Path
from fractions import Fraction as F
resource.setrlimit(resource.RLIMIT_CPU,(10,10))
assert os.getpriority(os.PRIO_PROCESS,0) >= 15
old=json.loads(Path('~/codex_op_1114r3/briefs/T102/matching_results.json').read_text())
new=json.loads(Path('circuit_results.json').read_text())
for a,b in zip(old['sharpness_family'],new['earlier_sharpness']):
    assert a['L']==b['L']
    assert F(a['R'])==F(b['R'])
    assert F(a['D'])==F(b['D'])
    assert a['D_over_sum']==b['D_over_previous_sum']
assert old['earlier_family_cases']==new['earlier_interface_cases']==255
assert old['earlier_positive_corrections']==new['earlier_positive']==210
assert old['weighted_star_cases']==new['earlier_weighted_star_cases']==729
print('Round-3 saved data agree exactly: 255 cases, 210 positive, 729 stars, all 11 sharpness values.')
print('Final run:',new['elapsed_seconds'],'seconds;',new['peak_RSS_bytes_macOS'],'bytes RSS; nice',new['effective_nice'])
```

Exit 0. Output, besides the already-explained nice warning:

```text
Round-3 saved data agree exactly: 255 cases, 210 positive, 729 stars, all 11 sharpness values.
Final run: 2.9471 seconds; 17334272 bytes RSS; nice 20
```

## 6. Completion and limitations

No mathematical assertion failed in the exact runs. The inference that
nested circuit connectivity could alone control the gluing ratio fails;
that obstruction is part of the result. No percolation configurations
were sampled, no IIC tail estimate was proved, and no value or bound for
beta_res was obtained. The tests are deterministic finite-network families.
Published novelty of these elementary network consequences was not
established. REPORT.md records the result and the next probabilistic
quantity to study. All created artifacts are inside this folder.

One documentation patch initially failed because its context matched only
part of a line; it made no change and was reapplied with the full line.
