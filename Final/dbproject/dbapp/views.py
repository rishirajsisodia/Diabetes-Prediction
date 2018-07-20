from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request,'index.html',{'utext':'admin@hc.in','upass':'mypass'})
def result(request):
    return render(request,'result.html')
#MACHINE LEARNING STARTS HERE ===============================================================================================================
def register(request):
    p=request.GET["P"] 
    g=request.GET["G"] 
    b=request.GET["B"] 
    s=request.GET["S"] 
    i=request.GET["I"] 
    bm=request.GET["BM"] 
    d=request.GET["D"] 
    a=request.GET["A"] 
    #fetch user,pass from POST 
    from keras.models import Sequential
    from keras.layers import Dense
    import numpy 
    # fix random seed for reproducibility
    numpy.random.seed(5)

    dataset = numpy.loadtxt("C:/Users/dell/Desktop/Project Work on Diabetes/Project/pima-indians-diabetes.csv", delimiter=",")
    # X will be our training_data, Y will be our target_data (ex: all the factors that could determine if someone has diabetes and if they got diabetes in the past 5 years or not)
    X = dataset[:,0:8] # in other words, take all values from 0-7 (inclusive) from all the rows
    Y = dataset[:,8] # in other words, take each value of index 8 from all the rows

    #creating model
    model = Sequential()
    model.add(Dense(12, input_dim=8, activation='relu'))
    model.add(Dense(8, activation='relu'))
    model.add(Dense(1, activation='sigmoid')) # there is only one output neuron and it has a sigmoid function to switch to a 1 when above .5 and 0 when below .5
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy']) # using accuracy because this is a classification problem

    model.fit(X,Y, epochs=150, batch_size=10) # batch_size refers to how many instances should run before a weight value is updated.

    # evaluating the model
    scores = model.evaluate(X, Y)
    # calculate predictions
    predictions = model.predict(X)
    # round predictions
    rounded = [round(x[0]) for x in predictions]
    predictions
    p1=float(p)
    g1=float(g)
    BloodPressure=float(b)
    st=float(s)
    ins=float(i)
    BMI=float(bm)
    Di=float(d)
    Age=float(a)
    a=numpy.array([[p1   , g1   , BloodPressure  ,  st  , ins   , BMI  , Di,
            Age ]])

    predictions = model.predict(a)

    percentage=predictions[0]*100
    percentage1=int(percentage[0])
    rounded = [round(x[0]) for x in predictions]
    if rounded[0]==1:
        response=percentage1
    else:
        response=percentage1
#MACHINE LEARNING ENDS  HERE ===============================================================================================================

    return HttpResponse(response)
    

