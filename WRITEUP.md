# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

*For **both** a VM or App Service solution for the CMS app:*

- *Analyze costs, scalability, availability, and workflow*
  - VM: VMs tend to be more expensive and time consuming to maintain. The VMs can be scaled using VM Scale Sets to provide high availability and redundancy.
  - App Service: App Services are highly available and allow both horizontal and vertical scaling of resources. They also allow continuous deployment via git. One drawback is that you continue to pay for the App Service, even if the app or service is not running.
- *Choose the appropriate solution (VM or App Service) for deploying the app*
  - App Service
- *Justify your choice*
  - For a simple python app, App Service provides us a quick path to deployment and removes the operations overhead of managing a full OS and VM. We can focus on our app code and functionality by choosing App Service.

### Assess app changes that would change your decision.

*Detail how the app and any other needs would have to change for you to change your decision in the last section.* 

- If the app gained popularity, we would probably exhaust the 14GB memory and 4 vCPU limits for our App Service. 