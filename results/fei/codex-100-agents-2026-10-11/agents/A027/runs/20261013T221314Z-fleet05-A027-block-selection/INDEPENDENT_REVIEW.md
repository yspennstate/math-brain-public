# Scoped independent reconstruction of A028 stage 2

Source: agents/A028/runs/20261012T011208Z-fleet05-A028-stopping-tree-payment/REPORT.md, sections 1, 2, and 6; claim A028-UNBALANCED-ACTIVATION-STOPPING-PAYMENT@2. Verdict: HOLDS for the arbitrary-controller exact spectrum, the C0 bias bound and terminal-inclusive control-first implication, and the stated FEI-equivalence in finiteness. This is a scoped review, not acceptance of every component of the bundled version-2 claim. The unchanged magnitude-KL component, separate stronger-conjunction composition, and literature examples are not reviewed here.

The controller and core have DISJOINT physical inputs. Independent Fourier reconstruction and a new checker using canonical prime-log coefficient vectors (rather than the author's checker) verify the exact identity H(F)=p H(u)+d Hplus(a)+R(p,d), as displayed in DERIVATION.md. Physical edge counting gives I(F)=pI(u)+dI(a); a determining controller-only tree has actual terminal entropy pH(u) and query budget dI(a). No variable occurrence in a formula is treated as an additional physical influence budget.

Reconstruct the scalar bound as follows. Put b=1/ln2 and phi(t)=E(1-2t). Direct differentiation gives phi''(t)=-16 log2|1-2t|-24b away from t=1/2. Its positive logarithmic singularity is locally integrable and phi' extends continuously. Thus phi(t)+12bt^2 is convex on [0,1]. Its chord from 0 to d yields phi(pd)-p phi(d)<=12bp(1-p)d^2=3bd^2 V. Also eta(p^2)<=bV/2. Substituting in R and dividing only when dV>0 gives

    R/(dV)<=2+2b+d[b-2+2log2(1/d)].

The last summand reaches b/sqrt(e), at d=1/(2sqrt(e)). Therefore R<=C0 dV, C0=2+2b+b/sqrt(e)<6. The endpoint dV=0 follows from R=0 directly. Using ln2>=56/81 and e>8/3>(8/5)^2 gives C0<2597/448<6. This reconstruction uses the exact negative terminal empty-sector subtraction throughout.

Consequently Pi_H<=d Hplus(a)+C0 dV. If Hplus(a)<=T[I(a)-V], then Pi_H<=max(T,C0)dI(a), because V<=I(a). An ordinary certificate H(a)<=K I(a) instead gives (K+C0)dI(a). Adding pH(u)<=pL I(u) uses a DISJOINT terminal account, giving the stated maximum constant against I(F). Taking u identically -1 gives F=a, Pi_H=H(a), and queried influence I(a); therefore the arbitrary-controller uniform-rate endpoint implies full FEI. Conversely full FEI plus the scalar bound supplies a finite controller-first rate. No conclusion about shared physical inputs follows.

Validation: 6,072 controller/core pairs including restricted terminals were checked with exact prime-log entropy vectors, independent physical edge counts, and Parseval, inside 23,232 declared proper core partitions. All 23,232 rational interval checks R<=6dV passed. The all-dimensional sharper C0 statement rests on the reconstructed analytic proof, not on this finite census. A027 supplies no substantive repair to the reviewed A028 assertions and is independent of their authorship. No external review message or registry adoption is claimed.
