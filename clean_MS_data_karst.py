import pandas as pd

filepath = "data/FBS_Alone_top3.csv"
Save_Descriptor = "FBS_Alone_top3"

#import data and drop uneeded columns and rows
MS_data = pd.read_csv(filepath)
MS_data_reduced = MS_data[["Protein IDs", "Intensity FBS"]]
MS_data_reduced.drop([0], axis=0, inplace=True)
MS_data_reduced = MS_data_reduced.reset_index(drop=True)

#Clean Acessions IDs
Acession_IDS = MS_data_reduced["Protein IDs"]
ID_List = []

for i in Acession_IDS:
   ID = i[3:9]
   ID_List.append(ID)

IDs_series = pd.Series(ID_List, name="IDs")
IDs_df = IDs_series.to_frame()
#Add Cleaned Acessions IDs back to df
MS_data_temp = pd.concat([MS_data_reduced,IDs_df], ignore_index=True, axis=1)

#rename columns and drop uncleaned IDs
MS_data_temp.rename(columns={0: "temp", 1: "Intensity", 2: "Acession Numbers"}, inplace=True)
MS_data_cleaned = MS_data_temp[["Acession Numbers", "Intensity"]]

#save data to excel sheet
save_filepath = "data/" + Save_Descriptor + ".xlsx"
MS_data_cleaned.to_excel(save_filepath)
