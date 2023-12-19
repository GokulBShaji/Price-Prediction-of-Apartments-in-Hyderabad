# Price-Prediction-of-Apartments-in-Hyderabad
Educational purpose project with considerable assumptions

## Objective
- To create a price predictive model for real estate evaluation.
- Analysis of the prediction done by the model.

## Assumptions
- For considering the importance of location only 2 parameters are taken i.e Shortest Haversine Distance to Nearest Railway station and Nearest Hospital.
- Railway stations database used here was created as part of Location-Score project [link](https://github.com/GokulBShaji/Location-Score-Apartments-Bangalore) and geocoding was done using OpenMaps api.So the accuracy is relatively less as compared to Googlemaps api
- Hospitals database used here is a subset(to reduce run time) from goverment website dated back to 2016 [link](https://data.gov.in/catalog/all-india-health-centres-directory)

## Procedure
- Install the following libraries - sklearn,Pandas,Openpyxl
- Download all the files from the Hyderabad_Price_Prediction folder of this repository.
- Run the Data_Collection.py file for entering the data for price prediction
- Then open the jupyter notebook file(Final Model.ipynb) and execute Restart kernal and run all cells.
- Predicted price is displayed as the last cell of the Jupyter notebook file

## Results
- Regression Model Used here - Polynomial Regression of degree 4
- Obtained a regression score or R^2 value of 0.589244593688183 (close to 1 than to 0 but still the model is far behind in Accuracy)
- Prediction analysis was done on 10 listings under various projects of Hyderabad and the average absolute error observed was 29.78552134% (Refer Prediction_Analysis.xlsx file under the project folder)

