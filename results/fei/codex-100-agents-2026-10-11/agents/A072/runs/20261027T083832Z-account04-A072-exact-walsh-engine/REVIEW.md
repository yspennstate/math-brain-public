# Independent review of A084's scalar reserve

The coefficient 9/4 is valid for the supplied coherent bank. Its initialization remains unpaid. The source's sharp coefficient concerns an exceptional row, not the optimal complete composition drift.

Let eta(u)=-u log2(u), eta(0)=0, and

    L(a,b)=eta(a*a)+eta(b*b)-(eta((a+b)^2)+eta((a-b)^2))/2.

L is the COMPLETE entropy decrement of a paired Fourier row. It is the sum of a binary mixing entropy and a Jensen--Shannon concavity gap, both nonnegative. All terms of a scaling logarithm cancel, so L is homogeneous of degree two. Replacing eta(a*a)+eta(b*b) by eta(a*a+b*b) removes the mixing entropy and is an error. This stage caught exactly that mistake in its floating discovery helper; the erroneous v1 outputs are excluded from every conclusion.

For a,b>0 off the diagonal, the mixed derivative is 2 log2((a+b)/|a-b|). Integrating from either axis shows separate monotonicity. The singularity across the diagonal is locally integrable, and the first derivatives extend continuously because u log|u| tends to zero. Evenness covers the other quadrants.

For a Boolean core g and physical coordinate i, put mu=E g, t=ghat({i}), d=Inf_i(g). Both conditional means mu+t and mu-t lie in [-1,1], which gives |mu|+|t|<=1. The derivative takes values 0,+1,-1, so |t|<=d. This uses Booleanity; normalized real vectors alone need not satisfy these constraints. If t=0, L=0 even if d>0. Otherwise monotonicity reduces L(mu,t)/d to ell(b)/b, where b=|t| and ell(b)=L(1-b,b).

On (0,1/2), direct differentiation gives ell''=4 log2((1-2b)^2/(b(1-b))) and ell'''=-4/(ln(2)b(1-b)(1-2b)). Every denominator is positive on this open interval. Thus ell'' decreases through its single zero alpha=(1-1/sqrt(5))/2. For N(b)=b ell'(b)-ell(b), N'=b ell'', N(0+)=0, and N(1/2-)=-1. Consequently N first increases and then decreases through one root beta. The ratio ell(b)/b has its unique maximum there. Symmetry of ell reduces b>1/2 to the smaller argument; endpoints are evaluated continuously. Exact root signs and the enclosure ell(a)/(c ln2)<=lambda<=ell(c)/(a ln2), with ell in nats in the code, give 2<lambda<9/4. Dyadic b realized by one constant positive child and a negative child of minority density b approach beta. This proves primitive scalar sharpness over actual Boolean cores.

For arbitrary disjoint cores under any Boolean outer gate, decompose the outer gate as A+z_j D. Transform A(g_-j),D(g_-j) on the other physical variables. Every nonexceptional Fourier row cancels after subtracting q_j times the inner decrement. The exceptional full rows remain, so

    average C_child-C_parent
      = q_j L(mu,t)-sum_W L(Ahat(W)+mu Dhat(W), t Dhat(W))
      <= (9/4) q_j d = (9/4) Inf_i(F).

Here q_j=E D^2 is unchanged by a query within core j, and q_k for k!=j has conserved conditional mean. This handles constant cores, zero pivotal probability, and zero influence without division. The exact engine checks the signed identity against literal parent and both child spectra, not just normalization.

For every fixed real K>=0, let rho_K be the complete finite physical stopping hull of (H-KI)_+. Then C+(9/4)I is superharmonic by influence telescoping and vanishes at complete revelation. Finite backward induction implies nonnegativity. Each q_j rho_K(g_j) is separately superharmonic, and their sum with C majorizes H(F)-KI(F). This proves the source bank claim for every physical query of a fixed partition.

For ACTUALLY supplied a>=U(parent), assign a_b=U(child_b)+a-average U(children). These child credits are nonnegative, dominate their banks, and average to a. Nonnegative credit labels use a_b/a when a>0; at a=0 both child credits are zero. The debit has sign d_b=KI(F_b)-H(F_b)+a_b and is nonnegative. If its average T>0, transport signed debit labels by d_b/T. At T=0 both total child debits vanish, and cancelling signed labels may retain kernel 1. No full child or already stopped sibling is removed. This is exactly the source's conditional original-owner statement, with no extra supplier premise concealed.

Against the previous rational-3 bank, the required credit falls by exactly 3I/4, releasing only 3 Inf_i/4 in a conditional mean query. This cannot replenish a previously spent owner. Since 0<=H(g)-rho_K(g)<=KI(g), the bank stays between H(F)+(9/4-K)I(F) and H(F)+(9/4)I(F). Its universal initial influence price remains FEI-equivalent. The first unproved line is that initial ORIGINAL O(I) payment, or an eligible different source mechanism on arbitrary indecomposable cores.

Verdict: A084's stated scalar and supplied-bank theorem HOLDS unchanged, as an analytic proof independently reconstructed here. Lean admission was held before compilation; no Lean-checked claim is made. The finite search and certificates are additional engine controls, not an all-dimensional FEI proof.

The literal finite witness has outer mask7 on three bits with queried input2, inner mask3 on three bits with queried coordinate1, and two fresh dictator inputs. Its five-bit truth mask is16579836; physical bit0 is dummy. If l=log2(3), the parent entropy is6-(27/16)l, inner entropy2, and outer pivotal probability3/4. The two full child entropies are4-(9/8)l and2; both inner child entropies are zero. Thus the correction drift is(9/8)l-3/2, while physical query influence is3/8. Their ratio is3l-4>1/2, the final strict inequality following from9>8 by logarithm monotonicity. All spectra and physical edges are reconstructed independently in the witness helper. This refutes only the proposed full-drift coefficient1/2, and is not an FEI counterexample.
