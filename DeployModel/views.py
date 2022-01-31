from django.http import HttpResponse
from django.shortcuts import render
import joblib

def home(request):
	return render(request,"home.html")

def Liver_Patient_ML(request):
	return render(request,"Liver_Patient_ML.html")
	
def result(request):

	cls = joblib.load('liver_model.pkl')

	lis = []

	#lis.append(request.GET['Age'])
	lis.append(request.GET['Total_Bilirubin'])
	lis.append(request.GET['Direct_Bilirubin'])
	lis.append(request.GET['Alkaline_Phosphotase'])
	lis.append(request.GET['Alamine_Aminotransferase'])
	#lis.append(request.GET['Aspartate_Aminotransferase'])
	lis.append(request.GET['Total_Protiens'])
	lis.append(request.GET['Albumin'])
	lis.append(request.GET['Albumin_and_Globulin_Ratio'])
	#lis.append(request.GET['Gender_Binary'])

	print(lis)

	ans = cls.predict([lis])

	if ans[0] == 1:
		resultAnswer = "Patient can have a liver disease"
	
	else:
		resultAnswer = "Patient might not have a liver disease"
	return render(request,"result.html",{'ans':resultAnswer})