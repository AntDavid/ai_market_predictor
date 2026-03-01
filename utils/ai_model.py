import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from datetime import timedelta

def predict_future_trend(dataframe, days_to_predict=30, backtest=False):
    df = dataframe.copy()
    col_name = 'Close' if 'Close' in df.columns else df.columns[0]
    
    if backtest:
        if len(df) <= days_to_predict + 10:
            return None 
        
        train_df = df.iloc[:-days_to_predict].copy() 
        test_df = df.iloc[-days_to_predict:].copy()  
        
        train_df['Day_Index'] = np.arange(len(train_df))
        X_train = train_df[['Day_Index']].values
        y_train = train_df[col_name].values
        
        model = LinearRegression()
        model.fit(X_train, y_train)
        
        future_X = np.arange(len(train_df), len(train_df) + days_to_predict).reshape(-1, 1)
        raw_predictions = model.predict(future_X)
        
        last_train_date = train_df.index.max()
        last_train_price = train_df[col_name].iloc[-1]
        difference = last_train_price - raw_predictions[0]
        adjusted_predictions = raw_predictions + difference
        
        future_df = pd.DataFrame({
            'Tendência IA': adjusted_predictions,
            'Valor Real (Mercado)': test_df[col_name].values
        }, index=test_df.index)
        
        future_df.loc[last_train_date] = {'Tendência IA': last_train_price, 'Valor Real (Mercado)': last_train_price}
        future_df = future_df.sort_index()
        
        combined_df = pd.DataFrame({'Histórico': train_df[col_name]})
        combined_df = pd.concat([combined_df, future_df])
        return combined_df

    else:
        df['Day_Index'] = np.arange(len(df))
        X = df[['Day_Index']].values
        y = df[col_name].values

        model = LinearRegression()
        model.fit(X, y)

        last_date = df.index.max()
        last_real_price = df[col_name].iloc[-1]
        
        future_dates = [last_date + timedelta(days=i) for i in range(1, days_to_predict + 1)]
        future_X = np.arange(len(df), len(df) + days_to_predict).reshape(-1, 1)
        raw_predictions = model.predict(future_X)

        difference = last_real_price - raw_predictions[0]
        adjusted_predictions = raw_predictions + difference

        future_df = pd.DataFrame({'Tendência IA': adjusted_predictions}, index=future_dates)
        
        future_df.loc[last_date, 'Tendência IA'] = last_real_price
        future_df = future_df.sort_index()
        
        combined_df = pd.DataFrame({'Histórico': df[col_name]})
        combined_df = pd.concat([combined_df, future_df])
        return combined_df