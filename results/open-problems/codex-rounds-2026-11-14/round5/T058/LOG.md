# T058 work log

Task: “take the NEXT checkable step on this problem, building on that work” — 15 November 2026; first recorded local clock 07:45:50 +04.

## 1. Orientation and bounded literature check

Only this folder will be changed. No git, external messages, subagents, or shared-state registrations. The folder-only instruction takes precedence over the general brain/mesh/checklist write requirements. Read the startup memory index and the compute state: status `warn`, mode `owner_away_open`, free memory 86%, CPU saturated. All computational checks will use one thread and nice >=15, with small fixed inputs.

Read the three predecessor reports, logs, proofs, audits and Python scripts (remaining sections are being inspected in smaller reads to avoid output truncation).

Within five minutes, searched the web for recent chromatic-number concentration results, the Zigzag Conjecture and the cube-root announcement. Opened Annika Heckel and Oliver Riordan, *How does the chromatic number of a random graph vary?*, https://arxiv.org/html/2103.14014; Robert Morris and Oliver Riordan, *Random cliques in random graphs revisited*, https://arxiv.org/abs/2504.00964 and https://arxiv.org/html/2504.00964v1; and Heckel's publication list https://annikaheckel.github.io/. No full solution was found. The 2025 cube-root talk remains a lead; a search result is not a verified paper theorem. One Oxford listing fetch failed with a cache miss. No SOLVED_ELSEWHERE.md is warranted. This is a bounded check, not an exhaustive literature survey.

## 2. Recheck in progress

Re-derived the forcing identity from round 4: the forced increment D is zero precisely when the chosen set was independent, and otherwise is at least one. Hence E|D-1|=Var(X)/mu-1+2q. The characteristic-function differential equation has leading coefficient -z, and integration gives z^2 epsilon/2+|z|^3/(6 sqrt(mu)). Positive association supplies a nonnegative threshold-covariance kernel; integrating it against the two exponential derivatives bounds the dependence by |st| Cov(U,V). No gap found in the earlier joint limit. Its overlap estimates will be checked independently before extending it.

Completed the remaining smaller reads. Re-derived the moment input by separating overlaps j<=k/2 from complementary sizes s=k-j: their midpoint logarithms are -u^2/2+O(u log u), u=log_2 n, so the endpoint bounds in round 4 apply uniformly. The mean expansion gives mu_k=n^(t+o(1)), mu_(k-1)=n^(1+t+o(1)); the normalized mixed covariance is O((log n)^(3/2)/sqrt(n)). Combined with the forcing and kernel arguments this verifies the joint Gaussian main claim analytically, by re-derivation rather than assumption.

Command: `OMP_NUM_THREADS=1 nice -n 15 python3 ~/codex_op_1114r4/briefs/T058/verify_joint.py` (current working directory is this round-5 folder, so its output file is local).

Exit 0. Status `all forcing, kernel and CF checks passed`; actual nice=20; elapsed 0.120709291 seconds; peak RSS 18,022,400 bytes. Reproduced all exact forcing distributions and covariance kernels for 1024 graphs on five vertices and 32768 on six, plus the 49 argument-pair checks per joint distribution. Full stdout is in local joint_verification.json. The launcher's `nice: setpriority: Operation not permitted` diagnostic reflects inherited nice=20, which the script verifies. Earlier main result holds. No earlier file was changed.

## 3. Chosen extension (before proof or computation)

Prove the packing lemma proposed in round 4. Let M_k be the largest number of pairwise vertex-disjoint independent k-sets. On each fixed band a<={f(n)}<=b with 0<a<b<2/3, target E(X_k-M_k)=o(sqrt(mu_k)), and hence transfer the previous joint Gaussian limit to (M_k,X_(k-1)). This is one extension: replacing the top count by a packing statistic, with an explicit error bound.

The proposed route counts every intersecting unordered pair, including one-vertex intersections; deleting at most one set per conflict leaves a packing. I will derive the exact expectation and its leading term, check it by exhaustive enumeration and independent incidence counting, and audit the threshold and centering. No concentration theorem for chi is claimed. The reason for choosing this piece is that it moves the existing limit law to an actual disjoint family, rather than another count moment, and directly addresses the last report's next lemma.

## 4. Proof written

Created PROOF.md. The deterministic bound is 0<=X-M<=Y, where Y counts all intersecting unordered pairs. Its expectation is (mu/2) sum_(j=1)^(k-1) h_j. The j=1 contribution divided by mu^2 k^2/(2n) is exactly binom(n-k,k-1)/binom(n-1,k-1)=1+O(k^2/n). The other terms are O(mu^2 k^5/n^2+mu k^2 n2^(-k)), whose relative error is O(k^3/n+(log n)^2/mu)=o(1) on any fixed interior band. Thus EY~mu^2 k^2/(2n), and E[(X-M)/sqrt(mu)]<=n^(3b/2-1+o(1)) when phase <=b<2/3. Markov's inequality and a direct characteristic-function comparison transfer the previous joint limit to (M_k,X_(k-1)). Centering M_k at its own expectation is also valid. Variance convergence is not claimed.

Next: exact graph enumeration for the deletion bound and the expectation, a second combinatorial derivation of the one-vertex constant, and finite exact audits of the convexity bounds. Finite checks will include phases above 2/3 to expose the method's limitation, without claiming failure of the packing lemma there.

Created verify_packing.py and launched `OMP_NUM_THREADS=1 nice -n 15 python3 verify_packing.py`. It enumerates every graph on five and six vertices, tests every k=2,...,n, computes the maximum packing by two algorithms, and checks the pair expectation and incidence identity in exact arithmetic. Its large-n section uses a descending hypergeometric recurrence and exact rational overlap sums, checking the proof's two convexity bounds and product formula. The run is still in progress; no success claim yet.

Created AUDIT.md. A second count chooses the common vertex first and then two disjoint (k-1)-sets, reproducing the factor 1/2 in EY_1. A separate greedy rejection argument reproduces X-M<=Y. Re-solving the mean condition gives mu=o((n/k^2)^(2/3)), agreeing with phase <2/3. Slutsky's theorem independently checks the characteristic-function transfer. Replaced a shorthand probabilistic power statement in PROOF.md with an explicit Markov bound for the o_p(n) covered vertices, so this scope statement needs no unproved lower-tail inference. No load-bearing mathematical claim has failed so far.

## 5. Exact packing verification completed

Command: `OMP_NUM_THREADS=1 nice -n 15 python3 verify_packing.py`.

Exit 0; status `all exact packing and overlap checks passed`; actual nice=20; elapsed 153.033764458 seconds; peak RSS 41,353,216 bytes. Full stdout is packing_verification.json. No mathematical check failed. All 1024 graphs on five vertices and 32768 on six were checked for every k=2,...,n, including exact agreement of two maximum-packing algorithms and all intersection-size expectations. The incidence double count and deterministic deletion inequality passed on every graph.

At n=6,k=3: E X=5/2, E M=31085/32768, E(X-M)=50835/32768, EY=135/32. The one- and two-vertex contributions are 45/32 and 45/16. These exact values demonstrate that the finite deletion bound need not be tight.

Every large-n descending recurrence matches independently evaluated binomial coefficients at selected overlaps and sums to binom(n,k). Both convexity bounds and the one-vertex product bounds pass as exact rational inequalities at all nine test points. Selected diagnostics:

| log2(n), rounded | phase | EY/sqrt(mu) |
|---|---|---|
|40.134060|.5|1051.565937608871|
|80.131604|.5|38.700715730504314|
|160.130408|.5|0.001313362417534816|
|80.195250|.625|708984.5677298708|
|160.193477|.625|695298.450708347|
|320.192601|.625|20002.92898574005|
|320.255384|.75|1.0011429333144586e22|

At phase .625 near 2^320, the larger-overlap contribution relative to the leading term is 3.4508818310906668e-62. Thus the obstruction at this finite size is the one-vertex term itself, not a loose bound on other overlaps. Even these enormous n do not make the packing approximation numerically small close to 2/3. The theorem is asymptotic and gives no advertised finite cutoff. The phase .75 value only shows this method's upper bound is too large there.

One final independent floating log-sum calculation will check the normalization without huge rational arithmetic and inspect larger exponents cheaply; it is a diagnostic, not a certified finite bound.

## 6. Independent numerical audit and completed report

Command: `OMP_NUM_THREADS=1 nice -n 15 python3 audit_scales.py`.

Exit 0; status `independent log-scale diagnostics passed`. The calculation in logarithmic coordinates, using log-gamma and log-sum-exp rather than rational overlap recurrence, agrees with all nine exact normalized EY values within 3.121142456e-9 in log10 units. The largest discrepancy is the smallest n, where the omitted finite-population correction is largest. Extended floating diagnostics at phase .625 give log10(EY/sqrt(mu)) about -0.273186 at log2(n)=640, -10.885101 at 1280, and -33.550038 at 2560. These illustrate convergence; they are not certified finite-precision probability bounds.

The first run took 0.01944 seconds and 15,925,248 bytes. Its tiny positive finite-population error bounds underflowed to displayed zero at the largest exponents. Changed the display and comparison to logarithmic units, then reran. Final run: 0.017311333 seconds, 15,712,256 bytes, actual nice=20, all comparisons passed. Full final output is scale_audit.json. No mathematical assertion failed. One combined documentation patch was rejected because a no-op context did not match AUDIT.md; inspection confirmed no files changed, then the substantive changes were reapplied separately.

REPORT.md now records the theorem, the rechecked predecessor claim, all commands, exact verification results, slow convergence, the unresolved phase endpoint and the missing relation to chi. The next proposed step is to control centered packing-loss fluctuations above phase 2/3 via larger conflict clusters. All artifacts remain local; earlier folders were only read.

Reopened the already consulted paper sections for source verification: Heckel–Riordan Conjecture 10 explicitly states the phase-dependent exponent max(theta/2,(1-theta)/2) for a sequence indexed by all n, with the lower probability bound for every sequence of shorter intervals. Morris–Riordan Theorem 1.4 concerns clique-family probabilities and does not give a chromatic concentration conclusion. This confirms the formulation caveat and the limited scope of the later paper; no additional status-search round was undertaken.

Final command: `OMP_NUM_THREADS=1 nice -n 15 python3 - <<'PY'` with inline pathlib/json/ast assertions. Exit 0. Verified nine required artifacts, parsed both local scripts without producing bytecode, checked all stored passing statuses and time/RSS/priority limits, resolved the predecessor-proof link, checked the PARTIAL verdict and removed pending language from the report, and confirmed no SOLVED_ELSEWHERE.md.

Output: `Artifact audit passed: required files, scripts, result statuses, resource limits and predecessor link; actual nice=20.`

Completed result: the proposed packing lemma holds in L1 on each fixed phase band inside (0,2/3), and transfers the joint Gaussian count limit to the maximum disjoint packing. No new concentration-width bound for chi. All computation is finished; no background worker remains.
