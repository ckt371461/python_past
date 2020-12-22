# git的用法

```sh
git add -A
git commit -m "告訴自己(別人)的信息"
git push origin master
```

```py
def OK(q1, q2):
    if q1['x']==q2['x']: return False
    if q1['y']==q2['y']: return False
    if q1['x']-q1['y'] == q2['x']-q2['y']: return False
    if q1['x']+q1['y'] == q2['x']+q2['y']: return False
    return True

def allOk(q, qt):
    for qi in q:
        if not OK(qi,qt):
            return False
    return True

import sys
# m=[[0]*8]*8
q=[]

def _8queen(q):
    if len(q)==8:
        print('q=', q)
        sys.exit(0)
    for y in range(8):
        for x in range(8):
            qnew = {'x':x,'y':y}
            # print('qnew=', qnew)
            if allOk(q, qnew):
                q.append(qnew)
                _8queen(q)
                q.pop()   

print(_8queen(q))
```

