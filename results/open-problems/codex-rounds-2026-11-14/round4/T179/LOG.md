# T179 session log

Task: “take the NEXT checkable step on this problem, building on that work.”
Received 15 November 2026, approximately 04:59 Asia/Tbilisi.

## Orientation and brief literature check, 04:59–05:02 +04

All writes are restricted to this folder; earlier folders remain read-only.
No git, subagents, external messages, or external mesh/checklist/brain writes.
Read startup memory index and brain navigation index. The compute governor
reports warn/owner_away_open with CPU saturation; no heavy computation is
planned. Any diagnostic will use one thread, nice >=15, and <1 GiB RAM.

Read both prior REPORT.md and LOG.md files and began reading both complete
PROOF.md files and scripts. Web queries: '2611.07310 stochastic heat
uniqueness', 'Yi Han full Hölder uniqueness heat equation', '2608.01279'.
Opened official https://arxiv.org/abs/2611.07310 and full text
https://arxiv.org/html/2611.07310v1. Official page still shows the version
submitted 5 November 2026. Proposition 8.1 treats unbounded diffusion only
from bounded initial states; Proposition 8.5 is an L2-state Girsanov transfer
conditional on drift-free well-posedness. No later paper changing this
residual corner was found in the brief search. This is the same external
full-positive-Hölder result already recorded by both prior workers, not a
new resolution of the rough-data extension. Literature status check ended
within five minutes. No new SOLVED_ELSEWHERE.md is called for on that basis.

Next: independently check the round-3 ordered approximation and martingale
identification. If valid, select exactly one extension and record it before
beginning its proof.

## Independent audit of the earlier result

Read both complete proofs and both scripts. Independently re-derived the
round-3 main claim rather than relying on its arithmetic diagnostic.
For smooth Lipschitz approximants sigma_n and the common-noise solutions
from v min w and v max w, their gap D_n is nonnegative by scalar comparison.
Testing against 1 gives E integral D_n = integral(max(v,w)-min(v,w))
= ||v-w||_1. The two inner solutions differ pointwise by at most D_n.
This gives the contraction with constant one. Constant diffusion and a
constant displacement attain this constant, so the sign and factor check.

Checked the comparison proof independently: for spatially smoothed input
noise, the trace term for ||(A-B)^+||_2^2 is bounded by
Lip(sigma_n)^2 p_(2epsilon)(0)||(A-B)^+||_2^2. Gronwall gives order for
each epsilon; the closed positive cone and L2 convergence at fixed times
pass order to white noise. No uniform derivative bound is used.

Checked identification separately. Uniform-H path convergence implies
||g_n(X_n)-g(X)||_2 <= L n^(-beta)+L||X_n-X||_2^beta ->0.
The square difference converges in L1 by factoring a^2-b^2; uniform path
moments give uniform integrability for the martingale and product identities.
This identifies each marginal, without requiring a unique coupled limit.
The factorization exponents 2eta+(1+beta)/2<1 and eta>3/(2p) are compatible
for every beta<1. The exact L1 estimate then closes rough-start uniqueness
on Fourier characteristic tests with error O(delta^(1/4)). Its validity
depends on Han's bounded-start uniqueness input, as the prior proof states.
No error found in the earlier main result. This audit does not verify the
full-positive-Hölder theorem's main finite-expansion argument.

## Chosen extension, recorded before its proof

Prove weak existence and uniqueness with Borel drift b(t,x,z) satisfying
|b(t,x,z)| <= B_T(1+|z|), for every deterministic L2 initial state and
unbounded elliptic globally beta-Hölder g. Also identify the two path laws
by a canonical density and prove finite relative entropy in both directions.
The drift extension is the single new piece; the entropy identity is an
audit of its density and integrability, not a second research direction.

Reason: the round-3 result supplies exactly the input missing in Han's
Proposition 8.5. That proposition and Section 8.2 were opened in full.
The transfer method is already in Han; the new scope is the combination
of unbounded diffusion, arbitrary L2 initial state, and measurable drift.
A complete derivation here will check the stopped-density moment bound,
the signs of both measure changes, and why state-law uniqueness suffices
without assuming uniqueness of the joint state-noise law.

## Re-run of prior arithmetic diagnostic

Command:
`env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 ~/codex_op_1114r3/briefs/T179/check_estimates.py`
Output follows (read-only script; bytecode disabled):
nice: setpriority: Operation not permitted
beta=1/100; eta=99/800; p=14; inner=301/400; outer_gap=93/5600
beta=1/2; eta=1/16; p=26; inner=7/8; outer_gap=1/208
beta=2/3; eta=1/24; p=38; inner=11/12; outer_gap=1/456
beta=3/4; eta=1/32; p=50; inner=15/16; outer_gap=1/800
beta=99/100; eta=1/800; p=1202; inner=399/400; outer_gap=1/480800
beta=999/1000; eta=1/8000; p=12002; inner=3999/4000; outer_gap=1/48008000
three crossing/signed envelope-mass identities: exact
three unit-L2 spike identities with growing supremum: exact
restart exponents: H modulus 1/8; L1 tests 1/4
nice=20; peak RSS=12.84 MiB

## Proof saved

Wrote PROOF.md with the drift extension, a uniform second-moment estimate
valid for all predictable drift multipliers in [0,1], normalization of the
forward and reverse densities, and a Borel density defined from canonical
state martingales. The final formula determines arbitrary drifted state
laws using only drift-free state-law uniqueness. The two entropy identities
follow from the same density and second moments. Explicit constants in
(7) make the Volterra absorption and energy bound checkable.

The first prior diagnostic re-run exited 0; its complete output is above.
Next audit: re-derive the heat coefficient and Volterra parameters, test
both signs of g and b, check rough initial examples, and check that the
weighted predictable approximation really uses the state law alone.

## Independent diagnostics of the new proof

Created check_transfer.py, using only scalar standard-library arithmetic.
It independently simplifies lambda to 1+24(T B^2+G^2)+72 G^4,
checks absorption over rational parameter triples, compares Fourier and
Gaussian-image heat traces, and checks Gaussian tilt normalization,
inverse-density signs, shifted mass mean and both entropy coefficients.
It includes both signs of the diffusion constant, both signs of drift,
zero drift, and rough-start integrability near its excluded endpoint.
These are diagnostics of constants and identities, not tests of SPDE
uniqueness or of the external Han theorem.

Command:
`env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 check_transfer.py`
Output:
nice: setpriority: Operation not permitted
Volterra absorption: 27 exact parameter triples passed
lambda = 1 + 24(T B^2 + G^2) + 72 G^4
each Laplace-kernel term <= 1/4; total <= 1/2
r=1e-06; heat trace=199.471140201; upper=200.471140201; expansion gap=2.84e-14
r=0.0001; heat trace=19.9471140201; upper=20.9471140201; expansion gap=0
r=0.01; heat trace=1.9947262692; upper=2.99471140201; expansion gap=0
r=1; heat trace=1; upper=1.1994711402; expansion gap=2.22e-16
Gaussian density, inverse signs, both entropies: 24 exact cases
sigma of either sign; positive, zero, negative drift included
rough initial example: 3 integrable exponents; a=1/2 excluded
nice=20; elapsed=0.002s; peak RSS=13.27 MiB

## Self-audit and a failed shortcut

The new scalar diagnostic exited 0. Actual nice was 20, peak RSS 13.27 MiB,
and runtime 0.002s. The launcher's setpriority warning comes from inherited
nice 20; both scripts explicitly verified the actual priority before doing
any calculation. No test failed, and no earlier file was edited.

Re-derived every load-bearing coefficient independently:
- Fourier heat trace and periodized Gaussians agree; the trace upper bound
  is 1+(8 pi r)^(-1/2), with generator Delta.
- The three summands in the mild equation give factor 3, leading to
  a1=6(T B^2+G^2), a2=6G^2/sqrt(8 pi). Squaring the latter separately
  simplifies 16 pi a2^2 to 72 G^4. Each Laplace-kernel term is <=1/4.
- The density in drift-free coordinates has -A/2; in drifted Brownian
  coordinates it has +A/2. The inverse removal density gives the same
  result. Constant drift of either sign and either diffusion sign verifies
  this and both entropy coefficients 1/2 by exact rational arithmetic.

Tried the shortcut of applying full Novikov directly. It fails under these
hypotheses: for g=1, h=0, b(z)=kz, the drift-free mass is Brownian Z and
A >= k^2/T (integral_0^T Z_s ds)^2. The Gaussian integral has variance
T^3/3 (checked both by stochastic Fubini and double covariance integration),
so E exp(A/2)=infinity for k^2 T^2>=3. This sufficient divergence condition
is not asserted to be sharp. Added this explicit obstruction to PROOF.md.
The stopped-energy proof handles this case without exponential moments.

Also corrected the order of explanation in Section 5: localizing in H
first justifies weak-to-mild conversion under each changed measure; the
uniform moment lemma is applied afterwards, avoiding a circular appeal to
moments to obtain that conversion.

Audited the potentially missing state-law step: elementary predictable
integrals are Borel functions of the canonical path. Their weighted L2
completion uses a finite measure, with predictable rectangles and smooth
spatial factors dense. One fixed almost-sure subsequence defines J for
all drift-free realizations with law mu0. Equivalence preserves convergence
in probability, so the change of integrator and entropy formulas remain
valid under the drifted measure. No uniqueness of joint state-noise laws
is assumed.

Checked the simultaneous hard example g(z)=1+|z|^beta,
h(x)=dist(x,0)^(-a), 0<a<1/2, and b(z)=z+1_{z>=0}.
All assumptions hold despite unbounded diffusion, unbounded spatial initial
norm, and discontinuous drift. The a=1/2 endpoint is correctly excluded.
Zero drift reduces to density one, zero energy, and zero entropies.

## Report saved and final scope check

Wrote REPORT.md with the required first-line verdict. The claimed new
result is precisely the drift extension plus its density/entropy checks,
conditional on the same drift-free input used by round 3. The transfer
method itself is attributed to Han's Proposition 8.5; this session does
not claim an independent proof of the full positive-Hölder theorem.
The report records both commands, successful outputs, resource use, the
failed direct-Novikov shortcut, remaining external uncertainty, and one
specific next extension to audit. All new files remain in this folder.

Final read-only audit at 05:09 Asia/Tbilisi: checked the report's verdict,
claims and commands against the saved proof and actual diagnostic output.
Re-read the two density directions, the entropy identities and the explicit
Novikov obstruction. The prior diagnostic used 12.84 MiB peak RSS; the new
one used 13.27 MiB, both at nice 20. No further tests were needed after
prose clarifications. REPORT.md, PROOF.md, LOG.md and check_transfer.py
are the completed deliverables.
