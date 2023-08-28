import yaml
import psycopg2


def extract(userProfile):
    dbCredentials = userProfile['postgres']
    conn = psycopg2.connect(
        f"dbname={dbCredentials['database']} user={dbCredentials['username']} password={dbCredentials['password']}")
    return conn


def debugTransform(cursor, query):
    cursor.execute(query)
    rows = cursor.fetchall()
    print(rows)


def transform(connection, UserFile):
    cursor = connection.cursor()

    resQueries = {}
    for taskName, task in UserFile["transform"].items():
        combinedQuery = ""
        for step, query in task.items():
            combinedQuery += query + " "
            debugTransform(cursor, combinedQuery)
        resQueries[taskName] = combinedQuery
    return resQueries

def load(connection, resQueries, userFile):
    loadConfigs = userFile['load']

    cursor = connection.cursor()
    for queryName, query in resQueries.items():
        copySql = f"COPY ({query}) TO STDOUT WITH CSV HEADER DELIMITER ','"
        with open(f"{loadConfigs[queryName]['fileName']}.{loadConfigs[queryName]['format']}", "w") as file:
            cursor.copy_expert(copySql, file)


def getUserFile(userFileName):
    with open(userFileName, 'r') as file:
        userFile = yaml.safe_load(file)
    return userFile


def getUserProfile():
    with open('profiles/profiles.yaml', 'r') as file:
        userProfile = yaml.safe_load(file)
    return userProfile


def runCommand(userFileName):
    UserFile = getUserFile(userFileName)
    UserProfile = getUserProfile()

    connection = extract(UserProfile)
    resQueries = transform(connection, UserFile)
    load(connection, resQueries, UserFile)