import boto3
s3 = boto3.resource('s3')
def main(args):
      name = args.get("name", "There")
      greeting = "Hello " + name + "!"
      print(greeting)
      return {"body": greeting}