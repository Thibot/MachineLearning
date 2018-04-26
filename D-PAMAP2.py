# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 20:00:54 2018

@author: Thibaut
"""
import D_DataFormatting as D_DF


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
    D_DF.DATtoCSV("./Data/PAMAP2_Dataset/Protocol/subject101.dat","./Data/PAMAP2_Dataset/Protocol/subject101.csv",Columns)
    D_DF.DATtoCSV("./Data/PAMAP2_Dataset/Protocol/subject102.dat","./Data/PAMAP2_Dataset/Protocol/subject102.csv",Columns)
    D_DF.DATtoCSV("./Data/PAMAP2_Dataset/Protocol/subject103.dat","./Data/PAMAP2_Dataset/Protocol/subject103.csv",Columns)
    D_DF.DATtoCSV("./Data/PAMAP2_Dataset/Protocol/subject104.dat","./Data/PAMAP2_Dataset/Protocol/subject104.csv",Columns)
    D_DF.DATtoCSV("./Data/PAMAP2_Dataset/Protocol/subject105.dat","./Data/PAMAP2_Dataset/Protocol/subject105.csv",Columns)
    D_DF.DATtoCSV("./Data/PAMAP2_Dataset/Protocol/subject106.dat","./Data/PAMAP2_Dataset/Protocol/subject106.csv",Columns)
    D_DF.DATtoCSV("./Data/PAMAP2_Dataset/Protocol/subject107.dat","./Data/PAMAP2_Dataset/Protocol/subject107.csv",Columns)
    D_DF.DATtoCSV("./Data/PAMAP2_Dataset/Protocol/subject108.dat","./Data/PAMAP2_Dataset/Protocol/subject108.csv",Columns)
    D_DF.DATtoCSV("./Data/PAMAP2_Dataset/Protocol/subject109.dat","./Data/PAMAP2_Dataset/Protocol/subject109.csv",Columns)

main()