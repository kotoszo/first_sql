import psycopg2
from random import randrange
import assignment
from time import sleep


def username():
    dbname = input("Username: ")
    return dbname


def password():
    password = input("Password: ")
    return password


def login_validator(username, password):
    """Conects to my database. Yes my friend, i have a database."""
    connect_str = "dbname='richter' user='{username}' host='localhost' password='{password}'".format(
        username=username, password=password)
    try:
        return psycopg2.connect(connect_str)
    except:
        print("Uh oh, wrong username or password!")
        assignment.main()


# All the sql functions returns tuples.

def connect_to_DB():
    """Conects to my database. Yes my friend, i have a database."""
    # setup connection string
    connect_str = "dbname='richter' user='richter' host='localhost' password='richter123ads'"
    # print(connect_str)
    try:
        return psycopg2.connect(connect_str)
    except:
        print("Uh oh, can't connect. Invalid dbname, user or password?")
        print("or STFU I KNOW!")


def custom(something, somewhere):
    """ Select smth from smwh"""
    conn = connect_to_DB()
    cur = conn.cursor()
    try:
        cur.execute("""SELECT {something} FROM {somewhere}""".format(
            something=something, somewhere=somewhere))
    except:
        print("meh")
        assignment.main()
    result = cur.fetchall()
    return result


def full_name_creator(group):
    """Selects from the given group all the full names"""
    conn = connect_to_DB()
    cur = conn.cursor()
    try:
        cur.execute("""SELECT (first_name, last_name) as fullname FROM {group}""".format(
            group=group
        ))
        result = cur.fetchall()
    except:
        print("Something went wrong")
        assignment.main()
    full_names = []
    for _ in range(len(result)):
        for i in result[_]:
            full_names.append(str(result[_][0]).replace(",", " ").replace("(", "").replace(")", ""))
    print(str(result[0][0]).replace(",", " ").replace("(", "").replace(")", ""))
    return full_names


def cities():
    """Collects all the cities"""
    conn = connect_to_DB()
    cur = conn.cursor()
    try:
        cur.execute("""SELECT DISTINCT city FROM mentors""")
    except:
        print("meh")
        assignment.main()
    city_tuple = cur.fetchall()
    return city_tuple


def search(where, chosen, what):
    """Selects everything FROM {where} WHERE {chosen} = {what}"""
    conn = connect_to_DB()
    cur = conn.cursor()
    try:
        cur.execute("""SELECT * FROM {where} WHERE {chosen} = '{what}'""".format(where=where, chosen=chosen, what=what))
    except:
        print("Something went wrong")
        assignment.main()
    people_tuple = cur.fetchall()
    return people_tuple


def new_applicanto(first_name, last_name, phone_number, mail):
    """inserts new applicant into the database"""
    conn = connect_to_DB()
    cur = conn.cursor()
    conn.autocommit = True
    id_and_code = applicant_id_generator()
    req_id = id_and_code[0]
    req_code = id_and_code[1]
    try:
        cur.execute("""INSERT INTO applicants VALUES
        ({id_number}, '{first}', '{last}', '{phone}', '{mail}', {app_code})""".format(
            id_number=req_id, first=first_name, last=last_name,
            phone=phone_number, mail=mail, app_code=req_code))
        print("Done")
    except:
        print("még mindig szar")


def applicant_id_generator():
    """Generates id for the new applicant and a random application id"""
    conn = connect_to_DB()
    cur = conn.cursor()
    try:
        cur.execute("""SELECT id FROM applicants""")
        applicants_id_tuple = cur.fetchall()
        cur.execute("""SELECT application_code FROM applicants""")
        application_code_tuple = cur.fetchall()
    except:
        print("Something went wrong")
        assignment.main()

    applicants_id_list, application_code_list = [], []
    for _ in applicants_id_tuple:
        for elements in _:
            applicants_id_list.append(elements)
    for _ in application_code_tuple:
        for elements in _:
            application_code_list.append(elements)
    up_to_date_id = max(applicants_id_list)+1
    is_good = False
    while not is_good:
        random_int = randrange(10000, 100000)
        if random_int not in applicants_id_list:
            is_good = True
    return [up_to_date_id, random_int]


def remove_applicant(condition, key):
    """removes the chosen applicant. That stupid."""
    conn = connect_to_DB()
    cur = conn.cursor()
    conn.autocommit = True
    if condition == ("id" or "application_code"):
        try:
            cur.execute("""DELETE FROM applicants WHERE {what} = {key} """.format(
                what=condition, key=key))
            print("\nDone\n")
        except:
            print("Something went wrong")
            assignment.main()
    else:
        key = "%"+key+"%"
        try:
            cur.execute("""DELETE FROM applicants WHERE {what} LIKE '{key}' """.format(
                what=condition, key=key))
            print("\nDone\n")
        except:
            print("SOmething went wrong")
            assignment.main()


def update(group, what, new_info, person_id):
    """Updates in the given group.
    @what = what to set"""
    conn = connect_to_DB()
    cur = conn.cursor()
    conn.autocommit = True
    try:
        cur.execute("""UPDATE {name_of_the_page} SET {what} = '{new_info}' WHERE id = '{person_id}'""".format(
            name_of_the_page=group, what=what, new_info=new_info, person_id=person_id))
        print("\nDone\n")
    except:
        print("Something went wrong")
        assignment.main()


def tuple_to_dict(people, people_tuple):
    """Converts the tuple into dictionary.
    people can be applicants or mentors, people_tuple = the tuple itself"""
    people_dict = {}
    if people == "mentors":
        for i in range(len(people_tuple)):
            people_dict.update({
                people_tuple[i][0]: {
                    "first_name": people_tuple[i][1], "last_name": people_tuple[i][2],
                    "nick_name": people_tuple[i][3], "phone_number": people_tuple[i][4],
                    "email": people_tuple[i][5], "city": people_tuple[i][6],
                    "favorite_number": people_tuple[i][7]
                    }})
    else:
        for i in range(len(people_tuple)):
            people_dict.update({
                people_tuple[i][0]: {
                    "first_name": people_tuple[i][1], "last_name": people_tuple[i][2],
                    "phone_number": people_tuple[i][3], "email": people_tuple[i][4],
                    "application_code": people_tuple[i][5]
                }})
    return people_dict


def tuple_to_list(info):
    """Converts the tuple into list. e.g. to print out the choosable options"""
    result = [element for i in info for element in i]
    return result


def details_details_everywhere(name_of_the_page, person_id, what):
    """Details about the chosen mentor/applicant"""
    conn = connect_to_DB()
    cur = conn.cursor()
    if (what == "id") or (what == "application_code") or (what == "favorite_number"):
        try:
            cur.execute("""SELECT * FROM {where} WHERE {what} = {searched}""".format(
                where=name_of_the_page, what=what, searched=person_id))
        except:
            print("Something went wrong")
            assignment.main()
    else:
        person_id = "%"+person_id+"%"
        try:
            cur.execute("""SELECT * FROM {where} WHERE {what} LIKE '{searched}'""".format(
                where=name_of_the_page, what=what, searched=person_id))
        except:
            print("Something went wrong")
            assignment.main()
    person_tuple = cur.fetchall()
    return person_tuple


def new_applicant_validator(first_name, last_name, phone_number, email):
    """Somewhat validates"""
    if first_name == "" or last_name == "" or phone_number == "" or email == "":
        print("\nAll the information is requiered.\n")
        sleep(0.5)
        print("You will be redirected to the main menu.")
        sleep(1)
        assignment.main()
    if phone_number[6] != "/" or phone_number[10] != "-" or len(phone_number) < 15:
        print("\nNot valid phone number.")
        sleep(0.5)
        print("\nPlease, use the format 0036xx/xxx-xxxx")
        sleep(1)
        assignment.main()
    if "@" not in email:
        print("\nPlease, try with a valid email.")
        sleep(1)
        assignment.main()
