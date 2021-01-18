# Pummaruola
A discord simple yet useful pomodoro timer

<img src="static/tomato.png" width="50">

## Usage

### Self-hosted

First install dependencies wit pip:

```
pip install -r requirements.txt
```

then add your token inside the `config.toml` file:

```toml
token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

once done, launch the bot:

```
python pummaruola.py
```

## Commands

* `!pummaruola -h` displays a list of commands
* `!pummaruola --help` displays a list of commands
* `!pummaruola` starts a default 5 minutes pomodoro timer
* `!pummaruola X` starts a custom pomodoro timer where X = seconds

## Output

Once the timer is finished, Pummaruola will send you a private message:

<img src="static/pummaruola_pvt.png" width="80%">

Also, when invoking `-h` or `--help` the bot will reply with a list of commands in the same channel you invoked it:

<img src="static/commands.png" width="80%">