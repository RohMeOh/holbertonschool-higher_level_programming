#!/usr/bin/python3
"""Fetch and process data from JSONPlaceholder API"""

import requests
import csv


def fetch_and_print_posts():
    """Fetch posts and print status code and titles"""
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts"
    )

    print("Status Code:", response.status_code)

    if response.status_code == 200:
        posts = response.json()

        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    """Fetch posts and save selected data to CSV"""
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts"
    )

    if response.status_code == 200:
        posts = response.json()

        data = [
            {
                "id": post.get("id"),
                "title": post.get("title"),
                "body": post.get("body")
            }
            for post in posts
        ]

        with open("posts.csv", "w", newline="") as csvfile:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(
                csvfile,
                fieldnames=fieldnames
            )

            writer.writeheader()
            writer.writerows(data)
