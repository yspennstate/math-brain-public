# T122 work log

Task received: 2026-11-15 01:32 +04 (Asia/Tbilisi).

## 01:32–01:35 — prior files and literature check

Read the earlier REPORT.md, LOG.md, and SOLVED_ELSEWHERE.md in
`~/codex_op_1114/briefs/T122` without editing them.
`rg --files` confirms there is no PROOF.md or research script there.
Read the startup memory index and compute-state snapshot (status warn,
mode owner_away_open). No research computation is needed. The task's
folder-only write rule overrides shared mesh/checklist/brain logging;
none of those commands is invoked because they write outside this folder.
No git or subagents.

Commands: `pwd`, `rg --files`, `sed -n`, `cat`, `date '+%Y-%m-%d %H:%M:%S %Z'`.
Initial clock: 2026-11-15 01:32:42 +04.

Web queries: `"Mézard-Parisi formula" Panchenko 2610.39545 maximum cut regular`
and `"maximum cut" "cavity" "2026" formula regular`.
Opened arXiv abstracts 2610.39545 and 2610.39542, the full HTML of
2610.39545v1, and the primary OpenAI model.tex linked by the earlier report.
The latter still states the general equality at lines 122–127. A guessed
main-theorem.tex path failed; model.tex already contains the theorem.
No post-report advance has been identified in this first search.

Independent preliminary check of the earlier result: with
theta(s,t)=beta(1-st)/2,
exp(theta)=(1+exp(beta))/2 * (1-(exp(beta)-1)/(exp(beta)+1)*st).
The two possible products st=1,-1 give 1 and exp(beta), respectively.
Thus b<0 and (-b)^k>=0 for every k. A finite sum of 2^n weights gives
0 <= log Z/beta - MaxCut <= n log(2)/beta. The earlier
temperature reduction holds. A full graph-coupling audit will be written
in PROOF.md.

## Chosen checkable piece (before further deduction)

Check whether Theorem 2.1's general lower bound in Panchenko's arXiv
paper combines with its stated interpolation upper bound for the
deterministic antiferromagnet. If so, record the direct arXiv route,
including the precise functional; this removes the earlier report's
dependence on a separate manuscript for this implication. This is a
scope audit and elementary corollary, not a new proof of the external
theorem. The user's literature stopping rule takes precedence over
attempting the abandoned subdivision lemma or new regular-graph research.

## 01:35 — literature cutoff and direct route found

Literature searching ended within five minutes of the opening clock.
Additional queries used the phrases `max cut regular Mézard November 2026`,
`2610.39545 antiferromagnetic regular`, and a max-cut Parisi-formula query
restricted to 2026-11-14 through 2026-11-15. No additional solution or
regular-ensemble extension was identified. This is not a proof of absence.

Read Panchenko, arXiv:2610.39545v1, equations (2.5)–(2.12), and
Panchenko–Talagrand, arXiv:math/0405357, conditions (1.2)–(1.4),
Theorem 4, Proposition 2 and Section 5. The general lower bound (2.11)
covers the bounded deterministic antiferromagnetic clause. Theorem 4
provides its upper bound after matching trial parameters. The matching
can be checked directly: a no-root h_0 hierarchy is a nested-measure
hierarchy with deterministic top measure; cascade recursion converts
expected logarithms to power means, which multiply for disjoint message
families. Hence the compound Poisson edge correction is d/2 times the
single-edge correction. Endpoints +/-1 can be handled by clipping.
This supplies the promised arXiv-only implication; details follow in PROOF.md.

The old conclusion holds as an application of the stated external theorem.
The proof manuscripts have not been audited in full. The regular branch
is still outside the scope established here. The requested stopping
condition applies to the Erdős–Rényi branch, as in the earlier report.
One log append failed because its patch context split a line incorrectly;
the successful append is this entry. No mathematical result was affected.

## 01:36–01:38 — proof written and adversarial checks

Wrote PROOF.md and read it back in full using `sed -n '1,300p' PROOF.md`.
The proof treats the stated external theorems as dependencies and does
not assert their full verification. Wrote SOLVED_ELSEWHERE.md and REPORT.md.

Independent checks of the new matching:

* At r=1 the top nested-measure law is the point mass at the distribution
  of artanh(h_0(U)), so no unwanted root randomness is introduced.
  At r=2 the first uniform selects the conditional law of the last
  field; independent children then draw from that law. The recursive
  construction handles all r by the same conditional independence.
* For two edge factors, already at one power mean,
  (E[(C_1 C_2)^m])^(1/m)=(E C_1^m)^(1/m)(E C_2^m)^(1/m).
  Repeating this identity at each conditional level verifies the general
  factorization. Physical counts must remain outside those averages.
* h_0=0 gives P=log(2)+(d/2)log((1+exp(beta))/2) in both representations:
  the site contribution is d log(a) and the edge correction is
  (d/2)log(a). This checks the site degree, edge density and sign.
  As beta goes to zero its derivative is d/4, the expected density
  of cut edges under independent fair spins (up to the vanishing loop
  correction in the Poisson finite graph). As beta goes to infinity
  this trial gives d/2, the trivial edge-count upper bound.
* The clipping coefficient is 2d a tau = d(exp(beta)-1), also obtained
  by differentiating log C with respect to each incoming mean and using
  C>=1. It is used only at fixed beta; no uniform beta claim is needed.
* Checked the dangerous endpoint cases h_0=+/-1, zero Poisson count,
  loops, repetitions, n>d in the Bernoulli coupling, and r=1. No omitted
  case was found. The d=0 formal check gives pressure log(2) and cut zero.

Independent checks of the old constants:

* Pair-rate counting gives d/n; summing distinct-pair and loop means
  returns dn/2. The integral identity in PROOF.md independently yields
  the same d^2(n-1)/(2n) edit bound as the earlier derivative argument.
* log Z=beta <Cut>+entropy with entropy between zero and n log(2)
  also gives the upper temperature error, since <Cut><=MaxCut;
  the largest summand supplies the lower bound.
* The Bernoulli variance bound can also be derived from martingale
  differences: reveal edges in order; each conditional effect is
  between zero and one, hence its conditional variance is at most
  p(1-p), and sum over binom(n,2) edges. This matches Efron–Stein.
* Cut=(M-sum sigma_u sigma_v)/2 confirms both temperature normalization
  and exact cancellation of a loop.

Outcome: earlier result holds; new contribution is a direct arXiv-only
scope deduction with explicit parameter matching. No further research
is undertaken under the literature stopping instruction. Fixed-degree
regular graphs and full proof validation remain outside this finding.

## 01:37:59 +04 — final readback

Read REPORT.md and SOLVED_ELSEWHERE.md in full and the final log entries
with `cat` and `tail -n`; checked the shell clock. The verdict, external
dependencies, scope limitation and next-worker instruction agree across
the files. PROOF.md had already been read in full. All deliverables are
inside this folder; the earlier folder was read only. Finished the
literature-stop branch and its independent recheck.
