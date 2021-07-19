from django.shortcuts import render
# Sends JSON responses
from django.http import JsonResponse
# Serializes(?) objects into JSON string
from django.core.serializers import serialize
# Turns JSON strings into dictionaries
import json
# Post model
from .models import Post
# View class
from django.views import View
# GetBody
from .helpers import GetBody


# Create your views here.

# Class for Index route
class IndexView(View):
    # Route to get all posts
    def get(self, request):
        # Get all posts
        all = Post.objects.all()
        # Turn object into JSON string
        serialized = serialize("json", all)
        # Turn JSON string into dictionary
        data = json.loads(serialized)
        # Send JSON response and turn off safe(?) to avoid errors
        return JsonResponse(data, safe=False)

    def post(self, request):
        # Get data from the body
        body = GetBody(request)
        print(body)
        # Create a new post
        post = Post.objects.create(battletag=body["battletag"], personal_sr=body["personal_sr"], role=body["role"], lobby_sr=body["lobby_sr"], replay_code=body["replay_code"], details=body["details"])
        # Turn new post into JSON string and dictionary
        data = json.loads(serialize("json", [post]))
        # Send JSON response
        return JsonResponse(data, safe=False)

class SinglePostView(View):
    # Show 1 post
    def get (self, request, id):
        # Get the post
        post = Post.objects.get(id=id)
        # Serialize and turn into dictionary
        data = json.loads(serialize("json", [post]))
        # Send JSON response
        return JsonResponse(data, safe=False)

    # Update turtle
    def put (self, request, id):
        # Get the body
        body = GetBody(request)
        # Update body
        Post.objects.filter(id=id).update(**body)
        # Query for post
        post = Post.objects.get(id=id)
        # Serialize and turn into dictionary
        data = json.loads(serialize("json", [post]))
        # Return JSON response
        return JsonResponse(data, safe=False)

    def delete (self, request, id):
        # Query post
        post = Post.objects.get(id=id)
        # Delete post
        post.delete()
        # Serialize and turn into dictionary
        data = json.loads(serialize("json", [post]))
        # Return JSON response
        return JsonResponse(data, safe=False)

