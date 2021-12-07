
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox


xData = np.array([20, 15, 10, 5, 0, -5, -10, -15, -20])
yData = np.array([20, 25, 30, 35, 38, 41, 45, 48, 50])

fig, ax = plt.subplots(figsize=(10, 10))
fig.subplots_adjust(bottom=0.2, left=0.2)


global line_1
line_1 = ax.plot(xData, yData)
global line_2
line_2 = ax.plot(xData, yData)


def math(polynomialOrder):
    # curve fit the test data
    fittedParameters = np.polyfit(xData, yData, polynomialOrder)
    print('Fitted Parameters:', fittedParameters)

    modelPredictions = np.polyval(fittedParameters, xData)
    absError = modelPredictions - yData

    SE = np.square(absError) # squared errors
    MSE = np.mean(SE) # mean squared errors
    RMSE = np.sqrt(MSE) # Root Mean Squared Error, RMSE
    Rsquared = 1.0 - (np.var(absError) / np.var(yData))
    print('RMSE:', RMSE)
    print('R-squared:', Rsquared)

    print()
    #print(equation(fittedParameters, polynomialOrder))
    return fittedParameters

def submit(expression):       
    expression = int(expression) 
    fittedParameters = math(expression)
  

    # create data for the fitted equation plot
    xModel = np.linspace(min(xData), max(xData))
    yModel = np.polyval(fittedParameters, xModel)

    ax.legend(['original','created'])
    ax.plot(xData, yData)
    ax.set_title('Find the function for a given list')
    ax.legend(['original','created'])
    l= ax.get_legend()
    l.legendHandles[0].set_color("green")
    l.legendHandles[1].set_color("red")
    ax.xaxis.set_label_text('Grad Celsius')
    ax.yaxis.set_label_text('?')
    ax.grid(True)

    global line_1
    line = line_1.pop(0)
    line.remove()

    global line_2
    line = line_2.pop(0)    
    line.remove()
    
    line_1 = ax.plot(xData, yData, color='green')    
    line_2 = ax.plot(xModel, yModel, color="red")   
    ax.relim()
    ax.autoscale_view()
    plt.draw()


# t = np.arange(-2.0, 2.0, 0.001)
# l, = ax.plot(t, np.zeros_like(t), lw=2)
# def submit_equation(expression):
#     ydata = eval(expression)
#     l.set_ydata(ydata)
#     ax.relim()
#     ax.autoscale_view()
#     plt.draw()

def equation(polynomialOrder, fittedParameters):
    final=[]
    final.append("y = ")
    for i in range(0, polynomialOrder+1):
        if i<polynomialOrder:
            #print(plotted_list[-i-1])
            final.append(str(fittedParameters[-i-1]) + " x^" + str(i) + " + ")
        else:
            #print(plotted_list[-i-1])
            final.append(str(fittedParameters[-i-1]) + " x^" + str(i))
    
    return  "".join(final)



axbox = fig.add_axes([0.1, 0.05, 0.8, 0.075])
text_box = TextBox(axbox, "Evaluate")
text_box.on_submit(submit)
text_box.set_val("")  # Trigger `submit` with the initial string.

axbox2 = fig.add_axes([0.05, 0.9, 0.1, 0.1])
text_box2 = TextBox(axbox2, "x Value")#, textalignment="center")
text_box2.on_submit(submit)
text_box2.set_val("")  # Trigger `submit` with the initial string.

axbox3 = fig.add_axes([0.05, 0.8, 0.1, 0.1])
text_box3 = TextBox(axbox3, "y Value")#, textalignment="center")
text_box3.on_submit(submit)
text_box3.set_val("")  # Trigger `submit` with the initial string.

plt.show()
