from django.shortcuts import render

# Create your views here.
def abc(request):
    return render(
        request,
        "abc.html"
    )

def getdata(request):
    # 서버에서 받는 값
    num1 = request.GET.get("var1")
    num2 = request.GET.get("var2")

    print(int(num1) + int(num2))

    # 서버 -> 클라이언트
    context = { 'key1': int(num1) + int(num2) }

    return render(
        request,
        "getdata.html",
        context  # 해당 html 안에 context 라고하는 딕셔너리가 들어가게 됨
    )

def getpostpage(request):
    return render(
        request,
        "sendpost.html"
    )

def postdata(request):
    # 서버에서 받는 값
    num1 = request.POST.get("var1")
    num2 = request.POST.get("var2")

    print(int(num1) + int(num2))

    # 서버 -> 클라이언트
    context = {'key1': int(num1) + int(num2)}

    return render(
        request,
        "sendpost.html",
        context
    )