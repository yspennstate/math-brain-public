# T223 working log

## 1. Orientation and literature check (2026-11-14)

Scope: all writes remain in this folder; no git or external publication. Read
`~\AGENTS.md`; the current task's explicit local-only instruction
overrides its general archival/upload instructions. Shell work uses
`OMP_NUM_THREADS=1` and BelowNormal priority; Python bytecode writing is disabled.

Web queries: `mean field ReLU Gaussian initialization Wasserstein gradient flow
convergence 2026 Chizat Bach global`; `2605.10775`; and queries combining
Wasserstein/ReLU convergence with October/November 2026. Opened:

- https://arxiv.org/abs/2603.01977 and
  https://arxiv.org/html/2603.01977v1
- https://arxiv.org/abs/2605.10775

Relevant finding: arXiv:2603.01977 (Lénaïc Chizat, Maria Colombo, Roberto Colombo,
Xavier Fernández-Real) proves a local polynomial convergence theorem for an
even, nonnegative spherical ReLU representation, with positive smooth target
density and a small initial discrepancy (Theorem 1.7). This is a restricted
advance, predating the supplied November baseline; it does not establish the
Gaussian/signed/finite-teacher statement. Theorem assumptions were read in the
paper, not inferred from its abstract. arXiv:2605.10775 was revised August 10,
2026 and remains a conditional global-optimality result. No post-baseline
solution has been identified in the searches so far.

Machine-wide rules read with `Get-Content ~\AGENTS.md`;
directory and memory orientation plus a batched math recall are in progress.

## 2. Concrete choice (before proof work)

Prove global well-posedness, exponential population-risk decay, and exponential
W2 convergence in input dimension one, for an explicit unbounded Gaussian
initialization conditioned to the invariant cone `|a| < |w|`. More generally,
derive the result for finite-second-moment initial laws supported in that cone
with mass in both signs of w. This is a special case, not a claim about a full
independent Gaussian in arbitrary dimension.

Why this piece: in one dimension every finite bias-free ReLU teacher is a pair
of half-line slopes. The cone prevents collisions with the ReLU kink. Each
half-line then has a hyperbolic characteristic flow and two closed moments.
This permits a proof for the parameter law itself, not merely its risk, with
all rates and normalization factors checkable independently.

## 3. Literature gate closed; algebraic reduction

The follow-up date-restricted searches (after 2026-11-01, before 2026-11-15,
and arXiv 2609/2610 wording) did not identify a solution of the stated problem.
The literature stage ended within the ten-minute cap. No SOLVED_ELSEWHERE.md
is warranted: the restricted March result predates the supplied baseline and
does not cover its initialization or target class.

For each sign sector, use `b=|w|`, `m=integral a*b`,
`q=integral (a^2+b^2)`, and target coefficient c. With
`R=E[(f-y)^2]/2`, Gaussian input gives
`R=sum (m-c)^2/4`. The characteristic equations yield
`m'=-(m-c)q/2`, `q'=-2(m-c)m`, hence
`D^2=q^2-4m^2` is constant. The strict cone gives D>0 in each
nonempty sector. Therefore risk decays at least as exp(-min(D)t).
The integrated residual is a convergent hyperbolic clock, which also gives an
explicit transport coupling to the limiting parameter law.

For an independent standard Gaussian conditioned on `|A|<|W|`, radial/angular
independence predicts `m_+=m_-=0`, `q_+=q_-=1`, and hence `D_+=D_-=1`.
These constants will be independently checked by Cartesian integration.

Read-only recall commands (OMP_NUM_THREADS=1, BelowNormal priority):
`python ~\.claude\dreaming\math_recall.py 'T223 mean field convergence' --or 'ReLU balanced invariant cone Wasserstein gradient flow' --or 'Gaussian initialization population risk gradient flow' > math_recall.txt`.
The initial batched recall also used the three phrasings recorded in the tool
transcript; it completed, but the combined console output was truncated.
The saved recall output is the durable record used for inspection.

Recall returned the balancedness invariant and the conditional-convergence
warning. Following its links, the cards `claim_ce04026e`, `claim_5c67a07a`, and
`claim_16839d4f` were requested in full and saved to `recalled_cards.txt`.
The general mistakes recall is saved to `recalled_mistakes.txt`.

Scope correction: inspecting math_recall.py revealed that its nominally
read-only store access can still append a co-use log outside this folder.
The first calls used its default settings before this was discovered. They
may therefore have made that incidental write; no attempt was made to edit
or undo anything outside this folder. Subsequent calls set
`MATH_STRENGTH_NOLOG=1` and `PYTHONDONTWRITEBYTECODE=1`.

## 4. Proof saved and first independent verification

Saved PROOF.md. It proves the result for arbitrary finite-second-moment laws
in the strict cone with positive mass in each sign sector, and specializes to
the explicitly conditioned Gaussian. It includes a transport Taylor estimate
across the kink, verifying the metric energy dissipation identity rather than
just assuming that a characteristic ODE is a metric gradient flow. Uniqueness
is stated precisely for self-consistent characteristic solutions.

Saved verify.py, a standard-library-only audit (no network training). Exact
fraction arithmetic checks the hyperbolic formulas, individual balancedness,
moment invariant, both moment derivatives and energy dissipation on a rational
ensemble. Cartesian truncated-normal integrals and a separate radial/polar
integral independently check the Gaussian constants. A deterministic clock
grid checks the root formula and the L2 transport estimate.

Exact PowerShell command, from this folder:

```powershell
$env:OMP_NUM_THREADS='1'; $env:PYTHONDONTWRITEBYTECODE='1'; [System.Diagnostics.Process]::GetCurrentProcess().PriorityClass='BelowNormal'; python .\verify.py
```

Output:

```text
PASS: 22 identity/quadrature/adversarial checks.
Cartesian conditioned-sector q = 0.999999999998895
Polar conditioned-sector q = 0.999999999999349
Maximum root residual = 1.77636e-15
Maximum positive coupling-bound excess = 0
Outside-cone kink: u = -0.549306144334055, a = 1.73205080756888
Data: verification.json
```

Data are in verification.json; the complete short output is also saved as
verification_output.txt. Finite differences additionally check M'(u)=q(u)
on 205 clock/target combinations. These numerical checks supplement the
analytic proof and are not used as proof of universal inequalities.

Adversarial checks: (a,b)=(2,1) hits b=0 at u=-atanh(1/2), with a=sqrt(3),
so unconditioned Gaussian initializations cannot inherit the sector closure.
At the balanced boundary a=-b, c>0, a single-neuron flow remains wrong-signed
and approaches risk c^2/4; thus nonempty sectors alone, without D>0, do not
give the theorem. The proof also separately handles zero residual/zero clock,
signed target coefficients, no uniform cone margin, and unbounded support.

## 5. Adversarial reread and final artifacts

Saved AUDIT.md and REPORT.md. Strengthened the characteristic uniqueness
argument by proving moment continuity under W2 and excluding kink contact
for each individual neuron, rather than assuming a common population-wide
first-contact time. The metric-slope Taylor remainder is bounded by
`(3/2)|displacement|^2` per feature even across the kink, using the cone.

Whole-card recall has been inspected. Its old finite-particle T223 numerical
card says that a=0 particles are frozen, which the current equations directly
contradict when b>0 and residual is nonzero. That assertion, the finite-width
simulation, and its power-law fit were not used. General mistakes recall
returned low-separation leads; it supplied no applicable convergence theorem.

Added resource instrumentation to verify.py to resolve the remaining compute
audit: on Windows it reads and asserts BelowNormal process priority and peak
working-set/commit below 1 GB, and records them in verification.json. The
same exact verification command is rerun once for this instrumentation.

The instrumented rerun exited 0 and again printed the identical 22-check PASS
output above. Both peak-memory assertions and the actual process-priority
assertion passed. The final resource measurements are in verification.json.
All universal statements in the report refer to the strict-cone,
one-dimensional theorem, with its characteristic uniqueness qualification;
none assert a solution of the original general Gaussian problem.

Final file/readback check confirmed REPORT.md begins with its required
VERDICT line and all deliverables exist. Instrumented Python run: 0.0267 s
inside the audit script, peak working set 25,628,672 bytes, peak commit
16,777,216 bytes, actual BelowNormal priority, OMP_NUM_THREADS=1.
No further mathematical changes or repeated verification were needed.
