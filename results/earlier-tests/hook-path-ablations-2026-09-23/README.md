# Two changes to the math hook, measured on the hook's own path, 23 September 2026

The math hook decides on every prompt whether to serve store cards and which ones. Two changes to its selection were
measured on 23 September before they were switched on, each with the same bank, the same store and the same code, the
change off in one run and on in the other. The bank is the fresh probe of 3 September: 89 results, each asked in two
forms (`q_content` describes the result without naming it, `q_hinted` names it the way a reader would), and 40
results the store did not hold when the bank was written. The runs go through `framework/dreaming/eval_math_hookpath.py`,
the same entry point production uses. An answerable row counts when a served title is the asked result, and counts as
first when it heads the block. An unanswerable row is a false fire when anything is served; seven of those 40 targets
had entered the store by 23 September, and serving one of them is not wrong, so the strict count leaves them out.

The first change treats a named family as one family. When a prompt names a result ("prove the FEI conjecture") and
the store holds several cards about it, the selector had read the two best cards as rivals, judged the margin between
them too small, and stayed silent. Now a runner-up whose title carries a name from the prompt that the leading card
also carries counts as a sibling of the leader.

| named family | q_content: theorem / first / silent | q_hinted: theorem / first / silent | unanswerable: served / strict | median s |
|---|---|---|---|---|
| off | 72 / 57 / 9 | 83 / 80 / 4 | 28 / 21 of 33 | 1.12 |
| on | 73 / 57 / 8 | 86 / 83 / 1 | 28 / 21 of 33 | 1.13 |

Four items moved, each from silence to the right theorem (the zero-one law of Kolmogorov, the log-Sobolev inequality,
the Nullstellensatz and the KKL theorem), and none moved the other way. Four discordant pairs cannot reach
significance (exact McNemar p = 0.25 on the named form); the change went on because it lost nothing.

The second change expands seven acronyms the store uses for its own results (FEI, KKL, LTF, MMPP, FPP, SAW, LYM) in
both directions, on the retrieval query only. Every count on the bank was the same with it off and on, and the median time was 1.07 s off and 1.05 s on. It was switched on for the prompts the bank does not
cover: asked for the best known lower bound on the Fourier entropy-influence constant, the hook had led with a
percolation card, and with the expansion it leads with the card on that bound.

The false-fire count did not move in either run. Twenty-one of the 33 strict unanswerable prompts still get a card,
usually a neighbouring result.

## Files

`rows.json` holds one row per prompt: an opaque item number (the two forms of one result share it), the kind, the area,
the form, and for each of the four runs whether anything was served, whether the asked result was served and whether it
came first (for an unanswerable prompt, whether the served card was the target the store had gained since). The bank's
own keys name the results, so they and the prompts are not included. `python recompute.py` derives every count above
and lists the items that moved.
