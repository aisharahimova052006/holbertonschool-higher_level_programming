#!/usr/bin/python3
"""work with jsonplaceholder posts"""
import requests
import csv


def fetch_and_print_posts():
    """get posts and print titles"""
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status Code:", r.status_code)
    if r.status_code == 200:
        posts = r.json()
        for p in posts:
            print(p.get("title"))


def fetch_and_save_posts():
    """get posts and save to csv"""
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    if r.status_code == 200:
        posts = r.json()
        data = [{"id": p.get("id"),
                 "title": p.get("title"),
                 "body": p.get("body")} for p in posts]

        with open("posts.csv", "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(data)

