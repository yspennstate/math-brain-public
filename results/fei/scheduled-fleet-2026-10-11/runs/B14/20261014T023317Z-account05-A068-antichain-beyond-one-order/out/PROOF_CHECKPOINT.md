# Checkpoint: influence-safe parity stars

For a unate Boolean h, write P_ij=sum_{S containing i,j} hhat(S)^2. Its j-derivative has values a,b in {0,sigma_j} at the two i endpoints. Therefore

    Inf_j(h)-2P_ij = E_rest[a b] >= 0.

Partition any selection of coordinates into vertex-disjoint stars with centers j and leaves L_j. Set y_j=x_j product_{i in L_j} x_i and y_i=x_i otherwise. For every original spectral set S the physical data label T has T_j=S_j, T_i=S_i xor S_j for a leaf, and T_i=S_i elsewhere. This map is invertible. For arbitrary overlapping quadratic control phases a_i(z), define G(x,z)=h(y_i(x)a_i(z)). Its exact packets are hhat(S)^2 ahat_S(U)^2, now indexed by (T(S),U). Thus entropy and the accepted parent rank-reference cost are preserved, while

    I_x(G)=I(h)+sum_stars sum_leaves [Inf_j(h)-2P_ij] >= I(h),
    I_z(G)=sum_S hhat(S)^2 I(a_S).

For regular unate h the complete reference R(T(S),U)=w_|S| prod_{i in S}i^-2 / Z_|S| * 2^-rank(B_S) * 1_{U in L_S} is normalized and obeys Gamma_R(G)<=C_reg I(h)+2I_z(G)<=C_reg I_x(G)+2I_z(G). The rank-reference dependency is the accepted A068 v1 recovered-C001 source, not a new proof of it. This does not assert a refined min(influence,1-influence) inequality.

Example h=MAJ3 and y2=x1*x2: G=MAJ3(x1,x1*x2,x3) is nonunate in x2 (opposite derivative signs at (x1,x3)=(+,-),(-,+)). Globally oriented desirability-width bounds for unate functions do not apply to that example. Its entropy is 2 and influence is 3/2.

A one-leaf star can be read as identified votes x and x*v, with an independent physical tag v. The tag makes the spectral projection bijective and prevents the signed merger. Fixing/deleting v produces the genuine two-row collision from stage3; the present theorem does not refund that untagged collision. Multiple overlapping stars/iterated shears are also unsupported: the transformed core may be nonunate, so the pair inequality cannot be iterated for free.

This is a narrow rank-reference extension of the existing packet. Independently reconstruct A079's completed same-full-cube quadratic collision payment before proposing any broader unequal-support closure.

