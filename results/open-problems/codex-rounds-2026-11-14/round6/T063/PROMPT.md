# Open problem T063: Gaussian free field limit of the six-vertex height function

Statement: For the six-vertex model on Z^2 with weights a = b = 1 and c ∈ (0, 2), so that Δ = 1 − c²/2 ∈ (−1, 1), the height function converges in the scaling limit to a Gaussian free field whose variance is an explicit function of Δ.

Source: R. J. Baxter, Exactly Solved Models in Statistical Mechanics (Academic Press, 1982); B. Nienhuis, Critical behavior of two-dimensional spin models and charge asymmetry in the Coulomb gas, J. Stat. Phys. 34 (1984)

Where it stands (checked by us, Nov 2026): Δ = 0 is the dimer model, with GFF limit (Kenyon 2001); small perturbations of it by interacting-dimer methods (Giuliani–Mastropietro–Toninelli, arXiv:1406.7710). For a = b = 1, logarithmic variance (delocalization) for c ∈ [1, 2] (Duminil-Copin–Karrila–Manolescu–Oulamara, arXiv:2012.13750, JEMS 2024), after unbounded variance for c ∈ [√(2+√2), 2] (Lis, arXiv:2004.05337); localization for c > a + b and delocalization at c = a + b (Glazman–Peled, arXiv:1909.03436). Averous–Duminil-Copin–He–Lammers–Manolescu (arXiv:2610.07454) prove convergence to the GFF in simply connected domains with piecewise constant boundary conditions for a wide range of Δ, including Δ near 0 and Δ between −1 and −1/2. The whole range Δ ∈ (−1, 1) is open.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T063 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T063 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 4 worker built on that session. Its folder is ~/codex_op_1114r4/briefs/T063 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 5 worker built on the latest of these. Its folder is ~/codex_op_1114r5/briefs/T063 (read it, never
edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Your job for this session: take the NEXT checkable step on this problem, building on that work.
1. Five minutes at most: check whether anything after the earlier report changes the picture. If the problem was
   solved elsewhere, write SOLVED_ELSEWHERE.md (reference, arXiv id, what exactly is proved) and REPORT.md, then stop.
2. First re-check the earlier result: re-derive its main claim or re-run its computation an independent way, and
   write in LOG.md whether it holds. If it does not hold, that finding is your result.
3. Then choose ONE piece that extends it: the next step its report names, a wider special case, a sharper constant,
   more cases computed, the missing lemma. Write the choice and why in LOG.md first, then do it. A proof goes in
   PROOF.md with every step written out; a computation is a script in this folder with the command and output in LOG.md.
4. Try to break your own result: re-derive every load-bearing number a second way; look for the case you miss.
5. Finish with REPORT.md: first line exactly one of  VERDICT: PROVED <what> | VERDICT: PARTIAL <what> | VERDICT: COMPUTED
   <what> | VERDICT: NO PROGRESS <why> | VERDICT: EARLIER RESULT WRONG <what> . Then what is new beyond the earlier
   report, the commands, what failed, what you are unsure of, and what the next worker should do.

Rules (the author's standing laws):
- Work only inside this folder. Read anything, but never edit files elsewhere, never use git, never push, post, email or
  create accounts. Nothing you write leaves this folder except when the coordinating agent copies it.
- Compute: every program you run stays under 1 GB of RAM, one thread (set OMP_NUM_THREADS=1), runs under `nice -n 15`,
  and finishes within 20 minutes per run. No GPU, no MLX, no torch. This Mac is shared; never fill it.
- Literature: use the web search tool. Cite only papers you actually opened, with the authors exactly as on the paper or
  its arXiv page. Never invent a reference, a number or a step.
- Save as you go: append to LOG.md after every step (what you did, the command, the output that matters). The account's
  weekly allowance runs out within hours and the session may stop at any moment; LOG.md is what survives.
- Write plainly, like a working mathematician: no hype, no talk about yourself or the process inside PROOF.md.




----- earlier REPORT.md -----
VERDICT: PROVED finite binary-bridge swap invariance and conditional fair cluster signs for inhomogeneous weights c_v >= 1

The earlier result holds. Its reflection, insertion and entropy argument was independently re-derived; its unchanged script passed again; a separate all-edge enumeration reproduced both 2x2 partition polynomials. The five-minute literature check found no newer full-range GFF proof that could be certified.

The new result verifies one finite ingredient of the November uniqueness argument. In a finite face rectangle, take two independent six-vertex height functions with possibly different fixed boundary heights, but the same vertex weights a_v=b_v=1, c_v>=1. At a fixed integer level ell of D=(h2-h1)/2, independently open each saddle diagonal with probability

    1 - c_v^(-2).

A saddle has D=ell±1 with the same sign relative to ell on its two endpoints and D=ell on the perpendicular diagonal. Join nearest neighbours with D!=ell and open saddle bridges. Exchanging any union of components that avoid the boundary, with height shifts by ±2ell, preserves the augmented Gibbs law. Conditional on the height sum, |D-ell| and the bridges, all interior component signs are independent and fair. [PROOF.md](PROOF.md) gives every step, including the direct treatment of c_v=1.

This supplies a binary marginal of the geometric-residual swap in Lemmas 3.2–3.5 of Yan Ru Pei's [November preprint](https://hexagonmath.org/pdf/2611.00291v1), identifier hexagon:2611.00291v1, not an arXiv identifier. It extends the finite formulation to inhomogeneous weights and the weight-one endpoint. Global novelty is not claimed. Corollary 1.3 and its infinite-volume dependencies are still not certified here; neither uniqueness nor a GFF limit follows from this finite theorem alone.

[check_binary_swaps.py](check_binary_swaps.py) passed 5,184 local admissibility checks, 4,976 exact rational mass checks, 10,368 nonzero-level checks, and 51,660 whole-domain swap images across 26 cases. It enumerated 37,452 augmented states and checked all 32,184 conditional sign fibers. Tests include unequal boundaries, bridges at the collar, mixed weights 1,3/2,2,3, and levels -2 and 3. Runtime was 2.573 seconds; peak RSS 49,987,584 bytes; effective nice 20. All counts and outputs are in [LOG.md](LOG.md).

Commands:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 check_binary_swaps.py
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 ~/codex_op_1114r4/briefs/T063/check_two_flux.py
```

Audit: the factor c_v^(-2) was derived both from the changed vertex weights and from an independent geometric-series calculation. A separate nonrecursive enumerator confirmed the domain filling counts. Omitting bridges fails explicitly: a single-block swap changes pair weight from c^2 to one. The closed-bridge probability supplies exactly the missing factor. This is not a counterexample to Pei's augmented construction.

What failed or remains uncertain: a shell PDF download failed with DNS error; the web tool opened the paper. The nice launcher could not increase an already inherited nice value of 20. No mathematical checks failed. The bridge theorem is at one fixed level; passing to the all-level fold, infinite-volume Gibbs law, and roughness still requires proof. The formula gives a negative opening probability for c_v<1 and establishes nothing there. No full uniqueness audit was completed.

Next worker: audit Pei's Lemma 4.4, the local reconstruction of the fold, then its entropy consequence in Lemma 4.5. Keep the original all-level residual coupling explicit; the fixed-level binary result alone does not justify that passage. The earlier torus-minimisation result remains available if uniqueness is eventually certified.

Only this folder was written. No git, subagents, external messages or publication were used.

Task: “take the NEXT checkable step on this problem, building on that work” (T063); received approximately 07:48 Asia/Tbilisi, 15 November 2026.
