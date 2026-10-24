# Independent review and prescribed witness bank

All entropies are in bits. The physical cube is uniform. Transcripts are actual fresh-coordinate stopping transcripts; no leaf bill is suppressed.

## A083 review: retained root versus terminal reset

In one AND-sign block the truth table is (1,1,1,-1), and its Walsh-square law is uniform on four masks. The first physical query has a constant child and a character child. Keeping the original mask, the coherent joint has two masses 1/4 at the stopped first-zero transcript and four masses 1/8 at the first-one/second-bit transcripts. Therefore H(Pi)=3/2, H(S)=2, H(S,Pi)=5/2. The residual label is empty, so H(Pi|S)=1/2 and H(Pi|W)=3/2. The difference is exactly one bit, with influence one. Tensor multiplication of disjoint blocks preserves the branch kernel because unqueried tensor factors cancel from its numerator and denominator. Consequently every formula in A083's all-r statement follows by entropy additivity and E f=2^-r. The sign of C_root for r=1 is -1+(3/4)log2(3)>0, since 27>16; C_reset=-2+(3/4)log2(3)<0, since 27<256. This does not refute retained-root conversion or FEI.

The rational transport theorem is also valid: off zero rows ((a+b)/2)a/(a+b)=a/2; when a+b=0 and a,b>=0, both vanish, and any fallback transports zero mass. The 1/2 fallback normalizes the two branches. Lean source and its printed axioms were inspected; this stage independently checks the algebra and Boolean interpretation, and does not claim to have rerun Lean. Formal scope remains local rational transport.

## A050 review: exact deletion capacity

Let S be the root label, Q(Pi) the queried mask, D=S intersect Q, W=S\Q, and A a fixed superset of possible queries. Given S, D and W are inverse encodings and both are determined by Pi. Thus e=I(W;Pi|S)=H(D|S). Each label is deleted at most once. The conditional current spectrum is the restricted Fourier law; its queried-coordinate marginal is actual uniform influence. Therefore E|D|=R=I(f)-E I(f_leaf). Restriction preserves expected influence of every coordinate other than the queried coordinate; telescoping over coordinates in A gives a-R=E I_A(f_leaf), where a=I_A(f).

Conditionally on S, independently delete each label of S intersect A with probability theta. This defines the normalized reference rho_theta(d|S)=theta^|d|(1-theta)^(|S intersect A|-|d|). Its mean cross-entropy is -R log2 theta-(a-R)log2(1-theta). Subtracting conditional KL gives H(D|S) exactly, and choosing theta=R/a proves e<=a h2(R/a). Endpoints are point masses. This verifies the reference normalization, rather than assuming a schedule code funds a different history bank.

If all leaves are independent of A, a=R, hence D=S intersect A almost surely and W=S\A. Conversely root-Markov compatibility is exactly e=0 by conditional mutual information. If a-R<=kappa R, monotonicity of t h2(1/t) gives the stated bounded-reservoir clause.

For completeness, the channel information is bounded by 2R/ln2. In each erased spectral fiber the natural-unit fair binary channel divergence g(z) has coefficients 1/[2k(2k-1)] in z^(2k); those of 1-sqrt(1-z^2) are binom(2k,k)/[4^k(2k-1)]. The latter dominate, since b_1=1/2 and b_(k+1)=b_k(2k+1)/(2k+2) imply b_k>=1/(2k) inductively. Multiplication by fiber mass gives (|G|-|H|)^2/2 <= (G-H)^2/2, and Parseval gives J_v<=2 Inf_i/ln2. The retained-root channel chain gives j=I(S;Pi)<=2R/ln2. Actual output information satisfies o<=R, because conditional on every physical history the remaining coordinates are independent and I(X_i;Y)<=H(Y|X_-i)=Inf_i; sum the chain with reach weights. Finally j_W<=j+e by the information chain, so max(o,j_W)/2<=R/ln2+e/2. No positive cost is dropped when Gamma_W=j_W-o changes sign.

Sharpness also survives independent reconstruction. On r point-defect blocks h_k times parity on 2^r fresh indexed coordinates, query one bit per defect, then the parity bit indexed by the r observed outcomes. Write d=2^(1-k), v=4d(1-d), j_k=h2(v/2)-h2(v)/2. Each defect's branch information is j_k, independently, and the retained parity witness recovers the complete index. The subsequent parity outcome changes only signs and is independent of the spectral/index joint. Thus e=r(1-j_k), a=2^r+rd, R=1+rd. Taking k=2r+2 gives r j_k<=2rd/ln2->0 and a h2(R/a)=r+log2(euler_number)+o(1). The capacity coefficient one is sharp. This is a schedule-capacity claim, not a full-history or FEI claim. We accept A050 v1 unchanged at this exact scope.

## Actual three-output shared-control family and complete reference

For m>=1, take independent controller bits z_1,...,z_m,a,b and shared data u,v. Let Z=AND(z_1,...,z_m), g(u,v)=(-1)^(u+v), h(u,v)=1-2*1_{u=v=1}, and

    F_m = g if Z and a; else h if Z and b; else +1.

Query z bits in order and stop at the first zero. If all are one, query a, stopping at g when a=1; otherwise query b and stop at h or +1. Every queried node is essential. The terminal data cores remain nonconstant on positive-probability leaves. Let t=2^-m, A={z_1,...,z_m,a,b}, and use the actual coherent W=S\Q. All leaves are independent of A, so W=S intersect {u,v} almost surely and e=0.

Fix one complete conditional reference: rho(pi|w)=P_physical(Pi=pi), independently of w. Early-zero transcripts have probabilities 2^-j, j=1,...,m. The g, h and last constant transcripts have probabilities t/2,t/4,t/4. Their sum is one. This is a normalized stopped-tree reference on every possible W; no future side information or root-dependent reference choice is used. Its expected code length is H(Pi)=2-t/2 and its conditional KL rebate is I(Pi;W). Thus the exact reference-side conditional cost is H(Pi|W)=H(Pi)-I(Pi;W).

The actual inherited data spectrum is

    P(W=empty)=1-11t/16,
    P(W={u})=P(W={v})=t/16,
    P(W={u,v})=9t/16.

Indeed g contributes only its parity mask with reach t/2, h contributes each of its four masses 1/4 with reach t/4, and every other leaf is constant. Write h_W=H(1-11t/16,t/16,t/16,9t/16). Conditional on Pi the W law is precisely the actual leaf Fourier law, whose expected entropy is t/2. Hence

    H(Pi,W)=H(Pi)+E H(f_leaf)=2,
    H(Pi|W)=2-h_W,
    I(Pi;W)=h_W-t/2.

For the inner priority G, P(G=-1)=5/16, Inf_a(G)=5/8, Inf_b(G)=1/8, and expected terminal data influence is 5/4. Direct pivotal counting therefore gives

    R=a=t(5m/8+3/4), I(F_m)=t(5m/8+2),
    E I(f_leaf)=5t/4, E H(f_leaf)=t/2.

Since h_W->0 and R->0, H(Pi|W)/R->infinity. The exact statement refuted is: there exists an absolute K such that H(Pi|W)<=K R for every such controller-complete shared-core priority tree, even with e=0 and this prescribed actual Fourier witness. It also refutes the analogous bound with I(F_m) in place of R. It does not refute a joint signed residual payment, A050 conversion, a different witness retaining transcript side information, or FEI. At m=6 the exact certificate proves H(Pi|W)>16R, with R=9/128 and 16R=9/8. The atanh bounds prove this strict inequality; floating displays are not used as a sign certificate.

This family's own Fourier entropy is <4I. To see it directly, its nonempty root Fourier mass is v_0=Var(F_m)=(5t/4)(1-5t/16). For m>=1, t<=v_0<=5t/4. With n=m+4, elementary support counting gives H(F_m)<=h2(v_0)+v_0 n. The inequality h2(x)<=x(log2(1/x)+log2(euler_number)), together with log2(euler_number)<2 and log2(1/v_0)<=m, yields H(F_m)<(5t/4)(2m+6)<4t(5m/8+2)=4I(F_m). Thus the unbounded conditional-bank ratio is a route obstruction with an explicitly bounded FEI ratio.

## Exact signed ledger and first unsupported universal line

Let M=sum reach times erased-sector entropy, J=I(S;Pi), B=H(Pi|W), j_W=I(W;Pi), and L=E H(f_leaf). The exact residual is Sigma=H(Pi)/2+M-J. The full ledger is

    H(F_m)=L+2M+B/2+j_W/2-Sigma.

No term has been replaced by a nonnegative surrogate. Since W is a fixed projection of S, the root-to-W bank increase is J-j_W=I(Pi;S|W), nonnegative and <=2R/ln2; half costs at most R/ln2 once. This removes the injection issue without supplying B. As m grows, H(F_m), L, J and M tend to zero, B/2 tends to one, and Sigma tends to one. The large bank is cancelled by the signed residual. Separately paying B/2 by influence destroys this necessary cancellation.

FIRST UNSUPPORTED universal line: construct one normalized reference whose joint signed cost L+2M+B/2+j_W/2-Sigma is bounded by a single exclusive multiple of I for arbitrary unfinished shared-core trees. The independent physical transcript reference above prices B exactly but fails as a standalone influence code. The next mechanism must preserve the cancellation or use certified terminal/core slack, rather than repeat that false separate-bank inequality.
