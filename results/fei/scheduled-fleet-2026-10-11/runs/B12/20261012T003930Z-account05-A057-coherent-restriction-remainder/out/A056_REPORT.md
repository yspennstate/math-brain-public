# A056 stage 2: biased-child erasure and physical entropy decrement

## exact target, quantifiers, hypotheses and units

Extend the adopted A056 composition interface, as directed by B12 STREAM_NOTES v2 (23:30 UTC), to every physical query inside a potentially biased child. Let F=h(g_1,...,g_k), with Boolean sign children on mutually disjoint independent uniform physical blocks. Delete deterministic other children first. Fix child j and a physical coordinate i inside it; the selected child may be biased. Entropies here are **bits**, whereas A057 and the lead's L1 formulas use nats. Write B_i(f)=H(1_{i in S}|S without i) for the squared Fourier law and D_i(f)=H(f)-[H(f_i^+)+H(f_i^-)]/2. D_i denotes entropy decrement, not spectral deficit or the character-centered influence.

This stage supplies exact B_i and D_i splits, their signed empty-pair corrections, and a positive-sector bound valid below the root after actual physical restrictions. It does not establish a universal stopping-tree payment. This is a focused completion of the recentered interface, not a new broad gate-family candidate; B12's review-cap direction is retained.

## sources actually read, revisions and theorem locators

Read BOARD.md snapshot 2026-10-11 23:29 UTC, B12 STREAM_NOTES.md v2 23:30 UTC, and own STATUS.md at stage start. The lead adopts A056's first-stage disjoint identities and directs this biased-child extension. A091 REPORT.md independently accepts A056 v1 at scope by a separate coefficient reconstruction; this review is consumed, not merely inferred from the board. A057 REPORT.md supplies the balanced B/JS split, the paid explicit logarithm, its precise unsupported universal line, and NEXT_HANDOFF's proposed signed biased correction. A057's claims are still pending review; the present derivation independently reconstructs all identities used. EXECUTION_PROTOCOL.json v2 was reread; its required schemas and review cap apply. Local byte hashes of these sources and prior A056 proof/interface are in out/source_manifest.json. Earlier general campaign and paper source pins remain those in the stage-1 manifest; no new whole-manuscript audit or external lookup is claimed.

## complete derivation or exact first unsupported line

### 1. Pair functionals and the exact coordinate identity

Define phi(s)=s log2(1/s) for s>0, phi(0)=0, and

    e(s,t)=phi(s)+phi(t)-phi(s+t),
    d(a,b)=phi(a^2)+phi(b^2)-[phi((a+b)^2)+phi((a-b)^2)]/2,
    j(a,b)=d(a,b)-e(a^2,b^2).

All three relevant functions are homogeneous of degree one in squared amplitudes: e(cs,ct)=c e(s,t), and d(sqrt(c)a,sqrt(c)b)=c d(a,b), likewise j. In particular e(s,t)=(s+t)h2(t/(s+t)), and

    j(a,b)=(a^2+b^2)[1-h2(1/2+ab/(a^2+b^2))] >= 0.             (1)

For a physical Fourier pair a_U=fhat(U), b_U=fhat(U union {i}), where U excludes i,

    B_i(f)=sum_U e(a_U^2,b_U^2),
    D_i(f)=sum_U d(a_U,b_U),
    JS_i(f)=D_i(f)-B_i(f)=sum_U j(a_U,b_U).                       (2)

Indeed restriction replaces the pair by a_U+b_U or a_U-b_U. The average pair mass equals a_U^2+b_U^2, so subtracting the raw entropies proves (2), without normalization or omitted empty pair. Formulas (1)-(2) apply even if a pair has zero mass.

### 2. Recentered outer coefficients and exact biased splits

Write h(y)=A(y_-j)+y_j B(y_-j). Expand A and B in the **normalized product basis of the other child outputs under their current means**, not necessarily under the uniform output law. Let their coefficients be a_T,b_T. For the chosen child, put

    m=E g_j, v=1-m^2, beta=g_jhat({i}), t=beta^2,
    C_T=a_T+m b_T, q=sum_T b_T^2=E[B(Y_-j)^2].

Since h is Boolean, B is 0 or +/-1 and q is its pivotal probability under the other outputs. For v>0 the recentered outer coefficients are C_T and sqrt(v)b_T; its biased spectral j-inclusion is w_j=vq. The physical multiplier is q, including when other children are biased. The actual influence identity is

    Inf_i(F)=q Inf_i(g_j).                                      (3)

Define the positive outer functions

    M(t)=sum_T e(C_T^2,t b_T^2),
    N(t)=sum_T j(C_T,beta b_T).

N depends only on beta^2, since j is even in either amplitude. Define the child's residual sectors, with precisely its empty i-deleted pair removed,

    B_i^*(g_j)=B_i(g_j)-e(m^2,t),
    D_i^*(g_j)=D_i(g_j)-d(m,beta).

Both are nonnegative, as sums of the nonempty U sectors in (2). Then the exact identities are

    B_i(F)=q B_i^*(g_j)+M(t),                                   (4)
    D_i(F)=q D_i^*(g_j)+M(t)+N(t).                              (5)

Equivalently, define signed corrections

    L_m(t)=M(t)-q e(m^2,t),
    K_m(t)=N(t)-q j(m,beta).

Then

    B_i(F)=q B_i(g_j)+L_m(t),
    D_i(F)=q D_i(g_j)+L_m(t)+K_m(t).                            (6)

Proof: for a nonempty selected-child Fourier set U, both coordinate-pair amplitudes have multiplier b_T, times the normalized nonempty spectra of occupied other child blocks. Homogeneity and Parseval on those child laws give q times the corresponding child pair contribution. For U=empty, the no-i amplitude is C_T, while the with-i amplitude is beta b_T. Parseval eliminates the other-block factors, giving M or M+N. The physical union identifies T and each other child's nonempty set, so no two distinct outer terms are squared incoherently. This also proves (3). Signed recentering is carried by C_T=a_T+m b_T throughout.

When m=0, e(m^2,t)=j(m,beta)=0, so (6) reduces to A057's balanced identity. When t=0, M=N=0 and the selected empty pair contributes nothing. When v=0, the child is constant, beta=0, its B/D and every query influence are zero; fix the gate coordinate and do not divide by v. Irrelevant gates have q=0 and all terms vanish. These statements cover every endpoint.

### 3. Positive-sector envelope valid at biased descendants

For v>0, Parseval gives 0<=t<=v. As a function of s>=0, M(s) is nonnegative, nondecreasing, concave, and M(0)=0. Each e(C^2,s b^2) has derivative b^2 log2(1+C^2/(s b^2)) when s b^2>0; its second derivative is nonpositive, with zero-amplitude cases handled by continuity. At s=v,

    M(v)=B_j^mu(h),                                            (7)

where B_j^mu means coordinate erasure of the **normalized biased outer squared spectrum**. This is a spectral conditional entropy, not the erasure under a uniform outer law and not a pivotal probability.

Set theta=t/v. Concavity of phi yields, term by term,

    M(t) <= theta M(v)+q t log2(v/t),
    M(t) <= M(v).

Thus, with t log(v/t)=0 when t=0,

    M(t) <= min{B_j^mu(h),
                 (t/v) B_j^mu(h)+q t log2(v/t)}.                (8)

To check the first inequality explicitly, phi(C^2+theta v b^2)>=(1-theta)phi(C^2)+theta phi(C^2+v b^2), while phi(theta v b^2)=theta phi(v b^2)+theta v b^2 log2(1/theta). Sum the resulting e inequality. No positivity of the signed L_m or K_m is assumed; the envelope applies to M.

The one-bit logarithmic Sobolev inequality gives

    0<=N(t)<= (2/ln 2) sum_T min(C_T^2,t b_T^2)
             <= (2/ln 2)q t.                                  (9)

Here is a self-contained scalar proof of the inequality used. For x>=y>=0, Ent_uniform((x^2,y^2)) in nats is at most (x-y)^2/2. By homogeneity take y=1. The difference F(x) between this upper bound and the entropy satisfies F(1)=F'(1)=F''(1)=0 and F'''(x)=2(x^2-1)/(x(x^2+1)^2)>=0; integrate three times for x>=1. The y=0 endpoint follows by continuity. Apply it to x=|a+b|, y=|a-b| (interchange if needed); their squared difference is 4 min(a^2,b^2). Division by ln2 proves j(a,b)<=2 min(a^2,b^2)/ln2. This proves (9), independently of an unreviewed imported estimate.

Combining (5),(8),(9) gives the exact positive-sector interface with the outer logarithmic remainder retained. In particular D_i(F) is bounded by q D_i^*(g_j) plus the right-hand side of (8) plus (2/ln2)qt.

### 4. What is paid once in a physical stopping tree

The Boolean derivative takes values 0,+/-1, so |beta|=|E D_i g_j|<=E[(D_i g_j)^2]=Inf_i(g_j). Since v<=1,

    q t log2(v/t) <= q t log2(1/t)
                   <= [2/(e ln2)] q |beta|
                   <= [2/(e ln2)] Inf_i(F).                    (10)

The scalar middle bound maximizes u ln(1/u) at u=1/e. Also qt<=Inf_i(F), so (9) costs at most (2/ln2)Inf_i(F). At every node of an adaptive **physical** restriction tree, the remaining blocks stay disjoint and the unrevealed physical signs stay independent uniform; recompute all child means and the current other-output basis. Therefore these two components have cumulative expected price at most

    [(2+2/e)/ln2] [I(root)-E I(leaf)].                          (11)

This uses the physical-query influence telescope once. It does not recharge a whole-subformula bank at each depth. Formula (11) pays only the explicit logarithm and outer JS component; it does not pay q D_i^*(child), the capped biased outer-erasure terms, or terminal entropy.

### 5. Restriction control and a signed-correction obstruction

For the required AND2(Maj3(x,a,b),z) control, first fix x=+1. The selected child is OR2(a,b) with m=1/2, v=3/4, beta=1/2 at either a or b. The other child is a fresh dictator. The recentered gate has C_empty=-1/4, C_{z}=3/4 and b_empty=b_{z}=1/2, so q=1/2. Equations (4)-(6) retain the child's nonzero empty pair e(1/4,1/4)=1/2 and d(1/2,1/2)=1. Its full B_i is 1 and D_i is 2, hence B_i^*=1/2 and D_i^*=1. Independently restricting a gives a dictator z at a=+1 (H=0), and AND2(b,z) at a=-1 (H=2). Thus

    D_a(F)=H(F)-1=3-(9/8)log2(3),
    Inf_a(F)=1/4,
    B_a(F)=1/4+M(1/4).

The exact coefficients and prime-log vectors are saved in out/checks.json. The total influence of this restricted F remains 5/4, as adopted in stage 1.

Signed corrections need not be nonnegative at biased descendants. Take h=AND2 and both children OR2 on disjoint two-bit blocks. For a selected coordinate of the first child, m=1/2, beta=1/2, q=3/4; the other child has mean 1/2 and variance 3/4. The signed erasure correction is

    L_m(1/4)= 1/4-(9/8)log2(3)+(5/8)log2(5)<0.                (12)

Indeed (12) is negative exactly when 4*5^5<3^9 (12500<19683), an integer comparison. The same fixture has K_m(1/4)=5/4-(5/8)log2(5)=(5/8)log2(4/5)<0, certified simply by 4<5. This directly prevents silently applying the balanced nonnegative-L/JS bank to biased children. The positive M,N envelope remains valid. The finite census records 512 negative L and 512 negative K cases; their exact signs use integer products, never decimals. These are scope controls inside the same interface extension, not additional broad candidate claims.

### 6. Honest first unsupported line

For a represented physical stopping tree, the unproved universal line is a dimension-independent bound on

    E H(leaf) + E sum_visited [q_v D_{i_v}^*(g_{v,j_v})
                 + min{B_{j_v}^{mu_v}(h_v),
                       (beta_v^2/v_v) B_{j_v}^{mu_v}(h_v)}]

by K I(root), with any legitimate allocation of the paid logarithmic terms and without repeatedly spending the same influence or dropping the negative empty-sector credit. Our estimates justify such a residual target but do not prove it. The displayed min is the smaller gate-only part after applying the two alternative bounds; a proof must couple that choice with the associated logarithmic bill. Using min of gate parts and paying the logarithm regardless is a valid upper bound. Arbitrary terminal child entropy remains present, so admission of an arbitrary hard core has not been bypassed.

## executed validation with domain, arithmetic, commands and outputs

out/FROZEN_SPEC.json was saved before search. code/check.py uses exact Fraction Fourier amplitudes, raw entropy vectors in rational prime-log coefficients, and denominator-cleared integer-product sign comparisons. It reconstructs D independently from actual truth-table restrictions as well as pair amplitudes. Domain: all 16 two-input gates and all 16^2 pairs of two-bit Boolean children on disjoint blocks, all four physical coordinates (16,384 splits), plus four named control splits. Constants are included as endpoint cases; no symmetry reduction or dimension escalation. A pilot and main execution are recorded in out/pilot.json and out/checks.json, with measured computation runtime. Command: python -X utf8 code/check.py --pilot, then python -X utf8 code/check.py, using the full path from the A056 workspace.

The finite inequalities use the weaker exact rational constant 4 for N<=4qt; the analytic proof establishes the sharper 2/ln2. Pilot: 64 physical splits passed in 0.0756476 seconds. Main: all 16,384 physical splits and four fixtures passed in 18.7090997 seconds, with 512 negative L and 512 negative K cases. The all-dimensional claims are supplied by the above proof, not by enumeration. All memory estimates are below 300 MB; no heavy job or memory-gate override was used. Exact counts, negative-correction witnesses and final outcomes are those in checks.json, not inferred from planned coverage.

## proof dependencies and changed downstream conclusions

Consumes A056-DISJOINT-COMPOSITION v1 and A091's independent acceptance at scope; the balanced A057 source is a comparison interface, with its review status still pending. All new pair identities and bounds are independently derived above. The signed witness repairs a tempting biased extension, not A057's correctly scoped balanced theorem. A057 can now formulate its stopping-tree payment at biased descendants with q B_i^*/q D_i^* and current mu-gate erasure. A059 must retain these empty-pair credits at biased stopping frontiers. A060 can optimize the biased envelope without assuming L_m>=0. The logarithm and JS components preserve the same once-per-query influence payment below the root.

## one next mathematical action and independent reviewer

Next: A057/A059 test the residual gate term and removed empty-sector credit on one source-pinned sparse-bent physical stopping tree, alongside its actual terminal reserve; use this recentered split at every reached branch. Independent reviewer A091, alternate A090, should reconstruct the U=empty sector and use an independent physical-child calculation on AND2(OR2,OR2). The lead's A057 review-first ordering remains in force; no independent acceptance of this extension is claimed.

## actual persistence receipts or precise save blocker

All stage artifacts and code/out files are written only inside agents/A056/runs/20261011T233147Z-account05-A056-balanced-composition; rolling STATUS.md, WORKLOG.md and LEARNED.md are updated in A056. out/receipts.json supplies final local hashes and sizes. Protocol schema and certificate checks are saved after completion. No shared registry, other agent folder, brain, repository or external message was modified. Local persistence, independent review, supervisor copy and downstream use are distinguished; the last three are pending.

## Universal bridge

This stage moves the lead-named biased-descendant transport interface for C019 stopping-tree payment, and secondarily C018 erasure: it replaces the balanced-only split by exact recentered B_i/D_i identities at every disjoint physical branch, preserves signed empty-sector credits, and extends the influence-paid logarithm plus JS bill with unchanged constant (2+2/e)/ln2. It pays zero additional units of the still-unbounded gate-erasure/inner-decrement/terminal reserve; that residual remains the first unsupported line. NEXT is to test and then amortize that exact residual on the sparse-bent tree using actual branch means, which attacks the missing universal payment directly rather than spending another stage on a separate easy formula class.
