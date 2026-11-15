# T076 work log

Task received: 15 November 2026, approximately 01:12 Asia/Tbilisi (14 November 21:12 UTC).
Request: “take the NEXT checkable step on this problem, building on that work.”

## Orientation and earlier files, 21:12–21:14 UTC

Read the previous REPORT.md, LOG.md, SOLVED_ELSEWHERE.md, and directory listing
at ~/codex_op_1114/briefs/T076. There is no previous PROOF.md
or computational script. The previous result is a literature correction and
an algebraic conversion of scales, not a new delocalization proof.

Commands: `pwd`; `rg --files ...`; `cat` on the listed files, the startup memory,
the mesh protocol, and the compute governor state. The governor says `warn`,
`owner_away_open`, CPU saturated. No heavy computation is planned.
The task's restriction to writes in this folder takes precedence over global
mesh, checklist, recall-log, and brain-write instructions. Those external
databases will not be changed. No git commands and no subagents.

## Literature check begun, 21:13 UTC

Web queries:
- `"Lai" "Yang" "2609.24426"`
- `random band matrices delocalization two three dimensions November 2026 polylogarithmic bandwidth`

Opened https://arxiv.org/abs/2609.24426. Latest revision remains v4,
8 November 2026, by Xujie Lai and Fan Yang. The abstract agrees with the
earlier report. No later solution appeared in these queries. Full theorem
and one targeted follow-up check remain within the five-minute budget.

## Literature check completed and earlier result rechecked, 21:14 UTC

Follow-up queries:
- `"random band" "2026" "bounded" "bandwidth" "three"`
- `"random band matrices" "November" "2026" localization`

Opened the v4 HTML and PDF of https://arxiv.org/abs/2609.24426,
and https://arxiv.org/abs/2507.20274. The latter still states a power-law
bandwidth assumption in dimensions at least three. No later solution to T076
was found. Search completed in under five minutes; this is a bounded search,
not a proof that no other paper exists.

The earlier theorem transcription holds: Theorem 1.2 of Xujie Lai and Fan Yang,
*Localization Lengths for Two-Dimensional Random Band Matrices: Exponential
Lower Bounds*, v4 (8 November 2026), has fixed A>1, C>A+100,
(10+log N)^A <= W <= (10+log N)^C and squared sup-norm bound
(log W)^10(10+log N)^2/N for all bulk eigenvectors. Equation (1.5) is
the Gaussian periodic five-block variance profile. PDF printed page 4
independently agrees with HTML. This checks the statement, not its full proof.

Independent re-derivation of the scale conversion: fix 0<delta<1 and choose
A=1/(1-delta). Put N approximately exp(c W^(1-delta)), 0<c<1,
rounding the block side M to an integer and taking N=(WM)^2.
Then (10+log N)^A/W tends to c^A<1, while
W/(10+log N)^C tends to zero for any C>A+100. Both hypotheses hold.
The physical side WM consequently has logarithm
(c/2)W^(1-delta)+o(W^(1-delta)). Conversely the lower bandwidth assumption
implies log N <= W^(1/A)-10. The earlier exponent and side/volume conversion
are correct. No universality or infinite-volume assertion follows from this algebra.

## Choice recorded before proof, 21:14 UTC

One piece: prove the exact logarithmic coefficient, with a uniform finite-size
cutoff and the constant Fourier mode separated, for the deterministic return
propagator of the same two-dimensional five-block profile. More precisely,
for B=(I+nearest-neighbor adjacency)/5 on the M by M block torus and
mu=1-t in (0,1/2], establish

    [(I-tB)^(-1)]_00 - 1/(mu M^2)
      = (5/(4*pi)) log(1/(mu+M^(-2))) + O(1),

uniformly in M>=3 and mu. The physical-site nonconstant-mode contribution
has a further factor W^(-2). This isolates the logarithmic accumulation
relevant to the proposed exp(cW^2) scale. It is a deterministic sublemma,
not an improvement of the known random-matrix bandwidth threshold, and
no claim of novelty in random-walk theory is intended.

The proof will compare the exact Fourier symbol to its quadratic part,
then compare the nonzero lattice sum to an explicit radial integral.
Audit: independently recover the coefficient from the infinite-lattice
return probability and examine zero-mode dominance, parity, and negative
Fourier eigenvalues. Save the detailed proof in PROOF.md.

A priority probe, `OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 /usr/bin/true`,
printed `nice: setpriority: Operation not permitted` (exit 0).
No numerical program will run without the required priority. The result
will be analytic; no computational output is used as evidence.

## Proof saved, 21:17 UTC

Created PROOF.md with a complete analytic proof of the selected lemma.
No numerical computation or script is used. The exact Fourier eigenvalue is

    b(q) = (1+2 cos q_1+2 cos q_2)/5,
    1-b(q) = |q|^2/5 + O(|q|^4).

The nonzero-mode sum differs by O(1), uniformly, from

    sum_{k != 0} 1/(mu M^2+(4*pi^2/5)|k|^2).

Unit-cell comparison has summable errors O(|k|^(-3)); the resulting annular
integral has coefficient pi/(4*pi^2/5)=5/(4*pi). The uniform result is

    R_M(mu) = (5/(4*pi)) log(1/(mu+M^(-2))) + O(1).

The mean mode contributes exactly 1/(mu M^2). Multiplication by W^(-2)
gives the normalized propagator; in the regime mu <= M^(-2), its centered
diagonal is (5/(2*pi))log M/W^2+O(W^(-2)).

Independent coefficient derivation saved in the same proof: Fourier inversion
for the infinite-lattice return probability gives
n p_n(0) -> (2*pi)^(-2) integral exp(-|u|^2/5) du = 5/(4*pi).
Summing t^n/n recovers (5/(4*pi))log(1/(1-t)). This checks the coefficient
by the long-time return probability rather than by the resolvent lattice sum.
The one-step covariance is diag(2/5,2/5), which agrees with diffusion 1/5.

The lemma sharpens the diagonal information relative to the previous session,
which proved no deterministic estimate. The logarithmic order itself is
standard and is already bounded in Lai–Yang, Lemma 2.7. This is not a new
random-matrix delocalization theorem or a claim of novelty in random walks.

## Adversarial audit and report, 21:18 UTC

Read back the full PROOF.md and LOG.md using `cat`. Rechecked the factors
M^(-2), W^(-2), 2*pi, and the factor of two between log mass and log side.
All load-bearing coefficients have two derivations in PROOF.md.

Additional exact checks, done algebraically without a program:
- M=3 has eigenvalues 1 (once), 2/5 (four times), -1/5 (four times).
  Hence R_3(0)=(4/9)(5/3+5/6)=10/9 and R_3(1/2)=95/99.
- For even M the most negative eigenvalue is -3/5, whose inverse denominator
  is 1+3t/5>=1. It cannot introduce an overlooked low-mass singularity.
- The representative-cell rectangle contains the disk of radius M/4 and
  lies inside the disk of radius M for every M>=3, including odd M.
  M=1,2 are excluded because their neighbor convention changes.
- For S=B tensor J, summing only n>=1 gives
  tS(I-tS)^(-1)=(G_mu-I) tensor J. Subtracting its global constant mode
  leaves W^(-2)[R_M(mu)-1+M^(-2)], checking the site normalization separately.
- A counterexample to omitting the constant mode is M=floor(exp(W)),
  mu=N^(-1): log M/W^2 tends to zero but 1/(mu N)=1. The full normalized
  diagonal tends to one. This failed inference is explicitly excluded.

Saved REPORT.md with a PARTIAL verdict. The uncertainty is the stochastic
resolvent comparison, not the deterministic Fourier calculation; no attempt
to close that comparison is claimed. The proposed next step is one
time-integrated quadratic drift estimate from equations (2.33)–(2.34),
with the constant mode handled separately. All files written are in this folder.

Final readback: `OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
VECLIB_MAXIMUM_THREADS=1 nice -n 15 cat REPORT.md` returned the complete
report, with the same sandbox priority warning. Verified the required
first-line verdict, scope, links, and next action. No additional calculation ran.
