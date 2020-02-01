salaries=['$876,001','$543,903','$2453,896']
salary1=[]
for salary in salaries:
    s=salary[1:]
    s1=s.split(',')
    s2="".join(s1)
    s3=int(s2)
    salary1.append(s3)
    print(s3)
