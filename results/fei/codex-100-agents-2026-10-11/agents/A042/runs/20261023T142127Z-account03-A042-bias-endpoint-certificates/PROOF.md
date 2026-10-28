# Quantified rare activation reinstates the complete seed rounding law

All logarithms are natural. Let g be any finite Boolean sign at an interior
independent product law, with deterministic coordinates already contracted.
For occupied nonempty T use P_T=v_T c_T^2 and choose j_T by
1/2<2^j_T|c_T|<=1. Write W_T=v_T4^-j_T; thus P<=W<4P.
Let A=sum_single P, M=sum_high P, V=A+M=Var(g),
Z_1=sum_single W, Z_h=sum_high W, Z=Z_1+Z_h.
High means degree at least two. Empty sectors contribute zero costs.

The complete all-rounded seed law Q_all freezes P_empty and assigns
V W_T/Z to every nonempty label. The complete paid-sector law Q_* freezes
both actual empty and singleton masses, and assigns M W_T/Z_h on high.
Let K_all=KL(P||Q_all), K_h=KL(P||Q_*), and
K_1=A KL(P_single/A || W_single/Z_1), using zero for an empty singleton
sector. All are ordinary full-law quantities, not entropy after conditioning.

## 1. Actual dyadic activation and its complete KL partition

Let X be independent Bernoulli e=2^-k, k>=1, and F=1-X+Xg. Its occupied
physical coefficients are c_F(T)=e c_T, c_F(XT)=c_T/2 and c_F(X)=-a,
where a=(1-mean(g))/2. Accordingly

P_F(T)=e^2 P_T, P_F(XT)=e(1-e)P_T,
P_F(X)=4e(1-e)a^2.

The ORIGINAL deficit remains
Delta_F=e Delta_g+e(1-e)V. No seed bank is renewed.
Dyadic scaling gives W_F(T)=e^2 W_T and W_F(XT)=e(1-e)W_T.
Use the complete paid-sector reference Q_*,F at the actual final function.
Its low labels are exactly actual, including the full empty atom.
Its high sector is the disjoint union of:

* imported seed singletons XT, total physical mass e(1-e)A and raw
  reference mass e(1-e)Z_1;
* seed high labels T and XT, total physical mass eM and raw reference
  mass eZ_h. Within this sector both laws have the same placements
  probabilities e and 1-e for each conditional seed label.

Thus H_F=e[M+(1-e)A] and Z_h,F=e[Z_h+(1-e)Z_1]. The exact full ordinary
KL chain rule, including zero low likelihood ratios, is

K_F=e K_h+e(1-e)K_1
    +H_F d_Bern((1-e)A/[M+(1-e)A] ||
                (1-e)Z_1/[Z_h+(1-e)Z_1]).              (1)

This identity preserves BOTH complete terminal laws. It is not an independent
Boolean reset or the complete composed reference. The latter has K_tree=eK_h
because the outer binary gate's paid-sector reference equals its actual law.
Consequently K_F-K_tree is the NONNEGATIVE refinement cost displayed in (1).
It also equals the signed reference conversion from the preceding stage,

K_F-eK_h=n_F-e n_h-e(1-e)L_1(g),                       (2)

where n_F=H_F ln(Z_h,F/H_F), n_h=M ln(Z_h/M), and
L_1=sum_single P ln(W/P). Formula(1) proves nonnegativity for THIS dyadic
activation specialization; arbitrary reference changes remain signed.
No old KL is subtracted twice. Full ordinary cross-entropies add the same
actual empty entropy and physical-bias correction to both corrected bills.

## 2. Monotone concave transport and a uniform error certificate

Introduce a scalar lambda>=0, and set m(lambda)=M+lambda A,
z(lambda)=Z_h+lambda Z_1. Define the exact transport function

G(lambda)=sum_high P ln(P/W)+lambda sum_single P ln(P/W)
                +m(lambda) ln[z(lambda)/m(lambda)].   (3)

At lambda=0, G=K_h. At lambda=1, G=K_all. Equation(1) is exactly
K_F/e=G(1-e). For positive A,M, set
r=A z(lambda)/[Z_1 m(lambda)]. Differentiation gives

G'(lambda)=K_1+A[ln r+1/r-1]>=K_1>=0,
G''(lambda)=-(A Z_h-M Z_1)^2/[m(lambda)z(lambda)^2]<=0. (4)

The sign uses ln r>=1-1/r. If A=0, G is constant K_h=K_all.
If M=0, G(lambda)=lambda K_1, and its endpoint values are continuous.
Therefore G is monotone and concave, including all zero-sector limits.
The chord from0 to1 and monotonicity prove the finite certificate

e(1-e)K_all+e^2 K_h <= K_F <= e K_all,                 (5)
0<=K_all-K_F/e <= e(K_all-K_h)<=e K_all.               (6)

Also (1) gives K_F>=eK_h. Thus a rare activation of the NEW paid-sector
reference reinstates the OLD all-nonempty-rounded seed KL, rather than just
the paid-sector seed KL:

K_F/e -> K_all, with error at most e(K_all-K_h).        (7)

This rate is UNIFORM over every finite Boolean seed, every arity and every
product law, including a seed that varies with e. Since P<=W<4P,
K_all<=V ln(Z/V)<=V ln4. Hence the fully explicit error is <=e V ln4,
or |K_F-eK_all|<=e^2 V ln4 before division by e.
The difference K_all-K_h is exactly K_1 plus the weighted seed
singleton/high Bernoulli divergence; it is not a new capacity source.

## 3. Scale, entropy and original-reference endpoint consistency

The exact physical activation identities from direct summation are

J_hi(F)=e J_hi(g)+e(1-e)J_1(g)
              +ln4[e^2 k M+e(1-e)V],
E_1(F)=4e(1-e)h(a)+e^2 E_1(g)+ln4 e^2 k A,
L_hi(F)=e L_hi(g)+e(1-e)L_1(g),
E_F=e E_g+e(1-e)V ln4+2e^2 V ln(1/e)+4e(1-e)h(a),
h(a)=a^2 ln(1/a^2), h(0)=0.

Consequently, for every FIXED seed as e tends to zero dyadically,

C_*,F^+/e -> C_all,g^+ + V ln4+4h(a),
E_F/e -> E_g+V ln4+4h(a),
K_F/e -> K_all,g.

Here C_all,g^+=J_1(g)+J_hi(g)+V ln(Z/V). The same complete seed KL
appears in BOTH leading complete-reference identities. The known reference
correction and singleton payment do not eliminate the arbitrary high-scale
charge. When the seed varies with e the exact finite formulas, not an
unquantified fixed-seed limit, must be used; (5)-(6) remain uniform.

## 4. Zero deficit, unit atoms and probability-one coordinates

If V=0, g is constant. g=1 makes F constant; g=-1 makes a signed literal,
with no high labels and all KL and corrected costs zero. A physical literal
seed has M=0, its unique normalized coefficient magnitude one, and K_1=0;
then the activated high conditional law is a unit atom and K_F=K_all=K_h=0.
If A=0, (1) reduces exactly to K_F=eK_h=eK_all.
At e=0 contract the selector and use the actual constant law, rather than
normalizing a zero mass. Reflecting X preserves squared Fourier masses
and carries the same theorem to activation on X=0 with Pr(X=1)=1-e,
covering selected probabilities tending to one. No assertion replaces a
zero-variance coordinate by an artificial positive-variance law.

## 5. Universal bridge and honest unsupported line

The complete reference supplier at a rare endpoint still inherits the
ALL-rounded seed bill to first order, even after final singleton masses are
frozen. Equations(1),(5)-(7) close that exact history-transfer interface and
give its uniform error; they do not prove FEI. The first unsupported line
remains an arity-independent bound on the arbitrary seed/prime J_hi from
genuinely unused ORIGINAL capacity after existing singleton/import/carry
debits, with the same full references and ordinary KL. The sharper joint
singleton source reviewed separately does not supply this universal term.
