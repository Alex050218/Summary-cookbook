import mysql.connector as db


def summary(conn):
    cursor_data = conn.cursor(buffered=True)
    cursor_emp = conn.cursor(dictionary=True, buffered=True)

    cursor_emp.execute("SELECT DISTINCT name FROM driver_log")

    emp_summary = {"name": None, "date_miles": [], "miles": 0}
    query_data = "SELECT name, trav_date, miles FROM driver_log WHERE name = '%s'"

    for emp in cursor_emp:
        emp_summary["name"] = emp["name"]
        cursor_data.execute(query_data % emp["name"])

        for name, trav_date, miles in cursor_data:
            if name == emp_summary["name"]:
                emp_summary["date_miles"].append([trav_date, miles])
                emp_summary["miles"] += miles

        yield emp_summary
        emp_summary["date_miles"] = []
        emp_summary["miles"] = 0

    cursor_data.close()
    cursor_emp.close()


if __name__ == "__main__":
    # Add your parameters
    con = db.connect()
    cursor_amount = con.cursor(buffered=True, dictionary=True)
    cursor_amount.execute("SELECT SUM(miles) as miles FROM driver_log")

    total_miles = cursor_amount.fetchone()
    print(f"Total miles driven by all employees {total_miles['miles']} \n")

    for emp in summary(con):
        print(
            f"Name: {emp['name']}, days on road: {len(emp['date_miles'])}, "
            f"miles driven: {emp['miles']}"
        )

        for road_day in emp["date_miles"]:
            print(f"{'' * 3} date: {road_day[0]}, driven miles: {road_day[1]}")

    con.close()
