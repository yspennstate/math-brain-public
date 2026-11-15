# T076 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
Received 15 November 2026, approximately 04:39 Asia/Tbilisi (00:39 UTC).

## Orientation and literature check, 00:39–00:43 UTC

Read REPORT.md and LOG.md in both earlier folders, the round-3 PROOF.md,
and the first folder's SOLVED_ELSEWHERE.md. `rg --files` confirms that
neither folder contains computational scripts; the first has no PROOF.md.
Both folders are read-only for this task. Read the startup memory index,
its note on macOS nice errors, and the compute governor state. The governor
reports warn / owner_away_open / cpu_saturated. No heavy computation planned.
The instruction to write only in this folder precludes mesh, checklist,
brain-recall logs, and memory writes outside it. No git and no subagents.

Document reads used `OMP_NUM_THREADS=1 nice -n 15 /bin/cat ...` and
`OMP_NUM_THREADS=1 nice -n 15 rg --files ...`. The sandbox prints
`nice: setpriority: Operation not permitted` and executes these document
reads anyway. No numerical program will be run under unverified priority.
The work below is analytic.

Web search queries (under five minutes total):
- `"2609.24426" random band matrices`
- `random band matrices two three dimensions localization November 2026 polylogarithmic bandwidth`
- `"random band matrices" "three" "2026" bounded bandwidth delocalization`
- `"random band matrices" "two-dimensional" "November" "2026"`

Opened https://arxiv.org/abs/2609.24426 and
https://arxiv.org/html/2609.24426v4 (Xujie Lai and Fan Yang,
Localization Lengths for Two-Dimensional Random Band Matrices: Exponential
Lower Bounds). Latest listed version is v4, 8 November 2026.
Opened https://arxiv.org/abs/2507.20274 (Sofiia Dubova, Fan Yang,
Horng-Tzer Yau, Jun Yin, Delocalization of Non-Mean-Field Random Matrices
in Dimensions d>=3): its abstract still assumes W>=N^c.
One search hit, https://papex.org/ai-claims, was inspected to disambiguate
an apparent new band-matrix claim; the cited crossover claims concern
dimension one. No solution to T076 found. This is a bounded search.

## Independent check of the earlier main claim

The round-3 estimate holds. A second integral comparison uses physical
Fourier cells rather than integer-lattice cells. Write q=2*pi*k/M,
a(q)=(2/5)(2-cos q1-cos q2), h=2*pi/M. For t=1-mu>=1/2,
the reciprocal of mu+t*a(q) differs from that of mu+|q|^2/5 by O(1)
uniformly on the Fourier square. On a nonzero cell at radius r>=h,
the quadrature error is bounded by its area times C*h/r^3.
After the (2*pi)^(-2) normalization, summing annuli gives
C*h*integral_h^1 r^(-2) dr=O(1). The finitely many nearest cells
also cost O(1), because the zero cell is removed. Replacing the remaining
square by an annulus h<=|q|<=1 costs O(1). Its integral is

    (2*pi)^(-2) * 2*pi * integral_h^1 r/(mu+r^2/5) dr
      = (5/(4*pi))*log((mu+1/5)/(mu+h^2/5)).

For the finitely many small M for which h>1, the whole nonzero sum and
the claimed logarithm are bounded, so they are included by enlarging
the error constant. Thus R_M(mu)=(5/(4*pi))*log(1/(mu+M^(-2)))+O(1).
An independent check from covariance diag(2/5,2/5) gives Gaussian return
density 5/(4*pi*n), agreeing with the coefficient. The exact M=3
values 10/9 at zero mass and 95/99 at mu=1/2 also recheck correctly.
The constant mode is exactly 1/(mu*M^2). No earlier error found.

## Choice recorded before extension, approximately 00:43 UTC

One piece: test the quadratic error W^2 D B D from Lai–Yang (2.33)–(2.34)
with its exact Duhamel propagator U_(u,t)=(I-uB)(I-tB)^(-1).
Take the centered, positive semidefinite comparison family

    D(u)=delta*W^(-2)*(I-uB)^(-1)*(I-P).

It satisfies the strongest natural relative Loewner envelope, has zero
row sums, and has uniformly small entries when log(M)/W^2 is small.
Compute its integrated quadratic contribution exactly, then determine
its diagonal asymptotic down to mu=1-t<=M^(-4). This directly tests
whether centering and the previous diagonal estimate alone can control
that term. It does not assume this artificial family is a random
resolvent error, and cannot disprove a theorem about that random error.

Anticipated identity:

    integral_0^t U_(u,t) [W^2 D(u) B D(u)] U_(u,t) du
      = delta^2*W^(-2)*t*B*(I-tB)^(-2)*(I-P).

The issue to resolve is its low-frequency square, not another estimate
of the already known single return kernel. Proof and independent audits
will be saved in PROOF.md.

## Refinement before proof

Impose D(0)=0 as well: use D(u)=delta*u*W^(-2)*G_u*(I-P).
The exact integral then has coefficient t^3/3, replacing t above.
Its failure suggests a precise stronger hypothesis to test in the same
quadratic-drift calculation: in the commuting Fourier case, require

    |d_u(k)| <= delta*u*W^(-2)*a_k/(1-u*b_k)^2, k!=0,
    a_k=1-b_k, d_u(0)=0.

This has a factor a_k/(1-u*b_k), which suppresses a low mode before
its diffusive time. The identity integral_0^t (1-u*b)^(-2) du
=t/(1-t*b) suggests a log-free relative bound for its quadratic
Duhamel term. The chosen piece remains the single quadratic drift:
prove this sufficient spectral condition and test necessity by the
weaker-envelope family. No condition on the actual random error is
being claimed. The weak family need not make K+D entrywise nonnegative;
this limitation must be explicit in the final audit.

## Proof saved, 00:45 UTC

Created PROOF.md. For real symmetric translation-invariant errors with
Fourier coefficients satisfying

    |d_u(k)| <= delta*u*W^(-2)*a_k/(1-u*b_k)^2, d_u(0)=0,

the integrated quadratic drift J_t satisfies the operator inequalities

    -delta^2*t*W^(-2)*G_t*Q <= J_t <= delta^2*t*W^(-2)*G_t*Q.

Every entry is consequently at most delta^2*t*W^(-2)*r_M(t) in absolute
value: one return-kernel logarithm, with no further time logarithm.
Key exact antiderivative: integral_0^t (1-u*b)^(-2) du=t/(1-t*b).
This avoids dividing by b and covers negative and zero eigenvalues.

For the weaker family D(u)=delta*u*W^(-2)*G_u*Q, the exact drift is
delta^2*t^3/(3W^2)*B*G_t^2*Q. At 0<1-t<=M^(-4), its diagonal is

    delta^2/W^2 * [c_* M^2 + O(log M)],
    c_* = 25/(48*pi^4) * sum_(k in Z^2, k!=0) |k|^(-4).

The coefficient comes from the reciprocal-square Fourier symbol; the
tail of the infinite lattice sum costs O(1), the symbol replacement
O(log M), and the positive mass cutoff O(1). Its explicit bounds are
125/(48*pi^4) < c_* <= 175/(48*pi^4). No numerical experiment used.

## Adversarial checks

The coefficient is also recovered by the real-space identity
(B*G_1^2*Q)_00=sum_x (H_1)_0x^2-r_M(1), followed by Parseval.
Differentiating the inverse matrix gives the separate exact check
J_t,00=delta^2*t^3/(3W^2)*d_t r_M(t). No derivative of an O(1)
remainder is taken. For M=3, direct enumeration gives
(B*G_1^2*Q)_00=35/81; the square norm minus return diagonal gives
125/81-10/9=35/81. Hence J_1,00=35*delta^2/(243*W^2).

The sufficient envelope's logarithmic order is sharp in its class:
the saturating family delta*u*W^(-2)*A*G_u^2*Q has, at t=1 on Q,
low-mode drift asymptotic delta^2/(W^2*a_k). Direct substitution
v=1-u*b gives the same scale as the bound's elementary antiderivative.
A lower bound on u in [1-a_k,1] is 27*delta^2/(256*W^2*a_k).
Summing small positive modes yields order log(M)/W^2; the total
negative-mode diagonal contribution is only O(W^(-2)).

Attempt to break the obstruction: although the weak family is centered,
PSD, smooth and starts at zero, K+D need not be entrywise nonnegative.
For distinct nonneighbors, its derivative at zero is
-delta/(W^2*M^2). Thus it is not a counterexample to an estimate using
all the constraints of an actual two-loop observable. This limitation
is explicit. It is a counterexample only to sufficiency of the stated
relative centered-kernel envelope and small-entry conditions. Under
M=floor(exp W), all its error entries tend to zero uniformly in time,
but its integrated quadratic diagonal diverges.

No estimate of the sufficient envelope for a random resolvent error,
or extension to noncommuting errors, has been established. These are
the remaining obstacles, and no new T076 bandwidth threshold is claimed.

## Final readback, 00:46–00:47 UTC

Read PROOF.md and REPORT.md in full using
`OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1
nice -n 15 /bin/cat PROOF.md REPORT.md`. The same priority warning
appeared; this was document inspection only. Corrected display-math
delimiters, then counted 39 opening and 39 closing display delimiters
and 29 numbered equations across the two documents. Made q_k explicit
where the sharpness argument uses it. Rechecked the exact 1/3 time
factor, W^(-2) normalization, cutoff error C*mu*M^4, positivity and
sign issues, and the distinction between the conditional lemma and
the unproved stochastic input. REPORT.md has the required PARTIAL
first line, failed inference, scope, commands and next-worker action.
The three deliverables are complete and remain within this folder.
