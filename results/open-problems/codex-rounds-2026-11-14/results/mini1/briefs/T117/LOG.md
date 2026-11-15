# T117 work log

Task received: “push this problem forward by one checkable piece,” 2026-11-14, approximately 22:00 Asia/Tbilisi (18:00 UTC; exact prompt timestamp unavailable).

## Scope and constraints

Only this folder will be changed. No git, subagents, network publication, mesh/checklist/brain writes, or external-state writes. The later folder-only instruction overrides the global requirements that would write outside it. Startup memory and the compute governor were read. The governor reports warn/cpu_saturated, mode owner_away_open, with ample free memory. Computation will be tiny, standard-library-only and single-threaded, with OMP_NUM_THREADS=1 and a nice -n 15 launch. The sandbox prints `nice: setpriority: Operation not permitted`; priority cannot be independently inspected because ps is also denied. No escalation is available. Avoid heavy computation.

## Step 1: literature check (begun 18:00 UTC)

Used the web search tool for the exact arXiv identifiers in the brief and queries for binary deletion capacity in October/November 2026. Opened the arXiv abstract pages of 2609.19412, 2609.13351, 2609.24908 and 2609.24889. No resolution or substantial advance after the supplied status was located. This is a bounded search, not a proof of absence. The first three match the supplied status. The fourth is relevant existing finite-block symmetry work and will be inspected to avoid claiming its reduction as new.

Opened primary references:
- Dimitris Papailiopoulos, *Binary Deletion Channel Capacity to Within One Hundredth of a Bit*, https://arxiv.org/abs/2609.19412.
- Özgür Soysal, *A New Upper Bound on the Binary Deletion Channel Capacity*, https://arxiv.org/abs/2609.13351.
- Hassan Khodaiemehr, Chen Feng, Tolga M. Duman, *Improved Lower Bounds on the Capacity of the Binary Deletion Channel via a Learning Approach to Run-Length Inputs*, https://arxiv.org/abs/2609.24908.
- Hassan Khodaiemehr, Chen Feng, *Orbit Reduction and Learned Run Distributions for Finite-Blocklength Binary Deletion Channels*, https://arxiv.org/abs/2609.24889.

## Step 2: chosen finite special case

Determine the exact maximizer of I(X^3;Y) for every 0<d<1 by reducing the three complement/reversal orbit masses to one scalar equation. Then check whether any stationary binary first-order Markov input attains that finite-block maximum. This is small enough to prove completely and verify by independent enumeration of all deletion masks and an unconstrained eight-input capacity calculation. The result is a finite-block statement, not a solution of C(d), and no novelty claim is made for the standard symmetry reduction or the finite-block converse.

The planned artifact is PROOF.md, accompanied by a one-thread standard-library verification script and saved numerical data.

## Step 3a: prior-work inspection and preliminary algebra

Opened the full HTML of Khodaiemehr–Feng 2609.24889v2. It explicitly proves uniqueness, full support and complement/reversal symmetry, and says run-count inputs are optimal for N<=3. These facts must be attributed rather than claimed as new. The intended deliverable specializes this to an explicit scalar equation and investigates the first-order Markov obstruction. A quick scalar probe shows that a guessed all-d sign of the Markov obstruction changes; no all-d nonattainment claim will be made without resolving the crossing.

## Step 3b: the checkable result selected after the sign probe

Let k=d/(1-d). The three orbit masses are a,b,c for constant, two-run and alternating words. Optimizing at fixed a gives b/c=2^(1+2k). The remaining scalar derivative is strictly decreasing. A stationary first-order Markov law additionally requires b^2=4ac. Combining these gives a scalar obstruction B(k). Contrary to the initial guess of nonattainment for every d, B changes sign: preliminary binary64 values B(1)=0.18384497888207818 and B(2)=-0.9378661196101081. The new target is an exact theorem: there is exactly one d in (0,1) where the three-bit optimizer is first-order Markov. A symbolic second derivative reduces strict concavity of B to positivity of 3z^4+24z^3+21z^2+6z for z=2^(2k)>0. Exact sign certificates at k=1,2 are ratios 26244/23104>1 and 9526572/18249984<1.

Literature search stopped well within ten minutes; no later solution was located. The existing 2609.24889v2 theorem is acknowledged explicitly. Nothing in this session improves the best known asymptotic capacity bounds.

## Step 3c: proof saved

Wrote PROOF.md: exact three-bit optimizer, scalar derivative equation, necessary and sufficient Markov constraint, and uniqueness of the positive zero of B. The rigorous enclosure d_* in (1/2,2/3) uses integer comparisons, independent of floating-point root finding. Next: enumerate all channel masks, compare with a survivor-pair construction, verify formula values and dual divergences, run unconstrained Blahut–Arimoto, and independently find the exceptional parameter with high-precision Decimal arithmetic.

Saved verify_three_bit.py. It sets a 180-second wall alarm, uses only the standard library and writes results only to this directory. No interval arithmetic claim is made for the decimal approximations.

Starting audit command: `OMP_NUM_THREADS=1 nice -n 15 python3 -B verify_three_bit.py`. Wall alarm: 180 seconds.

## Step 4: numerical and independent algebra audit

Exact command:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 -B verify_three_bit.py
```

Output (the launch also reports `nice: setpriority: Operation not permitted`):

```text
All checks passed.
Exact rational channel rows verified: 32
Random orbit-law formula checks: 100; maximum error 6.66e-16 bits
Concavity numerator coefficients (ascending): [0, 6, 21, 24, 3]
Exact B(1) log argument: 6561/5776 > 1
Exact B(2) log argument: 264627/506944 < 1
k_* (Decimal, 90-digit working precision): 1.17951454339254740782543133411112580064458272469047953765889879538510436188947687059712658
d_* (Decimal, 90-digit working precision): 0.541182231138756721675487785340046141846365478411646477981476404208529299490749716018878160
theta_* (Decimal, 90-digit working precision): 0.163125488452710037252822760855622808785129704975210600386258867568916273392768848556659064
k_* (independent raw-channel criterion): 1.179514543392547
Maximum optimum row-divergence spread: 5.27e-15 bits
Unconstrained asymmetric-start BA runs: 7
Observed nice: 20
Peak RSS: 16.22 MiB
Elapsed: 0.083 seconds
Data: results.json, results.csv
d          M3(d)/3         b^2-4ac
0.010000000  0.981581079588  -0.0013091805
0.050000000  0.910574224346  -0.00651661072
0.100000000  0.827679159359  -0.0127020402
0.250000000  0.615607969536  -0.024230929
0.500000000  0.365269059079  -0.00467225113
0.541182231  0.333670049708  +2.77555756e-17
0.600000000  0.291920106474  +0.00424048184
0.650000000  0.258846718732  +0.00494709357
0.750000000  0.195761099248  +0.00151958607
0.900000000  0.090334974551  +3.08898689e-08
```

The decimal root values are numerical estimates, not outward-rounded enclosures. The exact root bracket (1/2,2/3) is established by rational inequalities in the proof. Every input law was checked directly against the channel, including the exceptional Markov candidate. Raw deletion-mask enumeration and a separate recursive construction agree exactly over rational probabilities. BA makes no symmetry assumption and begins asymmetrically.

## Step 4b: audit outcome and algebraic d=1/2 corollary

The first verification run passed. The observed inherited nice level is 20 (more yielding than 15); the sandbox warning reflects the attempted change from this inherited level. The run used 16.22 MiB peak RSS and 0.083 seconds. Seven unconstrained BA runs and ten direct dual checks agree with the scalar result; the independent channel-divergence root matches Decimal evaluation.

The exact d=1/2 case simplifies further: the optimizing constant-word mass is the unique root of 85a^3-239a^2+244a-81=0 in (0,1), and its capacity has the explicit divergence expression in PROOF.md (20). This was added to the same finite-block result. At this deletion probability the only possible optimal Markov candidate has theta=1/5, excluded by the exact derivative sign log2(6561/5776)>0. The script will now audit this extra algebra independently before the final report.

Starting audit command: `OMP_NUM_THREADS=1 nice -n 15 python3 -B verify_three_bit.py`. Wall alarm: 180 seconds.

## Step 4: numerical and independent algebra audit

Exact command:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 -B verify_three_bit.py
```

Output (the launch also reports `nice: setpriority: Operation not permitted`):

```text
All checks passed.
Exact rational channel rows verified: 32
Random orbit-law formula checks: 100; maximum error 6.66e-16 bits
Concavity numerator coefficients (ascending): [0, 6, 21, 24, 3]
Exact B(1) log argument: 6561/5776 > 1
Exact B(2) log argument: 264627/506944 < 1
k_* (Decimal, 90-digit working precision): 1.17951454339254740782543133411112580064458272469047953765889879538510436188947687059712658
d_* (Decimal, 90-digit working precision): 0.541182231138756721675487785340046141846365478411646477981476404208529299490749716018878160
theta_* (Decimal, 90-digit working precision): 0.163125488452710037252822760855622808785129704975210600386258867568916273392768848556659064
k_* (independent raw-channel criterion): 1.179514543392547
Maximum optimum row-divergence spread: 5.27e-15 bits
Unconstrained asymmetric-start BA runs: 7
Half-deletion cubic coefficients (ascending): [-81, 244, -239, 85]
Half-deletion optimal a: 0.6508389034459541
Half-deletion M3 from independent divergence formula: 1.095807177237158 bits
Observed nice: 20
Peak RSS: 16.16 MiB
Elapsed: 0.079 seconds
Data: results.json, results.csv
d          M3(d)/3         b^2-4ac
0.010000000  0.981581079588  -0.0013091805
0.050000000  0.910574224346  -0.00651661072
0.100000000  0.827679159359  -0.0127020402
0.250000000  0.615607969536  -0.024230929
0.500000000  0.365269059079  -0.00467225113
0.541182231  0.333670049708  +2.77555756e-17
0.600000000  0.291920106474  +0.00424048184
0.650000000  0.258846718732  +0.00494709357
0.750000000  0.195761099248  +0.00151958607
0.900000000  0.090334974551  +3.08898689e-08
```

The decimal root values are numerical estimates, not outward-rounded enclosures. The exact root bracket (1/2,2/3) is established by rational inequalities in the proof. Every input law was checked directly against the channel, including the exceptional Markov candidate. Raw deletion-mask enumeration and a separate recursive construction agree exactly over rational probabilities. BA makes no symmetry assumption and begins asymmetrically.

## Step 5: attempts to break the result

- The original guess “the optimum is never Markov” failed. The crossing at d_*=0.5411822311387567 is retained and proved, rather than hidden.
- Checked all eight input rows against all 15 output strings, including the empty output; conditioning on output length does not reveal deleted positions.
- Checked that symmetry alone does not imply Markov structure: the extra equation b^2=4ac is imposed separately. Arbitrary stationary binary transition matrices are covered because uniqueness forces the putative maximizing marginal to have uniform one-bit marginals and complement-invariant pair marginals.
- Checked boundary cases a=0, a=1 and r=0, r=1 by endpoint derivative limits; the optimum is interior for every 0<d<1. The d=0 channel is an identity and d=1 has zero mutual information; neither is included in the unique-positive-exception claim.
- Verified the concavity polynomial by independent integer coefficient multiplication, and the derivative formula by finite differences at k=0,0.1,1,2,4.
- At d=1/2 checked the cubic independently from polynomial multiplication, found its root by a separate polynomial bisection, and recomputed capacity from the constant-input row divergence.
- Checked units: M_3 is bits per three-bit block; the table divides by 3. These are finite-block optima and do not supply achievable infinite-channel rates without a boundary-loss argument. No asymptotic claim is drawn from the Markov obstruction.
- Checked numerical certification language: direct dual gaps and BA comparisons use floating point, not directed intervals. The proof and coarse exact root bracket stand independently of those computations.
- Checked compute limits: one thread, nice 20 inherited, about 16 MiB peak RSS, well below one second per verification run. No heavy run was needed.

No further unresolved mathematical gap was found in the finite-block argument. Literature priority for the explicit scalar/cubic specialization and unique exception has not been established.

## Step 6: completed artifacts

Saved REPORT.md with the required PROVED verdict, finite-block scope, exact and numerical results, reproduction command, failed initial guess, numerical limitations, prior-work attribution and a blocklength-four next step. PROOF.md, verify_three_bit.py, results.json, results.csv and computation_output.txt contain the supporting derivation and checks. No files outside this folder were written.
