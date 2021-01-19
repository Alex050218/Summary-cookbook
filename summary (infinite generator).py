import mysql.connector as db
from time import perf_counter


def inf_data(connexion):
    try:
        cursor_data = connexion.cursor(buffered=True)
        cursor_data.execute(
            """
                SELECT name, trav_date, miles
                FROM driver_log ORDER BY name
            """
        )

        ended = True
        while ended:
            row = cursor_data.fetchone()
            if row:
                yield row
            else:
                ended = False

        cursor_data.close()
    except db.Error as e:
        print(e)


def summary():
    conn = db.connect(
        host="localhost",
        database="cookbook",
        password="rgnqmwzlf589pnzn",
        user="root"
    )

    cursor_emp = conn.cursor(buffered=True)
    cursor_emp.execute(
        """
            SELECT DISTINCT name FROM driver_log
        """
    )

    emp_summary = {"name": None, "date_miles": [], "miles_dr": 0}
    for emp in cursor_emp:
        curr_emp = emp[0]
        emp_summary["name"] = curr_emp

        for row_name, row_date, row_miles in inf_data(conn):
            if curr_emp == row_name:
                emp_summary["date_miles"].append([row_date, row_miles])
                emp_summary["miles_dr"] += row_miles

        print(emp_summary)
        emp_summary["date_miles"] = []
        emp_summary["miles_dr"] = 0


if __name__ == "__main__":
    start = perf_counter()
    summary()
    print(f"Taken time: {perf_counter() - start}")
