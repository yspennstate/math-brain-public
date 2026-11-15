---
name: bm25_index_writer_streams_json_in_pieces_2026_11_11
description: "bm25 refresh MemoryError while writing the index (json.dumps of 234M chars; 6 in bm25_refresh.log, four on 9 Nov)? Since 11 Nov 01:06 bm25.py (97dea957) writes the json in pieces: same bytes, 33 MB extra instead of 232 MB, same speed warm (about 4 s); a cold first round misreads as 1.5-2x slower"
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T01:10:31+02:00
  status: verified
  evidence: "brain_improvement/agent_run/bm25_json_stream/landed_20261111 (test.txt, bench.txt, verify.txt)"
---

Since 11 Nov 2026 01:06 (laptop clock) `~/.claude/dreaming/bm25.py` (sha256 97dea957dddf3bb3) writes the index text in
pieces. `_write_json_text` no longer calls `json.dumps(payload)` once; `_json_pieces` hands a large dict or list to the
same C encoder 256 entries at a time and the writer flushes every 8 MB.

**The failure it closes.** The refresh died with MemoryError six times in `bm25_refresh.log`: twice inside the gzip
write ("Unable to allocate output buffer", 15 and 30 Oct) and four times in a row inside the json encoder on 9 Nov
04:22, at 59,248 docs. One `json.dumps` of the payload is a single string of 234 million characters (61,710 docs on
11 Nov) plus the encoder's chunk list; on a box at 85 pct commit that allocation fails and the refresh publishes
nothing, so new memories stay dark to recall until a later refresh gets through.

**Measured on the live payload.** Same bytes as `json.dumps(payload).encode()` (233,683,627 bytes, same sha256; and
again in each writer's own process). Extra private memory while writing: 232 MB old, 33 MB new. Time, three
alternating warm rounds in one process: old 4.33 / 3.38 s, new 3.68 / 4.37 s, so no cost. A first cold round read
14.8 s old against 26.7 s new and the control's own 1.5x timing check failed once (70.9 s against 45.3 s): that was
page-in on a loaded machine, not the writer; time a writer only after a warm pass over the payload. Seventeen small
cases (coerced keys, an int key beside its string, nested big containers, empties, floats, tuples) at six batch
thresholds give the text of `json.dumps` character for character.

**After landing.** `bm25.py refresh` ran once with the new writer (+8 memories, 61,710 docs); the index on disk
decompresses to 233,770,041 bytes that equal `json.dumps` of the loaded payload, and `brain.py recall` answers.

**How to apply.** If the index writer is changed again, keep the byte-equality control
(`brain_improvement/agent_run/bm25_json_stream/test_stream.py <patched> <old>`) and `verify_live.py` after the
first refresh. Rollback: copy `bm25.py.bak_stream_20261111_0110` over `bm25.py` (that backup carries the 10 Nov
one-query top-k change, sha 2181befb99b66d9c).

**Not covered.** The gzip compressor and the reader (`json.load` of the whole index) still hold the full payload;
a reader at 234 MB of text is the next place memory can fail.

