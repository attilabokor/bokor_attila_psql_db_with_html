from connect import connect_to_sql




@connect_to_sql
def question_1(cursor):
    data = {'header': [],
            'result_set': []}
    cursor.execute("""SELECT CONCAT(mentors.first_name, ' ', mentors.last_name) AS "Mentor's Name",
                        schools.name AS "School name",
                        schools.country
                        FROM mentors
                        INNER JOIN schools
                        ON mentors.city = schools.city
                        ORDER BY mentors.id ASC;""")
    column_names = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()
    data['header'] = column_names
    data['result_set'] = rows
    return data


@connect_to_sql
def question_2(cursor):
    data = {'header': [],
            'result_set': []}
    cursor.execute("""SELECT CONCAT(mentors.first_name, ' ', mentors.last_name) AS "Mentor's Name",
                        schools.name AS "School name",
                        schools.country
                        FROM mentors
                        RIGHT JOIN schools
                        ON mentors.city = schools.city
                        ORDER BY mentors.id ASC;""")
    column_names = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()
    data['header'] = column_names
    data['result_set'] = rows
    return data




@connect_to_sql
def question_3(cursor):
    data = {'header': [],
            'result_set': []}
    cursor.execute("""SELECT country AS "Country", count(mentors.id) AS "Number of Mentors"
                      FROM mentors
                      FULL OUTER JOIN schools
                      ON mentors.city = schools.city
                      GROUP BY country
                      ORDER BY country ASC;""")
    column_names = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()
    data['header'] = column_names
    data['result_set'] = rows
    return data


@connect_to_sql
def question_4(cursor):
    data = {'header': [],
            'result_set': []}
    cursor.execute("""SELECT schools.name AS "School Name",
                      CONCAT (mentors.first_name, ' ', mentors.last_name) AS "Contact Mentor's Name"
                      FROM mentors
                      INNER JOIN schools
                      ON mentors.id = schools.contact_person
                      ORDER BY schools.name ASC;
                      """)
    column_names = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()
    data['header'] = column_names
    data['result_set'] = rows
    return data


@connect_to_sql
def question_5(cursor):
    data = {'header': [],
            'result_set': []}
    cursor.execute("""SELECT applicants.first_name AS "Applicant's First Name",
                             applicants.application_code AS "Application Code",
                             applicants_mentors.creation_date AS "Creation Date"
                             FROM applicants
                             INNER JOIN applicants_mentors
                             ON applicants.id = applicants_mentors.applicant_id
                             WHERE applicants_mentors.creation_date >= '2016-01-01'
                             ORDER BY creation_date DESC;
                             """)
    column_names = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()
    data['header'] = column_names
    data['result_set'] = rows
    return data


@connect_to_sql
def question_6(cursor):
    data = {'header': [],
            'result_set': []}            
    cursor.execute("""SELECT applicants.first_name AS "Applicant's First Name",
                             applicants.application_code AS "Application Code",
                             CONCAT (mentors.first_name, ' ', mentors.last_name) AS "Name of the assigned Mentor"
                             FROM applicants
                             FULL OUTER JOIN applicants_mentors
                             ON applicants.id = applicants_mentors.applicant_id
                             LEFT JOIN mentors
                             ON applicants_mentors.mentor_id = mentors.id;
                             """)        
    column_names = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()
    data['header'] = column_names
    data['result_set'] = rows
    return data