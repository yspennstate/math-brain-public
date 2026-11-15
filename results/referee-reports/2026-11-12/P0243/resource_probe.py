import json, resource
out={}
for name in ['RLIMIT_DATA','RLIMIT_CPU','RLIMIT_RSS']:
    kind=getattr(resource,name)
    before=resource.getrlimit(kind)
    out[name]={'before':before}
    try:
        target=(768*1024*1024,768*1024*1024) if name=='RLIMIT_DATA' else before
        resource.setrlimit(kind,target)
        out[name]['after']=resource.getrlimit(kind)
    except (OSError,ValueError) as exc:
        out[name]['error']=str(exc)
print(json.dumps(out,indent=2))
