import math

a = int(input('请输入三角形的一条边长：'))
b = int(input('请输入三角形的另一条边长：'))
C = int(input('请输入三角形的两条边长的夹角度数：'))
# c = math.sqrt(a*a + b*b - 2*a*b*math.cos(C*math.pi/180))
c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(C*math.pi/180))
print(c)
    
