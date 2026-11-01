#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define N 9
#define MAXE 36
#define MAXP 630
#define MOD 1000000007LL

typedef long long i64;
typedef unsigned long long u64;
typedef __int128 i128;

static uint32_t tau_[1<<N];
static uint32_t te_[MAXE][1<<N];
static uint32_t tp_[MAXP][1<<N];
static u64 forest_[1<<N];
static int eu[MAXE], ev[MAXE], pair_index[MAXE][MAXE];
static i64 invmat[8][8];
static int min_edges=0,max_edges=36;

static i64 modnorm(i64 x){x%=MOD;if(x<0)x+=MOD;return x;}
static i64 invmod(i64 a){i64 b=MOD,u=1,v=0;while(b){i64 t=a/b,na=a-t*b;a=b;b=na;i64 nu=u-t*v;u=v;v=nu;}return modnorm(u);}
static void print_i128(i128 x){if(x<0){putchar('-');x=-x;}char s[64];int n=0;do{s[n++]='0'+(int)(x%10);x/=10;}while(x);while(n--)putchar(s[n]);}

static uint32_t tree_data(unsigned mask,uint32_t adj[N],int m){
 int verts[N],idx[N],k=0;for(int i=0;i<N;i++)idx[i]=-1;for(int i=0;i<N;i++)if(mask>>i&1u)verts[k++]=i;
 if(k==0)return 0;if(k==1)return 1;int root=verts[k-1],d=k-1;
 i64 a[8][8],b[8][8];memset(a,0,sizeof(a));memset(b,0,sizeof(b));for(int i=0;i<d;i++)idx[verts[i]]=i;
 for(int ii=0;ii<d;ii++){int u=verts[ii],deg=0;for(int jj=0;jj<k;jj++)if(jj!=ii){int v=verts[jj];if(adj[u]>>v&1u)deg++;}a[ii][ii]=deg;for(int jj=0;jj<d;jj++)if(ii!=jj){int v=verts[jj];if(adj[u]>>v&1u)a[ii][jj]=MOD-1;}b[ii][ii]=1;}
 i64 det=1;int sign=1;for(int col=0;col<d;col++){int pr=col;while(pr<d&&a[pr][col]==0)pr++;if(pr==d)return 0;if(pr!=col){for(int j=0;j<d;j++){i64 t=a[pr][j];a[pr][j]=a[col][j];a[col][j]=t;t=b[pr][j];b[pr][j]=b[col][j];b[col][j]=t;}sign=-sign;}i64 piv=a[col][col];det=det*piv%MOD;i64 ip=invmod(piv);for(int j=0;j<d;j++){a[col][j]=a[col][j]*ip%MOD;b[col][j]=b[col][j]*ip%MOD;}for(int r=0;r<d;r++)if(r!=col){i64 f=a[r][col];if(!f)continue;for(int j=0;j<d;j++){a[r][j]=modnorm(a[r][j]-f*a[col][j]);b[r][j]=modnorm(b[r][j]-f*b[col][j]);}}}
 if(sign<0)det=modnorm(-det);if(det<=0||det>4782969){fprintf(stderr,"bad tau %lld\n",det);exit(3);}uint32_t tau=(uint32_t)det;
 for(int i=0;i<d;i++)for(int j=0;j<d;j++)invmat[i][j]=b[i][j];
 i64 raw[MAXE];int inside[MAXE],ni=0;memset(raw,0,sizeof(raw));
 for(int e=0;e<m;e++)if(((mask>>eu[e])&1u)&&((mask>>ev[e])&1u)){inside[ni++]=e;int u=eu[e],v=ev[e];i64 val=0;if(u!=root)val+=invmat[idx[u]][idx[u]];if(v!=root)val+=invmat[idx[v]][idx[v]];if(u!=root&&v!=root){val-=invmat[idx[u]][idx[v]];val-=invmat[idx[v]][idx[u]];}raw[e]=modnorm(val);i64 q=det*raw[e]%MOD;if(q<0||q>(i64)tau){fprintf(stderr,"bad te\n");exit(4);}te_[e][mask]=(uint32_t)q;}
 for(int aa=0;aa<ni;aa++)for(int bb=aa+1;bb<ni;bb++){int e=inside[aa],f=inside[bb],pi=pair_index[e][f];int us[2]={eu[e],ev[e]},vs[2]={eu[f],ev[f]};int cs[2]={1,-1},ds[2]={1,-1};i64 cross=0;for(int xx=0;xx<2;xx++)if(us[xx]!=root)for(int yy=0;yy<2;yy++)if(vs[yy]!=root)cross+=(i64)cs[xx]*ds[yy]*invmat[idx[us[xx]]][idx[vs[yy]]];cross=modnorm(cross);i64 val=modnorm(raw[e]*raw[f]%MOD-cross*cross%MOD);i64 q2=det*val%MOD;if(q2<0||q2>(i64)tau){fprintf(stderr,"bad tp\n");exit(5);}tp_[pi][mask]=(uint32_t)q2;}
 return tau;
}

int main(int argc,char**argv){
 if(argc<2){fprintf(stderr,"usage: %s graph9.g6 [min_edges [max_edges]]\n",argv[0]);return 2;}if(argc>2)min_edges=atoi(argv[2]);if(argc>3)max_edges=atoi(argv[3]);
 FILE*fp=fopen(argv[1],"r");if(!fp){perror("fopen");return 2;}char line[256];long seen=0,graphs=0;u64 pairs=0,zero=0;long bym[37]={0};i128 minpos=-1,maxgap=0;char minline[32]="",maxline[32]="";int mine1=-1,mine2=-1,maxe1=-1,maxe2=-1;u64 maxF=0;char maxFline[32]="";clock_t t0=clock();
 while(fgets(line,sizeof(line),fp)){size_t len=strcspn(line,"\r\n");line[len]=0;if(!len)continue;seen++;if((unsigned char)line[0]!=63+N){fprintf(stderr,"bad n at line %ld\n",seen);return 6;}uint32_t adj[N]={0};int m=0,bitpos=0,bits[42],nb=0;for(size_t ci=1;ci<len;ci++){int x=(unsigned char)line[ci]-63;if(x<0||x>63)return 6;for(int b=5;b>=0;b--)bits[nb++]=(x>>b)&1;}if(nb<36)return 6;for(int j=1;j<N;j++)for(int i=0;i<j;i++){if(bits[bitpos]){adj[i]|=1u<<j;adj[j]|=1u<<i;eu[m]=i;ev[m]=j;m++;}bitpos++;}if(m<min_edges||m>max_edges)continue;graphs++;bym[m]++;
 int pc=0;for(int e=0;e<m;e++)for(int f=e+1;f<m;f++)pair_index[e][f]=pair_index[f][e]=pc++;
 memset(tau_,0,sizeof(tau_));memset(te_,0,sizeof(te_));memset(tp_,0,sizeof(tp_));for(unsigned mask=1;mask<(1u<<N);mask++)tau_[mask]=tree_data(mask,adj,m);
 forest_[0]=1;for(unsigned mask=1;mask<(1u<<N);mask++){unsigned lb=mask&-mask,rest=mask^lb;u64 sum=0;for(unsigned x=rest;;x=(x-1)&rest){unsigned T=x|lb;sum+=(u64)tau_[T]*forest_[mask^T];if(x==0)break;}forest_[mask]=sum;}
 unsigned full=(1u<<N)-1;u64 Z=forest_[full];if(Z>maxF){maxF=Z;strcpy(maxFline,line);}u64 ze[MAXE]={0};for(int e=0;e<m;e++){unsigned em=(1u<<eu[e])|(1u<<ev[e]);u64 s=0,other=full^em;for(unsigned x=other;;x=(x-1)&other){unsigned T=em|x;s+=(u64)te_[e][T]*forest_[full^T];if(x==0)break;}ze[e]=s;}
 for(int e=0;e<m;e++)for(int f=e+1;f<m;f++){pairs++;int pi=pair_index[e][f];unsigned em=(1u<<eu[e])|(1u<<ev[e]),fm=(1u<<eu[f])|(1u<<ev[f]),um=em|fm,o=full^um;u64 zef=0;for(unsigned x=o;;x=(x-1)&o){unsigned T=um|x;zef+=(u64)tp_[pi][T]*forest_[full^T];if(x==0)break;}if((em&fm)==0){for(unsigned x=o;;x=(x-1)&o){unsigned A=em|x,left=o^x;for(unsigned y=left;;y=(y-1)&left){unsigned B=fm|y,rem=left^y;zef+=(u64)te_[e][A]*te_[f][B]*forest_[rem];if(y==0)break;}if(x==0)break;}}
 i128 delta=(i128)ze[e]*ze[f]-(i128)Z*zef;if(delta<0){printf("COUNTEREXAMPLE seen=%ld tested=%ld g6=%s m=%d e=(%d,%d) f=(%d,%d) Z=%llu Ze=%llu Zf=%llu Zef=%llu delta=",seen,graphs,line,m,eu[e],ev[e],eu[f],ev[f],Z,ze[e],ze[f],zef);print_i128(delta);putchar('\n');return 1;}if(delta==0)zero++;else{if(minpos<0||delta<minpos){minpos=delta;strcpy(minline,line);mine1=e;mine2=f;}if(delta>maxgap){maxgap=delta;strcpy(maxline,line);maxe1=e;maxe2=f;}}}
 if(graphs%1000==0)fprintf(stderr,"progress seen=%ld tested=%ld pairs=%llu sec=%.2f\n",seen,graphs,pairs,(double)(clock()-t0)/CLOCKS_PER_SEC);
 }
 fclose(fp);printf("STATUS PASS\nsource_lines_seen=%ld\ngraphs_tested=%ld\nedge_range=%d..%d\nedge_pairs_tested=%llu\nzero_gaps=%llu\n",seen,graphs,min_edges,max_edges,pairs,zero);for(int m=0;m<=36;m++)if(bym[m])printf("graphs_m%d=%ld\n",m,bym[m]);printf("max_forest_count=%llu g6=%s\n",maxF,maxFline);if(minpos>=0){printf("min_positive_gap=");print_i128(minpos);printf(" g6=%s edge_indices=%d,%d\n",minline,mine1,mine2);}printf("max_gap=");print_i128(maxgap);printf(" g6=%s edge_indices=%d,%d\n",maxline,maxe1,maxe2);printf("elapsed_cpu_seconds=%.6f\n",(double)(clock()-t0)/CLOCKS_PER_SEC);return 0;
}
