import os, httpx, json, time


def get_devices():
    base_url = "https://192.168.128.30/api"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": "Token e267a40c876fd36c064e20ade17da6d7bd0cb18c",
    }

    with httpx.Client(
        headers=headers,
        verify=False,
    ) as client:
        r = client.get(url=base_url + "/dcim/devices")

    return r.json()


def filter_devices():
    results = get_devices()["results"]

    my_lst = [
        "",
        "       Hostname | Primary IP",
        "--------------------------------------",
    ]

    for result in results:
        if result["primary_ip"]:
            hostname = result["display_name"]
            ip = result["primary_ip"]["address"]
            my_lst.append(f"{hostname:>15} | {ip:<05}")

    return my_lst