# Kubernetes
## Prerequisites
I haven't installed [minikube](https://minikube.sigs.k8s.io/docs/start/) for this lab, I just used [built-in Kubernetes into Docker Desktop](https://docs.docker.com/desktop/kubernetes/): 
![Kubernetes enabled option in Docker Desktop](images/kuber.png)

## Steps
1. Deploy your application in the Kubernetes. Use the kubectl create command to create a Deployment:
    ![](images/kubectl-deploy.png)
2. Make your application accessible from outside the Kubernetes virtual network. Create a Service for it:
    ![](images/kubectl-svc.png)
3. Provide the output of `kubectl get pods,svc` command:
    ![](images/kubectl-initial.png)
4. Clean up. Remove deployment and service that you created: 
    ```bash
    kubectl delete deployment,svc my-app
    ```
5. Use configuration files to deploy your
application. Create a deployment.yml manifest for it. Set up at least 3 replicas:
    ```bash
    kubectl apply -f deployment.yaml 
    ```
6. Create a service.yml manifest for your app: 
    ```bash
    kubectl apply -f service.yaml 
    ```
7. Provide the output of `kubectl get pods,svc` command:
    ![](images/kubectl-final.png)
8. Clean up. Remove deployment and service that you created: 
    ```bash
    kubectl delete svc app-service
    kubectl delete deployment app-deployment
    ```

# HELM
1. Create a helm chart template:
    ```bash
    helm create my-app
    ```
2. Keep `deployment.yaml` and `service.yaml` only due to others are not needed for the lab. Configure them correctly.
3. Change `values.yaml` accordingly to my image, tag, port and type of service.
4. For `livenessProbe` and `readinessProbe` I have used `/metrics` endpoint.
5. Install my helm chart: 
    ```bash
    helm install my-app my-app
    ```
6. Provide the output of `kubectl get pods,svc` command:
    ![](images/helm-final.png)
