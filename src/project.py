import maya.cmds as cmds
import random

landsub = 100
landsize = 400
maxheight = 15
land = cmds.polyPlane(sx = landsub, sy = landsub, 
                      w = landsize, h = landsize)
vertex_nb = cmds.polyEvaluate(v=True)
vertex_Count = list(range(vertex_nb))

values = []
high_values = [random.triangular(0,1,0)
                for i in range(int(vertex_nb/10))]
low_values = [random.uniform(0,0.3)
              for i in range(int(vertex_nb/2))]
values = low_values + high_values
values_count = len(values)
SEED = 448
random.seed(SEED)
random.shuffle(vertex_Count)
random.shuffle(values)
optimize_setter = []

for x in vertex_Count:
    mod = x % values_count
    # cmds.move(values[mod-1]*maxheight, land[0] + '.vtx[' + str(x) + ']', y=True, absolute=True)
    optimize_setter += [float(0), values[mod-1]*maxheight,float(0)]
cmds.setAttr('pPlane1.vtx[:]', *optimize_setter)
cmds.select(land[0])

if __name__ == "__main__":
    main()