# A prescribed reference through mixed histories, with one original source account

Entropy, cross-entropy and KL are in bits. All physical measures are uniform on the unqueried coordinates. This is a proper-class theorem with a supplied, explicit original source account; full FEI remains open.

## Statement

Let m>=4 be even, delta=2^-m, and b any Boolean bent sign on m bits. Let v!=w be two vertices, b_v,b_w their actual single-vertex flips, and z an independent sign. With independent fair point controls A,B set

    g0=zb, g1=zb_v, g2=zb_w,
    f=g0+A[g1+B(g2-g1)-g0], pi_root=(1/2,1/4,1/4).

At a physical history h, controls and any of the original m data coordinates may have been queried adaptively, but z is NEVER queried. Let d_h be the number of queried original data coordinates. The label probabilities pi_h are the actual conditional control-cell probabilities, not a new prior. Let b_h be the restriction of the ORIGINAL unedited seed to the data history. Define prescribed references

    q_h = (P_(b_h)+Uniform_{2^(m-d_h)})/2,
    nu_root = (1-3delta/2, delta/2, delta/2, delta/2),
    nu_h = the MARGINAL PROJECTION of nu_root onto unqueried control frequencies,
    Q_h = q_h times nu_h times the point mass on the z frequency.

The coordinate axes of nu are the two original control frequencies. Both physical children receive the same marginal projection when a control coordinate is erased. Its weights are never reset to the actual child marginal. The data reference changes at EVERY data query according to the displayed prescription, including already nonflat restrictions. Q_h is normalized and has positive mass on every actual Fourier atom.

Let C_h=CE(P_(f_h),Q_h), K_h=C_h-H(f_h), and let I_D(h) be the actual remaining influence of z and the unqueried original data coordinates, excluding both controls. Retain the physical boundary bank

    R_h=2 sum_{j<k} pi_h(j) pi_h(k) I(g_(j,h) g_(k,h)).

Fix an OLD debit 0<=U<=m/8, carried unchanged in expectation (not reissued). Put

    B_h=4 I_D(h)-C_h-U-R_h.

For EVERY finite adaptive mixed stopping tree with E_leaf d_h<=m/4,

    E_leaf B_h >= 1+m/32.

This is an EXPECTED frontier balance. Individual branches can have negative B_h and remain fully present. In particular every policy with at most floor(m/4) original data queries on each path is covered, with arbitrary interleaved control queries. Both controls may be fully resolved. No conversion is charged to a fresh source or fresh copy of R. The original control-influence account is separate and is not needed to prove this lower bound.

## 1. The original source is explicit

Bent flatness gives I(b)=m/2. A vertex edit changes each coordinate influence by at most 2delta. Hence the ORIGINAL data owner has

    I_D(root)=sum_j pi_root(j) I(g_j) >= 1+m/2-m delta,
    4 I_D(root) >= 2m+3,

because m delta<=1/4 for m>=4. The last elementary bound follows since m/2^m is decreasing for integers m>=1 and equals1/4 at m=4. The shared z contributes exactly1 to I_D and is not dropped.

The three nonempty-control Fourier sectors each have total mass delta/2. Indeed at each such control frequency the physical data amplitude is supported on the two distinct edited vertices, with magnitude1/2 at each. Parseval gives (1/4)(2delta)=delta/2. The empty sector has the remaining mass. This proves nu_root directly without a phase or independence approximation of the coherent Fourier law.

Write t=3delta/2<=3/32. Then H(nu_root)=h2(t)+t log2(3)<1. One exact certificate is h2(t)<=h2(1/8)<5/8 and t log2(3)<3/16. The first strict bound follows from 7^7>2^19, giving log2(7)>19/7 and h2(1/8)=3-(7/8)log2(7)<5/8. Monotonicity of h2 on[0,1/2] follows from its derivative log2((1-t)/t)>=0, with endpoint continuity. Thus no floating logarithm estimate is needed.

The original boundary bank is

    R_root=(3m/2-eta/2)delta <=3m/32,

where eta=1 for adjacent v,w. Each single-point product has influence2m delta; the two-point product has influence4m delta-4delta eta. This is the corrected adjacency factor, retained from the preceding stage and independently rechecked below.

These source quantities are not inferred from a universal FEI theorem or from nonnegative child deficits. They are computed at the ORIGINAL root.

## 2. The prescribed controller reference is a conserved code

Let Z_h be the actual controller-frequency marginal. Its cross-entropy against nu_h is C_Y(h). At a DATA query, squared-amplitude Parseval gives the average child controller law equal to the parent law. The controller reference is unchanged, so

    C_Y(parent)=average C_Y(children).

At a CONTROL query i, the average child controller law is the spectral projection deleting i. For each remaining frequency s and deleted bit a,

    nu_next(s)=nu_h(s,0)+nu_h(s,1)>=nu_h(s,a)>0.

Therefore

    C_Y(parent)-average C_Y(children)
      =sum_(s,a) Z_h(s,a) log2(nu_next(s)/nu_h(s,a)) >=0.

All sums are finite and all denominators are positive. This is a reference cross-entropy statement, not an entropy bound obtained by pretending the actual controller marginal is unchanged at a control query. Finite telescoping on ANY adaptive mixed tree proves

    E_leaf C_Y(h) <= C_Y(root)=H(nu_root)<1.

It covers every partial frontier and never reissues the root controller reference.

## 3. The data reference pays actual conversions

The smoothing prescription gives q_h(S)>=2^(-(m-d_h)-1). For the ACTUAL joint spectrum, including coherent control/data correlations,

    C_h <= (m-d_h)+1+C_Y(h).

No independence of the actual spectral marginals is asserted. A product reference permits this cross-entropy decomposition even when the actual spectral law is correlated. At a control query the seed b_h and hence q_h are unchanged. At a data query the prescribed q changes and its complete actual cross-entropy change is booked; its cost is not silently omitted or renewed.

Let N_D be the random number of original data queries along a leaf. The exact physical influence telescope for the DATA owner is

    E_leaf I_D(h)=I_D(root)-sum_DATA reach(h) Inf_i(f_h)
                 >=I_D(root)-E N_D.

At control queries the DATA-owner influence averages exactly, so no control pivot is paid from this owner. Each actual data pivot is at most1; this is the only relaxation in the last inequality.

## 4. The SAME physical boundary reserve survives

For a remaining data edge let r_j be the pivotal indicator of source j and q=sum pi_j r_j. Direct Boolean edge counting gives

    R_h=2 sum_edges E q(1-q).

At a DATA query, the release is precisely

    R_h-average R_child =2sum_{j<k}pi_j pi_k Inf_i(g_jg_k)>=0.

At a CONTROL query pi=(pi^0+pi^1)/2, so its release is

    R_h-average R_child =(1/2)sum_edges E(q^0-q^1)^2>=0.

The z contribution to every pair product is zero. These are direct identities at actual conditional histories, including zero-probability labels and repeated restricted cores. Consequently E_leaf R_h<=R_root. Branch increases are allowed; no pointwise monotonicity is claimed. The original pi weights are preserved through physical reaches, not replaced by a uniform label law.

## 5. Complete frontier payment

Combining the preceding inequalities, with D=E N_D,

    E B_h >= 4 I_D(root)-4D-[m-D+1+H(nu_root)]-U-R_root
           >= m+1-3D-U-R_root
           >= 1+m/32,

since D<=m/4, U<=m/8, R_root<=3m/32. This uses only the SAME original DATA account. The full boundary reserve is still subtracted, and the old debit is still present. The complete controller cross-entropy is paid as part of C_h. Thus this is a real positive unused source for the specified reference conversions, not merely conservation of a JS component.

For clarity about earlier bookings, set c_v=C_v-average C_child, r_v=R_v-average R_child, and let a_v=Inf_i(f_v) on DATA queries, a_v=0 on CONTROL queries. Exactly

    B_v-average B_child =4a_v-c_v-r_v.

The signed charge on the right includes every prescribed data-reference change. CONTROL charges are nonpositive because q is unchanged, controller CE drops and r_v>=0. Every original debit and earned refund survives every later partial frontier. Positive-part clipping is not licensed.

For full physical influence put W_h=B_h+4I_controls(h). With KL K_h=C_h-H(f_h),

    E_leaf[W_h+K_h+R_h]+sum_queries reach*(4Inf_i-Delta_i H)
       = W_root+K_root+R_root.

This follows by adding the exact physical influence and entropy telescopes. Both actual terminal KLs, their signed reference changes, the remaining boundary bank, and all old debits remain. The formula is not an all-node Delta_i H<=4Inf_i theorem.

The source-sector equality H(f_h)=T_h+J_h+L_h from A029 is retained in full: C_h=T_h+J_h+L_h+K_h. T, J and L are not separate additional donors, and K is not discarded when a CE bank is negative on a rare branch. No component is counted twice.

## 6. Actual negative-branch guard

For every even m>=8 choose the canonical quadratic bent seed, v=0,w=e1, U=m/8. Query data coordinates in order, stopping at the first1, and stop after all m zeros if no1 appears. Leave both controls live. The expected data depth is 2(1-delta)<2<=m/4, so this tree satisfies the theorem even though one path has depth m.

At the all-zero leaf, f=z[1-2A(1-B)]. Its control spectrum is uniform on four sets, I_D=1, R_leaf=0, and the data reference has a single atom. Thus

    B_leaf=4-U-(1/4)log2(1/(1-3delta/2))-(3/4)(m+1)
           <13/4-7m/8<0.

This is an ACTUAL Boolean counterexample to promoting the expected frontier theorem to a nonnegative conditional bank. The complete KL is retained. The full frontier, including this negative branch with its physical probability delta, is still paid from the same root owner.

## Exact remaining universal line

The explicit large original source comes from bent flatness, a shared balancing sign, and only two edited vertices. General Boolean sources need not have this linear surplus. The shortest next step is to pay the next prescribed profile conversion after the original DATA capacity approaches the bound m+1-3E N_D-U-R_root, or derive a structural replacement for that source lower bound. Arbitrary-source admission, arbitrary reference prescriptions, and a nonnegative bank on every individual history remain unproved. Full FEI is OPEN.
