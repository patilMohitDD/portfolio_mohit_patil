import psycopg2
conn = psycopg2.connect(
    host="your_host_name",
    database="your_database_name",
    user="your_username",
    password="your_password"
)







# insert into sudoku(my_array) values
# (
# '{{".", "3", ".", "2", ".", ".", ".", ".", "."},
# {".", ".", ".", ".", "1", ".", ".", ".", "6"},
# {".", ".", ".", ".", ".", ".", ".", ".", "."},
# {".", ".", ".", "7", ".", ".", ".", ".", "5"},
# {".", ".", ".", ".", ".", "2", ".", ".", "."},
# {".", ".", ".", ".", ".", ".", "6", ".", "."},
# {".", ".", ".", ".", ".", ".", ".", ".", "."},
# {"6", ".", ".", ".", ".", ".", ".", ".", "."},
# {".", ".", ".", ".", ".", ".", ".", "4", "."}
# }'
# )