import argparse

from os import getenv
from .client import Client
from .libsodium import encrypt


def build_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--secret-name",
        help="Specifies the friendly name of the new secret",
        required=True,
        type=str,
    )
    parser.add_argument(
        "--secret-string",
        help="Specifies text data that you want to encrypt and store in this new version of the secret",
        required=True,
        type=str,
    )
    parser.add_argument(
        "--organization",
        default=getenv("GITHUB_ORGANIZATION"),
        help="The target GitHub organization",
        type=str,
    )
    parser.add_argument(
        "--token",
        default=getenv("GITHUB_TOKEN"),
        help="The GitHub personal access token",
        type=str,
    )
    return parser.parse_args()


def run():
    args = build_args()
    client = Client(organization=args.organization, token=args.token)
    response = client.get_public_key()
    body = response.json()
    encrypted_value = encrypt(body["key"], args.secret_string)
    client.create_secret(args.secret_name, encrypted_value, body["key_id"])
