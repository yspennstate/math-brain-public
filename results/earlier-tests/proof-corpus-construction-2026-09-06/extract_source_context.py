"""Extract review candidates with preserved source context; never certify proofs.

This continuation deliberately leaves sealed plit/mdlit banks untouched. The
upstream helper is byte-pinned and retains its repaired partial-proof headings
and distinguishable external references. Every output remains private review
material until source, license, hypotheses and mathematical validity are checked.
"""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import importlib.util
import gzip
import json
from pathlib import Path
import re
import tarfile

UPSTREAM_SHA256 = 'c162bbd256518a34a8b50c726b5f71b493e31c2110d180ecf69d3ff1451a3b94'
HERE = Path(__file__).resolve().parent
UPSTREAM = HERE / 'upstream_extract_proofs.py'


def sha(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def digest(value) -> str:
    return sha(json.dumps(value, ensure_ascii=False, sort_keys=True,
                          separators=(',', ':'), allow_nan=False).encode())


def load_upstream():
    if sha(UPSTREAM.read_bytes()) != UPSTREAM_SHA256:
        raise ValueError('upstream helper differs from its reviewed pin')
    spec = importlib.util.spec_from_file_location('pinned_proof_extractor', UPSTREAM)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


U = load_upstream()


class SourceContextError(ValueError):
    pass


def file_sha(path: Path, max_bytes=64_000_000) -> str:
    if path.stat().st_size>max_bytes:
        raise SourceContextError('archive byte budget exceeded')
    result=hashlib.sha256()
    size=0
    with path.open('rb') as stream:
        for block in iter(lambda:stream.read(1_000_000),b''):
            size+=len(block)
            if size>max_bytes:
                raise SourceContextError('archive grew beyond byte budget')
            result.update(block)
    return result.hexdigest()


def verify_archive_origin(archive: Path, download: dict, files: list[dict]):
    """Compare read TeX bytes to pinned archive members without extracting files."""
    archive=archive.resolve(strict=True)
    observed=file_sha(archive)
    if observed!=download['sha256']:
        raise SourceContextError('archive hash differs from download receipt')
    matches=[]
    if download['kind']=='tar':
        with tarfile.open(archive,mode='r:*') as stream:
            members=stream.getmembers()
            if len(members)>20000:
                raise SourceContextError('archive member budget exceeded')
            by_flat={}
            for member in members:
                if member.isfile():
                    flat=member.name.replace('/','__').replace('\\','__')
                    by_flat.setdefault(flat,[]).append(member)
            for receipt in files:
                found=by_flat.get(receipt['relative_path'],[])
                if len(found)!=1:
                    raise SourceContextError('source has missing or colliding archive origin: '+receipt['relative_path'])
                member=found[0]
                if member.size!=receipt['bytes'] or member.size>4_000_000:
                    raise SourceContextError('archive member size differs from source')
                with stream.extractfile(member) as member_stream:
                    raw=member_stream.read(member.size+1)
                if sha(raw)!=receipt['sha256']:
                    raise SourceContextError('source bytes differ from archived member: '+receipt['relative_path'])
                matches.append({'source_file':receipt['relative_path'],'archive_member':member.name,
                                'sha256':receipt['sha256'],'bytes':len(raw)})
    else:
        if len(files)!=1 or files[0]['relative_path']!='main.tex':
            raise SourceContextError('single-TeX archive cannot supply other local files')
        with archive.open('rb') as stream:
            magic=stream.read(2)
            stream.seek(0)
            if magic==b'\x1f\x8b':
                with gzip.GzipFile(fileobj=stream) as uncompressed:
                    raw=uncompressed.read(4_000_001)
            else:
                raw=stream.read(4_000_001)
        if len(raw)>4_000_000 or sha(raw)!=files[0]['sha256']:
            raise SourceContextError('single-TeX source differs from archive or exceeds budget')
        matches.append({'source_file':'main.tex','archive_member':'single_tex_payload',
                        'sha256':sha(raw),'bytes':len(raw)})
    if file_sha(archive)!=observed:
        raise SourceContextError('archive changed during source verification')
    return {'status':'ARCHIVE_HASH_AND_READ_SOURCE_MEMBER_BYTES_MATCH',
            'archive_path':str(archive),'archive_sha256':observed,'members':matches,
            'limit':'Verifies exact binary origin of files read. The arXiv version is the download log attribution, not an independently verified server version.'}


class SourceReader:
    def __init__(self, root: Path, max_bytes=4_000_000, max_depth=12):
        self.root = root.resolve(strict=True)
        self.max_bytes = max_bytes
        self.max_depth = max_depth
        self.receipts = {}
        self.issues = []
        self.total_bytes = 0

    def checked(self, path: Path) -> Path:
        resolved = path.resolve()
        if not resolved.is_relative_to(self.root):
            raise SourceContextError('include escapes paper source directory')
        return resolved

    def read(self, path: Path) -> str:
        path = self.checked(path)
        raw = path.read_bytes()
        relative = path.relative_to(self.root).as_posix()
        previous = self.receipts.get(relative)
        if previous and previous['sha256'] != sha(raw):
            raise SourceContextError('source changed during read: '+relative)
        if not previous:
            self.total_bytes += len(raw)
            if self.total_bytes > self.max_bytes:
                raise SourceContextError('paper source byte budget exceeded')
        try:
            text, encoding = raw.decode('utf-8'), 'utf-8'
        except UnicodeDecodeError:
            text, encoding = raw.decode('latin-1'), 'latin-1'
        self.receipts[relative] = {'relative_path':relative, 'sha256':sha(raw),
                                   'bytes':len(raw), 'decoding':encoding}
        return text

    def verify_unchanged(self):
        for relative, receipt in self.receipts.items():
            path = self.checked(self.root / relative)
            if sha(path.read_bytes()) != receipt['sha256']:
                raise SourceContextError('source changed after extraction: '+relative)

    def find_main(self) -> Path:
        ranked = []
        for path in sorted(self.root.iterdir()):
            if path.is_file() and path.suffix.lower() in {'.tex', '.ltx'}:
                text = self.read(path)
                score = (10*('\\begin{document}' in text)
                         +5*('\\documentclass' in text)
                         +min(5,text.count('\\begin{proof}')))
                ranked.append((score,path))
        if not ranked:
            raise SourceContextError('no main TeX candidate')
        best_score = max(score for score,_ in ranked)
        best = [path for score,path in ranked if score==best_score]
        if len(best)>1:
            self.issues.append({'kind':'ambiguous_main_file',
                                'candidates':[p.name for p in best]})
        return best[0]

    def resolve_include(self, name: str, parent: Path) -> Path:
        # Reject path escapes before applying the archive's flattened-name fallback.
        if not name or '\\' in name or re.search(r'[\x00-\x1f{}$#]', name):
            raise SourceContextError('unsupported include name')
        direct = self.checked(parent / name)
        candidates = [direct, direct.with_name(direct.name+'.tex')]
        for relative in (name, (parent / name).relative_to(self.root).as_posix()):
            flat = relative.removeprefix('./').replace('/', '__')
            candidates.extend([self.checked(self.root/flat),
                               self.checked(self.root/(flat+'.tex'))])
        present = sorted({p for p in candidates if p.is_file()})
        if not present:
            raise SourceContextError('missing include: '+name)
        if len(present)>1:
            raise SourceContextError('ambiguous include: '+name)
        return present[0]

    def expand_file(self, path: Path, active=()) -> str:
        path = self.checked(path)
        relative = path.relative_to(self.root).as_posix()
        if relative in active:
            raise SourceContextError('cyclic include: '+relative)
        if len(active)>self.max_depth:
            raise SourceContextError('include depth budget exceeded')
        text = U.strip_comments(self.read(path))
        pattern = re.compile(r'\\(input|include|subfile)\s*\{([^}]+)\}')

        def replace(match):
            try:
                target = self.resolve_include(match[2].strip(), path.parent)
                return '\n'+self.expand_file(target,active+(relative,))+'\n'
            except (SourceContextError,OSError) as exc:
                self.issues.append({'kind':'unresolved_include','file':relative,
                                    'directive':match[0],'reason':str(exc)})
                return match[0]  # Preserve the missing dependency in review context.

        expanded = pattern.sub(replace,text)
        if len(expanded.encode())>self.max_bytes:
            raise SourceContextError('expanded source byte budget exceeded')
        if re.search(r'\\(?:input|include|subfile)\b(?!\s*\{)',expanded):
            self.issues.append({'kind':'unsupported_include_syntax','file':relative})
        # Read local styles/classes as evidence, without pretending to execute TeX.
        for match in re.finditer(r'\\(?:usepackage|documentclass)(?:\[[^\]]*\])?\{([^}]+)\}',text):
            extension = '.cls' if match[0].startswith('\\documentclass') else '.sty'
            for name in match[1].split(','):
                candidate = self.checked(self.root/(name.strip()+extension))
                if candidate.is_file():
                    self.read(candidate)
                    self.issues.append({'kind':'local_style_not_expanded',
                                        'file':candidate.relative_to(self.root).as_posix()})
        return expanded


def parse_pairs(body: str, full_text: str, paper_id: str, metadata: dict):
    envmap = U.theorem_env_map(full_text)
    statements = U.find_envs(body,list(envmap))
    proofs = U.find_envs(body,['proof'])
    label_map = {}
    for statement in statements:
        for label in U.LABEL_RE.findall(statement[4]):
            label_map.setdefault(label,[]).append(statement)
    rows=[]
    for start,end,_,heading,inner in proofs:
        targets=[]
        labels=re.findall(r'\\(?:ref|cref|Cref|autoref)\{([^}]*)\}',heading)
        for label in labels:
            targets.extend(label_map.get(label,[]))
        targets=list({t[0]:t for t in targets}.values())
        pairing='explicit_label'
        if len(targets)>1:
            continue  # Several theorem references do not identify one whole proof.
        if not targets:
            if labels or re.search(r'[Pp]roof of',heading):
                continue
            previous=[t for t in statements if t[1]<=start]
            if not previous:
                continue
            target=previous[-1]
            if start-target[1]>2500 or any(target[1]<q[0]<start for q in proofs):
                continue
            pairing='nearest_preceding_heuristic'
        else:
            target=targets[0]
        local={}
        for number,label in enumerate(U.LABEL_RE.findall(target[4])+U.LABEL_RE.findall(inner),1):
            local.setdefault(label,'eq %d'%number)
        external=[0]
        statement_text=U.clean_text(target[4],local,external)
        proof_text=U.clean_text(inner,local,external)
        steps=U.split_steps(proof_text)
        if not steps:
            continue
        row={'schema':'source-context-proof-candidate/v1','paper':paper_id,
             'title':metadata.get('title',''),'published':metadata.get('published','')[:10],
             'primary_category':metadata.get('primary_category',''),
             'domain_group':metadata.get('domain_group',''),
             'kind':envmap.get(target[2],'theorem'),'env':target[2],
             'stmt_opt':target[3], 'proof_opt':re.sub(r'\s+',' ',heading)[:200],
             'proof_heading':heading,'partial_heading':U.is_partial_heading(heading),
             'labels':U.LABEL_RE.findall(target[4]),'statement':statement_text,
             'steps':steps,'n_steps':len(steps),'proof_chars':sum(map(len,steps)),
             'stmt_chars':len(statement_text),'external_refs':external[0],
             'math_steps':sum(map(U.has_math,steps)),
             'statement_span_characters':[target[0],target[1]],
             'proof_span_characters':[start,end],'raw_statement':target[4],
             'raw_proof':inner,'pairing_method':pairing,
             'semantic_acceptance':'UNREVIEWED','source_completeness':'UNREVIEWED',
             'license_status':'UNREVIEWED',
             'source_proof_identity':digest([paper_id,re.sub(r'\s+',' ',target[4]).strip(),re.sub(r'\s+',' ',inner).strip()]),
             'source_occurrence_identity':digest([paper_id,target[0],start,target[4],inner])}
        passed,reason=U.accept(row)
        # Preserve the old non-textual dependency exclusion, but report the row.
        if re.search(r'\\begin\{(?:figure|tikzpicture|table|tabular|itemize|enumerate)\}|\\includegraphics|\\input\{',proof_text):
            passed,reason=False,'nontext_or_unexpanded_dependency'
        row.update(candidate_filter_pass=passed,candidate_filter_reject_reason=reason)
        rows.append(row)
    return rows


def extract_paper(tex_root: Path, paper_id: str, download: dict, metadata=None, archive=None):
    if not re.fullmatch(r'(?:\d{4}\.\d{4,5}|[a-z-]+/\d{7})',paper_id):
        raise ValueError('unsupported paper identity')
    if (download.get('base_id')!=paper_id or
        not re.fullmatch(re.escape(paper_id)+r'v\d+',download.get('arxiv_id','')) or
        download.get('kind') not in {'tar','single_tex'} or download.get('n_tex',0)<=0 or
        not re.fullmatch(r'[0-9a-f]{64}',download.get('sha256',''))):
        raise ValueError('missing exact-version completed download receipt')
    reader=SourceReader(tex_root/paper_id.replace('/','_'))
    main=reader.find_main()
    full=reader.expand_file(main)
    macros=U.collect_macros(full)
    body_start=full.find('\\begin{document}')
    body=full[body_start:] if body_start>=0 else full
    n_expanded=0
    for _ in range(8):
        body,count=U.expand_macros(body,macros,rounds=1)
        n_expanded+=count
        if len(body.encode())>reader.max_bytes:
            raise SourceContextError('macro-expanded source byte budget exceeded')
        if not count:
            break
    metadata={**download,**(metadata or {})}
    rows=parse_pairs(body,full,paper_id,metadata)
    reader.verify_unchanged()
    origin=(verify_archive_origin(Path(archive),download,list(reader.receipts.values()))
            if archive is not None else {'status':'UNVALIDATED_DOWNLOAD_RECEIPT_ONLY'})
    receipt={'schema':'paper-source-context/v1','paper_id':paper_id,
             'source_version':download['arxiv_id'],'download_receipt':download,
             'download_receipt_sha256':digest(download),
             'source_version_status':'REPORTED_BY_DOWNLOAD_RECEIPT; server version not independently verified',
             'archive_origin_validation':origin,
             'source_directory':str(reader.root),'main_file':main.name,
             'files':list(reader.receipts.values()),'issues':reader.issues,
             'expanded_body_sha256':sha(body.encode()),'macro_substitutions':n_expanded,
             'upstream_sha256':UPSTREAM_SHA256,
             'mechanical_dependency_scan':'UNRESOLVED' if reader.issues else 'NO_DETECTED_INCLUDE_FAILURE',
             'semantic_source_completeness':'UNREVIEWED; absence of a parser warning is not a complete proof context',
             'license_status':'UNREVIEWED','created_utc':datetime.now(timezone.utc).isoformat()}
    for row in rows:
        row.update(source_version=download['arxiv_id'],source_context_sha256=digest(receipt),
                   expanded_body_sha256=receipt['expanded_body_sha256'])
        if reader.issues:
            row.update(candidate_filter_pass=False,candidate_filter_reject_reason='unresolved_source_context')
    return rows,receipt,body


def write_extraction(directory: Path, rows, receipt, body):
    directory.mkdir(parents=True,exist_ok=False)
    (directory/'NO_INGEST.md').write_text('Private review candidates and complete source context. Do not add these records to solver notes or indexes. No semantic, license, or heldout acceptance is implied.\n',encoding='utf-8')
    (directory/'expanded_body.tex').write_bytes(body.encode())
    (directory/'source_context.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    (directory/'proof_candidates.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False,sort_keys=True)+'\n' for r in rows),encoding='utf-8')
    summary={'candidate_occurrences':len(rows),
             'distinct_source_proof_texts':len({r['source_proof_identity'] for r in rows}),
             'structural_candidate_filter_pass_occurrences':sum(r['candidate_filter_pass'] for r in rows),
             'structural_candidate_filter_pass_distinct_proofs':len({r['source_proof_identity'] for r in rows if r['candidate_filter_pass']}),
             'reject_reasons':dict(Counter(r['candidate_filter_reject_reason'] for r in rows if not r['candidate_filter_pass'])),
             'semantic_accepted':0,'issues':len(receipt['issues']),
             'files':{p.name:sha(p.read_bytes()) for p in sorted(directory.iterdir()) if p.is_file()}}
    (directory/'MANIFEST.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')
    return summary


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--tex-root',type=Path,required=True)
    parser.add_argument('--download-log',type=Path,required=True)
    parser.add_argument('--source-archive',type=Path,required=True)
    parser.add_argument('--paper-id',required=True)
    parser.add_argument('--private-out-dir',type=Path,required=True)
    args=parser.parse_args()
    downloads=[json.loads(line) for line in args.download_log.read_text(encoding='utf-8').splitlines() if line.strip()]
    completed=[r for r in downloads if r.get('base_id')==args.paper_id and r.get('kind') in {'tar','single_tex'}]
    if len(completed)!=1:
        raise ValueError('paper needs one unambiguous completed download receipt')
    rows,receipt,body=extract_paper(args.tex_root,args.paper_id,completed[0],archive=args.source_archive)
    print(json.dumps(write_extraction(args.private_out_dir,rows,receipt,body),indent=2))


if __name__=='__main__':
    main()
