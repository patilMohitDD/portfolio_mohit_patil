import psycopg2
conn = psycopg2.connect(
    host="your_host_name",
    database="your_database_name",
    user="your_username",
    password="your_password"
)
