# T221 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
Session began 2026-11-15 01:40 Asia/Tbilisi (2026-11-14 21:40 UTC).

## 01:40–01:44 — orientation, earlier work, literature

Read the earlier REPORT.md, LOG.md, PROOF.md and audit_local_codes.py in
`~/codex_op_1114/briefs/T221`, without editing them.
Read the startup MEMORY.md index and compute_state.json. Compute status was
warn, owner_away_open; only small standard-library calculations are planned.
The instruction to write only in this folder takes precedence over global
instructions to mutate the external brain, mesh and checklist. Those tools
were not run. No git or subagents.

Literature check, under five minutes: web searches for `"Rokhlin"
"Bernoulli" "2026" entropy RBS`, `"Rokhlin" "Bernoulli shifts" conjecture
2025 2026 Seward`, `"RBS" "Rokhlin" "2026" solved`, and `"Rokhlin entropy"
"non-sofic" 2026`. Opened Brandon Seward, arXiv:1501.03367v4 (abstract
and PDF); Lewis Bowen and Michael Chapman, arXiv:2511.06586v1 (HTML,
especially Theorem 4.1 and Section 5); and Tim Austin, *Some Recent
Developments in Structural Ergodic Theory*, DOI 10.1137/25M1805564.
Austin's Question 3.1 still asks whether Rokhlin entropy can vanish for
every action of a group. No later resolution of arbitrary-group RBS was
found. This bounded search is not proof of absence. A search result about
mixing of all orders concerns a different Rokhlin problem and was excluded.

## 01:44 — independent re-derivation of the earlier result

The earlier main claim holds on inspection. Independently start with the
full repaired name Z=(Y,R): its decoder at g reads Y at gD and the rank
R_g, hence recovers x_g pointwise. Thus H(Z_e) bounds Rokhlin entropy
above and H(Z_e) <= H(Y_e)+b(error)+error log(k-1). In the converse,
first choose finitely many translates decoding x_e from a generator,
then truncate the generator, then approximate that finite partition by a
cylinder partition. This order makes both error probabilities tend to
zero while its entropy tends from above to at most the original generator
entropy. It proves the claimed infimum formula.

Independently check the presentation step using a quotient map P -> H:
imposed equalities give one implication; the quotient map gives the reverse
implication on the finite word list. Thus no extra collision appears in P.
The entropy of all repaired names on a finite H would be less than
|H|H(p), while determining |H| independent inputs, which is impossible.
Therefore H and P are infinite. Products are ts, not st.
The Seward theorem statements are being checked in the opened PDF before
the full-base reduction is accepted. A separate finite-cycle computation
will audit the earlier 768 exact gap signs without executing its script.

## Choice of one extension (recorded before its proof)

Derive an explicit lower bound on the fraction of defective vertices in
every finite permutation model of the multiplication pattern used by a
strict witness. This turns the earlier existential finite witness into a
quantitative obstruction that can be checked against finite models. Use
the sharper conditional cost H(Y_e)+H(x_e | Y_D), already present in
Bowen–Chapman, to improve the numerical obstruction. The intended new
piece is the explicit defect bound and its formulation in terms of a
finite presentation; no priority claim is made. It does not provide a
non-sofic candidate or prove RBS for a new group.

## 01:44 — proof saved

Wrote PROOF.md. The load-bearing estimate is the finite identity
H(U_V)=H(Z_V)+H(U_V|Z_V), followed by subadditivity and removing
conditioning. It gives the separate defect inequality
delta <= alpha(log|B|-a)+beta(H(p)-c), and hence the bound
eta >= delta/(log|B|+delta). Here a=H(Y_e), c=H(X_e|Y_D).
On bad vertices the conditional entropy is bounded by H(p), not log k;
this matters for nonuniform bases. The word version uses right actions
T_uv=T_v composed with T_u and correctly reads v_t w_s.

The opened Seward PDF, pages 5–6, confirms the exact statements of
Theorems 1.10 and 1.12 and the zero/infinity dichotomy used earlier.
This completes the check of the earlier full-base reduction; no error
was found. References are restricted to opened primary sources.

Next verification: a new standard-library script will (i) independently
enumerate full repaired names on a five-cycle and compare with the earlier
768 CSV rows, (ii) check the conditional identity on the regular action of
the noncommutative group S3, and (iii) test a deliberately impossible
collision pattern with a positive formal gap. The last is a unit test of
the quantitative bound, not an asserted group or an RBS counterexample.

## 03:32 — resumed artifact audit and successful computation

The saved draft, script and JSON were already present on resuming. Read
them, then reopened the cited Seward PDF and Bowen–Chapman HTML and
Austin's survey. The short repeated search found no resolution. Seward's
Theorems 1.10 and 1.12 agree with the earlier report, including the
infinite-base zero/infinity dichotomy. No SOLVED_ELSEWHERE.md is warranted.
All new mutations remain inside this folder; no brain, mesh, checklist,
git or external application was changed.

Re-ran the new script, without executing or editing the earlier script:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 audit_defects.py
```

Exit status 0. Output is saved in audit_defects.json. Relevant values:

```text
earlier CSV rows independently matched: 768
five-cycle full-name reconstruction checks: 24576
each of p=1/2,1/3,2/3: 256 pairs, 0 negative, 36 zero, 220 positive
S3 encoder/base cases: 512
S3 minimum information slack: 0.0
two conditional-entropy calculations, maximum discrepancy: 2.220446049250313e-16
formal-pattern delta: 0.130812035941137
formal-pattern defect threshold: 0.15876032857139014
3 vertices: 216 permutation assignments, minimum word-bad fraction 2/3, minimum Q 1
4 vertices: 13824 permutation assignments, minimum word-bad fraction 1/2, minimum Q 1
maximum information excess in either formal-pattern test: 0.0
effective nice priority: 20
peak RSS: 16859136 bytes
elapsed seconds: 0.6019315409939736
```

The wrapper prints `nice: setpriority: Operation not permitted`: the
inherited priority is already 20, which the script reads and asserts to
be at least 15. No priority increase or bypass was attempted. The script
uses only the standard library, one process, no workers, a 120-second
alarm, bounded finite loops and an RSS assertion below 1 GiB.

## 03:33 — attempt to break the result

Independently checked the constant by collecting coefficients in (4):
`(log|B|-a)+(H(p)-c)=log|B|+delta`. This yields (5) without dividing by
H(p), so degenerate bases cause no hidden division. For |B|=1, c=H(p)
and delta=0, hence this case cannot be a strict witness. Zero probabilities
do not affect the finite entropy argument. Arbitrary repeated decoder
coordinates still make N_v a function of Z_V, as required in (3).

Checked the constant a second way using the repaired full name: for
uniform bases the separate rank-correction derivation (12) gives exactly
the same Delta/(log|B|+Delta) bound. For nonuniform bases it is weaker;
the direct conditional derivation correctly uses H(p), not log k, at
bad vertices. This is a distinction in the theorem, not rounding.

Checked both multiplication conventions: T_uv=T_v composed with T_u,
so nested inputs read v_t w_s, and equality T_u(z)=T_v(z) is equivalent
to T_(uv^-1)(z)=z at the same vertex. The S3 check includes noncommuting
generators, unlike the earlier Z test.

The formal positive-gap pattern ca=cb=e with distinct a,b is impossible
in a group by cancellation. It is used only to exercise a positive
threshold against all finite permutation assignments of sizes 3 and 4.
It supplies no group example. Its constants were also simplified
independently: delta=(3/4)log 3-log 2 and threshold=1-4log 2/(3log 3).
The observed minima are stronger than the entropy bound, so no sharpness
claim is supported. No mathematical assertion failed in these checks.

Remaining limits: no candidate beyond known sofic cases was certified;
no genuine strict entropy witness was found; priority of the explicit
constant has not been established. The conditional-entropy criterion
itself is prior work. The extension is a proved necessary constraint on
any hypothetical witness, and does not give a converse to non-soficity.

## Final artifacts

Wrote REPORT.md with the required PARTIAL first line, the explicit bound,
independent earlier-result check, validation command and output, opened
references, limitations, and a concrete next refinement. Narrowed the
Bowen–Chapman attribution in PROOF.md to uniform bases, matching the
statement actually opened. The finite-model proof for arbitrary finite
p is self-contained. Read back the final artifact headers and checked
that the reported numerical values agree with audit_defects.json.
No additional computation was needed after the successful audit.
