import mysql.connector
import hashlib

conn = mysql.connector.connect(
    host="localhost",
    database="todo_db",
    user="root",
    password=""
)
cursor = conn.cursor()


def add_task(id_no, task, tag="active"):
    sql_check = "SELECT * FROM todo WHERE id = %s AND task = %s"
    val_check = (id_no, task)
    cursor.execute(sql_check, val_check)
    if cursor.fetchone():
        return "Task already exists"
    else:
        sql = "INSERT INTO todo (id, task, tag) VALUES (%s, %s, %s)"
        val = (id_no, task, tag)
        cursor.execute(sql, val)
        conn.commit()
        return cursor.rowcount == 1


def remove_task(id_no, task):
    sql = "DELETE FROM todo WHERE id = %s AND task = %s"
    val = (id_no, task)
    cursor.execute(sql, val)
    conn.commit()
    return cursor.rowcount > 0


def view_tasks(id_no, tag='active'):
    sql = "SELECT task FROM todo WHERE id = %s AND tag = %s"
    val = (id_no, tag)
    cursor.execute(sql, val)
    result = ""
    for row in cursor.fetchall():
        result += row[0] + ", "
    return result[:-2]


def view_completed_tasks(id_no, tag='completed'):
    sql = "SELECT task FROM todo WHERE id = %s AND tag = %s"
    val = (id_no, tag)
    cursor.execute(sql, val)
    result = ""
    for row in cursor.fetchall():
        result += row[0] + ", "
    return result[:-2]


def complete_task(id_no, task):
    task_ = '\u0336'.join(task) + '\u0336'
    sql = "UPDATE todo SET tag = 'completed', task = %s WHERE id = %s AND task = %s"
    val = (task_, id_no, task)
    cursor.execute(sql, val)
    conn.commit()
    return cursor.rowcount == 1


def signup(name, surname, email, password):
    sql_control = "SELECT email FROM login WHERE email = %s"
    val_control = (email,)
    cursor.execute(sql_control, val_control)
    result = cursor.fetchone()
    if result:
        return False
    else:
        password_bytes = password.encode("utf-8")
        hash256 = hashlib.sha256(password_bytes)
        password_hash = hash256.hexdigest()
        sql = "INSERT INTO login (name, surname, email, password) VALUES (%s, %s, %s, %s)"
        val = (name, surname, email, password_hash)
        cursor.execute(sql, val)
        conn.commit()
        return cursor.rowcount == 1


def signin(email, password):
    password_bytes = password.encode("utf-8")
    hash256 = hashlib.sha256(password_bytes)
    password_hash = hash256.hexdigest()
    sql = "SELECT id, name, surname FROM login WHERE email = %s AND password = %s"
    val = (email, password_hash)
    cursor.execute(sql, val)
    result = cursor.fetchone()
    if result:
        return result
    else:
        return False


def change_password(id_no, old_password, new_password):
    password_bytes_old = old_password.encode('utf-8')
    hash256_old = hashlib.sha256(password_bytes_old)
    old_password_hash = hash256_old.hexdigest()
    password_bytes_new = new_password.encode('utf-8')
    hash256_new = hashlib.sha256(password_bytes_new)
    new_password_hash = hash256_new.hexdigest()
    sql = "UPDATE login SET password = %s WHERE id = %s AND password = %s"
    val = (new_password_hash, id_no, old_password_hash)
    cursor.execute(sql, val)
    conn.commit()
    return cursor.rowcount == 1


def change_email(id_no, old_email, new_email):
    sql = "UPDATE login SET email = %s WHERE id = %s AND email = %s"
    val = (new_email, id_no, old_email)
    cursor.execute(sql, val)
    conn.commit()
    return cursor.rowcount == 1


def get_id_no(email):
    sql = "SELECT id FROM login WHERE email = %s"
    val = (email,)
    cursor.execute(sql, val)
    result = cursor.fetchone()
    if result:
        return result


def get_name_surname(email):
    sql = "SELECT name, surname FROM login WHERE email = %s"
    val = (email,)
    cursor.execute(sql, val)
    result = ''
    for row in cursor.fetchall():
        result += row[0] + ' '
        result += row[1]
    return result.upper()
