import argparse

parser = argparse.ArgumentParser(description='Deployment python script.')

parser.add_argument('--namespace', help='namespace for specs')
parser.add_argument('deployment_url', help='deployment.yaml url')
parser.add_argument('--service_url', help='service.yaml url')
parser.add_argument('--ingress_url', help='ingress.yaml url')

args = parser.parse_args()


def main():
    print(args)

    namespace = get_namespace()
    print("Using namespace %s" % namespace)

    if args.deployment_url:
        print("deployment.yaml is at work")
    if args.service_url:
        print("service.yaml is at work")
    if args.ingress_url:
        print("ingress.yaml is at work")


def get_namespace():
    if args.namespace:
        return args.namespace
    else:
        return "blah"


if __name__ == "__main__":
    main()
