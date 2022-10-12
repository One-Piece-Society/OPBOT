# OPBOT - Another python cogs based discord bot

## Overview

The following is a python based bot designed to help the UNSW OPSOC discord sever generate engagement and allow for members to get additional infomation about the OP universe.

### Considerations

When designing the bot the following was considered.

- Able to be run through a always online server running docker
- Low maintenance
- Low processing power and networking bandwidth

## Features

- [x] Help page with upto date spec
- [x] Random image generator (inc data)
- [x] Bot stats
- [ ] RPG style character collector
- [ ] Search character feature
- [ ] Guess the charcter game
- [ ] User profile
- [ ] Auto reverification tagger

## The Setup

1. If api keys file does not exist create a new file named ```api.key``` and insert the following

    ``` linix
        DiscordAPI-Key = [discord api key]
    ```

2. Start instance of Docker
3. Build script using docker
4. Run script from docker command

## Maintaining functionality

1. Generate python module requirements with

    ``` linix
        pipreqs ./ --force
    ```
