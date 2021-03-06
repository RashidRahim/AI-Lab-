from keras.models import Sequential
from keras.layers import Dense
import numpy
numpy.random.seed(7)
dataset = numpy.loadtxt("pima-indians-diabetes.csv",delimiter=",")
X = dataset[:700,0:8]
Y = dataset[:700,8]
evalX = dataset[701:1000,0:8]
evalY = dataset[701:1000,8]
model = Sequential()
model.add(Dense(12,input_dim=8,activation='relu'))
model.add(Dense(8,activation='relu'))
model.add(Dense(7,activation='relu'))
model.add(Dense(6,activation='relu'))
model.add(Dense(5,activation='relu'))
model.add(Dense(4,activation='relu'))
model.add(Dense(1,activation='sigmoid'))
model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
model.fit(X,Y,epochs=150,batch_size=10)
scores = model.evaluate(evalX,evalY)
print("\n%s: %.2f%%"%(model.metrics_names[1],scores[1]*100))
prediction = model.predict(X)
rounded = [round(x[0]) for x in prediction]
print(rounded)


