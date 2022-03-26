input_path = "/home/shubham/Desktop/Gender_Age_p//////.....gfhg//[[rediction/images/2.jpg"
# x = predict_age_and_gender(input_path)
# cv2.imwrite("output_image/output.jpg", frame)
x = input_path.rfind("/")
y = input_path.rfind(".")
z = "output_image/"+input_path[x+1:y]+"-output.jpg"
print(z)
