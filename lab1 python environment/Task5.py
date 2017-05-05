x = int(input('Enter the Year\n'))

if(x%4==0):
        if(x%100==0):
              if(x%400==0):
                  {
                      print("leap year")
                  }
              else:{
                  print("Not leap year")
              }
        else:{
            print("leap year")
        }
else:{
    print("Not leap year")
}