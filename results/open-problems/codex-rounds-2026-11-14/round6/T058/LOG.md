# T058 work log

Task: “take the NEXT checkable step on this problem, building on that work” — 15 November 2026, first recorded clock 10:13:54 +04.

## Orientation and bounded literature check

Only this folder is writable for this task. No git, subagents, shared brain/mesh/checklist writes, or external messages. Read the brain navigation index and compute state (warn, CPU saturated, owner_away_open). Checks use OMP_NUM_THREADS=1, nice >=15 and small bounded inputs.

The literature search was completed within five minutes. Searched for recent chromatic concentration results and the cube-root announcement; opened Annika Heckel and Oliver Riordan, *How does the chromatic number of a random graph vary?*, https://arxiv.org/html/2103.14014; Robert Morris and Oliver Riordan, *Random cliques in random graphs revisited*, https://arxiv.org/html/2504.00964v1; and the Oxford talk announcement https://www.maths.ox.ac.uk/node/70763. No full solution found in this bounded check. The talk announces a cube-root upper bound for certain n, not a full solution; no exact chromatic theorem obtained. The published conjecture remains the phase-dependent zigzag formulation. No SOLVED_ELSEWHERE.md warranted.

## Earlier result re-derived

Read predecessor reports, logs, proofs and scripts, in batches. For independent k-sets A,B with intersection j, the joint probability is q^2 2^(j choose 2). Consequently EY=(mu/2) sum h_j, where h_j=binom(k,j)binom(n-k,k-j)q2^(j choose 2), j=1,...,k-1. Independently counting the common vertex gives EY_1=(n/2)binom(n-1,k-1)binom(n-k,k-1)q^2, so its ratio to mu^2 k^2/(2n) equals binom(n-k,k-1)/binom(n-1,k-1). This tends to one. The predecessor's convexity split bounds the remaining sum by O(mu k^5/n^2+k^2 n2^-k). Its relative contribution is O(k^3/n+(log n)^2/mu)=o(1). Deleting an endpoint of each remaining conflict gives X-M<=Y. Dividing its expectation by sqrt(mu) yields exponent 3t/2-1. Thus the earlier L1 claim below 2/3 holds by independent re-derivation.

## Chosen extension, before proof or computation

Extend the packing central limit theorem to every fixed phase band inside (0,1), allowing a deterministic correction to the mean. The possible route is stronger than a triple-count expansion: the total expected number of pairs sharing at least two vertices tends to zero throughout these bands. Use a proved random-family approximation (after checking its hypotheses in the opened Morris–Riordan paper) to compare the entire independent-set family with the independent k-uniform hypergraph. In that model an Efron–Stein bound should give Var(X-M)<=mu^2 k^2/n=o(mu), since an added edge changes the loss only if it meets an existing edge. This directly targets the previous report's requested control of centered packing loss. The correction is initially defined as the independent-model expected loss; transfer of actual means needs a separate check and will not be assumed.

## Proof and first exact audit

Created PROOF.md. Checked the full hypotheses of Morris–Riordan Theorem 3.1, not just its abstract: use missing graph edges as ground elements, k-sets' internal edge sets as a symmetric binom(k,2)-uniform family, p=1/2 and pi=q. Their Delta_2 counts pairs meeting in a ground element, hence vertex intersection >=2. It equals (mu/2) sum_(j=2)^(k-1) h_j and is O(mu^2 k^5/n^2+mu k^2 n2^-k)=o(1) on every fixed interior phase band. The theorem explicitly permits variable graph size and copy size. It compares entire labelled families in total variation.

For the independent model H, c_n=E[|H|-nu(H)]. Revealing Bernoulli hyperedges and applying the product-variance inequality gives Var D(H)<=Nq(1-q)[1-(1-q)^R]<=mu^2 k^2/n, where R=N-1-binom(n-k,k). Adding one edge changes D by 0 or 1, and changes it by zero when it meets no present edge. Chebyshev plus total variation proves X-M-c_n=o_p(sqrt(mu)). This also transfers the round-4 JOINT Gaussian law with X_(k-1): the error event concerns the k-family only, so no simultaneous independent-model approximation for both families is needed. The correction is bounded by mu^2 k^2/(2n). This is a distributional statement and does not identify the actual mean.

Command: `OMP_NUM_THREADS=1 nice -n 15 python3 verify_centered.py`.

Exit 0, status `all exact centered-loss, pair-count and family-TV audits passed`. Full stdout is centered_verification.json. Actual nice=20; elapsed 0.652343625 seconds, peak RSS 17,727,488 bytes. Enumerated every independent hypergraph for (n,k)=(5,2),(5,3),(5,4),(6,3),(6,4), including 1,048,576 families in the (6,3) case. All edge-addition increments, exact rational loss variances and the entire chain of variance bounds pass at q=2^-binom(k,2), 1/4 and 3/4. For n<=5 a second vertex-subset packing algorithm agrees throughout. Enumerated every original graph for (5,2),(5,3),(5,4),(6,4); exact pair expectations agree with the earlier formula and an independent common-vertex count. Entire labelled-family TV is computed exactly, including TV=0 for k=2. These finite TV examples test the model definition, not the asymptotic comparison theorem.

One attempted no-op documentation patch used incomplete context and was rejected without changing files. No mathematical check failed. The remaining audit will recompute Delta and the normalized variance bound independently in logarithmic coordinates and recheck the joint-count input. Completed the remaining predecessor reads in smaller batches where earlier output had been truncated.

## Independent audit in progress

Command: `OMP_NUM_THREADS=1 nice -n 15 python3 ~/codex_op_1114r4/briefs/T058/verify_joint.py`. Exit 0; `all forcing, kernel and CF checks passed`; actual nice=20; elapsed 0.136992750 seconds; peak RSS 18,874,368 bytes. All output is local in joint_verification.json; the earlier folder remains unchanged. Independently checked its analytic forcing and association inputs when reading the proof; the exact rerun reproduces both five- and six-vertex distributions and all 49 argument-pair tests per joint distribution.

Created audit_scales.py. Command: `OMP_NUM_THREADS=1 nice -n 15 python3 audit_scales.py`. Running, with an internal 1150-second alarm. It checks exact binomial and descending-recurrence overlap counts at phases .5,.75,.875 near n=2^80,2^160,2^320, tests the proof's finite convexity bounds as rational inequalities, and independently recomputes all normalized scales in log space. Its extra floating diagnostics reach log2(n)=2560. No graph or large array is constructed.

Created AUDIT.md with a second variance derivation by independent coordinate resampling, an independent incidence count for R<=Nk^2/n, hand formulas for maximum packing when 2k>n and for complementary triples on six vertices, and checks of total variation, joint transfer, endpoint phases and expectation limitations. Added these closed-form checks to verify_centered.py, then reran with `OMP_NUM_THREADS=1 nice -n 15 python3 verify_centered.py > centered_run.txt`. Exit 0. The final run's complete output and metrics are recorded in centered_verification.json and centered_run.txt. No mathematical check failed.

## All computations finished

Final verify_centered.py run: 1.256263917 seconds, 17,268,736 bytes peak RSS, actual nice=20. It covers 1,083,424 hypergraph families and 550,992 edge-addition checks. The closed-form and complementary-pair additions pass. For example n=5,k=2,q=1/2 gives loss variance 2276567/1048576 and exact Efron–Stein bound 2355/1024; n=5,k=3,q=1/8 gives mean loss 550910705/1073741824. These values were checked by different enumerations or closed forms.

audit_scales.py exited 0: `all exact overlap and independent log-space audits passed`; elapsed 185.922224875 seconds, peak RSS 69,681,152 bytes, actual nice=20. All nine descending hypergeometric recurrences agree entry by entry with direct binomial coefficients. Both finite convexity bounds, the one-vertex product bound and the normalized independent-model variance bound pass as rational inequalities. Maximum discrepancy from the independently computed log-space values is 2.22258e-11 in log10 units. Complete output: scale_audit.json.

Selected exact diagnostics (all entries are base-10 logarithms):

| log2(n) | phase | Delta | EY/sqrt(mu) | variance bound / mu |
|---|---|---|---|---|
|80.258894|.75|1.655477|10.113493|.338361|
|160.256544|.75|-2.930572|14.565927|-4.511279|
|320.255384|.75|-13.530562|22.000496|-15.403888|
|160.319612|.875|3.009432|23.289651|1.298209|
|320.318167|.875|-1.699471|39.699883|-3.610597|

These display why subtracting a deterministic loss correction matters, and also why no finite cutoff may be guessed near the upper boundary. The independent log-space method extends the scales to log2(n)=2560 without material memory use; those extra values are floating diagnostics only. The earlier uncentered scale at phase .75 near 2^320 agrees with the round-5 recorded value (about 1.00114e22). The exact Delta bound can remain above 1 even when Delta itself is below 1 at a tested finite n; the proof is asymptotic.

Reopened the existing sources to verify Theorem 3.1's complete setup and Conjecture 10's all-n quantifiers. No additional broad literature search was undertaken. Created REPORT.md with PARTIAL verdict and replaced its pending audit language after the successful run. The chosen piece is complete: a deterministic correction makes the packing loss o_p(sqrt(mu)) on every fixed interior phase band, transferring the previous joint Gaussian law. Actual-mean centering, an explicit additive approximation to the correction, and a relation to the chromatic cost of the remaining graph remain open here.

Final command: `OMP_NUM_THREADS=1 nice -n 15 python3 - <<'PY'` with inline ast/json/path assertions. Exit 0. Output: `Artifact audit passed: scripts parse, all result statuses pass, resource limits hold, predecessor links resolve; actual nice=20`. Required proofs, report and log are nonempty; every stored computation passed within the memory, priority and time limits; the report has its required PARTIAL first line and no pending audit language. No SOLVED_ELSEWHERE.md is present. All computations have exited and no background worker remains. Earlier folders were read only; all new files are in this folder.
