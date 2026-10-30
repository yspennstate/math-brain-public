# Actual f6 iterates: bias closure and a high-erasure rare core

All cubes are uniform, outputs are signs, and entropies use bits. Let h be negative exactly on binary indices {0,1,2,4,8,16,32,6,17,40}; bit zero means sign +1. Its negative set consists of zero, the units and three disjoint paired units. Thus h is unate (decreasing in each sign variable). Let g0=h. For each of the first three steps, orient six identical disjoint copies of the previous core to chosen negative probability p=s if s<=7/32, or p=1-s otherwise, where s is its actual minority probability. Define g_(j+1)=h(oriented g_j in six copies). This is an explicit finite Boolean circuit, on 6^(j+1) actual inputs; it requires no hypothetical spectral realizability. After g3, audit both possible common signs separately.

## Physical and spectral identities, reconstructed independently

Let m=1-2p, v=4p(1-p). In one outer coordinate write h=A+y_j D. For each subset T of the other five coordinates, coefficients in the normalized biased basis are a_T,d_T. The corresponding squared parent/derivative packets are U_T=(a_T+m d_T)^2 and D_T=d_T^2. The checker constructs them directly from 32 actual conditional sections: compute expectations of A or D times product_(t in T)(y_t-m), then divide the square by v^|T|. No square root or irrational algebraic coefficient is needed.

Enumerating actual outer pivotal events gives

q(p)=E D^2=2p(1-p)^3(2-p), E D=-q,
alpha(p)=P(h=-1)=(1-p)^4(1+4p-2p^2).

All six q values agree by a separately checked physical enumeration. The matched-pair automorphisms are transitive on outer coordinates. Identical disjoint core copies recursively preserve transitivity on every physical input, even when their common output sign changes. Hence every computed physical coordinate ratio is the actual minimum, with no hidden new-coordinate sector.

For a physical core coordinate let d=Inf_i(g), t=ghat({i})^2. With Phi(x,y)=(x+y)log2(x+y)-xlog2x-ylog2y, the exact signed empty-row correction is

R_p(t)=sum_T Phi(U_T,t D_T)-q Phi(m^2,t).

Disjoint-block Fourier expansion, homogeneity of Phi and Parseval on every occupied other block give B_(j,i)(F)=q B_i(g)+R_p(t) and Inf_(j,i)(F)=q d. The coefficient of its singleton is E D times the chosen core singleton, so t'=q^2 t. In this unate transitive family the seed has t=d^2 and every iterate retains it. No assumption that arbitrary cores have singleton equal to influence is used.

The biased outer spectrum is the 64-atom law with entries U_T and v D_T. Its expected degree is 6v q, checked exactly by the code. The normalized nonempty inner law has mass v and conditional entropy (H(g)-h2(v))/v. Unique occupied blocks give the full entropy and influence recurrences

H(F)=6q H(g)+C_p, C_p=H_p(h)-6q h2(v),
I(F)=6q I(g), n'=6n.

Thus the certificate retains the entire terminal core entropy and signed C_p at each step. The compressed representation is an exact circuit certificate, not an approximation to a 1296- or 7776-bit truth table. Seed coefficients and all influences are separately checked using integer Walsh and physical edges on all 64 entries.

## Rigorous logarithm enclosure

For x>0 reduce x=2^k y with 1<=y<2 and set z=(y-1)/(y+1). Enclose z with outward dyadic bounds of denominator 2^128. The positive series

ln y=2 sum_(j=0)^31 z^(2j+1)/(2j+1)+tail,
0<=tail<=2 z^65/[65(1-z^2)]

is increasing in z. Evaluate its lower sum at z_lower and its upper sum plus tail at z_upper. Enclose ln2 by the same series at z=1/3, divide positive endpoints and add the exact integer k, then round outward at denominator 2^80. No floating-point value selects an orientation or certifies an inequality. Float displays in outputs are diagnostics only. The 32-term tail, rather than the rounding grid alone, determines the rigorous width.

## Rare bias is absorbing under either output orientation

For 0<s<=1/16, the two possible next minority probabilities are

1-alpha(s)=12s^2-28s^3+27s^4-12s^5+2s^6 <=12s^2,
alpha(1-s)=s^4(3-2s^2)<=3s^4<=12s^2.

The first upper bound follows because -28s+27s^2-12s^3+2s^4<0 on this interval (drop the negative cubic and use 27s+2s^3<28). Also alpha(s)>1/2 and alpha(1-s)<1/2 there, so these are indeed the minority probabilities. Both are positive. Consequently 0<s_next<=12s^2<=(3/4)s. For every future sign sequence, induction yields 12s_j<=(12s_0)^(2^j). This is a rigorous all-depth bias statement, and it proves the admission band [1/16,1/2] cannot be re-entered after exit through either output sign.

## Certificate interpretation and first unsupported line

The frozen checker audits the first three prescribed compositions and both fourth-level signs. A084-F6-CONTINUUM-ADMISSION@1 supplies the motivation and threshold 7/32 but is not a proof premise: every selected reserve is enclosed directly from exact packets. It does not certify the whole A084 continuum theorem. Execution passed 273 assertions. The actual orientation sequence is g1=h(g0^6), g2=h((-g1)^6), g3=h(g2^6). Their physical dimensions are 36, 216 and 1296. Exact endpoint inequalities in out/VALIDATION.json and the postprocessed out/CERTIFICATE_SUMMARY.json prove

E(g3)>669/200, 0<p_min(g3)<1/16,
E(h(g3^6))<669/200, E(h((-g3)^6))<669/200.

Both next signed reserves are strictly negative, at every physical coordinate by transitivity. Display values are E(g3)=3.348387256498542..., p_min=0.0222749348295741..., while its two 7776-bit children have E=3.344736180289902... and 3.338222225318484.... Their actual H/I ratios are approximately 5.070175 and 5.052719; g3 has H/I approximately 5.009978. Every ratio is finite. The threshold 669/200 is chosen by rigorous comparison of the already frozen cases, not by searching another family.

These certified inequalities refute the candidate extension 'every core with E>=K6 admits a common sign with E(h(g^6))>=E(g)' and disprove high-E rare-bias exclusion at the demonstrated finite threshold. More sharply, they refute the fixed-threshold implication E(g)>K => some common sign has E(h((sign*g)^6))>K at the rational K=669/200, which exceeds both the original K6 and the finite six-bit high-E guard 14/5. They do not refute A084's theorem within its stated band or A089's fixed-bias criterion, and do not refute a guarded statement with a larger threshold or an additional owned negative-reserve budget. They supply no unbounded H/I sequence.

First unsupported universal line remains a signed negative-reserve payment or another actual gain-preserving operation in the reached rare sector, with every physical influence and terminal entropy retained. The absorbing map excludes repair by merely choosing the other output sign to return to the safe bias band. It does not bound all-depth H/I, prove divergence, or pay C_p globally.
