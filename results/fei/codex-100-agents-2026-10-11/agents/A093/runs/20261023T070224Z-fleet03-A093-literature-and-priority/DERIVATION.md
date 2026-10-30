# Independent phase-bin review and its classical divergence content

All entropy, cross entropy and KL are in bits. This reviews A097-NONEMPTY-PHASE-BIN-FUNDED-TRANSFER@1, statement hash f8ee94db650f099b036f174a5e9d21989eee7c6110efd02901221b86b631a6a8. No repair of that statement is required. The optional stronger certificate in section3 is A093 contributor work, separately pending review; it is not independent acceptance of itself. No universal initial reference price is inferred.

## 1. Reconstruction of the unchanged claim

Let a take values -1,0,1 on controller bits and b=1-a^2; let h be a Boolean seed on disjoint bits. Put A=Fourier(a), B=Fourier(b), beta=sum B^2. Since ab=0, sum AB=0, and sum A^2=1-beta. Thus the stated coherent Q has total mass1 when R is normalized with R(empty)=(Eh)^2. Its occupied support remains positive after each physical marginal.

At seed query j write u_T=hhat(T), v_T=hhat(T+j). The physical child amplitudes are u_T+v_T and u_T-v_T. A pre-outcome partition of remaining nonempty seed labels gives c_l=sum_{T in W_l}u_T v_T. Calibrating each individual controller/vacuum atom and each controller/bin block to the actual child masses produces exactly the coherent seed law printed in A097, retaining the inherited conditional law within each bin. Positive true mass has positive inherited mass by support propagation; zero true blocks are assigned zero. This changes relative nonempty weights when needed, without assuming the inherited law already has the right bin masses.

For any two child block laws p+,p- and their SAME inherited block law q, set pbar=(p++p-)/2. Pinsker and the parallelogram identity give

  average KL(p_tau||q) >= sum_i ((p+_i-p-_i)/2)^2 /(2 ln2).

Indeed the average squared Euclidean deviation from q is the squared half-difference plus the nonnegative squared deviation of pbar from q. Half the physical probability difference is 2d B_U(sigma A_U+m B_U) at vacuum and 2B_U^2 c_l in bin l. The Gram minimum gives sum B^2(sigma A+mB)^2>=Gamma=C-D^2/E4. Thus the refund is >=2x/ln2 with x=Gamma*d^2+E4 sum c_l^2, exactly as claimed. For E4=0, beta=0 and no seed tail exists.

The complete-reference query identity is B_query+average CE(child,Qbar)-CE(parent,Q)=-D_occ. Calibration subtracts the actual block KL. Mixing a current tail law M with any normalized prescribed S at epsilon=x/(t+x) retains at least (1-epsilon)M on actual support and costs at most t log2(1+x/t)<=x/ln2. The average of the TWO child liabilities has the same bound; it is not their sum charged at full reach. Hence the complete transaction is <=-D_occ-x/ln2. Current coherence and physical reach make finite-tree telescoping valid without reissuing any ancestor debit. Controller transitions are accepted here only where independently paid/restored coherence is supplied, not as a new upstream chain acceptance.

Separating positive and negative u_T v_T maximizes sum c_l^2: split mixed-sign blocks, then merge like-sign blocks. When d=0, sum_nonempty u_T v_T=0 by Booleanity. Thus x=(E4/2)(sum_nonempty |u_T v_T|)^2. Child squared spectra differ by 4u_T v_T at each nonempty label and have equal vacuum mass. Therefore x>0 iff their spectra differ, for beta>0. The isospectral boundary is exact. This independently reconstructs the unchanged theorem, its constants and its stated nullspace.

## 2. Primary literature overlap, with normalization pinned

Jianhua Lin, *Divergence Measures Based on the Shannon Entropy*, IEEE Transactions on Information Theory37(1),145--151 (January1991), DOI10.1109/18.61115, SectionIV p147, defines the weighted Jensen-Shannon entropy gap. SectionIII equation(3.14) uses the symmetric L divergence equal to TWICE the equal-weight JS; these conventions must not be interchanged. The primary journal-copy PDF states received24October1989/revised20April1990. The inspected copy does not establish a first-ever result or an exhaustive correction/withdrawal history. No absence-of-corrections claim is made.

Source read: https://www.cise.ufl.edu/~anand/sp06/jensen-shannon.pdf . The overlap is the divergence and entropy-gap identity, not A097's specific Boolean coherent wrapper, original account, or source-selection construction. The identity used next is derived directly rather than attributed as a theorem whose exact wording was not checked.

## 3. Optional stronger zero-singleton certificate

For any common finite-CE q, expansion of the logarithms gives the exact identity

  average KL(p_tau||q) = JS(p+,p-) + KL(pbar||q),
  JS(p+,p-)=H(pbar)-[H(p+)+H(p-)]/2.

Suppose d=0. Both child means equal m, so their controller/vacuum block probabilities are identical. Let r_tau be the seed child spectrum coarsened to the vacuum and the TWO sign bins from section1. Every nonempty controller/bin mass is B_U^2 r_tau(l). The common scale cancels in the JS log ratios. Vacuum terms contribute zero, so exactly

  JS(p+,p-)=beta JS(r+,r-).

The sign bins retain the full total variation V=TV(P_h+,P_h-)=(1/2)sum|P_h+-P_h-|=2sum_nonempty|u_T v_T|. Consequently TV(r+,r-)=V. Each r_tau has L1 distance V from its midpoint. Pinsker therefore yields

  actual average calibration refund >= beta*V^2/(2 ln2).

For completeness, Pinsker follows by grouping the positive differences, applying log-sum, and Taylor-expanding binary KL in its first argument. Its second derivative is1/[p(1-p)ln2]>=4/ln2, so binary KL>=2(p-q)^2/ln2, giving KL>=||p-q||_1^2/(2ln2). Endpoints follow by continuity/finite-CE support. No dimensional assumption is needed.

Define y=beta*V^2/4, use epsilon_tau=y/(t_tau+y) for t_tau*y>0, and otherwise do no mixture. The SAME calibrated current law and SAME liability argument now give

  B_query+average CE(child,Qnew)-CE(parent,Q)
     <= -D_occ-y/ln2.

This is a narrow refinement of the zero-singleton supplied-coherent-reference sector. It changes neither the allowed targets nor the exact nullspace, and it does not price an initial source. A097's old energy is x=E4*V^2/8, so the new/old positive-energy ratio is2beta/E4. This is a stronger certificate because the controller scaling is handled exactly in JS before applying Pinsker. It is not a changed value for A097's Gram constant.

For the fixed A079 controller beta=3/8,E4=21/512,Gamma=9/3584 are unchanged. For h=x3 times the two-bit point defect, queried on bit1, m=d=0 and the two child seed spectra are distinct point laws, hence V=1. The old x=21/4096 and epsilon=7/519 become y=3/32 and epsilon=1/5, an energy ratio128/7. Choosing the other child's point law as target gives a STRICTLY POSITIVE child reset liability, beta log2(5/4). The exact original incoming reference is actual, occupancy KL is0, and the paid calibration refund is beta bits. Full signed increment is therefore (3/8)log2(5/8)<0. Both full terminals remain. The guarantee <=-3/(32 ln2) is weaker than this exact negative increment, as required. These are different certificates for the SAME example, not a revised old constant or source rate.

## 4. Adversarial endpoints and first unpaid line

If beta=0, the seed is physically absent and no change is authorized. If a child tail is0 it costs no mixture. If V=0 and d=0, the new y and old x both vanish. Parity3 with its exact reference has such an influence-one query and no erasure, occupancy or calibration refund; forcing a1/64 profile change toward an unoccupied singleton costs (3/8)log2(64/63)>0 on each child. Thus the strengthened estimate still gives NO bound y>=c*Inf_j for positive c. Constant seeds and reference-only bins use the explicit zero-mass conventions above; no constant leaf's old CE is silently erased.

The first unsupported universal line is an influence-priced initial coherent source for arbitrary seeds, or a NECESSARY isospectral zero-energy profile conversion paid from actual unused original surplus/occupancy with old debits and both terminals retained. A selected-source construction could avoid some such resets; this review does not establish necessity for every possible FEI proof. More phase lower bounds on this same nullspace cannot solve that missing step.
