from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .forms import GalleryForm
from .models import GalleryModel,GalleryModel2,GalleryModel3
from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
from httplib2 import Http
from django.shortcuts import redirect
from apiclient.http import MediaIoBaseUpload
from apiclient.http import MediaFileUpload
from io import BytesIO
from PIL import Image
scopes = ['https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('token.json', scopes)
import math
http_auth = credentials.authorize(Http())


def convertTowebp(im):
    with BytesIO() as f:
        im.save(f, format='webp')
        return f.getvalue()
# Create your views here.

def submit(request):
    context = {}
    if request.method == "POST":
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            img1 = form.cleaned_data.get("image_field")
            nme=img1.name
            url="https://drive.google.com/uc?export=view&id="
            folder_id = '1aDc1Md6zn-gNMqRX4ii4tnt8BFCcNhxo'
            file_metadata = {
            'name': nme+'.webp',
            'parents': [folder_id]
             }
            ima=Image.open(img1)
            img=convertTowebp(ima)
            img=BytesIO(img)
            drive_service = build('drive', 'v3', http=http_auth)
            media = MediaIoBaseUpload(img,
                                    mimetype='image/webp', resumable=True)
            file = drive_service.files().create(body=file_metadata,
                                                 media_body=media,
                                                 fields='id').execute()
            permission = {'type': 'anyone',
              'value': 'anyone',
              'role': 'reader'}
            file_id=file.get('id')
            drive_service.permissions().create(fileId=file_id,body=permission).execute()
            link=url+file_id
            obj = GalleryModel.objects.create(
                                 link=link
                                 )
            obj.save()
            print(obj)
            return redirect('index')
    else:
        form = GalleryForm()
    context['form']= form
    return render(request, "submit.html", context)


def index(request):
    post=GalleryModel.objects.all()
    # for i in post:
    #     j=str(i.link)
    #     j=j.replace("https://lh3.google.com/u/0/d/","https://drive.google.com/uc?export=view&id=")
    #     i.link=j
    #     i.save()
    return render(request,'index.html',{'post':post,'s':'submit'})

def index2(request):
    post=GalleryModel2.objects.all()
    return render(request,'index.html',{'post':post,'s':'submit2'})

def index3(request):
    post=GalleryModel3.objects.all()
    return render(request,'index.html',{'post':post,'s':'submit3'})

def submit2(request):
    context = {}
    if request.method == "POST":
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            img1 = form.cleaned_data.get("image_field")
            url="https://lh3.google.com/u/0/d/"
            folder_id = '1aDc1Md6zn-gNMqRX4ii4tnt8BFCcNhxo'
            file_metadata = {
            'name': 'photo.jpg',
            'parents': [folder_id]
             }
            drive_service = build('drive', 'v3', http=http_auth)
            media = MediaIoBaseUpload(img1,
                                    mimetype='image/jpeg', resumable=True)
            file = drive_service.files().create(body=file_metadata,
                                                 media_body=media,
                                                 fields='id').execute()
            permission = {'type': 'anyone',
              'value': 'anyone',
              'role': 'reader'}
            file_id=file.get('id')
            drive_service.permissions().create(fileId=file_id,body=permission).execute()
            link=url+file_id
            obj = GalleryModel2.objects.create(
                                 link=link
                                 )
            obj.save()
            print(obj)
            return redirect('index2')
    else:
        form = GalleryForm()
    context['form']= form
    return render(request, "submit.html", context)

def submit3(request):
    context = {}
    if request.method == "POST":
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            img1 = form.cleaned_data.get("image_field")
            nme=img1.name
            url="https://drive.google.com/uc?export=view&id="
            folder_id = '1aDc1Md6zn-gNMqRX4ii4tnt8BFCcNhxo'
            file_metadata = {
            'name': nme+'.webp',
            'parents': [folder_id]
             }
            ima=Image.open(img1)
            x, y = ima.size
            print(x,y)
            if(x>1600):
                x2=1600
                y2=math.floor((1600/x)*y)
                print(x2,y2)
                #x2, y2 = math.floor(x-50), math.floor(y-20)
                ima = ima.resize((x2,y2),Image.Resampling.LANCZOS)
            img=convertTowebp(ima)
            img=BytesIO(img)
            drive_service = build('drive', 'v3', http=http_auth)
            media = MediaIoBaseUpload(img,
                                    mimetype='image/webp', resumable=True)
            file = drive_service.files().create(body=file_metadata,
                                                 media_body=media,
                                                 fields='id').execute()
            permission = {'type': 'anyone',
              'value': 'anyone',
              'role': 'reader'}
            file_id=file.get('id')
            drive_service.permissions().create(fileId=file_id,body=permission).execute()
            link=url+file_id
            obj = GalleryModel3.objects.create(
                                 link=link
                                 )
            obj.save()
            print(obj)
            return redirect('index3')
    else:
        form = GalleryForm()
    context['form']= form
    return render(request, "submit.html", context)