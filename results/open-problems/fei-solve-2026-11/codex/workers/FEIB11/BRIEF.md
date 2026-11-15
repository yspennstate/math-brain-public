# Worker FEIB11 (account acc2)

disk: small

Read ~/fei_solve_agent/NOTES.md and ~/fei_solve_agent/FLOW.md first
(section 5(a), 5(d) of FLOW.md state this task).
The check scripts are in ~/fei_solve_agent/code (check_p.py, check_flow.py, check_feib09.py); write your own.

Task: the Renyi form of containment. f is Boolean on n bits with values +-1, mu(S) = fhat(S)^2, up(S) = E (D_S f)^2
= P_{U~mu}[U contains S], I = total influence, Var = 1 - mu(empty).
    WC(f) = P_{S,U iid mu}[S subset of U] = sum_S mu(S) up(S) = E_x sum_S fhat(S)^2 (D_S f(x))^2.
Jensen gives log2(1/WC) <= A = E_S log2(1/up(S)), and WC >= sum_S mu(S)^2 >= max_S mu(S)^2. So
    FEI  =>  containment A <= C I  =>  WC >= 2^(-C I),      and      FMEI (max mu >= 2^(-C I))  =>  WC >= 2^(-2 C I).
The conjecture "log2(1/WC) <= C I" (stated with I, and in the sharper form C I/Var-free: decide the right
normalisation for nearly constant f) is weaker than both open conjectures.

1. Literature: is WC, or anything equivalent, in the literature (O'Donnell-Wright-Zhou 2011; Keller-Mossel-Schlank;
   Chakraborty-Kulkarni-Lokam-Saurabh; Shalev 2018; Arunachalam-Chakraborty-Koucky-Saurabh-de Wolf 2021 on FMEI;
   Kelman-Kindler-Lifshitz-Minzer-Safra 2020)? Say exactly what is known for FMEI and whether the known FMEI cases
   and methods give WC in general. Work only from what you can actually read; mark anything recalled as RECALLED.
2. Compute sup of log2(1/WC)/I, and of log2(1/WC)/(I - 1) on balanced f, exhaustively for n <= 5 (use the NPN
   census), on a large sample for n = 6, 7, and on the families: AND, tribes, majority, address/MUX functions,
   bent functions, PM(K33) (the record function in NOTES.md), random functions, read-once formulas. Compare with
   the H and A values of the same functions. Which functions are extremal for WC?
3. Prove what you can. Targets in order: (a) log2(1/WC) <= C I^2 from the fixed-level theorem in FLOW section 3;
   (b) log2(1/WC) <= C I log I; (c) WC >= 2^(-C I) for monotone, unate, symmetric, read-once and low-degree
   classes; (d) the general statement. For (d), the form E_x sum_S fhat(S)^2 (D_S f(x))^2 invites a second-moment
   or a random-restriction argument: under a restriction to J with outside fixed to x, fhat_{J,x}(S) for S = J is
   D_J f(x) up to sign, so WC = E_x sum_J mu(J) fhat_{J,x}(J)^2. Try induction on restrictions, and try the
   tensor-power trick (WC is multiplicative under products of functions on disjoint variables with XOR; check).
4. Test the intermediate Renyi statements WC_q = (sum_S mu(S) up(S)^q)^(1/q) for q in (0, 1]; q -> 0 is containment.
   Does the sup of log2(1/WC_q)/I over the census stay bounded as q decreases, and how does it grow?

Deliverables: PROOFS.md, scripts with outputs, RESULTS.md (tables, extremal truth tables in hex), REPORT.md with a
verdict line per numbered item. Label every statement PROVED, CHECKED (numerically, with scope), RECALLED or OPEN.
Memory: each process under 3 GiB, at most 2 threads, nice 10.

