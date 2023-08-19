import numpy as np
from matplotlib import pyplot as plt

def fun1(x):
    return 1*(x-100)**2+100
def fun2(x):
    return 1*(x-200)**2+100
def meanfunc(x):
    return (fun1(x)+fun2(x))/2
def numerical_lim(f,x):
    h=1e-4
    return (f(x+h)-f(x))/h
def tangent_line(f,x):
    #d就是调用numerical_diff求得在x点点导数
    d=numerical_lim(f,x)
    # 这里直接y=kx+b求截，简单粗暴，y就是截距
    y=f(x)-d*x
    #使用lambda匿名函数，t是形参，'：'后是要执行的函数表达式
    return lambda t:d*t+y
x=np.arange(-100,700.0,0.1)
po=-20
y=fun1(x)
plt.figure(figsize=(6 , 6 ))
plt.xlim(-105,405)
plt.ylim(-1000,30000)
plt.grid(False)
plt.rcParams['font.sans-serif'] = ['Arial']  # 如果要显示中文字体，则在此处设为：SimHei
plt.rcParams['axes.unicode_minus'] = False
parameters = {'axes.labelsize': 25, 'xtick.labelsize': 25, 'ytick.labelsize': 25, 'legend.fontsize': 25,
                'legend.title_fontsize': 25}
plt.tick_params(labelsize=25)
plt.rcParams.update(parameters)
ax = plt.gca()
ax.spines.right.set_color('none')
ax.spines['top'].set_visible(False)
plt.ylabel("loss",fontsize=25,horizontalalignment='right',y=1.0)
plt.xlabel("$\\theta$",fontsize=25,horizontalalignment='right',x=1.0)
#把函数作为形参时i，传入实参函数时，只要函数名即可，不用()
tf=tangent_line(fun1,po)
#因为tf返回的是lambda函数，所以要多调一次函数
y2=tf(x)
y1=fun2(x)
my=meanfunc(x)
tf=tangent_line(fun2,po)
y3=tf(x)
tf=tangent_line(meanfunc,po)
mmy=tf(x)
plt.plot(x,y,linestyle='--',color='aquamarine')
plt.plot(x,y2,linestyle='--',color='aquamarine')
plt.plot(x,y1,linestyle='--',color='lightgreen')
plt.plot(x,y3,linestyle='--',color='lightgreen')
plt.fill_between(x,y3,y2,facecolor = 'blue', alpha = 0.05)
plt.plot(x,my,color='r')
plt.plot(x,mmy,color='r')
#ax.vlines([po], -200000, 300000, linestyles='dashed', colors='red',label='$\\theta_0$')
plt.xticks([])  #去掉横坐标值
plt.yticks([])
plt.scatter(po,-990)
plt.annotate('$\\theta_0$', xy=(po,0), xytext=(po-20,-3000),fontsize=25)
po=po+0.0015*tf(po)
print(po)
plt.scatter(po,-990)
plt.annotate('$\\theta_1$', xy=(po,0), xytext=(po,-3000),fontsize=25)
plt.scatter(150,meanfunc(150))
plt.annotate('$\\theta^*$', xy=(150,meanfunc(150)), xytext=(140,meanfunc(150)-3000),fontsize=25)
#plt.show()
plt.tight_layout()
plt.savefig('./l.png')
