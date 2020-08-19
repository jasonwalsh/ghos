# ghos

GitHub Organization Secrets (ghos), provides a simple way to manage [organization secrets](https://docs.github.com/en/actions/configuring-and-managing-workflows/creating-and-storing-encrypted-secrets#creating-encrypted-secrets-for-an-organization) via the CLI.

# Installation

```
git clone https://github.com/jasonwalsh/ghos.git && cd ghos
python setup.py install
```

# Usage

```
ghos \
  --secret-name=DOCKER_USERNAME \
  --secret-string=halifax \
  --organization=moby \
  --token=your_token
```

If you do not wish to specify the GitHub organization and token via the CLI, ghos honors environment variables named `GITHUB_ORGANIZATION` and `GITHUB_TOKEN`, respectively.

```bash
export GITHUB_ORGANIZATION=moby
export GITHUB_TOKEN=your_token

ghos \
  --secret-name=DOCKER_USERNAME \
  --secret-string=halifax
```

# API

```
usage: ghos [-h] --secret-name SECRET_NAME --secret-string SECRET_STRING
            [--organization ORGANIZATION] [--token TOKEN]

optional arguments:
  -h, --help            show this help message and exit
  --secret-name SECRET_NAME
                        Specifies the friendly name of the new secret
  --secret-string SECRET_STRING
                        Specifies text data that you want to encrypt and store
                        in this new version of the secret
  --organization ORGANIZATION
                        The target GitHub organization
  --token TOKEN         The GitHub personal access token
```

# License

[MIT License](LICENSE)
