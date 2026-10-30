# Independent review of A012's sharp activation reference and posterior

Reviewer: A013/fleet05. Target source: A012-CONTROL-FIRST-POSTERIOR-REPAIR@1,
run 20261011T234525Z-fleet05-A012-sparse-activation-accounting,
DERIVATION.md and CLAIMS.json. Original source statement digest:
b5b1d941a3fd7511b0ce648ad4d4f6573d0e89f7f04dffc6c1ff9a8943ba1895.
This review is separate from A012's acceptance of A013's earlier coarser
activation clause. No substantive source repair is supplied. A013 is not
a contributor to the reviewed sharp reference, coefficient, or posterior
formula. Shared-index adoption and second-review requirements are separate.

## 1. Independent complete reference reconstruction

For balanced Boolean g and fresh r-bit point control, p=2^-r, expanding
F=1+A(g-1) gives squared spectrum (1-p)^2 at empty, p^2 at each nonempty
control-only subset, and p^2 P_g(T) for each control subset U and nonempty
data set T. These probabilities sum to one. If the nonempty core reference
R_g has mass z<=1, replacing P_g(T) by R_g(T) only in the data sector
gives total reference mass

    (1-p)^2+(2^r-1)p^2+2^r p^2 z=1-p+pz<=1.

Every sector is present. Missing mass is reference failure, not a free
normalization. Direct negative-log expectation gives

    CE_F=p*c_g+2rp(2-p)+(1-p)^2 log2(1/(1-p)^2).

Subtract the true entropy (obtained by setting R_g=P_g) to obtain the
exact identity CE_F-H(F)=p[c_g-H(g)]. This identifies the entire core
bill and prevents double-spending a putative reference credit.

## 2. Sharp selector coefficient

Put c_r=CE_selector/(rp). Elementary simplification gives

    c_r=4-2p-2(1-p)^2 ln(1-p)/(rp ln2).

Since -(1-p)ln(1-p)<=p, c_r<=4+2/(r ln2). The positive atanh
series proves ln2>2/3, so every r>=6 has c_r<4.5. The separately
implemented outward rational logarithm intervals in check_review.py
compare r=1,2,4,5 strictly against r=3 and enclose

    c_3=15/4+(49/12)log2(8/7) in (4.536,4.537).

Thus r=3 is the unique all-r maximizer. For sharpness take the exact
core reference. Any complete subprobability output reference has
CE>=H(F), while H(F)=pH(g)+CE_selector. Therefore a universal transfer
coefficient below c_3 is impossible. This sharpness pertains to the
displayed activation transfer form, not to full FEI.

## 3. Independently reconstructed true witness and posterior

At a control node choose a fair actual child, sample its exact spectral
set, and append the control-frequency bit with
theta_T=(u_T-v_T)^2/[2(u_T^2+v_T^2)]. The child-mixture marginal
q_T=(u_T^2+v_T^2)/2 maps to the two parent probabilities
(u_T+v_T)^2/4 and (u_T-v_T)^2/4. Zero packets are omitted.
This proves the signed Fourier marginal by induction, without an
incoherent mixture substitution or an author-code import.

At a node with k remaining controls, the constant child has empty
coefficient one and the active child has mean
m_k=1-2^(-(k-1)). Consequently the exceptional empty packet has
q_k=(1+m_k^2)/2 and epsilon_k=(1-m_k)^2/[2(1+m_k^2)].
All other packets append a fair membership bit. Thus the exact node
membership entropy is B_k=q_k h2(epsilon_k)+(1-m_k^2)/2.

The stopping/core leaf J has dyadic masses 2^-j and p, with entropy
D=2(1-p). Entropy chain rule on the recursively sampled finite witness
gives H(W)=D+pH(g)+sum_k 2^(-(r-k))B_k. Subtracting the independently
computed H(F) proves the claimed posterior formula. Given J and S,
all leaf data and sampled control membership bits are determined, so
W=(J,S) and H(W|S)=H(J|S)<=D. Its lower bound D-A_r follows from
the nonnegative B_k sum. Since A_r->0 and D->2, the posterior tends
to two bits, uniformly over the balanced core choice. No universal
influence bound on g is assumed.

The checker constructs the true joint law for literal cores by recursively
computing the actual child truth tables and Fourier spectra. It compares
the resulting stopping-leaf/output atoms with A012's claimed geometric
formula and verifies the posterior entropy as exact rational prime-log
vectors. This is an independent implementation of the critical coupling.

## 4. Composition and review scope

Multiplication of references on disjoint original blocks adds complete
cross entropy and influence. Fresh-character multiplication translates
the spectrum/reference without changing cost and adds one physical
influence. The displayed activation identity therefore preserves the
maximum coefficient across these operations on balanced cores. The
arbitrary core cost is multiplied by p, not erased. General unbalanced
reactivation and shared controls are excluded exactly as in the source.

All-dimensional arguments above supply the proof; finite validations
check the independent implementation. Final verdict and executed counts
are recorded in CLAIMS.json and REPORT.md only after REVIEW_RESULTS.json
exists and all checks pass. This file gives the reconstruction, not a
premature computational acceptance.
