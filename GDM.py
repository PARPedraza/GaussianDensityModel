# -*- coding: utf-8 -*-
# @package Segmentation Cloud Points LiDAR 64E Velodyne
# GDM - Guassian Density Model
# Web Page
# https://github.com/PARPedraza/GaussianDensityModel
# autors: Alfonso Ramírez-Pedraza and José-Joel González-Barbosa

"""
Example:

        $ python GDM.py -i iValue
"""
import math, getopt
import numpy as np
import os, sys, csv, pandas as pd
from numpy import *
import matplotlib.pyplot as plt
from matplotlib import interactive
from itertools import cycle

class GaussianDensity(object):

    #######################################################
    #######################################################
    ####Builder
    #######################################################
    #######################################################
    def __init__(self, dir, Density):
        """The constructor Initialize Gaussian Density Model.
        Args:
            self: The object pointer.
            dir (str): destination directory (read and save files).
            rootname (str): objects name.
        Returns:
            pointer: The object pointer.
        """
        self.dir = dir
        self.rootname = "Object"
        self.WithDensity = "/dataset-with-Density"
        self.WithOutDensity = "/dataset-withOut-Density"
        self.Density = Density
        # Variables Declaration
        self.colors = cycle('grcmykgrcmykgrcmykgrcmyk')
        self.increOur = 1
        self.inputValue=0
        self.PtosDensiDentro = []
        self.MenorDistMaximos = []
        self.SubMax = []  # Matriz submax density
        self.extencionObject = ".csv"
        self.alpa = 194  # optimal value
        self.beta = 444  # optimal value
        self.gamma = 214  # optimal value
        self.dista = 100  # optimal value

    #######################################################
    #######################################################
    ####Utilities
    #######################################################
    #######################################################
    def findDistance(self, cloud, cen, flag):
        """Find distances on cloud ponts.
        Args:
            self: The object pointer.
            cloud (str): matrix with cloud point (x,y,z,d) where d is Density by point.
            cen (str): a point on the cloud.
            flag (int): distances type
        Returns:
            pos (str): positions on cloud point
        """
        x2 = np.array(cloud[:, 0])
        y2 = np.array(cloud[:, 1])
        x = np.array(cen)
        # Distance Euclidean
        dist = np.sqrt(((x2 - x[0]) ** 2 + (y2 - x[1]) ** 2))
        # Get kernel radial on different distances
        if (flag == 1):
            pos = [i for i, x in enumerate(dist) if x <= self.dista]
        if (flag == 2):
            pos = [i for i, x in enumerate(dist) if x <= self.alpa]
        if (flag == 3):
            pos = [i for i, x in enumerate(dist) if x > self.alpa and x <= self.beta]
        if (flag == 4):
            pos = [i for i, x in enumerate(dist) if x > self.alpa and x <= self.gamma]
        return pos

    def readData(self, file):
        """Read files cloud points csv.
        Args:
            self: The object pointer.
            file (str): path to files cloud points (csv).
        Returns:
            cloud (str): cloud points (x,y,z,d).
        """
        data = pd.read_csv(file)
        cloud = np.array(data)
        return cloud

    def Validate(self, dirFolder):
        """Create folder to save object segmentation.
        Args:
            self: The object pointer.
            dirFolder (str): path and name folder to save object segmentation.
        """
        try:
            os.stat(dirFolder)
        except:
            os.mkdir(dirFolder)

    def writeData(self, data, noObj, root):
        """Write objects.
        Args:
            self: The object pointer.
            noObj (str): number object segmented
            root (str): path and name folder to save object segmentation.
        """
        name = root + "/" + self.rootname + str(noObj) + self.extencionObject
        with open(name, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data)

    def searchItem(self, lista, elemento):
        """Search index, max density point.
        Args:
            self: The object pointer.
            lista (str): cloud points.
            elemento (str): max density point on cloud points.
        Returns:
            i (int): position (index) on cloud points.
        """
        for i in range(0, len(lista)):
            if (lista[i] == elemento):
                return i

    def findFiles(self, dir):
        """Find Files csv type.
        Args:
            self: The object pointer.
            dir (str): path to cloud points.
        Returns:
            list_files (str): list files cloud points founded.
        """
        list_files = [f for f in os.listdir(dir) if f.endswith(self.extencionObject)]
        return list_files

    def print2D(self, cloud, files, list_files1):
        """Find Files csv type.
        Args:
            self: The object pointer.
            cloud (str): cloud points.
            files (str): objects segmenented.
        """
        interactive(True)
        plt.figure(1)
        plt.plot(cloud[:, 0], cloud[:, 1], '.')
        for fileX, col in zip(list_files1, self.colors):
            filerootX = files + "/" + fileX
            # Read Cloud Point
            cloud1 = Point.readData(filerootX)
            plt.plot(cloud1[:, 0], cloud1[:, 1], col + '.')
        plt.xlabel('X Axis')
        plt.ylabel('Y Axis')
        interactive(False)
        plt.show()

    #######################################################
    #######################################################
    ####Gaussian Density Model Segmentation
    #######################################################
    #######################################################
    def DensityMetric(self, cloud):
        """Get Density cloud points.
        Args:
            self: The object pointer.
            cloud (str): cloud points (x,y,z).
        Returns:
            Data (str): cloud points with density (x,y,z,d).
        """
        sizeCloudY = len(cloud)
        data = np.array(cloud)
        dimensiones = (sizeCloudY, 4)
        Data = np.zeros(dimensiones)
        for i in range(sizeCloudY):
            cen = data[i, :]
            pos = Point.findDistance(data, cen, 1)
            TotPos = len(pos)
            Data[i][0] = cen[0]
            Data[i][1] = cen[1]
            Data[i][2] = cen[2]
            Data[i][3] = TotPos
        return Data

    def OurSegmentation(self, cloud, root):
        """Get Segmentation cloud points.
        Args:
            self: The object pointer.
            cloud (str): cloud points (x,y,z,d).
            root (str): path and name folder to save object segmentation.
        """
        global PosMax
        Ren = len(cloud)
        while (Ren > 0):
            max_item = max(cloud[:, 3], key=int)
            PosMax = Point.searchItem(cloud[:, 3], max_item)
            ##Define point Max on cloud point
            cen = cloud[PosMax, :]
            ##Find positions into alpa
            posInto = Point.findDistance(cloud, cen, 2)
            ##Find positions out beta
            posOut = Point.findDistance(cloud, cen, 3)
            # Get points into beta
            self.PtosDensiDentro = cloud[posOut, :]
            ##Get Sub-Max-and-Neighbors
            Point.SubMaxNeighbors(self.PtosDensiDentro, posOut)
            # Search other part object
            if (len(self.SubMax) != 0):
                posFaltaObject = Point.searchPointsJoins(cloud, cen)
                # Join points and save objects
                if (len(posFaltaObject) != 1):
                    Faltantes = cloud[posFaltaObject, :]
                    posObjeto = posInto + posFaltaObject
                else:
                    posObjeto = posInto
            else:
                posObjeto = posInto
            ##Save object to disk
            dataObject = np.array(cloud[posObjeto, :])
            # Save Objects
            Point.writeData(dataObject, self.increOur, root)
            self.increOur = self.increOur + 1
            # Delete points segmented
            cloud = delete(cloud, posObjeto, axis=0)
            Ren = len(cloud)
            if (Ren <= self.Density):
                Ren = 0
        self.PtosDensiDentro = []

    def searchPointsJoins(self, cloud, centroide):
        """Get object complete.
        Args:
            self: The object pointer.
            cloud (str): cloud points (x,y,z,d).
            centroide (str): max density point on cloud points.
        Returns:
            posFaltaObject (str): object, missing points.
        """
        for i in self.SubMax:
            cenSubMax = np.array(i)
            cen = np.array(centroide)
            # Search Distances Point Centroide Max Density versus Centroide SubMax Density
            dist = np.sqrt(((cenSubMax[0] - cen[0]) ** 2 + (cenSubMax[1] - cen[1]) ** 2))
            # Save Distances Point Centroide Max Density versus Centroide SubMax Density
            self.MenorDistMaximos.append(dist)
        # Find min distance
        Minimo = min(self.MenorDistMaximos)
        # Search position min distance on Vector MenorDistMaximos
        indice_min = [ii for ii, j in enumerate(self.MenorDistMaximos) if j == Minimo]
        # Find position min distance on cloud
        POSIC = np.array(self.SubMax[indice_min[0]])
        for i in range(0, len(cloud)):
            if ((cloud[i, 0] == POSIC[0]) and (cloud[i, 1] == POSIC[1]) and (cloud[i, 2] == POSIC[2]) and (
                    cloud[i, 3] == POSIC[3])):
                Index1 = i
        if 'Index1' in locals():
            # Search point on gamma
            posInto = Point.findDistance(cloud, centroide, 4)
            # Validate if min distance is area gamma
            indice_Esta = [ii for ii, j in enumerate(posInto) if j == Index1]
            if (len(indice_Esta) == 1):
                # If index have data, then, we segmented part object
                posFaltaObject = Point.findDistance(cloud, self.SubMax[indice_min[0]], 2)
            else:
                posFaltaObject = [0]
        else:
            posFaltaObject = [0]
        self.MenorDistMaximos = []
        self.SubMax = []
        return posFaltaObject

    def SubMaxNeighbors(self, cloudBeta, posOut):
        """Get objects subMax on Beta with size alpha and delete objects on variable cloudBeta
        Args:
            self: The object pointer.
            cloud (str): cloud points on kernel beta (x,y,z,d).
            posOut (str): positions out beta.
        """
        Ren = len(posOut)
        while (Ren > 0):
            ##Search Max on points out alpha and into beta
            max_item = max(cloudBeta[:, 3], key=int)
            ##Search position of point Max
            PosUpMax = Point.searchItem(cloudBeta[:, 3], max_item)
            ##Define point Max on cloud point beta
            cen = cloudBeta[PosUpMax, :]
            ##Find positions on Max and Neighbors to distances alpha
            posIntoOut = Point.findDistance(cloudBeta, cen, 2)
            # Point.print2D(cloudBeta, posIntoOut, 'r')
            ##Size point into alpha of submax point
            Ren1 = len(posIntoOut)
            if (Ren1 > 300):
                ##Save sub max out alpha into beta
                self.SubMax.append(cen)
                ##Find part object, positions on Max and Neighbors to distances alpha
                posObj = Point.findDistance(cloudBeta, cen, 2)
                ##Delete points sub object
                cloudBeta = delete(cloudBeta, posObj, axis=0)
                Ren = len(cloudBeta)
            else:
                Ren = 0

    def iniParam(self, dir,flag):
        # Find cloud points
        list_files = Point.findFiles(dir)

        # Get process on cloud point find on path
        print("Segmentation in process...")
        for file in list_files:
            ##Cadena File Name and Path
            fileroot = dir + "/" + file

            ##Validate: if exist folder to save objects
            Point.Validate(fileroot[:-4])
            ##Read Cloud Point
            cloud = Point.readData(fileroot)

            ##Get Density cloud point
            if(flag=="2"):
               print("Density in process...")
               cloud=Point.DensityMetric(cloud)

            ##Get Our-Segmentation
            Point.OurSegmentation(cloud, fileroot[:-4])

            # Plot results
            list_files1 = Point.findFiles(fileroot[:-4])
            Point.print2D(cloud, fileroot[:-4], list_files1)

    def usage(self):
        print(" Opcions:")
        print("--help (-h)")
        print("-i 1 \t\t <Get Segmentation using cloud points with Density>")
        print("-i 2 \t\t <Get Segmentation using cloud points without Density>")
        sys.exit()

    def main(self, argv):
        #inputValue = ''
        try:
            opts, args = getopt.getopt(argv, "i:", ["iValue="])
        except getopt.GetoptError:
            Point.usage()
        for opt, arg in opts:
            if opt in ("-h", "--help"):
                # print("GDM.py -i <inputValue>")
                Point.usage()
            elif opt in ("-i", "--iValue"):
                inputValue = arg[0]
                if arg[0] == "1":
                    self.inputValue=inputValue
                    Point.iniParam(self.dir+self.WithDensity,arg[0])
                elif arg[0] == '2':
                    self.inputValue=inputValue
                    Point.iniParam(self.dir+self.WithOutDensity,arg[0])
                else:
                    Point.usage()

if __name__ == "__main__":
    # Variables Input
    #dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dataset")
    dir = os.path.dirname(os.path.abspath(__file__))
    Density = 0  # Density segmentation number
    Point = GaussianDensity(dir, Density)
    Point.main(sys.argv[1:])
