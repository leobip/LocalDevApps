

# Test cmds
# start minikube cluster

import subprocess
import json
from matplotlib.font_manager import json_dump

from pip import main
from kubernetes import client, config, utils


def get_2():
    config.load_kube_config()
    k8s_client = client.ApiClient()
    print (type(k8s_client))
    
    list_apiC = k8s_client.l
    # example nginx deployment
    example_dict = {'apiVersion': 'apps/v1', 'kind': 'Deployment', 'metadata': 'name', 'spec': {'selector': {'matchLabels': {'app': 'nginx'}}, 'replicas': 1, 'template': {'metadata': {'labels': {'app': 'nginx'}}, 'spec': {'containers': [{'name': 'nginx', 'image': 'nginx:1.14.2', 'ports': [{'containerPort': 80}]}]}}}}
    utils.create_from_dict(k8s_client, example_dict)

def get_k():
    config.load_kube_config()

    v1=client.CoreV1Api()
    print(type(v1))

    print("Listing pods with their IPs:")
    
    tmp = v1.list_service_for_all_namespaces(watch=False)
    tmp_items = tmp.items
    print(type(tmp_items))
    # print(tmp_items)
    jsonStr = json.dumps(tmp.items)
    
    
    
    ret = v1.list_pod_for_all_namespaces(watch=False)
    print(type(ret))
    
    str_items = ret.items
    print(type(str_items))
    
    

    for i in ret.items:
        print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
        print(i)


def create_clustr():
    
    nm_clstr = input("Enter name for Cluster: ")
    args = 'minikube start -p ' + nm_clstr
    
    subprocess.call(args, shell=True)
    
    
def main():
    
    get_k()
    print("#########/n")
    get_2()
    
    # create_clustr()
    
if __name__ == "__main__":
    main()
