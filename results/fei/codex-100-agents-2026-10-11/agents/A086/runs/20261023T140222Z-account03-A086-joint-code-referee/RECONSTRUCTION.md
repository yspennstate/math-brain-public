# A094 small-padding payment: independent reconstruction

Information is in bits. Reviewed claim A094-SMALL-PADDING-POSITIVE-SOURCE-PATH-PAYMENT@1, statement SHA256 6f875d0de8dc2dbbdcda33d02c52f50ffaff391cfbde15e1f74919945ec520ec, from A094 20261023T131208Z DERIVATION.md sections 2,3,5. Verdict: HOLDS at its stated conditional scope, without repair. A086 authored two dependencies; this conflict is disclosed, so this is an independent reconstruction of the NEW denominator estimate, not a second independent review of A086's own premises.

Write e=2^(-a-m), u=2^-m, N=|supp(g-hat)|. Boolean quantization gives N e<=u, |A|>=2^-a. This includes constant sources and a=0. True data probabilities are A^2-2eA+2e^2 on old source support and 2e^2 elsewhere. The floor is (P_g+3e Uniform)/(1+3e), lifted by the true selector kernel. The complete divergence equals the data divergence, since the conditional kernels cancel pointwise.

The weighted Euclidean triangle inequality bounds old-support chi-square by N e^2 (5+u+6(1+u)e)^2/(1+3e). Put A0=5+u, B0=6(1+u). Direct expansion gives

3 A0^2-2 A0 B0-B0^2 u=15-78u-81u^2-36u^3.

The derivative is negative for u>=0 and the value at 1/8 is 501/128>0. Since e<=u, B0^2 e<=3A0^2-2A0B0, so (A0+B0e)^2<=A0^2(1+3e). Therefore the old contribution is <=(41/8)^2 N e^2. Off-support chi-square is (1/e-N)e^2(1-6e)^2/[3(1+3e)]<=e/3. Using 1/ln2<3/2 gives

Dfloor < (1/2+5043u/128)e = C(u)e.

Every actual finite-cost incoming subprobability has CE-H>=0, including its mass penalty. Hence positive conversion cost is <lambda C(u)e. At source depth k, lambda_k e_k=lambda e; every complementary inherited reference, its full terminal bill, and all prior positive charges are retained. Entry plus d fresh floors cost <(d+1)lambda C(u)e. The minimum nonzero cube edge boundary I_g>=2a2^-a, for nonconstant original g, implies (a+1)e<=u I_g. No descendant influence certificate is issued.

C(1/8)/8=5555/8192; the original A011 supplied owner after old U has >=7I_g/8, leaving >1613I_g/8192. This is a prospective policy from the ACTUAL prescribed root, not a replacement of executed padding history. For the ACTUAL A095 two-narrow-reset child (reach 1/4, four source bits), m>=5 gives C(u)<=7091/4096 and e<=1/512. Five reached floors cost <35455/8388608. Original residual >3/256 therefore leaves >62849/8388608. Rates, U, p1,p2 and both full exits are unchanged.

No strict entry positivity at m=3 follows. No initial arbitrary-source influence price, selector-exposed floor, or arbitrary interacting-edit closure follows from this claim. Its full conditional statement holds; full FEI remains OPEN.
