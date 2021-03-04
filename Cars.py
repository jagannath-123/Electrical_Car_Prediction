import pickle

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


class Cars:
    def __init__(self):
        self.model = DecisionTreeClassifier()
        
    def data_seperation(self, X, y):
        self.X_train,self.X_test,self.y_train,self.y_test = train_test_split(X, y, test_size=0.2)
        
    def training_model(self):
        self.model.fit(self.X_train,self.y_train)
        pickle.dump(self.model, open("../saved", "wb"))
        
    def testing_model(self):
        pred = self.model.predict(self.X_test)
        print(classification_report(self.y_test,pred))
        
    def new_data(self, raw):
        test = self.modify_data(raw)
        model = pickle.load(open("../saved", "rb"))
        pred = model.predict(test)
        return pred[0]
    
    def modify_data(self,x):
        test=pd.DataFrame(data=[[0 for i in range(17)]],columns=df.columns)
        test.drop("CAR",axis=1, inplace=True)
        test[x[0]] = 1
        test["(km)"] = df["(km)"].mean()
        test["CITY (Le/100 km)"] = df['CITY (Le/100 km)'].mean()
        test["HWY (Le/100 km)"] = df['HWY (Le/100 km)'].mean()
        test["COMB (Le/100 km)"] = df['COMB (Le/100 km)'].mean()
        if x[1]=="city": 
            test["CITY (kWh/100 km)"] = df['CITY (kWh/100 km)'].max()
            test["HWY (kWh/100 km)"] = df['HWY (kWh/100 km)'].min()
            test["COMB (kWh/100 km)"] = df['COMB (kWh/100 km)'].mean()
        if x[1]=="hwy": 
            test["CITY (kWh/100 km)"] = df['CITY (kWh/100 km)'].min()
            test["HWY (kWh/100 km)"] = df['HWY (kWh/100 km)'].max()
            test["COMB (kWh/100 km)"] = df['COMB (kWh/100 km)'].mean()
        if x[1]=="comb": 
            test["CITY (kWh/100 km)"] = df['CITY (kWh/100 km)'].mean()
            test["HWY (kWh/100 km)"] = df['HWY (kWh/100 km)'].mean()
            test["COMB (kWh/100 km)"] = df['COMB (kWh/100 km)'].max()

        # Battery
        if x[2]=="s":
            test['(kW)'] = df["(kW)"].min()
        if x[2]=="m":
            test['(kW)'] = df["(kW)"].mean()
        if x[2]=="l":
            test['(kW)'] = df["(kW)"].max()
        
        # Time
        if x[3]=="s":
            test["TIME (h)"] = df["TIME (h)"].min()
        if x[3]=="m":
            test["TIME (h)"] = df["TIME (h)"].mean()
        if x[3]=="l":
            test["TIME (h)"] = df["TIME (h)"].max()

        return test
        
        


df = pd.read_csv("cars.csv")


df["CAR"] = df["MAKE"]+' '+df["MODEL"]

dummy = pd.get_dummies(df['SIZE'])
df.drop(["MAKE","MODEL","YEAR","Unnamed: 5","TYPE","SIZE", "(g/km)","RATING"],axis=1,inplace=True)

for i in dummy.columns:
    df[i] = dummy[i]

rf = Cars()
rf.data_seperation(df.drop("CAR",axis=1),df["CAR"])
rf.training_model()


plt.show()