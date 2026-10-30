# Per-set witness transport through physical restrictions

All information is in bits. The universal statements below concern finite Boolean uniform-cube restriction trees and supplied normalized spectral references. They do not supply a universal initial reference price and do not prove FEI. This continues the corrected original-set witness from A056 v8 rather than the refuted influence-normalized witness.

## 1. Original-set lift and its precise price

Let P(S)=fhat(S)^2 and let R be normalized, support P, and have empty mass P(empty). For nonempty S choose a mark l uniformly in S; for the empty set use a null mark. Write J_P(S,l)=P(S)/|S| and J_R(S,l)=R(S)/|S|, with the respective empty/null masses. Define

    L(P)=sum_(S nonempty) P(S)log2|S|.

Direct expansion, including the null atom, gives

    H(J_P)=H(P)+L(P),
    CE(J_P,J_R)=CE(P,R)+L(P),
    D(J_P||J_R)=D(P||R).                                (1)

The last equality matters: the witness lift creates no additional relative-entropy debt. For positive integer d, log2 d<=d-1, so

    0<=L(P)<=I(f)-Var(f).                               (2)

Equations(1),(2) price the lift once at the original source. They do not price CE(P,R) for arbitrary f.

## 2. Explicit physical kernel: keep or reselect the mark

Query physical coordinate i. For each remaining set T, let p0=P(T), p1=P(T+i), and p=p0+p1. The actual restricted squared spectra P_0,P_1 satisfy P_0(T)+P_1(T)=2p. Use the common outcome kernel

    kappa_t(T)=P_t(T)/(2p) when p>0;
    kappa_0(T)=kappa_1(T)=1/2 when p=0.                 (3)

Crucially the same zero-true-fiber extension is used for true and reference laws, and kappa depends only on T, not on which parent set or mark was present. Map the mark as follows:

* If T is empty, output the null mark.
* If the old mark survives in T, keep it.
* If the old mark is i and T is nonempty, choose uniformly in T.

For S=T the input mark was uniform on T. For S=T+i, each surviving point receives probability1/(|T|+1) from retention and1/(|T|(|T|+1)) from reselection, totaling1/|T|. Thus both parent alternatives produce the SAME uniform mark on T, even on reference-only fibers.

Pushing J_P by this kernel gives exactly(1/2)J_(P_t) on each physical outcome. Pushing J_R gives the lift of the RAW reference

    r_t(T)=[R(T)+R(T+i)] kappa_t(T).                    (4)

Its outcome normalizer Z_t=sum_T r_t(T) is positive because R supports P. Normalize by Z_t, then calibrate the empty/nonempty category to the child's ACTUAL squared mean and variance. The same calibration on the joint law (null versus non-null marks) gives exactly J_(R_t). Therefore lift, physical transport, outcome normalization and empty calibration commute. The reference outcome masses Z_t need not equal1/2 and must be retained. No new source reference certificate is issued.

This is valid for biased children, constants, zero spectral atoms, and reference-only atoms. A zero-true-fiber may not be discarded before reference transport. The label remapping when deleting coordinate i is only a renaming of surviving physical coordinates.

## 3. Exact lifted release and complete stopping-tree ledger

The averaged child squared coefficients obey the pair identity above, so coherence cancels exactly in the average L. Writing d=|S|,

    lambda_i=L(P)-[L(P_0)+L(P_1)]/2
      =sum_(i in S,d>=2) P(S)log2[d/(d-1)],
    0<=lambda_i<=Inf_i(f).                              (5)

Thus L is a supermartingale under arbitrary adaptive PHYSICAL queries. It is not being assumed restriction-hereditary from an unchanged root certificate.

For the compatible references in section2, if Delta CE_base is the old full scalar CE release (including erasure, JS, reference-outcome KL, erased KL and category savings), then

    Delta CE_lift=Delta CE_base+lambda_i.                (6)

For completeness the scalar release is nonnegative without an assumed cheap-child certificate. Let B=sum_T p(T) h2(P(T+i)/p(T)) and J=1-sum_T p(T) h2(kappa_0(T)), with zero-weight terms zero. The entropy chain rule gives H(P)-average H(P_t)=B+J, and J>=0. Apply relative-entropy data processing to the common channel (3): D(P||R)>=D((1/2,1/2)||Z)+average D(P_t||r_t/Z_t). Calibrating the empty category subtracts exactly the binary category divergence from each latter KL. Therefore the scalar CE release is B+J plus nonnegative channel KL loss, reference-outcome KL and category savings. This also explains why Z and reference-only fibers must survive. All formulas use actual physical outcome probabilities1/2.

All old debits and both complete child CE bills remain. Joint KL release is exactly the scalar KL release by(1). For every finite adaptive stopping tree with actual physical reaches,

    sum reach*Delta CE_lift + E CE(J_Pleaf,J_Rleaf)
                      =CE(P_root,R_root)+L(P_root),
    sum reach*lambda_i=L(P_root)-E L(P_leaf).             (7)

No child is declared cheap merely because its parent was. Full terminal H+KL, plus the mark overhead L, is retained on every stopped branch. The proof is finite telescoping of(5),(6); it does not change when query choices depend on earlier outcomes.

## 4. Explicit randomness is a second invoice, paid by original influence

The above stochastic kernel may require fresh random bits to reselect a mark. Under the TRUE input law the expected Shannon entropy of those reselections at a query is exactly

    rho_i=sum_(i in S,d>=2) P(S)log2(d-1)/d.             (8)

The factor1/d is the probability the queried point was the mark. The SHARP pointwise bound is log2(d-1)/d<=2/5 for integer d>=2. Equivalently (d-1)^5<=4^d: verify d=2,3,4,5 by the integer comparisons 1<=16,32<=64,243<=256,1024=1024. For d>=5 the induction step multiplies the left side by (d/(d-1))^5<= (5/4)^5<4, since3125<4096. Equality holds only at d=5. Thus0<=rho_i<=(2/5)Inf_i(f), with optimal pointwise constant attained by the actual Boolean character parity_5. The physical influence telescope therefore gives

    sum reach*rho_i<=(2/5)(I_root-E I_leaf).                   (9)

This is ONE original influence account, not a renewed whole-subfunction bank at each query. If the accounting convention includes this additional randomness invoice as well as the complete lifted CE ledger, their explicit combined bound is

    full lifted CE ledger + reselection entropy
      <=CE(P_root,R_root)+(7/5)I_root-Var(root)-(2/5)E I_leaf.    (10)

In particular a supplied CE(P_root,R_root)<=C I_root gives rateC+7/5. This is an upper bound for the combined accounting convention, not a claim of its optimal global rate. If only the lifted CE ledger is charged, the overhead is just(2); rho is not silently added to its entropy release or confused with lambda.

The probabilities for kappa in(3) are the pre-existing physical spectral transport; rho counts ONLY the mark reselection, not the randomness needed to simulate that full spectral channel, and not prefix-free integer coding length. It is Shannon conditional entropy under the stated joint law. No sampling complexity or executable spectral sampler is claimed.

An adversarial character guard shows why rho cannot be paid just from lambda. For f=parity_d and any queried i,

    lambda=log2[d/(d-1)], rho=log2(d-1)/d.

At d=8, rho>lambda because7^9>8^8. More generally their ratio diverges: lambda<=1/((d-1)ln2), so rho/lambda>=(d-1)ln(d-1)/d. The additional original-influence invoice is real for this explicit kernel. This does not claim minimal randomness among all possible witness transports.

## 5. Validation and first unsupported line

FROZEN_SPEC fixes every labelled three-bit Boolean function, each physical coordinate, exact and uniform-nonempty calibrated references (1536 one-query cases),512 complete least-coordinate trees, and compressed actual parity characters of degrees2..64. Four disjoint truth-code-mod4 lanes are frozen before the runs. Reference-only fibers, actual normalizers, zero-variance children and null-mark calibration are kept. The implementation pushes explicit true and reference JOINT atoms by the keep/reselect kernel and independently compares them to lifted scalar marginals; exact identities are checked separately from sign bounds and complete original-owner telescopes.

FROZEN_SHARPENING.json separately fixes63 exact integer certificates for d2..64 before running code/sharp.py; out/SHARP_RESELECTION.json retains the sharp2/5 guard. The original exhaustive checker deliberately retains its weaker valid <=Inf bounds; the sharper bound is supplied by the independent integer inequality and induction above, not by retroactively relabeling those assertions.

The all-dimensional finite-tree theorem is sections1-4, not an extrapolation from these checks. The source premise CE(P_root,R_root)<=C I_root remains unpaid for arbitrary Boolean f. The lift and its history updates are now influence-priced conditional on that premise, but this does not reduce the initial source problem to something already proved. NEXT must exploit Boolean realizability to price an original-spectrum per-set/shared-label source rather than repeat transport or resampling identities. Full FEI is OPEN; independent reconstruction is pending.
