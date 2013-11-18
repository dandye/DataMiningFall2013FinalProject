import pandas as pd
import sklearn
import pydot 
from sklearn import tree
from sklearn.externals.six import StringIO  
import StringIO

all_df = pd.read_csv(r"C:\Users\DanDye\Google Drive\Academic\DataMiningFall2013\FinalProject\DataMiningFall2013FinalProject\data\adult_data.csv")
clean_df = pd.read_csv(r"C:\Users\DanDye\Google Drive\Academic\DataMiningFall2013\FinalProject\DataMiningFall2013FinalProject\data\adult_data_no_missing_no_missing.csv")

x_cols =  ["age","education-num"] #,"marital-status","occupation"]
y_cols = ["gtlt"]
clf = tree.DecisionTreeClassifier()
clf.fit(all_df[x_cols], all_df[y_cols])

dot_data = StringIO.StringIO() 
tree.export_graphviz(clf, out_file=dot_data) 
graph = pydot.graph_from_dot_data(dot_data.getvalue()) 
graph.write_png("tree.png") 

    