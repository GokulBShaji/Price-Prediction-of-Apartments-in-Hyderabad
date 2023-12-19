import pandas as pd
from haversine import haversine


df1 = pd.DataFrame()
df2 = pd.read_excel('Railway_Station.xlsx')
df3 = pd.read_excel('hospitals_telangana.xlsx')


n3 = df2['latitude'].to_list()
n4 = df2['longitude'].to_list()
n5 = df3['Latitude'].to_list()
n6 = df3['Longitude'].to_list()

d1 = []
d2 = []

def min_haversine_distance(target_point, point_set):
    min_distance = 2000.000 # randam float value
    for point in point_set:
        distance = haversine(target_point, point)
        if distance < min_distance:
            min_distance = distance
    return min_distance


l2 = len(n3)
l3 = len(n5)

for i1 in range(l2):
    b = (n3[i1],n4[i1])
    d1.append(b)


for i3 in range(l3):
    b1 = (n5[i3],n6[i3])
    d2.append(b1)

def get_float_input(prompt):
    while True:
        try:
            user_input = float(input(prompt))
            return user_input
        except ValueError:
            print("Please enter a valid number.")

area = get_float_input("Enter the Super Buildup Area(sqft): ")
type_of_property = get_float_input("Enter the Type of property (eg:- for 3bhk enter 3, for semi-furnished 3 bhk enter 3.5 and for land plots and farm lands enter 0.5): ")
lat = get_float_input("Enter the Latitude (within the range-(17.4,17.56) ): ")
lon = get_float_input("Enter the Longitude (within the range-(78.2,78.6) ): ")
WS = get_float_input("24Hrs Water Supply(enter 1 if present and 0 if not): ")
BE = get_float_input("24Hrs Backup Electricity(enter 1 if present and 0 if not): ")
lift = get_float_input("Lift(enter 1 if present and 0 if not): ")
GC = get_float_input("Gated Community(enter 1 if present and 0 if not): ")
CH = get_float_input("Club House(enter 1 if present and 0 if not): ")
P = get_float_input("Parking(enter 1 if present and 0 if not): ")

given_point = (lat , lon)
result1 = min_haversine_distance(given_point,d1)
result2 = min_haversine_distance(given_point,d2)

print(f"Nearest Railway Station :{result1}")
print(f"Nearest Hospital : {result2}")

print(f"Reciprocal of Nearest Railway Station :{1/result1}")
print(f"Reciprocal of Nearest Hospital : {1/result2}")

rail = [1/result1]
hospital = [1/result2]
k1 = [area]
k2 = [type_of_property]

df1['Area'] = k1
df1['Type_Score'] = k2
df1['Rail_Score'] = rail
df1['Hospital_Score'] = hospital
df1['24Hrs Water Supply'] = WS
df1['24Hrs Backup Electricity'] = BE
df1['Lift'] = lift
df1['Gated Community'] = GC
df1['Club House'] = CH
df1['Parking'] = P

df1.to_excel('test1.xlsx',sheet_name='Sheet1',index=False)