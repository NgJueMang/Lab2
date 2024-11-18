def calculate_bmi(height,weight):
    print("Height = " + str(height))
    print("Weight = "+ str(weight))

    #Add code here to calculate BMI
    bmi = weight/(height * height)
    #Add code here eto display calculate BMI
    print("BMI = "+ str(bmi))

    if(bmi<18.5):
        classification = "Under Weight"
        return_value = -1
    elif(18.5<=bmi<=25.0):
        classification = "Normal Weight"
        return_value = 0
    else:
        classification = "Over Weight"
        return_value = 1

    print("Weight Classification = " + classification)
    print("Return Value = " + str(return_value))
    return return_value

calculate_bmi(weight=57, height=1.73)