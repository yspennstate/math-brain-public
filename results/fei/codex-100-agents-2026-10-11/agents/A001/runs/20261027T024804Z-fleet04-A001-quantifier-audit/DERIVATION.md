# Independent reconstruction of the physical-query accounting boundary

All entropy and complete cross-entropy are in bits. Full FEI remains OPEN. This is an independent review of A094-A011-V5-PHYSICAL-QUERY-KL-LEDGER-GAP@1, not a reconstruction of every numerical inequality of A011 v5.

## 1. Quantifiers and the finite physical-query identity

The full target is: there exists one real finite C>=0 such that for every integer n>=0 and every f:{-1,1}^n->{-1,1}, H_2(f)<=C I(f), under uniform measure. Here p_f(S)=fhat(S)^2, H_2=-sum p log2 p, I=sum |S|p. Use 0 log 0=0. Constant functions have H=I=0; division by I is limited to nonconstant functions. Neither a separate C_f for each function nor C_n for each dimension satisfies this quantifier order.

Fix ONE Boolean target on a finite cube throughout a physical restriction tree. At each actual node v let P_v be its squared Fourier law and Q_v its covering subprobability reference, of mass s_v in (0,1]. References retain model mass on true-zero atoms. Put CE(P,Q)=-sum P log2 Q and D(P||Q)=CE-H. Physical reach is lambda_v=2^(-depth(v)); both children have reach lambda_v/2. If a child reference is reset from actual inherited Q_vb^inh to prescribed R_vb, book the SIGNED charge e_vb=(lambda_v/2)[CE(P_vb,R_vb)-CE(P_vb,Q_vb^inh)]. A target-changing edit is not such a reset.

Define delta_v=lambda_v[D(P_v||Q_v)-avg_b D(P_vb||Q_vb^inh)]. The exact one-step identity is

lambda_v[CE(P_v,Q_v)-avg_b CE(P_vb,Q_vb^inh)]
=lambda_v[H(P_v)-avg_b H(P_vb)]+delta_v.

Sum over all query nodes, adding actual signed resets. Every interior complete CE cancels, and every interior entropy cancels. Thus, with the current reference at each complete terminal,

    CE_root + sum e = H_root + sum delta_v + sum_leaf lambda_v D(P_v||R_v). (A)

This is finite algebra; no limit, entropy monotonicity, or independent-child solvency is assumed. It applies to arbitrary finite adaptive trees, stopped or complete, with every sibling retained. A normalized scalar reference at a constant leaf gives terminal D=0; a scalar mass s<1 instead retains -log2 s.

## 2. Actual inheritance and the sign of delta

For a queried coordinate group parent atoms in pairs. Let m(T)=P(T0)+P(T1) and r(T)=Q(T0)+Q(T1). Actual child spectra P_b obey (P_0+P_1)/2=m by the signed Fourier restriction formula. Raw inherited child references are r(T)P_b(T)/m(T) when m(T)>0; when m(T)=0, retain r(T) on BOTH children. Write Z_b for each raw mass, and normalize the child reference to s times raw/Z_b, where s=sum Q. Cover gives Z_b>0. Exactly Z_0+Z_1=2s, including all reference-only fibers.

Direct expansion gives

    avg_b D(P_b||Q_b^inh)=D(m||r)+avg_b log2(Z_b/s).

The difference D(P||Q)-D(m||r) is the nonnegative average conditional relative entropy inside each pair (normalize Q within the pair; the common subprobability mass cancels). Jensen gives avg log2(Z_b/s)<=0. Consequently delta>=0. When Q has the ACTUAL conditional law inside every pair, the conditional relative entropy vanishes and

    delta/lambda = -1/2 log2[(Z_0/s)(Z_1/s)].             (B)

The normalized exact-source boundary Q=sP has Z_b=s and delta=0. A uniform or other covering reference can have a strict loss. Changing the inheritance convention changes this calculation; these formulas concern the exact convention in A011 v5 section1 and A094 section1, not every imaginable reference transport.

## 3. An actual A011 v5 witness, independently reconstructed

Take source g(x)=(-1)^x, a=1, b>=12 untouched padding bits, one new fair controller w. The original supplied reference is P_g, with c=C0=0 and I_g=1. Let e=2^(-1-b), and flip g only at x=0, padding=0, w=0. This is M=1,r_1=1 in A011's construction. Its global edit probability is e/2, so the actual first floor beta=6rho is 3e.

Group the FULL data masks into the unique original source atom A=1, multiplicity1, and A=0, multiplicity1/e-1. The actual parent data marginal and reference are

    q(A)=(A-e)^2+e^2,
    r(A)=(A^2+3e^2)/(1+3e).

Both distributions sum to1 with these multiplicities. Lift r by the TRUE controller conditional law. The clean child has P_clean(A)=A^2; the edited child has P_edit(A)=(A-2e)^2. Actual inheritance therefore gives

    Z_clean=(1+3e^2)/[(1+3e)(1-2e+2e^2)],
    Z_edit=2-Z_clean.

Let t=1-Z_clean. Direct rational subtraction factors as

    t=e(1-e)(1-6e)/[(1+3e)(1-2e+2e^2)].

For b>=12, 0<e<=1/8192<1/6. The numerator is positive; the denominator is >1 since it equals 1+e(1-4e+6e^2), and 1-4e+6e^2>0. Hence 0<t<e. The product Z_clean Z_edit=1-t^2 is strictly between0 and1. By (B), the query loss is

    delta=-(1/2)log2(1-t^2)>0.                          (C)

A011 prescribes P_g at the clean child and its actual 6e floor at the edited child (r_local=0). These are covering references, retaining reference-only atoms. Equation (A) is valid for their actual signed conversions, irrespective of their signs. Therefore A011 equation(6)'s prose identification of L=H_root+E D_terminal with root CE plus actual signed resets omits this positive delta. The displayed functional remains well-defined, and none of its numerical upper bounds is thereby disproved.

## 4. Reserve adequacy is a separate question

For 0<=y<1, -ln(1-y)<=y/(1-y), e.g. integrate 1/(1-u) on [0,y]. Also ln2>2/3 (integrating the convergent atanh series at1/3 already gives2/3 from its first term, with a positive tail). Thus

    delta <= t^2/[2 ln2(1-t^2)]
          < (3/4)e^2/(1-e^2) < e^2 <= 2^-26.

All denominators are positive; the last strict inequality uses e^2<1/4. For this source and M=1, A011's claimed old numerical residual is at least18111/4096 (ignoring the additional nonnegative K sum G). This exceeds2^-26. Consequently THIS witness does not refute numerical reserve adequacy. This is a new scope check on the objection, not a repair of its EVERY-policy theorem. A bound for ONE query cannot be summed over arbitrarily many queried nodes without a common account argument.

The corrected residual for the physical transaction bill is

    K I(F)-U-[CE_root+sum e] = K I(F)-U-L - sum delta_v.

The first unproved policy implication is an upper bound on this accumulated sum from the SAME unused original reserve for EVERY admitted tree, or a precisely stated accounting convention that explicitly books its release. A bound on L alone does not provide that implication.

## 5. Executed tests and independence

The checker is written independently from the authors' implementations. It reconstructs spectra from integer Walsh transforms of labelled truth tables, checks child amplitudes using both direct transforms and the signed restriction identity, constructs COMPLETE raw/normalized inherited references, checks exact rational normalizers and zero fibers, and validates (A) and its local form using rigorous outward log intervals. The proof of equality is sections1-2; interval overlap alone is explicitly only a diagnostic. The witness's strict sign has a separate exact rational product certificate, not just a floating entropy difference.

The frozen domain is every labelled Boolean function n=0..3; all physical root queries, initial mixing1/4 or1, signed reset mixing1/4 or1, mass1 or1/2; complete fixed-order trees for all functions n<=2 and all variable orders; and compressed witness b=12,13,16,24,40. Constants, n=0, full reference-only fibers and subprobability mass are included. No symmetry quotient or automatic dimension increase. Finite cases check the implementation; they do not replace the all-dimensional finite-algebra argument or imply universal FEI. Main/pilot results and any formal-check limit are recorded separately in REPORT and out/.

## 6. Source quantifier and carried manuscript inventory

The 37-route recovered manuscript inventory is carried byte-identically in out/RECOVERED_GAP_MAP.json. It separates equivalences, one-way sufficient criteria and proved classes. No fresh manuscript theorem is asserted. The present review changes only the downstream use of A011 v5 as a complete physical transaction payment. It leaves its conditional terminal-functional theorem unrefuted and its numerical bounds unreviewed here.

Even a full policy repair leaves the universal supplier line: produce, without assuming FEI, ONE absolute C0 such that EVERY Boolean core has a complete subprobability reference R_g with CE(P_g,R_g)<=C0 I_g. Gibbs gives H<=CE, and conversely R_g=P_g gives CE=H. Thus that existence statement is exactly FEI(C0), not an easier initial condition. Reusing K=4C0+15 cannot create or improve a uniformly supplied C0. A genuinely decreasing, well-founded source construction would need a new proof.

Independent-review verdict for A094 accounting claim: HOLDS at its full named scope without substantive repair. Section4 adds a separate reserve-scope clarification. It supplies no repair to A011's all-policy payment and does not count as independent acceptance of A011's full numerical dependency chain.
