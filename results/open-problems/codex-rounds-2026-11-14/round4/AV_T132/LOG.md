# T132 round 4 verification log

Started 2026-11-15T04:17:18.128197+04:00.

1. Read both prior REPORT.md and LOG.md, round-3 PROOF.md and audit.py; the first folder has no PROOF.md or scripts. Read startup memory index, brain index and compute state (warn, owner_away_open, CPU saturated). Folder-only rule overrides global mesh/checklist/brain writes; none invoked. Commands use OMP_NUM_THREADS=1 nice -n 15; inherited process priority is 20. The nice warning reflects an already lower priority, as in prior work. No heavy computation.

2. Bounded initial web search: exact metric title plus error/correction/November, and spanning-tree planar-map metric/OpenAI/November. Opened arXiv abstract pages 2610.10501 and 2610.10505 and the metric manuscript community page. No later solution or primary error report located; community page still says No notes yet. Embedding papers remain different conclusions. Search finished within five minutes.

3. Choice of extension: audit the universal internal-norm comparison, especially its maximizing-zoom upper bound and finite-enlargement moment passage, as requested by round 3. First independently re-derive the deterministic fixed-offset implication before accepting its conditional result.

4. Independent re-derivation: put t_j=log_2(A_j)-pj. For fixed m, eventual fixed-offset bounds imply |t_(j+m)-t_j|<=c with c independent of m. Iterating in residue classes gives limsup |t_j|/j<=c/m; let m tend to infinity. Tightness and noncollapse of both normalized diameters bound a_n B_(2n) above and below. The earlier conditional implication holds; no proof of its input assertions is inferred.

5. Re-opened main.tex, sections/tree/bootstrap.tex, moments.tex, certificates.tex and comparison.tex through read-only GitHub fetch; saved exact returned TeX under sources/. Incorrect build/tree raw paths returned cache misses; corrected build/sections/tree paths succeeded. Copied prior VERIFY.md and its source files as explicitly marked inherited material, keeping every earlier folder read-only.

6. Read maximizing-zoom proof (bootstrap.tex lines 78–149), moment compactness/UI proofs, certificate-limit proposition, nonzero-local-cost lemma, transport proposition and interior reconstruction clause. The moment step can be isolated and checked independently: finite disjoint interval costs retain their unconditional product law under joint weak limits, and normalized dyadic costs satisfy q_l<=2^(-lp). Narrowed extension: prove an explicit uniform tail bound for their kth moments, including varying continuum laws and fixed dyadic enlargements. The separate spatial certificate-lifting step is not yet verified.

7. Wrote PROOF.md and provisional REPORT.md. New analytic result: for the normalized maximizing-zoom family, E[X^k; X>R] <= (1+2^(kp-1)) R^(-(kp-1)/(k-1)). Derived by multinomial expansion, independence, Holder/Markov and a dyadic partition chosen at scale R^(1/(k-1)); a separate fixed-partition limit checks UI. The bound implies a uniform (k+delta) moment and proves moment passage on every fixed dyadic enlargement. No certificate geometry is claimed verified.

8. Freshly opened all three introduction TeX files, lean/docs/211.md and FKCRT.lean using read-only GitHub fetch. Main theorem quotations and q>4/CRT formalization scope agree with the prior record; exact comparison will be run in audit.py. Primary arXiv pages confirm Nina Holden and Nina Holden/Pu Yu authorship and embedding scope.

9. A document-writing tool call failed at JavaScript parse time because a Markdown fence conflicted with its string delimiter; no command ran or file changed. Corrected the delimiter construction and wrote audit.py.

10. Tried to break the new analytic result: constructed a consistent shared-Bernoulli interval process that loses its moment if independence is dropped, and an independent additive Poisson process that loses its moment at kp=1. Neither satisfies all hypotheses of the lemma. Re-derived the exponent by balancing the two tail terms and checked the order of limiting operations by a fixed-partition proof. Added the details to PROOF.md. Preserved the prior normalization proof in PRIOR_PROOF.md and corrected inherited VERIFY.md proof links; appended the session-specific source record, Spot check and three-sentence recommendation. About to execute audit.py.

11. Ran `OMP_NUM_THREADS=1 nice -n 15 python3 audit.py`: exit 0. Output follows. The inherited priority is 20 (lower priority than requested 15); peak resident memory was under 19 MB and the command completed in under one second.

```text
nice: setpriority: Operation not permitted
OMP_NUM_THREADS=1; process priority= 20
All 4 exact main theorem blocks match freshly opened source TeX
No source drift in 3 introductions, moments, bootstrap or 2 Lean scope files
Exact multinomial/Hölder checks: 700 exponent vectors
Tail exponent and dyadic rounding: exact rational checks in 8 parameter cases
Illustrative k=6, p=1/3: theta=1/5, C=3 (not a value of d_sqrt(2))
Dependent example: r= 2 P(nonzero)= 1/16 unit kth moment=1
Dependent example: r= 10 P(nonzero)= 1/10000 unit kth moment=1
Dependent example: r= 100 P(nonzero)= 1/100000000 unit kth moment=1
Poisson boundary: lambda= 1/10 normalized fourth moment=1; P(nonzero)<=lambda
Poisson boundary: lambda= 1/1000 normalized fourth moment=1; P(nonzero)<=lambda
Poisson boundary: lambda= 1/1000000 normalized fourth moment=1; P(nonzero)<=lambda
Poisson polynomial [1,7,6,1] checked by recurrence and falling-factorial identity
Verdict format and local Markdown links pass
SHA256 411c5ed72963ddab908dde013f0d42a606fbd4f2a8d6bcd633e679ed075380a2 bootstrap.tex
SHA256 708e16605a48d8913eb9f73a27eb3f41f0d19d1d9b13906c22821bc5be16b93e moments.tex
SHA256 f856fa05b811f2a6fce12e420c337553d5c32ceaa4c417e5454fc1fe11751167 certificates.tex
SHA256 d57772c035ea3fbf0efd8a50bd533fa512013c2badde2a93c7ec4565f1eeb906 comparison.tex
SHA256 bc4826b62aa9fc383aca319c28db03dc4ba66f6d367500ae483afde684be84b4 metric-introduction.tex
SHA256 3b11009a3415f83309b45d312d0c90b1d905809900c6d697998cf699119131c6 critical-introduction.tex
SHA256 f3037597fa46851ad0f91719599d16aabc0cccaab23df66a0244a4be7d491714 clock-introduction.tex
Peak resident memory bytes: 18038784
All checks passed. These checks do not verify spatial certificate geometry.

```

12. Final scope audit: no full proof correctness verdict, positive-q exponent, uniform-vertex measure conclusion or Lean verification is claimed. The earlier conditional exponent implication holds; the new proved analytic estimate closes only the moment-preservation step under the stated retained interval structure. Remaining target: spatial upper-certificate comparison and interior lifting. REPORT.md records PARTIAL and successful validation; VERIFY.md preserves exact main theorem statements and adds the three-sentence recommendation. All writes stayed in this folder; earlier folders remained read-only. No git command, account creation, message, external mutation, subagent, GPU or heavy computation was used.

Task: “Verify: has open problem T132 been settled by the OpenAI math release?” First recorded local time: 15 November 2026, 04:17 Asia/Tbilisi.
