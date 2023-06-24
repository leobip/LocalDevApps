# SonarQube

Ref: <https://artifacthub.io/packages/helm/sonarqube/sonarqube>

## Install by Kubernethes MAnifests

## Install by Helm

- To deploy with a NameSapce:

```bash
    helm repo add sonarqube https://SonarSource.github.io/helm-chart-sonarqube
    helm repo update
    kubectl create namespace sonarqube
    helm upgrade --install -n sonarqube sonarqube sonarqube/sonarqube
```

- The Helm Manifest comes with DB already integrated
  - If we want to verify the values of the insrtall:

    ```helm install --debug --dry-run sonarqube sonarqube sonarqube/sonarqube```

- To set custom values, the best option is to create a .yaml with the settings, it will overrride the defaults from the original
  - ```helm upgrade --install sonarqube sonarqube/sonarqube```
- To expose the service as NodePort from the cmd line:
  - ```kubectl expose service sonarqube-sonarqube --type=NodePort --target-port=9000 --name=sonarqube-np```

- Create & Apply a service manifest
  - ```kubectl apply -f sonarqube-serv.yaml```
  
### Actual User & Psw

  User: admin
  Password: Ll276700

  
NX8HTYm2-p6Gej78