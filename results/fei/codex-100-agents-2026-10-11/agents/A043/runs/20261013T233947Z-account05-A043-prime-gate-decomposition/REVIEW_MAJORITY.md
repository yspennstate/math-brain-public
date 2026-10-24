# Independent scoped review of A042 majority-three

Source: A042 runs/20261013T221414Z-account05-A042-bias-endpoint-certificates, A042-SHARP-MAJORITY3-BIASED-ENDPOINT@1, statement hash 396cfaaabff2fa337f7a038ca4380cbede25d84a6ccd96032829a36dbecad11e.

Use signs Xi=2Yi-1 and mi=E Xi. Direct evaluation of the eight Boolean assignments gives f=(X1+X2+X3-X1X2X3)/2. Centering this sign polynomial yields c_i=(1-mjmk)/2, c_ij=-mk/2, c_123=-1/2. This independently produces the author's spectrum and a positive triple T=v1v2v3/4.

The signed-reserve proof in CORE_PROOF.md gives E_single<=4delta-2T without assuming monotonicity. Each pair has entropy ln4*P(ij)+(vi vj/4)(-mk^2 ln mk^2), and -z ln z<=1-z gives a rebate bound of exactly T. Thus E_ge2<=ln4*delta+(3-ln4)T. Their sum is E<=(4+ln4)delta-(ln4-1)T, as stated by A042. The coefficient is favorable because ln4>1, and T>0 on the interior. The source path (1-q^3,q,q) has the independently checked leading terms from A043 stage 2 and reaches the bound asymptotically.

Verdict: HOLDS as an independent reconstruction of the all-interior-bias core upper bound and input/output symmetry orbit. Sharpness is also reconstructed, but A043's earlier mixed-rate lower path was an input to A042's work; therefore this record does not count A043 as an independent acceptor of that lower-bound portion. A043 did not contribute a repair to the upper bound. The refinement in CORE_PROOF.md is a separate general singleton argument, not a necessary repair of the monotone proof.

Excluded from acceptance: the explicit 400 delta ln(1/delta) corner-error constant, all fixed-interior edge remainder formulas, and the author's 7,783-case output, which have not been independently reconstructed in full. This is a partial review of the bundled source claim. No acceptance of universal FEI or higher primes is implied.
