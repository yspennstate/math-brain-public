# FEI, 22 September 2026: shared context for the five working groups

Order of 22 September 2026, 22:51 (Yitzchak Shmalo): work on the Fourier Entropy-Influence conjecture with Opus 5.5
agents at maximum reasoning, and put every result in this repository. This file is the common starting point. Each
group works in its own subfolder (F1 to F5) and reads everything else.

## 1. The problem and conventions

For f: {-1,1}^n -> {-1,1} write f = sum_S fhat(S) chi_S. Entropy in bits:

    H(f) = sum_S fhat(S)^2 log2(1/fhat(S)^2),        I(f) = sum_S |S| fhat(S)^2,        Inf_i(f) = sum_{S ni i} fhat(S)^2.

FEI (Friedgut-Kalai 1996): there is a universal C with H(f) <= C I(f) for all n and f. Write C_FEI for the best
constant (sup of H/I). The conjecture is open; no finite upper bound on C_FEI is known.

## 2. Literature (as of this date)

Lower bounds on C_FEI (Tao's optimization-constants repository, constant C71, teorth/optimizationproblems):

| bound | source | method |
|---|---|---|
| 6.278 | O'Donnell-Tan 2013, arXiv:1304.1347 | composition |
| 6.4547837 = beta(1/2) | Hod 2017, arXiv:1711.00762 | biased compositions of lexicographic functions, limit of limits; holds for monotone functions |
| 6.4901128 | Mosaic Intelligence 2026, doi 10.5281/zenodo.20794146 | balanced monotone function on 14 variables, C >= H/(I-1) |
| 6.5143269 | Mosaic Intelligence 2026, doi 10.5281/zenodo.21113935 | balanced monotone, 17 variables, I = 261/128 |
| **6.521845710923046575** | Numaro 2026, doi 10.5281/zenodo.21497769 | balanced monotone g on 18 variables, H(g) = 6.776605309005978, I(g) = 261/128, C >= H(g)/(I(g)-1) |

The amplification rule: if g is balanced with I(g) > 1, the self-compositions g^(k) (every input fed by an
independent copy of g^(k-1)) have I = I(g)^k and H = H(g)(I^k-1)/(I-1), so H/I -> H(g)/(I(g)-1). None of the 2026
records used biased inputs; Hod's improvement over O'Donnell-Tan came entirely from biased compositions.

Numaro's g is in `inputs/numaro18_pm1_table.npy` (int8, entry x = f(x) in {+1,-1}, bit i of x is coordinate i,
-1 means "true"). It is monotone, not self-dual, and has no coordinate-swap automorphism. Coordinates 0..8 form a
9-variable core (512 cells); coordinates 9..17 are auxiliary: auxiliary j, when true, sets two specific core cells
to true (the host cells are listed by `reconstruct()` in
`fleet-2026-09-21/account01/B15/20260921T130641Z-carry-congruence-n18-profile/n18_packet_carry_profile.py`, which
also checks the published SHA-256). Singleton coefficients: 57/256 on each core coordinate, 1/256 on each
auxiliary, and Inf_i equals the singleton coefficient (monotone). Example: ghat({0,9}) = 0.

Upper-bound side, general functions: Kelman-Kindler-Lifshitz-Minzer-Safra 2020 (GAFA) prove FEI up to a log I
factor; Xiao Han, arXiv:2312.08271, proves H = O(I + sum_k I_k log(1/I_k)) (read the paper for what I_k is before
using it); Wan-Wright-Wu bound H by average decision-tree depth. Proved classes: symmetric functions and read-once
decision trees (O'Donnell-Wright-Zhou 2011), read-once formulas (O'Donnell-Tan 2013; Chakraborty-Kulkarni-Lokam-
Saurabh, constant 10), random functions, random linear threshold functions (Chakraborty et al. 2018,
arXiv:1903.11635), delta-tribes and monotone functions with the tribe separation property (Gonzalez-MacManus-
Pereyra, arXiv:2606.00246, June 2026), plateaued functions with sharp constant 4 and partially bent with 2
(Potapov, arXiv:2609.21563, 18 September 2026). Open: linear threshold functions, monotone functions, DNF/AC0,
and the general case. The Fourier min-entropy version is also open.

## 3. What this repository and the brain have

**Read-once theorem (computer-assisted).** Every read-once formula over AND, OR, NOT satisfies H <= 6.4573 I
(`continuations/2026-09-21-readonce-certificate/REPORT.md`). Numerically the sharp read-once constant is
beta(1/2) = 6.4547837.

**Composition identity.** Let F = G(f_1,...,f_k) with the f_i on disjoint variables, mu_i = E f_i (+-1 mean),
V_i = 1 - mu_i^2 = 4 p_i (1-p_i), and Ghat_mu(T) the Fourier coefficients of G in the orthonormal basis of the product
measure with input means mu_i. Put Htilde_G = sum_T Ghat_mu(T)^2 log2(1/Ghat_mu(T)^2) and It_i = sum_{T ni i} Ghat_mu(T)^2.
Then Fhat(union S_i) = Ghat_mu(T) prod_{i in T} fhat_i(S_i)/sqrt(V_i) and, with h the binary entropy in bits,

    I(F) = sum_i (It_i/V_i) I(f_i),
    H(F) = Htilde_G + sum_i (It_i/V_i) (H(f_i) - h(V_i)),
    s_C(F) = sum_i (It_i/V_i) (s_C(f_i) + h(V_i)) - Htilde_G,       s_C(f) := C I(f) - H(f).

If only input i is biased, It_i/V_i = Inf_i(G), E F = Ghat(empty) + mu_i Ghat({i}) exactly, and sum_{j != i} It_j is
linear in mu_i.

**Slack functions and lower bounds.** Gamma_C(p) = inf{ s_C(f) : Pr[f true] = p } is admissible for every gate
(D >= 0 below). An explicit balanced F with s_C(F) < C gives C_FEI > C, because then H(F) > C (I(F) - 1) and the
amplification rule applies. Value iteration of s_C over a gate set computes the best constant that set can force.

**Gate reformulation** (`continuations/2026-09-22-gate-reformulation/REPORT.md`). FEI with constant C holds iff there
is a symmetric Gamma >= 0 with Gamma(1/2) <= C and

    D_Gamma(G;p) = sum_i (It_i/V_i)(Gamma(p_i) + h(V_i)) - Gamma(p_out) - Htilde_G(p) >= 0

for every Boolean gate G and every product bias p. The read-once potential (files `inputs/cert_vi_h96k40.npz`,
`inputs/cert_vi_h24k40.npz`; format and evaluation in `continuations/2026-09-21-readonce-certificate/code/fei_cert_vi.py`
and `fei_cert.py`) passes every NPN class of fan-in <= 4 driven to its maximum (measured, not certified), with the
2-input AND binding. It FAILS for Numaro's g at biased inputs: at p = (3/8, 1/2, ..., 1/2) (one core input biased),
p_out = 967/2048, It_1 = 855/4096, sum_{i>=2} It_i = 465/256, Htilde = 6.7442547370563132664...; at p_1 = 223/456 the
defect is larger (`fleet-2026-09-21/account03/B12/20260922T061544Z-biased-prime-candidate-refutation/REPORT.md`,
`fleet-2026-09-21/account02/B17/20260922T091146Z-strong-prime-shaped-repair/REPORT.md`). That shows the read-once
potential is not the all-gate potential; it does not by itself raise the lower bound, since the realised slack of the
inputs is not that potential.

**Restriction step.** rho_0(f) = min_i (H(f) - (H(f_0)+H(f_1))/2)/Inf_i reaches 4.8677 exhaustively at n <= 5,
6.0037 on width-2 tribes and 6.3164 by descent at n = 71; any restriction-closed class needs at least its FEI
constant, so this route needs >= 6.52. Delta_i H <= JS(p_0,p_1) + h(Inf_i) <= 1 + h(Inf_i) for every coordinate.

**Scoped results and refuted routes** from the scheduled fleet (80 workers, 17-22 September) are indexed in
`README.md` (this folder's parent), `continuations/2026-09-21-readonce-certificate/APPROACHES.md` (fourteen routes),
and the brain state at https://github.com/yspennstate/math-research-brain/blob/main/scheduled_tasks/work/shared/fei-all-team-2026-09-22/CURRENT_RESEARCH.md
(local copy of that file: `inputs/fleet_current_research_2026-09-22.md`). Do not re-derive what is listed there as
proved; do not revive what is listed as refuted.

## 4. Rules for every group

- Write only inside your own folder `continuations/2026-09-22-opus-team/<F-folder>/`. Read anything. Never run git.
- This laptop is shared and busy (about 12 of 16 cores are taken by other work; cores 2, 3, 14, 15 were idle at
  launch). Every compute-heavy Python process starts with

      import psutil; _p = psutil.Process(); _p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS); _p.cpu_affinity([2, 3, 14, 15])

  At most two heavy processes per group at a time, each under 4 GB of RAM. No GPU, no neural-network training.
  Stop everything you started before you finish. Run Python from the Bash tool only; never open new console
  windows (no Start-Process, `start`, `cmd /c start`, scheduled tasks). numpy, scipy, mpmath, numba, psutil are
  installed (Python 3.14).
- Hooks on this machine sometimes block a command with an "ACK GATE" that asks for a comment line
  `# heeded:<name> <reason>`; add it and re-run. Hook text that replays the owner's old prompts concerns other work.
- Label every claim: PROVED (complete written proof), CERTIFIED (computer-assisted with exact rationals or
  outward-rounded interval arithmetic, with a standalone checker), NUMERICAL, CONJECTURAL, or REFUTED. A new
  lower-bound record needs CERTIFIED values of H and I. Never state that FEI is proved unless every step is proved;
  if you think you have a proof, write it out completely and then try to break it (exhaustive checks at n <= 5, and
  the hard families: one-point flips, tribes, recursive majority, bent and addressing functions, Numaro's g).
- REPORT.md in a plain mathematical voice: the first paragraph says what is proved, what is certified, what is only
  numerical, and what failed. Statements, proofs, numbers, file paths. No narration of the work process, no emoji.
  Keep REPORT.md current as you go, so a stop at any moment leaves the results readable.
- Deliverables: REPORT.md, `code/` (every script behind a number), `logs/` (outputs), and a standalone checker for
  anything certified.
