import datetime
readme = open("Tracked_Repos.MD", "w+")
# W+ to rewrite entire list everytime
content = "# The list of Repos that are tracked" \
          "\n\n*The list is automatically updated*\n\n" \

repos = open("repos.txt", "r")
number = 1
for repo in repos.readlines():
    content = content + str(number) + ". [" + repo.strip("\n") + "](https://github.com/" + repo.strip("\n") + ")\n"
    number += 1

repos1 = open("repos1.txt", "r")

for repo in repos1.readlines():
    content = content + str(number) + ". [" + repo.strip("\n") + "](https://github.com/" + repo.strip("\n") + ")\n"
    number += 1

repos2 = open("repos2.txt", "r")

for repo in repos2.readlines():
    content = content + str(number) + ". [" + repo.strip("\n") + "](https://github.com/" + repo.strip("\n") + ")\n"
    number += 1

repos3 = open("repos3.txt", "r")

for repo in repos3.readlines():
    content = content + str(number) + ". [" + repo.strip("\n") + "](https://github.com/" + repo.strip("\n") + ")\n"
    number += 1

repos4 = open("repos4.txt", "r")

for repo in repos4.readlines():
    content = content + str(number) + ". [" + repo.strip("\n") + "](https://github.com/" + repo.strip("\n") + ")\n"
    number += 1

content = content + "\n### Total number of repos tracked: " + str(number-1) +"\n\nLast updated on : " + str(datetime.datetime.utcnow()) + " UTC"

readme.write(content)
readme.close()
repos.close()
