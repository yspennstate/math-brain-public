# Proper partial-core activation transport

All spectra are normalized Boolean Fourier spectra on uniform cubes, and all entropies are in bits. Fresh point controls remain physically unqueried throughout this stopping partition. The result transports a specified actual core partition; it does not assert a universally cheap partition exists.

## Exact unbalanced activation correction

For any Boolean u on a core cube, let delta=Pr(u=-1), p=2^-r for r>=1 fresh controls, and F=1+A_r(u-1). Define

    E(a)=a^2 log2(1/a^2), E(0)=0,
    G_p(delta)=8rp delta(1-p delta)
               +p(1-p)E(2delta)+E(1-2p delta)-pE(1-2delta).

Then, with every empty coefficient retained,

    H(F)=p H(u)+G_p(delta).                                      (1)

Proof: nonempty core coefficients are p*uhat(T) for each of 2^r control sets; empty-core nonempty-control coefficients are -2p delta up to signs, and the full constant coefficient is 1-2p delta. Sum their exact entropy contributions. The nonempty-core contribution is p[H(u)-E(1-2delta)]+2rp*4delta(1-delta). The nonempty-control contribution is p(1-p)E(2delta)+8rp(1-p)delta^2. The constant contribution is E(1-2p delta). Combining gives (1). Neither delta nor the child biases are assumed near zero or 1/2.

## Dimension-free Lipschitz control of the shifted row

Let J_p(delta)=G_p(delta)-8rp delta. The removed term is affine and therefore cancels exactly on every actual stopping partition. On [0,1],

    J_p(delta)=-8rp^2 delta^2+p(1-p)E(2delta)
               +E(1-2p delta)-pE(1-2delta).

For a!=0, E'(a)=-2a(ln(a^2)+1)/ln2, continuously extended by E'(0)=0. On |a|<=1, |E'(a)|<=2/ln2: on a in (0,1) the only internal extremum of a(2ln a+1) occurs at exp(-3/2), where its absolute value is 2exp(-3/2)<1, and the boundary value at 1 is 1. On |a|<=2, |E'(a)|<=8+4/ln2, since the additional interval [1,2] is monotone in absolute derivative. Thus, using rp<=1/2,

    |J_p'(delta)| <= p(24+16/ln2)=2*kappa*p,
    kappa=12+8/ln2 <24.                                         (2)

The proof covers delta=0,1/2,1 by continuity. The exact lower bound ln2>=2(1/3+1/81)=56/81>2/3 proves kappa<24. No logarithmic bias singularity is discarded, and no derivative numerical search is used.

## Universal transfer for an actual partial-core leaf partition

Let T be any finite adaptive physical restriction tree querying only core coordinates. Branch assignments are fair conditional on their history, and no coordinate is queried twice on a path. Let w_l be its actual leaf probabilities, u_l the Boolean core restrictions, and

    Pi_H(u,T)=H(u)-sum_l w_l H(u_l),
    Pi_I(u,T)=sum_v w_v Inf_(i_v)(u_v).

For the core-first theorem, stop with at least one core coordinate unqueried on each path. The derivation itself also remains valid for other finite trees. Lift the same tree to F and call it T^A. Every leaf is F_l=1+A_r(u_l-1), and its physical probability is still w_l. The standard physical influence telescope gives

    Pi_I(F,T^A)=p Pi_I(u,T),
    expected leaf influence=p sum_l w_l I(u_l)+2rp delta.

The control reserve 2rp delta has not been consumed in the tree.

At a core node v, let delta_v=Pr(u_v=-1). It is the average of its two children. The disagreement d_v=Inf_(i_v)(u_v) satisfies |delta_(v,+)-delta_(v,-)|<=d_v, because differences of minority counts cannot exceed the physical disagreement. Coupling a uniform actual input to its own path gives

    sum_l w_l |delta_l-delta_root|
       <= sum_v w_v |delta_(v,+)-delta_(v,-)|/2
       <= Pi_I(u,T)/2.                                          (3)

This is a finite martingale variation estimate; no limiting terminal argument is used. It also applies to a fixed proper subset queried as one block, by ordering its coordinates. Only the physical leaf partition is used.

Subtracting the weighted leaf version of (1), using sum_l w_l delta_l=delta_root, and then (2)-(3), proves the exact correction and quantitative transport:

    Pi_H(F,T^A)=p Pi_H(u,T)+J_p(delta_root)-sum_l w_l J_p(delta_l),
    |Pi_H(F,T^A)-p Pi_H(u,T)|<=kappa Pi_I(F,T^A).                 (4)

Consequently, whenever the specified core partition has Pi_H(u,T)<=K Pi_I(u,T),

    Pi_H(F,T^A)<=(K+kappa) Pi_I(F,T^A).                          (5)

This statement controls the COMPLETE entropy decrement B+M, rather than merely its block erasure. For a fixed block W the recovered B_W/M_W identity remains exact; no conditional remaining-core spectrum is substituted by an erasure proxy. All remaining-core entropy is present in the actual F_l terms in (4).

## Terminal certificates and a growing low-density proper-subset rule

Point controls preserve C001 regularity. To see this, orient the negative indicator q=(1-g)/2 of a regular Boolean g to be monotone with a total desirability order. The negative event for 1+A_r(g-1) is A_r*q. Give all oriented controls the highest desirability ranks: switching a control from 0 to 1 while switching any data bit from 1 to 0 cannot reduce A_r*q compared with the opposite switch, since the latter has A_r=0. Data-to-data order is inherited from q, and control-to-control order is symmetric. Complement and orientation convert the sign function back to a regular Boolean sign. Thus the activated leaf is regular and satisfies H<=C_reg I with C_reg<8.937. Constant core leaves give constants or point defects; their elementary H<=4I bound is already independently accepted from stage 1.

If all u_l are regular, including constants, (5) and the unchanged physical influence telescope give

    H(F)<=max(K+kappa,C_reg) I(F).                              (6)

The core payment hypothesis K in this general statement is explicit and is not claimed universally.

A concrete proper-subset rule needs NO such unpaid hypothesis. Let t>=1, g be any C001-regular Boolean sign on s>=1 data coordinates, and

    u(z,y)=chi_[t](z)*g(y).

Query exactly the t character coordinates, leaving every g coordinate and every control unqueried. This is a proper subset of the core. Its leaves are +/-g, so all H(u_l)=H(g)=H(u): Pi_H(u,T)=0 and Pi_I(u,T)=t. Apply (4), or just its exact two-bias correction, to obtain

    Pi_H(F,T^A)<=kappa*p <=kappa*Pi_I(F,T^A),
    H(F)<=kappa I(F), since kappa>C_reg.                        (7)

The slightly stronger first inequality follows directly from (2) and |delta_l-1/2|=|Eg|/2<=1/2. The complete terminal influence is pI(g)+rp, and queried influence is pt; these budgets are disjoint.

For a genuinely low-density example choose g=D_s=1-2*1_(y=0), with s->infinity and t fixed. Then

    I(u)=t+2s*2^-s,  core dimension=t+s,
    I(u)/(t+s)->0,
    I(F)=p(t+2s*2^-s+r).

Rarity can independently make I(F)->0. A positive core-density hypothesis fails on this family, while the proper partial-core rule (7) remains paid. The +g terminal is the (r+s)-bit point defect. The -g terminal has negative event A_r*(1-A_s), is regular by the proved closure, and retains its full entropy and influence. This resolves a concrete low-density version of the lead's requested proper-subset partition, with no core dimension charge.

## Necessary activation surcharge on the same proper low-density rule

The additive surcharge in (4) cannot universally be zero, or even any fixed number below 4. For u=z*D_s, reveal only z and leave the s>=1 point-defect data coordinates and all controls unqueried. Then Pi_H(u)=0 and Pi_I(F)=p. With q=2^-s, the exact surcharge/p is

    [G_p(1/2)-(G_p(q)+G_p(1-q))/2]/p.                           (8)

For fixed delta, J_p(delta)/p converges as r->infinity to

    j(delta)=E(2delta)+4delta/ln2-E(1-2delta).

Indeed rp->0 and the first-order expansion of the C1 function E at 1 gives E(1-2p delta)/p->4delta/ln2. The removed affine terms cancel in (8). Next s->infinity, so q->0. Continuity gives j(1/2)=2/ln2, j(0)=0, j(1)=-8+4/ln2, and hence

    lim_(s->infinity) lim_(r->infinity) Pi_H(F)/Pi_I(F)=4.       (9)

Thus any uniform forward transfer Pi_H(F)<=p Pi_H(u)+c Pi_I(F) must have c>=4. All cores and leaves in this family are actual Boolean functions, the queried block is a genuine proper core subset, the density tends to zero, and the terminal entropy remains paid. This is a lower bound on the activation TRANSPORT surcharge, not an unbounded H/I family. The isolated exact witness s=32,r=16 is certified separately using compressed Fourier histograms rather than the G formula; no large cube is enumerated. Its outward rational enclosure is strictly ABOVE 4 (indeed above 8193/2048), so the stronger tempting choice c=4 itself is false. The iterated limit does not assert approach from below. The decimal value approximately 4.00049328 is only a display of the rational certificate.

## Honest universal boundary and next mechanism

The first unsupported universal line is selecting, for every Boolean core, a proper-core leaf partition with Pi_H(u,T)<=K Pi_I(u,T) and regular/point-defect terminals for one absolute K. Equation (4) TRANSFERS that payment; it does not supply it. Complete core trees recover FEI-strength after retaining all terminal cost. Therefore the new work eliminates rarity and child-bias instability from partial-core activation transport, not the universal core selection gap. The next test is a multilevel core decomposition where consecutive activations reuse a paid partition: can the exact J_p Jensen corrections be charged jointly, rather than spending +kappa at every level? That is a quantitative C019 question, not another dense-core class.
