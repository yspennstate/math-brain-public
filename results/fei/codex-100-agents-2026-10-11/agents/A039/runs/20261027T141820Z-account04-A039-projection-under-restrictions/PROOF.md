# Sparse transport under every physical query order

All functions are genuine Boolean functions on finite uniform cubes. All entropies and KL divergences are in bits. The proof pays normalized-reference transport from a SUPPLIED original core bank and an unused ORIGINAL guard allowance. It does not supply the core's initial cross-entropy or a universal terminal-entropy bound. Full FEI remains open.

## 1. Supplied core interface and the independent guard

At each core restriction h, let p_h be its actual squared spectrum, q_h a complete normalized reference covering its support, and K_h=D(p_h||q_h). Use the actual signed-amplitude coherent channel, erasing the queried spectral bit first and using fair fallback on source-zero rows. Each physical outcome has probability1/2. Keep the reference's OWN outcome r and inherited normalized laws. Assume the supplied nonnegative bank B_h pays its ACTUAL both-child reset cost:

    sigma_core <= B_h-mean_y B_hy.                     (1)

This is an explicit hypothesis, not a free initial supplier. A039 moving-anchor factors have B=ell(d-1)(1-p(J)) until projected anchor absorption, zero after. A048's product-bank extension has B equal to the sum of factor banks; its ghost correction is reconstructed below. Initial K and full entropy H remain separately owed. Finite dominance q_h>=c_h p_h with c_h>0 suffices for every denominator below; moving-anchor products have this property. Reference-only atoms are retained.

Let k>=0 independent controllers activate only when all are +1, rho=2^-k, and let x be an independent fair guard. Define

    F=1+AND_k*(x*g-1).

For each controller frequency R the guard-bearing data row S has squared mass rho^2 p_g(S). On selector-only rows the empty frequency has mass(1-rho)^2 and all other controller frequencies have mass rho^2. These sectors are disjoint because the guard is present in every data row, even at S=empty. Keep selector-only masses exactly and replace p_g by q_g on ALL guard-bearing rows. This defines a normalized complete Q_F, including ghosts. Direct separation gives

    K_F=rho*K_g,
    H(F)=H_quotient+rho*H(g),
    CE(P_F,Q_F)=H_quotient+rho*CE(p_g,q_g),
    I(F)=rho*(k+1+I(g)).                              (2)

The quotient is the full law with the stated selector/guard masses; its entropy is retained. Formula(2) is valid for biased g as well: the independent guard balances x*g. At k0, F=x*g and the formula is still valid with H_quotient=0.

## 2. Data queries may precede or alternate with controllers

Query a core coordinate while x is unqueried. The actual children retain the same sparse form with the restricted cores and the same rho. Reset both to the corresponding sparse lifts of q_child. The selector-only sector has a fair physical outcome channel and zero erasure release. In each guard-bearing source-positive row the physical kernel is the core's actual channel. In source-zero core rows both kernels use the SAME fair fallback. Therefore, writing r_g for the reference core outcome,

    r_F=(1-rho)*fair+rho*r_g,
    E_F=rho*E_g,
    K_F=rho*K_g, mean K_F,fresh=rho*mean K_g,fresh.

Subtract the two exact KL/reset chains, with erasure E and outcome O=D(fair||r):

    sigma_F=rho*sigma_g+O_F-rho*O_g <= rho*sigma_g.    (3)

The inequality is convexity of D(fair||r) in its second argument. Thus a data query is paid by rho times the ORIGINAL core bank decrease, regardless of how many controllers have already been queried. This is not an assertion that inherited conditional references factor: that assertion can fail on ghost rows.

For clarity, in a product core query of factor j, let z_other be reference mass on zero-source spectator rows. The reference outcome is(1-z_other)r_j+z_other*fair, the erasure is local, and sigma_product=sigma_j+O_product-O_j<=sigma_j. This independently reconstructs the product-bank scope of A048@1 using the same complete reference and fair fallback. It does not assume the core source's initial CE is influence-priced.

## 3. Controller cost and a bank independent of changing ghost mass

Let z_h=q_h({S:p_h(S)=0}), which may change after DATA resets. For a controller query at k>=1, the true passing outcome is fair. On supported data rows the channel selects pass deterministically; on ghosts it is fair. Hence

    r_pass=(1-rho*z_h)/2, r_fail=(1+rho*z_h)/2,
    E_controller=0,
    sigma_controller=O(rho*z_h),
    O(t)=-(1/2)log2(1-t^2).                           (4)

The mean fresh KL equals the old KL: passing reaches the canonical sparse lift at2rho, failing reaches the exact constant spectrum. Thus the inherited failure ghosts are actually removed at the stated signed reset cost, not discarded for free. Positivity follows from rho<=1/2 and 0<=z_h<1; even z_h=1 gives positive branch probabilities. Source domination ensures z_h<1 for supplied references.

A048's sharper fixed-z bank is not invariant under an arbitrary data reset, because z_h can increase. An actual3bit example is g=first-two-bit parity at third bit0 and first-bit character at third bit1, with anchor J={first bit}. Its parent anchor coefficient is1/2 and all reference-positive atoms are source-positive, hence z_root=0. Query the third bit: the parity child has a1/6 reference-only anchor and the character child has none, so mean child ghost mass is1/12>0. out/GHOST_INCREASE.json checks this exactly. The original controls-first theorem is unchanged. Instead define the finite ghost-independent controller potential

    W_0=0,
    W_k=sum_(j=1)^k 2^(j-k)*O(2^-j), k>=1.

It satisfies W_k-(1/2)W_(k-1)=O(rho). Since O is increasing on[0,1/2],(4) is at most this decrease for EVERY current z_h. A data query leaves k unchanged and hence leaves W_k unchanged. No expected ghost mass monotonicity is claimed or needed.

## 4. Querying the guard and the complete interleaved theorem

Before guard exposure use the state potential

    V_h=rho_h*B_core,h+W_(k_h).

For a data query,(1),(3) give sigma_F<=V_h-mean V_child. For a controller query, the passing child has rho'=2rho and core bank unchanged, with reach1/2; the failing child is constant with bank0. Consequently mean core potential remains rho*B, while W pays(4).

If the guard is queried at ANY time, reset BOTH full child references to their EXACT child spectra and set V=0 on both children and every descendant. Then sigma_guard=-mean K_inherited<=0; this is paid by nonnegative V_h. All subsequent exact spectra transport exactly and reset cost is zero. Their entropy is still the full actual child entropy. No new independent guard or source is introduced after absorption.

Thus for ANY finite adaptive order of data, controllers and guard, both outcomes, and arbitrary stopping,

    Sigma_total<=V_root-E V_terminal,
    K_F,root+Sigma_total
       <=rho*(K_core,root+B_core,root)+W_k-E V_terminal. (5)

The exact transaction identity also retains

    K_F,root+Sigma_total
       =sum reach*E +sum reach*O +E K_terminal.        (6)

All trees have finite physical depth; telescope at actual input reach probabilities, not reference outcomes. No independence between adaptive choices is used. Full terminal entropy, quotient entropy and every previous debit remain in the SAME original account. Equation(5) is a transport theorem, not an entropy conclusion. If a guard allowance is already spent it cannot be used again.

## 5. Sharp universal guard allowance

Since rho=2^-k,

    W_k/rho=sum_(j=1)^k 2^j O(2^-j)<gamma,
    gamma=(1/(2 ln2))*sum_(r=1)^infinity 1/[r(2^(2r-1)-1)]<4/5. (7)

For the equality of positive series, expand -ln(1-t^2)=sum_(r>=1)t^(2r)/r. Every term is nonnegative, so monotone convergence justifies interchanging the two sums. The inner geometric sum is sum_(j>=1)2^(-j(2r-1))=1/(2^(2r-1)-1). Convergence follows already from O(t)<=t^2 on[0,1/2], which gives sum2^j O(2^-j)<=sum2^-j=1. The strict<4/5 is independently rational-certified in out/GAMMA.json with a positive-series truncation, a proved geometric tail and a bounded atanh series for ln2.

An analytic coarse certificate is also available: retain r1 andr2, and bound all r>=3 by (32/93)*sum_(r>=3)2^(1-2r)=4/279. Therefore the series is at most1+1/14+4/279. The two positive atanh terms give ln2>56/81, and direct rational comparison shows(1+1/14+4/279)/(2*(56/81))<4/5. Thus a previously UNUSED ORIGINAL guard allowance(4/5)*rho suffices for every interleaving. The initial core term is unchanged and not supplied by this allowance.

The coefficient gamma is sharp for this canonical controller-reset protocol over supplied moving-product references. Use T independent two-bit parity factors f_j=x_j*y_j, anchor J_j={x_j}, alpha1/6. Each reference has ghost mass1/6 and each factor is essential. The product has z_T=1-(5/6)^T ->1. Add the independent guard and k controllers; every coordinate is essential. Query controllers first, retaining all failures, before querying any data or guard. The exact controller cost divided by ORIGINAL guard influence rho is

    C_(k,T)/rho=sum_(j=1)^k 2^j O(2^-j*z_T).

For fixed k it increases to the partial sum in(7) as T increases; those partial sums increase to gamma as k increases. Hence any smaller universal coefficient fails for some finite actual Boolean example with a supplied product reference. This is sharpness of an OPTIONAL normalized controller protocol, not an FEI lower bound, and it does not claim a supplied core source is O(I).

## 6. Scope, review and exact unpaid line

A048-GHOST-CORRECTED-MOVING-TENSOR-SPARSE-TRANSFER@1, hash5eff8b1ca154107f76752c29d531d851e172a1706fdbcd12ac5a83770e2e3923, is independently reconstructed at its product/controls-first normalized transport scope in sections1-3. New sections3-5 extend to arbitrary interleavings, permit guard absorption, and give the sharp universal controller coefficient. The first unsupported universal line is a useful arbitrary-core ORIGINAL complete source and required terminal-entropy descent paid by O(I) unused original capacity. This theorem transports a supplied core bank; it never pays its initial CE by naming it a bank. A039's prior majority obstruction still applies to the n*a upper envelope. Full FEI remains open; external review of this extension is pending.
