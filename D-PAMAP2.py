# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 20:00:54 2018

@author: Thibaut
"""
import D_DataFormatting as D_DF
import D_GenerateDQR as D_DQR
import pandas as pd


def main():
    #This is an example but DON'T EXECUTE IT
    
    Columns=["Timestamp","ActivityID","HeartRate","Hand_Temperature","Hand_3Dacceleration16_X","Hand_3Dacceleration16_Y",
             "Hand_3Dacceleration16_Z","Hand_3Dacceleration6_X","Hand_3Dacceleration6_Y","Hand_3Dacceleration6_Z",
             "Hand_3Dgyroscop_X","Hand_3Dgyroscop_Y","Hand_3Dgyroscop_Z","Hand_3Dmagnetometer_X",
             "Hand_3Dmagnetometer_Y","Hand_3Dmagnetometer_Z","Hand_Orientation_1","Hand_Orientation_2",
             "Hand_Orientation_3","Hand_Orientation_4",
             "Chest_Temperature","Chest_3Dacceleration16_X","Chest_3Dacceleration16_Y",
             "Chest_3Dacceleration16_Z","Chest_3Dacceleration6_X","Chest_3Dacceleration6_Y","Chest_3Dacceleration6_Z",
             "Chest_3Dgyroscop_X","Chest_3Dgyroscop_Y","Chest_3Dgyroscop_Z","Chest_3Dmagnetometer_X",
             "Chest_3Dmagnetometer_Y","Chest_3Dmagnetometer_Z","Chest_Orientation_1","Chest_Orientation_2",
             "Chest_Orientation_3","Chest_Orientation_4",
             "Ankle_Temperature","Ankle_3Dacceleration16_X","Ankle_3Dacceleration16_Y",
             "Ankle_3Dacceleration16_Z","Ankle_3Dacceleration6_X","Ankle_3Dacceleration6_Y","Ankle_3Dacceleration6_Z",
             "Ankle_3Dgyroscop_X","Ankle_3Dgyroscop_Y","Ankle_3Dgyroscop_Z","Ankle_3Dmagnetometer_X",
             "Ankle_3Dmagnetometer_Y","Ankle_3Dmagnetometer_Z","Ankle_Orientation_1","Ankle_Orientation_2",
             "Ankle_Orientation_3","Ankle_Orientation_4"]
    
    #Conversion .dat files into .csv files with columns names  
    #PROTOCOL
#    D_DF.DATtoCSV("./Data/PAMAP2_Dataset/Protocol/subject101.dat","./Data/PAMAP2_Dataset/Protocol/subject101.csv",Columns)
#    D_DF.DATtoCSV("./Data/PAMAP2_Dataset/Protocol/subject102.dat","./Data/PAMAP2_Dataset/Protocol/subject102.csv",Columns)
#    D_DF.DATtoCSV("./Data/PAMAP2_Dataset/Protocol/subject103.dat","./Data/PAMAP2_Dataset/Protocol/subject103.csv",Columns)
#    D_DF.DATtoCSV("./Data/PAMAP2_Dataset/Protocol/subject104.dat","./Data/PAMAP2_Dataset/Protocol/subject104.csv",Columns)
#    D_DF.DATtoCSV("./Data/PAMAP2_Dataset/Protocol/subject105.dat","./Data/PAMAP2_Dataset/Protocol/subject105.csv",Columns)
#    D_DF.DATtoCSV("./Data/PAMAP2_Dataset/Protocol/subject106.dat","./Data/PAMAP2_Dataset/Protocol/subject106.csv",Columns)
#    D_DF.DATtoCSV("./Data/PAMAP2_Dataset/Protocol/subject107.dat","./Data/PAMAP2_Dataset/Protocol/subject107.csv",Columns)
#    D_DF.DATtoCSV("./Data/PAMAP2_Dataset/Protocol/subject108.dat","./Data/PAMAP2_Dataset/Protocol/subject108.csv",Columns)
#    D_DF.DATtoCSV("./Data/PAMAP2_Dataset/Protocol/subject109.dat","./Data/PAMAP2_Dataset/Protocol/subject109.csv",Columns)
#    
#    #OPTIONAL
#    D_DF.DATtoCSV("./Data/PAMAP2_Dataset/Optional/subject101.dat","./Data/PAMAP2_Dataset/Optional/subject101.csv",Columns)
#    D_DF.DATtoCSV("./Data/PAMAP2_Dataset/Optional/subject105.dat","./Data/PAMAP2_Dataset/Optional/subject105.csv",Columns)
#    D_DF.DATtoCSV("./Data/PAMAP2_Dataset/Optional/subject106.dat","./Data/PAMAP2_Dataset/Optional/subject106.csv",Columns)
#    D_DF.DATtoCSV("./Data/PAMAP2_Dataset/Optional/subject108.dat","./Data/PAMAP2_Dataset/Optional/subject108.csv",Columns)
#    D_DF.DATtoCSV("./Data/PAMAP2_Dataset/Optional/subject109.dat","./Data/PAMAP2_Dataset/Optional/subject109.csv",Columns)
    
    
    
    ContinuousColumns=["HeartRate","Hand_Temperature","Hand_3Dacceleration16_X","Hand_3Dacceleration16_Y",
             "Hand_3Dacceleration16_Z","Hand_3Dacceleration6_X","Hand_3Dacceleration6_Y","Hand_3Dacceleration6_Z",
             "Hand_3Dgyroscop_X","Hand_3Dgyroscop_Y","Hand_3Dgyroscop_Z","Hand_3Dmagnetometer_X",
             "Hand_3Dmagnetometer_Y","Hand_3Dmagnetometer_Z","Hand_Orientation_1","Hand_Orientation_2",
             "Hand_Orientation_3","Hand_Orientation_4",
             "Chest_Temperature","Chest_3Dacceleration16_X","Chest_3Dacceleration16_Y",
             "Chest_3Dacceleration16_Z","Chest_3Dacceleration6_X","Chest_3Dacceleration6_Y","Chest_3Dacceleration6_Z",
             "Chest_3Dgyroscop_X","Chest_3Dgyroscop_Y","Chest_3Dgyroscop_Z","Chest_3Dmagnetometer_X",
             "Chest_3Dmagnetometer_Y","Chest_3Dmagnetometer_Z","Chest_Orientation_1","Chest_Orientation_2",
             "Chest_Orientation_3","Chest_Orientation_4",
             "Ankle_Temperature","Ankle_3Dacceleration16_X","Ankle_3Dacceleration16_Y",
             "Ankle_3Dacceleration16_Z","Ankle_3Dacceleration6_X","Ankle_3Dacceleration6_Y","Ankle_3Dacceleration6_Z",
             "Ankle_3Dgyroscop_X","Ankle_3Dgyroscop_Y","Ankle_3Dgyroscop_Z","Ankle_3Dmagnetometer_X",
             "Ankle_3Dmagnetometer_Y","Ankle_3Dmagnetometer_Z","Ankle_Orientation_1","Ankle_Orientation_2",
             "Ankle_Orientation_3","Ankle_Orientation_4"]
    
    
    CategoricalColumns=["ActivityID"]
    
    #DQRs on the first versions of datas
#    for i in range(1,10):
#        #Read csv files for generating DQR of each one
#        data = pd.read_csv("./Data/PAMAP2_Dataset/Protocol/subject10"+str(i)+".csv", header = 0,na_values={"HeartRate": [" ?"],"Hand_Temperature": [" ?"],"Chest_Temperature": [" ?"],"Ankle_Temperature": [" ?"]},keep_default_na=False)
#        D_DQR.outputContinuous(data,ContinuousColumns,"Protocol","subject10"+str(i)+"")
#        D_DQR.outputCategorical(data,CategoricalColumns,"Protocol","subject10"+str(i)+"")
#        print("DQR - subject10"+str(i)+"Protocol Activities   :   Generated")
#        
#    for i in [1,5,6,8,9]:
#        #Read csv files for generating DQR of each one
#        data = pd.read_csv("./Data/PAMAP2_Dataset/Optional/subject10"+str(i)+".csv", header = 0,na_values={"HeartRate": [" ?"],"Hand_Temperature": [" ?"],"Chest_Temperature": [" ?"],"Ankle_Temperature": [" ?"]},keep_default_na=False)
#        D_DQR.outputContinuous(data,ContinuousColumns,"Optional","subject10"+str(i)+"")
#        D_DQR.outputCategorical(data,CategoricalColumns,"Optional","subject10"+str(i)+"")
#        print("DQR - subject10"+str(i)+"Optional Activities   :   Generated")
    
    
    #------------------------------------------------
    #-----------CLEANING-----------------------------
    
    #Delete the rows where the ActivityID = 0 and the columns of orientation and 3D acceleration scale 6g
    ColumnsClean = ["ActivityID","HeartRate","Hand_Temperature","Hand_3Dacceleration16_X","Hand_3Dacceleration16_Y",
             "Hand_3Dacceleration16_Z","Hand_3Dgyroscop_X","Hand_3Dgyroscop_Y","Hand_3Dgyroscop_Z","Hand_3Dmagnetometer_X",
             "Hand_3Dmagnetometer_Y","Hand_3Dmagnetometer_Z",
             "Chest_Temperature","Chest_3Dacceleration16_X","Chest_3Dacceleration16_Y",
             "Chest_3Dacceleration16_Z","Chest_3Dgyroscop_X","Chest_3Dgyroscop_Y","Chest_3Dgyroscop_Z","Chest_3Dmagnetometer_X",
             "Chest_3Dmagnetometer_Y","Chest_3Dmagnetometer_Z",
             "Ankle_Temperature","Ankle_3Dacceleration16_X","Ankle_3Dacceleration16_Y",
             "Ankle_3Dacceleration16_Z","Ankle_3Dgyroscop_X","Ankle_3Dgyroscop_Y","Ankle_3Dgyroscop_Z","Ankle_3Dmagnetometer_X",
             "Ankle_3Dmagnetometer_Y","Ankle_3Dmagnetometer_Z"]
    
    
    
#    for i in range(1,9):
#        
##        #Read csv files for generating DQR of each one
#        data = pd.read_csv("./Data/PAMAP2_Dataset/Protocol/subject10"+str(i)+".csv", header = 0,na_values={"HeartRate": [" ?"],"Hand_Temperature": [" ?"],"Chest_Temperature": [" ?"],"Ankle_Temperature": [" ?"]},keep_default_na=False)
#        data= D_DF.delRow(data,"ActivityID",0)
#        data= D_DF.delRow(data,"HeartRate","NaN")
#        data= D_DF.delRow(data,"Hand_Temperature","NaN")
#        data= D_DF.delRow(data,"Chest_Temperature","NaN")
#        data= D_DF.delRow(data,"Ankle_Temperature","NaN")
#        data=data.drop(["Timestamp","Hand_3Dacceleration6_X","Hand_3Dacceleration6_Y","Hand_3Dacceleration6_Z",
#                        "Hand_Orientation_1","Hand_Orientation_2","Hand_Orientation_3","Hand_Orientation_4",
#                        "Chest_3Dacceleration6_X","Chest_3Dacceleration6_Y","Chest_3Dacceleration6_Z",
#                        "Chest_Orientation_1","Chest_Orientation_2","Chest_Orientation_3","Chest_Orientation_4",
#                        "Ankle_3Dacceleration6_X","Ankle_3Dacceleration6_Y","Ankle_3Dacceleration6_Z",
#                        "Ankle_Orientation_1","Ankle_Orientation_2","Ankle_Orientation_3","Ankle_Orientation_4"],axis=1)
#        data.to_csv("./Data/PAMAP2_Dataset/Protocol/subject10"+str(i)+"_clean.csv",columns=ColumnsClean)
#        print("subject10"+str(i)+"_clean.csv   :   Generated")
#        
#    ContinuousColumns = ["HeartRate","Hand_Temperature","Hand_3Dacceleration16_X","Hand_3Dacceleration16_Y",
#             "Hand_3Dacceleration16_Z","Hand_3Dgyroscop_X","Hand_3Dgyroscop_Y","Hand_3Dgyroscop_Z","Hand_3Dmagnetometer_X",
#             "Hand_3Dmagnetometer_Y","Hand_3Dmagnetometer_Z",
#             "Chest_Temperature","Chest_3Dacceleration16_X","Chest_3Dacceleration16_Y",
#             "Chest_3Dacceleration16_Z","Chest_3Dgyroscop_X","Chest_3Dgyroscop_Y","Chest_3Dgyroscop_Z","Chest_3Dmagnetometer_X",
#             "Chest_3Dmagnetometer_Y","Chest_3Dmagnetometer_Z",
#             "Ankle_Temperature","Ankle_3Dacceleration16_X","Ankle_3Dacceleration16_Y",
#             "Ankle_3Dacceleration16_Z","Ankle_3Dgyroscop_X","Ankle_3Dgyroscop_Y","Ankle_3Dgyroscop_Z","Ankle_3Dmagnetometer_X",
#             "Ankle_3Dmagnetometer_Y","Ankle_3Dmagnetometer_Z"]
#    
#    for i in range(1,9):
#        data = pd.read_csv("./Data/PAMAP2_Dataset/Protocol/subject10"+str(i)+"_clean.csv", header = 0)
#        D_DQR.outputContinuous(data,ContinuousColumns,"Protocol","subject10"+str(i)+"_clean")
#        D_DQR.outputCategorical(data,CategoricalColumns,"Protocol","subject10"+str(i)+"_clean")
#
#    for i in [1,5,6,8,9]:
#         #Read csv files for generating DQR of each one
#        data = pd.read_csv("./Data/PAMAP2_Dataset/Optional/subject10"+str(i)+".csv", header = 0,na_values={"HeartRate": [" ?"],"Hand_Temperature": [" ?"],"Chest_Temperature": [" ?"],"Ankle_Temperature": [" ?"]},keep_default_na=False)
#        data= D_DF.delRow(data,"ActivityID",0)
#        data= D_DF.delRow(data,"HeartRate","NaN")
#        data= D_DF.delRow(data,"Hand_Temperature","NaN")
#        data= D_DF.delRow(data,"Chest_Temperature","NaN")
#        data= D_DF.delRow(data,"Ankle_Temperature","NaN")
#        data=data.drop(["Timestamp","Hand_3Dacceleration6_X","Hand_3Dacceleration6_Y","Hand_3Dacceleration6_Z",
#                        "Hand_Orientation_1","Hand_Orientation_2","Hand_Orientation_3","Hand_Orientation_4",
#                        "Chest_3Dacceleration6_X","Chest_3Dacceleration6_Y","Chest_3Dacceleration6_Z",
#                        "Chest_Orientation_1","Chest_Orientation_2","Chest_Orientation_3","Chest_Orientation_4",
#                        "Ankle_3Dacceleration6_X","Ankle_3Dacceleration6_Y","Ankle_3Dacceleration6_Z",
#                        "Ankle_Orientation_1","Ankle_Orientation_2","Ankle_Orientation_3","Ankle_Orientation_4"],axis=1)
#        data.to_csv("./Data/PAMAP2_Dataset/Optional/subject10"+str(i)+"_clean.csv",columns=ColumnsClean)
#        
#    for i in [1,5,6,8,9]:
#        D_DQR.outputContinuous(data,ContinuousColumns,"Optional","subject10"+str(i)+"_clean")
#        D_DQR.outputCategorical(data,CategoricalColumns,"Optional","subject10"+str(i)+"_clean")
    

main()