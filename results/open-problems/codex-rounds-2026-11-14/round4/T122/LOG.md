# T122 work log

Task received 2026-11-15, approximately 04:55 +04 (Asia/Tbilisi).

## Opening: prior work and bounded literature check

Read both earlier REPORT.md and LOG.md files, round 3 PROOF.md, and both
SOLVED_ELSEWHERE.md files. File inventories show that the original folder
has no PROOF.md and neither folder contains a research script. Neither
earlier folder was edited. Read the startup memory index and compute
snapshot: status warn, mode owner_away_open, CPU saturated. No research
computation has run. The folder-only rule supersedes shared-state logging;
no mesh, checklist, brain logging, git, or subagent commands are used.

Read-only commands: pwd, rg --files, cat, sed -n, ls, date. One initial
directory listing was unnecessarily broad and its output was truncated;
subsequent reads were targeted.

Web searches: "2610.39545" Panchenko diluted; random regular max cut
Parisi formula November 2026 cavity; "random regular" "Mézard"
"formula" "2026" max cut exact; "2610.39545" correction regular
antiferromagnet. Opened Dmitry Panchenko, The Mézard-Parisi formula,
arXiv:2610.39545v1 (abstract and full HTML), and Viktor Harangi,
RSB bounds on the maximum cut, arXiv:2506.21296 (abstract).
The arXiv history still lists only v1 for Panchenko. The search found
no post-report solution for regular graphs. The known Poisson result
was already the result of both earlier sessions; repeating that finding
alone would not extend their work.

Preliminary independent check: exp(beta(1-st)/2) equals
((1+exp(beta))/2)(1-tanh(beta/2) st) at both st=1 and st=-1.
The clause is bounded and permutation invariant; its negative coefficient
has nonnegative alternating moments. The finite-volume entropy bound is
MaxCut <= log Z/beta <= MaxCut+n log(2)/beta. The claimed Poisson-to-simple
pair multiplicity rate d/n follows directly from Poisson thinning.
The substantive matching of trial spaces is being checked against the
opened primary theorem before recording a final verdict on the earlier
deduction.

## 04:56 — recheck and choice

Opened Dmitry Panchenko and Michel Talagrand, Bounds for diluted mean-fields
spin glass models, arXiv:math/0405357, equations (1.2)–(1.4), Theorem 4,
and Proposition 2. The conditions admit deterministic f(s)=s and
b=-tanh(beta/2). Checked the hierarchical field conversion independently:
each prefix determines a law of the remaining conditional laws; a
deterministic top law gives exactly the no-root message array. Iterated
conditional power means multiply for independent edge-coordinate families.
Thus the compound-Poisson edge correction is d/2 times the single-edge
correction. Clipping changes a log edge weight by at most
2a*tau*delta, and a log site weight by at most K_s*a*tau*delta;
the total bound is d(exp(beta)-1)delta. The earlier main corollary holds
conditional on the stated external theorems. Their full proofs are not
independently verified here.

Choice of ONE extension: specialize the general random-regular variational
principle of Amin Coja-Oghlan and Will Perkins, Spin systems on Bethe
lattices, arXiv:1808.03440, to the deterministic Ising antiferromagnet.
Derive its exact zero-temperature implication and identify precisely the
additional restriction needed to obtain a finite-hierarchy cavity formula.
This follows the round 3 next-worker recommendation and targets the
uncovered ensemble. Primary abstract and full HTML have been opened.
This is a scope deduction from an existing theorem, not a claim to prove
the missing hierarchical representation.

## 04:57 — regular formula and an adversarial sign check

Recent-literature searching is finished within five minutes. Subsequent
web calls read the already identified primary papers, not a continuing
search. Read Coja-Oghlan–Perkins Sections 2.1, 2.3, 2.4 and 7.2:
Theorem 2.7 minimizes over all cavity-reweighting-invariant kernel laws;
Section 2.5 explicitly leaves the hierarchical structure unresolved.
This does not satisfy T122's full-cavity stopping condition.

Important transcription issue: the HTML Potts specialization displays
a PLUS d/2 log(edge factor), whereas general equation (2.12) has MINUS.
Use the general equation, not that displayed specialization. With the
zero kernel, the two expressions would have derivatives -3d/4 and
-d/4 respectively (after removing the spin-count constant); direct
differentiation of the finite-graph partition function gives -d/4.
The general theorem's minus sign passes. This concerns the opened
HTML display; no claim about a different published version is made.

Derived the binary scalar-kernel functional directly from (2.12),
with uniform spin prior. An independent edge scaling check yields
Z_cut=2^n exp(beta*d*n/2) Z_normalized_antiferromagnet. Hence the
regular max-cut density is d/2+lim Phi(beta)/beta, with a one-sided
error at most log(2)/beta when the normalized Phi is used.
The invariant trial space depends on beta; no temperature-limit and
infimum exchange is justified.

To enforce strictly subunit positive weights in the general model's
definition, use psi/2. Its POS condition follows by expanding
(1/2+(1-exp(-beta))*q/2)^ell: every term is an integral of a square.
This scaling shifts the pressure by -(d/2)log(2), leaves the invariant
class unchanged, and cancels from the final expression. Details are
being written in PROOF.md. No computation or numerical optimization.

## Proof saved — explicit regular-ensemble reduction

Wrote PROOF.md. It defines the beta-dependent invariant law space,
proves POS directly for strictly subunit edge weights, and derives the
scalar functional from general equation (2.12). In addition to the
pressure/beta error, it proves the explicit finite-difference estimate

  0 <= c_d - [d/2 + (Phi(beta+L)-Phi(beta))/L]
       <= (log(2)/L) log(1+L/beta) <= log(2)/beta.

This makes the temperature step quantitative without differentiating
the limiting pressure or identifying its minimizing kernels. It is an
elementary corollary of the finite-graph Gibbs entropy bound and the
existing regular variational theorem, not a new solution of the
hierarchical problem. The proof includes a direct matching-exposure
concentration argument and explains the exact remaining trial-space
comparison. No research program was run; no script is needed for this
analytic result. Next: full readback and adversarial audit.

## 05:01–05:03 — readback and attempts to break the result

Read PROOF.md in full with cat and read REPORT.md and the updated proof
tail with sed -n. Corrected a formatting artifact in a later proof patch.
No mathematical change was needed after this readback.

Additional independent checks:

* Rechecked the earlier edit constant: for x=d/n, per-pair expected
  parallel deletions and Bernoulli additions each equal x-1+exp(-x).
  This is at most x^2/2, by integrating 1-exp(-u)<=u. Multiplication
  by twice binom(n,2) gives d^2(n-1)/(2n). Alternatively, deletion
  loss is at most E[C(C-1)]/2=x^2/2, and the Bernoulli addition bound
  follows from exp(-x)<=1-x+x^2/2. Both routes give the same constant.
* Scaling each edge weight by kappa shifts finite-graph pressure by
  (d/2)log(kappa). The general minus-sign functional has this exact
  scaling; the displayed plus-sign specialization would have three
  times that shift. This check does not assume that the zero kernel
  minimizes anything.
* Re-derived POS with scalar overlap moments: every moment difference
  becomes the integral of the square of a difference of column-product
  averages. The binomial coefficients remain nonnegative, including
  after strict-subunit scaling.
* Re-derived the temperature bound without Gibbs entropy: the convex
  gap log-partition g has g(0)=n log(2), g>=0 and tangent slope
  g'(beta)>=(g(beta)-g(0))/beta. Integrating -g'<=n log(2)/beta
  reproduces the logarithmic finite-difference error.
* Rechecked the Azuma constant: dn/2 revelations, each with increment
  at most 2, give sum of squared bounds 2dn and denominator 4dn.
  Conditional partner choices couple by one switch of two pairs.
* Checked beta>0 (not beta=0 in a denominator), L>0, N=M=0,
  endpoint message values +/-1, constant kernels, odd d with n even,
  loops and parallel edges in the pairing ensemble, and conditioning
  on simplicity. Fixed-beta positivity makes all tilt denominators
  nonzero. All temperature errors have the stated lower-estimate sign.

The finite-hierarchy regular expression has been written explicitly,
with deterministic degree d. Its comparison with the invariant-law
minimum is NOT proved. In particular, invariance of arbitrary cascade
trials was not assumed. The external theorem's full proof remains an
external dependency. Report saved with a PARTIAL verdict. No research
program, simulation, optimization, git, external write, or subagent was used.

Final clock from date: 2026-11-15 05:02:44 +04. Read back the report's
verdict and the proof's equation labels; the three deliverables agree on
the scope and remaining gap. All authored files are inside this folder.
