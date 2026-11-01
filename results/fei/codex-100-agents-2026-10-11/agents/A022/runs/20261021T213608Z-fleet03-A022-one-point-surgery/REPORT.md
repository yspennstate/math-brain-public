# A022: signed seed-reference cost of controlled point surgery

## Exact target, quantifiers, hypotheses and units

Full FEI remains OPEN. This stage replaces the ambient seed bill in the preceding A022 root estimate by a supplied complete seed reference. It gives an exact signed cut formula, an explicit unchanged-bank eligibility condition, and a rate-4 application below the preceding high-influence hypothesis. Entropy is in bits.

Let b:{0,1}^k -> {+1,-1}, N=2^k, delta=1/N. Distinct vertices v_j have arbitrary, possibly dependent indicators A_j(z) on an independent uniform control cube. Set a_j=1-2A_j, alpha_j=E A_j, mu_j=E a_j, and F(x,z)=b(x)(1-2 sum_j 1_{x=v_j} A_j(z)). Let P_b(S)=bhat(S)^2. A supplied reference Q(S)>0 is normalized on ALL data Fourier labels. No support is silently omitted. Define ell(S)=log2(1/Q(S)), K_Q(d)=delta sum_S ell(S) chi_S(d), L=delta sum_j H(a_j), V=delta sum_j(1-mu_j^2), and phi(u)=-u log2 u with phi(0)=0.

## Sources actually read, revisions and theorem locators

The execution protocol is fei-execution-protocol/2, revision 2026-10-11-execution-v2. The board, B05 STREAM_NOTES.md v2 and A022 rolling notes were read at stage entry. The last source-complete A022 run is 20261014T103056Z-fleet05-A022-one-point-surgery (stage6); the later fleet05 directories inspected contain only .final, so their timestamps are not additional mathematical evidence. The source manifest records the campaign files, supplemental ledgers, earlier A022 reports, B05 lead report availability, and relevant paper passages read. The current user deadline, 2026-10-23 14:49 UTC, supersedes the older endpoint printed in the static protocol. No external source is needed for the algebra below. No new result is attributed to the paper without a specific passage.

## Complete derivation or exact first unsupported line

### 1. Exact signed spectrum and controller marginal

Write Ahat_j(T)=E A_j chi_T. Direct transformation gives

    Fhat(S,T) = 1_{T=empty} bhat(S)
                -2 delta sum_j b(v_j) chi_S(v_j) Ahat_j(T).

Retain this signed expression before squaring. Orthogonality of the distinct vertex characters gives the exact control spectral marginal R:

    R_empty=1-V;
    R_T=delta sum_j ahat_j(T)^2, T!=empty.

For nonempty T with R_T>0 set xi_{j|T}=delta ahat_j(T)^2/R_T and M=sum_{T!=empty} R_T H(xi_{.|T}). Terms of zero mass are zero. Then

    H(R)=L+kV+phi(1-V)-delta sum_j phi(mu_j^2)-M.             (1)

This is a spectrum mixture, not a physical reset. In particular M>=0 is a label-mixing refund. The assumption q<=N ensures the equivalent mixture has nonnegative empty-point weight 1-q delta; alternatively (1) follows directly from the nonempty rows and does not divide by that weight.

### 2. Exact reference loss is a signed physical cut

For fixed z let D_z={v_j:A_j(z)=1}. The data spectral marginal is P_X(S)=E_z f_z_hat(S)^2. Define

    W_Q = -4 delta E_z sum_{x in D_z, y notin D_z}
                                b(x)b(y) K_Q(x xor y).       (2)

The cut is oriented once, from its edited endpoint. The Walsh matrix with entries K_Q(x xor y) represents multiplication by ell in Fourier space. Therefore

    CE_Q(P_X)-CE_Q(P_b)=W_Q.                                (3)

To verify the factor: CE_Q(fhat^2)=delta sum_{x,y} f(x)f(y)K_Q(x xor y). Across the cut, f(x)f(y)-b(x)b(y)=-2b(x)b(y). Both ordered orientations occur in the quadratic form; (2) follows. The diagonal cancels. This derivation applies to every deterministic cut and hence to all correlations of A_j.

Let D_joint=D(P_{S,T} || Q(S)R(T)), with zero R rows omitted. Q positivity makes every remaining reference atom positive. The entropy identity is

    H(F)=CE_Q(P_b)+L+kV+phi(1-V)-delta sum_j phi(mu_j^2)
                     +W_Q-M-D_joint.                       (4)

Here CE_Q(P_b)=H(b)+D(P_b||Q). Thus the entire seed reference bill remains present, as do the controller bill L and both signed/refund terms. For Q=P_b this requires full Fourier support; a seed with zeros must instead supply a positive normalized Q and retain its reference mismatch.

### 3. Actual physical influence, including adjacent cancellation

Put s_b(v)=sum_{i=1}^k b(v)b(v xor e_i). Counting each affected data edge gives

    DeltaI = I_data(F)-I(b)
      =2 delta sum_j alpha_j s_b(v_j)
       -4 delta sum_{j<l:dist(v_j,v_l)=1}
                          b(v_j)b(v_l) E[A_j A_l].           (5)
    I_ctrl(F)=delta sum_j I(a_j).                           (6)

For a boundary edge exactly one endpoint flips; an edge whose two endpoints flip does not change. Expanding the XOR indicator yields the negative adjacent correction in (5). Separated edits have no such physical-edge term, though (2) can still have nonlocal interactions.

### 4. The same supplied bank, with old bookings

Fix C>=0 and an already booked nonnegative amount U. Define the ORIGINAL remaining seed bank S=C I(b)-CE_Q(P_b)-U. Equation (4) gives the following exact equivalence:

    H(F)+U <= C I_data(F)+L
    iff kV+phi(1-V)-delta sum_j phi(mu_j^2)+W_Q-M-D_joint
                                                        <= S+C DeltaI. (7)

There is no replenishment of S. In particular a convenient sufficient condition is

    (k+log2(e))V+W_Q <= S+C DeltaI,                         (8)

because phi(1-V)<=log2(e)V and the three removed terms are nonnegative. Equation (7), rather than an unsigned continuity cost, identifies exactly what a physical-bank payment must cover. A reference may have a large positive or negative W_Q. Neither sign may be presumed from proximity of the spectra.

### 5. Tensor locality of the logarithmic cost

If Q is a product of positive normalized block references, ell is a sum of block ell functions. Hence K_Q(d)=0 whenever d has nonzero components in two or more blocks. Within a single changed block its off-diagonal value is exactly that block's kernel. Thus all adjacent-point and k-point logarithmic interaction terms are restricted to within-block pairs. This is a statement about the complete supplied reference, with the original tensor seed bill still present.

For one edited vertex v and Q=P_b of full support set

    J_b(v)=delta sum_S log2(1/P_b(S))
             -b(v) sum_S bhat(S)chi_S(v)log2(1/P_b(S)).

Then W=4 delta alpha J_b(v). For b=product_l b_l and v=(v_l),

    J_b(v)=sum_l J_{b_l}(v_l),  s_b(v)=sum_l s_{b_l}(v_l).  (9)

The factorization uses sum_S bhat(S)chi_S(v)=b(v), including its sign. In the one-point case M=0. Thus (4) gives every logarithmic term explicitly, including the nonnegative D_joint which (8) discards.

### 6. A nonflat, low-influence seed spends only its original bank

Let g on three bits be -1 at 000 and +1 elsewhere; let b=g^{tensor t} on k=3t bits, for any integer t>=2. Choose ANY data vertex v and ANY independent control indicator A (arbitrary dimension and bias). Then

    H(F)+U <= 4 I_data(F)+delta H(1-2A)
                    for every 0<=U<=t/64.                 (10)

In particular, a controller with H(a)<=4I(a) gives H(F)<=4I(F). The controller's full entropy has been paid exactly once. Finite recursive constructions using fresh data blocks obey the same implication by induction; this does not admit arbitrary uncertified controllers at rate 4.

Proof. Direct Walsh transformation gives ghat(empty)=3/4 and ghat(S)=-1/4 for S!=empty. Thus

    I(b)=3t/4, H(b)=t[4-(9/8)log2 3]<9t/4.

The original rate-4 surplus is consequently >3t/4. Explicitly,

    J_g(000)=-(7/4)log2 3;
    J_g(v)=(5/4)log2 3 for v!=000.

The local signed edge counts are -3 at 000, 1 at Hamming weight one, and 3 otherwise. By (9), J_b(v)<2t and s_b(v)>=-3t. With alpha=EA, delta=8^{-t}, V=4delta alpha(1-alpha), c=log2(e)<3/2, the upper bound in (4) yields

    H(F)-L-4I_data(F)
      <= -[4I(b)-H(b)]
                         +delta alpha[4J_b(v)+4k+4c-8s_b(v)]
      < -3t/4 + delta(44t+6)
      <= -3t/4 +(47/64)t = -t/64.

The last inequality uses t>=2, delta<=1/64 and 6/t<=3. The elementary log comparisons are certified by integers: log2 3>14/9 because 3^9>2^14, and log2 3<8/5 because 3^5<2^8. The estimate c<3/2 follows from ln2=2 sum_{j>=0}(1/3)^{2j+1}/(2j+1)>2/3. No floating logarithmic sign is used. The cases alpha=0 and alpha=1 are included: zero-mass phi terms use their stated convention, and no division by alpha occurs. At alpha=0 the stronger original surplus remains. This seed has I(b)/k=1/4, so it is outside the preceding root theorem's I(b)>=k/2 hypothesis.

### First unsupported universal line

For arbitrary b, edits and actual mixed restriction histories, there is no proof that the signed left side of (7) is bounded by the SAME remaining seed bank plus C DeltaI at a dimension-independent C. Full support does not supply that payment, and conditioning on a data query does not authorize replacing Q or restoring S. Arbitrary seed entropy/reference cost is still an unpaid terminal. Equation (10) does not prove the universal bridge.

## Executed validation with domain, arithmetic, commands and outputs

Frozen specification: FROZEN_SPEC.json, written before computation. Helper: code/check_reference.py. Pilot: 128 declared cases, 3,968 exact assertions, PASS in 0.723 seconds of helper runtime. Main results are in out/exact_checks.json. The checker compares direct truth-table transforms with the signed spectral formula; compares cross-entropy with the independently formed physical cut; retains the full joint KL in the entropy identity; and independently counts actual physical edges for (5). Rational linear combinations of prime logarithms are canonicalized and compared exactly. No floating-point equality or sign supplies a certificate.

Checks that could fail: cut orientation or factor 4; omitting double-flipped adjacent edges; treating controller events as independent; dropping a zero reference atom; losing the joint KL or seed mismatch; incorrect tensor sign; restoring the bank; extending finite checks to all dimensions. The declared finite suite checks the algebra. Section 6's all-t proof supplies the infinite extension. Formal-check status and independent-review status are recorded separately in the final validation receipt.

Main: 4,256 cases, 137,425 exact assertions, PASS in 52.782 seconds of helper runtime. The follow-up bank replay passes 362 checks, including all eight local vertices, the two integer log comparisons, t=2..20 and zero/full activation. Its finite replay is supporting verification; the displayed all-t argument supplies the proof. The adversarial endpoint replay passes 24 cases and 144 exact assertions: zero seed atoms with a positive supplied reference, q delta=1, V=0, V=1, fully correlated full edits, and cycling edits. These checks ensure that neither full Fourier support nor a positive empty row was used by the general reference identity. Across the pilot and all three suites there are 141,899 exact assertions.

The requested formal attempt returns RUNTIME_UNVERIFIED after 123.5 seconds; translation fidelity is UNVERIFIED. It exceeds the follow-up's 60-second target and supplies no Lean certification. No retry or broader formal search was started. The saved code/Bank.lean states only the rational final bank comparison, not the entropy theorem. Mathematical rung: analytic proof with exact author checks, pending independent review. No compiled theorem or transitive-axiom acceptance is claimed.

Commands: python -X utf8 <run>/code/check_reference.py --pilot; python -X utf8 <run>/code/check_reference.py; python -X utf8 <run>/code/check_bank.py; python -X utf8 <run>/code/check_endpoints.py. The exact jobs are small (<300 MB by the frozen estimates; peak unmeasured); no heavy search, GPU, detached process or other-agent process control was used.

## Proof dependencies and changed downstream conclusions

The derivation uses finite Walsh orthogonality, the entropy chain identity, KL nonnegativity, and phi(1-V)<=V log2(e). It reconstructs the stage6 controller marginal rather than assuming review of that run. The new reference identity refines the stage6 ambient conditional-data bound; the earlier theorem is unchanged. A087/A094 should check (2), (4), (5), and the fixed-bank sign in (7). A021/A025/A028/A029 can use the signed tensor-block interaction cost without suppressing L, CE_Q(P_b), U, M or D_joint.

## One next mathematical action and independent reviewer

Next: expose one actual data coordinate of the nonflat tensor construction, carry the incoming Q and booked U through BOTH children, and compare its signed conditional reference loss against the remaining original t/64 reserve. A087 and A094 are the requested independent reviewers; no independent acceptance is claimed.

## Actual persistence receipts or precise save blocker

All files are local to the assigned A022 run and rolling-note paths. Final receipts include file hashes and schema validation in out/persistence.json. Shared indices, the brain, other agent folders and external services were not modified. Upload/mirror verification is the supervisor's step and is not claimed here.

## Universal bridge

This advances C024 history transfer at its root interface and the B05 localized stopping-tree payment target: it replaces the entire ambient seed bill by its complete supplied reference, identifies the exact signed log-kernel cut and the SAME-bank admission inequality, and pays a nonflat low-influence tensor surgery at rate 4 with at least t/64 of the original reserve retained. What remains is the signed loss after an actual data query with both terminal references, old bookings and the original bank unchanged. That next query is the shortest route toward a general FEI payment because the root logarithms and their tensor interactions are now explicit; another fixed family census would not resolve the unpaid history transfer.
