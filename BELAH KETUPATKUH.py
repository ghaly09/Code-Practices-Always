'''
3
 _ (1,0,1) 2
_ _(0,1,0) 1
 _ (1,0,1) 2
 
5
  _  (2,0,2) 4
 _ _ (1,1,1) 3
_   _(0,3,0) 3
 _ _ (1,1,1) 3
  _  (2,0,2) 4

7
   _   (3,0,3) 6
  _ _  (2,1,2) 5
 _   _ (1,3,1) 5
_     _(0,5,0) 5
 _   _ (1,3,1) 5
  _ _  (2,1,2) 5
   _   (3,0,3) 6

9
    _    (4,0,4) 8
   _ _   (3,1,3) 7
  _   _  (2,3,2) 7
 _     _ (1,5,1) 7
_       _(0,7,0) 7
 _     _ (1,5,1) 7
  _   _  (2,3,2) 7
   _ _   (3,1,3) 7
    _    (4,0,4) 8

1
_(0,0,0) 0
'''
jum=int(input())
print(" "*int(jum/2)+"_"+" "*int(jum/2))
for i in range(int(jum/2)-1,-1,-1):
	print(" "*i+"_"+" "*((jum-2)-i*2)+"_"+" "*i)
for i in range(1,int(jum/2)):
	#print(i)
	print(" "*i+"_"+" "*((jum-2)-i*2)+"_"+" "*i)
if jum!=1: print(" "*int(jum/2)+"_"+" "*int(jum/2))
