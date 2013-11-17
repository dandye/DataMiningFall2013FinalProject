import pandas as pd
import sklearn
import pydot 
from sklearn import tree
from sklearn.externals.six import StringIO  
import StringIO




def atree(X,Y):
    
    X = [[0, 0], [1, 1]]
    >>> Y = [0, 1]
  
    
    clf = clf.fit(, Y)

    dot_data = StringIO.StringIO() 
    tree.export_graphviz(clf, out_file=dot_data) 
    graph = pydot.graph_from_dot_data(dot_data.getvalue()) 
    graph.write_pdf("iris.pdf") 



if __name__ == "__main__":
all_df = pd.read_csv(r"C:\Users\DanDye\Google Drive\Academic\DataMiningFall2013\FinalProject\data\adult_data.csv")
clean_df = pd.read_csv(r"C:\Users\DanDye\Google Drive\Academic\DataMiningFall2013\FinalProject\data\adult_data_no_missing_no_missing.csv")
all_df.describe()

x_cols =  ["age","workclass","education-num","marital-status","occupation","race","sex"]
x_cols =  ["age","education-num"]
y_cols = "gtlt"
clf = tree.DecisionTreeClassifier()
clf.fit(all_df[x_cols], all_df[y_cols])
dot_data = StringIO.StringIO() 
tree.export_graphviz(clf, out_file=dot_data) 
graph = pydot.graph_from_dot_data(dot_data.getvalue()) 
graph.write_pdf("tree.pdf") 

    