# T102 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
Session start: 15 November 2026, approximately 01:28 Asia/Tbilisi.

## 1. Orientation and bounded literature check

Read the previous REPORT.md, LOG.md, PROOF.md and complete check_gluing.py in
~/codex_op_1114/briefs/T102, without editing them.
Read startup/identity memories and compute_state.json. The governor reported
warn, owner_away_open, CPU saturation; only tiny standard-library calculations
are planned. No subagents or git. The current folder-only rule overrides the
global instructions to mutate checklist, mesh, and memory stores; none of
those commands will be used. A startup brain recall was attempted before
that conflict was recognized; it reported a failed detached index refresh.
No further brain commands will be run.

Commands: rg --files on the current and previous folders; cat/sed on the
previous artifacts; startup brain recall under OMP_NUM_THREADS=1 nice -n 15;
read-only inspection of compute state and startup memory. The recall found
no useful T102 memory. nice printed “setpriority: Operation not permitted”;
the inherited priority will be checked in the calculation itself.

Web search began at about 01:28 and ended at about 01:31, within five minutes.
Queries included:
- "2604.14122" resistance exponent
- two dimensional incipient infinite cluster resistance exponent 2026 spectral dimension
- "percolation" "resistance exponent" "2026" "Alexander"
- "spectral dimension" "two-dimensional" "2026" percolation -site:wikipedia.org

Opened https://arxiv.org/abs/2604.14122 and
https://arxiv.org/html/2604.14122v1. The arXiv page lists only v1, submitted
15 April 2026. Corollaries 1.3–1.4 still express the exponents in terms of
unidentified beta_res. Exact author names: Irina Đanković, Maarten Markering,
Jason Miller, Yizheng Yuan. Also opened https://arxiv.org/abs/2611.09427,
a search hit on critical long-range percolation, not a solution of T102.
No later solution was located; this bounded check cannot prove absence.

## 2. Independent re-derivation of the earlier result

Use the voltage/flow inner product: if theta minimizes energy in an affine
flow space and eta has zero terminal totals, E(theta+t eta) is minimized at
t=0. Thus <theta,eta>_r=0 and E(theta+eta)=E(theta)+E(eta).
For two pieces, impose matching interface current q; the energy is exactly
R_A+R_B+Q_A(q-q_A)+Q_B(q-q_B). Minimizing gives the earlier identity.
Alternatively the full current is an orthogonal projection onto the smaller
space satisfying conservation at every interface vertex. The projection
cost is precisely the missing nonnegative term. This also works for
several, possibly disconnected, layers in edge-flow variables.

Independent scalar audit on the cycle: two x-to-y paths each have resistance
L+1, so R_full=(L+1)/2. Each wired half is 1 in parallel with L, so the sum
is 2L/(L+1). Subtracting gives (L-1)^2/[2(L+1)], agreeing with the report.
No flaw found. A new script will independently solve full Laplacians and
check the earlier numbers, without running the old script (which writes
into its own folder).

## 3. Chosen extension, recorded before calculation

Prove an explicit upper bound on the earlier matching cost using total
variation of adjacent optimal boundary-current profiles and the *unwired*
effective-resistance diameters of those interfaces inside the two layers.
The two-layer coefficient should be the harmonic mean of the two resistance
diameters; for many connected layers a factor 2 follows from adding the two
repairs entering each layer. Establish sharpness or find a counterexample
to an unnecessarily optimistic constant. Verify by exact rational full-network
Kirchhoff solves, including nonuniform edge resistances and a disconnected
case where a diameter is infinite.

Why: this replaces the previous abstract requirement on D_m by separately
measurable shell quantities and identifies why ordinary wired resistances
alone do not suffice. It does not supply a percolation probability estimate
or identify beta_res. No claim of novelty is made for quadratic network
principles.

## 4. Derivation and sharpness design

For a zero-sum boundary demand h, put t=||h||_1/2. A coupling of h_+ to
h_- expresses h as a nonnegative sum of dipoles. Minkowski in the energy
norm gives Q(h)<=diam_R(S)*t^2. Both interfaces remain UNWIRED when
computing this diameter. This estimate is attained by a single dipole
between a diameter pair.

For one interface with mismatch delta and adjacent diameters a,b, choose
the matched profile q as a convex combination of the two wired optima.
The energy bound is [a(1-lambda)^2+b lambda^2]*TV(delta)^2. Minimizing at
lambda=a/(a+b) gives ab/(a+b)*TV(delta)^2. For m layers, repair each
interface on its two sides this way. A layer receives at most two repair
flows, so E(f+g)<=2E(f)+2E(g). Therefore
D_m <= 2 sum_i [a_i b_i/(a_i+b_i)] TV(delta_i)^2.
With only two layers the factor 2 is absent.

Candidate showing the multi-layer factor 2 is needed: three layers with
S1={u,v}, S2={p,q}, and path resistances
G1: x-u=1, x-v=K;
G2: u-p=1, v-q=1, p-q=L;
G3: p-y=K, q-y=1.
All can be subdivided to unit edges; the graph is planar of degree at most 3.
Take K=L^2. The middle wired profile is (1/2,1/2) at both ends, so both
mismatches have TV=(K-1)/(2(K+1)). Diameters are K+1, L+2, L, K+1.
The proposed sum without factor 2 is asymptotic to L/2. A path of length
L+3 and contraction of its three unit edges sandwich the full resistance
between (1/L+2/(K+1))^(-1) and L+3. Thus D_m/L -> 1, and the ratio of
D_m to that sum tends to 2. This will be checked by exact full solves.

## 5. Independent exact computation passed

Created check_matching.py, using unit-voltage Dirichlet equations followed by
current normalization. This is independent of the old script's prescribed-
divergence solves and its interface quadratic-form inversion. Did not import
or run the old script. Long subdivided paths are represented by their exact
series resistance, so the largest solve is tiny.

Command:
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B check_matching.py

Exit 0. Important output (complete output saved in matching_results.json):
- all 255 earlier interface configurations passed; 210 positive corrections;
- all seven earlier cycle values agreed exactly, and attained the new bound;
- 729 weighted star pairs passed, 696 with 0<D<bound;
- 128 three-layer strip cases passed;
- all 11 sharpness-family cases passed; D/sum_terms=1.3463522476 at L=2,
  1.9545632131 at L=64, 1.9970760280 at L=1024;
- disconnected example: R_full=15/8, D=1/8, one-sided bound=1/4;
- inherited nice=20, OMP_NUM_THREADS=1;
- peak RSS 15,826,944 bytes; internal elapsed time 0.344 seconds.

The nice command again reported setpriority denied, but the script checked
that the actual inherited nice was 20 (lower priority than requested).
CPU limit 90 seconds; wall alarm 120 seconds; one process and no numerical
libraries. The fixed-size exact solves stay far below 1 GB.

Second checks within the script: energy orthogonality for every solved
network; independent series/parallel cycle values; analytic expressions
for all four diameters and the mismatches in the sharpness family; Rayleigh
contraction/path bounds; and a separate two-variable flow minimization of
the sharpness family, agreeing exactly with the full Dirichlet solve.
The factor 2 cannot be dropped: already at L=2 the ratio is 1827/1357>1.

## 6. Audit caught and corrected a contraction count

Reading the proof back against the network found an error in the first
sharpness argument: contracting x-u,u-p,q-y leaves routes L,K,K+1, not
L,K+1,K+1 as stated in section 4 of this log. The reported stronger numeric
lower bound happened to hold in the tested cases, but that contraction
did not prove it. Corrected the proof and script to contract all FOUR unit
edges x-u,u-p,v-q,q-y. The quotient has precisely three parallel edges
of resistances L,K,K, giving the valid lower bound (1/L+2/K)^(-1).
Both sides still have asymptotic ratio 1 to L when K=L^2. The sharpness
limit and all exact resistances are unaffected. Section 4's contraction
sentence is superseded by this correction.

Further audit: the two interface repairs have the same divergence sign,
because the base total divergence on the interface is -delta_i. Using
lambda_i=a_i/(a_i+b_i) gives a(1-lambda_i)^2+b lambda_i^2=ab/(a+b).
The two-vertex case is an exact equality; many-layer coefficient 1 fails
already in the L=2 example. Infinite diameters are never multiplied by
zero: a zero mismatch is assigned zero energy and a one-sided finite
repair is constructed explicitly. No claim is made when both diameters
are infinite and a mismatch is nonzero.

## 7. Corrected rerun and final mathematical audit

Reran the command from section 5 after correcting the contraction bound.
Exit 0, all exact checks passed. Every network value and case count was
unchanged. Final peak RSS: 15,810,560 bytes; elapsed 0.3646 seconds;
effective nice 20. matching_results.json contains the full final output.

The proof now includes every step of: orthogonal gluing, the dipole-coupling
bound, harmonic allocation of one-interface repairs, the factor 2 from two
repairs per layer, the explicit planar sharpness family, and the conditional
shell-exponent implication. Sharpness uses a corrected quotient bound and
an independent two-variable energy calculation. The AO threshold is checked
both by cross multiplication, 6d_f=4(d_f+beta), and substitution:
beta=d_f/2=91/96 gives d_w=91/32 and d_s=4/3.

Limits: no IIC-law estimate on the boundary mismatch or unshorted diameter;
no exponent improvement. A general geometric shell need not be connected.
The finite-side extension is sufficient only when one adjacent diameter is
finite (or the mismatch vanishes). It does not address all component-balanced
demands when both diameters are infinite. Using worst-pair diameters may be
much coarser than using the energy of the actual demand. Published novelty
of the network inequalities has not been investigated or claimed.

Wrote REPORT.md with verdict PARTIAL and a specific next-worker task.
