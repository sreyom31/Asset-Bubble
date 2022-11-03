import numpy as np
import pandas as pd 
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow.keras.models import Sequential 
from tensorflow.keras.layers import Dense , Dropout
from sklearn import metrics
from tensorflow.keras.optimizers import Adam
def model():
            df=pd.read_csv('/home/coder/project/workspace/data.csv')
            df.drop(columns='Reason',axis=1,inplace=True)
            df.drop(columns='LOCATION',axis=1,inplace=True)
            df['DateTime']=pd.to_datetime(df['TIME'])
            df['year']=df['DateTime'].dt.year
            df['month']=df['DateTime'].dt.month
            df.dropna(inplace=True)
            df.drop(columns='DateTime',axis=1,inplace=True)
            df.drop(columns="TIME",inplace=True)
            x=df.drop(columns="Crash")
            y=df["Crash"]
            x_train,x_test,y_train,y_test=train_test_split(x,y)
            model=Sequential()
            model.add(Dense(256,activation="relu"))
            model.add(Dropout(0.2))
            model.add(Dense(128,activation="relu"))
            model.add(Dropout(0.25))
            model.add(Dense(128,activation="relu"))
            model.add(Dropout(0.25))
            model.add(Dense(64,activation="relu"))
            model.add(Dropout(0.25))
            model.add(Dense(1,activation="sigmoid"))
            model.compile(optimizer='Adam',loss="binary_crossentropy",metrics=['accuracy'])
            model.fit(x_train,y_train,epochs=100)
            #y_pred=model.predict(x_test)
            #print("Accuracy: ",metrics.accuracy_score(y_test,y_pred))
def main():
    model()
if __name__=="__main__":
    main()