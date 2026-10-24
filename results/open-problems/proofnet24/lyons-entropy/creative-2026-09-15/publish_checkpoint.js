/* Execute in functions.exec with tools, load, store, text, message as parameters.
 * Only the coordinator runs this. It publishes completed, explicitly indexed work.
 * No credentials are stored. Branch updates are always non-forced.
 */
const base = load('creative2026_base');
const prefix = load('creative2026_repo_prefix');
const repo = 'yspennstate/math-open-problems';
if (!base || !prefix) throw Error('Missing observed campaign paths');
const indexed = await tools.exec_command({
  cmd: 'python3 ' + base + '/campaign_admin.py --index',
  max_output_tokens: 70000,
});
if (indexed.exit_code !== 0) throw Error(indexed.output);
const index = JSON.parse(indexed.output);
store('creative2026_index', index);
const old = load('creative2026_published_hashes') || {};
const changed = Object.keys(index.files).filter(p => old[p] !== index.files[p].sha256);
if (!changed.length) { text({unchanged: true, counts: index.counts}); return; }
const files = [];
const utf8Length = value => {
  let size = 0;
  for (const character of value) {
    const point = character.codePointAt(0);
    size += point < 128 ? 1 : point < 2048 ? 2 : point < 65536 ? 3 : 4;
  }
  return size;
};
async function readCompleteFile(p) {
  const metadata = index.files[p];
  const chunkSize = 16000;
  async function readChunk(start) {
    const result = await tools.exec_command({
      cmd: "python3 -c 'import json,hashlib; from pathlib import Path; b=Path(" +
        JSON.stringify(base + '/' + p) + ").read_bytes(); s=b.decode(\"utf-8\"); " +
        "print(json.dumps({\"content\":s[" + start + ":" + (start + chunkSize) +
        "],\"total\":len(s),\"sha256\":hashlib.sha256(b).hexdigest()},ensure_ascii=False))'",
      max_output_tokens: 65000,
    });
    if (result.exit_code !== 0 || result.original_token_count > 65000 ||
        result.output.startsWith('Warning: truncated')) {
      throw Error('Incomplete indexed chunk read: ' + p + ':' + start);
    }
    const chunk = JSON.parse(result.output);
    if (chunk.sha256 !== metadata.sha256 ||
        Array.from(chunk.content).length !== Math.min(chunkSize, chunk.total - start)) {
      throw Error('Changed file or incomplete chunk: ' + p + ':' + start);
    }
    return chunk;
  }
  const first = await readChunk(0);
  const pieces = [first.content];
  const starts = [];
  for (let start = chunkSize; start < first.total; start += chunkSize) starts.push(start);
  for (let begin = 0; begin < starts.length; begin += 8) {
    const results = await Promise.allSettled(starts.slice(begin, begin + 8).map(readChunk));
    for (const result of results) {
      if (result.status !== 'fulfilled') throw result.reason;
      if (result.value.total !== first.total) throw Error('Changed file length: ' + p);
      pieces.push(result.value.content);
    }
  }
  const content = pieces.join('');
  if (Array.from(content).length !== first.total || utf8Length(content) !== metadata.bytes) {
    throw Error('Incomplete assembled file: ' + p);
  }
  return {path: p, content};
}
for (let begin = 0; begin < changed.length; begin += 8) {
  const results = await Promise.allSettled(changed.slice(begin, begin + 8).map(async p => {
    if (!/^[A-Za-z0-9_./-]+$/.test(p)) throw Error('Unexpected indexed path: ' + p);
    if (!/^[A-Za-z0-9_./-]+$/.test(base)) throw Error('Unexpected base path');
    return readCompleteFile(p);
  }));
  const errors = results.filter(r => r.status === 'rejected');
  if (errors.length) throw Error(errors.map(r => String(r.reason)).join('\n'));
  files.push(...results.map(r => r.value));
}
store('creative2026_checkpoint_files', files);
let published;
for (let attempt = 0; attempt < 4; attempt++) {
  const response = await tools.mcp__codex_apps__github_fetch({
    url: 'https://api.github.com/repos/' + repo + '/branches/master',
  });
  if (response.isError) throw Error(JSON.stringify(response));
  const head = JSON.parse(response.structuredContent.content);
  const tree = await tools.mcp__codex_apps__github_create_tree({
    repository_full_name: repo,
    base_tree_sha: head.commit.commit.tree.sha,
    tree_elements: files.map(f => ({path: prefix + '/' + f.path,
      mode: '100644', type: 'blob', content: f.content})),
  });
  if (tree.isError || !tree.structuredContent?.sha) throw Error(JSON.stringify(tree));
  const commit = await tools.mcp__codex_apps__github_create_commit({
    repository_full_name: repo,
    parent_sha: head.commit.sha,
    tree_sha: tree.structuredContent.sha,
    message,
  });
  if (commit.isError || !commit.structuredContent?.sha) throw Error(JSON.stringify(commit));
  store('creative2026_pending_commit', commit.structuredContent.sha);
  const updated = await tools.mcp__codex_apps__github_update_ref({
    repository_full_name: repo, branch_name: 'master',
    sha: commit.structuredContent.sha, force: false,
  });
  if (updated.structuredContent?.success) {
    published = commit.structuredContent.sha;
    break;
  }
  if (!/fast.forward|non.fast.forward|reference update failed/i.test(JSON.stringify(updated))) {
    throw Error(JSON.stringify(updated));
  }
}
if (!published) throw Error('Concurrent branch changes prevented publication; nothing forced');
const hashes = Object.fromEntries(Object.entries(index.files).map(([p, m]) => [p, m.sha256]));
store('creative2026_published_hashes', hashes);
store('creative2026_last_commit', published);
const recovery = JSON.stringify({last_commit: published, published_hashes: hashes});
await tools.apply_patch('*** Begin Patch\n*** Add File: ' + base +
  '/tmp_campaign_recovery.json\n+' + recovery + '\n*** End Patch');
const saved = await tools.exec_command({
  cmd: "python3 -c 'import json; from pathlib import Path; p=Path(" + JSON.stringify(base) +
    "); f=p/\"SESSION_STATE.json\"; s=json.loads(f.read_text()); " +
    "s[\"campaign\"].update(json.loads((p/\"tmp_campaign_recovery.json\").read_text())); " +
    "l=json.loads((p/\"execution_ledger.json\").read_text()); " +
    "a=json.loads((p/\"ASSIGNMENTS.json\").read_text()); " +
    "seen={r[\"id\"] for r in l}; " +
    "s[\"campaign\"][\"active_handoff\"]={\"assignments_launched\":len(l)," +
    "\"actual_agent_launches\":len({a[\"task\"] for r in l for a in r.get(\"attempts\",[{\"task\":r[\"task\"]}])})," +
    "\"execution_attempts\":sum(len(r.get(\"attempts\",[0])) for r in l)," +
    "\"completed_assignments\":sum(r[\"status\"]==\"completed\" for r in l)," +
    "\"running_tasks\":[r[\"task\"] for r in l if r[\"status\"]==\"running\"]," +
    "\"next_unlaunched\":next((r[\"id\"] for r in a if r[\"id\"] not in seen),None)," +
    "\"goal\":\"Complete all100 creative assignments, with replacement attempts separately recorded. Paper and email done; full Lyons open.\"}; " +
    "f.write_text(json.dumps(s,indent=2)+\"\\n\"); " +
    "(p/\"tmp_campaign_recovery.json\").unlink()'",
  max_output_tokens: 1000,
});
if (saved.exit_code !== 0) text({recovery_save_error: saved.output});
text({commit: published, changed_files: files.length, counts: index.counts});
