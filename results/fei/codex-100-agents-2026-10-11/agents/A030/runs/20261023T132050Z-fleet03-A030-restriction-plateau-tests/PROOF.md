# External controller and source envelopes through mixed stopping histories

Author reconstruction, not independent acceptance. Uniform physical cubes, normalized real Walsh coefficients, all information in bits. Full FEI is OPEN.

## 1. One inherited account, including disappearing labels

Let F(y,x)=g_{L(y)}(x), with ell>=1 labels and independent uniform control/data cubes. Sources are arbitrary Boolean functions on the SAME data cube. Put C_j=1_{L=j}, c_j=hat C_j, b_j=hat g_j, and pi_j=E C_j. Supply normalized controller references A_j and source references R_j, and finite nonnegative mu_j and positive lambda_j, such that pointwise

    c_j(U)^2 <= mu_j A_j(U),   b_j(t)^2 <= lambda_j R_j(t).       (1)

Initially zero-probability labels may have mu_j=0; retain every label and every reference-only row. These are explicit domination hypotheses, not an entropy-price supplier. Controller references are full spectra of the indicator, INCLUDING its empty coefficient; they are not references for a +/-1 controller with its constant row discarded.

For a physical CONTROL query transport CURRENT A_j through the actual phase-pair channel of c_j. For a pair a,b its two branch probabilities are (a+(-1)^s b)^2/[2(a^2+b^2)], fair when a=b=0. If the transported reference branch mass is rho_j,s, set

    mu_j,s=2 rho_j,s mu_j,  A_j,s=transported branch/rho_j,s.     (2)

When rho=0, set mu_child=0 and choose any normalized A_child: domination forces this child's C_j to be identically zero. No division by pi_child is made. Keep R_j,lambda_j unchanged. The actual restricted indicator coefficients are a+(-1)^s b, even though the indicator's squared norm pi_j is not generally one. Thus (1) propagates by positivity of the channel and the factor2 in (2). In particular mu_child>=pi_child. Both actual outcomes are fair physical outcomes, not distributed according to rho.

For a physical DATA query use the same construction on EACH actual Boolean source b_j and CURRENT R_j, setting lambda_j,s=2 rho_j,s lambda_j, while A_j,mu_j stay fixed. Here rho>0 because each Boolean source child has norm1 and (1) holds. Hence lambda_j,s>=1. This proves (1) at every mixed history, including extinct labels and constant source children. Extinct-label reference mass is retained and transported; it is not dropped to obtain a smaller account.

Define a_j=mu_j lambda_j. For EVERY physical query and every j, average_s a_j,s=a_j. Therefore, for any fixed strictly positive prior theta summing to1,

    M_theta=sum_j a_j/theta_j                                  (3)

is a nonnegative harmonic process under arbitrary adaptive physical queries. It is inherited from the ORIGINAL data, never recomputed as a fresh minimal domination constant.

## 2. A genuinely external complete output reference

At every history prescribe the full normalized reference

    Q_theta(U,t)=sum_j theta_j A_j(U) R_j(t).                    (4)

Weighted Cauchy and (1) give

    P_F(U,t)=(sum_j c_j(U)b_j(t))^2
       <= (sum_j a_j/theta_j) sum_j theta_j A_j(U)R_j(t)
       = M_theta Q_theta(U,t).                                 (5)

One way to check the zero cases is to omit each zero A_j R_j term: its true c_j b_j vanishes. No reference-only rows are erased. Consequently D(P_F||Q_theta)<=log2 M_theta. Since P_F and Q_theta are normalized, M_theta>=1. At EVERY finite adaptive stopping frontier,

    E D(P_leaf||Q_leaf) <= E log2 M_leaf <= log2 M_root.         (6)

This follows from harmonicity and concavity of log, not from a bound on every realized child M. Terminal Q can change both controller shapes/odds and data-row marginals. It need not belong to the conditional-label-channel image in A028@9.

The root prior can be optimized: inf_theta M_theta=(sum_j sqrt(a_j))^2, by Cauchy, attained at theta_j proportional to sqrt(a_j) when all a_j>0. For zero a_j this is an infimum over strictly positive priors; allowing zero prior on zero-envelope labels attains it. This is an optional root choice, not a new child optimization needed in (6). More generally choosing the optimizing prior at each child and omitting zero-envelope labels gives W=(sum sqrt(a_j))^2, a concave function of the nonnegative vector a; each cross term sqrt(a_i a_j) is concave. Thus W is a supermartingale and yields the analogous log W_root bound for those optimized targets. W>=1 follows again from normalization and pointwise domination. This optional improvement is not needed for the rate4 corollary below, and arbitrary switching with Qinc is asserted only for the UNIFORM-prior account.

Use UNIFORM theta for compatibility with earlier Qinc targets. Then M=ell sum_j mu_j lambda_j >=ell sum_j pi_j=ell. Hence BOTH (4) and the earlier CURRENT Qinc=sum_j c_j^2 b_j^2 satisfy D(P||Q)<=log M. At each history one may choose either prescribed target, by any declared adaptive rule. This includes any already-paid Qinc prefix followed by an external installation at a stopping frontier and further mixed queries/switches. The latent envelopes have been transported from the ORIGINAL root in all cases; they are never initialized for free at that frontier.

## 3. Full signed history and all terminal costs

Write d_v=D(P_v||Q_v) for whichever allowed target is current. Transport CURRENT OUTPUT Q_v through the OUTPUT's own phase channel, not the label/source channels, to obtain inherited children with KL e_s. Let E_v,O_v>=0 denote its actual erasure and reference-outcome KL refunds. Chain rule gives

    d_v=average_s e_s+E_v+O_v.

The raw target-replacement charge is kappa_v=average_s(d_child-e_s). Thus its signed net charge is

    sigma_v=kappa_v-E_v-O_v=average_s d_child-d_v.               (7)

Both full child CE costs remain. No positive clipping, renewed descendant bank, or omission of internal refunds is allowed. On every finite adaptive tree,

    sum_v reach_v DeltaH_v + E_leaf CE(P_leaf,Q_leaf)
       =H_root+E_leaf d_leaf <=H_root+log2 M_root.               (8)

Equivalently d_root+sum reach sigma=E d_leaf. Prior raw conversions/refunds are this same history's exact expansion, not charges added a second time to (8). An original quota U and an actual old unrelated debit b suffice if U-b>=H_root+log M_root. This admission is a hypothesis in the universal theorem.

## 4. Supplied external targets paid by the SAME tagged-bent original quota

Use exactly A030-THREE-STATE-BOOLEAN-CUT-RESERVE@5 section3: even r>=4, epsilon=2^-r, bent controller with the one rare relabel, and private sources a*PD2, Maj3, b*PD2. All three labels have positive root probability. Its already proved bounds are

    I_root>=r/4+27/16,    H_root<=r+3+log2 3.

Set delta=1/64. At the ORIGINAL root supply genuinely external complete references

    A_j=(63/64) c_j^2/pi_j +(1/64) Uniform(all control sets),
    R_j=(63/64) b_j^2      +(1/64) Uniform(all data sets),
    mu_j=(64/63)pi_j,  lambda_j=64/63, theta_j=1/3.             (9)

These are explicit distributions, not only an existence assertion. They satisfy (1). They change controller and data profiles and keep off-true mass. Their CURRENT descendants are (2), not re-smoothed copies of the child's true spectrum. At the root M_root=3(64/63)^2.

Keep the SAME original U=4I_root and old debit b=1/4, including ANY earlier Qinc installations and all actual previous releases. At every mixed adaptive frontier, choosing Qinc or (4) on each leaf, (8) gives

    U-b-full_cost >=7/2-2log2 3-2log2(64/63) >3/16.           (10)

Exact integer certificates: 3^8=6561<8192=2^13 implies log2 3<13/8, and 64^32<2*63^32 implies log2(64/63)<1/32. Substitution yields the strict3/16 bound. No local depth, rarity or child-FEI premise is used; r remains arbitrary even>=4. In particular a real external-controller/source installation after the old paid DATA prefix is now funded, and further CURRENT-target queries/resets are also funded. This strengthens @5's source-only conditional interface and closes its specified external-controller handoff for this already funded family.

## 5. Why this differs from free conditional-channel conversion

Take one fair control y and one data bit z, g0=z, g1=-z. Exact indicator references A0=A1=Uniform(two control sets), exact source references R0=R1=point mass at {z}, mu0=mu1=1/2, lambda0=lambda1=1, theta=(1/2,1/2). Then F is parity yz, its spectrum is a point mass, while Q_theta splits mass equally between the empty and nonempty control rows. Thus D(P||Q_theta)=1=log2 M_root, M_root=2.

Here A028@9's source posterior alpha equals rho and its W=0, so its admissible conditional-channel image contains only the true profile at the positive data row. Our target is outside that image and is paid by a REAL one-bit envelope liability. This does not refute A028@9 or give it free capacity; it identifies a different sufficient supplier. It also shows a label-coherence cost can survive when every individual reference is exact. A cost-zero claim would be false on this Boolean example.

## 6. Exact first unsupported universal line

For arbitrary Boolean inputs there is still no influence-priced initial supplier U-b>=H_root+log M_root (or a substitute that pays every full terminal without assuming H_root). The ell=1 case contains an arbitrary source and hence its H_root term already contains full FEI. The universal theorem proved here is conditional reference transport; the unconditional rate4 payment is only for the explicitly admitted tagged-bent family. A028@9 is a comparison, not a proof dependency. Independent external review of this author proof remains pending.
