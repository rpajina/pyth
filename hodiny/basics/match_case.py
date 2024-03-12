
pozdrav = "ahoj"

if pozdrav == "ahoj":
    print ("ahoj")
elif pozdrav == "cau":
    print("cau")

match pozdrav:

    case "ahoj"| "Ahoj": #takto dame dve hodnoty pomoci | alt gr + w
        print("ahoj")
    case "cau":
        print("cau")
    case "hello":
        print("hello")
    case _: # jako else 
        print("nezvolen pozdrav")