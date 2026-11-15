# I0003 work log

2026-11-13, started about 19:57 Asia/Tbilisi (15:57 UTC).
Task: "Open problem I0003" — literature, then proof attempt and audited report.

Constraints: work only in this directory; no publication or pushes; no subagents;
computational commands use nice 10 and one numerical thread; no PDFs or page images
are written. Source PDFs, where needed, are parsed from memory into plain text.
The explicit directory restriction takes precedence over global requests to mutate
brain, mesh, or checklist databases outside this directory. Startup brain recall,
identity note, compute state and mesh protocol were read. Compute state warned of
CPU saturation; no parallel numerical jobs will be launched.

## Literature pass, in progress

- Retrieved source arXiv HTML and abstract, 2609.07621v1 (7 September 2026).
- Section 1.4 explicitly distinguishes the coupled Manhattan model from the
  partially oriented model with an independent vertical skeleton.
- It cites Bosi (2019), Theorem 9, for the alternating/random mixed Manhattan
  case: transient. This requested case is already in the literature.
- Section 1.1 cites Beaton–Holmes (2023) for the alternating/alternating reduction
  to simple random walk, attributed to Guillotin-Plantard.
- No theorem extending these assertions is claimed at this stage.

Priority check: the sandbox already inherits nice 20 (lower priority than nice 10).
An attempted extra +10 was refused because 20 is the ceiling; the fetcher now
checks priority and preserves inherited nice >=10. No heavy work ran.

## Literature checkpoint and proof direction

- Full plaintext source and checksums saved for the source paper, CP 2003/2014,
  Bosi 2019, Brémont 2017 published version and 2019/2020 preprints, GPLN's joint
  limit theorem, CGPS, Devulder–Pène, Pène 2009, Beaton–Holmes, Nguyen 2026,
  and GPLN–Pène–Watbled 2025. Retrieval failures are recorded in
  data/fetch_attempts.jsonl; mirrors are being used for two missing texts.
- Bosi Theorem 9 (printed/PDF pp. 72–73) has THREE parts, not just the iid
  mixed case: alternating versus any zero-mean periodic field is recurrent;
  sparse random replacements of a periodic field have threshold beta=1
  (beta<1 transient, beta>1 recurrent). Equality is not settled there.
- Brémont 2017 published Theorem 2.4, p.754, gives a full criterion for the
  STRATIFIED model, not the coupled Manhattan model. Proposition 7.1, p.790,
  proves the half-circle rotation example recurrent for a.e. angle.
- Planned deduction: Bosi 9(iii) plus a maximal variance bound produces, for
  every a>0, deterministic transient Manhattan fields with two-sided primitive
  envelopes O(n^a). Hence no positive power upper-bound guarantee can hold.
- Planned theorem: for normalized two-sided primitives S,T, let
  M(r)^2=max_{|k|<=r} S(k)^2+max_{|k|<=r} T(k)^2.
  If sum_m [1+M(2^m)^2]^{-1} diverges, the walk is recurrent.
  This includes bounded primitives and O(sqrt(log r)) growth. Method: write the
  antisymmetric rates as the face curl of h=(S-T)/2; bound its bilinear form by
  weighted Dirichlet energy; use the symmetric resolvent variational formula
  with dyadic radial cutoffs. Gaudillière–Landim Lemma 5.5 gives the bounded
  second-moment predecessor; the unbounded deterministic envelope criterion
  will be proved explicitly, without a claim that the general method is new.
- No full characterisation or deterministic exact-power phase diagram obtained.

## Additional deterministic class

The four-quadrant sign fields provide a sharper test of the magnitude premise.
For e_y=sign(y+1/2), f_x=-sign(x+1/2), use
R(x,y)=|x+1/2|+|y+1/2|. For u=phi(R), Au is supported on
four pairs of adjacent sites per radius, with opposite charges of size
[phi(r)-phi(r-1)]/2. Their H_{-1} norm is bounded by
2 sum_r [phi(r+1)-phi(r)]^2. Meanwhile
E(u)=4 sum_r r[phi(r+1)-phi(r)]^2.
A logarithmic radial cutoff proves recurrence despite |S_n|,|T_n|~n.
Changing f to +sign(x+1/2) gives a saddle field and transience; the absolute
primitive sequences are IDENTICAL. Thus magnitudes alone cannot classify fields,
even with exact linear powers. This is being checked before inclusion as a theorem.
The two Bosi–Hu–Peres revolving walks are different graphs (vertical edges remain
bidirectional off an axis), so their recurrence theorem does not prove this claim.

## Verified extension

The exact rational quadrant identities passed for 12 independently chosen finite
radial profiles, including the centre and the outer support boundary.

A useful general lemma follows from the same resolvent formula: adding a bounded
face stream function preserves type, with uniform multiplicative comparison of
diagonal resolvents. Consequently bounded changes to the two primitives preserve
type. This proves all of the following:
- finite line flips preserve type (even though infinitely many lattice edges change);
- fields eventually constant on all four tails are recurrent exactly when both
  sequences reverse sign between their tails and their positive-tail signs oppose;
- iid in one direction and ANY bounded-primitive orientation in the other are
  transient, simultaneously on the same full-probability set, by Bosi 9(i).
No claim of priority for the general sector comparison method is made.

Numerics: exact path transfer to time 128 for four periodic fields; brute-force
cross-check to time 12 and dense convolution to time 32; 100 integer face-identity
checks; finite-matrix resolvent identities; 784 periodic quotient indegree checks.
Monte Carlo: 2048 independent paths up to time 2048 in each of four fixed fields.
Peak numerical RSS <42 MB, one thread, inherited nice 20. All checks passed.
An initial BLAS matmul emitted floating status warnings while producing accurate
values; replaced that multiplication by explicit einsum and reran without warnings.

## Completed

REPORT.md now starts PARTIAL and contains complete proofs of bounded-primitive
type stability, the dyadic recurrence criterion, the classification of eventually
constant tails, the iid/bounded-primitive mixed result, and the sharp universal
polynomial upper-bound obstruction. It also gives the standard periodic
classification, exact theorem/page citations, numerical results and limitations.

Final audit passed: 22 source text records match their hashes; 28 cited result
patterns were located in the saved texts; zero PDF/image artifacts; all numerical
and exact rational checks passed. Numerical peak RSS 41,074,688 bytes, one thread,
nice 20. Data and reproducible scripts are confined to this directory. No pushes
or publication. Full characterization and exact sublinear-power classes remain
unsettled. Access limits: Pène 2020 publisher HTTP 403; Brémont 2016 author host
certificate failure. Later directly read primary results cover their relevant
recurrence questions, with those limits stated in the report.

Task done: "Open problem I0003" — asked about 19:57 Asia/Tbilisi, 13 November 2026.
