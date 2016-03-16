#!/usr/bin/env python3
from numpy.linalg import pinv
from numpy import multiply
from numpy import dot
from numpy import diag
from math import exp
import numpy as np
import sys

def B(pts, w_pts, w_nomials):
    return np.array([w_pts[i] * multiply(w_nomials, np.array([1, x, y, x**2, x*y, y**2, x**3, x**2*y, x*y**2])) for i, (x, y) in enumerate(pts)])

def fit(pts, phis, w_pts, w_nomials):
    Binv = pinv(B(pts, w_pts, w_nomials))
    return dot(dot(diag(w_nomials), Binv), multiply(w_pts, phis))

def f(pt, a):
    (x, y) = pt
    return a[0] + a[1]*x + a[2]*y + a[3]*x**2 + a[4]*x*y + a[5]*y**2 + a[6]*x**3 + a[7]*x**2*y + a[8]*x*y**2

def plot(a):
    return "f(x,y) = {a:.4g} + {b:.4g}*x + {c:.4g}*y + {d:.4g}*x**2 + {e:.4g}*x*y + {f:.4g}*y**2 + {g:.4g}*x**3 + {h:.4g}*x**2*y + {i:.4g}*x*y**2".format(a=a[0], b=a[1], c=a[2], d=a[3], e=a[4], f=a[5], g=a[6], h=a[7], i=a[8])

def plot_pt_surface(pt, a):
    (x, y) = pt
    return "\"<echo '{x:.4g} {y:.4g} {z:.4g}'\" with points ps 1.5 pt 6 lc rgb 'yellow' notitle, \\".format(x=x, y=y, z=f(pt, a)) + \
        "\n\"<echo '{x:.4g} {y:.4g} {z:.4g}'\" with impulses lc rgb 'yellow' notitle, \\".format(x=x, y=y, z=f(pt, a))

view1 = float(sys.argv[1]) % 360
view2 = float(sys.argv[2]) % 360
suffix = sys.argv[3]

pts = np.array([(-2.5, -1), (-1.5, -1), (-0.5, -1), (0.5, -1), \
                (-2.5, 0), (-1.5, 0), (-0.5, 0), (0.5, 0), \
                (-2.5, 1), (-1.5, 1), (-0.5, 1), (0.5, 1)])
phis = np.array([0.4, 0.3, 0.9, 0.5, \
                0.2, 1.1, 0.6, 0.7, \
                0.6, 2, 0.9, 0.5])

w_pts = np.ones_like(phis)
w_nomials = np.ones(9)
#w_nomials[0] = 1000
#w_nomials[0] = 1000
#w_pts[6] = 1000
#w_pts[7] = 1000

#print("set terminal wxt")
print("set terminal pngcairo size 1280,768 font 'sans-serif,18'")
print("set output 'plot{suffix}.png'".format(suffix=suffix))
print("unset key")
xs = [pt[0] for pt in pts]
ys = [pt[1] for pt in pts]
print("set xrange [{xmin}:{xmax}]".format(xmin=min(xs), xmax=max(xs)))
print("set yrange [{ymin}:{ymax}]".format(ymin=min(ys), ymax=max(ys)))
print("""set xlabel 'x'
set ylabel 'z'
set zlabel 'T'
set xtics offset 0,-0.5
set ytics offset 1,0
set xyplane 0
set xzeroaxis
set yzeroaxis
set isosamples 6,6
set pm3d
set palette gray
unset colorbox
set style line 1 lt 1 lw 1.5
set style line 2 lt 2 lw 2
set style line 3 lt 2 pt 2 ps 3 lw 2.5
set style line 4 lt 3 lw 2.5 lc rgbcolor '#feb24c' pt 6 ps 3""")
print("set view {x},{y}".format(x=view1, y=view2))

print("$pts << EOD")
for (x, y), phi in zip(pts, phis):
    print(x, y, phi)
print("EOD")

print("$central_pts << EOD")
for (x, y), phi in list(zip(pts, phis))[6:8]:
    print(x, y, phi)
print("EOD")

a = fit(pts, phis, w_pts, w_nomials)
print(plot(a))
print("splot f(x,y) with lines, \\")
print("""$pts using 1:2:3 with impulses ls 2 notitle, \\
$pts using 1:2:3 with points ls 3 notitle, \\""")
print("\"<echo '0 0 {z:.4g}'\" with impulses ls 4 notitle, \\".format(z=a[0]))
print("\"<echo '0 0 {z:.4g}'\" with points ls 4 notitle".format(z=a[0]))

