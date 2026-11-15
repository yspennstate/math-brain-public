VERDICT: PARTIAL proved phase-mesh-uniform two-wall link bounds and column independence

The round-5 envelope theorem holds under its stated assumptions. Its
variation argument and constants were independently re-derived in
[LOG.md](LOG.md). The bounded literature update found no verified solution
of the full problem.

New beyond round 5: [PROOF.md](PROOF.md) supplies the actual counts for
a two-wall link, using the round-4 gauges and normalized averaging over
mesh offsets. Four periods suffice. Consecutive marks need one neighboring
anchor comparison; the two window starts need at most three. The result is

    E X^- <= (24+147 C_(2,40)) beta,

uniformly in the finite phase-group size, row spacing and 0<s<1/10.
The theorem states its dominated-potential, product-input and conditional
road-period assumptions explicitly. It proves the local comparison input
with error 7 beta and radius H=40 before applying the earlier theorem.

For this construction, one link has input radius 408 in the tracking norm,
and uses only phases of walls j through j+244. Entire-column sigma-fields
are mutually independent within each residue class modulo 2000. These
constants concern the smaller-cutoff round-4 construction; they are not
claimed as the manuscript's own numerical constants.

Checks include a second argument at the objective level for averaging,
independent counts of every coefficient and support radius, and tests of
pauses, repeated visits, rounding ties and interior-edge attachments.
A categorical example distinguishes independent phase sampling from a
phase selected after seeing weights. No bound on a maximum over rows or
over all phase assignments follows from this result.

Commands were `env OMP_NUM_THREADS=1 nice -n 15` followed by `rg --files`
on the prior folders or `cat` on the reports, logs and proofs. There are
no prior research scripts, and the original folder has no PROOF.md.
No executable computation or simulation was required. The command details,
web queries, outputs and exact calculations are in LOG.md.

Opened primary source: OpenAI, *Strict convexity and differentiability of
the planar exponential first-passage limit shape*, September 24, 2026,
[manuscript](https://mathcommunity.github.io/oai-math-revised/papers/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/main.pdf),
Sections 10–11 and 14.1, with Sections 15.1–15.2 and 15.6–15.7 for scope.
No arXiv identifier was verified. The opened
[scope note](https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/212.md)
still excludes strict convexity from its selected formalization.

Failures and limits: direct PDF access failed; the landing-page link
worked. The sandbox denied nice's priority change; reads completed, and
no heavy program ran. No mathematical error was found in round 5. No
mutation outside this folder, git, subagent or external write was used.
Strict convexity and the contraction remain unproved here. Stationarity
of the full link field and the selected-path estimates are not proved by
the negative-moment and support bounds alone.

Next worker: audit the fixed-phase template reduction in Section 13.6 and
its later selected-row use. Track which template counts may depend on the
mesh, and which constants must stay uniform before s is fixed. Separately,
verify the common-baseline gauge comparison in Lemma 10.6 for the gauge
construction being used before asserting the full output support in 15.6.
The present result removes phase-mesh size from the single-link constants;
it does not remove costs of optimizing over many templates or rows.

Task: “take the NEXT checkable step on this problem, building on that work” —
first recorded 2026-11-15 10:08:11 Asia/Tbilisi (06:08:11 UTC;
receipt time not supplied).
