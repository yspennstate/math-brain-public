# A036: normalized occupancy reference through a biased rare-core history

Full FEI remains OPEN. This is a scoped reference-transfer closure, not a new entropy bound for point defects. It consumes the live A039 continuation request and preserves all source, outcome and terminal accounts.

## exact target, quantifiers, hypotheses and units

For every integer n>=2 let v_n(z)=1-2*1[z=0] on n independent fair data bits, delta=2^-n, N=n+1. The reached Boolean fixture is F(x,a,b,z)=-1 when x=0,a=1; v_n(z) when x=1,b=1; +1 otherwise. This is A039's actual reached root after the essential u0=0 query; no costs before that reached root are newly paid here. Query a, then one original data coordinate in each branch, stopping with all four physical leaves. Permuting the data bits makes all n^2 adaptive labelled choices equivalent for this core and this reference. No equivalence for general cores is asserted.

P is the squared Fourier law. Write e=P(empty)=(1-delta)^2/4 and zeta=1-e (code uses z for zeta). Complete the nonempty maximum-entropy occupancy reference by M(empty)=e, M(S)=zeta Q_r(S) for S nonempty, r_i=Inf_i/zeta. This M is an explicit normalized law, with the positive-root normalizer retained below. It is distinct from the product reference R=prod Ber(Inf_i). Campaign marginal entropy is sum h2(Inf_i); campaign B is erasure. All logarithms, entropies and divergences are in bits.

Transport this SAME inherited M by erasing each queried Fourier indicator and using the physical common kernel k(y|T)=P_y(T)/(2q(T)), q=(P_0+P_1)/2. On q=0 use k=1/2; propagate every reference row. Do not replace the reference at the intermediate frontier. Let A=D(P||M), E_tot the weighted conditional-erasure KL, O_tot the weighted outcome KL, K_end the mean inherited terminal KL, and TC_end the mean KL to each terminal's actual product projection. The named final conversion excess is

    D_end = TC_end-K_end-E_tot = O_tot+TC_end-A.

Result: D_end<0 for ALL n>=2. More quantitatively D_end<-N*delta/8 for n>=16, and D_end/(N*delta)->-1/2. No terminal surplus withdrawal is needed for this one conversion. The exact terminal entropy and influence are retained; the result does not pay arbitrary incoming debts or prove a universal reference-payment rule.

## sources actually read, revisions and theorem locators

Execution protocol read in full: fei-execution-protocol/2, revision 2026-10-11-execution-v2. BOARD.md snapshot 2026-10-14 08:31UTC read, including all stream updates; B08 STREAM_NOTES.md v2, 2026-10-11 23:35Z, and own STATUS/LEARNED/WORKLOG. Earlier A036 completed stages 1 and 2 were used as context only. Three intervening directories contain only supervisor .final markers, with no reports or proofs; neither these markers nor board stage counts establish mathematical work. Those directories remain untouched.

Read A037 REPORT.md, run 20261014T043944Z-fleet05-A037-conditional-credit-ledger, Sections 1-5: terminal-inclusive bent ledger and all-rarity cancellation. That closes the saved disjoint-control baseline, so this stage does not repeat it. Read A039 REPORT.md, PROOF.md and code/mixed.py, run 20261014T055326Z-fleet05-A039-projection-under-restrictions, especially final-frontier account (1), finite non-flat interface and NEXT biased rare-core continuation. Read A038 PROOF.md, run 20261014T051947Z-fleet05-A038-occupancy-term-audit, Sections 1-4: parity requires an actual unused terminal owner. All are source-hashed in out/SOURCES_READ.json. No external paper theorem is used as a premise; previously read campaign/paper context is not advertised as a newly audited source.

This follows the lead's notation and no-reuse direction. Its older A036 finite-family task was completed in stage 2; the board and the live A039 dependency supply the next unfinished target. No claim of independent acceptance for A036's previous or current results is made.

## complete derivation or exact first unsupported line

### 1. Actual signed spectra and retained terminals

The root marginals are Inf_x=Inf_a=1/2 and Inf_b=Inf_j=delta/2 for each data j. Its nonzero squared coefficients are two atoms 1/4, two atoms e, and 2^(n+2)-2 atoms delta^2/4. Root Fourier coefficients outside these sectors are zero; M puts reference mass there, and this is retained in A. Defining phi(t)=-t log2 t,

    H(F)=1+2phi(e)+(delta-delta^2/2)(2n+2).

At a=0 the child is the (n+2)-bit point defect on the event x=1,b=1,z=0. The a=1 child has the same squared law translated in the x Fourier indicator. After querying one data bit, two final laws are constant and x-character (entropy zero, influences 0 and 1), and the other two are x-translated versions of the (n+1)-bit point-defect law. Its entropy is

    H_pt=phi((1-delta)^2)+(2delta-delta^2)*2n.

Therefore, with all four reach weights 1/4,

    H_end=H_pt/2,
    I_end=1/2+n*delta/2,
    TC_end=N*h2(delta)/2-H_pt/2,
    H(F)-H_end=2.                                      (2)

The last identity is exact: phi(4e)=4phi(e)-8e cancels all logarithms and all n terms. The inactive character leaf contributes influence 1/4 to the expectation; omitting it gave an initial validation failure, repaired and recorded in out/VALIDATION_REPAIRS.md. No certificate from that failed pilot is adopted.

### 2. Root normalizer, maximum entropy and compatible transport

Let c be the unique positive solution

    1-c=(1-c/(2zeta))^2(1-c*delta/(2zeta))^N.            (3)

Put u=c/(2zeta), t=delta*u. Q_r is the product of two Ber(u) and N Ber(t) bits conditioned on being nonempty; conditioning mass is c. Its conditional marginals are r, so M has the actual root marginals and mass e at empty. Positivity follows since all r_i are interior. The function g(c)=1-c-product(1-cr_i) has g'(0)>0, g(1)<0 and g''(c)<0 on (0,1), giving uniqueness of its positive crossing. The finite code checks separated rational signs at every final root bracket.

For the conditional law, log Q_r(S) is affine in the indicators plus a constant on nonempty S. Every feasible occupancy law has the same expectation of log Q_r. KL nonnegativity thus proves maximum entropy, with no unsupported projection theorem. The complete reference entropy is

    H_M=h2(zeta)+(zeta/c)[2h2(u)+N*h2(t)-h2(c)],
    A=H_M-H(F).                                        (4)

The latter follows from the same moment matching, retaining empty mass and all normalizers. It is checked against directly summed D(P||M) and H(M) in the finite truth-table implementation.

For a single physical query, two KL chain rules under the common kernel give

    D(P||Q)=E+O+mean_y D(P_y||Q_y).

This follows first by conditioning the erased indicator and then by adjoining the common outcome kernel. O=D(fair||Q_Y), Q_y(T)=Q_erased(T)k(y|T)/Q_Y(y). Hence, across this two-query history,

    A=E_tot+O_tot+K_end,
    sigma_end=TC_end-K_end,
    D_end=sigma_end-E_tot=O_tot+TC_end-A.                (5)

No root account is renewed; E_tot is not spent both before and after conversion. The declarations on source-zero fibers are fixed. In this family the erased source laws are positive everywhere at all three queried nodes, proved by the point-defect spectra and independently checked for n2..7. This special fact is not generalized to other cores.

### 3. A feasible law supplies a real reference saving

Set r_x=r_a=1/(2zeta). Select the control pair {x},{a},{x,a} with probabilities 1-r_x,1-r_x,2r_x-1, independently of N Ber(delta/(2zeta)) remaining bits. This law is nonempty and has all the required conditional marginals. Complete it with empty mass e. Its four control-pattern probabilities are e,1/2-e,1/2-e,e, so its completed entropy is

    H_feas=1+h2(2e)+zeta*N*h2(delta/(2zeta)).

Maximum entropy gives H_M>=H_feas; this comparison is only a variational lower bound for the fixed inherited reference, not a reset to the feasible law. With (2)-(5),

    D_end <= O_tot+1-h2(2e)
                     +N[h2(delta)/2-zeta*h2(delta/(2zeta))].

Write h2(s)=s log2(1/s)+s log2(euler_e)-R(s), where

    R(s)=log2(euler_e)*sum_(k>=2) s^k/[k(k-1)].

R(s)/s is increasing. Since delta/(2zeta)<=delta, the bracketed reference saving satisfies

    zeta*h2(delta/(2zeta))-h2(delta)/2
      >= (delta/2)log2(2zeta) > delta/4,                 (6)

because 2zeta>=3/2>sqrt(2), certified by 9>8. No asymptotic inference is used for this inequality.

### 4. Exact outcomes and the all-dimensional bound

Here are the transported outcome normalizers, including all reference mass. Put w=(1-t)^N,

    E=e+(1-u)w/2, X=w/2,
    k=(1-delta/2)^2/[(1-delta/2)^2+delta^2/4],
    q0=1/2+(k-1/2)(E-X), q1=1-q0,
    B0=(delta/2)(1-u)(1-t)^(N-1),
    B1=(t/2)(1-t)^(N-1).

After the first a query and subsequent data erasure, the respective heavy residual reference atoms have masses

    L0=(kE+B0/2)/q0, L1=(kX+B1/2)/q1.

Let kappa=(1-delta)^2/[1+(1-delta)^2]. Each second-query active outcome probability is p_y=1-(1-kappa)L_y. All other residual atoms go to the active outcome with probability one. Thus

    o(q)=-log2(4q(1-q))/2,
    O_tot=o(q0)+[o(p0)+o(p1)]/2.                        (7)

These formulas are independently reconstructed against full reference arrays for n2..7, then used for exact finite bases n8..15 without constructing enormous tables.

For n>=16, N*delta<=17/65536; N*2^-n decreases thereafter. The positive root in u solves G(u)=1-2zeta*u-(1-u)^2(1-delta*u)^N=0. We have G(2/5)>0, u<1/(2zeta)<=2/3. On [2/5,2/3],

    G'(u)<=-3/2+6/5+(9/25)N*delta < -1/4.

Indeed zeta>=3/4 and the two nonnegative product derivative terms are bounded separately. Also |G(1/2)|<=delta/2+N*delta/8. The mean value theorem gives

    |u-1/2| <= (N+4)delta/2,
    1-w <= 2N*delta/3.

Consequently |q0-1/2|<=N*delta/2: use E-X=e-u*w/2, |e-1/4|<=delta/2, and the preceding two estimates. Further

    E>=1/2-(9N/20+3/2)delta>=1/2-N*delta,
    X>=1/2-N*delta,
    k>=1-delta^2.

Both L_y are at least (1/2-2N*delta)/(1/2+N*delta/2)>=1-5N*delta. They are probabilities in [0,1]. Since |kappa-1/2|<=delta, this implies |p_y-1/2|<=6N*delta. All deviations are <=1/10. For |q-1/2|=s<=1/10,

    o(q)<=2*log2(euler_e)*s^2/(1-4s^2)<=4s^2,

using log2(euler_e)<3/2. Hence O_tot<=145*N^2*delta^2. For the reverse fair-law divergence, the second derivative of 1-h2(1/2-s) is 4*log2(euler_e)/(1-4s^2); integrating twice from zero gives the same upper bound 2*log2(euler_e)*s^2/(1-4s^2). Thus 1-h2(2e)<=4delta^2: its deviation from 1/2 is delta-delta^2/2. Applying (6),

    D_end <=150*N^2*delta^2-N*delta/4
          <-N*delta/8, n>=16.                          (8)

The final strict comparison is 1200*17<65536, with monotonic N*delta. This is a genuine all-n bound, not extrapolation from the finite bases. All n2..15 have strictly negative rational upper certificates in out/FORMULA_CHECK.json. Thus D_end<0 for every n>=2.

### 5. Normalized asymptotic price and separate recovery implication

Let R_root be the actual product-marginal law. Because M matches its marginals, Delta=D(M||R_root)=M_root-H_M, with M_root=2+N*h2(delta/2). For nonempty S with k selected controls and l selected remaining bits,

    M(S)/R_root(S) = (1/(2u))*(2u)^k*[2(1-u)]^(2-k)
                   *(2u)^l*[(1-delta*u)/(1-delta/2)]^(N-l).

At empty the ratio is e/[(1/4)(1-delta/2)^N]. Since |u-1/2|=O(N*delta), every such ratio is 1+O(N^2*delta), uniformly in S; expand logarithms on a fixed neighborhood of one and exponentiate, since N^2*delta->0. All ratio factors and the prefactor are displayed, so no support or normalization term is hidden. The elementary log bound KL<=log2(euler_e)*chi-square gives Delta=O(N^4*delta^2)=o(N*delta).

Equations (2),(4),(5) now give exactly

    D_end=O_tot+Delta+N[h2(delta)/2-h2(delta/2)].

O_tot=O(N^2*delta^2), while h2(delta)/2-h2(delta/2)=-delta/2+O(delta^2). Therefore D_end/(N*delta)->-1/2. This is a quantitative normalized divergence-payment margin for the named conversion excess, using a completed occupancy reference; it is distinct from collision T and does not reintroduce raw L.

The recovery implication needed by a downstream reference ledger is proved separately from negativity: from (5), D_end<=0 implies sigma_end<=E_tot, equivalently O_tot+TC_end<=A. Adding the SAME full H_end yields

    O_tot+TC_end+H_end <= A+H_end.

This retains all terminal bills; the final conversion is paid by the single original source account with its erasure release, and no final child surplus is withdrawn. The inherited K_end is the debt being converted, not an additional reserve. None of these inequalities pays H_end universally by influence or licenses treating KL as a new entropy-payment bank.

### 6. Exact first unsupported line

For an arbitrary non-flat core, the root feasible law still exists, but identity H(root)-H_end=2, the heavy-atom kernel, and the negative saving domination need not hold. The first unsupported universal line is: choose an actual mixed policy with O_tot+TC_end-A and the other incoming owned debts paid by previously unused source/child accounts while retaining every terminal reference bill. Priority-separator costs preceding this reached root remain separately owned. This stage neither assumes universal 4I-H>=0 nor spends a renewed occupancy projection. The shortest continuation is a core whose two data children are both nonconstant and unequal, where the exact entropy decrement changes and the same source reference must still be retained.

## executed validation with domain, arithmetic, commands and outputs

Both frozen specs were written before their respective computations: out/FROZEN_SPEC.json and out/FROZEN_FORMULA_SPEC.json. From A036 workspace:

    python -X utf8 -B runs\20261014T083156Z-fleet05-A036-reference-law-divergence\code\check.py --pilot
    python -X utf8 -B runs\20261014T083156Z-fleet05-A036-reference-law-divergence\code\check.py
    python -X utf8 -B runs\20261014T083156Z-fleet05-A036-reference-law-divergence\code\formula.py

Final enriched pilot n2: 1,145 checks, 0.332seconds. Full truth-table/ref-array run n2..7: 34,443 checks, 3.965seconds. It independently compares Walsh influences with physical differences, root entropy with the explicit atom list, reference entropy and direct KL with (4), reference normalizers/marginals, each direct conditional KL chain, global inherited terminal KL, signed reset and retained entropy/influence/TC formulas. The two final KL calculations enclose the same analytic identity; interval overlap alone is not claimed as a proof.

Compressed finite bases n2..15: 1,167 checks, 0.439seconds in the final recorded run, with every D_end upper endpoint negative and exact derivative/entropy constants checked. n2..7 are independent representation cross-checks against the full arrays, not independent external review. Reruns after enriching the array checker are recorded by the persistence tool. No automatic dimension escalation occurred; n8..15 were separately frozen as formula-only bases. Every positive-root bracket uses 60 exact rational bisections. Logarithms reduce to [1,2], then use 24 terms of 2 sum a^(2j+1)/(2j+1), with a=(x-1)/(x+1)<=1/3 and tail <=2a^49/[49(1-a^2)]. Division by the positive ln2 enclosure and directed 2^-110 rounding preserves outward bounds. Strict signs use separated rational endpoints, never decimals.

Estimated memory <=60MB for full arrays and <=10MB for formulas; no job expected above300MB and no memok trigger. All observed jobs were below60seconds, no GPU or background process. out/CHECK.json and out/FORMULA_CHECK.json preserve rational certificates and runtime/check counts. The pilot correction is saved, not concealed.

## proof dependencies and changed downstream conclusions

Proof dependencies: none external. Common-kernel KL accounting is independently rederived and credited to A039/B08. No parity estimate or unreviewed universal source payment is assumed. This registers one scoped application/repair, within the existing review queue rather than another broad FEI candidate. A037's disjoint-control ledger supplied the reason to move to this mixed query; its results are not proof premises.

A039/A038/A064/A047 now have an all-dimensional biased non-flat rare-core continuation where final conversion is covered entirely by the original reference account, with quantitative negative margin and explicit outcome normalizers. This differs from the parity branch, where positive debit grows and a child bank is necessary. The source-bound distinction prevents silently importing the parity withdrawal or spending terminal surplus in the rare case. Independent external reconstruction is pending; mirror/shared registry adoption and downstream use have not been observed.

## one next mathematical action and independent reviewer

Next: replace the point-event core by a certified unequal non-flat core with two nonconstant physical data children, retain the SAME incoming M through the identical history, and test the signed excess against measured entropy decrement and one genuinely unused source/child owner. A039 can consume the formulas; A088/A094 should independently reconstruct the all-n outcome bounds and variational comparison. No outbound messages were sent.

## actual persistence receipts or precise save blocker

All four protocol files, code and rational outputs are inside this run. STATUS.md, WORKLOG.md and LEARNED.md are current. out/PERSISTENCE_RECEIPTS.json records local SHA256/bytes and checks the exact field schemas and identical PROGRESS/PACKET_DELTA. out/SOURCES_READ.json pins actually read source artifacts. No save blocker; supervisor copying, public mirrors, brain ingestion, shared adoption and independent review are unverified.

Universal bridge: This advances C024 history transfer and its C019 stopping-frontier interface by closing the SAME-reference two-query conversion on every biased rare point-defect core n>=2, with D_end<-(n+1)2^-n/8 for n>=16 and normalized margin tending to -1/2; no child-surplus withdrawal occurs and all four terminal entropy/influence/KL bills remain explicit. The universal bridge still lacks an eligible arbitrary-core policy and a nonreusing payment for other incoming debts with full terminals. NEXT changes the actual two-child entropy/profile rather than proving another point-defect FEI bound: an unequal nonconstant-child query is the nearest place where the exact two-bit entropy release and reference-outcome domination can fail, so pricing that same source account tests the missing universal induction step directly.
