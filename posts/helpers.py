import json
def GetBody(request):
    # decode request into unicode string
    unicode = request.body.decode("utf-8")
    # turn unicode string into dictionary
    return json.loads(unicode)
