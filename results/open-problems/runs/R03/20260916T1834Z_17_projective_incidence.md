Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED; GPT-6 / maximum was requested, but the exposed scheduler still has no model or reasoning selector or authenticated runtime telemetry, so GPT-6 maximum is not claimed. METRIC MOVED: the strict collision-subtracted certificate improves from `r(10)<=437.96141105148837...` to `r(10)<=275.9996818469674...`, and the same new theorem gives `r(11)<=525.1358249571144...` instead of the retained C249 `985.0384031182641...`. Section-B methods actually used: #2 ATTACK THE NEGATION FIRST, #16 COMPUTE EVERY SMALL CASE AND STARE AT THE SEQUENCE, #18 SAY IT IN ANOTHER LANGUAGE.**
Problem: **iid Rademacher square-matrix singularity — Komlós (1967) lineage; Jain--Sah--Sawhney (2021), Conjecture 1.1 specialized to uniform Rademacher; Vu (2020), Section 2, Conjecture 2.2; Sahasrabudhe (2025), Eq. (4.1). Overall source status: OPEN / R03 status: PARTIAL.**

# R03 run 17 — projective modular null incidence after exact collision removal

Run ID: `20260916T1834Z_17_projective_incidence`  
Repository: `yspennstate/math-open-problems`, branch `master`.

## 1. Continuity, source, exact target, and fixed metric

Before new mathematics I reread/recovered the campaign controls `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the newest own report `runs/R03/20260916T1808Z_16_exact_trivial_rowbound.md`, the current R03/F0001 intake lineage by repository search, the newest discoverable neighboring R02 state, and the newest R04 package. Large intake JSONL responses remain connector-truncated, so I do not claim a semantic row-by-row reread of all roughly 780 intake rows.

Current source chain checked again on 2026-09-16:

1. J. Komlós, *On the determinant of (0,1)-matrices* (1967): historical nonsingularity lineage.
2. Van H. Vu, *Recent progress in combinatorial random matrix theory* (2020), Section 2, Conjecture 2.2: iid Rademacher model; the symmetric dependent-entry ensemble is separate in Section 3.
3. Vishesh Jain, Ashwin Sah and Mehtaab Sawhney, *Singularity of discrete random matrices*, arXiv:2010.06554 / GAFA 31 (2021), Conjecture 1.1. Their full sharp theorem covers finite-support laws not uniform on their support. Their uniform-support theorem, including iid Rademacher, is exponential-scale, and their paper explicitly records unresolved issues in the Irmatov Rademacher resolution claim.
4. Julian Sahasrabudhe, *Probabilistic combinatorics at exponentially small scales*, arXiv:2512.15077v1 (17 Dec 2025), Eq. (4.1):
   \[
   \Pr(\det B_n=0)=(1+o(1))2n^2 2^{-n}.
   \]
   The text says establishing this for `{-1,1}` matrices remains perhaps the central open problem in the area, then switches to the symmetric ensemble.
5. Thomas Voigt and Günter M. Ziegler, *Singular 0/1-matrices, and the hyperplanes spanned by random 0/1-vectors* (2006).
6. Vishesh Jain, Ashwin Sah and Mehtaab Sawhney, *Rank deficiency of random matrices*, arXiv:2103.02467: fixed-corank exponential rates, not the sharp corank-one prefactor.

The owner-normalized exact leading expression is

\[
\Pr(\det B_n=0)=(1+o(1))n(n-1)2^{1-n}
=(1+o(1))2n(n-1)2^{-n}.
\]

This matches Sahasrabudhe's `2n^2 2^{-n}` asymptotically while retaining the exact signed-pair event count before overlaps.

Let `T_n` be the exact union of all equal/opposite row-pair and column-pair events. Retained C225 gives the matching lower asymptotic with explicit overlap correction. The fixed metric is

\[
\boxed{r(n):=2^n\Pr(\det B_n=0,\ T_n^c).}
\tag{M}
\]

Sharp closure is equivalent to

\[
\boxed{r(n)=o(n^2).}
\]

The prior strict certificate was C249:

\[
r(10)\le
\frac{4039481031913758122055}{9223372036854775808}
=437.96141105148837\ldots,
\]

and its checker gave `r(11)<=985.0384031182641...`.

Retain without re-deriving C225--C249 and killed routes X27--X28, subject to the prior-art correction in Section 7 below.

## 2. Idea before code: #18 SAY IT IN ANOTHER LANGUAGE

Run16 counted collision-free singular binary matrices directly. This run translates the same residual into a finite-field **projective null-incidence** problem and then uses Möbius inversion only to enforce the already-fixed collision-free condition.

Retained C240 maps an iid sign matrix of order `n` to a uniform binary matrix `A` of order

\[
m=n-1
\]

without changing singularity. Retained C246 identifies `T_n^c` exactly with

\[
\mathcal G_m:=\{A\in\{0,1\}^{m\times m}:\text{ every row and column is nonzero and pairwise distinct}\}.
\]

Fix a prime `p`. For `A` write

\[
d_p(A):=m-\operatorname{rank}_{\mathbb F_p}A
\]

and define its number of projective left-null directions

\[
Z_p(A):=\frac{p^{d_p(A)}-1}{p-1}.
\]

If `A` is singular over the reals, choose a primitive integer left-null vector `a`. For **every** prime `p`, its reduction modulo `p` is nonzero because the coordinates have gcd one, and it remains a left-null vector. Hence

\[
\mathbf 1_{\{\det A=0\}}\le Z_p(A).
\tag{2.1}
\]

This is the key asymmetry from the preceding F3 invertibility certificate: rather than proving nonsingularity by one modulus, count all projective modular null witnesses of the already collision-free matrices.

Define the exact incidence count

\[
S_{p,m}:=\sum_{A\in\mathcal G_m}Z_p(A).
\tag{2.2}
\]

Then immediately

\[
\boxed{
\Pr(\det B_n=0,T_n^c)
\le \frac{S_{p,n-1}}{2^{(n-1)^2}}
}
\tag{C250.1}
\]

and therefore

\[
\boxed{
r(n)\le R_p(n):=2^{n-(n-1)^2}S_{p,n-1}.
}
\tag{C250.2}
\]

This is valid for **every prime `p` and every `n>=2`**.

## 3. R03-C251 — exact partition-lattice formula for `S_{p,m}`

**STATUS: PROVED.**

For `c in F_p^b` put

\[
h_p(c):=\#\{y\in\{0,1\}^b:c\cdot y=0\pmod p\},
\]

and define

\[
G_{p,b}(m):=\sum_{c\in\mathbb F_p^b}(h_p(c)-1)_m,
\tag{3.1}
\]

where `(x)_m=x(x-1)\cdots(x-m+1)` is the falling factorial. Let `s(r,k)` be the signed Stirling number of the first kind.

Then

\[
\boxed{
S_{p,m}
=\frac1{p-1}
\sum_{b=0}^{m}s(m+1,b+1)
\left[
 p^{m-b}G_{p,b}(m)-(2^b-1)_m
\right].
}
\tag{C251}
\]

### Proof

Adjoin an artificial row index `0`, whose row is fixed to the zero vector. Requiring the `m` actual rows to be nonzero and pairwise distinct is equivalent to requiring all `m+1` rows indexed by `{0,1,...,m}` to be distinct.

Use Möbius inversion on the partition lattice `Pi_{m+1}`. For a partition `pi`, let `B_0` be the block containing the artificial zero index and let the remaining `b` blocks be `B_1,...,B_b`. Its Möbius value is

\[
\mu(\pi)=\prod_{B\in\pi}(-1)^{|B|-1}(|B|-1)!.
\]

Fix a projective normal `[a] in P^{m-1}(F_p)`. Under the row equalities encoded by `pi`, a binary column is specified by `y in {0,1}^b`; rows in `B_0` are forced to zero. Its null condition is

\[
\sum_{j=1}^{b}\left(\sum_{i\in B_j}a_i\right)y_j=0.
\]

Thus, with the linear aggregation map

\[
\Phi_\pi(a)_j=\sum_{i\in B_j}a_i,
\]

the number of available column patterns satisfying the null equation is `h_p(Phi_pi(a))`. The zero column is forbidden, and all `m` columns must be pairwise distinct, so the number of ordered column choices is exactly

\[
(h_p(\Phi_\pi(a))-1)_m.
\]

Hence Möbius inversion gives the number of collision-free matrices having `[a]` as a left modular null direction:

\[
C_p([a])=
\sum_{\pi\in\Pi_{m+1}}
\mu(\pi)(h_p(\Phi_\pi(a))-1)_m.
\tag{3.2}
\]

Now sum (3.2) over projective nonzero `a`. For a fixed partition with `b+1` blocks, `Phi_pi:F_p^m -> F_p^b` is surjective and every fibre has size `p^{m-b}`. The summand is invariant under multiplication of `a` by a nonzero scalar, so

\[
\sum_{[a]}(h_p(\Phi_\pi(a))-1)_m
=\frac{p^{m-b}G_{p,b}(m)-(2^b-1)_m}{p-1};
\tag{3.3}
\]

the subtracted term is exactly the contribution of `a=0`.

Finally, the sum of partition-lattice Möbius values over partitions of `m+1` elements into `b+1` blocks is

\[
\sum_{\pi:|\pi|=b+1}\mu(\pi)=s(m+1,b+1).
\]

Substitute (3.3) into (3.2) and sum by `b`. This is C251. QED.

For exact computation without enumerating `p^b` coefficient vectors, group coefficients by their multiplicities `nu=(nu_0,...,nu_{p-1})`. If

\[
H_p(\nu)
=[z^0]\prod_{j=0}^{p-1}(1+z^j)^{\nu_j}
\quad\text{in }\mathbb Z[z]/(z^p-1),
\]

then

\[
G_{p,b}(m)=
\sum_{\nu_0+\cdots+\nu_{p-1}=b}
\frac{b!}{\prod_j\nu_j!}
(H_p(\nu)-1)_m.
\tag{3.4}
\]

Equations C251 and (3.4) are finite exact integer formulas for every prime and every dimension.

## 4. #2 ATTACK THE NEGATION FIRST

Before accepting C251, the exact checker searched for a counterexample to the incidence identity on **every binary matrix** through `m=4`, for `p=3` and `p=7`. It independently:

1. filters `A in G_m` directly;
2. computes `rank_Fp(A)` by exact modular elimination;
3. sums `(p^{d_p(A)}-1)/(p-1)`;
4. compares to C251.

All eight brute-force comparisons agree exactly. In particular, at `m=4` the two incidence counts differ (`1920` for `p=3`, `1800` for `p=7`), which is a useful check that the prime parameter is genuinely doing mathematical work rather than merely rewriting the same bound.

I also attacked the tempting stronger heuristic “the prime `7` that is best at `n=10` remains the best finite-field choice.” It is already false at `n=11`:

\[
R_{11}(11)=525.1358249571144\ldots
< R_7(11)=530.4294970077205\ldots.
\]

This is **R03-X29 — DISPROVED ROUTE:** do not freeze one small prime as a supposedly universal optimum.

## 5. #16 COMPUTE EVERY SMALL CASE AND STARE AT THE SEQUENCE — metric movement

For `n=10` (`m=9`), the exact projective-incidence counts are

\[
\begin{array}{c|c}
p&R_p(10)\\ \hline
2&725.9885342440617\ldots\\
3&399.7974051930277\ldots\\
5&290.1636106907137\ldots\\
7&\mathbf{275.9996818469674\ldots}\\
11&286.7446185240955\ldots\\
13&296.5644084734106\ldots
\end{array}
\]

The best tested prime is `p=7`, with

\[
S_{7,9}=651685823418402269683200
\]

and, after reducing the rational,

\[
\boxed{
R_7(10)
=\frac{1272823873864066932975}{4611686018427387904}
=275.9996818469674\ldots.
}
\tag{C252.1}
\]

This improves the previous strict R03 certificate by

\[
\frac{1493833284185624256105}{9223372036854775808}
=161.96172920452096\ldots.
\]

At `n=11`, the tested values are

\[
R_7(11)=530.4294970077205\ldots,
\]

\[
\boxed{
R_{11}(11)
=\frac{1269700515190567964091374325}{2417851639229258349412352}
=525.1358249571144\ldots,
}
\tag{C252.2}
\]

and

\[
R_{13}(11)=537.2705245480341\ldots.
\]

The previous C249 value at `n=11` was `985.0384031182641...`, so the improvement is substantial there as well.

### Full-domain retained envelope

Let `r_exact(n)` denote the retained exact published values through `n=9`, and let `R_C249(n)` be the retained all-`n` C249 certificate. A new explicit certified envelope on the complete domain is

\[
\boxed{
\mathcal R_{17}(n)=
\begin{cases}
r_{exact}(n),&1\le n\le9,\\
\min\bigl(R_{C249}(n),R_2(n),R_3(n),R_5(n),R_7(n),R_{11}(n),R_{13}(n)\bigr),&n\ge10.
\end{cases}}
\tag{C252.3}
\]

Every term in the second line has an exact finite formula. Thus C252.3 is a rigorous uniform upper-bound function for the owner's fixed metric on its full domain.

**Limitation:** this is not the source asymptotic. Fixed finite-field moduli introduce modular-singularity false positives, and no estimate here proves `mathcal R_17(n)=o(n^2)`. The source problem remains OPEN.

## 6. Why this route is materially different, and its next asymptotic question

The earlier F3 route lower-bounded real invertibility by modular invertibility. C250 instead weights **projective null incidences after both row and column trivial collisions are removed exactly**. It therefore localizes the precise source residual rather than the whole singular event.

The observed prime drift (`7` at `n=10`, `11` at `n=11`) suggests that treating `p` as a scale parameter may be more useful than any fixed-prime theorem. The next question is not to enumerate another support class; it is to estimate

\[
\inf_{p=p(n)}R_p(n)
\]

for a growing prime scale. A source-closing version would need

\[
\inf_p R_p(n)=o(n^2).
\]

The obstruction is clear: `Z_p(A)` counts modular false positives, while large `p` increasingly weights genuine higher corank through `(p^d-1)/(p-1)`. Retained C244 makes real corank at least two exponentially negligible for fixed corank, but that theorem cannot simply be multiplied by an arbitrarily fast-growing `p`. The useful next attack is therefore a **two-scale estimate**: control modular corank-one false positives at a growing prime and genuine higher real corank separately, choosing the prime only after both terms are quantified.

## 7. Prior-art correction: earlier support classifications are not novel

A fresh failure-oriented literature search found a directly relevant paper that the earlier fixed-support reports did not cite:

Richard Arratia and Stephen DeSalvo, *On the singularity of random Bernoulli matrices - novel integer partitions and lower bound expansions*, arXiv:1105.2834 (2011).

They already prove that the only novel partitions with at most six parts are

`11, 1111, 21111, 111111, 221111, 311111, 322111`

and that there are fourteen novel partitions with seven parts. Therefore the **partition-type classification content** of retained R03-C226--C236 must be relabelled **KNOWN / independently rediscovered and exactly checked**, not novel. The R03 exact finite certificates remain valid as independent checks, and some explicit direction counts / target-scale bookkeeping may be additional, but I do not claim novelty for the classification itself.

Arratia--DeSalvo also study interaction between left and right null vectors. Accordingly, the general idea of controlling that interaction is prior art; retained X28 remains a useful exact obstruction to *naive conditional independence*, not a new research programme by itself.

The dated search artifact records this correction and the bounded search for the new finite-field incidence formula. No exact prior occurrence of C251 was located, but that is negative search evidence only; novelty of C251 is **UNVERIFIED**.

## 8. Exact self-check

Source:
`artifacts/R03/20260916T1834Z_17_projective_incidence_exact.cpp`

Archived output:
`artifacts/R03/20260916T1834Z_17_projective_incidence_exact.out`

Executed with exact `boost::multiprecision::cpp_int` arithmetic. The checker:

1. exhausts every binary matrix through `m=4` for `p=3,7` and verifies the direct projective-null incidence sum equals C251 exactly;
2. computes C251 exactly for `n=10` and primes `2,3,5,7,11,13`;
3. checks the strict improvement over the exact prior C249 fraction;
4. computes `n=11` at `p=7,11,13` and exactly verifies `p=11` beats `p=7` and `p=13`;
5. terminates `SELF-CHECK PASS`.

Local SHA-256 values at execution were:

- source: `473e35aa1728299f7b02ddb444416027f09b618279eae1ff0080f7033f21f328`;
- output: `40fdd683e4aee1fd10b7da7e97ff1c4dde822032e5efe26cd6f5a2b621ea4425`.

These are self-checks, not independent audits.

## 9. Independent audit duty: newest R04 package

The newest R04 report is now
`runs/R04/20260916T181213Z_i0027_diameter_profile.md`, on the Aldous--Fill Open Problem 6.13 Kemeny/`tau_0` half.

I independently audited its theorem

\[
\limsup_{n\to\infty}\frac{M_n}{n^3}
\le\frac1{27\sqrt2}=\frac{\sqrt2}{54}.
\]

I record

\[
\boxed{\texttt{R03-AUDIT-R04-I0027-C2-05 = PASS}}
\]

**claim-scoped**, not a package closure audit.

The key external input was independently source-checked: Mukwembi's 2012 Gutman-index proof contains the diameter-sensitive estimate

\[
\operatorname{Gut}(G)\le\frac1{16}d(n-d)^4+O(n^4)
\]

before its final global maximization. The remainder is uniform for `0<=d<=n-1` because the displayed lower-order terms are polynomial in `d,n`.

The rest of R04-C2 rederives correctly:

\[
K(G)=\frac1{2m}\sum_{u<v}d_ud_vR_{uv},
\quad K\le dm,
\quad 2mK\le\operatorname{Gut}(G),
\]

then splits `m/n^2` below/above `n^{-1/2}` so the `O(n^4)/m` error is harmless, and uses

\[
\min\left(\delta\alpha,
\frac{\delta(1-\delta)^4}{32\alpha}\right)
\le
\frac{\delta(1-\delta)^2}{\sqrt{32}}.
\]

The last profile is maximized at `delta=1/3`, giving `sqrt(2)/54`. I did **not** pass or assume R04's separate open strengthening `K<=m d/2`.

## 10. Method outcomes

**#18 SAY IT IN ANOTHER LANGUAGE — SUCCESS.** The collision-free singularity residual becomes a projective finite-field null-incidence problem. Partition-lattice Möbius inversion turns that language into the closed formula C251.

**#2 ATTACK THE NEGATION FIRST — SUCCESS diagnostically.** Exhaustive small matrices found no counterexample to C251 and then the prime-comparison search **did** refute a tempting fixed-`p=7` optimum at `n=11`. This prevented hard-coding the wrong modular scale.

**#16 COMPUTE EVERY SMALL CASE AND STARE AT THE SEQUENCE — SUCCESS.** The prime table exposed a real movable parameter and produced the strict metric improvement `437.9614 -> 275.9997` at `n=10`, plus `985.0384 -> 525.1358` at `n=11`.

This triple differs from the preceding run's `15/25/30`.

## 11. Model/scheduler capability status

Still unchanged. The exposed automation mutation interface offers title, prompt, schedule / relative start, timing mode and enabled state. It exposes **no model-family selector and no reasoning-effort selector**, and no authenticated runtime telemetry. Therefore GPT-6 / maximum can only be requested in prompt text here; it cannot be verified or set as a native scheduler field from this interface.

`RESULTS.md` now records the important context distinction: a full P26 prompt update succeeded in one authorized P/C context, while another exposed context had returned `You cannot modify this task`, and all R-series native edits were denied there. This is consistent with an ownership/workspace authorization boundary, not a repository setting. The legitimate workaround is the owning/admin-authorized native-task context or platform support. Do not bypass it and do not create a duplicate task. This run made no scheduler changes.

## 12. Cumulative target ledger

| Item | Status |
|---|---|
| Source asymptotic `P(det B_n=0)~n(n-1)2^(1-n)` | **OPEN** |
| C225 exact pair-collision lower bound incl. overlaps | **PROVED / retained** |
| C226--C236 support-pattern classification | **KNOWN/REDISCOVERED in core pattern scope after Arratia--DeSalvo prior-art correction; R03 exact checks retained** |
| C237 growing-support payment through `3 sqrt(n)/4` | **PARTIAL / retained** |
| C238/C239 JSS structured reduction | **PARTIAL / retained** |
| C244 real corank `>=2` target-negligible at fixed corank scale | **PROVED REDUCTION / retained** |
| C246 exact `T_n^c` count | **PROVED / retained** |
| C247 exact integer residual identity | **PROVED / retained** |
| C249 prior strict finite-field envelope | **PROVED / retained** |
| **C250 projective modular incidence upper bound** | **PROVED NEW** |
| **C251 exact partition-lattice incidence formula** | **PROVED NEW; novelty UNVERIFIED** |
| **C252 full-domain improved certified envelope** | **PROVED NEW; metric moved** |
| **X29 fixed `p=7` optimum** | **REFUTED as an internal route, not a source refutation** |
| `r(n)=o(n^2)` | **OPEN** |
| symmetric Bernoulli ensemble | **SEPARATE / not imported** |
| Irmatov/Blinovsky exact-resolution claims | **NOT VERIFIED / not accepted as closure** |

## 13. Next attack

Do **not** return to another fixed-support enumeration. The next source-relevant question generated by C250--C251 is quantitative and global:

\[
\boxed{
\text{Can one choose a growing prime }p(n)\text{ so that }R_{p(n)}(n)=o(n^2)?
}
\]

The first honest decomposition should separate:

1. real collision-free corank-one matrices, each contributing one projective direction once `p` does not introduce extra modular rank loss;
2. real corank at least two, whose known exponential probability must be balanced against the factor `1+p+...+p^{d-1}`;
3. real-nonsingular but mod-`p` singular matrices, i.e. the actual modular false positives.

A useful next run should attack the third term by determinant anti-concentration/divisibility or by estimating C251 asymptotically at a growing prime. If that route gives no movement for three runs, the stuck protocol applies; the stagnation count is **not reset** by renaming this decomposition.

## 14. Structured ledger delta

```yaml
ledger_delta:
  track: R03
  source:
    lineage: "Komlos 1967"
    locators:
      - "Vu 2020 Section 2 Conjecture 2.2"
      - "Jain-Sah-Sawhney arXiv:2010.06554 Conjecture 1.1, Rademacher specialization"
      - "Sahasrabudhe arXiv:2512.15077 Eq. (4.1)"
  target: "P(det B_n=0)=(1+o(1)) n(n-1) 2^(1-n)"
  metric: "r(n)=2^n P(det B_n=0, T_n^c), complete-domain rigorous upper envelope"
  before:
    n10: "<=4039481031913758122055/9223372036854775808 = 437.96141105148837..."
    n11: "<=985.0384031182641... via retained C249"
  after:
    full_domain: "exact retained n<=9; for n>=10 min(C249,R_p for p in {2,3,5,7,11,13})"
    n10: "<=1272823873864066932975/4611686018427387904 = 275.9996818469674..."
    n11: "<=1269700515190567964091374325/2417851639229258349412352 = 525.1358249571144..."
  status: PARTIAL
  source_status: OPEN
  movement: true
  unchanged_count: 0
  methods: [2,16,18]
  exact_evidence:
    - "artifacts/R03/20260916T1834Z_17_projective_incidence_exact.cpp"
    - "artifacts/R03/20260916T1834Z_17_projective_incidence_exact.out"
    - "artifacts/R03/20260916T1834Z_17_status_search.md"
  proof_ids: [R03-C250,R03-C251,R03-C252]
  killed_routes_added: [R03-X29]
  prior_art_correction: "Arratia-DeSalvo 2011 already classifies core novel partitions through support 7"
  outgoing_audits:
    - "R03-AUDIT-R04-I0027-C2-05=PASS claim-scoped"
  closure_audits:
    p26: NONE
    second_other_track: NONE
```

**NO CLOSURE CLAIM.** No shared root ledger, peer file, Gmail, Drive, public posting, purchase, permission, workflow or scheduler state was changed in this run.
