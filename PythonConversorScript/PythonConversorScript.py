import os
import glob
import sys, traceback
import csv
import openpyxl
import os
import pandas as pd
import optparse

root_path = os.path.dirname(os.path.abspath(__file__))


class ConversionDatos(object):

    def __init__(self, a):
        self.nombreArchivo = a


    def ObtenerCantidadColumnas(self):
        ObtenerLargoArchivo = pd.read_csv(self.nombreArchivo, quoting=csv.QUOTE_ALL)
        return int(ObtenerLargoArchivo.shape[0])


   
    def CargarArchivo(self):
        Archivo = open(self.nombreArchivo, 'rU')
        variableDatos = csv.reader(Archivo, delimiter=',')
        TablaMatriz = [row for row in variableDatos]
        print("Cargando en la memoria ...")
        return TablaMatriz




    def ConvertirData(TablaMatriz):
        bufferPrimario =[]
        #for IndexMatriz in range(0, ObtenerCantidadColumnas()):
        #    bufferPrimario.append([("%s, %s, %s, %" % tablaMatriz[IndexMatriz][0], tablaMatriz[IndexMatriz][1], tablaMatriz[IndexMatriz][2], tablaMatriz[IndexMatriz][3])])

        return TablaMatrix[0][0]


    def EscribirArchivoPantalla():
        for a in range(0, ObtenerCantidadColumnas()):
           print (bufferPrimario[a])
    




if  __name__ =='__main__':

         p = optparse.OptionParser()
         p.add_option('--A', '-a')
         p.add_option('-V','-v')
         options, arguments = p.parse_args()
         a = ConversionDatos('007.csv')
         a.CargarArchivo()
         a.ConvertirData()
            

         print(a.ObtenerCantidadColumnas())
         



 
  







      



    

