# T255 routes tried

- , proved, not audited (agent Q): m=2 exact reduction: D=0 so w=tr(PV) is autonomous; scale density s'(y)=(2c+(g2^2/tau0^2)y^2)^(-1/(4 g2)); Feller test gives explosion with probability in (0,1) iff gamma^2<1/2, global (w->0) iff gamma^2>=1/2
- , proved, not audited (agent Q): all m: PD preserved up to explosion (tr(V^-1 b) has no inverse left; congruence noise)
- , open: control r^T W D when anti-aligned (agent Q): m>=3: W=PVP has autonomous noise; drift couples to r=PV1 only; r is pumped along +WD at rate g2 S/(2 m^2 tau0^2) (rdrift.py) so the r-term in d log trW tends to be positive; for gamma^2<1/2 the remaining terms give drift(log trW) >= eps|W|^2 - c
