# common fixtures

user_fixture = {
    "username": "User0",
    "first_name": "Us",
    "last_name": "Er",
    "password": "pass",
}

user_fixture1 = {
    "username": "User1",
    "first_name": "Us",
    "last_name": "Er",
    "password": "pass",
}
user_fixture2 = {
    "username": "User2",
    "first_name": "Usir",
    "last_name": "Erus",
    "password": "pass",
}


default_task_fixture = {"id": 1, "name": "Default_Task"}
default_status_fixture = {"id": 1, "name": "Default_Status"}


# labels fixtures

labels_urls_data = (
    {
        "viewname": "labels_index",
    },
    {
        "viewname": "labels_create",
    },
    {"viewname": "labels_update", "kwargs": {"pk": "1"}},
    {"viewname": "labels_delete", "kwargs": {"pk": "1"}},
)
default_label_fixture = {"id": 1, "name": "Default_Task"}
default_label_fixture = {"id": 1, "name": "Default_Label"}

# default label must be created in TestsLabels.setUp;
valid_labels = (
    # id 1 is reserved for default label
    {"pk": 2, "name": "Do something"},
    {"pk": 3, "name": "Do something else"},
    {"pk": 4, "name": "Do nothing"},
    {"pk": 5, "name": "Do thing"},
    {"pk": 6, "name": "Do anything"},
    {"pk": 7, "name": "Do everything"},
)
new_valid_labels = (
    {"pk": 2, "name": "1Do something"},
    {"pk": 3, "name": "1Do something else"},
    {"pk": 4, "name": "1Do nothing"},
    {"pk": 5, "name": "1Do thing"},
    {"pk": 6, "name": "1Do anything"},
    {"pk": 7, "name": "1Do everything"},
)
invalid_labels = (
    {
        "name": """too long label name too long label name too long label
        name too long label name too long label too loong too long""",
    },
)

# statuses fixtures

statuses_urls_data = (
    {
        "viewname": "statuses_index",
    },
    {
        "viewname": "statuses_create",
    },
    {"viewname": "statuses_update", "kwargs": {"pk": "1"}},
    {"viewname": "statuses_delete", "kwargs": {"pk": "1"}},
)
default_status_fixture = {"id": 1, "name": "Default"}

# default status must be created in TestsStatuses.setUp;
valid_statuses = (
    # id 1 is reserved for default status
    {"pk": 2, "name": "Status"},
    {"pk": 3, "name": "On delay"},
    {"pk": 4, "name": "Stopped"},
    {"pk": 5, "name": "In work"},
    {"pk": 6, "name": "In test"},
    {"pk": 7, "name": "Preparing"},
)
new_valid_statuses = (
    {"pk": 2, "name": "1Status"},
    {"pk": 3, "name": "1On delay"},
    {"pk": 4, "name": "1Stopped"},
    {"pk": 5, "name": "1In work"},
    {"pk": 6, "name": "1In test"},
    {"pk": 7, "name": "1Preparing"},
)
invalid_statuses = [
    {
        "name": """too long status name too long status name too long status
        name too long status name too long status""",
    }
]


# tasks fixtures

tasks_urls_data = (
    {
        "viewname": "tasks_index",
    },
    {
        "viewname": "tasks_create",
    },
    {"viewname": "tasks_update", "kwargs": {"pk": "1"}},
    {"viewname": "tasks_delete", "kwargs": {"pk": "1"}},
)

# default task must be created in TestsStatuses.setUp;
valid_tasks = (
    # id 1 is reserved for default task
    {"pk": 2, "name": "Do something"},
    {"pk": 3, "name": "Do something else"},
    {"pk": 4, "name": "Do nothing"},
    {"pk": 5, "name": "Do thing"},
    {"pk": 6, "name": "Do anything"},
    {"pk": 7, "name": "Do everything"},
)
new_valid_tasks = (
    {"pk": 2, "name": "1Do something"},
    {"pk": 3, "name": "1Do something else"},
    {"pk": 4, "name": "1Do nothing"},
    {"pk": 5, "name": "1Do thing"},
    {"pk": 6, "name": "1Do anything"},
    {"pk": 7, "name": "1Do everything"},
)
invalid_tasks = (
    {
        "name": """too long task name too long task name too long task
        name too long task name too long task too loong too long""",
    },
)


# users fixtures

valid_users = (
    {
        "pk": 1,
        "username": "Alex",
        "password1": "123",
        "password2": "123",
        "first_name": "Alex",
        "last_name": "Andreas",
    },
    {
        "pk": 2,
        "username": "HarryPotter",
        "password1": "3312",
        "password2": "3312",
        "first_name": "Harry",
        "last_name": "Potter",
    },
    {
        "pk": 3,
        "username": "Max1",
        "password1": "mmaxxx2_1",
        "password2": "mmaxxx2_1",
        "first_name": "Max",
        "last_name": "Smart",
    },
)


# extend list of valid users to use it with invalid_users in some tests
extended_valid_users = valid_users * 4


invalid_users = (
    {
        "pk": 1,
        "username": "!drakula",
        "new_password1": "333",
        "new_password2": "333",
        "first_name": "Harry",
        "last_name": "Potter",
    },
    {
        "pk": 2,
        "username": """111111111111111111111111111111111111111111111111111
        111111111111111111111111111111111111111111111111111111111111111111
        111111111111111111111111111111111111111111111111111111111111111111
        11111111111111111111111111111111111111111111111111111111111111""",
        "new_password1": "333",
        "new_password2": "333",
        "first_name": "Harry",
        "last_name": "Potter",
    },
    {
        "pk": 3,
        "username": "",
        "new_password1": "333",
        "new_password2": "333",
        "first_name": "Harry",
        "last_name": "Potter",
    },
    {
        "pk": 4,
        "username": "aaa",
        "new_password1": "33",
        "new_password2": "33",
        "first_name": "Harry",
        "last_name": "Potter",
    },
    {
        "pk": 5,
        "username": "aaa",
        "new_password1": "33",
        "new_password2": "333",
        "first_name": "Harry",
        "last_name": "Potter",
    },
    {
        "pk": 6,
        "username": "aaa",
        "new_password1": "333",
        "new_password2": "33",
        "first_name": "Harry",
        "last_name": "Potter",
    },
    {
        "pk": 7,
        "username": "aaa",
        "new_password1": "333",
        "new_password2": "3333",
        "first_name": "Harry",
        "last_name": "Potter",
    },
    {
        "pk": 8,
        "username": "aaa",
        "new_password1": "3333",
        "new_password2": "333",
        "first_name": "Harry",
        "last_name": "Potter",
    },
    {
        "pk": 9,
        "username": "aaa",
        "new_password1": "3333",
        "new_password2": "333",
        "first_name": "Harry",
        "last_name": "",
    },
    {
        "pk": 10,
        "username": "aaa",
        "new_password1": "3333",
        "new_password2": "333",
        "first_name": "",
        "last_name": "Potter",
    },
    {
        "pk": 11,
        "username": "aaa",
        "new_password1": "3333",
        "new_password2": "333",
        "first_name": "",
        "last_name": "",
    },
)

other_user_data = {
    "username": "Autobot",
    "first_name": "Prime",
    "last_name": "Optimus",
    "password1": "password",
    "password2": "password",
}
