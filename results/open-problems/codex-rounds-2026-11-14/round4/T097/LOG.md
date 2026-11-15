# T097 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
Session date: 15 November 2026, Asia/Tbilisi. First retained local clock
reading: 04:49:23 +04 (the earlier orientation output was truncated).

## Orientation and source reading

Read both predecessor folders' REPORT.md, LOG.md, PROOF.md and AUDIT.md.
`rg --files` found no mathematical scripts in either predecessor folder.
The current folder initially has PROMPT.md and runner files. Neither earlier
folder is edited. No git, subagents, or writes outside this folder are used.
The task-specific folder restriction supersedes external brain/mesh/checklist
updates. Startup memory and compute state are read only.

Read commands use `OMP_NUM_THREADS=1 nice -n 15 cat <files>` and
`OMP_NUM_THREADS=1 nice -n 15 sh -c '<read-only checks>'`.
The sandbox reports `nice: setpriority: Operation not permitted`.
No numerical workload is run; this will be a proof-only extension.
An initial broad file listing produced unnecessary output; subsequent reads
are bounded to the relevant files.

## Brief literature check

Used the web search tool with the queries:

- `"Gaussian free field" "lattice" "critical exponents" 2026`
- `"Gaussian free field" "2610.03703"`
- `"Gaussian free field" "critical" "2206.10724"`

Opened the arXiv pages for 2611.05357, 2610.03703, 2406.02397, and the full
HTML of 2206.10724v2. The first three concern cable-system clusters.
Muirhead's Theorems 1.2 and 1.10 supply the same lattice density input as
before. No lattice solution was found. The brief search is complete;
no SOLVED_ELSEWHERE.md is warranted. This search does not certify novelty.

## Independent verification of the earlier result

For fixed annulus R <= k < N, minimize
`sum (2k+1)^2 d_k^2` under `sum d_k=1` using Lagrange multipliers.
The equations give `d_k = c/(2k+1)^2`, with
`c = 1/sum (2k+1)^(-2)`. Thus the claimed restricted infimum A_R holds.
Writing v=k(k+1), the two numerators in the rational telescoping identity
are `144v^2+24v+13` and `144v^2+24v-3`; their difference is exactly 16.
The residual is O(k^-6), so A_R=4R+1/(3R)+O(R^-3) follows. This part holds.

Independently use the Gaussian likelihood moment and optimized Holder:
for s=t sqrt(cap(B_R)), p=p_R(h), q=p_R(h+t),
`q/p >= exp[-s sqrt(2 log(1/p))-s^2/2]`.
The existing density bound theta(h_*-u)>=c_q u^q for every q>4,
at u=R^-1/2, gives `limsup -log p_R(h_*)/log R <=2`.
At R=c t^-2/log(1/t), the maximal leading negative logarithm of the ratio
is sqrt(32c). Checking every smaller R and finite radii by continuity gives
the predecessor's coefficient `(log 2)^2/32`. The earlier result holds.
This verifies a lower bound for its specified relative radius, not a
conventional correlation length or any exact exponent.

## Chosen extension, recorded before proof

Choose one sharper-constant extension: leave the sup-norm-shell class and
construct a lattice capacity bound from continuum trial functions depending
on Euclidean distance to a cube. First establish an exact transfer by unit
cell averaging, avoiding an assumed lattice-to-continuum limit. Then optimize
the one-dimensional distance profile using the surface areas of rounded
cubes, and insert its coefficient into the same relative radius estimate.

Reason: A_R is optimal only in its shell class. A non-shell profile can lower
its leading coefficient 4 without requiring an unproved connection-event
score estimate. This does not aim to change a power or remove the logarithm.
The audit will independently check the cell averaging, all geometric factors,
the exact integral, and the resulting crossover coefficient.

## Proof completed

Created PROOF.md. For a compactly supported continuum Lipschitz function F,
set f(x) to its average over the unit cell centered at x. Jensen's inequality
and tiling, applied to each discrete difference, give exactly

    E_Z(f) <= (1/6) integral |grad F|^2.

Taking F=1 on the cube of half-side a=R+1/2 ensures f=1 on B_R. Profiles
depending on Euclidean distance s to that cube have weighted energy with

    S_a(s)=24a^2+12 pi a s+4 pi s^2.

Optimizing a compactly supported profile out to distance T gives energy
`[integral_0^T 1/S_a(s) ds]^-1`. Let T tend to infinity only after applying
the lattice capacity bound. The exact outcome is

    cap(B_R) <= C_cube (R+1/2),
    C_cube = 2 pi delta/[3 log((3+delta)/(3-delta))],
    delta=sqrt(9-24/pi).

The trial profile (lambda a)/(lambda a+s) with lambda=3/2 proves
`C_cube <=8/9+2 pi/3<3`. Thus this improves the preceding restricted
shell bound for every R>=2. No assertion of improvement at R=1 is made.

Substituting into the same relative-radius argument gives

    liminf t^2 log(1/t) L_rel(t) >= (log 2)^2/(8 C_cube)
                                > (log 2)^2/24,

improving the previous coefficient `(log 2)^2/32`. The increase is strictly
greater than a factor 4/3. This does not improve the exponent or remove
the logarithmic loss. All displayed constants are exact expressions;
no decimal computation, numerical script, or simulation was run.

The retained compute reading was warn / owner_away_open, CPU saturation
97.5 percent, with no distress flag. Work remained lightweight and proof-only.

## Adversarial audit completed

Created AUDIT.md with second derivations of each load-bearing constant:
parallel-body volume differentiation verifies the rounded-cube surface
polynomial; Euler's equation verifies the distance-profile minimizer;
completing the square verifies the exact logarithmic integral; Gaussian
tails reproduce the crossover coefficient independently of Holder.
The rational trial profile at lambda=3/2 gives the explicit check
`C_cube <=188/63<3`, using pi<22/7. A separate magnitude bound is
`C_cube>=2pi/3`. These are hand inequalities, not numerical outputs.

Tried the larger scale R=c t^-2: the logarithmic sensitivity still grows,
so the stronger constant-factor relative-radius bound does not follow.
Checked that using half-side R without its half-cell enlargement would
invalidate the averaging construction. All finite-T functions satisfy
the finite-support requirement before taking limits. No case requires
critical nonpercolation or monotonicity of the defining ratio in R.

Created LITERATURE.md and REPORT.md. The final targeted web read confirms
that Muirhead's equation (1.8) is the same SRW Green covariance; no
normalization conversion is needed. The complete new result is a sharper
constant for the earlier comparison method, not an exponent theorem.

Intermediate file check:

    OMP_NUM_THREADS=1 nice -n 15 sh -c 'wc -l LOG.md PROOF.md AUDIT.md; head -n 12 PROOF.md; date "+%Y-%m-%d %H:%M:%S %Z"'

Output: LOG.md 109 lines, PROOF.md 289 lines, AUDIT.md 163 lines at that
point; timestamp 2026-11-15 04:52:43 +04. These counts precede this append.

## Final file verification

Ran:

    OMP_NUM_THREADS=1 nice -n 15 sh -c 'for f in LOG.md PROOF.md AUDIT.md LITERATURE.md REPORT.md; do if test -s "$f"; then echo "$f: present"; else echo "$f: MISSING"; fi; done; head -n 1 REPORT.md; wc -l LOG.md PROOF.md AUDIT.md LITERATURE.md REPORT.md; date "+%Y-%m-%d %H:%M:%S %Z"'

Output:

    nice: setpriority: Operation not permitted
    LOG.md: present
    PROOF.md: present
    AUDIT.md: present
    LITERATURE.md: present
    REPORT.md: present
    VERDICT: PARTIAL a non-shell capacity bound and a larger relative crossover coefficient
    139 LOG.md
    289 PROOF.md
    163 AUDIT.md
    33 LITERATURE.md
    68 REPORT.md
    2026-11-15 04:53:52 +04

The LOG.md count is before this final append. Also ran

    OMP_NUM_THREADS=1 nice -n 15 rg -n 'C_cube|VERDICT|8/9|188/63|8 C|24|Next worker|Task:' REPORT.md PROOF.md AUDIT.md LOG.md

Output confirmed consistency of the exact capacity formula, the coefficient
`(log 2)^2/(8 C_cube)`, its lower bound `(log 2)^2/24`, and next-worker
guidance across the documents. The verdict is PARTIAL. The predecessor's
claims survived the recheck; the new result is the sharper constant.
