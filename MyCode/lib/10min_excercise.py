def say_hello(name):
    print(f'hello '+ (name))
    return "hello " + (name)


# Intended output:
#
# > say_hello("kay")
# => "hello kay"

# print(say_hello('kay'))
# say_hello('kay')


def factorial(n):
    product = n
    #print(f"at the start product is {product}")
    while n > 1:
        n -= 1
        #print(f"we multiply {product} by {n}")
        product *= n
        #print(f"we get {product}")

    return product

print(f"""
Running: factorial(5)
Expected: 120
Actual: {factorial(5)}
""")

print(f"""
 Running: factorial(3)
Expected: 6
  Actual: {factorial(3)}
""")

print(f"""
 Running: factorial(7)
Expected: 5040
  Actual: {factorial(7)}
""")
