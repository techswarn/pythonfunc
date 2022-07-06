

def main(args):
      name = args.get("name", "There")
      greeting = "Hello " + name + "!"
      print(greeting)
      return {"body": greeting}