import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib import pyplot
matplotlib.use("Qt5Agg")


pyplot.rcParams['font.sans-serif'] = ['SimHei']
pyplot.rcParams['axes.unicode_minus'] = False


class Figure_Bar(FigureCanvasQTAgg):

    def __init__(self, width, height, parent=None):
        self.fig = pyplot.figure(figsize=(width, height), facecolor='#FFFFFF', dpi=100, edgecolor='#FFFFFF')
        FigureCanvasQTAgg.__init__(self, self.fig)
        self.setParent(parent)

        self.myAxes = self.fig.add_subplot(111)

    def ShowImage1(self, correctTime, answerTime):
        self.myAxes.clear()
        self.myAxes.barh([0], [answerTime],  height=0.01, color='red', label="FalseTimes", align='center')
        self.myAxes.legend()
        self.myAxes.barh([0], [correctTime], height=0.01, color='green', label="correctTimes", align='center')
        self.myAxes.legend()
        self.fig.canvas.draw()

    def ShowImage0(self, history):
        self.myAxes.clear()
        self.myAxes.bar(range(len(history)), history, label="capbility")
        self.myAxes.legend()
        self.fig.canvas.draw()

    def ShowImage2(self, history):
        self.myAxes.clear()
        self.myAxes.plot(range(len(history)), history, label="correctness")
        self.myAxes.legend()
        self.fig.canvas.draw()

    def ShowImage3(self, history):
        self.myAxes.clear()
        self.myAxes.plot(range(len(history)), history, label="history")
        self.myAxes.legend()
        self.fig.canvas.draw()
