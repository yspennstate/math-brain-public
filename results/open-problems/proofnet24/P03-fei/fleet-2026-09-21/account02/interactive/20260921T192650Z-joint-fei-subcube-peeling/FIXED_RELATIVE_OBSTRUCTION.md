# Further full-problem attempt: fixed-relative support accuracy is not enough

Full FEI remains OPEN / NOT PROVED. This continuation followed the coefficient-12 near-support theorem in ADDENDUM.md and tried to remove its codimension-dependent tolerance. The attempted strengthening is false: even a centered Boolean function with a UNIQUE maximum-influence pivot and sensitivity support within relative error 1/16 of a coordinate subcube can have an unbounded entropy-decrement/folded-budget ratio for the corresponding control block.

This is a counterexample to that selected-block bridge, not to FEI or to existence of another useful restriction. The displayed family itself has H<11I after the stated threshold r>=32. It does not refute a theorem using additional JOINT assumptions on every derivative row. The valid ADDENDUM theorem retains tolerance 2^-r/(16r).

## 1. A genuine Boolean rare multiplexer with a subcube override

Fix r>=4, put M=r+4, q=2^-r and delta=2^-M=q/16. Use one pivot x, r control bits z, and M selector bits w, all independent and uniform. In the w cube let P={0}, A_k={e_k} for 1<=k<=r, and C be the complement of these r+1 points. Write chi_x=(-1)^x and chi_zk=(-1)^z_k. Define f by

    f(x,z,w)=chi_x                 if z=0 or w in P,
              chi_zk             if z!=0 and w in A_k,
              1                  otherwise.             (1.1)

The cases are disjoint and the function is Boolean pointwise. Its sensitivity indicator in x is exactly

    eta_x(z,w)=1{z=0 or w=0}.

Thus Q={z=0} is a coordinate subcube of codimension r and

    Pr(eta_x != 1_Q)=(1-q)delta <=q/16,
    p:=I_x(f)=q+(1-q)delta.                             (1.2)

Direct edge counting gives, for each control k,

    I_zk(f)=q+delta-3qdelta=p-2qdelta<p.                 (1.3)

To see this, on P the function is independent of z; on C and each A_j with j!=k, its k-influence is q; on A_k it is 1-q. Weight by the corresponding point probabilities. Hence

    I_Z(f)=r(q+delta-3qdelta)<rp.                       (1.4)

This already satisfies the average-control hypothesis of ADDENDUM, but not its stronger q/(16r) accuracy for large r.

The raw selector-coordinate influences are also exact:

    I_wk(f)=delta(r-q)          for 1<=k<=r,
    I_wk(f)=delta(r+1-q)        for r<k<=M.              (1.5)

Indeed in a first-r selector direction the edge 0--e_k joins P and A_k, the other r-1 active point edges join A_j to C, and in an extra selector direction all r+1 active points join C. Averaging over z,x yields (1.5). In particular

    I_w(f)=delta[r(r-q)+4(r+1-q)] >=delta r^2.           (1.6)

## 2. Spectral control entropy is at least order r delta log r

Let T be the control Fourier frequency, b the membership of x, and W the selector frequency. The part of f not containing x is

    (1-1_Q(z))[1_C(w)+sum_k chi_zk 1_Ak(w)].

Since 1_C+sum_k 1_Ak=1-1_P and 1_Q has every control Fourier coefficient equal q, for W!=0 and T={k} the normalized Fourier coefficient is exactly

    a_(b=0,T={k},W)=delta[(-1)^W_k+q].                 (2.1)

For each fixed nonzero W, the r singleton-control atoms therefore have squared masses between delta^2(1-q)^2 and delta^2(1+q)^2. Let m_W be the total mass at b=0,W, including all control frequencies. Then

    m_W >= r delta^2(1-q)^2.

The r singleton terms in the homogeneous conditional entropy contribute at least

    r delta^2(1-q)^2
    *[log_2 r+2log_2((1-q)/(1+q))].                    (2.2)

The bracket is positive for r>=4. Other conditional-entropy terms are nonnegative. There are delta^-1-1 nonzero selector frequencies. Consequently

    B_Z:=H(S_Z | S_x,S_w)
      >= r delta(1-delta)(1-q)^2
         *[log_2 r+2log_2((1-q)/(1+q))].               (2.3)

The exact physical block-restriction identity is Delta_Z H=B_Z+JS_Z, with JS_Z>=0: average restricted squared Fourier coefficients over z to get the marginal squared spectrum on x,w, then apply the entropy chain rule and concavity. Thus (2.3) is also a lower bound for Delta_Z H. No non-Boolean law is introduced.

## 3. Make x the unique largest folded influence without changing the block decrement

Raw selector directions may have larger influence than p when r is large. Replace EVERY w-coordinate by a balanced recursive ternary-majority function of depth d=r+5 on its own fresh disjoint block. Leave x and z unchanged. Call the resulting Boolean function F.

Every majority leaf has influence 2^-d; balanced disjoint substitution preserves the uniform distribution of the outer w bits. Thus (1.2)-(1.4) and the exact support-error probability remain unchanged, while every new selector leaf has influence at most 2^-d<p. The pivot x is now the UNIQUE maximum ordinary influence. For r>=4, p<1/2; hence every influence of F is below 1/2, so F is already in the folded/centered gauge I(F)=J(F).

Balanced disjoint substitution preserves the decrement of any retained PHYSICAL block, not only a singleton. Indeed

    H(F)=H(f)+sum_k I_wk(f) H(g_k),

and the same identity on every z restriction averages to the same added sum because E_z I_wk(f_(Z=z))=I_wk(f). Therefore

    Delta_Z H(F)=Delta_Z H(f).                         (3.1)

On the branch z=0 the remaining function is exactly chi_x, so the pivot's influence one folds to zero. For z!=0 its pivot influence is delta<1/2. Every new selector leaf stays below 1/2 even after restricting z. Hence the ONLY additional folded refund relative to ordinary influence is q, and

    D_Z(F):=J(F)-E_zJ(F_(Z=z))=I_Z(f)+q.               (3.2)

Equations (2.3), (3.1), and (3.2) give

    Delta_Z H(F)/D_Z(F)
      >= [r delta(1-delta)(1-q)^2/(r(q+delta-3qdelta)+q)]
         *[log_2 r+2log_2((1-q)/(1+q))].               (3.3)

For r>=4, q<=1/16, delta<=1/256, and the denominator is at most (21/16)rq. The prefactor in square brackets is at least

    (1/21)*(255/256)*(225/256)>1/25.

Also ((1-q)/(1+q))^2>1/2, since (15/17)^2>1/2. Thus the explicit all-dimensional conclusion is

    boxed{ Delta_Z H(F)/D_Z(F) > (log_2 r-1)/25. }      (3.4)

This tends to infinity. Taking r=2^k makes the lower bound (k-1)/25. These are finite Boolean constructions of large formal dimension, not claims of enumerating those truth tables.

The general substitution facts are derived in REPORT.md, Lemma 6.1. Recursive majority is balanced, with leaf influence 2^-d, total influence A_d=(3/2)^d and entropy 4(A_d-1). This is standard balanced-disjoint composition, not an independent novelty claim.

## 4. The counterfamily itself satisfies a fixed FEI bound

Let alpha=q+(r+1-q)delta. Directly from (1.1), E f=1-alpha. Thus the total nonempty Fourier mass is v=alpha(2-alpha). For r>=32, alpha<=1 and

    r delta<=v<=2delta(r+17).

The raw dimension is n=2r+5. Entropy maximization with fixed empty mass gives

    H(f)<=h_2(v)+v log_2(2^n-1)
         <=v[log_2(e/v)+n]
         <=2delta(r+17)(3r+11).                        (4.1)

Here v>=r delta and log_2 e<2 were used; dropping a negative log_2 r only enlarges the last expression. By (1.6),

    H(f)/I_w(f)<=2(1+17/r)(3+11/r)<11 for r>=32.       (4.2)

If A=(3/2)^d is the total influence of each substituted majority, then

    H(F)=H(f)+4(A-1)I_w(f),
    I(F)=I_(x,Z)(f)+A I_w(f).

Equation (4.2) implies H(F)<11I(F). Therefore (3.4) is emphatically a failure of the proposed local restriction payment, NOT a counterexample to FEI. A different block or a globally refunded strategy could still succeed.

## 5. Consequence for the joint proof programme

The coefficient-12 theorem in ADDENDUM remains valid under support error q/(16r). The tempting replacement by q/16, while keeping only a maximum-influence pivot and a coordinate-subcube approximation, is now rigorously refuted for EVERY universal coefficient, not merely twelve. The same obstruction includes the full folded drift refund D_Z.

This also explains why an approximate-row argument must retain exceptional-set geometry or jointly coordinated rows rather than importing a fixed-relative isoperimetric support approximation and declaring its defining block cheap. The source account04 all-row theorem has additional joint hypotheses and is NOT refuted here. Neither are arbitrary adaptive/existential selectors or the exact-support, low-surplus peeling theorem.

## 6. Executed checks

New check_fixed_relative_obstruction.py materializes the raw r=2,...,7 cases, dimensions 9,11,13,15,17,19 with 512 through 524,288 truth-table entries. Integer Walsh transforms and direct edge counts verify every influence in (1.2)-(1.5), the exact sensitivity-support error, and every nonzero-selector-frequency singleton coefficient in (2.1). It checks the entropy lower bounds and true block decrements as floating diagnostics; those diagnostics are not the proof of the universal inequalities.

The script also directly materializes a six-variable r=2,s=1 outer example after replacing its three selector bits by disjoint three-bit majorities, producing a 12-variable truth table. The retained influences agree exactly; the block-decrement diagnostic discrepancy is 3.2862601528904634e-14. Exact rational comparisons verify the constants 1/25 and the coefficient eleven at r=32. The all-r construction and bounds are proved analytically above.

Actual output is fixed_relative_obstruction_checks.json. All checks passed. This is an additional self-checked derivation after the earlier packages were pushed; no independent review, proof-assistant formalization or publication-priority clearance is claimed. Full FEI remains OPEN / NOT PROVED.
