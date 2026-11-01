# A scoped dyadic weak-L2 theorem for canonical QFORM

**Status:** Proved under summable square-root P-bin masses; in particular under bounded centered variance of genuine original product inputs. This does **not** settle the unrestricted arbitrary-fragmented-input RW2 problem.

Let independent three-dimensional bank vectors A=(L_A,V_A,P_A), B=(L_B,V_B,P_B) have joint densities bounded by M_A,M_B, and put (L,V,P)=A+B. Define m_{A,k}=Pr(P_A∈[k,k+1)), likewise for B, and assume S_A=Σ_k√m_{A,k}<∞, S_B<∞. For arbitrary real β,ε,s, r>0, finite-measure Borel E⊂R, and interval I, set q(h)=2hL+βL²+V²+2εLP. Then

∫_E Pr{r≤|L|≤2r, q(h)∈I} dh
≤ 4√2(√2−1)√(M_A M_B) S_A S_B |I|√(r|E|).                         (1)

This is the conjectured dyadic RW2 estimate in a scoped product-source class, uniformly in β and ε (indeed with no spectral gate needed).

**Proof.** First let g(l,v) be a nonnegative planar subprobability density bounded by M. For fixed c, β and target s, change v through its square. With an arbitrary interval E of hub values and r≤|l|≤2r, the conditional level density integrated over E is at most

M ∫_{r≤|l|≤2r}dl ∫_E dh [s−2hl−βl²−2cl]_+^{−1/2}.

One-sided rearrangement gives ∫_E [s−2lh−βl²−2cl]_+^{−1/2}dh≤√(2|E|/|l|), independently of c and s. Since ∫_{r≤|l|≤2r}|l|^{−1/2}dl=4(√2−1)√r, this yields 4√2(√2−1) M√(r|E|). Integrate s over I to obtain the interval form, which avoids pointwise-density version issues.

For the 3D convolution density F=a*b, set F_p(l,v)=F(l,v,p), and let M(p)=(2π)^{−2}∫_{R²}|Fourier_{l,v}F_p(ξ)|dξ. Then F_p≤M(p) almost everywhere. The archived finite-P slice Wiener lemma gives ∫M(p)dp≤√(R_A R_B M_A M_B) whenever the respective bank P supports have lengths R_A,R_B; it follows directly by Cauchy–Schwarz in P, then in planar Fourier space, and Plancherel. For the subprobability banks restricted to bin k and j, the P support lengths are one and their squared L2 norms are ≤M_A m_{A,k}, ≤M_B m_{B,j}; hence their convolution satisfies

∫M_{k,j}(p)dp≤√(M_A M_B m_{A,k}m_{B,j}).

For fixed p, q(h)=2(h+εp)L+βL²+V². Apply the planar estimate to F_{k,j,p}; translating E by εp preserves its measure. Integrate p, and then sum the nonnegative output interval laws over all bin pairs. This gives (1).

**Moment corollary.** If a bank scalar Z=P_A has Var(Z)≤V_A, then S_A≤C(1+V_A)^{1/4}. To prove it, set R=max(1,√V_A); split each bin's mass into its intersections with the central distance region |Z−EZ|<R and outer shells 2^jR≤|Z−EZ|<2^{j+1}R. Subadditivity √(Σ_jm_{k,j})≤Σ_j√m_{k,j}, Cauchy–Schwarz over at most C2^jR bins, and Chebyshev shell mass≤V_A/(2^jR)² give a convergent series C R^{1/2}Σ_j2^{−j/2}. Apply similarly to B, yielding RW2 constant ≤C√(M_A M_B)(1+V_A)^{1/4}(1+V_B)^{1/4}.

Finally, for independent original-coordinate leaf Xi with density≤1 and Var(Xi)≤V0, orthonormal ℓ,v,p rows with max leverage≤1/24 admit a random physical two-bank cut whose two 3D Gram matrices are ≥I/4: E||G_A−I/2||F²≤(3/4)(1/24)=1/32<1/16. Standard three-dimensional projection density bounds give M_A,M_B≤M3 absolute, while Var(P_A),Var(P_B)≤V0. Therefore (1) holds for this genuine-product canonical form with a universal constant times (1+V0)^{1/2}; independent physical hub H needs only density≤1 to integrate the RW2 estimate. Original cap-one laws with no moment condition are outside this argument.

The finite-P Fourier slice ingredient is proved in `proofnet24/QFORM-density/interactive/20260923T205630Z-finite-p-support-fourier/ALL_BETA_ADDENDUM.md`; the full RW2 target and its role are in `proofnet24/QFORM-density/interactive/20260923T205500Z-dyadic-rw2-hub-target/REPORT.md`.
