# A source-owned reserve on a non-flat collision row

Costs and entropies are in bits. All coordinates below are original independent fair physical coordinates. This is a scoped extension of the bent/flip reserve, not a universal child-slack theorem.

## 1. Actual Boolean family and exact physical accounts

Let k>=4 be even, m>=0, n=k+m, delta=2^-n and e=2^(-k/2). Put b(x)=(-1)^(x1*x2+...+x(k-1)*xk), in binary coordinates. Embed G(x,y)=b(x) with m dummy bits y, and flip the actual all-zero point: H=G-2*1_{(x,y)=0}. Both are Boolean because G(0)=1. A fresh bit z selects them: M=(G+H)/2+z(G-H)/2. Every data bit is shared by the children, although the y bits are dummy only in G. This is not the old witness tensor a dummy: the flip requires ALL padding bits to vanish.

Each original point-to-neighbor edge in G is nonpivotal, including all padding edges. Flipping zero adds one undirected boundary edge on every data coordinate. Hence

    I(G)=k/2, I(H)=k/2+2n delta,
    d=Inf_z(M)=delta, I(M)=k/2+(n+1)delta.

Let E be the 2^k Fourier sets containing no padding variable. On E, Ghat=sigma e, Hhat=sigma e-2delta, with N_sigma=(2^k+sigma*2^(k/2))/2. Outside E, Ghat=0 and Hhat=-2delta. M has selector-absent coefficient sigma e-delta on E and -delta outside E, and selector-present coefficient delta everywhere. These explicit probabilities define a normalized complete reference Q_M=P_M. It is a structural formula for this family, not an influence-paid oracle for arbitrary Boolean functions. Non-flat rows include both old bent packets and the new packets outside E.

## 2. Transfer the proved minority cap into the missing seed reserve

Use the NEW shared-width clause of A095-RANK-KL-EQUIVALENCE@3: for n shared bits, Delta=H(M)-[H(G)+H(H)]/2 <=(n+2+3/ln2)d. Its hypotheses hold here: actual Boolean children, fresh selector, shared n-bit uniform block, no private variables, d=delta<=1/2 and n>=4. The exact source substitution is t=n and d*=delta. A086 independently reconstructed this clause; the entire broad rank/equivalence claim is not required.

We must pay E_K=Delta-K delta from an ACTUAL averaged child bank

    S_K=[K I(G)-H(G)+K I(H)-H(H)]/2.

Merely writing this identity would not close the missing term. The following non-flat entropy bound certifies its size. The new-frequency mass of H is w=4delta(1-2^-m). Splitting its spectrum into E and its complement, with the true sector probabilities, gives

    H(H)<=h2(w)+(1-w)k+w log2(2^n-2^k)
          <=k+h2(w)+wm.

For m=0 use w=0 and H(H)<=k. For m>=1, 4*2^-m(1-2^-m)<=1 implies w<=2^-k. Since h2 increases up to one half, h2(w)<=2^-k(k+1/ln2). Also m*2^-m<=1/2, so wm<=4m delta<=2^(1-k). Therefore

    H(H)-k <=2^-k(k+2+1/ln2)<2^-k(k+7/2),

using ln2>2/3. This includes the sector label and every new physical subset.

Choose K=17/8. Exact influence accounts and H(G)=k now give

    S_K=k/16+(17/8)n delta-[H(H)-k]/2
        >k/16-(k+7/2)2^(-k-1)+(17/8)n delta.

The transferred tax gives E_K<(n+35/8)delta. Thus

    S_K-E_K > k/16-(k+7/2)2^(-k-1)+(9n-35)delta/8.

The first two terms are >=1/64 for k>=4: k/16>=1/4, and (k+7/2)2^(-k-1) decreases from 15/64. Since n>=4, 9n-35>=1. In particular the bank pays the exact missing excess once, with a strict margin >1/64. Consequently

    CE(P_M,Q_M)=H(M)<(17/8) I(M).

This is a verified payment inequality S_(17/8)>=Delta-(17/8)d on a genuinely non-flat shared row. It borrows the additional k/16 price slack in the original bent component and the actual point-edge increment; neither calibration savings nor posterior credit funds it. All child reference bills are exact and remain in S_K. This does not claim 17/8 is optimal.

## 3. The old price-two reserve does not survive this padding surgery

A086's price-two theorem for the UNPADDED family is not refuted. Its unrestricted extension to this padding surgery is false. Fix k=4 and n=4+m>=22. On E the selector-absent probabilities p_T=(sigma/4-delta)^2 lie in [1/32,1/8]. For L(p)=-p log2 p, the derivative has absolute value <=5 on this interval. Also sum_E |p_T-1/16|=8delta-4delta^2<=8delta. The mean value theorem yields H_old>=4-40delta.

Outside E there are exactly 2(2^n-16) parent atoms, each of mass delta^2, so their entropy is 4n delta(1-2^(4-n)). Dropping the other positive selector-present entropy only weakens the bound. Therefore

    H(M)-2I(M)>=delta[2n-42-4n*2^(4-n)]>0, n>=22.

The last sign is analytic: 4n*2^(4-n)<1 for n>=22 and decreases there, while 2n-42>=2. At n=22 the bracket equals 2-11/32768. Hence S_2<Delta-2d for every m>=18. Exact spectra and ordinary edges witness failure, with no reference mismatch. The failure concerns a reserve transport, not FEI: the repaired 17/8 bound holds on the entire family. No original source claimed the false padded extension, so no accepted claim is marked refuted.

## 4. Arbitrary terminal reference and one actual recursive insertion

Let q be ANY Boolean sign on an independent data block, physically shared by both children, and let R_q be a supplied normalized positive-support finite-cost reference, c_q=CE(P_q,R_q). For g=q M use the fixed product reference R_g=R_q tensor Q_M. Fourier and edge products give

    CE(P_g,R_g)=c_q+H(M)<c_q+(17/8)I(M),
    D(P_g||R_g)=D(P_q||R_q), I(g)=I(q)+I(M).

The full c_q is preserved once. It is not assumed influence-paid. The collision reserve is spent inside M only; no q influence is used to fund it.

Now insert g under r>=1 fresh physical point controls A_r, p=2^-r: F=1+A_r(g-1), mu=E g. Apply the earlier biased-activation clause of A095@3 (retained v2), with empty calibration R_g^0. The normalized complete reference is

    Q_F(vacuum)=[1-p(1-mu)]^2,
    Q_F(U!=empty,T=empty)=p^2(1-mu)^2,
    Q_F(U,T!=empty)=p^2 R_g^0(T).

Empty calibration saves exactly D_Ber(P_g(empty)||R_g(empty)), with all remaining conditional data debt intact. The source lemma yields

    CE_F <=p CE_gcal+6rp(1-mu)
          <p c_q+(17/8)p I(M)+6rp(1-mu),
    I(F)=p[I(q)+I(M)+r(1-mu)],
    D(P_F||Q_F)=p[D(P_q||R_q)-D_Ber(P_g(empty)||R_g(empty))].

These are three exclusive accounts: p times the terminal q bill, p times the already-paid M bill, and the fresh controller influence. Conditional c_q<=C I(q) gives CE_F<=max(C,6) I(F). No previous reserve is spent a second time. All biases, complement normalizers and complete output reference masses are included; integer-word rounding is separate.

## 5. First unsupported universal line

The all-parameter scoped claims above have complete proofs. The first unsupported universal line is replacing the certified k/16 and nonpivotal point-edge increment by a source-owned surplus for arbitrary unequal overlapping children whose point edits may destroy edges and whose spectrum has no bent support sector. A universal recursive proof also needs arbitrary terminal reference payment. The family-specific reserve cannot be inferred from non-flatness or Booleanity alone; the padded price-two counterexample prevents that shortcut.
