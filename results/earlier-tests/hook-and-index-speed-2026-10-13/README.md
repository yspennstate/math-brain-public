# Index and hook speed work (13-14 October 2026)

The probes of 12 October showed where a recall spends its time. In the two days after them, the next round of work
moved to the lexical index's publish step, the hook dispatcher that runs on every tool call, and the reflex triggers
the dispatcher matches. Each change was made on a copy and compared with the live code on the same inputs, and it
counted only if the output was unchanged. Times are on one busy laptop, so the before and after numbers for a change
were taken side by side in alternating order.

| change | before | after |
|---|---|---|
| index publish: one-shot text encoding instead of a streamed encoder | refresh 20.3 s median | 6.0 s, same text |
| index cache written with the index, not after it | stale cache in 15 to 18 per cent of samples; recalls of 12 to 20 s | cache moves in with the index |
| index publish waits out a reader instead of failing | 10 of 104 publishes failed | waits up to 20 s under the lock |
| one background refresh at a time | 34 to 35 refreshes stacked, about 11 GB | single flight |
| nine hooks moved into the dispatcher's own process | Bash pre-call 0.34 s | 0.01 s |
| compiled hook code kept between calls, allowlist read once | 0.748 s per tool call | 0.457 s |
| compaction hook moved in process | 176.7 ms per call | 27.7 ms |
| one quadratic reflex trigger anchored | 8.43 s on a 16 KB text | 0.0009 s |

## The index publish

A refresh folds new and changed memories into the lexical index and publishes it. Under load it took 17 to 28 s, and
three quarters of that was the JSON encoder. Python's fast encoder is used only for a one-shot `dumps`; `dump` into a
compressed stream runs the pure Python encoder and pushes every small piece through two stream layers. On the live
index (21,512 memories, 307,789 terms) that cost 17.0 to 17.6 s, against 4.2 to 4.4 s for one `dumps` and one
compressed write of the same bytes. The change also stopped re-interning strings that the parsed payload already
shared. In shadow refreshes on copies of the index, alternating order, the refresh took 20.3 s median before and 6.0 s
after (four runs each, 19.8 to 20.9 against 5.7 to 6.4), and the published text was identical where the runs read the
same documents.

The parsed cache beside the index used to be written after the index was replaced, best effort. When a reader held
the old cache or the lock was busy, the write gave up and every reader paid a full parse until one of them rebuilt it.
A probe that only reads file metadata found the cache behind the index in 15.5 and 18.1 per cent of samples over two
windows, with lags of 4.4 to 89.3 s after a publish. Stack samples put all four 12 to 20 s recall stalls in that
load. The cache is now written first, bound to the staged index's file signature, and moved in under the same lock.

On Windows the final rename fails while any process holds the index open without delete sharing; 10 of 104 publishes
over one night died that way, 9 of them in the busiest hour. The publish now retries with backoff for up to 20 s inside
the lock. Two publishes still failed after the full wait the next morning; the readers that streamed the compressed
file were changed to read its bytes first, which shortens how long a reader holds it from 9.05 and 13.34 s to 0.067 and 0.107 s.

Every recall started a detached refresh whenever a memory was newer than the index. Two diagnostic loops stacked 34
to 35 of them, about 11 GB, on a machine with 6.8 GB free. A guard now starts one only when no live refresh is
already running.

## The hook dispatcher

Every tool call starts a fresh dispatcher, which runs a few hundred small hooks. Nine hooks that still started their
own Python each time were moved into the dispatcher's process. In an A/B on fixed payloads:

| event | before | after |
|---|---|---|
| Bash pre-call | 0.34 s | 0.01 s |
| Bash post-call | 0.19 s | 0.03 s |
| Edit post-call | 0.38 s | 0.04 s |
| prompt submit | 2.21 s | 1.14 s |
| stop | 0.45 s | 0.08 s |

Pooled over every live session, the median Bash pre-call went from 1.31 s to 0.79 s; an untouched control event fell
about 0.1 s over the same minutes, so about 0.4 s of the drop is this change.

The move found a blind spot in the equivalence check. In process a hook is handed a string buffer as its input, and a
string buffer has no byte stream under it. A hook that reads the byte stream with no fallback fails inside its own
error handler and prints nothing, and the check passes because on its test payloads the hook printed nothing in
either mode. The check now records any input attribute a hook looked for and did not find. Two hooks that had been
kept out of process for that reason (the project check and the compaction hook) then joined: the compaction hook went
from 176.7 ms a call as a process to 27.7 ms in process, with the same output, state and records on 30 of 30 payloads.

Two costs were paid again on every call. Hook files were compiled from source each time (166 ms of a Bash pre-call
and 372 ms of a prompt under load, against 10 and 17 ms from kept code), and a 13 KB allowlist was parsed once per
hook entry (64 ms warm, 113 to 125 ms loaded). Code objects are now kept keyed on path, size and modification time,
and the allowlist is read once per dispatch. Exact control: 240 of 240 kept code objects equal a fresh compile, 407 of
407 hook runs gave the same output, and 1,385 of 1,385 entries made the same in-process or subprocess decision. End to
end, a Bash pre-call went from 0.748 s to 0.457 s and a Write from 0.754 s to 0.461 s.

## Reflex triggers

The reflex hook matches a few hundred regular expressions against the tool input, cut at 16 KB, on every call. One
learned trigger was two dotall lookaheads and nothing else. With `findall` it is retried at every position and each
`.*` scans to the end, so its cost is quadratic in the text:

| text | old | anchored |
|---|---|---|
| 500 characters | 0.011 s | 0.00003 s |
| 2 KB | 0.087 s | 0.00009 s |
| 8 KB | 2.05 s | 0.0005 s |
| 16 KB | 8.43 s | 0.0009 s |

The hook had logged a second or more 233 times in six hours, at most 13.6 s. A cost check added for every new trigger
timed each one on a single fixed text. It passed a second quadratic trigger whose exclusions happened to cut that text
short; that trigger took 89.7 s of one day's matching (9.3 per cent of all of it, worst call 7.5 s) and fired four
times. The check now times every trigger on texts built from its own words.

Three more triggers opened with a negative lookahead over a 200 to 320 character window and paid that scan at every
position of a 16 KB text. A guard of the words their alternatives begin with now stands in front of the window; the
matches are the same. Separately, the prefilter that skips a trigger on texts lacking its required words learned that
whatever a positive lookahead requires is also required by the text. Before, 22 triggers had no words and ran on
every text. Over 22,847 real hook texts of one day the new words skip texts that took 416 s of matching, and none of
the skipped texts holds a match.

## The query encoder

Building the encoder session holds the interpreter lock for its whole 0.65 s; a spinning thread got 3 to 4 per cent
of that time, so recall's main thread stalled behind it. The session is now built in a helper process. In paired runs
a recall was 1.04 s faster as a command (25 of 40 pairs) and 1.20 s faster in process (26 of 40).

## Measured but not changed

- Where a recall spends its time: about 5.0 s in process (7.4 to 7.8 s as a command), of which 1.5 s choosing seeds
  and 1.2 to 1.7 s in the graph lane, most of that importing a sparse matrix library. A cold recall in a fresh process
  took 1.9 to 2.5 s on a quiet machine and 3.4 to 5.9 s loaded.
- A profiler put 7 to 11 s on path normalisation calls that, untraced, took 135 to 185 ms a recall, so the profile
  was wrong about this code by a factor of about fifty.

Counts only.
