from django.core.files.storage import default_storage
from django.shortcuts import render
import age_and_gender_detection as detect


def index(request):
    if request.method == "POST":
        #
        # Django image API
        #
        file = request.FILES["imageFile"]
        file_name = default_storage.save(file.name, file)
        file_url = default_storage.path(file_name)
        predicted_data = detect.predict_age_and_gender(file_url)
        context = {"data": predicted_data}
        print(file_url)
        print(predicted_data)
        return render(request, "output.html", context)
    else:
        return render(request, "index.html")
