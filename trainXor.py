

def trainHidden(x,y,r,w1,w2,w0):
    for i in range(100):
        lr=0.1
        for j in range(4):
            p = x[j]*w1 + y[j]*w2 + w0
            if p>=0:
                r1 = 1
            else:
                r1 = 0
            
            error = r[j] - r1
            w1 += lr*error*x[j]
            w2 += lr*error*y[j]
            w0 += lr*error
    return w1,w2,w0

        
def trainOutput(p,q,r,s,t,w1,w2,w3,w4,w0):
    for i in range(100):
        lr=0.5
        for j in range(16):
            p1 = p[j]*w1 + q[j]*w2 + r[j]*w3 + s[j]*w4 + w0  
            if p1>=0:
                r1 = 1
            else:
                r1 = 0
            
            error = t[j] - r1
            w1 += lr*error*p[j]
            w2 += lr*error*q[j]
            w3 += lr*error*r[j]
            w4 += lr*error*s[j]
            w0 += lr*error
            
    return w1,w2,w3,w4,w0



x = [1,0,1,0,]
y = [1,1,0,0,]
r1 = [1,0,0,0,]
r2 = [0,1,0,0,]
r3 = [0,0,1,0,]
r4 = [0,0,0,1,]
p = [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]
q = [1,1,1,1,0,0,0,0,1,1,1,1,0,0,0,0]
r = [1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0]
s = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]
t = [0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,0]

w5_1=0
w5_2=0
w5_3=0
w5_4=0
w5_0=0

w1_1=0
w1_2=0
w1_0=0
w2_1=0
w2_2=0
w2_0=0
w3_1=0
w3_2=0
w3_0=0
w4_1=0
w4_2=0
w4_0=0

w1_1,w1_2,w1_0 = trainHidden(x,y,r1,w1_1,w1_2,w1_0)
w2_1,w2_2,w2_0 = trainHidden(x,y,r2,w2_1,w2_2,w2_0)
w3_1,w3_2,w3_0 = trainHidden(x,y,r3,w3_1,w3_2,w3_0)
w4_1,w4_2,w4_0 = trainHidden(x,y,r4,w4_1,w4_2,w4_0)

w5_1,w5_2,w5_3,w5_4,w5_0 = trainOutput(p, q, r, s, t, w5_1,w5_2,w5_3,w5_4,w5_0)

for i in range(4):
    h1 = x[i]*w1_1 + y[i]*w1_2 + w1_0
    h1 = 1 if h1 >=0 else 0
    
    h2 = x[i]*w2_1 + y[i]*w2_2 + w2_0
    h2 = 1 if h2 >=0 else 0
    
    h3 = x[i]*w3_1 + y[i]*w3_2 + w3_0
    h3 = 1 if h3 >=0 else 0
    
    h4 = x[i]*w4_1 + y[i]*w4_2 + w4_0
    h4 = 1 if h4 >=0 else 0
    
    p1 = h1*w5_1 + h2*w5_2 + h3*w5_3 + h4*w5_4 + w5_0
    p1 = 1 if p1 >=0 else 0
    
    print(f'{x[i]} xor {y[i]} = {p1}')

