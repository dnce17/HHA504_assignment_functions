# Assignment: Exploring Serverless Computing and Cron Jobs in Azure, GCP, and GitHub

# Instructions
* Screenshots of the serverless function deployment process in both Azure and GCP.
* The code and configuration of your GitHub Action workflow.
* Screenshots or documentation of the GCP Cloud Scheduler setup.
* A brief reflection on the use cases, benefits, and limitations of serverless functions.

## Screenshots of Serverless Function Deployments
### Azure
1. Click "Function App," then "Create" or "Create Function App"
![Search "Function App" in search bar](img/azure/deploy/deploy_1.png)
![Click "Create" or "Create Function App"](img/azure/deploy/deploy_2.png)
2. Choose "Consumption" for the hosting option
![Choose "Consumption" for the hosting option](img/azure/deploy/deploy_3.png)
3. Ensured the following configurations were used in these tabs
    * Basics
        * Subscription: Azure for Students
        * Resource Group: HHA-504
        * Runtime stack: Python
        * Version: 3.11
        * Region: East US
        * Operating System: Linux
![Basics tab config](img/azure/deploy/deploy_4.png)
    * Monitoring
        * Enable Application Insights: No
![Monitoring tab config](img/azure/deploy/deploy_5.png)
    * Deployment
        * Basic authentication: Enable
![Deployment tab config](img/azure/deploy/deploy_6.png)
4. Click "Review + create," then click "Create"
5. Once deployment is successful, go to the resource
6. In "Overview", scroll down and click "Create Function" below the "Create in Azure portal" header
![Overview of created function](img/azure/deploy/deploy_7.png)
7. In the new panel that opens, click "HTTP trigger"
![Click "HTTP trigger"](img/azure/deploy/deploy_8.png)
8. Click "Next" and then "Create"
![Create function](img/azure/deploy/deploy_9.png)
9. Alter the code to do a desired function
10. Click "Save," then "Test/Run"
11. Add name(s) and value(s) below "Name" and "Value" header OR enter them in JSON format below "Body" header (choose 1 method), then click "Run" to see if function ran successfully
![Test function](img/azure/deploy/deploy_10.png)

### GCP
1. Click "Cloud Run functions," then "Create Function"
![Search "Cloud Run functions" in search bar](img/gcp/deploy/deploy_1.png)
![Click "Create Function"](img/gcp/deploy/deploy_2.png)
2. Ensured the following configurations were used in these tabs:
    * Basics
        * Trigger type: HTTPS
        * Authentication: Allow unauthenticated invocations
![Basics tab config](img/gcp/deploy/deploy_3.png)
    * Runtime
        * Autoscaling --> Maxinum number of instances: 3
![Runtime tab config](img/gcp/deploy/deploy_4.png)
    * Left everything else as default
3. Go to next page, taking you to the "Code" section
4. Set runtime to Python 3.10
5. Alter the code to do desired function (like checking blood pressure)
6. Click "Test Function"
7. Change key names as needed in JSON, then click "Run Test" to see if function ran successfully
![Test code](img/gcp/deploy/deploy_5.png)
8. Click "Deploy"
![Deployment successful](img/gcp/deploy/deploy_6.png)

### Running Function Outside of Azure and GCP 
9. Copy URL
    * In Azure, click "Get function URL" and copy the link under "default (Function key)"
10. In your editor
    * paste the URL into some kind of variable
    * store test keys and values in a dict
11. Running the function outside of GCP and Azure may look something like the images below, but will depend on what the function is.
    * GCP
![Testing func outside of GCP](img/gcp/deploy/deploy_7.png)
    * Azure 
![Testing func outside of Azure](img/azure/deploy/deploy_11.png)

### Documentation of Cloud Scheduler setup.

## GitHub
### Code and Configuration for the Cron Job
