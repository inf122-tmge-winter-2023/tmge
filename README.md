# tmge

## About

This is the executable version of the TMGE required for the final assignment of INF122. It allows for multiplayer matches of the following games

- Columns
- Candy Crush

The TMGE and games themselves are built using the `tilematch_tools` package (created in-house) that provides a set of extensible classes that can be used to build any tile-matching game with relative ease. Candy crush is implemented in the `candy_crush_widget` package and the columns game is implement as `columns_widget` package. Both games are built using tools provided in the `tilematch_tools` package.

## Getting started

### Setting up the environment

After cloning this repository, you will be met with a few configuration files and a couple of directories containint source code. To develop or test the TMGE as smoothly as possible it is recommended to use the provided `Makefile` to streamline the setup of the environment. If you are running a unix machine, congratulations, setup is a simple as 

```bash
$ make bootstrap
$ source .venv/bin/activate
```

For the windows users out there, you will require some additional setup as there is no native way to execute a `Makefile` without additional setup. Instead, you'll want to open up that `Makefile` to see what is going on. Looking at the steps in the `bootstrap` target and you should recognize that it is a pretty standard python virtual environment setup. All you'll have to do is execute the windows version of these commands. The makefile only streamlines the process, it does not actually contribute anything to building or packaging the application.

### Caveats for setup

- Python 3.11 or newer is required. So, what are you doing using that old version of Python?
- This application utilizes `tkinter` for its GUI. On unix machines, it may be installed separately from the actual python installation. Check your package manager for details

### Executing the TMGE

Assuming, you made it this far through the set up, all you need to do is ensure that the virtual environment is created and execute the following command

```bash
$ tmge
```

This command will start the TMGE, and you should see a brand new `tkinter` window on your screen. If the command above does not work, verify the following

- The virtual environment for this project is activated
- You are utilizing Python 3.11 and it is installed properly
- The environment bootstrap process went through without *any* errors
    - If any errors occurs, assume the environment was not set up correctly and start over
    - You can start over by removing `.venv/` directory at the top-level of the project
- The `tkinter` module is available to use. (See caveats for setup above)

## Special thanks to

- [tilematch_tools](https://github.com/inf122-tmge-winter-2023/tile-matching-tools)
- [candy_crush_widget](https://github.com/inf122-tmge-winter-2023/candy-crush-widget)
- [columns_widget](https://github.com/inf122-tmge-winter-2023/columns-widget)

These in-house packages separate the application into managable parts and made this application trivial to implement.

## Contributors

- Nathan Mendoza (nathancm@uci.edu)
