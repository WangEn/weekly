import os
import httpx
import re
import urllib.parse
import datetime

def fetch_ci_time(filePath):
    entries = httpx.get("https://api.github.com/repos/WangEn/weekly/commits?path=" + filePath + "&page=1&per_page=1")
    ciTime= entries.json()[0]["commit"]["committer"]["date"].split("T")[0]
    return ciTime
    # return datetime.datetime.strptime(ciTime,"%Y-%m-%d")

if __name__ == "__main__":
  readmefile=open('README.md','w')
  readmefile.write("# 爱情的纹理\n\n> 记录自诩热爱生活的工程师 Warn 的简单生活纹理，不限于技术，期待成为一个周更写手(*❦ω❦)，欢迎订阅~\n\n")
  readmefile.write("## 打油诗\n\n> 门前有座前端城\n>\n> 城郊草庐舞花灯\n>\n> 九流杂耍欲乘风\n>\n> 俊杰精英唤相逢\n\n")
  readmefile.write("## Directroy Structure\n\n\xa0\xa0- src\n\xa0\xa0\xa0\xa0- pages\n\xa0\xa0\xa0\xa0\xa0\xa0- posts/*   `markdown博客文件`\n\n")
  readmefile.write("## Update Log\n\n> 2024-02-04 Fork from Tw93, start deploying static blogs with Astro.\n\n")
  readmefile.write("## Fork自用\n\n可见 [开发文档](https://github.com/WangEn/weekly/blob/main/Deploy.md)\n\n")
  readmefile.write("## 致谢\n\n> 💖 感谢 [Tw93](https://github.com/tw93) Astro仓库模板Fork自 [潮流周刊](https://github.com/tw93/weekly)\n\n")


  recentfile=open('RECENT.md','w')

  for root, dirs, filenames in os.walk('./src/pages/posts'):
    filenames = sorted(filenames, key=lambda x:float(re.findall("(\d+)",x)[0]), reverse=True)

  for index, name in enumerate(filenames):
      if name.endswith('.md'):
        filepath = urllib.parse.quote(name)
        oldTitle = name.split('.md')[0]
        url   = 'https://www.715721.xyz/posts/' + oldTitle
        title = '第 ' + oldTitle.split('-')[0] + ' 期 - ' + oldTitle.split('-')[1]
        readmeMd= '* [{}]({})\n'.format(title, url)
        dateList = ["2022-10-10","2022-09-26","2022-09-12","2022-09-05","2022-08-29"]
        num = int(oldTitle.split('-')[0])
        if index < 5 :
          # if num < 100 :
          #   modified = dateList[99-num]
          # else :
          #   modified = fetch_ci_time('/src/pages/posts/' + filepath)
          modified = fetch_ci_time('/src/pages/posts/' + filepath)

          recentMd= '* [{}]({}) - {}\n'.format(title, url, modified)
          recentfile.write(recentMd)
        readmefile.write(readmeMd)

  recentfile.close()
  readmefile.close()
