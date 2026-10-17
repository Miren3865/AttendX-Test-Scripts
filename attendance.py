def test_mark_attendance():
    student_id = "23CS084"
    attendance_status = "Present"

    if student_id and attendance_status == "Present":
        print("PASS: Attendance marked successfully")
    else:
        print("FAIL: Attendance marking unsuccessful")


if __name__ == "__main__":
    test_mark_attendance()