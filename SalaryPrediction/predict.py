from sklearn.linear_model import LinearRegression
import pandas as pd
import cgi

form = cgi.FieldStorage()
per_10 = float(form.getvalue('box_1'))
per_12 = float(form.getvalue('box_2'))
collegeTier = int(form.getvalue('box_3'))
collegeCgpa = float(form.getvalue('box_4'))
engMarks = int(form.getvalue('box_5'))

dataset = pd.read_excel('train.xlsx')

trainData = dataset[['10percentage', '12percentage','CollegeTier','collegeGPA','English']]
target = dataset['Salary']

reg = LinearRegression()

reg.fit(trainData, target)
# reg.predict([[85.45,90.1,1,76,690]])
pred = reg.predict([[per_10, per_12, collegeTier, collegeCgpa, engMarks]])

print("Content-type:text/html\r\n\r\n")
print("""
<html>
<head>
<title>Machine Learning</title>
</head>
<body>
<h1>Your Predicted Salary is : {}</h1>
</body>
</html>
""".format(int(pred)))
