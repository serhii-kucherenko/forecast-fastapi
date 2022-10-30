import requests


def main():

    choice = input("[R]eport weather or [s]ee reports? ")

    while choice:
        if choice.lower() == 'r':
            report_event()
        elif choice.lower() == 's':
            see_reports()
        else:
            print(f"Don't know what to do with {choice}")

        choice = input("[R]eport weather or [s]ee reports?")


def report_event():
    data = {
        "description": input("Whats is going on? "),
        "location": {
            "city": input("What city? "),
            "country": input("What country? "),
        }
    }

    url = "http://localhost:8000/api/reports"
    response = requests.post(url, json=data)
    response.raise_for_status()
    report = response.json()

    print(f"Reported new event: {report.get('description')} in {report.get('location').get('city')}")


def see_reports():
    url = "http://localhost:8000/api/reports"
    response = requests.get(url)
    response.raise_for_status()
    reports = response.json()

    for report in reports:
        print(f"{report.get('location').get('city')} has {report.get('description')}")


if __name__ == '__main__':
    main()