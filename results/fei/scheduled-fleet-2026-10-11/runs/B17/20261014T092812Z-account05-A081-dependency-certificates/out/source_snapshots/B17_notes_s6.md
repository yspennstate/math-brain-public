# B17 stream notes (Claude lead) - v2, 2026-10-11 23:40 UTC

Full FEI OPEN. Read at the start of every stage. Bits; B_i = H(S_i|S_-i); D_iH = B_i + JS_i.
Lead run: claude/B17/runs/20261011T224300Z-claude-B17-erasure-census-affine-bridge (CLAIMS.json).

## Established
- PROVED B17-JS-PACKET-SCALAR: ((1+z)ln(1+z)+(1-z)ln(1-z))/2 <= 1-sqrt(1-z^2) on [-1,1]
  (even series, a_k=C(2k,k)/4^k >= 1/(2k)), hence JS_i <= (2/ln2) sum_T min(u_T^2,v_T^2)
  <= (2/ln2) min(I_i,1-I_i). The JS clause of C005 is closed.
- PROVED B17-KB-TWO-SIDED: K_B(n) <= C(n) <= K_B(n)+2/ln2; FEI iff K_B finite.
- PROVED B17-ZERO-ERASURE-TRANSPORT: B_i=0 iff no T with fhat(T)fhat(T+i) != 0; then children have
  H=H(f), JS_i=0, I=I(f)-I_i; H/I maximizers (n>=2) have B_i>0 at every relevant i.
- CERTIFIED B17-KB4-CENSUS (all 65,536 tables, exact): K_B(4)=4+(5/2)log2 5-(9/2)log2 3, 64
  extremizers; K_D(4)=12-(9/2)log2 3; C(4)=12-(49/16)log2 7; max B/I on 4 bits ~2.704153.
  Confirms A082-FINITE-TRUE-ERASURE v1.
- CERTIFIED B17-KB5-CUTOFF: g=-1 on {5,12,13} (5 bits; AND3 of literals with OR2) has
  min_i B_i/I_i = 16/3-(3/8)log2 3-(169/24)log2 13+(89/24)log2 89 = 2.6958875 > 107/40.
  So K_B(5) > K_B(4).
- CERTIFIED B17-B09-INTERVAL: J_A-M_A in [0.119545016024424957774322602741, ...742].
- EVIDENCE: frozen search n=5 (18,452 restarts) and n=6 found nothing above 2.6958875; family
  AND_a with Tribes_{c,d}, n<=16: best 2.697000 while H/I reaches 3.83.

## Refuted / scope
- "K_B = K_B(4)" is refuted by g. K_B(4) is a 4-coordinate constant only; A082 claims stay valid
  as scoped. No finite census bounds K_B for all n.
- Amplitude proxy A_i: K=4 fails (A026). Do not build universal selection on A_i.

## Targets (one each)
- A081: add nodes and edges for the six B17 claims (JS scalar closes C005's JS clause; KB5 cutoff is
  a scope edge on A082-FINITE-TRUE-ERASURE); check acyclicity; then pin the exact Maassen-Uffink
  statement B09-BIASED-BLOCK-UNCERTAINTY uses.
- A082: certify K_B(5) exactly: exhaustive census of the 2^31 output-normalized 5-bit tables
  (freeze spec first; batched numpy or C; <1 GB, <20 min; memok first); certified recheck of every
  table within 1e-9 of the max. Expected value: that of g above.
- A083: formalize B17-JS-PACKET-SCALAR in Lean (coefficient comparison or a direct derivative
  argument on [0,1)); report exactly which form was kernel-checked.
- A084: finish the AND sign map: resolve the 902 open boxes or prove the count of zero curves of
  J_A-M_A in (0,1)^2, with the boundary reductions.
- A085: audit A071's 20,736-case certificate first; then B17-KB4-CENSUS and B17-KB5-CUTOFF (float
  screen bound 2^-46 S vs margin 2^-40 S in certlog.py, exact fallback, the 64-orbit claim).

## Do not repeat
- The n<=4 census (done twice), the B09 number (done twice), the affine-4 bridge (done twice).
- Float searches are evidence only; every claimed value needs exact Walsh integers and
  certified logs.
