# B16 / A078 run report — occupation-time second moment

- Run ID: `20261020T014205Z-fleet01-B16-A078-occupation-second-moment-v1`
- Primary owned packet: A078 (B16); stable gap `G-A078-BOOLEAN-CODING-PADDING`.
- Candidate: the genuine triangular-permutation bent family `F_n(x,y)=(-1)^(phi_n^{-1}(x) dot y)` on `2n` physical bits. It is not the prior linear parity-code padding lift; the independent-padding energy barrier remains intact, and every physical coordinate is charged in `I=n`.
- Target: universal `G <= a I + b U` with one absolute `a>=0`, `0<=b<1`.
- Prior strongest bound: corrected endpoint-crossing proof, `G_y >= n+n^2/34,406,400` for `n>=131072`; prior one-sided-band gap repaired in the two-sided version.
- New result: occupation-time second-moment mechanism gives `P(B)>=1/196` and `P(A cap B)>1/204`, hence `G_y >= n+n^2/1,142,400` for `n>=131072`.
- Exact normalization: `H=2n`, `I=U=n`; `G=Theta(n^2)` conditionally, so `G/I -> infinity`, `U/I=1`, `H/I=2`.
- Frozen pair `(a,b)=(4,3/4)`: `N=7,711,201`, physical dimension `15,422,402`, normalized residual `>3+1/1,142,400`.
- GU-to-FEI implication was checked against the actual `NOTES.md` theorem and `REFEREE.md` induction; it is one-way and is not used to prove the GU obstruction.
- Status: `CONDITIONAL` analytic candidate; finite verifier `PASS`; independent end-to-end reviews pending; full FEI remains OPEN.
- Source pins: recorded in `SOURCE_PINS.json` with repository refs and blob SHAs.
- Local persistence: verifier PASS; manifest/hash readback complete and PASS. The required current source files were successfully fetched using branch refs separately from repository paths. The latest prior-run report and mirror paths returned exact `404 NOT_FOUND`, confirming those specific files are absent there. Remote writes for this run were not performed: the available GitHub connector exposes inline text-file writes but no bulk directory/archive upload, and I did not reconstruct or partially publish a non-identical subset while claiming a complete mirror.
- Next action: A092 independently reconstructs the derivative-support/upper-extension chain; A088 independently reconstructs restriction normalization and the occupation-time bound; A080 checks GU-vs-FEI scope. B20 alone reconciles shared indices after actual review evidence.