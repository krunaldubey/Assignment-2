import pandas as pd

res=pd.read_json("https://api.github.com/search/repositories?q=is:public")
for i in range(len(res['items'])):
  if (res['items'][i]['language']=='python' or res['items'][i]['forks']>=200) and (res['items'][i]['stargazers_count'])>2000:
    col1=(res['items'][i]['name'])
    col2=(res['items'][i]['description'])
    col3=(res['items'][i]['html_url'])
    col4=(res['items'][i]['watchers_count'])
    col5=(res['items'][i]['stargazers_count'])
    col6=(res['items'][i]['forks_count'])
    data = {'Name': col1,
        'Description': col2,
        'Html_Url': col3,
        'Watchers_Count':col4,
        'Stargazers_Count':col4,
        'forks_count':col5
        }

ans=pd.DataFrame([data],index=None)
print(ans)
temp=ans.to_csv()
with open("test.csv","w") as fp:
  fp.write(temp)
