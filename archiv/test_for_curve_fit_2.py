import sys
from matplotlib import animation
import numpy, matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation as FA


polynomialOrder = 14 # example quadratic

xData = numpy.array([20, 15, 10, 5, 0, -5, -10, -15, -20])
yData = numpy.array([20, 25, 30, 35, 38, 41, 45, 48, 50])

class math:
    def __init__(self):
        pass

    def math(self, polynomialOrder):

        # curve fit the test data
        fittedParameters = numpy.polyfit(xData, yData, polynomialOrder)
        print('Fitted Parameters:', fittedParameters)

        modelPredictions = numpy.polyval(fittedParameters, xData)
        absError = modelPredictions - yData

        SE = numpy.square(absError) # squared errors
        MSE = numpy.mean(SE) # mean squared errors
        RMSE = numpy.sqrt(MSE) # Root Mean Squared Error, RMSE
        Rsquared = 1.0 - (numpy.var(absError) / numpy.var(yData))
        print('RMSE:', RMSE)
        print('R-squared:', Rsquared)

        print()
        return fittedParameters

class plotting:
    def __init__(self, m):
        self.m = m
        self.fittedParameters = self.m.math(polynomialOrder)

        graphWidth = 800
        graphHeight = 600
        self.f = plt.figure(figsize=(graphWidth/100.0, graphHeight/100.0), dpi=100)
        self.axes = self.f.add_subplot(111)        

    def main(self):

        def animate(i):
            self.fittedParameters = self.m.math(polynomialOrder)

            # first the raw data as a scatter plot
            self.axes.plot(xData, yData,  'D')

            # create data for the fitted equation plot
            xModel = numpy.linspace(min(xData), max(xData))
            yModel = numpy.polyval(self.fittedParameters, xModel)

            # now the model as a line plot
            self.axes.plot(xModel, yModel, "blue")
            #plot the original data
            self.axes.plot(xData, yData, "red")

            self.axes.set_xlabel('X Data') # X axis data label
            self.axes.set_ylabel('Y Data') # Y axis data label
        
        ##########################################################
        # graphics output section
        def ModelAndScatterPlot(graphWidth, graphHeight):
            # f = plt.figure(figsize=(graphWidth/100.0, graphHeight/100.0), dpi=100)
            # axes = f.add_subplot(111)

            # # first the raw data as a scatter plot
            # axes.plot(xData, yData,  'D')

            # # create data for the fitted equation plot
            # xModel = numpy.linspace(min(xData), max(xData))
            # yModel = numpy.polyval(self.fittedParameters, xModel)

            # # now the model as a line plot
            # axes.plot(xModel, yModel, "blue")
            # #plot the original data
            # axes.plot(xData, yData, "red")

            # axes.set_xlabel('X Data') # X axis data label
            # axes.set_ylabel('Y Data') # Y axis data label
                        

            ani = animation.FuncAnimation(self.f, animate, interval=1000)
            plt.show()  
            plt.close('all') # clean up after using pyplot

        graphWidth = 800
        graphHeight = 600
        ModelAndScatterPlot(graphWidth, graphHeight)

        def equation():
            final=[]
            final.append("y = ")
            for i in range(0, polynomialOrder+1):
                if i<polynomialOrder:
                    #print(plotted_list[-i-1])
                    final.append(str(self.fittedParameters[-i-1]) + " x^" + str(i) + " + ")
                else:
                    #print(plotted_list[-i-1])
                    final.append(str(self.fittedParameters[-i-1]) + " x^" + str(i))
            
            return  "".join(final)

        print(equation())

#CHECKPOINT
#tausch dieses mit dem aus pygame_input aus, da der Input übergibt und nicht bekommt
if __name__ == "__main__":
    m = math()         
    p = plotting(m.math(polynomialOrder))     
    p.main() 
    sys.exit()    
    sys.exit()  
    