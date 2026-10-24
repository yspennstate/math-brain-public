# Solo FEI continuation: unequal NAND contraction

## Outcome

Full Friedgut--Kalai Fourier entropy--influence remains **OPEN**. This continuation resolves the unequal-block gap in the previously saved logarithmic NAND potential. A new complement-invariant potential contracts under arbitrary unequal disjoint NAND composition and gives an explicit Fourier logarithmic-edge bound for read-once NAND/De Morgan formulas.

The read-once class was already known to satisfy FEI, so this is a structural advance inside the current logarithmic route, not a new resolution of that class and not a breakthrough solution of FEI. Novelty of the particular potential is UNVERIFIED.

No finite universal K/I, B/I or H/I bound for arbitrary Boolean functions is proved.

All work in this continuation was done by the primary assistant. Subagents, delegated tasks, other-model calls, commissioned audits and outside contacts: zero. Actual model and reasoning-level metadata are not exposed and are therefore UNVERIFIED.

The freshly read master head at the start was `40f073af2d274fbd06d04cd632aee5a580ccfb42`; the newest prior solo commit was `d4f836b29183d5d032c337b8beb62d807f5bac8a`. The current root exclusion register, the latest P03 fleet handoff, the solo README and NEXT_STEPS, the erasure reduction, the signed-balance note, and the newest solo report were read before continuing. The direct solo instruction controls this track; no fleet rotation or exhausted cell enumeration was resumed. The original P03 finite-dimensional metric 6 remains only a prior reported fact, not freshly audited.

## 1. The old unequal-block obstruction

For an indicator A with mean alpha, Fourier coefficients c_S, singleton-square mass Q_A=sum_i c_i^2, define

    K_A=sum_edges min(c_S^2,c_T^2)|log_2(c_S^2/c_T^2)|,
    I_A=4 sum_S |S|c_S^2.

The earlier identical-block potential controlled repeated NAND of equal children but failed under unequal blocks and even under complementing a child with a constant-one block.

The saved complement-invariant correction was

    U(A)=K_A-2Q_A log_2(alpha).

For A'=1-product_j A_j on disjoint blocks, put

    p=product_j alpha_j,   w_j=p/alpha_j.

The exact unresolved identity was

    U(A')=sum_j w_j U(A_j)
       +2 sum_j w_j Q_Aj
          [(1-w_j)log_2(alpha_j)-w_j log_2(w_j)].       (1)

## 2. New contracting potential

Define

    V(A)=U(A)+(2/ln2)Q_A.                               (2)

For 0<w<=1,

    (1-w)log_2(alpha)-w log_2(w)
       <=-w log_2(w)<=(1-w)/ln2.                        (3)

The first inequality uses alpha<=1. The second is `w ln(1/w)<=1-w`, an immediate consequence of `ln x<=x-1` at x=1/w.

The exact singleton identity is

    Q_A'=sum_j w_j^2 Q_Aj.                              (4)

Insert (3) in (1), add `(2/ln2)Q_A'`, and combine (4):

    V(A')
      <=sum_j w_j U(A_j)
        +(2/ln2)sum_j w_j(1-w_j)Q_Aj
        +(2/ln2)sum_j w_j^2Q_Aj
       =sum_j w_jV(A_j).                                (5)

Also

    I_A'=sum_j w_j I_Aj.                                (6)

Therefore

    V(A')/I_A'<=max_j V(A_j)/I_Aj                       (7)

for every nonconstant output. Complementation preserves V and I. The positive unequal-child correction is paid exactly by the loss between `sum w_jQ_Aj` and `sum w_j^2Q_Aj`; no equal-means assumption remains.

The exact derivation of (1), (4) and (6) is included in `UNEQUAL_NAND_CONTRACTION_2026-09-18.md`, not inferred from the checker.

## 3. Transfer to the Boolean K functional

For F=1-2A, all nonempty Fourier masses are four times those of A. Edges not touching the empty coefficient therefore contribute four times the corresponding internal part of U.

For an empty--singleton edge, let x=c_i^2<=1/4, q=4x, and r=(1-2alpha)^2. A scalar split into r>=q and r<=q proves

    min(q,r)|log_2(q/r)|<=4[-x log_2 x].                (8)

In the second case, `r log_2(q/r)<=q/(e ln2)<=2q`; in the first, use `r<=1`. Summing gives

    K(F)<=4U(A)<=4V(A).                                 (9)

For a literal indicator,

    K_A=0, Q_A=1/4, U(A)=1/2, I_A=1,
    V(A)/I_A=1/2+1/(2ln2).

Induction using (7) proves for every read-once NAND formula, with optional complementations,

    K(F)/I(F)<=2+2/ln2.                                 (10)

AND, OR and NOT are obtained without variable reuse, so the same holds for read-once De Morgan formulas. Combining the previously proved inequalities `K<=B<=K+(2/ln2)I` and the erasure reduction yields

    B(F)/I(F)<=2+4/ln2,
    H(F)/I(F)<=2+6/ln2.                                 (11)

## 4. What this does and does not resolve

Proved:

- the exact all-arity unequal-product recursion;
- contraction of V under arbitrary unequal disjoint NAND;
- the comparison K(1-2A)<=4V(A);
- the explicit constants (10)--(11) for read-once NAND/De Morgan formulas.

Not proved:

- any bound on V(A)/I_A for arbitrary seed indicators;
- any decomposition of arbitrary Boolean functions into disjoint products to which (5) applies;
- any universal FEI constant.

Thus the composition step cannot amplify a bad seed, but the full conjecture is exactly the missing seed-independent bound. The result should not be presented as solving FEI.

## 5. Abandoned approach in this continuation

The first attempted route was to exploit the joint partial-Boolean branches after a spectral parity query. Their odd-branch support is the physical coordinate-sensitivity set, and two-face parity pays one split entropy by transverse influence. On inspection this is exactly the one-data-coordinate specialization already proved in `SELECTOR_CHARGING_2026-09-18.md`:

    B_i<=h_2(Inf_i)<=2 sum_{j!=i} Inf_j.

Summing repeats the transverse budget n-1 times; the one-point defect makes this repeated-credit loss explicit. Since this did not move the existing frontier, the work changed to the unequal NAND correction rather than relabeling the prior lemma as progress.

## 6. Exact checks

Executed from the solo folder:

    python check_unequal_nand_potential.py
    python check_logarithmic_structures.py
    python -m py_compile check_unequal_nand_potential.py check_logarithmic_structures.py

Both scripts returned PASS. The new certificate uses exact rational arithmetic and 160-bit outward rational logarithm intervals and records:

- 49 deterministic unequal seed-pair recurrences and strict V contractions;
- K(1-2A)<=4U(A) for all 270 nonconstant indicator truth tables through three variables;
- six recursively unequal literal NAND trees through seven variables.

The prior script rechecked 41 identical-block recurrences, 16 unequal identities, and 64 selector examples. Finite checks are consistency evidence only; universal statements are proved algebraically. These are self-checks, not independent audits.

## 7. Literature and novelty scope

A fresh primary-source search reopened O'Donnell and Tan, *A composition theorem for the Fourier Entropy-Influence conjecture*, arXiv:1304.1347, https://arxiv.org/abs/1304.1347 . Its abstract explicitly states FEI for read-once formulas over arbitrary bounded-arity gates. Therefore (11) is not claimed as a new class theorem.

The exact relationship of V to potentials in that paper or elsewhere has not been exhaustively checked. Search results do not establish novelty; the potential is labeled UNVERIFIED.

## 8. Remaining full-scope obligation

For every real vector a whose inverse Walsh transform is Boolean, prove

    sum_edges min(a_S^2,a_T^2)|log_2(a_S^2/a_T^2)|
       <=C sum_S |S|a_S^2

for a finite universal C, or exhibit a Boolean counterexample family. The new theorem says this normalized cost is stable under a broad disjoint composition operation once it is controlled at the seeds. It supplies no control for arbitrary seeds.

## 9. Measured execution

The supplied run start was 2026-09-18T03:01:19Z and the first sampled shell clock was 03:01:37Z. This report checkpoint is 03:09:06Z: 7 minutes 47 seconds from the supplied start and 7 minutes 29 seconds between sampled shell clocks. This includes retrieval, mathematical derivation, writing and exact checks; it is not a claim of continuous model compute. GitHub delivery time is not included.

Intervals between continuations are not counted as research time. Neither the schedule nor this report establishes an hour of work or ten continuous hours.
