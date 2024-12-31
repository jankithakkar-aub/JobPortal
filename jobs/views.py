from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Company, JobPost
from .forms import CompanyRegistrationForm, JobPostForm

@login_required
def dashboard(request):
    """
    View to register a company. A user can register only one company.
    """
    if hasattr(request.user, "company"):
        return redirect("job_list") #If already registered then redirect it to job_list
    
    if request.method == "POST":
        form = CompanyRegistrationForm(request.POST)
        if form.is_valid():

            #Create and save the company instance
            company = form.save(commit=False) #Do not save yet to avoid the not null constraint error

            #Assign the current user to the company
            company.user = request.user
            company.save() #Now save the company
            return redirect("job_list")
        
    else:
        form = CompanyRegistrationForm()

    return render(request, "dashboard.html", {"form": form})

@login_required
def job_list(request):
    """
    View to list all job posts created by user's company
    """
    company = get_object_or_404(Company, user=request.user) #Get the current user's company
    job_posts = JobPost.objects.filter(company=company) #Get all the job posts related to the company retrieved

    return render(request, "job_list.html", {"job_posts": job_posts})

@login_required
def job_create(request):
    """
    View to create the job post
    """
    company = get_object_or_404(Company, user=request.user)
    if request.method == "POST":
        form = JobPostForm(request.POST)
        if form.is_valid():

            #Create and save the job post
            job_post = form.save(commit=False) #Do not save yet to avoid the not null constraint error
            job_post.company = company #Assign the foreign key
            job_post.save() #Now save it
            return redirect("job_list")
    
    else:
        form = JobPostForm()

    return render(request, "job_create.html", {"form": form})

@login_required
def job_edit(request, job_post_id):
    """
    View to update an job post which exists
    """
    job_post = get_object_or_404(JobPost, id=job_post_id)

    if job_post.company.user != request.user:
        return redirect("job_list")
    
    if request.method == "POST":
        form = JobPostForm(request.POST, instance=job_post) #Helps to pre-propulate teh form as no new form is being created
        if form.is_valid():
            form.save()
            return redirect("job_list")
    
    else:
        form = JobPostForm(instance=job_post)

    return render(request, "job_edit.html", {"form":form})

@login_required
def job_delete(request, job_post_id):
    """
    View to delete a job post which exists
    """
    job_post = get_object_or_404(JobPost, id=job_post_id)

    if job_post.company.user != request.user:
        return redirect("job_list")
    
    if request.method == "POST":
        job_post.delete() #Delete the respective job post
        return redirect("job_list")
    
    return render(request, "job_delete.html", {"job_post": job_post})



