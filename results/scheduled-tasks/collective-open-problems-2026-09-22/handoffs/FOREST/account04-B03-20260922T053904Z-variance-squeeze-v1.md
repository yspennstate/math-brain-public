# FOREST handoff — account04/B03 — rank-sensitive variance squeeze

Outcome: **AUXILIARY_ONLY**. Candidate `FOREST-3CONN-VARIANCE-SQUEEZE-v1`. Parent target remains OPEN. Context: `WITHOUT_VERIFIED_BRAIN`.

Named OTHER-account theorem consumed: account02/B01, commit `97feb5d7c3122f12cd446f95c2bfb3eec6ffe0ff`. For a lexicographically minimal counterexample `(G,e,f)`, that report proves `G` is 3-connected and, on a uniform forest `H` of `G0=G-{e,f}`, with addability indicators `X,Y`, deficit `D=E[X]E[Y]-E[S]=-delta<0`, and `T_g=1{g in H}`, it proves for every third edge

    a_g=-Cov(X,T_g)>0,
    b_g=-Cov(Y,T_g)>0,
    a_g b_g >= delta Var(T_g).

New exact consequence. Let `rho=r(M(G0))`. Summing all third edges and applying Cauchy twice gives

    delta (sum_g sqrt(v_g))^2
      <= (sum_g a_g)(sum_g b_g)
      <= sqrt(Var X Var Y) Var(|H|),

where `v_g=Var(T_g)`. Minimality gives pairwise NC inside `G0`, hence `Var(|H|)<=sum_g v_g`. For a uniform independent set of any loopless rank-`rho` matroid: (i) each element has inclusion probability at most `1/2`, by the injection `Ind(M/g)->Ind(M\g)`; (ii) its mean size is at least `rho/2`, because `(k+1)i_{k+1}>=(rho-k)i_k` makes `i_k/binom(rho,k)` nondecreasing. Therefore `sum v_g>=rho/4`, while `sqrt(v_g)>=2v_g`, so

    delta <= sqrt(x(1-x)y(1-y))/rho <= 1/(4rho).

Since the peer reduction makes `G` 3-connected, `G0` stays connected after deleting `e,f`; thus `rho=|V(G)|-1` and

    delta <= 1/[4(|V(G)|-1)].

This is a genuine aggregate compatibility constraint on the remaining 3-connected obstruction, but it is **not** a contradiction. Do not promote it to target closure or spend a run merely sharpening the constant. The next unpaid step is graph-global: exploit that all `a_g,b_g` arise from endpoint-connectivity addability events to force extra cancellation/lower deficit incompatible with the displayed squeeze.

Complete proof and exact checker/output are in:
`proofnet24/P14-probability-correlation/collective-2026-09-22/account04/B03/20260922T053904Z-B03-forest-r13/`.
