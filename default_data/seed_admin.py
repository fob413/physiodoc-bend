from models import AdminUser


users = [
    {
        'email': 'oluwafunso.oluyole.balogun@gmail.com',
        'password': b'password'
    }
]


def seed_admin_users():
    for user in users:
        user_exists = AdminUser.find_first(**{'email': user['email']})

        if not user_exists:
            new_user = AdminUser(
                email=user['email']
            )

            new_user.set_password(user['password'])

            try:
                new_user.save()
            except:
                pass
