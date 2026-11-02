# Tests

Each test runs agents on a fixed set of questions with and without the brain and counts correct answers. P values come from exact paired tests on the items where the arms disagree. The questions, the answer keys and the per-question records are kept private, to avoid disclosing the test instruments. Public answer-bearing records can still contaminate later evaluations; repeated runs on exposed items are regression checks, not fresh holdouts. Anchors for some blinded experiments were committed in advance and are public: [brain-benefit-experiment-anchors](https://github.com/yspennstate/brain-benefit-experiment-anchors). The rows of earlier tests not described here are kept in [results/earlier-tests](results/earlier-tests/), each with its own README.

## The tests at a glance

| Test | Agents | Without the brain | With the brain | On the items where they differ |
|---|---|---|---|---|
| 2,000 questions about files in 113 git repositories, new questions (30 Oct 2026) | Codex | git and the files: 91.4% | consulting the brain once a question: 93.7% | 83 to 43, p = 4.6e-4, on the 1,726 both arms reached |
| the same design, an earlier bank, pairs run at a normal machine load (29 and 30 Oct 2026) | Codex | 86.1% | 90.5% | 78 to 36, p = 1.0e-4, n = 967 |
| 1,000 items whose answer must be recalled (13 Sep 2026) | | 538 | 1,000 | 462 to 0, p = 1.7e-139 |
| 988 items, 600 seconds each (23 and 24 Oct 2026) | Claude | model alone 18.9%; research repositories 82.0% | 95.4% | 146 to 13 against the repositories, p = 1.2e-29; 30.6 session-hours against 53.2; 0.074 dollars a right answer against 0.153; tied at 99.3 and 99.4 percent on the 806 items both finished in time |
| 394 of the same bank, 900 seconds each (23 to 28 Oct 2026) | Codex | model alone 21.6%; research repositories 97.0% | 94.7% | 10 to 19, p = 0.14 |
| 84 hard questions on the store, rerun (1 and 2 Nov 2026; stopped early when the quota ran out) | Codex | research repositories 82 of 84 | 83 of 84 | the same items in October scored 26 of 85 against 67 of 86; 56 of the repositories arm's right answers were computed from the files in Python, so this bank no longer separates the arms |
| 100 questions on results held in the store (11 Oct 2026) | Codex | no tools 0; text search 75 | recall tool 83; hook, recall and walk 82 | 10 to 3 against text search, p = 0.09 |
| 61 reasoning and audit items (5 and 6 Oct 2026) | Claude | tools only 41 | full package 52 | 15 to 4, p = 0.019 |
| 60 questions whose answer exists only in the store, no tools (5 Sep 2026) | Claude | none 0; a block served for another question 0 | 48 (20 before a retrieval fix) | 48 to 0, p < 0.0001; no wrong number copied in 240 verdicts |
| 160 proof audits with planted faults, right notes against scrambled notes (Aug 2026) | | scrambled 117 | right notes 128 | 18 to 7, p = 0.043, replicated on a second bank |
| 80 questions about files in GitHub repositories (12 Oct 2026) | Codex | git alone 68 | git and the brain 73 | 9 to 4, p = 0.27 |
| 20 recall items, one agent, without and then with (23 Oct 2026) | Claude | 9 | 19 | 10 to 0, p = 0.002 |
| 13 open problems, graded blind out of a possible 39 (11 Oct 2026) | Codex | 26 | 24 | referee preferred the no-brain attempt 8 to 3, p = 0.23 |

Without agents: 584 held-out questions went from 298 to 317 answers in the first eight after one day's ranking changes, and six more sets from 891 to 1,018 of 1,070. Two wordings fused by rank found 112 of 120 against 96 for one query. A rule for silence on questions the store cannot answer has AUC 0.997 and 6.4 percent false silences on 2,000 answerable and 60 unanswerable questions. Details, and the things that did not help, are further down.

## Brain against git, 2,000 questions (29 and 30 October 2026)

This is the largest test so far and the hardest setting for a memory, because the questions come from git's own ground. Questions were drawn from random files of 113 git repositories, in 15 kinds: a value, the file that holds it, the date it was added, the value before a change, a commit date, a two-step lookup, an identifier, a count, something that is not there, which repository, long digit strings, a memory note, a math statement, which came first, and a deleted file. Keys came mechanically from the files and git history. Fifty pairs of Codex agents (gpt-6.1-sol, medium reasoning) each took 40 questions with a budget of 12 commands. One arm of each pair had the working brain's recall tool (the larger private brain, not the public snapshot) as well as the files, and the other had git and the files only. The repositories include the brain's own, so both arms could read those. A missing answer is left out, never counted wrong.

| Round | Questions graded | Git | Brain | Differ | p | Recalls a question | Median seconds a question, brain and git |
|---|---|---|---|---|---|---|---|
| 2, told to consult once a question, load 30 to 75 | 967 | 86.1% | 90.5% | 78 to 36 | 1.0e-4 | 1.02 | 46 and 12 |
| 3, 2,000 new questions, load 30 to 75 | 1,726 | 91.4% | 93.7% | 83 to 43 | 4.6e-4 | 1.02 | 67 and 13 |

Runs where the machine was over capacity and agents could not finish are left out, whichever way they went. At a load of 100 to 340 one recall took 700 to 2,300 seconds and twelve agents stalled. That removes the first round, which went to git, and two parts of round 2, which went to the brain: the 640 pairs before a crash, and 393 pairs on which the arms ran under different conditions. Round 2 asked the first round's questions again, so it is a second measurement and not a fresh bank.

The grades were revised on 1 November, after the answers were known, under three rules applied to both arms. Answers on a question's accept list now count for dates, paths and repository names as well as values and identifiers, which were all the grader had read the list for. A question built by moving a real fact to a repository that lacks it now accepts either NOT_FOUND or the fact's true value. A which-repository answer counts if the file it names holds the fact, because the keys had checked that only against one other file: a read of the files found the fact in 119 of 143 wrong answers over both rounds, in none of 49 locate-file answers given the same check, and on none of 357 control lines. Answers that were close but rounded stay wrong. Before these rules round 3 read 88.6 and 90.2 (97 to 70, p = 0.044) and the 967 pairs 84.2 and 87.8 (83 to 48, p = 0.0028).

Where both arms committed to an answer they were right about equally often: 93.8 and 94.1 percent on 808 items in round 2, 95.5 and 94.9 on 1,517 in round 3. The lead comes from the git arm giving up, answering NOT_FOUND on 15.1 percent of round 2's items against 9.2 for the brain, and 11.0 against 8.2 in round 3. The brain arm was also slower, by about the cost of its one recall call on a busy machine (round 3 means: 154 seconds a question against 25). So this test does not repeat the time saving of the 988-item test. It says that a recall, once called, keeps an agent going on questions it would otherwise drop, and that the agent pays for it in time.

Round 3 was stopped early when the agents' quota was needed elsewhere. By then the brain arm had answered 1,726 questions and the git arm all 2,000. The git arm's other 274 answers are graded too, 239 right (87.2 percent, under the first grading), and stay out of the paired figures, since the brain arm has no answers to set beside them.

| Kind of question | Round 2 n | Brain % | Git % | Differ | Round 3 n | Brain % | Git % | Differ |
|---|---|---|---|---|---|---|---|---|
| value | 64 | 87.5 | 87.5 | 2 to 2 | 118 | 94.9 | 94.9 | 3 to 3 |
| locate file | 60 | 85.0 | 86.7 | 3 to 4 | 143 | 87.4 | 87.4 | 4 to 4 |
| date added | 72 | 87.5 | 80.6 | 8 to 3 | 146 | 92.5 | 87.7 | 11 to 4 |
| value before change | 28 | 85.7 | 82.1 | 2 to 1 | 76 | 86.8 | 84.2 | 4 to 2 |
| commit date | 73 | 94.5 | 90.4 | 6 to 3 | 46 | 97.8 | 95.7 | 1 to 0 |
| two-hop | 69 | 92.8 | 91.3 | 5 to 4 | 85 | 96.5 | 95.3 | 3 to 2 |
| identifier | 68 | 91.2 | 89.7 | 5 to 4 | 139 | 93.5 | 94.2 | 6 to 7 |
| count | 72 | 90.3 | 87.5 | 5 to 3 | 132 | 87.1 | 85.6 | 12 to 10 |
| absent (NOT_FOUND) | 69 | 100.0 | 98.6 | 1 to 0 | 133 | 98.5 | 99.2 | 1 to 2 |
| which repo | 73 | 97.3 | 87.7 | 8 to 1 | 135 | 96.3 | 94.8 | 3 to 1 |
| long digits | 77 | 85.7 | 83.1 | 3 to 1 | 133 | 93.2 | 91.7 | 6 to 4 |
| memory note | 42 | 81.0 | 61.9 | 10 to 2 | 95 | 92.6 | 93.7 | 2 to 3 |
| math statement | 51 | 94.1 | 94.1 | 1 to 1 | 74 | 94.6 | 91.9 | 2 to 0 |
| which first | 93 | 86.0 | 78.5 | 13 to 6 | 132 | 97.7 | 84.8 | 18 to 1 |
| deleted file | 56 | 94.6 | 85.7 | 6 to 1 | 139 | 97.1 | 92.1 | 7 to 0 |

The clearest wins in round 3 are which came first (18 to 1, p = 7.6e-5) and the deleted file (7 to 0, p = 0.016), and in round 2 the memory note (10 to 2, p = 0.039) and which repository (8 to 1, p = 0.039). The question whose fact is missing from the place named now comes out level (1 to 2 in round 3). Under the old rule git led it 17 to 4, because the git arm said NOT_FOUND where the brain arm more often gave the true value from where it really sits, so this test cannot say whether an agent notices that a fact is missing from a named place. No memory about this test held an answer. The keys and per-item rows stay private, since a resumed run would use them.

## Sixty questions whose answer exists only in the store (5 September 2026)

Sixty questions asked for exact counts of constrained self-avoiding walks that agents had computed and that appear in no published table. Claude Opus 5 had every tool denied and was graded on the exact integer. With no notes it answered 0, and with a block served for a different question 0, copying no wrong number. With the block the retrieval served that day it answered 20; after a fix to one margin in the retrieval it answered 48 (48 to 0 against no notes, p < 0.0001). A second script re-derived all 240 verdicts with no disagreement. The questions are worded like the store and come from one family, so this says the path works, not how often it will in the wild.

## Right notes against scrambled notes (August 2026)

Proof audits with a planted fault, with served notes from the brain against notes matched in kind and size but scrambled: 128 against 117 of 160 (18 to 7, p = 0.043), replicated on a second bank, so what the notes say matters. Whether having served notes beats having none did not show in the same setting: 80.0 against 77.4 percent at 150 items (p = 0.50), and 301 against 299 of 358 in the powered run.

## Corrections, and a plan test (October and November 2026)

Of the 1,137 cards in the math store that supersede an earlier card, 139 correct what a card said for a stated reason. The rest are labels, formula repair, duplicates, re-harvests, re-reads of extracted text, retirements and plain revisions. In a sample of 30 of the 139, 19 plainly changed the meaning.

In a preregistered test with a blind judge, at eight cut-offs on two open problems, a plan written with a digest of what the store held on the problem was preferred 7 of 8 times, on target 10 against 6, with redundant or dead-end steps 8 against 17. It judged plans and not proofs.

## Silence, fusion and long records (October and November 2026)

- A rule for when to say nothing: on 2,000 questions the store can answer and 60 it cannot, a simple word-score threshold has AUC 0.997 and 6.4 percent false silences. Prototype rules built on the meaning channel did worse, with 27 to 37 percent.
- Two wordings fused by rank found 112 of 120 against 96 for one query. Passing several wordings on hard rows moved the first five from 45 to 56 of 60.
- Fusing the meaning channel with word search on 279 reworded questions over a general store of 28,112 notes found 81 against 67 in the first eight (26 to 12, p = 0.034). The meaning channel alone found 57.
- A line past the point where the word index stops reading a long record reached the top ten 23 times of 60. With a separate index for the tail it reached it 53 times, with no change on a 700-question bank or in latency.
- A spelling corrector on the query replaced a rare word, one seen in at most eight records, with a far commoner word one edit away and dropped the original, which lost records that quote a misspelling or use a rare real word or name. Scoring each changed word again beside its correction (2 November) lifted the first hit on 496 stored questions containing such a word from 280 to 411 and the first eight from 384 to 487, with nine answers slipping one or two places; on 32 quoted sentences the first eight went from 27 to 32. Queries the corrector leaves alone are unchanged. The stored questions use each record's own words, which favours this change.
- When a user's own sentence is quoted back, the compaction summaries that repeat it word for word can fill the first eight and push down the record that holds the order. Lowering every summary's score loses the summaries themselves (see What did not help). Moving one row instead, the best record that is not a summary, up to eighth place when it scores at least 0.7 of the top word score, raised the first eight on 187 quoted sentences from 168 to 170 and the first hit from 97 to 98 through the full recall path, with none worse. On word scores alone it left 1,000 questions about ordinary records unchanged and moved 2 of 1,976 questions about summaries out of the first eight. It has been on since 2 November.
- A query made only of an identifier, such as a dated task id, found nothing at all: the word filter that seeds the walk keeps words that start with a letter and have three or more characters, so the id gave it no words and recall stopped before the word index, which does keep the id, was asked. Seeding from the word index's top five on the raw query whenever it holds such an id (2 November) found the record named for the id in the first eight for 10 of 10 bare ids, against 2 of 10 before; questions with ordinary words around the id were already right, 10 of 10, and stayed so.
- The rerank that rewards records whose names cover the query's words counted a word as covered when its first five characters matched, and for a token that begins with five digits that matched every record whose name carries the same date. A task's own record, ranked first by word score on its id, was then shown last of 60, under 59 summaries from one session dated alike. Applying the prefix match only when the five characters are not all digits (2 November, one frozen word index, the rule the only difference) put the task's record at rank 1 for 8 of 8 ids, against 1 of 8 in the first eight before; six word queries came out the same.

## Speed (29 October to 2 November 2026)

The medians are from one machine and move with its load.

| Change | Before | After | Answers |
|---|---|---|---|
| Resident recall server, fixed copy | 26.8 s | 7.4 s | 20 of 20 identical |
| Reading attachments from a snapshot | 121 s, 36 timeouts | 28 s, 0 timeouts | |
| Two-wording recall | 295 to 411 s | 45 to 61 s | |
| Problem recall on a stale index | past 600 s | about 5 s | |
| Fast path repinned on a second machine | 8 s | about 2 s | 69 of 69 identical |
| Superseded check in recall | 3.86 s | 1.25 s | same answers |
| Math recall answered by the resident server (1 Nov, two one-a-minute samples) | 24 to 60 s | 2.2 s median, 4.3 s at the 90th percentile | 87 of 87 calls served |
| A new card becoming findable | the next full rebuild, 20 to 39 minutes | the first call after it is written | 7 of 7 new cards at rank 1; with 1,000 cards added, 40 of 40 searches identical to a full rebuild |
| A recall bank at depth 0, quiet machine, mixed with the fixes above | 28.2 s | 8.4 s | accuracy held |
| Memory recall with Windows power throttling turned off for the process (1 Nov, three calls each) | 17 to 19 s | 5.3 to 11.6 s on a quiet machine; 20 to 26 s with every core busy, where most of the call is waiting for a core | |
| Memory recall encoding the query on a thread instead of starting a helper process (2 Nov, nine alternating pairs) | 14.1 s inside recall, 18.0 s from the command line | 6.4 s and 13.5 s | same answers on all three questions |
| Loading the meaning vectors lazily, checking only the rows a lane uses (2 Nov, by profile; wall times on the busy machine swung too much to show it) | 1.04 s | 0.13 s | same first eight on 9 of 9 |
| Memory recall's link walk reading only the links it reaches, about 35,000 of 315,000 (2 Nov, one question a call, busy machine) | 1.4 to 2.8 s, median about 1.7 s | 0.45 to 1.2 s, median about 0.8 s | same lists on 9 of 9 fresh-process runs and 20 of 20 random seed sets |
| Memory recall's graph walk splitting its matrix product over four threads, each row still summed in its own order (2 Nov, 20 queries, busy machine) | 25.5 s | 15.3 s | identical rankings on 20 of 20; the walk is the same bit for bit |
| Memory recall's graph walk finding node names by binary search over a saved sorted order, instead of building a dictionary of 351,403 names in every process (2 Nov, five paired rounds, busy machine) | 1.25 s median load | 0.76 s | every name and 2,004 misses agree with the dictionary; identical rankings on 20 of 20 |

Where the time goes (30 and 31 October). One recall call spent 2.2 seconds starting Python and 4.4 seconds importing, then read and hashed the 182 MB vector file four times, 9.1 seconds in all; it now reads that file once a question. On a heavily loaded machine a resident server saved little (22.0 against 24.0 seconds median), because the time went to waiting for the processor, not to computing: on 31 October the same 30-item bank took a median of 549 seconds wall time a question at 6.2 seconds of processor time, and answered 10 of 30, against 11 on a quiet machine.

## The brain, the repositories, and the model alone, 1,000 items (23 and 24 October 2026)

Three arms, one item a session, the same instructions in each. With the brain, the agent has the recall tool and the prompt hooks and no file tools. With the repositories, it has no brain, no hooks and no recall tool, but it can read, list and search the research repositories, which include the exported store, the campaign records and the open-problem files; the brain's own folders, the keys and every test folder are closed to it. The model alone has no tools. Claude Sonnet agents (high reasoning) had 600 seconds an item and no shell in any arm. Codex agents (gpt-6.1-sol, high reasoning) had 900 seconds; their brain arm had the recall tool and no shell, their repository arm a read-only shell. A timeout counts as wrong. A session that never reached the model (a refused account or a session limit, seen as an empty event stream) was rerun, not graded.

The bank, built on 12 September, has 1,000 items. 923 are lookups over the store's records: page sums and differences, the latest-posed problem and the odd source out among problems on the open-problem ledger, and combinations of two to four self-avoiding-walk counts. Their keys were generated by script and derived twice from separate reads, with no disagreement. The other 77 are proof audits: decide whether a numbered proof is correct and, if not, name its first invalid step. Their answers are stored nowhere, so they are a control.

The figures cover the items run in all three arms by the morning of 28 October: 988 for Claude and 394 for Codex.

| | Brain | Repositories | Model alone |
|---|---|---|---|
| Claude, 988 items: correct | 95.4% | 82.0% | 18.9% |
| Claude: sessions timed out | 3.7% | 17.5% | 29.8% |
| Claude: mean seconds an item | 120 | 211 | 211 |
| Claude, 806 items both brain and repositories answered in time | 99.3% | 99.4% | |
| Claude, 73 proof audits all arms answered in time | 98.6% | 97.3% | 98.6% |
| Codex, 394 items: correct | 94.7% | 97.0% | 21.6% |
| Codex, 56 proof audits | 98.2% | 94.6% | 92.9% |

For Claude the brain beat the repositories 146 to 13 on the items where they disagreed (exact McNemar p = 1.2e-29) and the model alone 757 to 1. On the 806 items that both the brain arm and the repository arm finished within the time, they were tied, 3 to 4. So the lead is time: an agent searching the files finds the same records, but it needs more searches, and on a sixth of the items it was still searching when the clock ran out. The gap is widest on the walk lookups that need three or four records, where the repository arm answered 31 to 51 percent of a family and the brain arm 76 to 94 percent.

A second pass gave every session that had timed out at 600 seconds a limit of 1,200 seconds. It covered one shard of 323 items, run in all three arms. The brain arm answered 297 of them correctly at 600 seconds and 307 with the longer limit; the repository arm 259 and 278. The extra time helped the repository arm more (19 of its 52 timed-out items came back, all correct, against 10 of the brain arm's 11), but the brain still led 33 to 4 on the items where they disagreed (p = 1.1e-6), and the repository arm was still searching on 33 items after twenty minutes. Over both passes a correct answer cost 0.074 dollars with the brain and 0.153 with the repositories.

Codex agents, with half again as much time, seldom ran out of it, and there the repositories scored 97.0 percent against 94.7 (19 to 10 on the items where they disagreed, p = 0.14). On the lookups alone the repositories led 19 to 8 (p = 0.052). Of the nineteen items the brain arm lost, ten ask for page sums, differences or maxima on the problem ledger, seven for spreads or growth differences of walk counts and two for the odd source out. Sixteen were abstentions and three ran out of time; none was a wrong value, and in four the agent never called the recall tool. The client drops a recall server that is not ready when a turn starts, and on the loaded test machine a server took 1.5 to 9 seconds to start, so some brain-arm runs had no recall tool at all; marking the server as required fixed this in a probe, and the rows that did call recall were right 96.8 percent of the time. The seventeen losses counted by 28 October were asked again in three reruns, and the brain arm answered fifteen of them correctly in at least one, again with no wrong value. Most of its misses in the reruns came while the recall tool was rebuilding its prepared state, so they measure how fast recall was, not a record the store lacks. Among the first 100 Codex items, three of these losses came from searches that missed a record the repository arm found by reading the files, once because the record was mostly punctuation and digits, which the recall tool's lexical match handles poorly and a text search finds at once. No arm moved the proof audits.

Could the repository arm have seen the keys? Its own records were checked on 1 November, 1,090 runs. It made 9,998 reads and searches inside the two repositories it was given. All 61 of its attempts on denied folders were refused. 58 of its searches across the whole home folder returned files, and none of those files named a bank item. A scan of the 212,367 files in the folders it could reach found no copy of the key and no file naming three or more bank items. In any case a leak into this arm could only have narrowed the brain's lead, never made it. The deny list did, however, miss folders sitting beside a denied one and working copies of the repositories, so the next run should allow the arm the two repositories and nothing else.

### What it cost

Building the bank: the lookups and their keys came from scripts. The proof audits were written by Claude Opus 5 agents and their keys confirmed by a separate verifier, in 32 minutes and 2.3 million tokens. That record keeps no split between input and output, so at list price (5 dollars a million input tokens, 25 a million output) it cost between 12 and 58 dollars.

Running it, every session to 24 October, timeouts and reruns included:

| | Sessions | Hours | Input tokens a session | Output tokens a session | Price a session |
|---|---|---|---|---|---|
| Claude, brain | 808 | 30.6 | 20,000 | 1,500 | $0.053 |
| Claude, repositories | 808 | 53.2 | 80,000 | 4,000 | $0.092 |
| Claude, model alone | 807 | 54.8 | 2,000 | 300 | $0.010 |
| Codex, brain | 227 | 27.6 | 45,000 | 400 | |
| Codex, repositories | 231 | 17.0 | 57,000 | 600 | |
| Codex, model alone | 232 | 14.8 | 7,000 | 3,100 | |

In all: 3,113 sessions, 198 session-hours, 107 million input tokens, 5.7 million output tokens, and 125.69 dollars at list price for the Claude sessions (the runs used subscription accounts; the Codex client reports no price). A session stopped at its time limit records no tokens and no price, so those columns leave out the timed-out sessions. With Claude the brain arm read a quarter of the repository arm's input, wrote two fifths of its output, used 58 percent of its hours and cost 58 percent as much a session; since the repository arm timed out four times as often, the true ratio is probably lower. With Codex the brain arm took longer, 204 seconds a graded item against 194 (25 October accuracy cutoff), partly from sessions rerun after the connection to the recall server dropped.

What this says: when an agent has the repositories and enough time, it finds what the brain holds; the brain gets there faster and at a fraction of the reading. The items the brain arm lost to the repositories fail differently by model: with Claude most of them (9 of 13) ran out of time, three were wrong values and one an abstention; with Codex sixteen of 19 were abstentions, four of them without a single search, and three ran out of time. [AGENTS_GUIDE.md](AGENTS_GUIDE.md) turns these results into a setup for agents.

## The same 1,000 items, Codex agents with and without the brain (28 and 29 October 2026)

A fleet of Codex agents on a second machine answered the 1,000-item bank of 12 September twice, once with the recall tool and once with nothing, and the answers were graded on 29 October with the bank's own grader. Every item was answered in both arms, so all 1,000 pairs count.

| | Items | Without the brain | With the brain | Helped | Harmed |
|---|---|---|---|---|---|
| All | 1,000 | 374 | 998 | 624 | 0 |
| Lookups over the store | 923 | 300 | 923 | 623 | 0 |
| Proof audits | 77 | 74 | 75 | 1 | 0 |

The brain helped on 624 items and harmed none (exact McNemar test, p = 2.9e-188). The whole gap is in the four lookup families whose values live only in store cards: without the brain every one of those 623 answers was "unknown", and with it every one was right, each citing the card it came from. The three families of self-avoiding-walk combinations, which an agent can compute for itself, were right in both arms. So the run measures whether recall reaches the right card, not reasoning gained. A plain string match on the same rows gives the same counts. The keys were kept on a different machine from the one the agents ran on, but the grade does not prove that the agents' machine held no copy.

## Recall of results held in the store, 100 questions (11 October 2026)

Every question asks for a fact held in the store. Sixty were reworded so they share no words with their card; forty are plain. Codex agents (gpt-6.1-sol, high reasoning) took one question per session.

| Arm | Correct |
|---|---|
| no tools | 0 |
| the hook's served notes, no tools | 7 |
| text search over a copy of the store's files | 75 |
| recall tool (whole cards, ids, linked ids) | 83 |
| hook, recall tool and link walk | 82 |

The full stack against the recall tool alone went 2 to 3 (exact McNemar p = 1.0). The test had room to fail: 17 questions were wrong under the recall tool alone, so a net gain of about seven would have shown. Against text search the full stack went 10 to 3 (p = 0.09).

The hook was silent on 85 of the 100 questions, including all 60 reworded ones: its gate reads them as non-mathematical, and its search has no shared words to start from. On the 15 plain questions where it spoke, the full stack answered 11, the recall tool alone 9, text search 10 and the hook's notes alone 7.

The way results are printed decided much of the score. The same retrieval printing titles and 700-character snippets without ids scored 34; printing ids, whole cards and linked ids scored 83.

Cost, from the session logs:

| | Recall tool alone | Hook, recall and link walk |
|---|---|---|
| Input tokens, all questions | 186 million | 24.6 million |
| Uncached input tokens per question | 24 thousand | 13 thousand |
| Output tokens per question | 1.9 thousand | 0.4 thousand |
| Session-minutes | 666 | 78 |

About 98 percent of all input tokens were cached re-reads, so the saving in uncached input is 1.8 times, not 7.6. On the first 20 questions, with the same search tool in both arms, both scored 18 of 20; with the walk the sessions read 3.1 million tokens and made 40 searches, without it 16.9 million tokens and 55 searches. That comparison has two sessions an arm, so the size of the saving is uncertain, but it went the same way in every session. Agents walked 82 times alongside 273 searches, and no walk failed.

## Ranking on held-out questions (12 October 2026)

This test measures the retrieval engine and the recall tool without an agent: how often the answer card is among the first eight results, on questions that played no part in tuning.

| | Answer in the first eight |
|---|---|
| 584 questions, frozen copy from the morning | 298 |
| 584 questions, after the day's ranking changes | 317 (27 gained, 8 lost, p = 0.002) |
| six more question sets, 1,070 questions, morning copy | 891 |
| the same six sets, after | 1,018 (143 gained, 16 lost) |

The six sets moved unevenly: three gained 32, 44 and 66, two that were already near the ceiling with word search alone lost 9 and 7, and one gained 1. The ranking was tuned on questions written by Codex agents, and its largest held-out gain is on a set written by Claude agents. The gain comes from the ranking, BM25 with b = 0.4 and titles counted twice. The meaning channel adds about nothing here, and the cards added that day moved none of these counts.

## Files kept in GitHub repositories (12 October 2026)

The questions were drawn from little-known files in GitHub repositories, and Codex agents (gpt-6.1-sol, medium reasoning) answered them. A crash cut the run short. With git and the brain the agents answered 83 of 90 questions; with git alone, 76 of 90. On the 80 questions answered in both arms the scores were 73 and 68 (9 to 4, p = 0.27). The brain arm read 14 percent more tokens per question and 6 percent more per right answer, and both arms had the same share of cached input, about 98.8 percent.

## Solving and auditing, 61 items (5 and 6 October 2026)

Claude Sonnet agents worked each item with Python, Lean and file tools for up to 600 seconds; the 61 items come from four runs, pooled. The arms add one layer at a time: tools only; documents; ranked recall; the math-brain hook and math recall; held notes, a six-minute clock and a hint; and the statement of any named result the item refers to. The full package has every layer.

| Comparison | Items | Scores | Disagreements | p |
|---|---|---|---|---|
| full package against tools only | 61 | 52 and 41 | 15 to 4 | 0.019 |
| the same, without 7 items whose keys proved ambiguous | 54 | 48 and 39 | 12 to 3 | 0.035 |
| items that name a known result | 26 | 22 and 13 | 10 to 1 | 0.012 |
| items that name none | 35 | 30 and 28 | 5 to 3 | 0.73 |
| full package against documents and recall | 61 | 52 and 46 | 10 to 4 | 0.18 |

The gain over tools alone is real and sits in the items that name a known result. Against agents that already have the documents and a recall tool, the further gain is not significant.

## One thousand items whose answer must be recalled (13 September 2026)

Without the brain agents answered 538 of 1,000; with it, all 1,000. The brain helped on 462 items and harmed none (p = 1.7e-139). Every item needs a fact that has to be recalled from the store. On items a strong solver can work out for itself, the brain changes nothing.

## Twenty recall items, one agent with and without the brain (23 October 2026)

One Claude agent (Opus 5.5, high effort) took 20 items drawn at random from a 50-item recall bank. It first answered every item from its own knowledge with no tools and wrote the answers down; it then answered them again using `math_recall.py`, two or three wordings per call. A script graded both sets against keys the agent never read. Without the brain it answered 9 correctly, with it 19 (10 to 0 on the discordant items, exact sign test p = 0.002). The items it missed alone were the store's own results, such as constants found in the FEI campaign; the items it got alone were classical facts. The one item missed both ways may have a strict key.

## One solver against pairs of solvers, 48 proof audits (10 October 2026)

There were 48 proof audits, each asking whether a proof is correct and, if not, where it first fails.
The GPT arms used gpt-6.1-sol at maximum effort: one agent alone, or two agents whose answers were
reconciled. A single Claude agent (Opus 5.5) answered the same items blind, one item per call, with
no tools and no brain.

| Arm | Correct of 48 |
|---|---|
| Claude, one agent | 42 |
| GPT, one agent | 35 |
| every GPT arm, pairs included | 35 to 37 |

By kind of item, Claude scored 16 of 20 clean proofs (GPT alone 15), 20 of 20 local logic faults
(15) and 6 of 8 faults in the use of a cited result (5). Of the 12 items both members of a GPT pair
missed, Claude answered 8. A pair of one GPT agent and Claude could reach at most 43, one more than
Claude alone, because on the items they split Claude was nearly always the one that was right. On
these items the choice of model family mattered and the pairing did not. Claude used 0.30 million
tokens for the 48 items and the single GPT agent 1.62 million (the vendors count tokens differently).
This was one run, with Claude at the client's default effort and the GPT arms at maximum.

## What did not help

- **Spreading activation** (11 October). Agents told why each card came up scored 79 with spreading and 80 without, while reading 46 percent more input tokens. Without agents, on the 584 questions, spreading moved first-eight hits from 298 to 307, but it found no card the word search had missed: it only re-ranks.
- **New open problems** (11 October). Fourteen Codex agents worked 13 open problems on which the store held only a first attempt from September. Graded blind, the brain arm scored 24 of 39 and the no-brain arm 26. A referee comparing each pair preferred the no-brain attempt 8 times and the brain's 3 times, with 2 even (p = 0.23).
- **An early version against plain documents** (a hard 300-item set, no tools). Version 1 of the math-brain stream (hook notes, math recall, Lean and an audit step) scored 238; agents given the documents directly scored 264 (14 to 40, p = 0.0005). Most of the loss was in one group of 70 items, 22 against 55. A later version, which routes to math recall first and adds a clock, scored 102 of 110 against 104 for documents with recall (6 to 8, p = 0.79).
- **Teams** (8 and 9 October). On 20 items run with Codex, graded with the current grader (version 1.19, which accepts equivalent expressions and answer forms that version 1.3 marked wrong), a single agent with the brain scored 19, a team with the brain 20, a single agent without the brain 18 and a team without it 17. Every contrast is a difference of one to three items. A team used about three times the tokens (a median of 56,000 to 68,000 against 17,000 to 18,000), and a vote of three Claude agents scored 19, no better than its best member. Six items that no run had solved under version 1.3 are solved by some or all runs; the gap was in the grading, not the reasoning. Each of the 20 keys grades itself correct, and none of 41 corrupted keys does.
- **Query expansion and fusion in the engine** (15 October). On a 300-item recall bank, split into two halves of 292 questions each, pseudo-relevance feedback, reciprocal-rank fusion with the meaning channel, a wider meaning pool and a one-edge graph hop all failed to beat the live ranking for first place, the first eight or mean reciprocal rank (live: first place 112 and 106, first eight 158 and 156). Fusing in the meaning channel moved about 15 more answers into the first 200 and cost 15 to 20 first places. On the 94 fully reworded questions the live ranking put no answer in the first eight. What helps there is the agent rewording its own query in the card's vocabulary.
- **BM25 in the math hook** (19 October). With BM25 (k1 = 1.2, b = 0.3) in place of the hook's length-penalized word score, on the 218-question hook bank, 12 questions gained first place and 10 lost it, cards with content served went from 70 to 69, and false fires on questions the store cannot answer rose from 28 to 31 of 40. The hook keeps its original scoring. Its firing thresholds are tuned to that scoring, so a new ranker needs its thresholds recalibrated before it can be compared fairly.
- **Spreading after the store's links grew** (28 and 29 October). With the store at about 90,800 cards and 126,000 links, depth 1 against depth 0 on the held-out recall bank: on the 43 items where depth 1 finished, the right card came first for 18 and 18 and was in the first eight for 22 and 22, at a median of 13.2 seconds a call against 2.9. A second bank was built to favour it: 30 items whose answer card shares few words with the question but sits one link from a card that shares more. The answer was printed for the same 11 items at both depths. On that bank the answers come from the link lines printed under each card at depth 0: with those lines switched off the answer is printed for none of the 30.
- **A cap on compaction summaries in recall** (28 October). One misspelled query returned four of its eight rows from a single session's compaction summaries, so a cap of one or two summaries a session was scored on 110 queries. On 40 ordinary memories, each asked for once cleanly and once with typos, the first eight held the answer 38 and 37 times in every arm, and summaries filled 1 and 3 of the 320 slots. On 30 queries asking for a summary itself, the cap cut exact hits in the first eight from 12 to 5 or 6. The cap stays off.
- **Weighting the second hop of the association walk** (28 October). The walk that adds associations to a recall result runs two hops. A flow tracer that keeps the inflow of each hop separately suggested scoring a node as its seed and first-hop activation plus lam times its second-hop activation, so that far associations count for less. Five values of lam from 1.0 down to 0 were scored on 195 held-out hand-written links, five folds of 40. At lam 1.0 the scores matched the shipped walk to 5e-10. Mean reciprocal rank on the graph arm was 0.1518 at lam 1.0 against 0.1521, 0.1512, 0.1504 and 0.1503 for the others; no value won or lost on every fold, and on one fold all five tied. The weighting stays out.
- **A floor on the association walk** (28 October). The same tracer stops expanding a node whose share falls below a small fraction of the source. On 97 real prompts against a graph of 36,191 nodes, floors up to 3e-4 of the total seed activation cut edge visits by 8 to 12 percent and saved a few milliseconds of a step that takes about 55, yet still changed the top five on 3 to 7 of the 97 prompts. From 1e-3 up the floor changed which associations passed the gate on 5 to 16 prompts, and on prompts with many small seeds it pruned every seed. Recall stops at two hops, so there is little for a floor to cut. No floor is used.
- **A store bank the repository arm could recompute** (1 November). Codex agents answered a sample of the 1,000-item bank in two arms, with the brain and with the repositories only. Counting the runs that reached the model, the brain arm scored 83 of 84 and the repository arm 82 of 84, so the bank no longer separates the two. The commands each repository run issued show why. Of its 82 right answers, 56 came from code the agent wrote and ran in the session, mostly counting the self-avoiding walks whose counts the store holds, and they searched nothing. Another 15 came from a text search whose output held the answer, nearly all of them paper-and-page lookups matched against titles in the store's export, which sat in one of the arm's repositories. A bank that separates the arms needs answers that cannot be recomputed in a few minutes or found by a title search, such as proof audits and facts the store took from a paper or a long run, and a repository arm without the store's export.
- **Down-weighting compaction summaries** (2 November). A compaction summary repeats the user's words exactly, so on a quoted sentence it can outrank the record that holds the order. Multiplying every summary's word score by 0.6 lifted the first hit on 187 quoted sentences from 140 to 157 and left 1,000 questions about ordinary records level (652 first hits; 853 to 857 in the first eight), but it cut the first eight on 1,976 questions about the summaries themselves from 482 to 129. A summary is the only record of its session, so the change was not kept. Each bank was written from its own answers and favours its own side, but a fourfold loss is beyond that.
