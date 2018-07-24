def health_calc(age, no_of_apples, cigs_smoked):
    answer = (100 - age) + no_of_apples * 2.5 + cigs_smoked * 2
    print(answer)

saurabh_exp_age = [19, 10, 0]
health_calc(saurabh_exp_age[0], saurabh_exp_age[1], saurabh_exp_age[2])
health_calc(*saurabh_exp_age)       # unpackaging of arguments means passing elements of array as parameters in function by using '*'
