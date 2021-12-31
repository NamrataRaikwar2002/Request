import os
import requests
import json

if os.path.exists("courses.json"):
    pass
else:
    file=open("courses.json","w")
    file.close()
def request():
    req=requests.get("http://saral.navgurukul.org/api/courses")
    with open("courses.json","w") as file:
        dic=json.loads(req.text)
        json.dump(dic,file,indent=4)
    with open("courses.json","r") as read1:
        read2=json.load(read1)
        sno=1
        id=[]
        for i in read2["availableCourses"]:
            print(sno,i["name"],":-",i["id"])
            id.append(i["id"])
            sno+=1
            
        course_id=int(input("enter your serial number:"))
   
        req2=requests.get("http://saral.navgurukul.org/api/courses/"+str(id[course_id-1])+"/exercises")
        course_detail=req2.json()
        
        detail_count=1
        slug=[]
        for name in course_detail["data"]:
            print(detail_count,".", name["name"])
            slug.append(name["slug"])
            detail_count+=1
        slug_input=int(input("enter slug number:"))
        slug_api=requests.get("http://saral.navgurukul.org/api/courses/"+str(course_id)+"/exercise/getBySlug?slug="+slug[slug_input])
        slug_json=slug_api.json()
        print(slug_json["content"])
        print("'UP':-for previous content")
        print("'NEXT':-for previous content")
        print("'SAME':-for previous content")
        for s in range(len(slug)):
            step=input("enter your choice: ")
            if step=="up":
                slug_api=requests.get("http://saral.navgurukul.org/api/courses/"+str(course_id)+"/exercise/getBySlug?slug="+slug[slug_input-1])
                up_json=slug_api.json()
                print(slug_input-1,up_json["content"])
            elif step=="next":
                slug_api=requests.get("http://saral.navgurukul.org/api/courses/"+str(course_id)+"/exercise/getBySlug?slug="+slug[slug_input+1])
                next_json=slug_api.json()
                print(slug_input+1,next_json["content"])
            elif step=="same":
                slug_api=requests.get("http://saral.navgurukul.org/api/courses/"+str(course_id)+"/exercise/getBySlug?slug="+slug[slug_input])
                same_json=slug_api.json()
                print(slug_input,same_json["content"])
            elif step=="exit":
                request()
request()
        


