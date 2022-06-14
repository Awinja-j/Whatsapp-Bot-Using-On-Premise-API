# Development

This document describes the process for running this application on your local computer.

# Getting started

This project is powered by Docker and Docker Compose.
:sparkles: :turtle: :rocket: :sparkles:

It runs on macOS, Windows, and Linux environments.

1. If not already done, [install Docker Compose](https://docs.docker.com/compose/install/)

2. Fork the repository.

    a. Using GitHub Desktop:
    - [Getting started with GitHub Desktop](https://docs.github.com/en/desktop/installing-and-configuring-github-desktop/overview/getting-started-with-github-desktop) will guide you through setting up Desktop.
    - Once Desktop is set up, you can use it to [fork the repo](https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/adding-and-cloning-repositories/cloning-and-forking-repositories-from-github-desktop)!
    b. Using the command line:
    - [Fork the repo](https://docs.github.com/en/get-started/quickstart/fork-a-repo#fork-an-example-repository) so that you can make your changes without affecting the original project until you're ready to merge them.

3. Clone the repository

```
$ git clone https://github.com/<your-repo-name>/Whatsapp-Bot-Using-On-Premise-API
```

4. Change directory to the repository
```
$ cd Whatsapp-Bot-Using-On-Premise-API
```

5. Install with docker
```
$ docker-compose up -d
```

You should now have a running server! Visit `localhost:5000` in your browser. It will automatically restart as you make changes to site content.

When you're ready to stop your local server, type Ctrl+C in your terminal window.