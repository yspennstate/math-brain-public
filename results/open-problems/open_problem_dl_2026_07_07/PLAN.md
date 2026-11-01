# Open-problem program — deep learning theory (2026-07-07)

## Goal
Find a *famous*, publicly-posed, recognized open problem in the mathematics of deep learning
(DNNs), one that strong people have genuinely worked on, and solve it COMPLETELY — full rigorous
proof, no partial credit. Write a standalone paper (house style: amsart, honest framing, human
voice) and push to math-open-problems.

## Constraints / principles (carried over from 2026-07-06 program)
- Optimize (recognized + precisely stated + genuinely open + completely solvable-by-me + important).
  Completability is decisive: a full resolution of a real, citable open problem beats a dent in a
  Tier-0 problem.
- Every claimed theorem: (i) written rigorous proof, (ii) numerical confirmation where meaningful,
  (iii) independent adversarial referee passes (>=2 clean). Tags: PROVED / PARTIAL / CONJECTURE.
- Paper must read human (no AI tells), boring commit messages, standalone artifact.

## Candidate slate (to be status-checked by scouts, July 2026)
- C1. Deep LINEAR networks: convergence of gradient flow/descent to a GLOBAL minimizer for almost
  every initialization (non-strict saddles at rank-deficient critical points are the obstruction).
  Posed/left open by Bah–Rauhut–Terstiege–Westdickenberg and follow-ups.
- C2. Bubeck–Sellke "law of robustness" TIGHTNESS conjecture (NeurIPS'21 outstanding paper):
  construct p-parameter nets interpolating n noisy points with Lipschitz O(sqrt(nd/p)).
- C3. Depth lower bounds for exact ReLU expressivity: max(x1..x5) with 2 hidden layers /
  CPWL depth conjecture ceil(log2(n+1)) (Arora–Basu–Mianjy–Mukherjee; Hertrich et al.).
- C4. Entezari et al. permutation linear-mode-connectivity conjecture (likely not fully provable —
  only width-dependent random-net versions).
- C5. Sweep: COLT open problems 2016–2026 (DL-related), Telgarsky notes open problems,
  Shamir/Safran/Vardi posed problems, minimal-width universal approximation exact constants,
  Hanin–Rolnick linear-regions conjectures, memorization-capacity gaps.

## Method
3 web scouts verify status + surface anything better → commit to ONE target → prove end-to-end
with numerics + adversarial referees → paper → push (branch + master, boring message).

## Log
- 2026-07-07: dir created; scouts dispatched (C1; C2; C3+C5 sweep).
- 2026-07-07: fetched BS'21 (2105.12806) directly. C2 "tightness" is CLOSED in their own
  Remark 1.1 (RBF construction traces the whole curve p in [~n, nd]). The live open problem
  from that thread is C2': the ORIGINAL Bubeck-Li-Nagaraj conjecture — law of robustness for
  TWO-LAYER nets with UNBOUNDED weights (BS prove it only under poly(n,d)-bounded parameters;
  their Appendix A shows unbounded weights BREAK the law for three layers, so two-layer is the
  exactly-critical case). Candidate attack: "ridge rigidity" — a width-m two-layer function f
  with Lip(f) <= L is a sum of ridge functions in m directions; kinks in distinct directions
  cannot cancel, so each univariate profile has derivative-variation O(L x kinks) after
  extracting one global linear part => the class {width m, Lip <= L, restricted to B(0,2sqrt d)}
  has metric entropy ~ md log(...) INDEPENDENT of weight magnitudes => rerun BS covering
  argument. If this holds up, the conjecture falls. MUST check 2022-26 literature (scout 2).
- 2026-07-07 (later): COMMITTED to C2'. Prior-art verified clean 4 ways (BLN citation crawl,
  BS citation crawl, 2 targeted searches; Wu-Huang-Zhang ICML'23 still keeps poly weights;
  Husain-Balle 2102.08093 withdrawn). Scout reports: deep-linear a.e. (C1) verified open but
  7-years-hard (degenerate saddles) — skip; max_5 depth conjecture DISPROVED at STOC'26,
  successor MAX_6 = coin-flip construction hunt — skip. MASTER_PROOF.md written (rigidity +
  entropy + self-contained BS core + assembly, 3 regimes unified). Caught + fixed myself: net
  members must be L-Lipschitz => internal net via packing duality vs the parameter-box class.
  Numerics: rigidity check PASSES 27/27 incl. planted 1e6-cancellation + near-parallel plants
  (saturate at ratio 0.50 as predicted). Paper main.tex written (11pp, compiles); empirical-law
  table pending background training; referee pass 1 (adversarial subagent) in flight.
