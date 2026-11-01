"""Replay actual display-loop AST against a live retraction and bounded synthetic controls.

This executes the display loops from the frozen original/candidate, without importing
brain.py or running graph, semantic, usage, index-refresh, or background operations.
"""
from pathlib import Path
import ast
import contextlib
import io
import json
import os
import re
import time
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parent
SLUG = 'the_binding_constraint_is_m_not_l1prime_2026_08_29'
MEM = '~/.claude/projects/<project>/memory'

def load_display(path):
    source = path.read_text(encoding='utf-8')
    tree = ast.parse(source, filename=str(path))
    compile(tree, str(path), 'exec')  # syntax-check the complete candidate
    names = {'_status_from_index', '_frontmatter_retracted', '_full_description', '_display_rows'}
    helpers = [node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name in names]
    recall = next(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == 'recall')
    collect = next(node for node in recall.body if isinstance(node, ast.For)
        and isinstance(node.iter, ast.Call) and isinstance(node.iter.func, ast.Name)
        and node.iter.func.id == '_display_rows')
    output = next(node for node in recall.body if isinstance(node, ast.For)
        and isinstance(node.iter, ast.Name) and node.iter.id == 'displayed')
    wrapper = ast.parse('def replay(scored, idx):\n    displayed = []\n    shown = 0\n    return displayed\n').body[0]
    wrapper.body[2:2] = [collect, output]
    module = ast.fix_missing_locations(ast.Module(body=helpers+[wrapper], type_ignores=[]))
    namespace = {'re': re, 'io': io, 'os': os, 'MEM': MEM, 'n': 8,
        '_floor_break': False, 'SNIPPET_MAX': 320, 'lineage': {},
        'superseded': {}, 'known_slugs': set(), '_part_flag': lambda *args: '',
        '_moved_flag': lambda *args: '', '_lesson_line': lambda *args: '',
        'sr': SimpleNamespace(_desc=lambda slug, idx: 'index fallback description')}
    exec(compile(module, str(path), 'exec'), namespace)
    return namespace

def replay(namespace, slug, index_status):
    tag = '' if index_status == 'legacy' else f' - [{index_status.upper()}]'
    index = {slug: f'- [{slug}.md]({slug}.md){tag} old description'}
    status = namespace['_status_from_index'](slug, index)
    captured = io.StringIO()
    with contextlib.redirect_stdout(captured):
        displayed = namespace['replay']([(0.9, 1.0, 0.0, 0.0, slug, status)], index)
    return {'status': displayed[0][-1], 'text': captured.getvalue()}

started = time.perf_counter()
before = load_display(ROOT/'copies'/'brain.before.py')
after = load_display(ROOT/'copies'/'brain.after.py')
actual_before = replay(before, SLUG, 'provisional')
actual_after = replay(after, SLUG, 'provisional')
assert before['_frontmatter_retracted'](SLUG), 'Live memory no longer has the observed retraction.'
assert actual_before['status'] == 'provisional'
assert actual_after['status'] == 'retracted'
assert 'block-increment exponent' in actual_before['text']
assert 'block-increment exponent' not in actual_after['text']

fixture_dir = ROOT/'display_fixtures'
fixture_dir.mkdir(exist_ok=True)
fixtures = {
    'retracted': '---\nstatus: retracted\ndescription: unsafe withdrawn mathematical conclusion\n---\nCorrection follows.\n',
    'withdrawn': '---\nstatus: "withdrawn"\ndescription: unsafe withdrawn mathematical conclusion\n---\nCorrection follows.\n',
    'headline': '---\nstatus: headline-retracted-in-place\ndescription: unsafe withdrawn mathematical conclusion\n---\nCorrection follows.\n',
    'active': '---\nstatus: verified\ndescription: an active mathematical statement\n---\nBody mentions status: retracted as an example.\n',
    'unclosed': '---\nstatus: retracted\ndescription: unclosed frontmatter\n',
}
for slug, content in fixtures.items():
    (fixture_dir/(slug+'.md')).write_text(content, encoding='utf-8')
for namespace in (before, after):
    namespace['MEM'] = str(fixture_dir)
control_results = []
for slug in ('retracted', 'withdrawn', 'headline'):
    for tag in ('provisional', 'verified', 'owner-stated', 'legacy'):
        old = replay(before, slug, tag)
        new = replay(after, slug, tag)
        assert new['status'] == 'retracted'
        assert 'unsafe withdrawn mathematical conclusion' not in new['text']
        control_results.append({'case': slug+'/'+tag,
            'before_stale_label': old['status'] != 'retracted',
            'after_stale_label': new['status'] != 'retracted',
            'before_unsafe_snippet': 'unsafe withdrawn' in old['text'],
            'after_unsafe_snippet': 'unsafe withdrawn' in new['text']})
for slug in ('active', 'unclosed', 'missing'):
    for tag in ('provisional', 'verified', 'owner-stated', 'legacy'):
        old = replay(before, slug, tag)
        new = replay(after, slug, tag)
        assert old == new, (slug, tag, old, new)
        control_results.append({'case': slug+'/'+tag, 'unchanged': True})
index_retracted = replay(after, 'active', 'retracted')
assert index_retracted['status'] == 'retracted'
assert 'an active mathematical statement' not in index_retracted['text']
receipt = {'command': 'python -X utf8 verify_recall_display.py',
    'observed_live_row': {'slug': SLUG, 'before': actual_before, 'after': actual_after,
        'stale_label_before': 1, 'stale_label_after': 0,
        'unsafe_snippet_before': 1, 'unsafe_snippet_after': 0},
    'synthetic_cases': len(control_results)+1, 'controls': control_results,
    'synthetic_stale_labels_before': sum(r.get('before_stale_label', False) for r in control_results),
    'synthetic_stale_labels_after': sum(r.get('after_stale_label', False) for r in control_results),
    'synthetic_unsafe_snippets_before': sum(r.get('before_unsafe_snippet', False) for r in control_results),
    'synthetic_unsafe_snippets_after': sum(r.get('after_unsafe_snippet', False) for r in control_results),
    'active_or_unavailable_cases_unchanged': sum(r.get('unchanged', False) for r in control_results),
    'elapsed_seconds': round(time.perf_counter()-started, 6), 'deployed': False,
    'limits': 'Actual display-loop replay; no end-to-end recall or corpus-wide improvement claim.'}
(ROOT/'DISPLAY_TEST_RECEIPT.json').write_text(json.dumps(receipt, indent=2)+'\n', encoding='utf-8')
print(json.dumps({k:v for k,v in receipt.items() if k not in ('observed_live_row','controls')}))
