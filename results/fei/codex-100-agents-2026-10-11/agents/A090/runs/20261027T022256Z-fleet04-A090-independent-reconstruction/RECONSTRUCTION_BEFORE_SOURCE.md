# Statement-only reconstruction checkpoint

A004-EXACT-FLEXIBLE-FLOOR-SIGNED-PRICE@1, statement SHA256 8dbf5314c0ed6db86c7c7d1127848d867db0208d93172a00ed45cee6f9bee3ac.
Producer DERIVATION and checker have not been opened. Current target selected from A090 NEXT and current BOARD, superseding stale B18 N5 search directions already retired in prior stages.

Let l_j=cT_j and x_j=max(l_j,k pi_j), sum x=1. Existence: F(0)=c<1, F(k)>=k for k>=0, continuous; after F exceeds c its slope is a nonempty sum of positive pi_j, so the root is unique and k>0. In fact 1-c<=k<=1. If pi_j=0, x_j=l_j, including ghost targets. These atoms cannot receive extra mass at optimum.

For any feasible y, use ln(y_j/x_j)<=y_j/x_j-1 only for pi_j>0 (if y_j=0 with pi_j>0, CE is infinite). On free positive-pi atoms pi_j/x_j=1/k. On floor-active positive-pi atoms pi_j/x_j<=1/k and y_j-x_j>=0. Thus sum pi_j*(y_j-x_j)/x_j <= (1/k)sum_all(y_j-x_j)=0, because ghost atoms have x_j=l_j and y_j>=l_j. Hence sum pi ln(y/x)<=0, so CE(y)>=CE(x). Equality requires y=x on positive-pi atoms by strict log inequality, and normalization plus ghost lower bounds gives equality on ghosts also. This independently proves uniqueness, including zero target/zero true-mass labels and ties.

With fixed incoming complete mass s, tail w and vacuum, actual CE difference is a sum pi_j log2(M_j/x_j)=a[D(pi||x)-D(pi||M)]. No normalizer or vacuum terms survive, precisely because they are fixed. A finite reached frontier is linear in actual probabilities; full sibling costs and old U persist. Therefore supplied budget B pays iff sum reached signed differences<=B-U-C. No reference renewal is implicit.

AND2 witness direct Fourier: all four squared coefficients1/4. Incoming tail M=(1/4,5/8,1/8), pi=(1/3,1/3,1/3), c=1/2,T=(1,0,0). Solution x=(1/2,1/4,1/4), k=3/4. Product M_j/x_j=5/8, so full cost=(1/4)log2(5/8)<0. Fixed incoming ratio5:1 on complement instead gives x=(1/2,5/12,1/12), product9/8, cost=(1/4)log2(9/8)>0. Both preserve full incoming vacuum1/4 and tail3/4.

First unreconstructed universal implication: choose an actually required compatible floor policy for arbitrary Boolean cores AND pay original full source CE plus necessary reached projections and all old debits from one universal K I(f). No arbitrary-core source or required policy is supplied by this optimization theorem.

Status: independent handwritten proof reconstruction; exact finite validation and source comparison pending. No full FEI closure or formal certification claimed.
