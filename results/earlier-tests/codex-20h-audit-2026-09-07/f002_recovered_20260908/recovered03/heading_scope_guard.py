"""Admission review for qualified proof headings; never labels a proof false."""
import ast
import hashlib
import json
from pathlib import Path
import re

HERE=Path(__file__).resolve().parent
QUALIFIED = re.compile(
    r'\b(?:in|for)\s+(?:the\s+)?(?:dimension|dimensions|characteristic)\b|'
    r'\b(?:for|when|if|assuming)\s+(?:the\s+)?(?:\$|\\\(|\\\[)?\s*'
    r'(?:[a-zA-Z](?:_[a-zA-Z0-9{}]+)?\s*(?:=|<|>|\\leq?|\\geq?|\\in\b)|'
    r'(?:odd|even|positive|negative|finite|infinite)\b|'
    r'[a-zA-Z]\s+(?:odd|even|positive|negative|finite|infinite)\b)|'
    r'\b(?:odd|even|positive|negative|finite|infinite)\s+(?:dimension|characteristic)\b',re.I)


def load_original_predicate():
    raw=(HERE/'bank_baseline/extract_proofs.py').read_bytes()
    manifest=json.loads((HERE/'BANK_HEADING_BASELINE.json').read_text(encoding='utf-8'))
    if hashlib.sha256(raw).hexdigest()!=manifest['extractor_sha256']:
        raise ValueError('Frozen extractor changed')
    tree=ast.parse(raw)
    nodes=[n for n in tree.body if
           isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='PARTIAL_RE' for t in n.targets)
           or isinstance(n,ast.FunctionDef) and n.name=='is_partial_heading']
    if len(nodes)!=2:raise ValueError('Expected standalone original heading predicate')
    module=ast.Module(body=nodes,type_ignores=[])
    env={'re':re};exec(compile(module,'frozen_heading_predicate','exec'),env)
    return env['is_partial_heading']


def assess(row,original_predicate):
    fields=[name for name in ['proof_heading','proof_opt'] if name in row]
    if not fields:return {'admit':False,'status':'HEADING_METADATA_UNVERIFIED'}
    values=[row[name] for name in fields]
    if any(not isinstance(v,str) for v in values) or len(set(values))!=1:
        return {'admit':False,'status':'HEADING_METADATA_CONFLICT'}
    heading=values[0]
    if row.get('partial_heading') or original_predicate(heading):
        return {'admit':False,'status':'EXISTING_PARTIAL_HEADING_EXCLUSION'}
    # Remove only reference commands for this predicate, leaving mathematical
    # parameter qualifiers intact. An explicit empty heading is ordinary metadata.
    text=re.sub(r'\\(?:ref|cref|Cref|autoref|label)\{[^}]*\}',' ',heading)
    cue=QUALIFIED.search(text)
    if cue:return {'admit':False,'status':'QUALIFIED_HEADING_REQUIRES_SCOPE_REVIEW','cue':cue.group(0)}
    return {'admit':True,'status':'NO_HEADING_SCOPE_FLAG','scope':'Heading screen only; whole-item validity still unverified'}
