// Controller function for execution through functions.exec, whose tools/store/load globals are supplied by Work Mode.
// Writes only this campaign's unique prefix and uses non-forced fast-forward updates.
async function publishX(message) {
 const repo="yspennstate/math-open-problems",base="/workspace/scratch/9028a8e284b1/crossfield-lyons-20260915",prefix="proofnet24/lyons-entropy/crossfield-2026-09-15/";
 const mr=await tools.exec_command({cmd:"python - <<'PY'\nfrom pathlib import Path\nimport hashlib,json\np=Path('/workspace/scratch/9028a8e284b1/crossfield-lyons-20260915')\na=[]\nfor f in sorted(p.rglob('*')):\n if not f.is_file() or '__pycache__' in f.parts or f.suffix=='.pyc':continue\n b=f.read_bytes();a.append({'name':f.relative_to(p).as_posix(),'sha':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\\0'+b).hexdigest(),'bytes':len(b)})\nprint(json.dumps(a))\nPY",max_output_tokens:15000});
 if(mr.exit_code!==0)throw new Error(mr.output);
 const hashes=load("x_published_hashes")||{},rows=JSON.parse(mr.output).filter(r=>hashes[r.name]!==r.sha);
 const gathered=await Promise.allSettled(rows.map(async row=>{
  let s="",total=null,sha=null,encoding=null;
  do{
   const r=await tools.exec_command({cmd:"python /workspace/scratch/9028a8e284b1/read_for_github.py '"+base+"/"+row.name+"' "+s.length,max_output_tokens:12500});
   if(r.exit_code!==0)throw new Error(r.output);const p=JSON.parse(r.output);
   if(sha&&sha!==p.sha)throw new Error("File changed during read: "+row.name);
   sha=p.sha;encoding=p.encoding;total=p.total;s+=p.content;
  }while(s.length<total);
  return {name:row.name,content:s,sha,encoding};
 }));
 const files=[];
 for(let i=0;i<gathered.length;i++){
  if(gathered[i].status==="fulfilled")files.push(gathered[i].value);
  else text({skipped:rows[i].name,reason:String(gathered[i].reason)});
 }
 if(!files.length){text({changed_files:0});return;}
 const entries=[];
 for(const f of files){
  const r=await tools.mcp__codex_apps__github_create_blob({repository_full_name:repo,content:f.content,encoding:f.encoding});
  if(r.isError||r.structuredContent?.sha!==f.sha)throw new Error("Blob mismatch "+f.name);
  entries.push({path:prefix+f.name,mode:"100644",type:"blob",sha:f.sha});
 }
 for(let attempt=0;attempt<5;attempt++){
  const hr=await tools.mcp__codex_apps__github_fetch({url:"https://api.github.com/repos/"+repo+"/branches/master"});
  if(hr.isError)throw new Error(JSON.stringify(hr));const head=JSON.parse(hr.structuredContent.content);
  const tr=await tools.mcp__codex_apps__github_create_tree({repository_full_name:repo,base_tree_sha:head.commit.commit.tree.sha,tree_elements:entries});
  if(tr.isError)throw new Error(JSON.stringify(tr));
  const cr=await tools.mcp__codex_apps__github_create_commit({repository_full_name:repo,parent_sha:head.commit.sha,tree_sha:tr.structuredContent.sha,message});
  if(cr.isError)throw new Error(JSON.stringify(cr));
  const ur=await tools.mcp__codex_apps__github_update_ref({repository_full_name:repo,branch_name:"master",sha:cr.structuredContent.sha,force:false});
  if(!ur.isError&&ur.structuredContent?.success!==false){
   store("x_last_commit",cr.structuredContent.sha);
   for(const f of files)hashes[f.name]=f.sha;store("x_published_hashes",hashes);
   const history=load("x_commits")||[];history.push({sha:cr.structuredContent.sha,message,files:files.map(f=>f.name)});store("x_commits",history);
   text({published:cr.structuredContent.sha,files:files.map(f=>f.name)});return;
  }
  text({retry:attempt+1,reason:ur});
 }
 throw new Error("Fast-forward publish did not succeed");
}

