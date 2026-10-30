# Independent review of the protected-character replacement

All cubes are finite and uniform; logarithms and KL use bits. This reviews A036-CHARACTER-ANCHORED-NORMALIZED-DIVERGENCE-BANK@1, statement SHA256 7394ec7514ebcfa945e20a463d9a41d170f1ee708c6b2a30af133db2fdf7bf1e, unchanged. No A036 program is imported. Exact finite checks support the identities; the following proof supplies the all-dimensional and all-history conclusions.

## 1. Reference, ghosts and complete physical channel

Write p(S)=fhat(S)^2, u=p(empty), a=1-p(J), for a fixed NONEMPTY protected mask J. For 0<alpha<1, beta=1-alpha and ell=log2(1/beta), use q(empty)=u and q(S)=beta p(S)+alpha(1-u)1[S=J] elsewhere. This is normalized. Equivalently q=beta p+alpha[u delta_empty+(1-u)delta_J]. Every source-positive atom remains. If p(J)=0, q(J) may be positive; that reference-only atom remains in the channel.

All nonempty non-J source atoms have likelihood ratio 1/beta; the J contribution to KL is nonpositive because q(J)>=p(J). The empty contribution is zero. Thus

    0 <= K(f)=D(p||q) <= ell(1-u-p(J)) <= ell a.

At query i outside J, erase i in p and q to pbar and qbar. Put k_y(T)=p_child_y(T)/(2pbar(T)) on positive rows, and k_y(T)=1/2 on source-zero rows, retaining their entire qbar mass. Parseval and the literal restriction formula give sum_y k_y(T)=1. The reference outcome r_y=sum_T qbar(T)k_y(T) is at least beta/2>0, from q>=beta p and the physically fair source outcome. Normalize each inherited child by its OWN r_y. Applying the finite KL chain rule first to erasure and then to this common kernel gives the exact equality

    K(f) = E_i + O_i + average_y K_inherited_y,

where E_i>=0 by data processing and O_i=D(fair||r)>=0. The argument also applies to source-zero rows: their source contribution is zero, their reference mass is transported with the stated fair fallback. No support equality is assumed.

The actual signed reset to fresh q_child has cost sigma_i=average K_fresh_child-average K_inherited_child. Hence sigma_i<=ell average a_child. This inequality preserves negative resets; it never independently clips or refunds them.

## 2. Adaptive bank and its precise restriction

Let r be the number of currently available coordinates outside J, c=fhat(J) and b=fhat(J+i). The children have J coefficients c+b,c-b. Consequently

    average a_child = a-b^2,
    r a -(r-1) average a_child = a+(r-1)b^2 >= average a_child.

Multiplying by physical history reaches and summing over ANY finite adaptive outside-J tree telescopes this NONNEGATIVE bank. Early stopping is allowed. Thus

    Sigma <= ell[B_root-E B_terminal],
    K(root)+Sigma <= ell(r_root+1)a_root.

Every queried parent must start with the stated anchored reference: reset both children after every query. Omitting a reset and later silently treating an inherited parent as fresh would invalidate this derivation. The exact chain telescope furthermore identifies K(root)+Sigma with the sum of actual erasure releases, actual outcome divergences and full final KL. Protecting every coordinate of J is essential; querying an anchor coordinate or replacing J later needs a separately priced operation. Constants and exact characters cause no exception.

## 3. SAME original source and all constants

Use A048's preceding mod3 family, now independently accepted by A036: N even>=10, k=N, delta=2^-N; h is parity z1 edited at z=e2,e1+e2 and at z=0 when the N-tail weight is 0 modulo3. Put J={z1}. Direct character sums give hhat(J)=1-4delta-2delta rho_N(0), so delta<=a<=12delta and hhat(J)>0. The root full-mask coefficient has squared magnitude at most4delta^2, strictly smaller than p(J).

At fixed u, KL of a spike on an atom of source mass s is

    K(s)=(1-u)ell-s log2(1+alpha(1-u)/(beta s)).

Its derivative is negative, since ln(1+x)-x/(1+x)>0 for x>0. Therefore changing from the original FULL spike to J has a strictly NEGATIVE actual signed conversion c=K_J-K_FULL. The original reference is not refunded a second time.

Retain the actual initial selector F=a-character on x=0, h on x=b=1, and +1 otherwise, and its already specified correlation-preserving FULL-spike reference. Query b and then x in b=1. Both complementary terminals remain. Nonempty data-sector likelihoods are identical across the four control copies, and the empty sector is actual; direct coefficient pairing therefore gives zero control releases, active reach1/4 and inherited reference exactly q_FULL. Initial KL is A0=K_FULL/4. Execute c at that reach, then ANY adaptive outside-J tree resetting both children each time. With r_root=2N-1 and alpha=1/6,

    A0+c/4+Sigma_later/4
      <=(2N)a ell/4 <=6N delta ell <1/64.

Here ell<4/15 is the INTEGER inequality 6^15<16*5^15. Also N/2^N decreases for N>=10 and 6*10*(4/15)/1024=1/64, so the strict log bound proves the strict inequality for every N>=10.

The bank identity also gives E a_leaf<=a at every stopped frontier. Partitioning leaf entropy at J, Jensen and the ambient bound2N give

    E H_leaf <=h2(a)+2Na <=12delta(3N+2)<=3/8,
    E I_leaf >=1-a.

The binary-entropy estimate uses delta<=a, h2(a)<=a(log2(1/a)+log2(e)), and log2(e)<2; the envelope decreases from N=10. These are direct analytic estimates, not FEI assumptions. The two complementary selector terminals have reached rate4 surplus1 each, so full final S>=2+[4(1-a)-3/8]/4>=741/256, since a<=3/256.

For completeness the ORIGINAL physical entropy bound can be re-derived without the source's prose convexity shortcut. The two a-character masses1/4 contribute entropy1. The four vacuum/control masses are two copies each of (1+mu)^2/16 and (1-mu)^2/16, mu=Eh<=0. Their entropy is 1+mu^2 minus (1/4)sum_sign (1+sign mu)^2 log2(1+sign mu). This correction is nonnegative: set y_sign=(1+sign mu)^2 and use sum y log2 y >= (sum y)log2(sum y/2)>=0, with sum y=2(1+mu^2). The four copies p_h(S)/16 for each nonempty data S contribute Var(h)+H_nonempty(h)/4. Hence H(F)<=3+H(h)/4. Also I(F)=1+t/2+I(h)/4 with t=Pr(h=-1)>=1/2 and I(h)>=1-a. Thus 4I(F)-H(F)>=741/256 independently of any supplier.

Let Sigma=c/4+Sigma_later/4 and e=H(F)-H_final-4(I(F)-I_final), with physical reaches included. Signed algebra, WITHOUT assuming e>=0, gives

    S-[A0+e+Sigma]_+ = min(S,4I(F)-H(F)-A0-Sigma)
                         >737/256.

Keeping ONE old booking omega<=1/4 leaves >673/256. This proves the full recovery statement, not only its local KL estimate. No positive parts have been split; no terminal or reference-only mass has been dropped. The original account, original conversion and every subsequent reset are paid once.

## 4. Tensor and sparse stress of this REPLACEMENT

For T independent copies use the PRODUCT of the factorwise anchored references, with each factor retaining its own anchor, r_j and a_j. Product KL adds. During a query in factor j, the other source/reference factors pass unchanged through the common kernel; the own outcome normalizer and reset are exactly the factor's. The decreasing bank is ell sum_j r_j a_j, not an unnecessarily re-spiked global anchor with a crude T^2 envelope. Interleaving queries, with branch-dependent choices of factors, still telescopes that additive bank. For identical supplied F copies and complete mapped bookings omega_j<=1/4, the proof above gives both S_total and remaining original margin greater than T*673/256. Therefore full signed recovery has that same lower bound. No T log T appears.

Under the SAME normalized guarded sparse lift from the previous stage, let lambda be active reach (renamed to avoid confusing it with the spike alpha). The actual quotient sectors remain actual and the active sectors contain the product factor reference. Physical control exposure inherits that reference exactly. Thus A, signed conversions and later reset bills all scale by lambda; the quotient retains its own nonnegative original surplus beta_l. Consequently mapped remaining owner margin is beta_l+lambda sum_j(M_j-Sigma_j), and the balanced retained sign gives full terminal surplus at least lambda sum_j S_j. With mapped old bookings lambda sum_j omega_j, recovery is >lambda*T*673/256. This assertion does NOT fund an additional unscaled whole-source quarter when lambda tends to zero. A dummy coordinate has no effect; an independent spectator adds only its own finite margin. These are direct product/sector identities, not an additional universal FEI theorem.

## 5. Review decision and first unpaid line

A036@1 HOLDS at its complete stated scope, unchanged, contingent on CHECK.json and AUDIT.json both recording PASS. This review supplies no substantive repair: the rewritten convexity calculation verifies the same inequality and constants. A036's review of A048's preceding obstruction is recorded as an incoming independent acceptance, not self-review. These results coexist because the replacement changes and explicitly pays its supplier; it does not validate the retired FULL-spike protocol.

The first unsupported universal line remains an influence price for a useful original protected anchor/decomposition on an arbitrary Boolean core, with any necessary later anchor change paid from the SAME depleted owner. Neither (r+1)(1-p(J))<=K I nor the usefulness of a protected anchor for every function is established. This stage closes an independent-review obligation and proves the tensor/sparse accounting of the repair; it does not close full FEI or improve a universal constant.
