# Deploy & Config: Prometheus / Grafana

## Prometheus

### En esta publicación os enseñaré a desplegar Prometheus y Grafana en vuestro cluster Minikube empleando Helm charts. Prometheus nos ayudará a monitorizar nuestro cluster Kubernetes además del resto de recursos que se ejecuten sobre él. Grafana nos ayudará a visualizar las métricas obtenidas por Prometheus mostrándolas en elegantes cuadros de mando o dashboards

- Req's:
  - Minikube
  - helm

- Ref's:
  - <https://github.com/bitnami/charts/tree/master/bitnami/kube-prometheus>
  - <https://blog.marcnuri.com/instalar-prometheus-grafana-minikube>
  - <https://github.com/bitnami/charts>

- Add Repo & Deploy:
  - ```helm repo add prometheus-community https://prometheus-community.github.io/helm-charts```

  - Install & set as NodePort
    - ```helm install prometheus prometheus-community/prometheus```
    - ```kubectl expose service prometheus-server --type=NodePort --target-port=9090 --name=prometheus-server-np```

  - Get the minikube ip & the service port
    - ```minikube ip```
    - ```kubectl get services``` --> Get the por of prometheus-server-np
    - prometheus-server-np (IP): 192.168.67.2:31523

TODO: get Syntaxis for set the nodePort in cmd.

## Grafana

- Ref's: <https://github.com/grafana/helm-charts/blob/main/charts/grafana/README.md>

TODO: Verify to set persistence volume to Grafana

- Add Repo & Deploy:
  - ```helm repo add grafana https://grafana.github.io/helm-charts```
  - ```helm repo update```
  - NOTE: You can then run ```helm search repo grafana``` to see the charts.

  - Install & set as NodePort:
    - ```helm install my-release grafana/grafana```
    - ```kubectl expose service grafana --type=NodePort --target-port=3000 --name=grafana-np```
  
    - Deploy with persistence & set to NodePort
  
  - Get the service-port
    - grafana-np (IP): 192.168.67.2:32468

  - Get the password for admin:
    - ```kubectl get secret --namespace default grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo```
    - This Case: 2LNZ0KpEDmkiSeDGoHWSb85KtYjgsiashDQ9gxMd

  - To Uninstall: ```helm delete my-release```

  - You can access the app with: ```minikube service grafana-np```, this print a table with the ip:port & open the page

  - Kubernethes dashboard:(6417) <https://grafana.com/grafana/dashboards/6417-kubernetes-cluster-prometheus/>

## HELM - Tip's

To override values in a chart, use either the '--values' flag and pass in a file or use the '--set' flag and pass configuration from the command line, to force a string value use '--set-string'. You can use '--set-file' to set individual values from a file when the value itself is too long for the command line or is dynamically generated. You can also use '--set-json' to set json values (scalars/objects/arrays) from the command line.

  -```helm install -f myvalues.yaml myredis ./redis```

  -```helm install --set name=prod myredis ./redis```

  -```helm install --set-string long_int=1234567890 myredis ./redis```

  -```helm install --set-json 'master.sidecars=[{"name":"sidecar","image":"myImage","imagePullPolicy":"Always","ports":[{"name":"portname","containerPort":1234}]}]' myredis ./redis```

- Set values from cmd line:
  - To debug & check the config to deploy:
    - ```helm install --debug --dry-run my-deploy runix/pgadmin4 \\n  --set service.type=NodePort \\n  --set service.nodePort=30865 \\n  --set env.email=leo@test.com```

### Helm values examples

Examples of sections to set values

- extraVolumeMounts
    Volume can be type persistentVolumeClaim or hostPath but not both at same time. If neither existingClaim or hostPath argument is given then type is emptyDir.

        ```yaml
        - extraVolumeMounts:
        - name: plugins
            mountPath: /var/lib/grafana/plugins
            subPath: configs/grafana/plugins
            existingClaim: existing-grafana-claim
            readOnly: false
        - name: dashboards
            mountPath: /var/lib/grafana/dashboards
            hostPath: /usr/shared/grafana/dashboards
            readOnly: false
        ```

## Install Prometheus & Grafana in One (1) Helm

<https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack>

- Verify & Copy, if needed to use a customize values:
  - ```helm show values prometheus-community/kube-OB```
- Install:
  - ```helm install prometheus prometheus-community/kube-prometheus-stack```
- Verify all the pods under prometheus
  - ```kubectl --namespace default get pods -l "release=prometheus"```
- Set Prometheus NodePort:
  - ```kubectl expose service prometheus-kube-prometheus-prometheus --type=NodePort --target-port=9090 --name=prometheus-server-np```
- Open Prometheus Web:
  - ```minikube service prometheus-server-np```
- Set Grafana NodePort:
  - ```kubectl expose service prometheus-grafana --type=NodePort --target-port=3000 --name=grafana-np```

  - Password for admin is in the values file (line: 727): prom-operator

https://github.com/prometheus-community/helm-charts/blob/main/charts/kube-prometheus-stack/values.yaml

TODO: Verify ... Set the values from file.
To Apply kustomization file... kubectl apply -k .

Check its status by running:
  kubectl --namespace default get pods -l "release=prometheus"

  kubectl expose service prometheus-kube-prometheus-prometheus --type=NodePort --target-port=9090 --name=prometheus-server-np