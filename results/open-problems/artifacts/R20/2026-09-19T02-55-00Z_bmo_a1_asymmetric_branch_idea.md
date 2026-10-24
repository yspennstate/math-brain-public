Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

# R20 idea before code — one adjacent degree-three edge

Current exclusive target: Bensmail–Marcille–Orenga Conjecture 2.6. Frozen fleet metric entering this run: `n_all=9`. This note is deliberately written before any new validation code.

Methods for this run: **#5 ADD A PARAMETER**, **#20 FIND WHY THE ALGORITHM FAILS**, **#27 SWAP THE QUANTIFIERS**.

Let
\[
a(G)=|E(G[V_3])|.
\]
The preceding R20 theorem proves the nice subcubic case `a(G)=0`. The next candidate theorem is the complete `a(G)<=1` case.

The obstruction in the old construction is exact: if the unique adjacent degree-three pair `b,c` both receive push 3, then their direct-edge sums differ only through the sums of the two non-direct incident port pushes. In the symmetric double-triangle configuration those port sums are forced equal, so the direct branch edge can collide.

The new asymmetric route is to set

- `rho(b)=3`,
- `rho(c)=2`,
- `rho(v)=3` at every other degree-three core vertex.

Then on the unique direct branch edge,
\[
\sigma(b)=14+s_b,\qquad \sigma(c)=12+s_c,
\]
where `s_b,s_c` are the sums of the two non-direct endpoint-port pushes. If every chain endpoint push is chosen in `{1,2}`, then `s_b,s_c in {2,3,4}`. The only possible direct-edge equality is therefore the extreme pair `s_b=2, s_c=4`. The old all-3 collision has been reduced to one forbidden local port pattern rather than a global equality problem.

The chain problem should be solved once, uniformly: for every degree-two chain between branch pushes `alpha,beta in {2,3}`, choose endpoint ports in `{1,2}` and an interior word in `{0,1,2}` so that (i) consecutive chain sums differ, (ii) every chain sum stays below the branch-sum floor 14, and (iii) a finite local rule avoids the single bad direct-edge pattern above. The previous analysis already gives the endpoint relation for boundary 3/3: length 1 identifies the two endpoint ports, length 2 requires them unequal, and length >=3 has full positive-port freedom. This run will determine whether the same freedom survives boundary type 2/3 and 2/2.

The key quantifier swap is: do not choose a whole-graph witness first. Prove a finite **port rule** that works for every chain length and every boundary type in `{2,3}^2`; then glue those local choices at branch vertices. If the port rule exists, the `a(G)=1` theorem follows without a graph census.

No theorem is claimed in this note. No source closure is claimed. Any finite checker added later in the run will only validate a formula or finite port table derived after this idea.