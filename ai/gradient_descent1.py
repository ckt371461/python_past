def kadd(a,i,c):#  a[i] = a[i]+c
    r = a.copy()
    r[i] += c
    return r

def length(p):#向量的長度,p是[x,y,z...]的值
    sum=0
    for x in p:
        sum+=x**2
    return sum**(0.5)

def vmul(v,c):#v是p偏微分後的結果(=g)
    for x in range(len(v)):
        v[x] = v[x]*c
    return v

def vadd(p,v):n
    for x in range(len(p)):
        p[x] += v[x]
    return p

def grad(f, p, h=0.00001): #偏微分,f是函數,p是[x,y,z...]的值
    end = p.copy()
    for i in range(len(p)):
        end[i] = (f(kadd(p,i,h))- f(p))/h
    return end

def gradient_descent(f,p0):#梯度下降,f是函數,p0是起點
    p = p0.copy()
    while True:
        g = grad(f,p)
        if (length(g) < 0.001):
            break
        p = vadd(p,vmul(g,-0.001))#下降,故乘負值
        print('p=', p, 'f(p)=', f(p))
    return p

def f(p):
    x,y,z=p
    return (x-1)*(x-1)+2*y**4+z*z-2*y

print(gradient_descent(f, [1.,2.,3.]))

 