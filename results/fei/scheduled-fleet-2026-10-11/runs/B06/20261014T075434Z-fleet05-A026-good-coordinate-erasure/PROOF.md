# Disagreement-information reserve and its terminal-capacity obstruction

Bits; all functions are actual Boolean signs on independent uniform physical cubes. Keep one fixed encoder/data partition. Write F(x,r)=A(r)+h(x)D(r), g+=A+D,g-=A-D, E(r)=1{g+!=g-}, delta=Pr(E=1), q=Pr(h=1), v=Var(h)=4q(1-q), and B=B_z(A+zD). All quantities at a history use the actual restrictions and their physical reaches.

## 1. A strictly smaller universal reserve

Define V=v H(E)=v h2(delta). The elementary concavity bound B<=h2(delta) and entropy tensorization H(E)<=I(g+g-) were proved in stage5 (the latter is also ordinary entropy tensorization). Hence

 0<=V<=W=v I(g+g-).

At an encoder query i, gamma=hat h({i}), the exact variance drop is gamma^2, while E is unchanged. Its V drop is gamma^2 H(E), paying shadow charge gamma^2 B and retaining nonnegative gap gamma^2[H(E)-B].

At a data query j, v is unchanged and E restricts to its two actual children. The V drop is

 v[H(E)-avg H(E_child)]=v I(E;r_j)>=0.

This is ordinary mutual information between the actual disagreement bit and the actual queried sign. It is not conditional pivotal information I_j(g+g-). Consequently for any finite adaptive stopping tree,

 Q + G_H + L_H + E V_leaf = V_root,                 (1)
 Q=sum_encoder w gamma^2 B,
 G_H=sum_encoder w gamma^2[H(E)-B]>=0,
 L_H=sum_data w v I(E;r_j)>=0.

This proves a sharper nonnegative interleaved shadow bank universally, without an FEI assumption. It is a coordinate-independent charge bound, not an existential coordinate-selection theorem.

There is an exact nested account. With W, G_I,L_I from stage5,

 (G_I-G_H)+(L_I-L_H)+E(W_leaf-V_leaf)=W_root-V_root. (2)

Each difference is nonnegative. For the data term, I(E;r_j)<=I(E;r_j|r_-j)=H(E|r_-j)=I_j(g+g-): add the independent other signs to the first mutual information, then use determinism of E. Thus no hidden negative release or root-bank renewal is used in passing from the boundary reserve to the information reserve.

## 2. Physical ownership, endpoints, and sharpness

Stage5's exclusive pivotal account X=q Aex+(1-q)Bex satisfies sum_data w e_j+E X_leaf=X_root and X<=I_data(F). Therefore

 V<=W<=4max(q,1-q) X<=4 I_data(F).                (3)

The coefficient 4max(q,1-q) is still sharp for each realizable interior bias: an oriented AND2 shadow has E a dictator, H(E)=I(product)=B=1, and its sole active branch occurs with probability min(q,1-q). A complete encoder tree has Q=v, so Q/X=4max(q,1-q). Balanced price2 and arbitrary-bias supremum4 are unchanged. Constant encoders have V=0; delta=0 or1 also gives V=0 and B=0. No division by a zero influence is needed.

## 3. The smaller reserve still cannot be subtracted from arbitrary price-four terminal slack

Use A003's actual point pair b_d=-1+2 1_0 on d bits, c_d=-1, delta=2^-d and any balanced encoder. Its true price-four branch surplus is

 S4=[4I(b_d)-H(b_d)]/2
   =4delta+4(d-1)delta^2-eta((1-2delta)^2)/2,

where eta(t)=-t log2(t). Both branches are price-four certified, as reconstructed by A003/A004. The full empty Fourier atom is retained. Since V=h2(delta)>=d delta and eta>=0,

 V-S4>=delta[d-4-4(d-1)2^-d]>=delta(d-5), d>=4.    (4)

The last inequality uses 4(d-1)2^-d<=1 for d>=4, first checked at4 and decreasing thereafter. Hence there is NO finite A such that V<=S4+A delta for every d. This refutes funding the whole new reserve from that terminal bank with a fixed unlocking/query allowance. It does not refute funding the actual Q: A003 proved Q+delta<=S4+(2/ln2-1)delta. The reserve is a sufficient envelope, not an unavoidable entropy bill.

This is not a constant-terminal artifact. Tensor both branches with a fresh point sign t on 2d bits. Both resulting branches b_d*t and -t are nonconstant. Their product and hence V are unchanged, while full terminal entropy and influence are additive. New surplus is S4'=S4+[4I(t)-H(t)] with the added term between0 and4I(t)=16d delta^2. For d>=8, 16d2^-d<=1/2, so

 V-S4'>=delta(d-11/2), d>=8.                       (5)

This supplies an actual Boolean family with both nonconstant terminals and the same failed fixed-allowance subtraction. It is a reserve-payment obstruction, not an unbounded H/I family. Original point cores satisfy H<=4I and their tensors do too. The exact first unsupported universal line is replacing the reserve envelope by actual retained Q plus inherited/data bills paid from unused certified child surplus, across all further physical histories.

For completeness the point certification needs no conjectural premise: I(b_d)=2d delta and H(b_d)=eta((1-2delta)^2)+8delta(1-delta)(d-1). For d>=2, -ln(1-2delta)<=2delta/(1-2delta) gives eta((1-2delta)^2)<=4log2(e)delta(1-2delta)<=8delta. Thus H(b_d)<=8d delta=4I(b_d). For d=1 it is a dictator with entropy0; the constant branch is immediate. Applying the same proof on2d bits certifies t, and exact tensor additivity certifies both nonconstant terminals.

## 4. A prescribed non-point data query with the original terminal owner

Consume A004 stage5's neutral six-bit pair: b=+1 exactly when its first3 bit labels are zero, independent of3 dummy bits; c flips its positive origin. I(b)=I(c)=3/4 and all spectra are unequal-amplitude. Set h=Maj3 and form actual F=A+hD on9 bits. At the root let T=avg H(g+),H(g-), S4=4I_data(F)-T, and Q=B_z(f). The inherited inner Maj3 erasure under complete encoder resolution is delta=1/64, as in the source baseline.

At one proper data query j define T'=average of the FOUR full branch-grandchild entropies, D_branch=T-T', D_F=H(F)-avg H(F_j), Q'=avg B_z(f_j). The original retained bill Q+delta becomes D_F+Q'+delta. Full new terminal entropy changes the same original bank by D_branch. Thus its exact remaining margin is

 M_j=S4+D_branch-D_F-Q'-delta
    =(S4-Q-delta)-[D_F+Q'-Q-D_branch].             (6)

This subtracts the booked root bill once and the signed incremental debit once. It never resets to a freshly admitted S4. D_F includes actual query erasure AND JS. All four terminal laws are kept, including destroyed pivotal edges. The extra exact future encoder decrement beyond Q'+delta is retained separately as Z_j=avg H(F_j)-T'-(Q'+delta). Hence the full margin M_j-Z_j=4I_data(F)-H(F) is constant across j; this last equality is the known entropy telescope, not a new FEI theorem. Exact finite certificates below test whether M_j and M_j-Z_j are nonnegative on this prescribed pair. A successful control grants no universal extension of (6).

Executed exact certificates show M_j>1/2 and M_j-Z_j>1/2 for every one of the6 alternative first queries. The signed incremental debit is between0 and10^-6 for each active coordinate, and between-2/1000 and0 for each dummy coordinate. In every case0<Z_j<51/1000, so the remaining actual encoder correction is not silently dropped. The bound is for the specified post-unlock pair/encoder node; a parity-partner query before this node retains its own physical JS allowance and is not retroactively funded here. The6 alternatives do not consume or add6 copies of the original bank.

## 5. Universal frontier

Equations(1)-(2) improve the universal isolated-bank capacity from boundary to disagreement information and keep every release nonnegative under arbitrary interleaving. Equations(4)-(5) show that even this reduced envelope cannot be presumed available inside a certified price-four child bank. The remaining mathematical target is a selected, signed bill below the envelope, with history and full terminal costs, funded once by actually unused child surplus. A further census or a weaker root H/I estimate would not supply that step.

## 6. A028 source alignment and limited independent review

A028-UNBALANCED-ACTIVATION-STOPPING-PAYMENT@5, statement hash66a08477db58867a640a8dc7202d62a73c1f8d766491eaf3a2cd26e896317b7d, already carries R=2p(1-p)I(GH) through arbitrary mixed queries. With h=1-2c, q=1-p and W=2R, so stage5's boundary conservation is a parallel reconstruction, not a new team mechanism. For a controller query p0-p1 has magnitude |hat h(i)|=|gamma|; halving stage5's exact drop gives release_R=gamma^2 I(GH)/2, exactly A028(7). Halving a data drop gives v I_j(GH)/2=2p(1-p)I_j(GH), exactly A028(9). With exclusive edge masses a_j,b_j, its ratio to actual data influence is at most2: 2q(1-q)(a_j+b_j)<=2[q a_j+(1-q)b_j]. Terminal restrictions and physical reaches agree, so finite telescoping reconstructs the complete stated reserve-conservation clause without repair. Verdict HOLDS at that clause only; no review of the entire control-entropy/reference theorem is claimed.

The tree checker uses A026's own integer Walsh/prime-log implementation and direct truth-table edge counts, independent of A028's checker, to verify the equivalent W accounts and the new nested information account on the frozen1208 roots. This review is not independent acceptance of A026's own stage5 claim. A028's R is smaller than W but pays a DIFFERENT full-block inequality with controller costs; V<=W does not assert V<=R, improve A028's full constant, or replace its signed local-data obligation.
