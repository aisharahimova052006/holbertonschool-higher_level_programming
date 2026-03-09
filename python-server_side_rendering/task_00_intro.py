#!/usr/bin/python3
def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Invalid input: template must be a string.")
        return

    if not isinstance(attendees, list) or \
       not all(isinstance(a, dict) for a in attendees):
        print("Invalid input: attendees must be a list of dictionaries.")
        return

    if template == "":
        print("Template is empty, no output files generated.")
        return

    if attendees == []:
        print("No data provided, no output files generated.")
        return

    keys = ["name", "event_title", "event_date", "event_location"]

    for i, attendee in enumerate(attendees, 1):
        content = template
        for k in keys:
            v = attendee.get(k)
            if v is None:
                v = "N/A"
            content = content.replace("{" + k + "}", str(v))

        with open(f"output_{i}.txt", "w", encoding="utf-8") as f:
            f.write(content)

