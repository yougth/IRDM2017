
from fastFM import sgd
import numpy as np

class SGDFMClassification(sgd.FMClassification):
    def fit(self, X, y, *args):
        y = y.copy()
        y[y == 0] = -1
        return super(SGDFMClassification, self).fit(X, y, *args)

    def predict_proba(self, X_test):
        """
        Override predict_proba as its original output is not in line with Scikit-Learn's general conventions.
        :param X_test:
        :return:
        """
        probOfClickOne=super(SGDFMClassification, self).predict_proba(X_test)

        resultingProb = []
        for item in probOfClickOne:
            click1prob = item
            click0prob = 1 - item
            resultingProb.append([click0prob, click1prob])
        predictedProb = np.array(resultingProb)
        # print("predictedProb sample:", predictedProb.shape, predictedProb[0])
        return predictedProb


    # def predict(self, X_test, threshold=0.5):
    #     """
    #     Override to allow manual setting of threshold instead of the default 0.5
    #     see threshold on top of class.
    #     :param X_test:
    #     :return:
    #     """
    #
    #     probOfClickOne=super(SGDFMClassification, self).predict_proba(X_test)
    #
    #     counter=0
    #     resultingChoice = []
    #     for item in probOfClickOne:
    #         if (item >= threshold):
    #             counter=counter+1
    #             resultingChoice.append(1)
    #         else:
    #             resultingChoice.append(-1)
    #     predicted = np.array(resultingChoice)
    #     print("No of ones predicted:", counter)
    #     return predicted
