# AzureResume


I was on the lookout for projects to dive deeper into Azure when I stumbled upon the Cloud Resume Challenge by Forrest Brazeal. I've always been keen on setting up my own website, and this seemed like a cool way to showcase myself online while getting better at web design and Azure.

Tackling this project had its tough moments, especially with figuring out the Azure functions and how everything worked together. But I managed to pull it off, and now I've got my own website up and running on Azure. It was a great way to apply what I've learned and step up my online game.

Website: https://www.zusnet.com

# Project Objectives
This project consists of the following challenges:
# Website Development:
Utilizing HTML, CSS, and JavaScript to showcase resume.
# Visitor Counter Integration
Implementing a JavaScript-based visitor counter interacting with Azure CosmosDB via an Azure Function written in Python.
# Github Repository
Storage of code within a GitHub repository.
# CI/CD Pipeline
Configuration of GitHub actions for automated deployment of code changes to the production environment.

# Taking on the Challenge:

Reading through the challenge, I had to create a static resume hosted on Azure Blob Storage. It needs to have a visitor counter that will be triggered by a function calling an API. The function would need to interact with CosmosDB which is where the counter info would be stored. We’d be using Azure CDN to enable features like HTTPS and custom domain support for the static site. For all the CI/CD tooling I would have to leverage GitHub.
![image](https://github.com/zus119/AzureResume/assets/51805317/637ad0ca-1ed4-423c-9200-78c2f8c6ca68)

The resume must be written in HTML. I knew almost nothing about HTML before this challenge so I looked for a nice resume template I could use. I’m also a huge “trial by fire” person and started to get my tools ready to start coding, looked at some HTML tutorials on YouTube and started building the site.
The resume had to be styled in CSS, thanks to the template I found, that had already been done. Once I had my code together, I created repositories in GitHub so that I could begin source controlling my code. The initial site was very simple, listed my job experience throughout the years and contact information, it truly was a simple resume. It took me about 2 hours to finish the simple HTML coding plus uploading the files to Blob storage and enabling Azure CDN as I was familiar with it. 

But…I’ve always been the type to go all in when I find something interesting/want to learn. There is this fire in me that always hungers for knowledge, so I dove deep into HTML/JavaScript/CSS and started to look at sites online for inspiration. I decided I wanted a Portfolio website where I could showcase future projects instead of a simple resume one, I put my bob the builder hat on and got to coding. I spent about a week putting together the Frontend of the website, it could have been a few hours, but I always go a step above when it comes to something I want to learn.

With part 1 of the resume challenge being done, I started to work on Part 2: Building the backend. This involved looking at documentation on setting up CosmosDB, container and data. Creating the azure function to interact with CosmosDB counter data and test the function locally to make sure the counter data is being displayed in the browser and in the website locally.

Getting the function to work was the hardest part of this challenge. I had to learn how to set up a python environment locally and test the function. I wasn’t very familiar with Python code so I had to read quite a lot and look at function examples from Microsoft and other web resources. Once I had the function code working properly I tried to deploy it to azure via VSCode; Here is where I encountered another problem. I wasn’t able to deploy it as it couldn’t find a “resource.” I had to create a Function App first, then the “resource” popped up.

After successfully deploying the function to Azure, I encountered another error. The visit count displayed an error on my site. I had to enable CORS and save my website’s address, or so I thought. I was still getting the same error. I went into the “Diagnose and solve problems” section of the Function and saw the error it was throwing. Within my function code I had defined the cosmos DB key and URL under different names, that was the issue. I went into the configuration settings and added the application settings. SUCCESS!! The function was now displaying the visit count correctly.

The final step was to create a CI/CD Pipeline using GitHub actions. I looked online for documentation and created the secrets needed to integrate into Azure. Now when I make a change in my local repo and push it to github it automatically gets pushed to Azure.

# Conclusion
Doing the Cloud Resume Challenge was a big journey for me. This project helped me learn web development and python code along with new Azure services. The most enjoyable thing about this was learning frontend web development. I never knew how fun it could be to create websites. I have many more ideas to keep improving my portfolio site and showcase more projects.

