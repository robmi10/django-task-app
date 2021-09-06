from django.http.response import HttpResponse
from django.shortcuts import render
import firebase
from rest_framework import generics
from rest_framework import response
from rest_framework.views import APIView
from .models import Task, Taskitem, User
from .serializers import TaskSerializer, TaskItemSerializer, UserSerializer
import pyrebase
import json

from django.core import serializers
from django.forms.models import model_to_dict
from firebase import firebase
from rest_framework.decorators import api_view
from rest_framework.response import Response
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate({
        "type": "service_account",
        "project_id": "django-react-8a05d",
        "private_key_id": "3dfd8736b2721606e13052042bd6eb65222ada5a",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCV24uIlCC6x5KG\n3CwIRiHjnEgOgbMv2QAP1qT3U4McPFqH/ZragMM14pLKijigSFzz3HIkwsBu1PZp\na7xf6ojkXEYN6yChKtwQolHydGdt/1/eD2TQdzL51i1igDtNLXFJkRFcAIgM52FT\nUm/JZe9kn5uRnt42Dhj4JBRSNysmuHV1KD9qDnbmZjX674o2CEYDD0AivBYP08bO\n7qO6VUt7XsG1v2BBWB1z/3xAgqAUosrFMiGrlJ762TGhQoNYPuE1xK5eqGzUfWrh\nHWOWQ4+bfIKzXTLfloNsmRTsYzy10j83MfN1MWytl3IYwhZezJjQk2YWZNvtQ+34\ngNuAgXRLAgMBAAECggEAB4ehijpPLrNqdGZJvByyBTrMEBaKR2Qy8ZjKbzb+BoQt\n1Fl013fS1zlMQOsTD1KzgPlZrukuPCNtQjzMmVEyka7lQjvHRvHdXuSZE4Kv08Ia\nMhE58pOatx0A6Msir60R3S1x3tqT+3oA1Ov2e/soPTkb2wRNjA/HR2igsMTe4TId\n1tzacXwqwC2qaaMZ3xKu4j9RIImlYkOIVAQooyDemeoTBqZ/THvJqZnVEOHkjcNo\nXPII9IQx8ntkbUmnf8SaoB8XGns7CTwo+R4RTMb8flsyzwSEKZT8m/Z9ZvLxHqYv\nJSDZ18c2ciN1d1BzCrDx5Ssmfn50i9dbrFFB9fUduQKBgQDObRsTkovqpThART0l\nduoeFMMSxpaWvt9KcLTskPh8OZTcj37/6K8KrpJ2rMcRDeoEsudoI7ESdjdRqEW2\nypFhkVdkjCtCPZ8MuNi+RKA7e5ATqEZ4O4DdPuWj91BDERF6qjxC3bT2Ew0hcnVb\n/loDyjsTb8WPcIe1NyQD+M5B9QKBgQC52KdOpLKmqNprnmmWuGOU7bzfPexJSyGH\nhSK7Logh1ZlP1L0TikCUGfggL8Lo/7plfXcfVAYvaO4lQ7ChOBPGVHQwlv3JdH30\nBQxoJiih/oTe0U1d44JkuYx2/Kp8g00HJmuMATWL4JePyuwRl0F7cHUc9bA+PNcA\nkvT1cYm1PwKBgCuiOm/3sSWnSO2k9RjfOvuizd1BJwG0VQSqMEQ1HKE9lq7Mkj7L\n03xBjGoTeXysYUQfAPUtXjeVz3muRRYvWW2zSDLTwi0dU2pgBEirvubz5m+RSVwO\nz910dxwioc+bYwN3yocj0CWXv1XLmO0aJbLZY4VnQe5hDf6LKkzAofClAoGBAJxf\nHk8+pw8xzi51KPTniuqZqqzQJot5CupDbHjA60xEtG4GW10gm7vBqhQy+7YezlBs\n5BlZEqc7i/2Q2gKc846SKv1jXoDuYrg6szjCurerN1NgGs/gCSwFL5pCeJSxydM1\nUZKIxew++mfD3yPh9/gMJI5Mb5G+kU1rWW9Xq/3zAoGBAL6ga6e83wexujQrONOx\nd7XgeNUPe1vLHbwgSYo+F9kudwYC7rqxRQgOOpYyhJChgE7/cgL7S/ugZRcdK4Oq\n5HR0oB4cSSvg0bVfTNZELur3WyMmlweM1Itmv4U4IEQwruEI08qIszxaj83SsY/Y\n0DYeXhbinRSFyMn8NTwZj/uH\n-----END PRIVATE KEY-----\n",
        "client_email": "firebase-adminsdk-ht7re@django-react-8a05d.iam.gserviceaccount.com",
        "client_id": "104351056570933714622",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-ht7re%40django-react-8a05d.iam.gserviceaccount.com"
    })

firebase_admin.initialize_app(cred)

new_firebase = firebase.FirebaseApplication("https://django-react-8a05d-default-rtdb.firebaseio.com/", None)
class UserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TaskView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskItemView(generics.CreateAPIView):
    queryset = Taskitem.objects.all()
    serializer_class = TaskItemSerializer


@api_view(['POST'])
def create_task(request):
    req = request.data
    to_db = json.dumps(req)
    new_parse = json.loads(to_db)
    db = firestore.client()

    print("curr post -> ", new_parse)
    db.collection('task').document(str(new_parse['id'])).set(new_parse)
    
    return HttpResponse(status=200)

@api_view(['PUT'])
def update_task_status(request):
    req = request.data
    to_db = json.dumps(req)
    new_parse = json.loads(to_db)
    db = firestore.client()
    db.collection('task').document(str(new_parse['id'])).update({'completed': new_parse['completed']})
    
    return HttpResponse(status=200)

@api_view(['DELETE'])
def delete_task(request):
    req = request.data

    to_db = json.dumps(req)

    new_parse = json.loads(to_db)
    
    print("new_parse->", new_parse['id'])

    db = firestore.client()

    db.collection('task').document(str(new_parse['id'])).delete()
    return HttpResponse(status=200)


@api_view(['POST'])
def post_taskitem(request):
    req = request.data
    to_db = json.dumps(req)
    new_parse = json.loads(to_db)
    db = firestore.client()

    print("new_parse", new_parse)

    db.collection('task').document(str(new_parse['doc'])).collection('taskitem').document(str(new_parse['id'])).set(new_parse)
    
    return HttpResponse(status=200)

@api_view(['PUT'])
def update_taskitem(request):
    req = request.data
    to_db = json.dumps(req)
    new_parse = json.loads(to_db)
    db = firestore.client()

    print("new_parse", new_parse)

    db.collection('task').document(str(new_parse['doc'])).collection('taskitem').document(str(new_parse['id'])).update({'completed': new_parse['completed']})
    return HttpResponse(status=200)

@api_view(['DELETE'])
def delete_taskitem(request):
    req = request.data

    to_db = json.dumps(req)

    new_parse = json.loads(to_db)
    
    print("new_parse and doc->", new_parse)

    db = firestore.client()

    db.collection('task').document(str(new_parse['doc'])).collection('taskitem').document(str(new_parse['id'])).delete()

    return HttpResponse(status=200)


@api_view(['POST'])
def create_user(request):
    req = request.data
    to_db = json.dumps(req)
    new_parse = json.loads(to_db)
    print("new_parse and doc->", new_parse)
    db = firestore.client()
    db.collection('user').document(str(new_parse['username'])).set(new_parse)
    return HttpResponse(status=200)

@api_view(['POST'])
def login_user(request):
    req = request.data
    to_db = json.dumps(req)
    new_parse = json.loads(to_db)
    print("new_parse and doc->", new_parse)
    db = firestore.client()
    db.collection('user').document(str(new_parse['username'])).get()
    return HttpResponse(status=200)
