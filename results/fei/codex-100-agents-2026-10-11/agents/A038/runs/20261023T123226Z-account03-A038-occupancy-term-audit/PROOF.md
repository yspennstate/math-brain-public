# Three full canonical reset bills, without reducing any old booking

Use exactly A038-BALANCED-CANONICAL-ADMISSION@4 hypotheses and definitions: independent uniform bits, entropy/KL in bits, rate4, d_m=1-2*1[y=0], h_m=chi_z d_m, m>=3, priority root chi_a on x0, h_m on x=b=1, +1 otherwise. Original completed occupancy reference M is fixed; A=KL(P_F||M)=(15/16)K_occ. Query b first, leave b0 and a untouched, and expose x on every b1 path before the first reset. Prefix booking L0 and ALL subsequent disjoint positive query-leg debits U_j remain their actual old values. Retain omega<=11/32 for ALL conservative excess beyond the named actual source/query/reset bills. No query is charged in overlapping groups without explicit additional liability. Keep all reference-only rows, current-reference normalizers, fair zero-source fallback, coherent common kernels and both physical terminals.

THEOREM. Allow at most THREE prescribed canonical reset frontiers, each after x exposure, interleaved with arbitrary finite fresh adaptive data queries. Let B0,B1,B2 denote their actual FULL new terminal KL bills, not numerical caps booked as independent liabilities. Preserve every old bill. Then

    L0+sum_j U_j <37/32,
    Bi<=5/32  (i=0,1,2),
    Sfinal-(L0+sum_j U_j+B0+B1+B2+omega)>1/32.

Every current-reference erasure/outcome/full-terminal KL decomposition remains owned once; it is not newly spendable credit. Any old conservative booking larger than its actual named bill is retained in omega. This is a stronger estimate on the SAME actual books, not a refund of an old cap. Earlier conclusions retain their original scopes.

## 1. Sharper cumulative source/query envelope

Version4 proves for EVERY stated finite adaptive history, regardless of reset positions,

    L0+sum U_j <= E_m=G_m-1-2(m-1)2^-m,
    G_m=2h2(1/4)+m h2(2^(-m-1)).

The exact Bellman identity Q_m=H(d_m)-8(m-1)2^-m is unchanged; no positive debit is replaced by a single net debit. Version3 proves h2(1/4)<13/16 (equivalent to 3^12>2^19), ln2>2/3, and

    m h2(2^(-m-1)) < e_m=m(m+5/2)/2^(m+1).

e_m decreases for m>=3: 2m(m+5/2)-(m+1)(m+7/2)=m^2+m/2-7/2>0. Hence E3<37/32 and E4<17/16 as before. At m5 retain the previously discarded subtraction: E5<155/128-1/4=123/128. For m>=6, drop only the nonnegative subtraction and use e_m<=e6=51/128, giving E_m<5/8+51/128=131/128. All four cases are strictly below37/32. This proves the sharper cumulative envelope for every m, not merely the checked finite domain.

## 2. Sharper actual reset price

A restricted character-point-defect core has actual canonical KL

    T_k=k h2(2^(1-k))-H(d_k),

with T0=T1=T2=0; a character-free point defect, constant or character has zero reset KL. Version3's exact entropy lower bound is H(d_k)>=8(k-1)epsilon, epsilon=2^-k. Since h2(t)<=t log2(1/t)+t/ln2 and 1/ln2<3/2, for k>=6,

    T_k < 2 epsilon [k^2-(7/2)k+4] = R_k.

R6=19/32. Moreover

    2[k^2-(7/2)k+4]-[(k+1)^2-(7/2)(k+1)+4]
      =k^2-(11/2)k+13/2>0 for k>=6.

Thus R_k decreases there and T_k<19/32<5/8. The remaining k3,k4,k5 inequalities T_k<5/8 are certified by the exact rational logarithm bounds in out/CHECK.json (also independently reconstructed with a different log series). These three explicit finite sign certificates, together with the displayed all-k argument, establish T_k<=5/8 for EVERY restricted core. No numerical extrapolation is involved.

The total rooted physical reach of core sectors is1/4. At every canonical reset frontier, including after any old data restrictions, the full new actual KL is therefore at most(1/4)*(5/8)=5/32. A reference-only row or outcome normalizer is not removed by this argument: it bounds the newly prescribed full reference, while each old full bill remains separately owned. Positive actual conversion is at most the charged full new KL; positivity of full new KL is not asserted to imply positive signed conversion.

## 3. Third reset and arbitrary later data histories

Every complete final restricted frontier has Sfinal=E(4I-H)>=2, from the untouched b0 and b1x0 sectors plus nonnegative restricted-core surplus. Keep L0, ALL old and new U_j, all three actual B_i and omega unchanged. Then

    Sfinal-(L0+sum U_j+B0+B1+B2+omega)
       > 2-37/32-3*(5/32)-11/32=1/32.

Queries after the third reset are included by the same version4 positive-variation theorem. This proves the stated theorem at all dimensions. The explicit m5 history b,x,reset,y0,reset,y1,reset,y2 has all three full reset bills positive (T5/4,T4/8,T3/16) and all three physical query debits positive. It retains every inactive/complementary terminal and transports the actual reference through each query.

## 4. Honest boundary and universal direction

Neither a fourth optional refresh nor exposing a is paid here. More importantly, repeatedly paying optional resets on this one family does not supply the universal FEI bridge. The first universal unsupported line is an all-Boolean analogue of the cumulative positive-variation/source bound, or a necessary compatible source conversion whose actual bill can be paid by the unchanged original owner. The next action is to confront that supplier directly, rather than iterate another optional reset. Author proof plus exact certificates is not independent external acceptance; FEI remains OPEN.

An explicit universal target is V4(f)=sup_T sum_h p_h[H(f_h)-E_s H(f_h|x_i=s)-4 Inf_i(f_h)]_+, the supremum over finite fresh-coordinate adaptive decision trees. For a complete tree with constant leaves, exact influence conservation I(f_h)-E_s I(child)=Inf_i(f_h) and entropy telescoping give sum_h p_h(signed deficit)=H(f)-4I(f). Therefore [H(f)-4I(f)]_+<=V4(f). A dimension-independent upper bound V4(f)<=K I(f) would prove full FEI with C=4+K. No such bound or converse is proved here. This gives an explicit universal debt for the NEXT audit; failure of this stronger positive-variation target would not by itself disprove FEI. The scoped point-defect theorem controls only its specified restricted histories, not the supremum over all trees for arbitrary f.
