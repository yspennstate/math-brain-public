# T092 work log

Started 2026-11-15 10:45 +04 (Asia/Tbilisi).
Task: “take the NEXT checkable step on this problem, building on that work.”

## Scope and startup

All writes stay in this folder. The specific task excludes global brain,
mesh and checklist mutations, git, external writes and subagents. Read
the startup memory and memory index directly rather than run recall tools
that log outside this folder. Read compute_state.json: status warn,
mode owner_away_open, CPU saturation. No numerical run or build is planned.

Read the original, round 3, round 4 and round 5 reports, logs and available
proofs. Directory listings show no computation scripts in those folders;
the original folder has no PROOF.md. The original SOLVED_ELSEWHERE.md and
round 3 CLAIM_AUDIT.md were also read. An overlarge combined read was
truncated; subsequent reads were split into smaller sections.

Shell reads use `env OMP_NUM_THREADS=1 nice -n 15 /bin/sh -c '...'`.
The sandbox prints `nice: setpriority: Operation not permitted` and still
executes tiny read-only commands. No substantive computation will run
without the requested priority. Writes use apply_patch.

## Bounded literature check

Queries through the web search tool:

* `"simple Lebesgue spectrum" "2026" Banach`
* `"A smooth three-torus diffeomorphism"`

Opened the primary passage section, Lean scope note and arXiv:2210.15480.
The search returns the same OpenAI claim discussed by earlier workers;
no newly verified resolution was established. The arXiv page still lists
el Houcein el Abdalaoui and version 2 of June 9, 2023. General literature
checking ends here, within five minutes. No SOLVED_ELSEWHERE.md is warranted.

Primary sources actually opened:

* https://raw.githubusercontent.com/openai/math/main/preprints/A-smooth-three-torus-diffeomorphism-with-simple-Lebesgue-spectrum-September-23-2026/build/sections/02-passages.tex
* https://raw.githubusercontent.com/openai/math/main/lean/docs/144.md
* https://arxiv.org/abs/2210.15480

## Earlier result independently rechecked

Re-derived the round 5 normalization from test functions. If s=j/N and
the model mass is N^-1 f(s,a) da, its image under t=s+s(La+beta)/N has
density K(s,Nt-j). Indeed dt/da=sL/N, so the Jacobian cancels N^-1.
This works with either sign of s. Integrating the density gives exactly
N^-1 int f(s,a) da, checking the scale a second way.

For the freezing step change y=Nt-j before summing. Each summand is at
most |y| sup_s|K_s(s,y)|/N and the exterior Jacobian is 1/N. There are
at most N(B-A)+2|y|+1 potentially nonzero indices. This reproduces
(B-A)J_1/N+J_2/N^2 with no residue factor. For each fixed t the residue
lattice in a has spacing P/(|t|L); centered-cell integration gives
|Q_h(t)-int f(t,a)da/P| <= int|f_a(t,a)|da/(2|t|L).
Summing over h gives PH/(2L). Cutoff mass sums once, and folding is an
L1 contraction. Thus the main round 5 transport bound holds.

Independently, for c and leading array ell, the pointwise difference of
squared moduli is at most |c-ell|(|c|+|ell|). The cutoff equal to one on
supp ell preserves this bound. Cauchy--Schwarz, Parseval and centered
quadrature give the stated eta_N coefficient factor. Counting shifted
support indices gives the rounding term. No failure was found, including
j=0, negative indices and N not divisible by P.

## One extension selected, before proving it

Prove the missing eta_N -> 0 assertion for the exact passage coefficients,
uniformly at stationary-support edges, with the sum over all integer j
and the retained cutoffs. Aim for a quantitative O(N^-1) bound for eta_N
using a uniform quadratic change of variables and Fourier inversion,
rather than the source's qualitative local-tail argument. This is the
next step named by round 5 and closes its coefficient-error input for
fixed smooth compactly supported packets. Keep all data fixed before N;
do not infer a full geometric or spectral construction.

## Uniform coefficient argument obtained

Extend V from a neighborhood of the packet's compact u support to a
strictly increasing proper smooth function on R with derivative bounded
above and below by positive constants. Extend the amplitude by zero.
This changes neither the exact integral nor its leading term. Every
parameter now has one stationary point, so there is no separate branch
edge to patch. A global quadratic coordinate gives an amplitude b(y)
whose compact support and first four derivative norms are uniform on
bounded frequency-parameter sets, including zero leading amplitude.

Fourier inversion of the quadratic exponential gives remainder at most
pi N^-3/2 int xi^2 |bhat(xi)| dxi. Splitting at |xi|=1 bounds the
moment by (2/3)||b||_1 + ||b''''||_1/(8 pi^4). Thus each of O(N)
bounded-frequency coefficients has error O(N^-3/2), giving squared
array error O(N^-2). Two integrations by parts bound the exterior
coefficients by D |j|^-2, with D independent of N when |j|>RN.
Their squared tail is at most 2D^2/(3R^3 N^3), for an integer R.
The planned eta_N=O(N^-1) estimate follows. Full constants, the exact
quadratic identity and the cutoff consequences are being written out.

This is stronger than merely verifying the source's qualitative array
limit. It is still a fixed-data result. No uniformity as the packet,
chart or jitter changes with N is asserted.

## Proof and cutoff consequences saved

Saved PROOF.md with eta_N^2 <= (2R+1) B^2/N^2 +
2D_0^2/(3R^3N^3). B is an explicit supremum of the transformed
amplitude's L1 and fourth-derivative L1 norms; its finiteness follows
from a single compact parameter set, including support crossings.
The tail constant D_0 is displayed after two integrations by parts.

For a fixed smooth support cutoff equal to one near the unshifted
stationary image, rounding moves the leading support by at most |m|/N.
For all large N the cutoff is one there. Deleted squared coefficient
mass is <=eta_N^2; Parseval gives retained reconstruction error <=C/N.
Combining this with the independently checked round 5 discrepancy
inequality proves E_N<=C_E/N and its residue bound with this explicit
input. Rounding is removed at the intensity stage, before fast sampling.

Opened the primary citation README to confirm author OpenAI and date
September 23, 2026:
https://raw.githubusercontent.com/openai/math/main/preprints/A-smooth-three-torus-diffeomorphism-with-simple-Lebesgue-spectrum-September-23-2026/README.md
The qualitative array limit already appears in its passage section.
The new work is an independent proof with a rate and retained-cutoff
consequences, not a claim of historical novelty or full validity.

One apply_patch append failed because its context wrapped differently
from the saved file. The tool made no change; the corrected patch saved
the intended Gaussian and direct-intensity checks. No mathematical
claim depended on that patch failure.

## Adversarial checks and final audit

Re-derived the quadratic coefficient and its phase sign using the exact
Gaussian integral (1-i epsilon N)^(-1/2). Its expansion has leading
e(epsilon/8)/sqrt(N) and first relative correction -i epsilon/(2N),
matching the Fourier-kernel calculation. This tests both signs of m.
Recomputed the Fourier moment constants: the inner interval contributes
2/3, and the two exterior half-lines contribute 2/(2 pi)^4=1/(8 pi^4).

Re-derived the tail bracket by differentiating A'/D^2-A D'/D^3;
its four coefficients are 1,-3,-1,3. Dividing the phase by N and
repeating the estimate gives the same 4,24,8,48 in D_0. The sum over
both tail half-lines is <=2 integral_(RN)^infinity x^-4 dx, hence
2/(3R^3N^3). The interior count 2RN+1 yields squared error O(N^-2).

Checked the retained intensity rate a second way, coefficient by
coefficient: if |ell|<=L_0/sqrt(N) and |C-ell|<=B/N^(3/2), its
intensity error is <=2L_0 B/N^2+B^2/N^3. Sum O(N) entries and add
the tail to obtain O(N^-1), independently of Parseval/Cauchy--Schwarz.

Tested the cases A=0, m<0, negative j, rounding of either sign,
stationary point outside the original branch, stationary point on
the support boundary, and the deleted j=0 coefficient. The leading
support is exactly the stationary image shifted by (m Delta_N,0),
so fixed neighborhoods suffice eventually. Added an explicit bound
for actual removed intensity sum (1-chi^2)|C|^2, besides the norm
difference sum (1-chi)^2|C|^2: both are <=eta_N^2 because ell=0
where chi<1. No overlooked support-edge term or nonsummable tail
was found. Finite packet lists require only finitely many constants.

Read back PROOF.md in sections and all of REPORT.md and LOG.md.
The report's first line has the required VERDICT: PROVED form and its
scope agrees with the proof. The coefficient bound is uniform over
permitted rounding but only for fixed smooth packet data. No assertion
of uniform control over future charts or N-dependent packet cutoffs is
present. No numerical experiment, script or proof-assistant build ran.

Final check commands:

    env OMP_NUM_THREADS=1 nice -n 15 /bin/sh -c 'sed -n "235,530p" PROOF.md; cat REPORT.md; wc -l LOG.md PROOF.md REPORT.md; date "+%Y-%m-%d %H:%M:%S %z"'

Output before the final audit additions: 130 lines LOG.md, 571 lines
PROOF.md, 67 lines REPORT.md; clock 2026-11-15 10:52:47 +0400.
Subsequent sed reads covered the rest of the proof and the added
removed-intensity bound. The sandbox again refused priority adjustment
on these tiny reads. All deliverables are in the current folder;
earlier-session files were never edited.

Result: the round 5 missing coefficient input is proved with rate
eta_N=O(N^-1) and E_N=O(N^-1). The next step is simultaneous physical
smooth control, support tracking and tag transmission, as REPORT.md
specifies. The complete finite-measure existence problem remains
unresolved here.
