# _*_ coding:utf-8 _*_
import requests
import re,time
import os


pattern = re.compile('<input type=.hidden. name=.lt.*?value=.(.*?).>')
pattern2 = re.compile('<input type=.hidden. name=.execution.*?value=.(.*?).>')
pattern3 = re.compile('id=.expandable_branch_.*?><a title=.(.*?)href=.(.*?).>.*?')
pattern4 =re.compile('.*?href=(.https://my.stu.edu.cn/courses/campus/mod/resource/view.php.*?).>.img.*?/f/(.*?).24.*?instancename.>(.*?)<.*?')



def download_file(url2,pathb):
    r2_file = s.get(url2)
    content2_file = r2_file.text
    position1 = content2_file.find('section-0')
    position2 = content2_file.find('id="region-pre"')
    content2_file =content2_file[position1:position2]
    items4 = re.findall(pattern4,content2_file)

    for item_file in items4:               
        print item_file[2],item_file[1],item_file[0]
        print u'开始下载'
        print item_file[2]

        name = item_file[2].replace('*','_').replace('/','_').replace('\\','_').replace(':','_').replace('?','_').replace('"','_').replace('<','_').replace('>','_').replace('|','_')
        print name

        if (item_file[1]=='powerpoint'):
            name = name + '.ppt'
        if (item_file[1]=='spreadsheet'):
            name = name + '.xls'
        if (item_file[1]=='document'):
            name = name + '.doc'
        if (item_file[1]=='pdf'):
            name = name + '.pdf'
        if (item_file[1]=='jpeg'):
            break
        if (item_file[1]=='archive'):
            name = name +'.rar'
        
        new_url = item_file[0][1:]

        filepath= pathb
        path =  filepath + name
        if not os.path.exists(path):            
        
            inword = s.get(new_url)
            with open(path,'wb') as code :
                code.write(inword.content)
                time.sleep(1)
            print u'下载成功'
        else:
            print u'文件存在，不再下载'


url = 'https://sso.stu.edu.cn/login'
url3 = 'https://my.stu.edu.cn/courses/campus/my'    

s = requests.Session()
te = s.get(url)
findit = te.text
items = re.findall(pattern,findit)
items2 = re.findall(pattern2,findit)
for item in items:
    lt=item[0:len(item)-2].encode()   
for item in items2:    
    el=item[0:4].encode()
headers={
         'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
         }
postData={'_eventId': 'submit',
          'execution': el,
          'lt':lt,
          'username':'15ytli3',          
          'password':'Doctor.Zen'}
s.post(url,data= postData,headers=headers)


r=s.get(url3)

content = r.text

items3 = re.findall(pattern3,content)
for item in items3:
    logn=len(item[0])-2
    item_change = item[0][8:logn].replace('*','_').replace('/','_').replace('\\','_').replace(':','_').replace('?','_').replace('"','_').replace('<','_').replace('>','_').replace('|','_')

    if os.path.exists('E:/STU_Courseware/'):
        if os.path.exists('E:/STU_Courseware/'+'/'+item[0][1:7]):
            if os.path.exists('E:/STU_Courseware/'+'/'+item[0][1:7]+'/'+item_change):
                print ' '
            else :
                os.mkdir(os.path.join('E:/STU_Courseware/'+'/'+item[0][1:7]+'/'+item_change))
            
        else:
            os.mkdir(os.path.join('E:/STU_Courseware/'+'/'+item[0][1:7]))
            os.mkdir(os.path.join('E:/STU_Courseware/'+'/'+item[0][1:7]+'/'+item_change))
                        
    else:
        os.mkdir('E:/STU_Courseware/')
        os.mkdir(os.path.join('E:/STU_Courseware/'+'/'+item[0][1:7]))
        os.mkdir(os.path.join('E:/STU_Courseware/'+'/'+item[0][1:7]+'/'+item_change))               
    pathb = 'E:/STU_Courseware/'+item[0][1:7]+'/'+item_change+'/'
    print pathb
    url2=item[1]
    print url2


    download_file(url2,pathb)


