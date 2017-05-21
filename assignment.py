import functions_for_assignment as functions


def list_printer(OPTIONS):
    """Prints the given list."""
    print()
    for i in range(len(OPTIONS)):
        print(str(i+1)+": "+OPTIONS[i])
    print(str(len(OPTIONS)+1)+": Back")
    print()


def main_menu_stage_one(usr_input, stage_list):
    """Asks for input and converts it.
    stage_list = list about the choosable options"""
    list_printer(stage_list)
    d_b = input("Which one? ")
    if d_b == "1":
        d_b = stage_list[0]
    elif d_b == "2":
        d_b = stage_list[1]
    else:
        main()
    full_names = functions.full_name_creator(d_b)
    list_printer(full_names)


def main_menu_stage_two(usr_input, stage_list):
    """Asks for input and converts it."""
    list_printer(stage_list)
    city = input("Which city? ")
    for i in range(len(stage_list)):
        if int(city)-1 == i:
            city = stage_list[i]
            break
    nicks_from_city(city)


def nicks_from_city(chosen_city):
    """Collects the mentors from the chosen city"""
    people_tuple = functions.search("mentors", "city", chosen_city)
    people_dict = functions.tuple_to_dict("mentors", people_tuple)
    dictionary_printer("mentors", people_dict)


def main_menu_stage_three(stage_list):
    """Prints the group from stage_list (mentors or applicants) and asks for input"""
    list_printer(stage_list)
    d_b = input("Which group? ")
    search_helper_1(d_b, stage_list)


def search_helper_1(d_b, stage_list):
    """Converts your input, prints and asks for input"""
    if d_b == "1":
        d_b = stage_list[0]
        OPTIONS = ["id", "first name", "last name", "nick name", "phone number", "email"]
    elif d_b == "2":
        d_b = stage_list[1]
        OPTIONS = ["id", "first name", "last name", "application code", "phone number", "email"]
    else:
        main()
    list_printer(OPTIONS)
    usr_input = input("Which one? ")
    search_helper_2(d_b, usr_input)


def search_helper_2(d_b, usr_input):
    """ Converts your input, asks for input and prints the result."""
    if usr_input == "1":
        usr_input = "id"
    elif usr_input == "2":
        usr_input = "first_name"
    elif usr_input == "3":
        usr_input = "last_name"
    elif usr_input == "4":
        if d_b == "mentors":
            usr_input = "nick_name"
        else:
            usr_input = "application_code"
    elif usr_input == "5":
        usr_input = "phone_number"
    elif usr_input == "6":
        usr_input = "email"
    else:
        main()
    info = input("Give me one detail, please. ")
    result_tuple = functions.details_details_everywhere(d_b, info, usr_input)
    result_dict = functions.tuple_to_dict(d_b, result_tuple)
    dictionary_printer(d_b, result_dict)


def main_menu_stage_four():
    """New applicant stage"""
    first_name = input("First name pls: ")
    last_name = input("Last name pls: ")
    phone_number = input("Phone number pls: ")
    email = input("Email pls: ")
    functions.new_applicant_validator(first_name, last_name, phone_number, email)
    functions.new_applicanto(first_name, last_name, phone_number, email)
    result = functions.details_details_everywhere("applicants", email, "email")
    dictionary_printer("applicants", functions.tuple_to_dict("applicants", result))


def main_menu_stage_five(stage_list):
    """Update stage"""
    list_printer(stage_list)
    d_b = input("Mentors or applicants? ")
    if d_b == "1":
        d_b = "mentors"
    elif d_b == "2":
        d_b = "applicants"
    else:
        main()
    person_id = input("Give me the unique id ")
    id_checker(person_id, d_b)
    list_printer(['Phone', "Email"])
    what = input("What dou you want to update? ")
    if what == "1":
        what = "phone_number"
    elif what == "2":
        what = "email"
    else:
        main()
    new_info = input("Please, enter the new info ")
    functions.update(d_b, what, new_info, person_id)
    result_tuple = functions.details_details_everywhere(d_b, person_id, "id")
    result_dict = functions.tuple_to_dict(d_b, result_tuple)
    dictionary_printer(d_b, result_dict)


def id_checker(person_id, d_b):
    """Validates the id"""
    id_tuple = functions.custom("id", d_b)
    id_list = functions.tuple_to_list(id_tuple)
    print(int(person_id) in id_list)
    if int(person_id) not in id_list:
        print("Sorry, there is no person with that Id")
        main()


def main_menu_stage_six(stage_list):
    """Remove stage"""
    list_printer(stage_list)
    condition = input("Choose please ")
    if condition == "1":
        condition = "id"
    elif condition == "2":
        condition = "first_name"
    elif condition == "3":
        condition = "last_name"
    elif condition == "4":
        condition = "application_code"
    elif condition == "5":
        condition = "phone_number"
    elif condition == "6":
        condition = "email"
    else:
        main()
    id_to_delete = input("Enter the unique key for the delete ")
    functions.remove_applicant(condition, id_to_delete)


def decision():
    chosen = input("Type something.")
    if chosen == "1":
        main_menu_stage_one(chosen, lists("d_b"))
    elif chosen == "2":
        main_menu_stage_two(chosen, lists("city"))
    elif chosen == "3":
        main_menu_stage_three(lists("d_b"))
    elif chosen == "4":
        main_menu_stage_four()
    elif chosen == "5":
        main_menu_stage_five(lists("d_b", "applicants"))
    elif chosen == "6":
        main_menu_stage_six(lists("applicants"))
    elif chosen == "7":
        quit()
    else:
        print("Please m8...")


def dictionary_printer(people, dictionary):
    """Which group to print? (people = mentors or applicants"""
    if people == "mentors":
        for key, value in dictionary.items():
            to_be_sure = value["first_name"]
            print("\nId: "+str(key))
            print("Name: "+value["first_name"]+" "+value["last_name"]+" alias "+value["nick_name"])
            print("Contact: "+value["phone_number"]+" & "+value["email"])
            print("Lol: "+str(value["favorite_number"])+"\n")
    else:
        for key, value in dictionary.items():
            to_be_sure = value["first_name"]
            print("\nId: "+str(key))
            print("Name: "+value["first_name"]+" "+value["last_name"])
            print("Contact: "+value["phone_number"]+" & "+value["email"])
            print("Lol: "+str(value["application_code"])+"\n")


def lists(main_menu):
    """Returns a list with options"""
    if main_menu == "d_b":
        info_list = ["mentors", "applicants"]
    elif main_menu == "city":
        city_tuple = functions.cities()
        info_list = functions.tuple_to_list(city_tuple)
    elif main_menu == "applicants":
        info_list = ["id", "first name", "last name", "application code", "phone number", "email"]
    return info_list


def main():
    username = functions.username()
    password = functions.password()
    functions.login_validator(username, password)
    print("\nWelcome {username}. Have a nice day!\n".format(username=username))
    OPTIONS = ["Let's see all the full names", "Mentors from one city", "Search",
               "New applicant", "Update", "Remove"]
    end = False
    while not end:
        list_printer(OPTIONS)
        decision()


if __name__ == '__main__':
    main()


# CodeCool asked for:
def carol_something():
    carol_smth = functions.details_details_everywhere("applicants", "Carol", "first_name")
    return carol_smth


def some_email():
    dunno_email = functions.details_details_everywhere("applicants", "@adipiscingenimmi.edu", "email")
    return dunno_email


def new_app():
    functions.new_applicanto(
        666, 'Markus', 'Schaffarzyk', '003620/725-2666', 'djnovus@groovecoverage.com', 54833)
    markus = functions.details_details_everywhere(
        "applicants", 54833, "application_code")
    return markus


def jemima_new_phone():
    functions.update("applicants", "phone_number", "juhuuu", "first_name", "Jemima")
    result = functions.details_details_everywhere("applicants", "Jemima", "first_name")
    return result


def mauri():
    return "DELETE FROM applicants WHERE email like ('%mauriseu.net')"
