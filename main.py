Y='/game'
X=enumerate
K=None
N=range
B=chr
D=abs
import os,json as C,urllib.request as O
MA=100000
P=os.environ.get('MAKEFUN_ENV_URL')
Z=[0,82,337,365,477,1025,0]
Q=[-33,-31,-18,-14,14,18,31,33]
R=[-17,-16,-15,-1,1,15,16,17]
G=[-17,-15,15,17]
E=[-16,-1,1,16]
a=[(A,2)for A in Q]+[(A,6)for A in R]
b=[G,E,G+E]
S={4:3,0:2,7:1,116:12,112:8,119:4}
M=[(1,4,1,7),(2,4,-1,0),(4,116,1,119),(8,116,-1,112)]
class c:
	def __init__(A):A.b=[0]*128;A.s=1;A.c=0;A.e=-1
def d(f):
	B=c();A=f.split();E=A[0].split('/')
	for(F,G)in X(E):
		D=0
		for C in G:
			if C.isdigit():D+=int(C)
			else:B.b[(7-F)*16+D]=('PNBRQK'.index(C.upper())+1)*(1 if C.isupper()else-1);D+=1
	B.s=2*(A[1]=='w')-1;B.c=sum(1<<B for(B,C)in X('KQkq')if C in A[2]);B.e=ord(A[3][0])-97+(int(A[3][1])-1)*16 if A[3]!='-'else-1;return B
def L(p,q,y):
	D=p.b;F=-16*y
	for B in(F-1,F+1):
		A=q+B
		if not A&136 and D[A]==y:return 1
	for(B,C)in a:
		A=q+B
		if not A&136 and D[A]==y*C:return 1
	for B in G+E:
		A=q+B
		while not A&136:
			C=D[A]
			if C:
				if C==y*5 or C==y*(3+(B in E)):return 1
				break
			A+=B
	return 0
def H(p,y):B=p.b;return next((A for A in N(128)if not A&136 and B[A]==y*6),-1)
def I(p):
	E=p.b;H=p.s;F=[]
	for A in N(128):
		O=E[A]
		if A&136 or not O or(O>0)!=(H>0):continue
		J=D(O)
		if J==1:
			K=16*H;C=A+K
			if not C&136 and not E[C]:
				P=C>>4;F+=[A|C<<7|B<<14 for B in(5,4,3,2)]if P in(0,7)else[A|C<<7]
				if A>>4==1+5*(H<0)and not E[A+2*K]:F.append(A|A+2*K<<7)
			for C in(K-1,K+1):
				B=A+C
				if B&136:continue
				G=E[B]
				if G and(G>0)!=(H>0):P=B>>4;F+=[A|B<<7|C<<14 for C in(5,4,3,2)]if P in(0,7)else[A|B<<7]
		elif J==2 or J==6:
			for C in[Q,R][J==6]:
				B=A+C
				if B&136:continue
				G=E[B]
				if not G or(G>0)!=(H>0):F.append(A|B<<7)
			if J==6:
				for I in M:
					if p.c&I[0]and A==I[1]:
						S=A+2*I[2]
						if not E[A+I[2]]and not E[S]and(I[2]>0 or not E[A+3*I[2]])and all(not L(p,A+B*I[2],-H)for B in(0,1,2)):F.append(A|S<<7)
		else:
			for C in b[J-3]:
				B=A+C
				while not B&136:
					G=E[B]
					if not G:F.append(A|B<<7)
					else:
						if(G>0)!=(H>0):F.append(A|B<<7)
						break
					B+=C
	return F
def J(p,m):
	B=p.b;E=m&127;C=m>>7&127;A=m>>14&7;G=B[E];J=B[C];K=-1;I=m,J,p.c,p.e,K;B[E]=0;B[C]=(A or D(G))*p.s
	if D(G)==6 and D(C-E)==2:
		for A in M:
			if C==A[1]+2*A[2]:B[A[1]+A[2]]=B[A[3]];B[A[3]]=0
	p.c&=~(S.get(E,0)|S.get(C,0));p.e=(E+C)//2 if D(G)==1 and D(C-E)==32 else-1;p.s=-p.s
	if L(p,H(p,-p.s),p.s):F(p,I);return
	return I
def F(p,u):
	E,H,I,J,K=u;B=p.b;F=E&127;C=E>>7&127;A=E>>14&7;G=B[C];p.s=-p.s;B[F]=(1 if A else D(G))*p.s;B[C]=H if K==-1 else 0
	if D(G)==6 and D(C-F)==2:
		for A in M:
			if C==A[1]+2*A[2]:B[A[3]]=B[A[1]+A[2]];B[A[1]+A[2]]=0
	p.c,p.e=I,J
def T(p):
	G=p.b;C=0
	for A in N(128):
		if A&136:continue
		B=G[A]
		if not B:continue
		E=D(B);F=56-(A>>4)*8+(A&7);F^=56*(B<0);C+=(Z[E]+((F>>3)*8 if E==1 else 0))*(2*(B>0)-1)
	return C if p.s>0 else-C
A=[0,0]
def U(p,a,b,y):
	A[0]+=1
	if A[0]>A[1]:return T(p)
	D=L(p,H(p,p.s),-p.s);B=-MA if D else T(p)
	if not D:
		if B>=b:return b
		if B>a:a=B
	for G in I(p,not D):
		E=J(p,G)
		if E is K:continue
		C=-U(p,-b,-a,y+1);F(p,E)
		if C>=b:return b
		if C>a:a=C
		if C>B:B=C
	return a if not D else B if B>-MA else-MA+y
def V(p,d,a,b,y):
	A[0]+=1
	if A[0]>A[1]or d<=0:return U(p,a,b,y)
	G=L(p,H(p,p.s),-p.s);M=I(p);B=-100000;C=0
	for N in M:
		D=J(p,N)
		if D is K:continue
		C+=1;E=-V(p,d-1,-b,-a,y+1);F(p,D);B=max(B,E);a=max(a,E)
		if a>=b:break
	if not C:return-MA+y if G else 0
	return B
def e(p,n):
	A[0]=0;A[1]=n;D=I(p);B=D[0];E=1
	while A[0]<n:
		C=-100000;G=B
		for H in D:
			L=J(p,H)
			if L is K:continue
			M=-V(p,E-1,-MA,-C,1);F(p,L)
			if M>C:C,G=M,H
		B=G;E+=1
	return B
def f(m):A=m&127;C=m>>7&127;D=m>>14&7;return B(97+A%8)+B(49+A//16)+B(97+C%8)+B(49+C//16)+('nbrq'[D-2]if D else'')
def W(q,w):
	try:return C.load(O.urlopen(P+q,C.dumps(w).encode()))
	except Exception:return C.load(O.urlopen(P+Y,b'{}'))
def g():
	C='game';B='status'
	while(A:=W(Y,{}))[B]!='done':
		while A[B]=='your_move':A=W('/move',{C:A[C],'move':f(e(d(A['fen']),99999))})
g()
