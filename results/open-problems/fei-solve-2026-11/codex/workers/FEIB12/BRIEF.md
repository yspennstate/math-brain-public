# Worker FEIB12 (account acc2)

disk: small

Read ~/fei_solve_agent/NOTES.md and ~/fei_solve_agent/FLOW.md first
(section 5(a)-(c) of FLOW.md state this task; section 1 defines Gamma and B).
The check scripts are in ~/fei_solve_agent/code (check_p.py, check_flow.py, check_feib09.py); write your own.

Task: the cancellation half of FEI in its noise form. f Boolean (+-1) on n bits, g_S = D_S f, mu(S) = (E g_S)^2,
up(S) = E g_S^2, T_u the noise operator. Define
    Phi(u) = E_{S~mu} log2( 1 / <g_S, T_u g_S> ),      0 <= u <= 1.
Then Phi(0) = H, Phi(1) = A, Phi is decreasing, and H <= Phi(u) + I log2(1/(1-u)); so for each fixed u < 1,
FEI is equivalent to Phi(u) <= C I. B = H - A = Phi(0) - Phi(1) = E_S log2(up(S)/mu(S)).

1. Verify the three claims numerically (all 4-variable functions, a 6-variable sample) and write the proofs out.
2. Tabulate Phi(u)/I for u in {0, 1/4, 1/2, 3/4, 7/8, 1} on the n <= 5 NPN census (sup and the extremal functions),
   tribes, majority, AND, PM(K33), address functions, read-once formulas, random functions. Report
   sup (Phi(1/2) - A)/I and sup (Phi(1/2) - A)/(I - Var): this is the cancellation cost at noise 1/2.
3. Prove an upper bound for Phi(u) - A that beats the log-convexity bound ln(1/u) E_nu|U - S| (nu is the superset
   coupling of FLOW 5; that bound is of order n on majority). Ideas to try, each to be tested numerically before any
   proof attempt: (a) <g, T_u g> >= ||g||_2^2 * u^(m(g)) with m(g) a median, not the mean, of the level of g's
   spectral measure; (b) reverse hypercontractivity applied to |g_S| together with a bound on the noisy
   cancellation ratio <|g|, T_u|g|> / <g, T_u g>; (c) a recursion in u: d/du Phi in terms of the influences of
   T_sqrt(u) g_S; (d) the identity B = E_nu log2(1/w(S)) = H_nu(S|U) - D(mu Z || mu) of FLOW 5(a): bound the
   conditional entropy H_nu(S | U) of a spectral subset S of U given U by C I directly.
4. Classes. Prove Gamma <= C I, B <= C I or Phi(1/2) <= C I, with explicit C, for: monotone and unate functions
   (there fhat(i) = Inf_i; say what survives at higher levels), symmetric functions (FEIB02 has B <= 3.462071 I and
   Gamma <= 8I/5: read ~/codex_fleet/20261108_pro/workers/FEIB02 and build on it, do not redo it), linear threshold
   functions, read-once formulas, functions whose derivatives all have one sign, degree-d functions.
5. The recursion B(E + x D) = B(E) + B(D) + sum_T Ehat(T)^2 log2(1 + up_D(T)/up_E(T)) of FLOW 5(b): find the
   largest c and the best functional G with  B(f) <= c * I(f) + G(f)  provable by induction on this recursion
   for Boolean f (G must vanish or be O(I) at the root). Use an LP over the n <= 4 census to find which G survive.

Deliverables: PROOFS.md, scripts with outputs, RESULTS.md (tables, extremal truth tables in hex), REPORT.md with a
verdict line per numbered item. Label every statement PROVED, CHECKED (numerically, with scope) or OPEN.
Memory: each process under 3 GiB, at most 2 threads, nice 10.

