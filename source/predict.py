class Predict:
    def __init__(self, X_final, model):
        self.X_final = X_final
        self.model = model

    def model_prediction(self):
        X_final = (self.X_final.reshape(len(self.X_final[0]), 1)).transpose()
        #y_pred = (self.model.predict(X_final) > 0.5).astype("int32")
        y_pred = self.model.predict(X_final).tolist()

        '''
        if y_pred[0][0] == 0:
            prediction = 'News is true'
        elif y_pred[0][0] == 1:
            prediction = 'News is fake'
        '''

        y_pred = 100 * y_pred[0][0]
        y_pred = round(y_pred, 3)

        return y_pred
