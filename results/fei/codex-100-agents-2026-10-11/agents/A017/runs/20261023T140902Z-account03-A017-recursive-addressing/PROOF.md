# Character overlap can be removed from a bound, but not the spectator obstruction

Uniform ORIGINAL physical cube, Boolean signs, entropy in bits. All author proofs below await independent review. Full FEI is OPEN. Write Delta_i(f)=H(f)-[H(f_0)+H(f_1)]/2. Real-function influence is the full Dirichlet energy sum_S |S| hhat(S)^2, equivalently sum_j E(h(x)-h(x^j))^2/4.

## 1. Exact character correction on overlapping physical coordinates

For any real h on m physical bits, let p=E h^2 and e_j=E(h(x)-h(x^j))^2/4. Then 0<=e_j<=p. For any ORIGINAL character chi_T,

 I(h chi_T)=I(h)+|T|p-2 sum_(j in T)e_j.                 (1)

Indeed an edge in T replaces (h-h')^2 by (h+h')^2, and e_j is replaced by p-e_j; other edges are unchanged. Thus the exact minimum over all physical characters is

 E_*(h):=min_T I(h chi_T)=sum_j min(e_j,p-e_j)
        =(1/2)sum_j[p-|E h(x)h(x^j)|].                (2)

Choose T={j:e_j>p/2}. This is an identity for the actual overlapping physical support, without independence or renewed influence. It repairs the character case of the stage20 failed p I(c) refund: the correction is |T|p-2 sum_T e_j, not |T|p. Neither term is a newly available source of payment.

## 2. A universally valid two-sector bound

For a selected original coordinate i, put D=(f_0-f_1)/2, A=(f_0+f_1)/2, p=Inf_i(f)=||D||_2^2; then ||A||_2^2=1-p. Multiplying f by any physical character permutes squared Fourier coefficients, preserving H(f). Each full child is multiplied by an unqueried character and possibly a constant sign, so Delta_i(f) is also invariant. Multiplication by chi_i exchanges the roles of A and D. Applying B04's established one-node bound Delta_i(g)<=3 Inf_i(g)/ln2+2 I(D_i g), and then (2), gives

 Delta_i(f)<=Gamma_i(f):=min{
   3p/ln2+2 E_*(D),
   3(1-p)/ln2+2 E_*(A)}.                             (3)

This is a direct character-invariant application of the existing bound, not a new proof of that bound or a novelty claim. The sector with mass 1-p is used only to bound the SAME actual entropy debit. The physical influence available to spend stays p. No changed function is installed in the actual tree, no shared gate is refreshed, and both original full children remain in the entropy ledger.

For completeness, the bound used in (3) has the following self-contained derivation. In each selected Fourier pair u=fhat(S),v=fhat(S+i), set q=u^2+v^2. The parent entropy is H(q)+B_i and the average child entropy is H(q)-JS_i, so Delta=B_i+JS_i. Conditional entropy concavity gives B_i<=h2(p). For z=2uv/q, the natural-log JS integrand J(z)=[(1+z)ln(1+z)+(1-z)ln(1-z)]/2 satisfies J(z)<=1-sqrt(1-z^2). It is even; on [0,1), its derivative atanh(z) is at most z/sqrt(1-z^2), because the derivatives 1/(1-z^2) and (1-z^2)^(-3/2) have that order and both functions vanish at zero. Integrating proves the inequality, including endpoints by continuity. Thus JS_i<=2 sum_S min(u^2,v^2)/ln2<=2p/ln2. Also h2(p)<=p log2(1/p)+p/ln2. The support E of D has measure p. Its indicator energy is at most I(D), and cube edge isoperimetry gives I(1_E)>=(p/2)log2(1/p). An elementary proof of the latter is induction on dimension: if the two slices have sizes a,b, the cross-boundary has at least |a-b| edges; the induction reduces to h2(a/(a+b))>=2 min(a,b)/(a+b), which follows by concavity on the two half intervals. Hence Delta<=3p/ln2+2I(D), as required. Cases p=0,1 follow by limits or direct substitution. This recalls an established estimate, and makes the present implication independent of an unexamined theorem locator.

For any physical stopping tree, reach weights w_v and actual spent original influence P_T=sum_v w_v p_v, the exact entropy telescope therefore implies, for every kappa>=0,

 H(f)<=kappa P_T+E H(full leaves)
       +sum_v w_v max(0,Gamma_v-kappa p_v).           (4)

This is valid at arbitrary overlapping reached cores. It supplies a corrected upper estimate; it does not bound the final adverse sum by O(I(f)).

## 3. Even the strongest character correction retains a quadratic proxy bill

Use the actual six-bit b reverified in stage20: H(b)=21/4, I(b)=9/4, chosen p=1/8, Delta_i(b)=delta<Kp, K=4+2/ln2, and B_i(b)>4p. Its physical influence vector is (1/8,5/16,5/16,1/2,1/2,1/2); hence every marginal is <=1/2. Let G_t=A_(b^tensor(t)), where A_h is 1 on p0=0 and (-1)^z h on p0=1, using ONE fresh unqueried physical pair p0,z for the entire tree. All t>=1 are allowed. Query each prescribed selected factor bit exactly once in ANY adaptive permutation, observing only previous selected bits; retain every outcome and full child.

At depth k, the selected factor remains an untouched b and m=t-k-1 other factors are untouched. For any physical coordinate j in those m factors, the current D sector has norm 1/16 and e_j=(1/16)Inf_j(b). Thus e_j<=||D||^2/2, and that coordinate contributes exactly e_j to E_*(D). The A sector has norm 15/16 and e_j=(7/16)Inf_j(b)<=7/32<15/32, also contributing exactly e_j. These identities follow directly by differentiating the product and averaging the ONE shared guard; conditioning the other factors changes neither their Boolean norm nor these untouched marginals.

Consequently BOTH alternatives in (3) are at least 2*(1/16)*(9/4)*m=9m/32. Each full level has total reach weight one, independently of adaptive order. Hence

 sum_v w_v Gamma_v >= 9t(t-1)/64,
 sum_v w_v max(0,Gamma_v-kappa p_v)
       >=9t(t-1)/64-kappa*t/16.                     (5)

I(G_t)=1+9t/8. For every fixed kappa the right side divided by I(G_t) is unbounded. All reached selected nodes still satisfy B_v>4p_v, so that filter cannot eliminate (5). Thus neither exact character minimization nor choosing the cheaper A/D sector repairs this prescribed proxy mechanism. This does NOT refute an existential stopping policy: other physical coordinates are available. It does NOT give an FEI counterfamily. In fact the actual debit remains delta*t/2, and every stopped prefix is paid at SAME K by the stage20 theorem; the actual-Delta adverse filter gives zero here. The failure is strictly the use of a derivative-energy surrogate instead of the actual coupled debit.

## 4. Noncharacter overlap is tested on the actual function

The frozen search consists of b*c, with c every Boolean function on every three-coordinate subset of the five OTHER ORIGINAL coordinates. It has 10*256=2560 descriptions, intentionally retaining lower-support duplicates; i stays the same physical coordinate, p=1/8, and both full children are retained. Integer Walsh entropy is represented as rational prime-log coefficients. Signs against Kp are certified by rational atanh intervals with a proved geometric remainder, not floating-point sorting. ALL 2560 descriptions obey Delta_i(bc)<=delta, with equality at c=1; the maximum comparison is checked against EVERY row by exact prime-log intervals. Every c depending on AT MOST three of the five coordinates occurs in this list. None exceeded Kp. This does not exhaust all Boolean functions on five overlapping coordinates.

A second implementation recomputes the retained maximum witness by direct character sums for root and BOTH full children, then checks its K margin using 256-term UNREDUCED rational logarithm intervals. This is a different author implementation, not external acceptance. The complete finite outcome and witness are in out/certificate.json and out/witness_certificate.json. Main validation: 2560 roots,6144 sector/character rows,37889 exact assertions,20.729 seconds; pilot 1.395 seconds.

The additional independently frozen code/audit_full.py audit reconstructs EVERY one of the2560 roots and BOTH of its full children using direct character sums rather than the primary Walsh transform. It compares every resulting prime-log entropy expression and the maximum bound using256-term UNREDUCED intervals, checks actual physical influence, and includes the positive control delta>4p. Its pass receipt and exact domain are out/independent_full.json and out/audit_spec.json. As with the other checker this is author verification, not a claim of independent-agent acceptance.

This exact finite certificate extends to an unbounded mixed-factor history statement. Choose ANY t>=1 and any fixed factors b*c_a from the certified list on disjoint ORIGINAL six-bit blocks, and put their product inside ONE A_h gate with the same unqueried p0,z. At each node choose an untouched selected factor coordinate, with arbitrary outcome-dependent order or stopping. Its p_v=1/16 and Delta_v=Delta_i(bc_a)/2<=delta/2<K/16. Therefore the whole stopped prefix has actual debit <=delta E[N]/2<K E[N]/16 (strict if E[N]>0). Both full terminal entropies are retained. The exact influence telescope spends E[N]/16 from the original function, keeping the remaining influence in full terminals; no old source or shared gate is renewed. This closes bounded noncharacter reuse for these queries, without paying arbitrary terminal FEI or arbitrary indecomposable overlap.

There is a useful exact sharing corollary. Multiply the ENTIRE root by any ONE fixed physical character chi_T avoiding all prescribed queried coordinates. T may include unqueried core coordinates and the SAME shared p0,z labels at every level. At every reached node it is still a common character, so the actual entropy debit is unchanged and Inf_i is unchanged (the character does not flip along i). Thus the entire stopped-prefix payment remains valid with BOTH full actual terminals and the ORIGINAL influence account of this character-modulated root. No change of function or character is installed during the policy. In particular every seed multiplier c_small*chi_U, with c_small depending on at most three unqueried coordinates and chi_U on any of the five, is covered: nonlinear reuse is bounded, while character reuse may span all five and the shared gate labels. This does not cover arbitrary five-variable nonlinear multipliers.

## 5. Universal frontier

For a general Boolean multiplier c independent of i but sharing other coordinates, the exact edge correction remains

 I(Dc)-I(D)=sum_j E[1_(c(x)!=c(x^j)) D(x)D(x^j)].

The actual entropy correction is Omega_i(b,c)=Delta_i(bc)-Delta_i(b); exact disjoint spectators and all characters have Omega=0. For noncharacters the signed edge identity alone does not price Omega. A024 v6's actual-spectrum B_i<=2 A(f)Inf_i(f) correctly handles interference before payment, but an arbitrary algebra norm is not an unused original influence account. No bound on that norm, renewed terminal budget, or universal source price is assumed here. The first unsupported universal line is to pay the positive coupled entropy correction at a reached overlapping core from the SAME remaining original source after old debits and BOTH full terminals. Equations (1)-(4) are valid universally; equation (5) explains why the corrected energy proxy alone cannot discharge that line.
