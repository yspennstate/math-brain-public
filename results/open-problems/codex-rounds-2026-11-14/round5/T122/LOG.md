# T122 work log, round 5

Task: “take the NEXT checkable step on this problem, building on that work”.
Received 2026-11-15 approximately 08:23 +04 (Asia/Tbilisi); first exact
clock read: 2026-11-15 04:25:47 UTC = 08:25:47 +04.

## Opening: read-only orientation and bounded literature check

Read startup memory and compute_state.json: status warn, mode
owner_away_open, CPU saturated. The task's folder-only restriction
supersedes shared-state mesh, checklist and brain logging. None of
those write-producing commands is run. No git or subagents.

Read REPORT.md, LOG.md and SOLVED_ELSEWHERE.md in the original and
round 3 folders, and round 3 PROOF.md. Read round 4 REPORT.md, LOG.md
and PROOF.md (the final few lines remain to be read). The file inventory
shows no research scripts in the earlier folders and no original
PROOF.md. Earlier folders are read only. An initial batched output was
truncated; the earlier files were then retrieved in smaller reads.

Commands: pwd; rg --files; cat; sed -n, with read commands launched as
`nice -n 15 env OMP_NUM_THREADS=1 ...`. As in the earlier sessions,
nice reports `setpriority: Operation not permitted`; the tiny reads
nevertheless execute. No research computation will be run while this
restriction holds. No GPU, MLX or torch.

Web searches (ended within five minutes):

* "random regular" "max-cut" "Parisi" 2026 formula
* "diluted" "spin glass" "Parisi formula" 2026
* "2609.19057" "2506.21296"
* "maximum cut" "regular" "Mézard-Parisi" November 2026
* "regular" "cavity" "formula" "2611" cut

Opened primary arXiv pages for Dmitry Panchenko, The Mézard-Parisi
formula, arXiv:2610.39545 (still v1 only), and Viktor Harangi, RSB bounds
on the maximum cut, arXiv:2506.21296 (v1). Opened full HTML of Amin
Coja-Oghlan and Will Perkins, Spin systems on Bethe lattices,
arXiv:1808.03440v1. No post-report regular-ensemble solution was found;
this bounded search is not a proof of absence. Known Poisson advances
were already handled by the earlier workers. Subsequent source reads
will concern these identified papers, not a continued literature search.

Preliminary independent recheck: on a d-regular graph,
Z_cut = 2^n exp(beta*d*n/2) Z_minus with the round 4 normalized Z_minus.
For g(beta)=log sum exp[-beta(U-min U)], g lies in [0,n log 2],
and convexity gives -g'(beta)<=n log(2)/beta. Integrating reproduces
the logarithmic finite-difference error in round 4. The invariant-law
specialization still needs comparison with the primary definition.

## 08:28 — earlier result rechecked; choice of one extension

Finished reading the round 4 proof. Read the source's general functional
(2.12), invariant-law definition (2.13)–(2.14), and Theorem 2.7 directly.
The round 4 scalar A and B factors, minus d/2 edge coefficient, uniform
spin prior and cancellation of constant edge scaling agree with the
source. Its POS check is the squared L2 distance between column-product
moments after a binomial expansion with nonnegative coefficients. Its
temperature error also follows independently from Gibbs entropy:
S=log Z+beta<E>, S<=n log 2 and log Z>=-beta min E.
The earlier principal conclusion holds, conditional on the stated
external theorem. Its proof has not been audited in full.

The HTML (2.13) has repeated edge-column indices in its M-product;
round 4 uses fresh indices for different factors. The extension below
will prove invariance for arbitrary bounded positive functions of any
finite set of sampled columns, including repeated use, so it does not
depend on resolving this indexing issue.

Opened Harangi's full paper and read Theorem 3.2: an arbitrary finite
RSB regular upper bound is already stated there with nested-measure
parameters. Thus a mere restatement would add little. The explicit
missing inclusion in round 4 offers a more useful checkable step.

CHOICE (before proof work): prove directly that every no-root finite
Ruelle-cascade trial in round 4 equation (11) induces a kernel law
invariant under its cavity row tilts. Use independent product coordinates
for the column space and prove cascade reweighting by successive marked
Poisson point processes. Then apply the already rechecked invariant-law
minimum to obtain the regular hierarchical UPPER bound in exactly round
4's normalization. This addresses the first next-worker request without
asserting the missing reverse inequality or a full solution. The claim
will be tested at r=1 and r=2 and with a nonconstant asymmetric h.

Potential obstruction to check: the tilt biases sampled column marks.
The column-space coordinate permutation can absorb the tree relabeling
in the weak-kernel quotient, but this must be proved explicitly, rather
than assuming that the biased marks are still uniform.

## 08:31–08:34 — proof saved and adversarial audit

Wrote PROOF.md and read it back in full with
`nice -n 15 env OMP_NUM_THREADS=1 cat PROOF.md`.
The main lemma is stronger than the required finite cavity case:
every bounded positive function of any finite set of sampled columns
preserves the law of the finite-cascade weak kernel. The proof uses
only the marked Poisson intensity calculation, from the bottom of
the cascade upward, then a coordinate permutation on the product
column space. It never assumes that the sampled marks remain uniform
after tilting. This proves the missing inclusion and hence the regular
hierarchical upper bound, conditional on the earlier external
invariant-law theorem.

Load-bearing checks, with no numerical program:

* Re-derived the Poisson scaling by substitution in the intensity:
  y=x*f/c gives intensity q*y^(-1-q)*E(f^q)/c^q. The correct scale
  is c=(E f^q)^(1/q), and the cascade ratios telescope to W/w^(0).
* Checked depth one directly. Checked depth two both by two successive
  markings and by nested power means. For w=f(Z1)g(Z2), the log scale
  is log E f^(zeta0)/zeta0 + log E g^(zeta1)/zeta1, so reversing the
  exponents would fail.
* Independently matched the result to Harangi Theorem 3.2: deepest
  exponent m1=zeta_(r-1), subsequent exponents are successive zeta
  ratios, and their product is zeta0. His star is 2*A, giving log 2;
  converting uncut pressure to cut pressure gives beta*d/2.
* Tested asymmetric endpoint messages h=+1 with probability 1/3 and
  -1 otherwise, with zeta=1/2 and the auxiliary tilt 2+h. The marked
  scale is ((sqrt(3)+2)/3)^2 and transformed plus-mark probability
  sqrt(3)/(sqrt(3)+2). The latter is not 1/3. Thus the proof must use
  weak-kernel coordinate relabeling, not an invalid claim of unbiased
  marks. No spin-flip assumption is hidden.
* Explicitly wrote the row map and inverse coordinate permutation to
  check their orientation. Added the measurability of the random
  kernel and the cascade total's finiteness and log integrability.
* Rechecked both shifts independently on the finite graph:
  U=d*n/2-Cut and Z_minus=2^(-n) sum exp(-beta*U), so
  p_cut=log 2+beta*d/2+Phi. Scaling every edge weight by kappa gives
  d*log kappa-(d/2)*log kappa=(d/2)*log kappa in the functional.

No counterexample found so far. What remains is a complete final
readback and a check of boundary cases and the stated scope.

## 08:34–08:35 — final checks and report

Read REPORT.md and LOG.md in full, and re-read the complete substantive
proof, including its additional exponent checks, with cat and sed -n.
The exact clock during this readback was 2026-11-15 04:33:59 UTC.
A full unfiltered `rg --files` inventory confirms there are no research
scripts to read in any earlier folder. Runtime logs/pid/exit files are
present and were not edited.

Checked constant h (deterministic kernel), h=0, messages at +/-1,
arbitrary measurable h, depth one, every strictly increasing finite
parameter sequence, N=M=0, repeated sampled columns and d*n even.
For h=0, with a_cut=(1+exp(beta))/2, the trial equals
log 2+(d/2)log a_cut; its beta=0 derivative is d/4 and its
zero-temperature slope is d/2. Independent fair-spin edge counting
and the total edge count reproduce these two values. All tilt bounds
are used only at finite beta; no uniform lower bound as beta grows
is required. No temperature limit is interchanged with a hierarchy
infimum. Degree two is outside the claim.

The only issue found in the final readback was minor prose repetition;
a cleanup patch first failed on context and was then applied with
the exact lines. It did not change the mathematics. The report's
PROVED verdict refers to the finite-cascade inclusion and its upper
bound consequence. The upper bound itself is already in the literature;
the fixed-degree equality and the o(beta) reverse comparison remain
open in this work. No numerical research computation was run, because
nice priority changes are denied. All three authored files are here.
