# React Tutorial 202408

# On Debug

## Run Debug Server

```bash
docker compose build
docker compose up -d
```

* front endpoint: `http://localhost:15173`
* back endpoint: `http://localhost:18000`
    * back docs: `http://localhost:18000/docs`

# Initial Setup Project

## Run Docker Compose

At host OS, execute following commands.

```bash
docker compose build
docker compose up -d
```

And enter docker container.

## Setup React Project with Vite

At the container, execute following commands.

```bash
npm create vite
✔ Project name: … front
✔ Select a framework: › React
✔ Select a variant: › TypeScript

cd react-beginner-tutorial
npm install
```

## Config package.json

Run with `--host` option to be able to access host OS.

```
7c7
<     "dev": "vite",
---
>     "dev": "vite --host",
```
