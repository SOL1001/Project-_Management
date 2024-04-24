from django.db import models

# Create your models here.
class Employee(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    phoneNumber = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)

    def __str__(self) :
        return self.fname
    
class Account(models.Model):
    Employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    username = models.CharField(max_length=20)   
    password = models.CharField(max_length=20)
    accounttype = models.CharField(max_length=20)

    def __str__(self) :
        return f'{self.Employee.fname} {self.accounttype}'
    
class ProjectUpload(models.Model) :
    # Employee = models.ForeignKey(Employee, on_delete=models.PROTECT)
    researcherName = models.CharField(max_length=20)
    researchTitle = models.CharField(max_length=20)
    areaOfStudy = models.CharField(max_length=20)
    Institute = models.CharField(max_length=20, default='BahirDar')
    yearOfStudy = models.IntegerField()
    budget = models.DecimalField(max_digits=15, decimal_places = 2)
    description = models.TextField()
     
    def __str__(self) :
        return f' {self.researcherName} {self.researchTitle} {self.areaOfStudy} {self.yearOfStudy} '
    
class Comment(models.Model) :
      project_upload = models.ForeignKey(ProjectUpload, on_delete=models.CASCADE, default=1)
      commentDate = models.DateTimeField(auto_now_add=True)
      commentText = models.TextField()
       
      def __str__(self):
        return f'{self.commentText}  {self.commentDate}'