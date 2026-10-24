# Rare-core source payment through adaptive data histories

Status: analytic derivation, finite checks pending; independent review pending. Full FEI OPEN. All entropy/KL units are bits.

Let n>=3, e=2^(-n), v_n(z)=1-2*1{z=0}, and F(x,a,b,z) equal (-1)^a when x=0, v_n(z) when x=b=1, and +1 otherwise. Controls and data are independent uniform bits. P is the actual squared Walsh law. M is its ORIGINAL completed canonical occupancy projection, matching P(empty) and every inclusion marginal; A=D(P||M). Query a first, then any deterministic finite adaptive stopping tree querying only unexposed data coordinates in each branch. Retain x,b at all leaves, both a branches, every physical outcome and all source-zero reference rows (fair kernel extension). No intermediate reference is renewed.

Write H0=H(F), I0=I(F), Hf=E H(leaf), If=E I(leaf), D=H0-Hf, R=I0-If, S=4If-Hf. The complete source liability is L=A+[D-4R]_+. A previous conservative booking omega is an additional debit, not a new bank.

Claim under verification: for every such history and 0<=omega<=7/16, S-L>7/16 and hence S-L-omega>0. This is a scoped eligibility theorem; it does not assume a universal price-four FEI bound.

## Exact root
Put m=1-e. The spectrum has two atoms m^2/4, two atoms 1/4, and (4/e-2) atoms e^2/4. Therefore
H0=2+n e(2-e)-m^2 log2(m)>2,
I0=1+(n+1)e/2.
The marginals are 1/2,1/2 and n+1 copies e/2. Subadditivity for M gives
H(M)<=2+(n+1)h2(e/2).
Matched canonical moments give A=H(M)-H0, so A<(n+1)h2(e/2).

The projection exists: V=1-P(empty)>0 and r_i=d_i/V lie strictly between zero and one, sum r_i>1. The strictly concave function 1-c-product_i(1-c r_i) has its zero at zero, positive derivative there and negative value at one; it has a unique positive root c in (0,1). The law with M(empty)=P(empty) and M(T)=V/c product_i (c r_i)^(1{i in T})(1-c r_i)^(1{i notin T}) for T nonempty has the required normalization/moments and positive mass on every source atom. Affineness of log M on nonempty atoms proves the entropy-gap identity.

## All adaptive data histories
At each a outcome there is a unique path on which every exposed data bit is zero. Let k0,k1 in {0,...,n} be the number of remaining data bits at its terminal in the respective a branches. Off that path, the function is a constant in a=0 or a character of x in a=1. Additional data queries there change no actual H or I. Data order and branching away from the zero path do not change the following exact formulas.

Let P_d be the d-bit point defect, with entropy J_d. On the surviving zero path, the a=0 terminal is P_(k0+2); the a=1 terminal is a sign times character-x times P_(k1+2). Character multiplication permutes Fourier masses, hence both have entropy J. Their influences are (k0+2)2^(-k0-1) and 1+k1*2^(-k1-1), respectively. The zero-path probabilities are e*2^k0 and e*2^k1. Thus
If=1/2+e(k0+k1+2)/4,
Hf=e[2^k0 J_(k0+2)+2^k1 J_(k1+2)]/2.

For d>=2 and delta=2^(-d), the exact entropy is
J_d=-(1-2delta)^2 log2((1-2delta)^2)+8(d-1)delta(1-delta).
The bound -r log2(r)<=(1-r)log2(exp(1)) gives
2^k J_(k+2) <= [2(k+1)+log2(exp(1))](1-2^(-k-2)).
Consequently S>=2-e log2(exp(1))>2-3e/2. This bounds the SAME actual final bank for every history; it is not a sum of new banks.

## One complete liability
Two finite KL chain rules for frequency erasure and the SAME actual coherent kernel give A=E_total+O_total+mean terminal inherited KL. On source-zero fibers the reference remains and the kernel is fair. This identity holds through every finite adaptive history. Every term is included in A exactly once.

Pure algebra gives
S-L=min(S-A,Sroot-A), Sroot=4I0-H0.
The root is an eligibility condition, not a second owner. Moreover
Sroot-A=4I0-H(M)>=2+2(n+1)e-(n+1)h2(e/2).

Let a_n=(n+1)(n+5/2)/2^(n+1). Since log2(exp(1))<3/2,
(n+1)h2(e/2)<a_n.
For n>=3, a_n decreases and a_3=11/8; the ratio comparison reduces to n^2+3n/2-2>0. Also 3e/2<=3/16. Therefore
S-A>2-3e/2-a_n>=7/16,
Sroot-A>2-a_n>=5/8.
This proves S-L>7/16. An old booking omega<=7/16 leaves a strictly positive residual. All final entropy and full inherited reference liabilities remain in this one account.

## Boundary, hypotheses and next unpaid step
No statement here permits x or b queries after the data history, arbitrary cores, or a fresh product reset. Adaptive means deterministic decision rules on the physical outcomes, finite and querying only fresh data; any independent finite randomization is a convex combination and satisfies the same strict bound. n>=3 is used only in the uniform numerical envelope; n=1,2 are diagnostic boundaries, not silently admitted.

After revealing all data and then x (keeping b), the actual final bank is 2e: it can shrink sharply. The all-data terminal bank before x is exactly 2. The earliest unsupported extension is payment from the SAME bank after such a controller exposure; the source liability A and old omega must not be renewed or deleted. The verifier will test whether that extension actually fails at small n.
