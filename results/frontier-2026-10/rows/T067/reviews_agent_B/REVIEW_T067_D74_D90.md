# Second audit: T067 degrees 74..90 and the all-regular composition

Reviewer: agent B (interactive Claude session). Not the author (worker R) and not worker S.
Requested by agent J (17 Oct 17:07Z, corrected 17:12Z). I did not open
(local dir) or worker S's audit files before writing this.

Texts read ((local dir), v1): BAND74-001, BAND74-UPPER-001 (parameters),
BAND77-001, BAND77-UPPER-001, BAND80/84/89-001 and -UPPER-001, EXPLICIT-CUTOFF80-001,
Q3-ALL-REGULAR-001, UNIVERSAL-FUSION-001, DEGREE-BAND-COMPARISON-001. Full hashes in
RECEIPT_T067_D74_D90.json.

## The envelopes: an exact replay with my own engine

uf_engine.py is written from UNIVERSAL-FUSION-001 alone and shares no code with worker R's
checks. It stores 817 orbit masses (N = 96, S = 2^32), applies the physical edge
p -> u + eta(p - u) with barycentric splitting over 3B, and fuses a left orbit
representative against every right grid point with joint mass m_k m_h (1/v) 3(k.h)/N^2
and barycentric weights over k.h. That gives integer numerators 6W/v over 2N^2 (worker R uses
108N^2; the rationals agree). Raw sums are exact by CRT over three 31-bit primes, and
every fusion checks that the CRT total equals S^2 2N^2. After the edge and after each
fusion every orbit mass is floored and the deficit goes to the pure orbit. Powers are built
by squaring, and a power is fused into the accumulator as soon as it is built if its bit is
set. The text leaves that order open; it is the order that reproduces the artifacts, and
any order gives a valid Blackwell upgrade (Section 4 of UNIVERSAL-FUSION).

Table checks inside the engine: each edge row sums to 3B; each ordered orbit-pair fusion row
sums to 2N^2 (817^2 rows).

RESULTS (compare.json). All five trajectories replay exactly, every depth and the final state:

| band | eta | depths | every depth: signal and all 11 node masses | final orbit masses | final x |
|---|---|---|---|---|---|
| 74..76 (d = 76) | 5/43 | 16 | equal | equal | 531277441825/4947802324992 < 1805/16641 |
| 77..79 (d = 79) | 31/272 | 16 | equal | equal | 177412024601/1649267441664 < 290405/2663424 |
| 80..83 (d = 83) | 35/313 | 66 | equal | equal | 2075411390651/19791209299968 < 179/1500 |
| 84..88 (d = 88) | 37/339 | 19 | equal | equal | 2346313218091/19791209299968 < 179/1500 |
| 89..90 (d = 90) | 529999/5000000 | 11 | equal | equal | 581906566811/4947802324992 < 179/1500 |

The artifacts compared are the files whose sha256 the texts state (48e47bfa.. d76 in BAND74-UPPER, 526edadb.. d79,
8651c6b8.. d83, f81f4104.. d88, 19a28665.. d90); every one matches. Each band uses its top degree, which is the one the
comparison lemma needs: a d-ary envelope at the band's largest degree bounds every smaller degree in the band.

## Arithmetic of the compositions (check_arith.py, check_arith.json)

All exact, all true:
- eta^2 >= 1/a at the bottom of each band: 74*25 = 1850 > 1849; 77 eta^2 - 1 = 13/73984;
  80 eta^2 - 1 = 31/97969; 84 and 89 likewise.
- Curve bands: 5(1-eta)^2/36 equals the stated radius exactly (1805/16641 at eta = 5/43,
  290405/2663424 at eta = 31/272). Since 1/sqrt(d) <= eta < 1, the actual LOCAL-CURVE radius
  is at least this, and d >= 4 holds.
- The three CUTOFF80 envelopes sit below 179/1500 with exactly the stated gaps.
- The band headers 7..79 (with 2..6 given separately) are disjoint and cover every integer,
  and 80..83, 84..88, 89..90 and d >= 91 cover the rest.
- The d >= 91 input T067-COMPENSATED-D91-001 v1 hashes to 3f41f298...ceb9bd, the hash in
  checks/d91_admission_bound.json (two-account PASS plus lead).

## The mathematics of the compositions

- DEGREE-BAND-COMPARISON: with c = lambda/eta, c K_eta + (1-c) J/q = K_lambda, so a hidden
  retention flag with an independent unconditional replacement gives the weak channel
  exactly. Discarding D-d branches and inducting on depth gives a root-independent kernel.
  Then Jensen bounds the weak signal by the strong one. Correct.
- Entry: the reverse martingale in the decreasing tail fields gives x_inf <= x_n. For fixed
  finite d the BP map is continuous (likelihood factors >= 1-lambda > 0). So the tail law is
  a calibrated, colour-invariant canonical fixed point, and the local lemma (LOCAL-CURVE for
  74..79, LOCAL-RADIUS80 for 80..90) is applied to it, never to the upgraded envelope.
  Correct, and the texts say so.
- Subcritical lambda by the same comparison at equal degree; lambda = 0 is independence.
- ALL-REGULAR is a pure composition. It promotes nothing: the statuses of its inputs carry
  through, and it is as strong as its weakest row.

VERDICT: PASS for BAND74-001, BAND77-001, BAND80-001, BAND84-001, BAND89-001, their five -UPPER-001 parameter texts,
EXPLICIT-CUTOFF80-001, and Q3-ALL-REGULAR-001 as a composition. The envelope numbers are reproduced exactly by an engine
written from the texts alone; the arithmetic is exact; the comparison and entry arguments are correct. ALL-REGULAR is as
strong as its inputs, and the d = 2..73 rows are outside this review. Scope: correctness of the v1 texts; novelty is not
judged.
