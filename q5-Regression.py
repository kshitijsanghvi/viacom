import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data_frame = pd.read_csv("""C:\\Users\\kshit\\Downloads\\q5q17.csv""")
n = len(data_frame)
d = data_frame["Sum of Installations"].tolist()
d_s = []
sm = 5
for i in range(n):
    d_s.append(np.median(d[max(i-sm,0):min(i+sm,n)]))
d_s2 = []
sm = 10
for i in range(n):
    d_s2.append(np.median(d[max(i-sm,0):min(i+sm,n)]))
x_array = [i for i in range(n)]
z2 = np.polyfit(x_array,d,2)
z3 = np.polyfit(x_array,d,3)
z1 = np.polyfit(x_array,d,1)
z4 = np.polyfit(x_array,d,4)
z9 = np.polyfit(x_array,d,5)
pred2 = []
pred3 = []
pred1 = []
pred4 = []
pred9 = []
for i in x_array:
    pred1.append(z1[0]*i + z1[1])
    
for i in x_array:
    pred4.append(z4[0]*i*i*i*i + z4[1]*i*i*i + z4[2]*i*i + z4[3]*i + z4[4])

for i in x_array:
    pred2.append(z2[0]*i*i + z2[1]*i + z2[2])
for i in x_array:
    pred3.append(z3[0]*i*i*i + z3[1]*i*i + z3[2]*i + z3[3])
n = 5
for i in x_array:
    ans = 0
    for ii,j in enumerate(z9):
        ans += i**(5-ii)*j
    pred9.append(ans)
plt.title("Installations - Mexico, Paid")
plt.xlabel("Day")
plt.ylabel("Installations")
plt.plot(d,label='True Distribution')
plt.plot(d_s, label = "Median denoising - window = 10")
plt.plot(d_s2, label = "Median denoising - window = 20")
plt.legend()
plt.savefig('denoise.png', dpi=300)
plt.show()
plt.title("Installations - Mexico, Paid")
plt.xlabel("Day")
plt.ylabel("Installations")
plt.plot(d,label='True Distribution')
#plt.plot(d_s, label = "Median denoising - window = 10")
#plt.plot(d_s2, label = "Median denoising - window = 20")
plt.plot(pred2, label = "Prediction Degree 2")
plt.plot(pred3, label = "Prediction Degree 3")
plt.plot(pred4, label = "Prediction Degree 4")
plt.plot(pred1, label = "Prediction Degree 1")
plt.plot(pred9, label = "Prediction Degree 5")
plt.legend();
plt.savefig('global.png', dpi = 300)
plt.show()
for i in range(93,100):
    print(round(z3[0]*i*i*i + z3[1]*i*i + z3[2]*i+z3[3]))
    #print(round(z2[0]*i*i + z2[1]*i + z2[2]))
#    print(round(z4[0]*i*i*i*i + z4[1]*i*i*i + z4[2]*i*i + z4[3]*i + z4[4] ))