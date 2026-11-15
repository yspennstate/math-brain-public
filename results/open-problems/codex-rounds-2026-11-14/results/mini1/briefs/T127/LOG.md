# T127 work log

Task received: 14 November 2026, approximately 21:17 Asia/Tbilisi.
Request: “push this problem forward by one checkable piece.”

## 1. Initial checks

The folder initially contained only PROMPT.md. No git commands were used.
All writes will stay in this folder. The task-specific instruction prohibiting
writes elsewhere takes precedence over global mesh/checklist/memory writes;
those commands were not run because they write outside this folder.

Read the startup memory index and the mesh protocol. Shell commands use
`OMP_NUM_THREADS=1 nice -n 15`. The sandbox prints
`nice: setpriority: Operation not permitted`; even `ps` is denied. No heavy
computation has been attempted. Subsequent computation will be small and use
one Python thread, standard library only, with an explicit time/memory guard.

Initial web searches:
- `frog model 3 ary 4 ary tree recurrence transience one frog Mathews 2025 2026`
- `frog model trees d=3 d=4 open problem recurrence 2024 2025`

Opened https://arxiv.org/abs/1404.6238 and its PDF: Christopher Hoffman,
Tobias Johnson, Matthew Junge, *Recurrence and transience for the frog model
on trees*. The abstract gives recurrence for d=2 and transience for d>=5.
Opened https://arxiv.org/html/2309.14443v2: *Improved critical drift estimates
for the frog model on trees*, credited to Poly Mathews Jr (the paper lists
the individual contributors in its title footnote). Its introduction still
describes d=3 and d=4 by simulations.
Opened https://arxiv.org/abs/2510.18792: Samyah Ahmed, Matthew Junge,
*The frog model with death revisited*. Its stated result concerns death and
drift, not the immortal simple-random-walk model in T127.

## 2. A potentially complete resolution found (about 21:21)

Further web queries included `"frog" "ternary" "2026" recurrence` and
`"frog model" "3" "4" "2026" transience recurrence`. These surfaced a
secondary report linking https://github.com/mt0-svg/frog-model-tree . Opened
the repository itself. Its current README claims BOTH recurrence for d=3
and transience for d=4, with one sleeper per non-root site and simple random
walks, and gives DOI 10.5281/zenodo.23121586. It describes unconditional
Lean statements `recurrent_three` and `transient_four`.

This is a candidate for the step-1 stopping condition, not yet treated as
verified. Next check: open the deposited paper, check the theorem statements
and formal model definitions, and distinguish a published claim from a proof
independently rerun here. The full Lean runs described by the repository
exceed the author's 1 GB and 20 minute limits, so they cannot be rerun here.

The compute governor read at 21:18 showed `status=warn`,
`mode=owner_away_open`, CPU saturation and 74% free memory. No simulation or
heavy search was launched.

## 3. Literature limit and concrete choice (21:22)

Opened the repository's releases page too:
https://github.com/mt0-svg/frog-model-tree/releases . Release v2.0.0,
dated 4 October 2026, states both cases and adds d=3 to the earlier d=4 result.
Attempts to retrieve the Zenodo record, paper, model definitions and statement
map all failed with tool `Cache miss` or `not accessible`. Consequently the
whole problem is REPORTED solved, but the actual paper and proof have not
been inspected. No arXiv id was found for that claim. Do not mistake the
README for a checked proof. The literature search is now closed, well within
ten minutes; the following work is independent of that claim.

Chosen piece: a rigorous three-type branching upper comparison for Bernoulli(q)
sleepers, on the same d=3 and d=4 trees. Derive its mean matrix by two methods
and seek small exact rational supervectors establishing transience at q above
the elementary single-particle branching bound (d-1)^2/(4d). This is a special
case of a different initial distribution, not a solution at q=1. It is a small,
reproducible application/refinement of the local comparisons in HJJ; no novelty
claim is made. The output will be a complete proof and exact certificate script.

Exploratory command: `OMP_NUM_THREADS=1 nice -n 15 python3 - <<'PY'`
with a standard-library 3x3 power iteration, scanning q on the hundredth grid
and t in [1.5,3.5] on the 0.05 grid (100 iterations per matrix).
Output:
```
3 (0.41, 0.99905879031721, 2.05, [0.5074385592267392, 1.0, 0.482787285170241])
4 (0.66, 0.9981877902655587, 2.55, [0.5086582067614356, 1.0, 0.48317786762811915])
```
Elapsed shell time 1.61 seconds. These floating-point values select candidates;
they are not certificates. The final script will use fractions and independent
enumeration instead. The exploratory here-document itself was not saved; the
final script will contain the exact candidates and all load-bearing checks.

Boundary refinement: rather than invoke a homogeneous-tree reduction, give
each individual frog at the actual root weight c=v_B. On a two-frog return to
the root split the pair, requiring 2c<=v_D; on a single return require c<=v_B.
The root's expected outgoing weight is ((1-q)v_F+qv_D)/t. Both conditions can
be checked directly, avoiding a hidden assumption about reflection at the root.

## 4. Exact verification and guard failures

Created `certificate.py`. Its matrix is checked against a separate routine
that enumerates every ordered direction tuple and every sleeper-mark tuple
at the distinct forward targets. It also checks the actual height-one and
root rules and tests q=0 and q=1 as well as the certified endpoints.

First two runs stopped before computation: macOS/sandbox rejected attempts
to set RLIMIT_AS and RLIMIT_DATA to 512 MB with `ValueError: current limit
exceeds maximum limit`. A read of the existing limits returned
9223372036854775807 for both hard and soft limits. The script now reports
the unavailable OS guard, has a 30-second alarm, and checks measured peak RSS.
Its finite enumeration has at most 25 direction pairs and four sleeper-mark
assignments per pair; it allocates no large arrays. The first successful run
used 15,122,432 bytes peak RSS and completed in under one second.

The successful exact margins are positive for both chosen endpoints. At q=1
all three margins of each chosen certificate are negative. This is an explicit
failed extension to the original problem, not evidence of recurrence.

Wrote PROOF.md, including a deferred-decisions coupling, the derivation of all
matrix entries, the reflecting-root inequalities, and the finite-expectation
argument. Wrote SOLVED_ELSEWHERE.md to preserve the unverified full-resolution
lead without representing it as a paper read or a proof checked.

## 5. Saved reproducible run

Exact command:
```
OMP_NUM_THREADS=1 nice -n 15 python3 certificate.py > certificate_output.txt 2>&1
```
Exit status: 0. Output (also saved verbatim in `certificate_output.txt`):
```
nice: setpriority: Operation not permitted
OS data-limit guard unavailable: current limit exceeds maximum limit; peak RSS checked below.
d=3 q=41/100 t=41/20 v=('203/200', '2', '483/500')
  v-Mv = 1367/1640000, 1239/820000, 1777/1640000
  root margin=11229/41000; pair margin=17/250
  rho=1638761/1640000; E[visits including time 0]<=1640000/1239
  elementary threshold=1/3; improvement=23/300
  q=1 margins = -347323/1640000, -1220769/3280000, -230683/1640000
d=4 q=33/50 t=51/20 v=('1017/1000', '2', '483/500')
  v-Mv = 1481/850000, 3173/796875, 1383/850000
  root margin=3323/10625; pair margin=17/250
  rho=273239/273700; E[visits including time 0]<=273700/461
  elementary threshold=9/16; improvement=39/400
  q=1 margins = -262933/2550000, -49268/265625, -65461/850000
  peak RSS bytes=15351808
PASS: formulas equal exhaustive one-step enumeration at q=0,q0,1;
      exact positive margins, root boundary, and q=1 failures checked.
```

Full rational matrices and boundary values are in `certificate_data.json`.
Peak RSS is platform/run dependent; all mathematical output is exact and
deterministic. The requested nice invocation was used, but priority could not
be set by this sandbox. The tiny runs stayed far below 1 GB and 20 minutes;
there were no worker threads or subprocesses in the certificate script.

## 6. Attempts to break the result

1. Re-derived every mean-matrix row by exhaustive enumeration, separately
   from its closed-form derivation. Checked at q=0, q=endpoint, q=1 for each d.
2. Checked both walkers choosing the same child: one shared sleeper mark,
   not two. With a sleeper this yields D+F, not two D packets.
3. Checked both walkers choosing the parent: a single D packet, with no
   new sleeper. At height one it becomes two individual R packets.
4. Checked the B packet's remembered empty child cannot spawn a sleeper.
5. Checked the actual reflecting root using its d outgoing neighbors, without
   assigning it a fictitious parent. The height-one enumeration gives an
   expected weight no greater than the interior matrix bound in all rows.
6. Audited the coupling with several packets simultaneously hitting a virgin
   vertex: choose the first packet with a real arrival before sampling marks;
   its mark supplies the single actual sleeper. Other marks add only auxiliary
   frogs. Unvisited sleepers are deferred, so their distribution remains iid.
7. Independently recomputed rho from the MINIMUM normalized slack rather than
   the maximum outgoing ratio, using the saved JSON. Exact agreement:
   d=3: 1638761/1640000; d=4: 273239/273700. Checked each proposed expectation
   bound times (1-rho) is exactly 1. Approximate bounds: 1323.6481 and 593.7093.
8. Checked the elementary thresholds by the independent discriminant identity
   (d+1)^2 = 4d(1+q_threshold), giving 1/3 and 9/16. Subtracting gives 23/300
   and 39/400, respectively.
9. At q=1, the saved certificates fail in every component. No conclusion about
   the original one-per-site model follows. No universal impossibility result
   for the three-type method was proved.
10. The expectation bound includes time zero. An additional initially sleeping
    root frog costs a factor two, as explicitly covered in PROOF.md.

The literature timestamps above are approximate local task-stage labels.
The tool clock read 21:19:49 during retrieval attempts, 21:20:59 before the
concrete computation and 21:28:04 during the final arithmetic audit. The web
search phase took under ten minutes. No claim is made that these Bernoulli
bounds improve the best published bounds; the verified comparison is with
the elementary single-particle test only.
