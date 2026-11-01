# The zero-refund sector contains an arbitrary Boolean core

All entropy, CE and KL are in bits. References are complete normalized laws;
reference-only atoms and both full physical children are retained. This is
an exact obstruction to local conversion payment, NOT a disproof of FEI or
a claim that a product-reference conversion is universally necessary.

## 1. Exact Boolean characterization of a zero-phase physical query

Write a Boolean f=A+x_i B with A=(f_++f_-)/2 and B=(f_+-f_-)/2 on the
remaining physical cube. Pointwise AB=0 and A^2+B^2=1. Let a_T=Ahat(T),
b_T=Bhat(T). The children have coefficients a_T+/-b_T. The following are
equivalent:

1. The two child squared Fourier spectra are identical (JS=0).
2. a_T*b_T=0 at EVERY remaining frequency T.
3. The spectral erasure B_i(f)=H(S_i|S_without_i) is0.
4. On the occupied Fourier support, S_i is a deterministic function of
   S_without_i; no remaining-frequency fiber contains both parent labels.

For1<=>2 expand (a+b)^2-(a-b)^2=4ab. For2<=>3 each fiber's two masses
are a_T^2,b_T^2 and its conditional binary entropy vanishes exactly when
one is0. Statement4 restates that support condition. The exact physical
entropy identity then gives H(f)=H(f_+)=H(f_-). Neither this equality nor
the complete signed Booleanity hierarchy implies an arbitrary fresh
reference change is free. The actual child functions can differ by Fourier
signs at every frequency occupied in B.

## 2. An arbitrary core inside the exact local nullspace

Let g be ANY Boolean function on n independent bits, including a constant
or a function with dummy coordinates. Add THREE fresh physical bits and set

    h(x1,x2,x3,y)=x1*x2*x3*g(y).

Query x1. The two actual children are +/-x2*x3*g. They are NONCONSTANT even
if g is constant. Their spectra are identical and equal to p_g shifted by
the mandatory labels {x2,x3}. Every singleton coefficient of h is0; its
mean is0; all nonempty pair-products across the queried spectral fibers
are0. Thus the zero-singleton, isospectral phase-energy nullspace contains
an entirely arbitrary Boolean Fourier law, not just a parity point law.
It satisfies ALL signed Booleanity equations because it is pointwise Boolean.

For compatibility with the existing stream use the original fixed A079 row
a=[1,0,0,0,-1,1,1,1,1,0,0,0,1,-1,-1,-1], b=1-a^2, beta=3/8.
At BOTH actual signed children of the earlier tag use

    G_sigma(u,x,y)=a(u)+sigma*b(u)*h(x,y), sigma=+/-1.

Since h is balanced, its exact spectral law has controller-vacuum atoms
A_U^2 and nonempty atoms B_U^2 times the shifted p_g. Take the current
complete reference to be that exact law. The x1 query has B_x1=0, JS=0,
conditional occupancy KL=0, singleton ghost mass0, and coherent calibration
refund0, at EACH signed parent. Inf_x1(G_sigma)=beta, independent of g.
All four full physical terminal spectra and the original CE are retained.

## 3. Exact arbitrary-core conversion charge

Prescribe ANY normalized core-frequency law q with finite CE(p_g,q).
At BOTH physical children replace their tail by q, shifted by {x2,x3};
retain EVERY true controller-vacuum atom A_U^2 and factors B_U^2. Then

    B_x1(G_sigma)+mean CE(P_child,Q_q)-CE(P_parent,P_parent)
                       = beta*D(p_g||q).                 (1)

Proof: physical erasure is0, both unchanged child entropies equal the parent
entropy, and their full KL to the prescribed reference is beta*D(p_g||q).
No controller or source term is dropped. In particular every positive core
conversion cost embeds unchanged, up to beta, in a query where all the
listed phase/occupancy/ghost refunds are exactly0. The initial actual-spectrum
reference here is NOT asserted to have a universal influence price.

More generally inject a CURRENT singleton ghost of mass rho,0<=rho<1,
before the query: source reference (1-rho)*shift_{123}(p_g)+rho*delta_{x1}.
It remains normalized and finite on the actual spectrum. With the same
prescribed q target, the complete increment is exactly

    beta*[D(p_g||q)+log2(1-rho)].                         (2)

Hence the conversion is paid iff rho>=1-2^(-D(p_g||q)). Manufacturing that
ghost from the matched reference costs beta*log2(1/(1-rho)), so it must
prepay at least the entire core conversion bill. This reconstructs A079's
ghost-prepayment boundary with an arbitrary retained core, not a renewed bank.

## 4. Actual Boolean unbounded local bill for a specified product conversion

Let v on THREE bits be the one-point defect, negative only at the all-plus
input. Its exact spectral law has p_v(empty)=9/16 and each of seven other
atoms1/16. Every coordinate influence is1/4. Let q_v be the PRODUCT of its
actual frequency-coordinate marginals, each Bernoulli(1/4). It is positive.
Then

    H(p_v)=4-(9/8)log2(3),
    CE(p_v,q_v)=3*h2(1/4)=6-(9/4)log2(3),
    tau=D(p_v||q_v)=2-(9/8)log2(3),  1/8<tau<1/4.

The strict bounds follow respectively from3^3<2^5 and3^9>2^14. Take the
ACTUAL Boolean tensor g_r=product of r independent copies of v, r>=1.
Its full spectrum is p_v tensor r; the uniquely specified product-of-coordinate-
marginals reference is q_v tensor r. Entropy and CE add, so (1) is beta*r*tau,
while Inf_x1(G_sigma)=beta. Therefore

    conversion charge / queried physical influence = r*tau > r/8.

For EVERY finite C, a positive integer r>8C is an actual Boolean certificate
against a uniform LOCAL bound of this conversion charge by C*Inf_x1.
No floating search or merely normalized inverse vector is involved. It
survives point-defect and tensor guards by construction. Formula(2) sharpens
the prepayment requirement to rho>=1-2^(-r*tau), which tends to1. A fixed
ghost fraction therefore cannot pay these conversions for every r.

This does NOT refute an ancestor influence budget: the full physical energy
is I(G_sigma)=7/4+beta*(3+3r/4)=23/8+9r/32. The bill grows with that energy.
Nor is product conversion shown unavoidable: carrying the old marginalized
reference costs exactly0 and preserves every actual terminal. This precise
distinction prevents a false negative conclusion about FEI.

In fact this ENTIRE family satisfies FEI at the exact core rate
Cstar=16/3-(3/2)log2(3). Its full entropy is
H(G_sigma)=5-(9/16)log2(3)+beta*r*[4-(9/8)log2(3)], and hence

    Cstar*I(G_sigma)-H(G_sigma)=31/3-(15/4)log2(3)>49/12.

The strict guard again uses log2(3)<5/3. Thus the local obstruction occurs
inside a uniformly FEI-bounded actual Boolean family. A different ancestor
rate can pay the product conversion; no divergence of global H/I is asserted.

## 5. Allowing finitely many product components does not remove the obstruction

The product example is not presented as a new general Booleanity inequality;
the peer frontier already reports product-block obstructions. The following
bounded-M extension quantifies what an optimized mixture can save.

For ANY mixture q=sum_{z=1}^M w_z product_{j=1}^{3r} q_{z,j} on the core
frequency cube, the actual Boolean tensor law P=p_v tensor r satisfies

    D(P||q) >= r*tau - 2*log2(M).                        (3)

If q vanishes on an occupied atom the left side is infinite. Otherwise use
the exact posterior Z|X under q to form a joint law P(X)q(Z|X), with X~P.
The mixture variational identity, obtained by expanding logarithms, gives

 D(P||q) = TC_P(X|Z) + D(P_Z||w)
             + sum_j E_Z D(P_{X_j|Z}||q_{Z,j})
          >= TC_P(X|Z).

Here TC(X|Z)=sum_j H(X_j|Z)-H(X|Z). The r three-coordinate blocks X_b
are independent under P. Hence

 sum_b I(X_b;Z) <= I(X;Z),
 sum_j I(X_j;Z) <= 3*sum_b I(X_b;Z) <= 3*I(X;Z).

The first inequality is conditional entropy subadditivity together with
the original block independence; the second uses data processing within
each block. Therefore

 TC(X|Z)=TC(X)-sum_j I(X_j;Z)+I(X;Z)
       >= r*tau-2*I(X;Z) >= r*tau-2*log2(M),

proving(3). This explicitly uses block independence; no per-coordinate
conditional estimates are multiplied. Combining(1) and(3) proves that
EVERY coherent target whose retained core reference is a mixture of at
most M products has full conversion charge at least
beta*[r*tau-2log2(M)], with both children retained. For fixed finite M
there is no universal bound by C times the queried influence beta. If a
scheme REQUIRES entering this bounded-mixture reference class at the
query, the conversion is necessary WITHIN THAT SPECIFIED CLASS and the
displayed liability cannot be avoided by choosing its best member. This
does not establish that full FEI requires using that class.

There is also an EXACT exponential representation certificate: the minimum
number of product probability components representing p_v tensor r is2^r.
Indeed p_v=(1/2)delta_empty+(1/2)Uniform({0,1}^3), so2^r suffice. Flatten
the3r coordinates with one coordinate of each block as row bits, and the
other two as column bits. Select per block the column labels00 and01.
The resulting2^r-by-2^r minor is K tensor r, where

    K=(1/16)*[[9,1],[1,1]], det K=1/32.

Its determinant is (1/32)^(r*2^(r-1))>0 by the Kronecker determinant
formula (or induction). Thus the flattening has rank at least2^r. Every
product component contributes a rank-one matrix, so M>=2^r. This is an
exact rational rank impossibility certificate for representations, on an
actual Boolean spectral law; it is not a sign-impossibility certificate
for that law, which has the displayed actual Boolean truth table.

The arbitrary-core ghost threshold(2) remains exact. For the optimized
M-mixture class, a necessary prepaid credit is at least
beta*max(0,r*tau-2log2(M)); adding free ghosts cannot bypass this bound.
If log2(M)=o(r), the post-conversion complete CE divided by the TOTAL
physical influence has asymptotic lower bound8-3log2(3), rather than
Cstar. This is the finite overhead of the specified reference restriction,
not an obstruction to every finite global rate.
The all-r family and its signs are explicitly given by products of actual
one-point-defect truth tables, so no large unexecuted truth-table census
is used to support the universal claim.

## 6. What the reduction does and does not settle

The phase-refund nullspace is not a small exceptional class that can be
discarded by complete signed Booleanity or by requiring nonconstant children:
it encodes EVERY Boolean core spectrum, with exact inherited full CE. Any
scheme that requires the displayed product conversion must pay its full
core total correlation from an ACTUAL unused ancestor account; the queried
coordinate's local influence and all listed zero-refund currencies cannot
provide a universal bound. An admissible scheme allowed to retain the old
reference avoids this particular conversion entirely. Thus the missing
universal line is a concrete restriction on the admissible reference family
that makes a conversion necessary AND pays it from the original account,
or an initially influence-priced source valid for arbitrary cores. This
stage proves neither line. Full FEI, C018/C019/C020/C024 remain OPEN.

The all-dimensional embedding and unbounded local-bill theorem are the
displayed algebra. Exact finite certificates separately validate all physical
queries through3 bits, all small core embeddings, and fixed tensor fixtures;
they are not extrapolated into the universal proof. External review of the
new reduction is pending. No Lean or formal entropy certificate is claimed.
