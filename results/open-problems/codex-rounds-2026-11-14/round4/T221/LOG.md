# T221 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
Session start: 2026-11-15 05:02 Asia/Tbilisi (01:02 UTC).

## 05:02–05:04 — orientation and bounded literature check

Read REPORT.md, LOG.md, PROOF.md and the Python scripts in both predecessor
folders, without editing or executing them. Read the startup MEMORY.md and
compute_state.json. Compute status: warn, owner_away_open, CPU saturated;
only small, single-threaded standard-library computations are planned.
The task-specific restriction to this folder overrides instructions to
write to the external brain, mesh or checklist. No git or subagents.

Commands: `pwd`; `ls -la`; `cat` on the predecessor artifacts and startup
files. The initial broad `rg --files` search returned too much unrelated
output; subsequent reads used exact paths.

Web searches: `"Rokhlin" "Bernoulli" entropy 2026 Seward RBS`;
`"Rokhlin" "collision" "entropy" Bernoulli`;
`"Rokhlin entropy" "2026" "Bernoulli" solved conjecture`.
Opened Brandon Seward, arXiv:1501.03367v4; Lewis Bowen and Michael Chapman,
arXiv:2511.06586v1 (HTML); and Tim Austin's ICM 2026 survey,
DOI 10.1137/25M1805564. Austin's Question 3.1 still asks about groups with
identically zero Rokhlin entropy. No resolution was found in the bounded
check, completed in under three minutes. This is not proof of absence of
later work. No SOLVED_ELSEWHERE.md is warranted.

## 05:04 — independent re-derivation of the earlier main claim

The round 3 bound holds. Independently, write the conditional chain rule
in an arbitrary order of the finite vertices:

    n H(p) = H(Z_V) + sum_i H(U_i | U_<i, Z_V)
           <= sum_i H(Z_i) + sum_i H(U_i | N_i).

Here Z is a deterministic function of U and N_i is a function of Z_V.
At good encoder and decoder vertices these two terms equal a and c.
Elsewhere they are at most log|B| and H(p), respectively. Subtracting
n(a+c) gives exactly

    delta <= alpha(log|B|-a) + beta(H(p)-c).

The sum of the two coefficients is log|B|+delta, proving the stated
union-defect bound. Right word evaluation gives T_(ts)=T_s composed with
T_t; hence the earlier word order is correct. The original finite-witness
repair and finitely presented lifting also survive inspection: the repair
recovers each input coordinate pointwise, and the quotient onto the
original subgroup prevents unwanted new equalities in the finite list.
This is a fresh chain-rule derivation, not a rerun of the old scripts.

## Choice of one extension, before its proof or computation

Implement and prove the proposed collision-cost refinement. For a fixed
finite word window, enumerate exactly those collision partitions that
can occur under finite permutations, compute H(Z_root)+H(U_root|N_root)
for each, and replace the universal bad-vertex cap by the maximum of
this finite table. A finite partial-permutation completion argument will
certify realizability, so spurious partitions need not weaken the bound.
Use a certified genuine group pattern for the numerical example; do not
reuse the inconsistent positive-gap audit pattern as a group candidate.
The aim is a sharper necessary condition on hypothetical witnesses, not
a new group satisfying RBS.

## 05:07 — proof, finite table, and first successful audit

Wrote PROOF.md and collision_costs.py. The proof characterizes precisely
the realizable partitions of a prefix-closed word set: for every
generator, the prescribed maps between classes must be well defined and
injective. Each partial bijection completes on the same finite set of
classes. Inverse letters are covered by reversing the prescribed edge.
This supplies the exact finite table rather than an arbitrary-partition
relaxation. The refined bound is

    eta >= delta / (M_bad - C0),

where C0 is the intended group cost and M_bad is the maximum cost of
an admissible type with an incorrect pattern. If delta>0, the one-point
model guarantees M_bad >= H(p)>C0. Thus there is no unverified positive
denominator assumption. The theorem also gives a finite list of
constraints for weights on individual word defects; those weights are
not numerically optimized in this session.

The genuine example uses the seven distinct words
1,a,b,aa,ab,ba,bb in F2, S=D=(1,a,b), and the three-input AND encoder.
Its cap was independently proved to be

    M = h(p) + p max(h(p),h(p^2)).

The two-point action a=b=transposition attains the first branch; the
three-point action a=cycle, b=inverse cycle attains the second. This
proves sharpness of the cap at a single root, not of the defect bound.

Re-read compute_state.json before running: warn, owner_away_open.
Command (exit 0):

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 collision_costs.py
```

Output saved in collision_summary.json; all table entries in
collision_table.json. Relevant first-run results:

* 877 set partitions (also checked by the Bell-number recurrence).
* 103 admissible types, 774 rejected; all 103 explicitly completed on
  at most seven points, with the resulting root pattern checked.
* All 576 pairs of four-point permutations: 2,304 root checks,
  52 distinct types, all admissible.
* Five bases 0,1/3,1/2,2/3,1; 515 full completed-model/base checks.
* Every table entry is at most the analytic cap, with exact rational
  entropy-product comparisons. The cap is attained for every base.
* p=1/2: M=1.0397207708399179, old cap=1.3862943611198906,
  difference=0.3465735902799727. This is exactly (1/2)log2.
* The genuine target has delta=-0.1155117709606206 at p=1/3,
  -0.2746765991340926 at p=1/2, -0.43181739761778837 at p=2/3.
  Exact signs confirm these are negative, not rounding artifacts.
* Maximum difference between conditional-entropy calculations:
  3.3306690738754696e-16. Minimum full-model information slack: 0.
* Nice priority 20, peak RSS 17,694,720 bytes, elapsed 0.262 seconds.

The wrapper again prints `nice: setpriority: Operation not permitted`;
the process inherited priority 20, as independently read and asserted.
No priority increase was attempted. The script uses only the standard
library, no workers, a 180-second alarm and an RSS assertion below 1 GiB.
No test failed. No new positive entropy-gap witness was obtained.

## 05:09 — independent target calculation and proof audit

Added a second derivation of the genuine target cost, conditioning first
on the two child outputs instead of enumerating seven bits. If a child
output is i, its root bit has probability q_1=1 or
q_0=p(1-p^2)/(1-p^3); its output probabilities are m_1=p^3, m_0=1-p^3.
Independence between the two disjoint child coordinate sets gives

    C0=h(p^3)+h(p)-sum_ij m_i m_j [h(p q_i q_j)-p h(q_i q_j)].

This gives the same C0 by exact entropy-product equality for all five
bases. The largest floating difference is 1.1102230246251565e-16.
Re-ran the same command after adding this independent check; exit 0,
same mathematical results, final peak RSS 17,924,096 bytes and elapsed
0.273 seconds. Final summary and table were regenerated by this run.

Audit of possible missing cases:

* Both implications in admissibility are needed: functionality alone
  permits noninjective maps and would introduce spurious types.
* Negative letters use inverse permutations. The separate signed window
  {1,a,a^-1} has exactly three admissible types: all equal, the two
  nonroot positions equal, and all distinct. The other two partitions
  violate bijectivity; the script checks this independently.
* Prefixes beyond W are required in general. Each reduced prefix in P
  has a prescribed outgoing edge or a reversed prescribed edge, so
  the realization proof covers cancellations and inverse letters.
* Noncommuting order matters: at decoder position a the encoder inputs
  are a,aa,ab; at b they are b,ba,bb. Both the class enumeration and
  full-model computation use that order.
* The one-point action proves M_bad>=H(p) for a hypothetical positive
  gap. This prevents dividing by zero or a negative coefficient.
* The degenerate bases p=0 and p=1 give zero costs and exact equality;
  no conditional probability with zero conditioning mass is evaluated.
* The analytic cap is re-derived without collision enumeration via
  H(E)+H(R|N)<=H(R)+H(E|R), since N includes E. Explicit two- and
  three-point actions prove attainability, rather than numerical maxima
  alone. Thus all load-bearing constants have a second derivation.
* Completing one rooted pattern gives a free-group action. It does not
  satisfy group relators at other roots and supplies no soficity claim.
  The proof now states this explicitly.

A first attempt to insert the last clarification used a mismatched patch
context and changed nothing; the corrected patch succeeded. No
mathematical assertion or computation failed. Remaining limitation: no
genuine positive-gap code was found, and the finite weighted optimization
was formulated but not solved. The next useful advance should constrain
distributions of rooted types, rather than only their individual costs.

## 05:12 — final artifacts

Wrote REPORT.md with the required PARTIAL verdict, the new theorem, sharp
example, validation command, actual limitations and next step. Final
read-back caught missing inline LaTeX delimiters introduced by string
escaping; repaired them without altering formulas. The repair and final
read-only artifact check ran as single-threaded Python under nice -n 15.

The final artifact check independently counted all 515 JSON table rows,
103 for each base, and checked the number of exact maximizers and maximum
cost against the summary. It verified all table comparison signs are
nonpositive, all 13 equation tags are present, and inline and display
math delimiters are balanced. Output:

    Final artifact audit passed: 515 table rows, five matching maxima,
    13 equation tags, balanced math delimiters.

The next worker can impose stationarity on this same 103-type table:
the pattern distributions on (1,a,b), (a,aa,ab), and (b,ba,bb) must be
equal, since a and b each permute the roots. This is a concrete finite
linear refinement that does not require a larger Bell-number search.
It was identified but not implemented here. All new files remain inside
this folder; the predecessor folders remain untouched.
