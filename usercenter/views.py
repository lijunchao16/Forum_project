# coding: utf-8
from django.shortcuts import render,render_to_response,redirect
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib import messages
from django.template import RequestContext
from django.http import HttpResponse
import uuid,datetime,os
from  models import ActivateCode,UserProfile
from myforum.settings import STORAGE_PATH,USERRES_URLBASE
from random import randint
# Create your views here.
def register(request):
    error = ''
    if request.method == 'GET':
        return render_to_response('usercenter_register.html',{},context_instance=RequestContext(request))
    else:
        username = request.POST['username'].strip()
        email = request.POST['email'].strip()
        password = request.POST['password'].strip()
        re_password = request.POST['re_password'].strip()

        if not username or not password or not email:
            error = u'任何字段都不能为空'
        if password != re_password:
            error = u'密码不一致'
        if User.objects.filter(username=username).count() > 0:
            error = u'用户已存在'
        if not error:
            user = User.objects.create_user(username=username,email=email,password=password)
            user.is_active = False
            user.save()
            profile = UserProfile(owner=user,avatar="http://res.myform.com/mmexport1445957752296.jpg")
            profile.save()

            new_code = str(uuid.uuid4()).replace("-","")
            expire_time = datetime.datetime.now() + datetime.timedelta(days=2)
            code_record = ActivateCode(owner=user,code=new_code,expire_timestamp=expire_time)
            code_record.save()

            activate_link = "http://%s%s" % ((request.get_host()),reverse("usercenter_activate",args=[new_code]))
            send_mail(u'激活邮件',u'您的激活链接为: %s' % activate_link,"895277169@qq.com",[email],fail_silently=False)
        else:
            return render_to_response("usercenter_register.html",{"error":error},context_instance=RequestContext(request))
        return redirect('login')

def activate(request,code):
    query = ActivateCode.objects.filter(code=code,expire_timestamp__gte=datetime.datetime.now())
    if query.count()>0:
        code_record = query[0]
        code_record.owner.is_active = True
        code_record.owner.save()
        return HttpResponse(u"激活成功")
    else:
        return HttpResponse(u'激活失败')

def uploadavatar(request):
    profile = UserProfile.objects.get(owner=request.user)
    if request.method == 'GET':
        return render_to_response('uploadavatar.html',{'profile':profile},context_instance=RequestContext(request))
    else:
        avatar_file = request.FILES.get("avatar",None)
        if avatar_file.size > 1048576:
            messages.add_message(request,messages.WARNING,u'图像大小不能超过2M')
            return render_to_response('uploadavatar.html',{'profile':profile},context_instance=RequestContext(request))
        temp_name = avatar_file.name
        while UserProfile.objects.filter(avatar=USERRES_URLBASE + temp_name).count() > 0:   # 判断是否有重名图像存在，如果有时加随机数改名
            temp_name = str(randint(1,100)) + temp_name
            if not UserProfile.objects.filter(avatar=USERRES_URLBASE + temp_name).count() > 0:
                break
        filr_path = os.path.join(STORAGE_PATH,temp_name)     # 存储文件到nginx
        with open(filr_path,'wb+')as destination:
            for chunk in avatar_file.chunks():
                destination.write(chunk)
        url = "%s%s" % (USERRES_URLBASE,temp_name)
        profile.avatar = url
        profile.save()
        return HttpResponse(u"上传成功")

        # messages.add_message(request,messages.WARNING,u'存在一个相同名称的头像，请修改图片名称')
        # return render_to_response('uploadavatar.html',{'profile':profile},context_instance=RequestContext(request))













