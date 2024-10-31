import maya.cmds as cmds
import random

def generate_mountain(width, height, num_peaks, smoothness):

    plane = cmds.polyPlane(width=width, height= height, 
                           subdivisionsX=width, subdivisionsY=height)[0]
    peak_heights = [random.uniform(0,height) for n in range(num_peaks)]
    for x in range(width+1):
        for y in range(height+1):
            vertex_pos = cmds.pointPosition(f"{plane}.vtx[{x}][{y}]")
            for i in range(num_peaks):
                peak_x + random.uniform(0, width)
                peak_y = random.uniform(0,height)
                distance = ((x - peak_x)**2 + (y- peak_y)**2)**0.5
                influence = max(0, smoothness - distance)
                vertex_pos[2] += peak_heights[i] * influence/smoothness

            cmds.move(f"{plane}.vtx[{x}][{y}]", 
                      vertex_pos[0], vertex_pos[1], vertex_pos[2])
            
    return plane

def main():
    width = input("Width: ")
    height = input("Height: ")
    num_peaks = input("Number of peaks: ")
    smoothness = input("smoothness: ")
    generate_mountain(width, height, num_peaks, smoothness)

if __name__ == "__main__":
    main()