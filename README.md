**Project Overview**

Developed a full-stack message storage application using HTML, CSS,
JavaScript, Python Flask, and MySQL. The project follows a 3-tier
architecture with clear separation between frontend, backend, and
database layers.

**Development (using AI)**

Built an interactive frontend using HTML, CSS to handle user
interactions and UI design.\
Implemented backend logic using Python Flask to manage APIs, requests,
and business logic.\
Used MySQL as the database to store and manage application data
efficiently.

**Version Control**

Managed the entire source code using Git and GitHub.\
Tracked changes, maintained repository history, and enabled
collaborative development practices**.**

**CI/CD Automation**

Integrated Jenkins to build a CI/CD pipeline for automated workflow.\
Automated code build, testing, and deployment whenever changes were
pushed to GitHub.

**Containerization**

Used Docker and Docker Compose to containerize the application.\
Managed frontend, backend, and database as separate services for
consistent deployment across environments.

**DevOps Implementation**

Automated the complete deployment process to reduce manual effort and
improve efficiency.\
Ensured faster delivery and reliable application deployment using DevOps
best practices**.**

**Conclusion**

**This project helped in understanding real-world full-stack development
along with DevOps tools and automation. It improved practical knowledge
of CI/CD pipelines, containerization, and production-level deployment
workflows.**

**Top of Form**

**Bottom of FormA 3-Tier Full Stack Application with frontend, backend,
and database architecture integrated using DevOps CI/CD automation.\**

**[Used technologies:]{.underline}**

**1.Github**

**2.Jenkins(CICD)**

**3.Docker**

**4.Python-flask(Backend)**

**5.HTML and CSS(Frontend)**

**6.Mysql(Database)**

**First, clone the project repository from
https://github.com/chandusaigari/project and open it in VS Code.**

**After making changes, push the code to your GitHub repository using
the following**

**Git commands:**

**git init**

**git clone https://github.com/chandusaigari/project.git**

**git branch -M main**

**git status**

**git remote add origin https://github.com/your_username/project**

**git add .**

**git commit -m \"code committed\"**

**git push origin main**

**Now the code will be available in your GitHub repository.**

**If your repository already contains files, use \`git pull origin
main\` before pushing the code, because the files in github may not
contain in your local vscode folder.**

**Make sure you downloaded Jenkins and docker for this project without
those , this project would not happen .**

**what to do next after pushing to github?**

**After installing successfully Jenkins and docker do these below
steps,**

**Open any distro of linux like Ubuntu latest version.**

**Type the command for starting Jenkins as shown in below picture**

**After this your Jenkins will start and you can access Jenkins from
browser with**

**localhost://8080.**

![](media/image1.png){width="5.493827646544182in"
height="3.088752187226597in"}

**You need to sign in with your Jenkins username and password**

**After sign in you will get the Jenkins dashboard like this below
one.**

![](media/image2.png){width="7.288288495188102in"
height="2.2700371828521435in"}

**Build your First Job by clicking the above mentioned button**

**The Outcome will be :**

![](media/image3.png){width="7.5in" height="4.153603455818023in"}

**Make sure that your repository name & Job name should be same , select
the pipeline**

**After saving ,you will be redirect to configure page then you need to
choose the pipeline script from scm .**

![](media/image4.png){width="6.098766404199475in"
height="3.4288615485564304in"}

**Now select the scm- source code management as Git**

![](media/image5.png){width="6.728395669291339in"
height="3.7828543307086613in"}

**Now add the URL of your project in the Repository URL**

![](media/image6.png){width="7.5in" height="4.215277777777778in"}

**If your project repo is not private no need to add credentials if it
is private make sure you need to add github credentials.**

![](media/image7.png){width="4.3209886264216975in"
height="2.429355861767279in"}

**Select the branch of your repo based on your project either it is main
or master branch.**

**After applying and save , you can build the Job by pressing the
button**

**BUILD NOW**

![](media/image8.png){width="7.5in" height="4.216666666666667in"}

**As you can see, by clicking BUILD NOW your job will get started..**

![](media/image9.png){width="6.135127952755906in"
height="2.740741469816273in"}

**To visualize the pipeline like above, install Blue ocean plugin from
manag Jenkins & plugins installation page.**

**Also you can see the pipeline flow from console output to view the
process**

**Benefits of viewing console is to know the failure at what point it is
happened**

![](media/image10.png){width="6.3209886264216975in"
height="3.553801399825022in"}

**Make sure the docker is also running in background if not run the
command in your terminal as shown below.**

![](media/image11.png){width="7.5in" height="4.216666666666667in"}

**Without docker running we canot containerize the application of what
we building**

**After docker run ,check the console for on going process**

**You can see we got a failure in pipeline**

**We need to check it in console output for knowing what is the actual
error is**

![](media/image12.png){width="4.024691601049868in"
height="2.262771216097988in"}**\**

**In console output**

![](media/image13.png){width="7.492521872265967in"
height="4.975308398950132in"}

**It was saying that we did not allowed the Jenkins to access docker**

**Solution is in terminal ,run the command :sudo usermode -aG docker
Jenkins**

**By this we will give the access Jenkins from docker**

![](media/image14.png){width="4.981981627296588in"
height="2.800980971128609in"}

**As you can see our Job as successfully done.**

**To check the Job done correctly or not we need to check the docker
containers running and open your application from browser**

![](media/image15.png){width="7.183354111986001in"
height="3.3456791338582677in"}

**Using docker ps command, you can check the running containers and also
see at what port your application running**

**Mine is localhost://5000. Run this in web browser**

**you will get final running application like this**

![](media/image16.png){width="5.506173447069116in"
height="3.095693350831146in"}

![](media/image17.png){width="7.169354768153981in"
height="3.5315321522309713in"}

**Click on this link for step by step process from an end to end picture
flow:**

**Check the YOUTUBE VIDEO for clear explanation:**

**Future Scope:**

**This project can be enhanced by migrating from Docker Compose to
Kubernetes for better scalability, load balancing, auto-scaling, and
self-healing capabilities. Kubernetes will help manage the application
more efficiently in production environments.**

**For monitoring, Prometheus can be used to collect real-time metrics
like CPU, memory, and request performance, while Grafana can visualize
these metrics through dashboards for better system insights.**

**These improvements will make the application more scalable, reliable,
and suitable for cloud-native production deployment.**

**Contact**

**I am actively seeking opportunities to apply my skills in DevOps &
realated fields .\
If you find my project interesting, I would be grateful for an
opportunity to contribute and prove my abilities in a professional
environment.**

**You can reach me at:\
Email: chandusaigari6@gmail.com\
Phone: +91-7396618269**
