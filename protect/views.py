from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from gevent import os
from protect.models import Member

def home(request) :
    return render(request, 'protect/home.html', {})

def join(request) :
    if request.method == 'GET' :
        return render(request, 'protect/join.html', {})

    else :
        user_id = request.POST['user_id']
        user_pw = request.POST['user_pw']
        user_name = request.POST['user_name']
        user_phonenumber = request.POST['user_phonenumber']
        user_address = request.POST['user_address']
        
        try :
            Member(user_id=user_id, user_pw=user_pw, user_name=user_name,
                   user_phonenumber=user_phonenumber, user_address=user_address).save()
            print(user_id) # cmd창에 출력
            return HttpResponse('회원가입 완료')
        except ValueError:
            return HttpResponse('내용을 전부 작성해주세요')

def login(request) :
    if request.method == 'GET' :
        return render(request, 'protect/login.html', {})
    
    else :
        user_id = request.POST['user_id']
        user_pw = request.POST['user_pw']
        
        try :
            Member.objects.get(user_id=user_id, user_pw=user_pw)
        except Member.DoesNotExist :
            return HttpResponse('로그인 실패')
        else : # 정상 로그인(세션값 저장 필수!!)
            request.session['user_id'] = user_id  # ' '안의 공간에 user_id의 값을 집어넣음(session에 보관)
            return HttpResponse('로그인 완료')

def logout(request) :
    del request.session['user_id']
    # return render(request, 'protect/home.html', {})
    return redirect('/home') # home이라는 주소에 다시 뿌려주라는 뜻

def enrollment(request) :
    if request.method == 'GET' :
        return render(request, 'protect/enrollment.html', {})

    else :
        upload_file = request.FILES['enroll_file']

        login_id = request.session['user_id']
        try:
            os.mkdir('C:\\Users\\어다희\\Desktop\\임치DB\\' + login_id)  # login_id라는 디렉토리 생성
        except FileExistsError:
            pass

        with open('C:\\Users\\어다희\\Desktop\\임치DB\\' + login_id + '\\' + upload_file.name, 'wb') as file:  # 껍데기 파일을 만든 것!!
            for chunk in upload_file.chunks():  # chunks가 호출되면 파일의 크기가 얼마든 다 쪼개냄
                file.write(chunk)  # 그걸 for문으로 청크청크해서 write해줌(장고 공식문서에 나와있는 파일 업로드 하는 코드)

        # return redirect('/home/enrollment')
        return JsonResponse({'result': 'ok'})

def certificate(request) :
    return render(request, 'protect/certificate.html', {})

def verification(request) :
    return render(request, 'protect/verification.html', {})

def contract(request) :
    return render(request, 'protect/contract.html', {})

