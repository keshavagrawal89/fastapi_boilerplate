from app.db import database


def get_user_profile():
    conn = database.get_connection()
    response = {"profile": "user profile"}
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT NOW()")
        time_now = cursor.fetchone()[0]
        response = {"profile": time_now}
    finally:
        cursor.close()
        database.release_connection(conn)    

    return response

def get_user_subscriptions():
    return {"subscriptions": "user subscriptions"}

def get_public_info():
    return {"info": "public information"}
