# Install & Config. ArgoCD

- Ref's:
  - <https://levelup.gitconnected.com/getting-started-with-argocd-on-your-kubernetes-cluster-552ca5d8cf41>

  - <https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml>

  - <https://redhat-scholars.github.io/argocd-tutorial/argocd-tutorial/index.html>
  
  - <https://argo-cd.readthedocs.io/en/stable/>

- Create the NameSpace
  - Cmd's Option:
    - ```kubectl create namespace argocd```

  - By Yaml file:
    - ```kubectl apply -f argocd-ns.yaml```
    - ```kubectl get ns```

- Active the argocd namespace, otherways the starting of the pods will fail
  - ```kubens argocd```

- Apply a Kubernetes manifest provided by the official ArgoCD documentation that contains several deployment and services resources to make ArgoCD work out of the box
  - ```kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml```
  - To watch the Container creation & starting
    - ```watch kubectl get pods -n argocd```
  - To get the status:
  - ```kubectl get all -n argocd```

- To access ArgoCD:
  - Get the ArgoCD Admin Password:
    - ```kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d; echo```
  - By PortForward:
    - ```kubectl port-forward svc/argocd-server -n argocd 8080:443```
    - Access with: ```https://localhost:8080```

  - By NodePort (Recomended):
    - Apply argocd-nodeport.yaml
      - ```kubectl apply -f manifests/argo/argocd-nodeport.yaml```
    - Get the minikube IP:
      - ```minikube ip```
    - Access Argo with web explorer:
      - ```minikube-ip:30007```

psw: NX8HTYm2-p6Gej78

psw: S9ZsmDphQLcQvH7y