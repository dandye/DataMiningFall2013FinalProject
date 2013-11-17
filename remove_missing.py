
of = open(r"C:\Users\DanDye\Google Drive\Academic\DataMiningFall2013\FinalProject\data\adult_data_no_missing.csv","w")

lines = open(r"C:\Users\DanDye\Google Drive\Academic\DataMiningFall2013\FinalProject\data\adult_data.csv").readlines()

for aline in lines:
    if "?" not in aline:
        of.write(aline)
        
of.close()