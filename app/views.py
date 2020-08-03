from django.shortcuts import render, redirect
from .models import contactdetails,educ, workexp,skills,extrafield
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.views.generic import ListView  ,DetailView, UpdateView ,DeleteView
from django.utils.decorators import method_decorator
from braces.views import CsrfExemptMixin
from django.views.decorators.cache import never_cache
from django.core import serializers
from .forms import Educationdetails,contactdetailsform,jobform,skilldetails, Extrafieldform
from django.urls import reverse_lazy





@csrf_exempt
def firstpage (request):
	

	form = contactdetailsform(request.POST or None)

	return render(request,'template.html',{'form':form})



@csrf_exempt
def edu(request):
	form = Educationdetails(request.POST or None)
	if not request.POST.get('full_name'):
		
		return render(request,'Tell us about your education.html',{'form':form})
	else:
		author = request.user
		resume = request.POST.get('resume_name')
		full_name = request.POST.get('full_name',False)
		position = request.POST.get('position',False)
		city = request.POST.get('city',False)
		state = request.POST.get('state',False)
		zipcode = request.POST.get('zipcode',False)
		email = request.POST.get('email',False)
		phone = request.POST.get('phone',False)
		personal_profile = request.POST.get('personal_profile',False)
		contactx=contactdetails.objects.create(author=author,resume_name=resume,full_name=full_name, position=position, city=city,state=state,zipcode=zipcode ,email=email,personal_profile=personal_profile,phone=phone)
		
		return render(request,'Tell us about your education.html',{'form':form})





class JobView(ListView):

	def get (self,request):
		msg = request.session.get ('msg',False)
		if(msg):
			del (request.session['msg'])
		Work = workexp.objects.filter(author=request.user);
		return render (request,'joblist.html',{'object_list':Work})


	def post(self,request):
		author = request.user
		resume_name=request.POST.get('resume_name')
		job_title = request.POST.get('job_title',False)
		employer = request.POST.get('employer',False)
		city = request.POST.get('city',False)
		state = request.POST.get('state',False)
		jobdesc = request.POST.get('jobdesc',False)
		something=workexp.objects.create(author=author,resume_name=resume_name,job_title=job_title ,employer=employer ,city=city, state=state ,jobdesc=jobdesc)
		#return render(request,'skills.html')
		nothing = serializers.serialize ('json',[something])
		request.session['msg']=nothing
		return redirect(request.path)


class EducationView(ListView):

	def get (self,request):
		msg = request.session.get ('msg',False)
		if(msg):
			del (request.session['msg'])
		Educ = educ.objects.filter(author=request.user);
		return render (request,'educationlist.html',{'object_list':Educ})


	def post(self,request):
		author = request.user
		resume_name=request.POST.get('resume_name')
		school_name = request.POST.get('school_name',False)
		school_location = request.POST.get('school_location',False)
		Degree = request.POST.get('Degree',False)
		CGPA = request.POST.get('CGPA',False)
		Field_of_Study = request.POST.get('Field_of_Study',False)
		Expected_year_of_grad = request.POST.get('Expected_year_of_grad',False)
		contactx = educ.objects.create(author=author,school_name=school_name,school_location=school_location,Degree=Degree,CGPA=CGPA,
			Field_of_Study=Field_of_Study,Expected_year_of_grad=Expected_year_of_grad)
		contactx2 = serializers.serialize ('json',[contactx])
		request.session['msg']=contactx2
		return redirect(request.path)




class UpdatepostViewjob(UpdateView):
	model = workexp
	template_name = 'updatepost.html'
	fields = '__all__'


class Deletepostviewjob(DeleteView):
	model = workexp
	template_name = 'delete_post.html'
	success_url = reverse_lazy('job')


class UpdatepostView(UpdateView):
	model = educ
	template_name = 'updatepost.html'
	fields = ['school_name','school_location','Degree','CGPA','Field_of_Study','Expected_year_of_grad']



@csrf_exempt
def educrev (request):
	return HttpResponseRedirect('/addr/cd/login')



@csrf_exempt
def job345(request):
	form = jobform(request.POST or None)
	return render(request,'about job.html',{'form':form})
	#return HttpResponseRedirect('/login/')



def formfunction(request):
	form = Educationdetails(request.POST or None)
	return render (request,'updatepost.html',{'form':form})




class Deletepostview(DeleteView):
	model = educ
	template_name = 'delete_post.html'
	success_url = reverse_lazy('education')


#Tejaswini****************************************************
@csrf_exempt
def home(request):
	
	#c_items = contactdetails.objects.all()
	#length = contactdetails.objects.all().count()
	#print(length)
	contact2 = contactdetails.objects.filter(author=request.user)
	contacte2 = educ.objects.filter(author=request.user)
	job2 = workexp.objects.filter(author=request.user)
	skill2=skills.objects.filter(author=request.user)
	adds2 = extrafield.objects.filter(author=request.user)
	contact1 = contactdetails.objects.all()
	contacte1 = educ.objects.all()
	job1 = workexp.objects.all()
	skill1=skills.objects.all()
	adds = extrafield.objects.all()
	#return render(request,'home.html',{'c_items':c_items,'contacte1':contacte1,'job1':job1,'skills':skill1})
	#if not request.POST.get('field_name'):
	#	return render(request,'home.html',{'i':contact1,'contacte1':contacte1,'job1':job1,'skills':skill1,'adds':adds})

	#else:
	if not request.POST.get('field_name'):
		pass
	else:
		author = request.user
		print(author)
		#resume_name=request.POST.get('resume_name')
		#print(resume_name)
		field_name= request.POST.get('field_name',False)
		explanation= request.POST.get('explanation',False)
		xyz = extrafield.objects.create(author=author,field_name=field_name,explanation=explanation)
	adds1 = extrafield.objects.all()
	return render(request,'home.html',{'i':contact2,'contacte1':contacte2,'job1':job2,'skills':skill2,'adds':adds2})
	#return render (request,'Extra_field')

class DeleteEFview(DeleteView):
	model = extrafield
	template_name = 'delete_post.html'
	success_url = reverse_lazy('extrafi')

class UpdateEFView(UpdateView):
	model = extrafield
	template_name = 'updateef.html'
	fields = ['field_name','explanation']

class ExtrafieldView(ListView):

	def get (self,request):
		msg = request.session.get ('msg',False)
		if(msg):
			del (request.session['msg'])
		ExtraField = extrafield.objects.filter(author=request.user);
		return render (request,'extrafieldlist.html',{'object_list':ExtraField})


	def post(self,request):
		author = request.user
		print(author)
		resume_name=request.POST.get('resume_name')
		print(resume_name)
		
		field_name=request.POST.get('field_name',False)
		explanation=request.POST.get('explanation',False)
		contactx = extrafield.objects.create(author=author,field_name=field_name,explanation=explanation)
		contactx2 = serializers.serialize ('json',[contactx])
		request.session['msg']=contactx2
		return redirect(request.path)


@csrf_exempt
def skillsadd(request):
	skill = request.POST.get('skill',False)
	something2= skills.objects.create(author=author,resume_name=resume_name,skill=skill)
	return HttpResponseRedirect('addr/cd/login/next/job')



@csrf_exempt
def addonstest(request):
	form = Extrafieldform(request.POST or None)
	if form.is_valid():
		form.save()
		form = Extrafieldform()
	if not request.POST.get('skill'):
		return render(request,'Extra_field.html',{'form':form})
	else:
		skill= request.POST.get('skill',False)
		xyz = skills.objects.create(author=author,resume_name=resume_name,skill=skill)
		return render (request,'Extra_field.html',{'form':form})
@csrf_exempt
def addonemoreaddon(request):

	#field_name= request.POST.get('field_name',False)
	#explanation= request.POST.get('explanation',False)
	#xyz = extrafield.objects.create(field_name=field_name,explanation=explanation)
	return HttpResponseRedirect('/addr/cd/logedin/login/next/job/skill/')

	#Tejaswini*************************************************************



#BELOW VIEWS ADDED BY SIRI  (import necesaary views )


@csrf_exempt
def skilledu(request):

	form = skilldetails(request.POST or None)

	if not request.POST.get('full'):
		
		return render(request,'skills.html',{'form':form})
	else:
		skills = request.POST.get('full',False)
		
		contactx=contactdetails.objects.create(author=author,resume_name=resume_name,skills=skills)
		contactx2 = serializers.serialize ('json',[contactx])
		return render(request,'skills.html',{'form':form})



class SkillsView(ListView):

	def get (self,request):
		msg = request.session.get ('msg',False)
		if(msg):
			del (request.session['msg'])
		skills2 = skills.objects.filter(author=request.user);
		return render (request,'skilllist.html',{'object_list':skills2})


	def post(self,request):
		
		skill = request.POST.get('skill',False)
		author = request.user
		#resume_name=request.POST['resume_name']
		contactx = skills.objects.create(author=author,skill=skill)
		contactx2 = serializers.serialize ('json',[contactx])
		request.session['msg']=contactx2
		return redirect(request.path)


class skillUpdatepostView(UpdateView):
	model = skills
	template_name = 'updatepost.html'
	fields = ['skill']



@csrf_exempt
def skillseducrev (request):
	return HttpResponseRedirect('addr/cd/login/next/skills')


@csrf_exempt
def skillsjob345(request):
	form = jobform(request.POST or None)
	return render(request,'skilllist.html')
	#return HttpResponseRedirect('/login/')


def formfunction(request):
	form = skills(request.POST or None)
	return render (request,'updatepost.html',{'form':form})


class skillDeletepostview(DeleteView):
	model = skills
	template_name = 'delete_post.html'
	success_url = reverse_lazy('skillsview')



from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,CreateView
from .models import Resume_No,Details
from .forms import Rform

class HomeView(ListView):
    model = Resume_No
    template_name = 'homelogin.html'

class addview(CreateView):
    model = Resume_No
    form_class = Rform
    template_name = 'addresume.html'
    #fields = ('name',)

class adddview(CreateView):
	model=Details
	template_name='adddetail.html'
	fields='__all__'
		





from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
from django.template import Context


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    context=Context(context_dict)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None



class viewPDF(View):
	def get(self , request ,*args , ** kwargs):
		contact1 = contactdetails.objects.filter(author=request.user)
		contacte1 = educ.objects.filter(author=request.user)
		job1 = workexp.objects.filter(author=request.user)
		skill1=skills.objects.filter(author=request.user)
		adds = extrafield.objects.filter(author=request.user)

		data={'i':contact1,'contacte1':contacte1,'job1':job1,'skills':skill1,'adds':adds}
		pdf = render_to_pdf('home.html',data)
		return HttpResponse(pdf,content_type='application/pdf')



class DownloadPDF(View):
	def get(self,request, *args , **kwargs):
		contact1 = contactdetails.objects.filter(author=request.user)
		contacte1 = educ.objects.filter(author=request.user)
		job1 = workexp.objects.filter(author=request.user)
		skill1=skills.objects.filter(author=request.user)
		adds = extrafield.objects.filter(author=request.user)

		data={'i':contact1,'contacte1':contacte1,'job1':job1,'skills':skill1,'adds':adds}
		pdf = render_to_pdf('home.html',data)
		return HttpResponse(pdf,content_type='application/pdf')
		filename = "Invoice_%s.pdf"%("1234512321")
		response['Content-Disposition'] = content
		return response

def index(request):
	context = {}
	return render (request,'home.html',context)



def homer(request):
	return render(request,'index_new.html')










#import os

#from weasyprint import HTML

#from django.template import Template, Context
#from django.http import HttpResponse 


#def generate_pdf(self, report_id):

        # Render HTML into memory and get the template firstly
      #  template_file_loc = os.path.join(os.path.dirname(__file__), os.pardir, 'templates', 'the_template_pdf_generator.html')
      # template_contents = read_all_as_str(template_file_loc)
       # render_template = Template(template_contents)

        #rendering_map is the dict for params in the template 
      #  render_definition = Context(rendering_map)
      #  render_output = render_template.render(render_definition)

        # Using Rendered HTML to generate PDF
      #  response = HttpResponse(content_type='application/pdf')
      #  response['Content-Disposition'] = 'attachment; filename=%s-%s-%s.pdf' % \
     #                                     ('topic-test','topic-test', '2018-05-04')
        # Generate PDF
     #   pdf_doc = HTML(string=render_output).render()
    #    pdf_doc.pages[0].height = pdf_doc.pages[0]._page_box.children[0].children[
    #        0].height  # Make PDF file as single page file 
    #    pdf_doc.write_pdf(response)
   #     return response

#def read_all_as_str(self, file_loc, read_method='r'):
  #  if file_exists(file_loc):
 #       handler = open(file_loc, read_method)
 #       contents = handler.read()
 #       handler.close()
#       return contents
#    else:
#        return 'file not exist'  




#def export_to_pdf(request, tip_id):
#    options = {
#       'page-size': 'A4',
#        'margin-top': '0.55in',
#        'margin-right': '0.55in',
 #       'margin-bottom': '0.55in',
 #       'margin-left': '0.55in',
  #      'encoding': "UTF-8",
  #      # any other wkhtmltopdf options
  #  }
  #  contact1 = contactdetails.objects.filter(author=request.user)
	#	contacte1 = educ.objects.filter(author=request.user)
	#	job1 = workexp.objects.filter(author=request.user)
	#	skill1=skills.objects.filter(author=request.user)
	#	adds = extrafield.objects.filter(author=request.user)

	#	data={'i':contact1,'contacte1':contacte1,'job1':job1,'skills':skill1,'adds':adds}

    #content = render_to_string(
    #    'home.html', {
    #       'contents': data
    #    }
    #)

    #pdf = pdfkit.PDFKit(content, "string", options=options).to_pdf()

    #response = HttpResponse(pdf)
    #response['Content-Type'] = 'application/pdf'
    # change attachment to inline if you want open file in browser tab instead downloading
    #response['Content-disposition'] = 'inline;filename={}.pdf'.format(your_filename)

    #return response



