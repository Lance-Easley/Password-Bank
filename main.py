import encoder
import json

def save() -> None:
    """Saves information to data.json and key.json
    """
    with open('key.json', 'w') as file:
        json.dump(key_list, file, indent=4)
    with open('data.json', 'w') as file:
        json.dump(data_list, file, indent=4)

with open('key.json') as file:
    key_list = json.load(file)
with open('data.json') as file:
    data_list = json.load(file)

print('Welcome to your Password Bank')
while True:
    choice = input('Would you like to view or add any login credentials? [V/A] ')
    if choice:
        if choice == 'a':
            application = input('What Application? ').strip()
            # Check if application name exists in data.json
            index = 0
            cancel = False
            for data, key in zip(data_list, key_list):
                check = encoder.decode(data[0], key[0])
                if application.lower() == check.lower():
                    print('There is already information for that application.')
                    overwrite = input('Would you like to change the saved information? [Y/N] ').lower()
                    if overwrite == 'y':
                        data_list.pop(index)
                        key_list.pop(index)
                        break
                    else:
                        cancel = True
                else:
                    index += 1
            if not cancel:
                username = input('Username: ')
                email = input('Email: ')
                password = input('Password: ')
                confirm = input('Do you want to save this information? [Y/N] ').lower()
                if confirm == 'y':
                    # Encrypt information
                    d_application, k_application = encoder.encode(application)
                    d_username, k_username = encoder.encode(username)
                    d_email, k_email = encoder.encode(email)
                    d_password, k_password = encoder.encode(password)
                    # Store encrypted data and key
                    data_list.append([d_application, d_username, d_email, d_password])
                    key_list.append([k_application, k_username, k_email, k_password])
                    save()

        elif choice == 'v':
            if data_list and key_list:
                for data, key in zip(data_list, key_list):
                    v_app = encoder.decode(data[0], key[0])
                    v_name = encoder.decode(data[1], key[1])
                    v_mail = encoder.decode(data[2], key[2])
                    v_pass = encoder.decode(data[3], key[3])
                    print(f"""
    Application: {v_app}
        - Username: {v_name}
        - Email: {v_mail}
        - Password: {v_pass}""")
            else:
                print('There is no information saved')